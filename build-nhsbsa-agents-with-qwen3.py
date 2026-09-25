#!/usr/bin/env python3

"""
NHSBSA Digital Playbook -> Agent Knowledge Pack

Pipeline:

    NHSBSA Playbook
          |
          v
    Recursive crawler
          |
          v
    Source extraction
          |
          v
    Topic/skill grouping
          |
          v
    Local LLM via Ollama
          |
          v
    Detailed SKILL.md files
          |
          v
    Validation
          |
          v
    AGENTS.md + SOURCES.md + VERSION.md
          |
          v
    ZIP archive

Requirements:

    Python 3.10+
    requests
    beautifulsoup4

Install:

    python3 -m pip install requests beautifulsoup4

Ollama:

    https://ollama.com/

Example:

    ollama pull qwen3:14b

Run:

    python3 build-nhsbsa-agents.py

Useful options:

    --model qwen3:14b
    --max-pages 300
    --output ./output
    --force
    --no-llm
"""


from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import time
import zipfile

from collections import defaultdict, deque
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup


# ============================================================================
# Configuration
# ============================================================================

ROOT_URL = (
    "https://nhsbsa.github.io/"
    "nhsbsa-digital-playbook/development/"
)

PLAYBOOK_ROOT = (
    "https://nhsbsa.github.io/"
    "nhsbsa-digital-playbook/"
)

HOST = "nhsbsa.github.io"

OLLAMA_URL = os.environ.get(
    "OLLAMA_URL",
    "http://localhost:11434",
)

DEFAULT_MODEL = os.environ.get(
    "NHSBSA_AGENT_MODEL",
    "qwen3:14b",
)

DEFAULT_MAX_PAGES = 300

REQUEST_TIMEOUT = 30

CRAWL_DELAY = 0.25

OLLAMA_TIMEOUT = 600

USER_AGENT = (
    "NHSBSA-Playbook-Agent-Knowledge-Builder/1.0 "
    "(documentation crawler)"
)


# ============================================================================
# Skill definitions
# ============================================================================

SKILL_DEFINITIONS = {
    "coding": {
        "title": "Coding",
        "keywords": [
            "coding",
            "clean code",
            "solid",
            "dry",
            "kiss",
            "12 factor",
        ],
    },
    "style-guides": {
        "title": "Style Guides",
        "keywords": [
            "style guide",
            "coding style",
            "formatting",
        ],
    },
    "licensing": {
        "title": "Licensing",
        "keywords": [
            "licence",
            "license",
            "apache",
            "open government licence",
            "ogl",
        ],
    },
    "naming-conventions": {
        "title": "Naming Conventions",
        "keywords": [
            "naming convention",
            "naming",
            "camelcase",
            "kebab",
            "snake case",
        ],
    },
    "logging": {
        "title": "Logging",
        "keywords": [
            "logging",
            "logs",
            "monitoring",
            "audit",
            "profiling",
        ],
    },
    "secure-development": {
        "title": "Secure Development",
        "keywords": [
            "secure development",
            "secure coding",
            "owasp",
            "ncsc",
            "security",
        ],
    },
    "personal-data": {
        "title": "Personal Data",
        "keywords": [
            "personal data",
            "personal information",
            "pii",
            "data protection",
        ],
    },
    "secrets-detection": {
        "title": "Secrets Detection",
        "keywords": [
            "secrets detection",
            "secret detection",
            "gitleaks",
            "secrets",
            "credentials",
        ],
    },
    "git-history-rewrite": {
        "title": "Git History Rewriting",
        "keywords": [
            "rewrite history",
            "git history",
            "filter-repo",
            "history rewrite",
        ],
    },
    "security-headers": {
        "title": "Security Headers",
        "keywords": [
            "security headers",
            "http headers",
            "headers",
        ],
    },
    "content-security-policy": {
        "title": "Content Security Policy",
        "keywords": [
            "content security policy",
            "csp",
        ],
    },
    "testing": {
        "title": "Testing",
        "keywords": [
            "testing",
            "unit test",
            "integration test",
            "test driven",
            "tdd",
        ],
    },
    "static-analysis": {
        "title": "Static Analysis and Quality Assurance",
        "keywords": [
            "sonarqube",
            "static analysis",
            "quality assurance",
            "quality gate",
            "code quality",
        ],
    },
    "peer-review": {
        "title": "Peer Review",
        "keywords": [
            "peer review",
            "merge request",
            "pull request",
            "code review",
        ],
    },
    "git": {
        "title": "Git",
        "keywords": [
            "git",
            "branch",
            "branching",
            "main branch",
        ],
    },
    "apis": {
        "title": "APIs",
        "keywords": [
            "api",
            "rest",
            "application programming interface",
        ],
    },
    "frontends": {
        "title": "Frontend Development",
        "keywords": [
            "frontend",
            "front end",
            "accessibility",
            "design system",
        ],
    },
    "repository-files": {
        "title": "Repository Files",
        "keywords": [
            "repository files",
            "code of conduct",
            "contributing",
            "security.md",
            "secrets.md",
        ],
    },
    "readmes": {
        "title": "README Documentation",
        "keywords": [
            "readme",
        ],
    },
    "patching": {
        "title": "Patching and Dependencies",
        "keywords": [
            "patching",
            "dependency",
            "dependencies",
            "vulnerability",
            "package manager",
        ],
    },
    "release-adoption": {
        "title": "Release Adoption",
        "keywords": [
            "release adoption",
            "adoption schedule",
            "pending",
            "assess",
            "adopt",
            "deprecate",
            "decommission",
        ],
    },
    "technologies": {
        "title": "Technology Landscape",
        "keywords": [
            "technologies",
            "technology landscape",
            "technology",
        ],
    },
    "java": {
        "title": "Java",
        "keywords": [
            "java",
            "spring boot",
            "spring mvc",
            "maven",
        ],
    },
    "nodejs": {
        "title": "Node.js",
        "keywords": [
            "node.js",
            "nodejs",
            "npm",
            "nvm",
        ],
    },
}


# Explicit URL mappings take precedence over keyword matching.

URL_SKILL_MAP = {
    "coding-securely": "secure-development",
    "coding-securely-personal-data": "personal-data",
    "coding-secrets-detection": "secrets-detection",
    "coding-git-rewrite-history": "git-history-rewrite",
    "security-headers": "security-headers",
    "content-security-policy": "content-security-policy",
    "coding-style-guide": "style-guides",
    "coding-licences": "licensing",
    "coding-naming-conventions": "naming-conventions",
    "coding-logging": "logging",
    "dev-tests": "testing",
    "coding-quality-assurance": "static-analysis",
    "coding-peer-review": "peer-review",
    "dev-git": "git",
    "coding-apis": "apis",
    "coding-frontend": "frontends",
    "dev-documentation-readme": "readmes",
    "dev-documentation": "repository-files",
    "tech-patching": "patching",
    "tech-release-adoption-schedule": "release-adoption",
    "tech-java": "java",
    "tech-node": "nodejs",
    "technologies": "technologies",
}


RELATED_SKILLS = {
    "coding": [
        "style-guides",
        "naming-conventions",
        "testing",
        "secure-development",
        "peer-review",
    ],
    "secure-development": [
        "personal-data",
        "secrets-detection",
        "logging",
        "testing",
        "peer-review",
        "security-headers",
        "content-security-policy",
    ],
    "personal-data": [
        "secure-development",
        "logging",
        "testing",
    ],
    "secrets-detection": [
        "secure-development",
        "git",
        "git-history-rewrite",
    ],
    "git-history-rewrite": [
        "git",
        "secrets-detection",
    ],
    "testing": [
        "coding",
        "static-analysis",
        "peer-review",
    ],
    "static-analysis": [
        "testing",
        "peer-review",
    ],
    "peer-review": [
        "git",
        "testing",
        "static-analysis",
    ],
    "git": [
        "peer-review",
        "git-history-rewrite",
    ],
    "apis": [
        "coding",
        "secure-development",
        "testing",
    ],
    "frontends": [
        "coding",
        "secure-development",
        "security-headers",
        "content-security-policy",
        "testing",
    ],
    "patching": [
        "release-adoption",
        "technologies",
        "secure-development",
    ],
    "release-adoption": [
        "patching",
        "technologies",
    ],
    "java": [
        "coding",
        "style-guides",
        "patching",
        "release-adoption",
        "testing",
    ],
    "nodejs": [
        "coding",
        "style-guides",
        "patching",
        "release-adoption",
        "testing",
    ],
}


# ============================================================================
# Data model
# ============================================================================

@dataclass
class Page:
    url: str
    title: str
    headings: list[str]
    content: str
    links: list[str]
    raw_markdown: str = ""


# ============================================================================
# HTTP
# ============================================================================

session = requests.Session()

session.headers.update(
    {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml",
    }
)


def fetch(url: str) -> str:
    response = session.get(
        url,
        timeout=REQUEST_TIMEOUT,
    )

    response.raise_for_status()

    content_type = response.headers.get(
        "content-type",
        "",
    ).lower()

    if "html" not in content_type:
        raise RuntimeError(
            f"Expected HTML but received {content_type}"
        )

    return response.text


# ============================================================================
# URL utilities
# ============================================================================

def normalise_url(url: str) -> str | None:
    url, _ = urldefrag(url)

    parsed = urlparse(url)

    if parsed.scheme not in {"http", "https"}:
        return None

    if parsed.netloc != HOST:
        return None

    if not parsed.path.startswith(
        "/nhsbsa-digital-playbook/"
    ):
        return None

    ignored_extensions = {
        ".pdf",
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".svg",
        ".webp",
        ".zip",
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
    }

    lower_path = parsed.path.lower()

    if any(
        lower_path.endswith(extension)
        for extension in ignored_extensions
    ):
        return None

    path = parsed.path

    if not path.endswith("/"):
        path += "/"

    return f"https://{HOST}{path}"


# ============================================================================
# HTML parsing
# ============================================================================

def clean(value: str) -> str:
    value = re.sub(
        r"\s+",
        " ",
        value,
    )

    return value.strip()


def html_to_markdownish(soup: BeautifulSoup) -> str:
    """
    Produce a useful structured representation for the LLM.

    This deliberately preserves headings, paragraphs, lists, tables and
    code blocks rather than reducing everything to plain text.
    """

    root = (
        soup.find("main")
        or soup.find("article")
        or soup.body
        or soup
    )

    chunks: list[str] = []

    for element in root.find_all(
        [
            "h1",
            "h2",
            "h3",
            "h4",
            "p",
            "li",
            "pre",
            "blockquote",
            "table",
        ]
    ):

        if element.name == "table":
            rows = []

            for tr in element.find_all("tr"):
                cells = [
                    clean(
                        cell.get_text(
                            " ",
                            strip=True,
                        )
                    )
                    for cell in tr.find_all(
                        ["th", "td"]
                    )
                ]

                if cells:
                    rows.append(
                        " | ".join(cells)
                    )

            if rows:
                chunks.append(
                    "\n".join(rows)
                )

            continue

        if element.name == "pre":
            text = element.get_text(
                "\n",
                strip=True,
            )

            if text:
                chunks.append(
                    "```text\n"
                    + text
                    + "\n```"
                )

            continue

        text = clean(
            element.get_text(
                " ",
                strip=True,
            )
        )

        if not text:
            continue

        if element.name.startswith("h"):
            level = int(
                element.name[1]
            )

            chunks.append(
                f"{'#' * level} {text}"
            )

        elif element.name == "li":
            chunks.append(
                f"- {text}"
            )

        elif element.name == "blockquote":
            chunks.append(
                f"> {text}"
            )

        else:
            chunks.append(text)

    return "\n\n".join(chunks)


def parse_page(
    url: str,
    html: str,
) -> Page:

    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    for element in soup(
        [
            "script",
            "style",
            "noscript",
            "svg",
        ]
    ):
        element.decompose()

    title = ""

    if soup.title:
        title = clean(
            soup.title.get_text(
                " ",
                strip=True,
            )
        )

    headings = []

    for heading in soup.find_all(
        ["h1", "h2", "h3", "h4"]
    ):
        value = clean(
            heading.get_text(
                " ",
                strip=True,
            )
        )

        if value:
            headings.append(value)

    links = []

    for anchor in soup.find_all(
        "a",
        href=True,
    ):
        target = urljoin(
            url,
            anchor["href"],
        )

        target = normalise_url(target)

        if target:
            links.append(target)

    links = list(
        dict.fromkeys(links)
    )

    content = html_to_markdownish(
        soup
    )

    return Page(
        url=url,
        title=title,
        headings=list(
            dict.fromkeys(headings)
        ),
        content=content,
        links=links,
    )


# ============================================================================
# Crawler
# ============================================================================

def crawl(
    start_url: str,
    max_pages: int,
) -> list[Page]:

    queue = deque(
        [normalise_url(start_url)]
    )

    visited: set[str] = set()

    pages: list[Page] = []

    print()
    print("Crawling NHSBSA Playbook")
    print("========================")
    print(start_url)
    print()

    while queue and len(pages) < max_pages:

        url = queue.popleft()

        if not url:
            continue

        if url in visited:
            continue

        visited.add(url)

        print(
            f"[{len(pages) + 1:03d}] {url}"
        )

        try:
            html = fetch(url)

            page = parse_page(
                url,
                html,
            )

            pages.append(page)

            for link in page.links:

                if link not in visited:
                    queue.append(link)

        except Exception as exc:
            print(
                f"      ERROR: {exc}"
            )

        time.sleep(
            CRAWL_DELAY
        )

    print()
    print(
        f"Crawl complete: {len(pages)} pages"
    )

    return pages


# ============================================================================
# Skill classification
# ============================================================================

def classify_page(
    page: Page,
) -> str | None:

    path = urlparse(
        page.url
    ).path.lower()

    for fragment, skill in URL_SKILL_MAP.items():

        if fragment in path:
            return skill

    searchable = (
        page.title
        + " "
        + " ".join(page.headings)
        + " "
        + page.content[:5000]
    ).lower()

    best_skill = None
    best_score = 0

    for skill, definition in (
        SKILL_DEFINITIONS.items()
    ):

        score = 0

        for keyword in definition[
            "keywords"
        ]:

            if keyword in searchable:
                score += 1

        if score > best_score:
            best_score = score
            best_skill = skill

    if best_score == 0:
        return None

    return best_skill


def group_pages(
    pages: list[Page],
) -> dict[str, list[Page]]:

    grouped = defaultdict(list)

    for page in pages:

        skill = classify_page(
            page
        )

        if skill:
            grouped[skill].append(
                page
            )

    return dict(grouped)


# ============================================================================
# Ollama
# ============================================================================

def ollama_request(
    model: str,
    prompt: str,
) -> str:

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_ctx": 32768,
        },
    }

    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json=payload,
        timeout=OLLAMA_TIMEOUT,
    )

    response.raise_for_status()

    data = response.json()

    result = data.get(
        "response",
        "",
    )

    if not result.strip():
        raise RuntimeError(
            "Ollama returned an empty response"
        )

    return result.strip()


def check_ollama(
    model: str,
) -> None:

    try:
        response = requests.get(
            f"{OLLAMA_URL}/api/tags",
            timeout=10,
        )

        response.raise_for_status()

    except Exception as exc:

        raise RuntimeError(
            "\nOllama is not available.\n\n"
            "Start Ollama and try again.\n\n"
            "Example:\n"
            "    ollama serve\n\n"
            f"Configured URL: {OLLAMA_URL}\n"
        ) from exc

    models = response.json().get(
        "models",
        [],
    )

    available = [
        item.get("name", "")
        for item in models
    ]

    if model not in available:

        raise RuntimeError(
            f"\nOllama model '{model}' is not installed.\n\n"
            f"Install it with:\n"
            f"    ollama pull {model}\n\n"
            "Available models:\n"
            + "\n".join(
                f"    {name}"
                for name in available
            )
        )


# ============================================================================
# LLM prompts
# ============================================================================

SYSTEM_INSTRUCTIONS = r"""
You are producing engineering guidance for AI coding agents based ONLY on
authoritative NHS Business Services Authority (NHSBSA) Digital, Data and
Technology Playbook source material supplied to you.

Your job is NOT to write a generic software-engineering article.

Your job is to transform the supplied NHSBSA source material into a detailed,
operational skill that an AI coding agent can actually follow.

SOURCE FIDELITY RULES

1. Do not invent NHSBSA requirements.
2. Do not invent thresholds, approval processes, tools, versions, deadlines,
   exceptions or organisational policies.
3. Preserve exact numerical requirements.
4. Preserve named tools where the source specifies them.
5. Preserve explicit exceptions.
6. Preserve mandatory approval requirements.
7. Distinguish:
   - MUST / REQUIRED
   - SHOULD / RECOMMENDED
   - MAY / OPTIONAL
8. If the source is ambiguous, explicitly say that it is ambiguous.
9. If the source points to another authoritative source, preserve that
   relationship.
10. Never turn an example into a mandatory requirement.
11. Never turn a recommendation into a mandatory requirement.
12. Never remove an exception simply to make the guidance easier to follow.

AGENT USEFULNESS

The resulting skill must tell an AI coding agent:

- when to load the skill
- what it must do
- what it must not do
- what decisions it should make
- what to check before changing code
- what to test
- what quality gates matter
- what security/privacy concerns apply
- when another skill must also be loaded
- what exceptions exist
- what to do when the source is unclear

Do not merely summarise the source.

Extract operational rules.

Use explicit IF / THEN decision rules when they are supported by the source.

QUALITY

The output should be detailed enough that an agent can perform routine
engineering work without repeatedly rereading the source page.

However, do not fabricate missing detail.

SOURCE TRACEABILITY

Every important requirement should be traceable to one or more source URLs.

At the end of the skill provide an "Authoritative sources" section.

When possible, include source URLs next to major sections.

The source URLs supplied in the input are authoritative.

OUTPUT

Return ONLY the Markdown document.

Do not surround it with Markdown fences.

Do not say "Here is the skill".

Do not include analysis.
"""


def build_llm_prompt(
    skill: str,
    pages: list[Page],
) -> str:

    title = SKILL_DEFINITIONS[
        skill
    ]["title"]

    source_material = []

    for index, page in enumerate(
        pages,
        start=1,
    ):

        source_material.append(
            f"""
================ SOURCE {index} ================

URL:
{page.url}

TITLE:
{page.title}

HEADINGS:
{chr(10).join(page.headings)}

CONTENT:
{page.content}

================ END SOURCE {index} ================
"""
        )

    related = RELATED_SKILLS.get(
        skill,
        [],
    )

    related_text = (
        "\n".join(
            f"- {name}"
            for name in related
        )
        if related
        else "- None identified"
    )

    return f"""
{SYSTEM_INSTRUCTIONS}

SKILL TO PRODUCE

Name:
{skill}

Title:
{title}

RELATED SKILLS

{related_text}

SOURCE MATERIAL

{"".join(source_material)}

Now produce the complete SKILL.md.

The document MUST contain:

# {title}

## Purpose

## When this skill applies

## NHSBSA requirements

## Mandatory requirements

## Recommended practices

## Detailed implementation guidance

## Decision rules

## Testing and quality gates

## Security and data considerations

## Common failure modes

## Exceptions and deviations

## Agent completion checklist

## Related skills

## Authoritative sources

Where a requested section genuinely has no source-backed content, say so
rather than inventing it.
"""


# ============================================================================
# LLM validation
# ============================================================================

REQUIRED_SECTIONS = [
    "Purpose",
    "When this skill applies",
    "NHSBSA requirements",
    "Mandatory requirements",
    "Recommended practices",
    "Detailed implementation guidance",
    "Decision rules",
    "Testing and quality gates",
    "Security and data considerations",
    "Common failure modes",
    "Exceptions and deviations",
    "Agent completion checklist",
    "Related skills",
    "Authoritative sources",
]


def validate_skill(
    content: str,
    pages: list[Page],
) -> list[str]:

    errors = []

    if not content.startswith("# "):
        errors.append(
            "Skill does not start with a Markdown H1."
        )

    lower = content.lower()

    for section in REQUIRED_SECTIONS:

        if section.lower() not in lower:
            errors.append(
                f"Missing section: {section}"
            )

    for page in pages:

        if page.url not in content:
            errors.append(
                f"Missing source URL: {page.url}"
            )

    if len(content) < 2500:
        errors.append(
            "Skill is suspiciously short; expected detailed agent guidance."
        )

    return errors


# ============================================================================
# AGENTS.md generation
# ============================================================================

def generate_agents(
    skills: Iterable[str],
    crawl_date: str,
) -> str:

    skills = sorted(skills)

    lines = [
        "# AGENTS.md — NHSBSA Engineering Guidance",
        "",
        "This repository contains an agent-oriented knowledge pack derived "
        "from the NHS Business Services Authority Digital, Data and "
        "Technology Playbook.",
        "",
        "Authoritative Playbook:",
        "",
        "https://nhsbsa.github.io/nhsbsa-digital-playbook/",
        "",
        "## Mandatory operating procedure",
        "",
        "Before modifying code, configuration, infrastructure, tests, "
        "dependencies, documentation or Git history:",
        "",
        "1. Inspect the existing repository conventions.",
        "2. Identify every applicable skill below.",
        "3. Read each applicable `SKILL.md` completely.",
        "4. Follow mandatory NHSBSA requirements.",
        "5. Apply recommendations where appropriate.",
        "6. Check related skills.",
        "7. Add/update tests for behavioural changes.",
        "8. Run applicable quality gates.",
        "9. Do not bypass security or review controls.",
        "10. Consult the authoritative source where the local skill is "
        "ambiguous or time-sensitive.",
        "",
        "## Always consider",
        "",
        "- `coding`",
        "- `style-guides`",
        "- `testing`",
        "- `peer-review`",
        "- `git`",
        "",
        "## Skill catalogue",
        "",
    ]

    for skill in skills:

        title = SKILL_DEFINITIONS.get(
            skill,
            {},
        ).get(
            "title",
            skill.replace("-", " ").title(),
        )

        lines.append(
            f"- `{skill}` — {title}: "
            f"`skills/{skill}/SKILL.md`"
        )

    lines.extend(
        [
            "",
            "## Security rule",
            "",
            "Security-sensitive work must load `secure-development` "
            "and any relevant specialist security skills.",
            "",
            "## Secrets rule",
            "",
            "Never commit credentials, tokens, private keys, passwords or "
            "other secrets. Load `secrets-detection` when credentials are "
            "involved.",
            "",
            "## Personal data rule",
            "",
            "Do not introduce unnecessary personal data into source code, "
            "tests, URLs, logs or error messages.",
            "",
            "## Runtime and dependency rule",
            "",
            "Before changing dependencies or runtime versions, load "
            "`patching` and `release-adoption`.",
            "",
            "Runtime-version information is time-sensitive. Check the "
            "current NHSBSA adoption schedule.",
            "",
            "## Git rule",
            "",
            "Do not rewrite shared Git history unless the specific "
            "`git-history-rewrite` process applies.",
            "",
            "## Review rule",
            "",
            "Production-code changes must follow the NHSBSA peer-review "
            "process unless an explicitly approved exception applies.",
            "",
            "## Source precedence",
            "",
            "The authoritative NHSBSA Playbook takes precedence over this "
            "generated knowledge pack.",
            "",
            f"Knowledge pack generated: {crawl_date}",
            "",
        ]
    )

    return "\n".join(lines)


# ============================================================================
# Source manifest
# ============================================================================

def generate_sources(
    pages: list[Page],
    grouped: dict[str, list[Page]],
    crawl_date: str,
) -> str:

    lines = [
        "# NHSBSA Playbook Sources",
        "",
        f"Generated: {crawl_date}",
        "",
        f"Pages crawled: {len(pages)}",
        "",
        "## Skill mapping",
        "",
    ]

    for skill in sorted(grouped):

        lines.append(
            f"### {skill}"
        )

        lines.append("")

        for page in grouped[skill]:

            lines.append(
                f"- {page.url}"
            )

        lines.append("")

    lines.extend(
        [
            "## Complete crawl",
            "",
        ]
    )

    for page in sorted(
        pages,
        key=lambda item: item.url,
    ):

        lines.append(
            f"- {page.url}"
        )

    lines.append("")

    return "\n".join(lines)


# ============================================================================
# Version
# ============================================================================

def generate_version(
    pages: list[Page],
    crawl_date: str,
) -> str:

    urls = "\n".join(
        sorted(
            page.url
            for page in pages
        )
    )

    digest = hashlib.sha256(
        urls.encode("utf-8")
    ).hexdigest()

    return f"""# Knowledge Pack Version

Generated: {crawl_date}

Pages crawled: {len(pages)}

URL manifest SHA-256:

`{digest}`

## Generation

This pack was generated from the NHSBSA Digital, Data and Technology
Playbook using a recursive crawler and local LLM generation.

LLM-generated guidance must always be treated as a derived interpretation.

The authoritative source remains:

https://nhsbsa.github.io/nhsbsa-digital-playbook/

Regenerate this pack when the source Playbook changes.
"""


# ============================================================================
# Main build
# ============================================================================

def build(
    output: Path,
    model: str,
    max_pages: int,
    use_llm: bool,
    force: bool,
) -> None:

    bundle = (
        output
        / "nhsbsa-playbook-agents"
    )

    if bundle.exists():

        if not force:

            raise RuntimeError(
                f"{bundle} already exists. "
                "Use --force to replace it."
            )

        shutil.rmtree(bundle)

    bundle.mkdir(
        parents=True
    )

    # ------------------------------------------------------------------------
    # Crawl
    # ------------------------------------------------------------------------

    pages = crawl(
        ROOT_URL,
        max_pages,
    )

    if not pages:
        raise RuntimeError(
            "No pages were crawled."
        )

    # ------------------------------------------------------------------------
    # Save raw source material
    # ------------------------------------------------------------------------

    source_dir = (
        bundle
        / "source"
    )

    source_dir.mkdir(
        parents=True
    )

    for index, page in enumerate(
        pages,
        start=1,
    ):

        digest = hashlib.sha1(
            page.url.encode(
                "utf-8"
            )
        ).hexdigest()[:10]

        parsed = urlparse(
            page.url
        )

        path = parsed.path.strip(
            "/"
        )

        slug = re.sub(
            r"[^a-zA-Z0-9]+",
            "-",
            path,
        ).strip("-")

        filename = (
            f"{index:03d}-"
            f"{slug[:80]}-"
            f"{digest}.md"
        )

        source_file = (
            source_dir
            / filename
        )

        source_file.write_text(
            f"# {page.title}\n\n"
            f"Source: {page.url}\n\n"
            f"{page.content}\n",
            encoding="utf-8",
        )

    # ------------------------------------------------------------------------
    # Group skills
    # ------------------------------------------------------------------------

    grouped = group_pages(
        pages
    )

    print()
    print("Skill groups")
    print("============")

    for skill, skill_pages in sorted(
        grouped.items()
    ):

        print(
            f"{skill:30} "
            f"{len(skill_pages)} source page(s)"
        )

    print()

    # ------------------------------------------------------------------------
    # LLM
    # ------------------------------------------------------------------------

    if use_llm:

        print(
            f"Checking Ollama model: {model}"
        )

        check_ollama(
            model
        )

    # ------------------------------------------------------------------------
    # Generate skills
    # ------------------------------------------------------------------------

    skills_dir = (
        bundle
        / "skills"
    )

    skills_dir.mkdir()

    generated = {}

    for skill, skill_pages in sorted(
        grouped.items()
    ):

        skill_dir = (
            skills_dir
            / skill
        )

        skill_dir.mkdir(
            parents=True
        )

        print()
        print(
            f"Generating skill: {skill}"
        )

        if use_llm:

            prompt = build_llm_prompt(
                skill,
                skill_pages,
            )

            content = ollama_request(
                model,
                prompt,
            )

        else:

            # Useful fallback if --no-llm is specified.
            content = (
                f"# "
                f"{SKILL_DEFINITIONS[skill]['title']}"
                f"\n\n"
                "## Purpose\n\n"
                "This skill is derived from the NHSBSA Playbook.\n\n"
                "## Authoritative sources\n\n"
                + "\n".join(
                    f"- {page.url}"
                    for page in skill_pages
                )
                + "\n"
            )

        errors = validate_skill(
            content,
            skill_pages,
        )

        if errors:

            print(
                f"  WARNING: validation found "
                f"{len(errors)} issue(s)"
            )

            for error in errors:

                print(
                    f"    - {error}"
                )

            if use_llm:

                print(
                    "  Regenerating with a stricter prompt..."
                )

                retry_prompt = (
                    build_llm_prompt(
                        skill,
                        skill_pages,
                    )
                    + """

IMPORTANT VALIDATION FAILURE

Your previous output failed structural validation.

Make absolutely sure the result contains every required section:

- Purpose
- When this skill applies
- NHSBSA requirements
- Mandatory requirements
- Recommended practices
- Detailed implementation guidance
- Decision rules
- Testing and quality gates
- Security and data considerations
- Common failure modes
- Exceptions and deviations
- Agent completion checklist
- Related skills
- Authoritative sources

The result must also contain EVERY supplied source URL.

Return only the corrected Markdown.
"""
                )

                content = ollama_request(
                    model,
                    retry_prompt,
                )

                errors = validate_skill(
                    content,
                    skill_pages,
                )

                if errors:

                    print(
                        "  WARNING: second validation "
                        "still has issues:"
                    )

                    for error in errors:

                        print(
                            f"    - {error}"
                        )

        skill_file = (
            skill_dir
            / "SKILL.md"
        )

        skill_file.write_text(
            content.strip()
            + "\n",
            encoding="utf-8",
        )

        references = (
            skill_dir
            / "references.md"
        )

        references.write_text(
            "# Authoritative References\n\n"
            + "\n".join(
                f"- {page.url}"
                for page in skill_pages
            )
            + "\n",
            encoding="utf-8",
        )

        generated[
            skill
        ] = {
            "pages": len(skill_pages),
            "validation_errors": errors,
        }

    # ------------------------------------------------------------------------
    # Root files
    # ------------------------------------------------------------------------

    crawl_date = datetime.now(
        timezone.utc
    ).strftime(
        "%Y-%m-%d %H:%M UTC"
    )

    (
        bundle
        / "AGENTS.md"
    ).write_text(
        generate_agents(
            grouped.keys(),
            crawl_date,
        ),
        encoding="utf-8",
    )

    (
        bundle
        / "SOURCES.md"
    ).write_text(
        generate_sources(
            pages,
            grouped,
            crawl_date,
        ),
        encoding="utf-8",
    )

    (
        bundle
        / "VERSION.md"
    ).write_text(
        generate_version(
            pages,
            crawl_date,
        ),
        encoding="utf-8",
    )

    (
        bundle
        / "PLAYBOOK.md"
    ).write_text(
        """# NHSBSA Digital, Data and Technology Playbook

This directory contains an agent-oriented knowledge pack derived from the
NHS Business Services Authority Digital, Data and Technology Playbook.

Authoritative source:

https://nhsbsa.github.io/nhsbsa-digital-playbook/

Start with `AGENTS.md`.

The `skills/` directory contains detailed agent guidance.

The `source/` directory contains the crawled source material used to
generate the skills.

The generated skills must not be treated as a replacement for the
authoritative NHSBSA documentation.
""",
        encoding="utf-8",
    )

    # ------------------------------------------------------------------------
    # Generation manifest
    # ------------------------------------------------------------------------

    manifest = {
        "generated": crawl_date,
        "model": model if use_llm else None,
        "ollama_url": OLLAMA_URL if use_llm else None,
        "pages": len(pages),
        "skills": generated,
    }

    (
        bundle
        / "GENERATION.json"
    ).write_text(
        json.dumps(
            manifest,
            indent=2,
        ),
        encoding="utf-8",
    )

    # ------------------------------------------------------------------------
    # ZIP
    # ------------------------------------------------------------------------

    zip_path = (
        output
        / "nhsbsa-playbook-agents.zip"
    )

    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(
        zip_path,
        "w",
        zipfile.ZIP_DEFLATED,
    ) as archive:

        for file in bundle.rglob("*"):

            if not file.is_file():
                continue

            archive.write(
                file,
                file.relative_to(
                    output
                ),
            )

    print()
    print("=" * 60)
    print("BUILD COMPLETE")
    print("=" * 60)
    print()
    print(
        f"Bundle: {bundle}"
    )
    print(
        f"ZIP:    {zip_path}"
    )
    print()
    print(
        f"Skills generated: {len(grouped)}"
    )
    print(
        f"Pages crawled:    {len(pages)}"
    )
    print()


# ============================================================================
# CLI
# ============================================================================

def main() -> int:

    parser = argparse.ArgumentParser(
        description=(
            "Build a detailed NHSBSA Playbook "
            "agent knowledge pack."
        )
    )

    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=(
            "Ollama model to use "
            f"(default: {DEFAULT_MODEL})"
        ),
    )

    parser.add_argument(
        "--output",
        default=".",
        help=(
            "Output directory "
            "(default: current directory)"
        ),
    )

    parser.add_argument(
        "--max-pages",
        type=int,
        default=DEFAULT_MAX_PAGES,
        help=(
            "Maximum number of pages to crawl "
            f"(default: {DEFAULT_MAX_PAGES})"
        ),
    )

    parser.add_argument(
        "--no-llm",
        action="store_true",
        help=(
            "Skip LLM generation. "
            "Useful for testing the crawler."
        ),
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help=(
            "Replace an existing output directory."
        ),
    )

    args = parser.parse_args()

    output = Path(
        args.output
    ).resolve()

    output.mkdir(
        parents=True,
        exist_ok=True,
    )

    try:

        build(
            output=output,
            model=args.model,
            max_pages=args.max_pages,
            use_llm=not args.no_llm,
            force=args.force,
        )

    except KeyboardInterrupt:

        print(
            "\nInterrupted."
        )

        return 130

    except Exception as exc:

        print(
            "\nERROR:"
        )

        print(
            str(exc)
        )

        return 1

    return 0


if __name__ == "__main__":
    sys.exit(
        main()
    )
