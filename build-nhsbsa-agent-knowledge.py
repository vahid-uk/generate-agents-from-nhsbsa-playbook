#!/usr/bin/env python3

"""
NHS Agent Knowledge Pack Builder

Combines:

    NHSBSA Digital Playbook
    NHS England Digital Service Manual
    llms.txt discovery
    HTML crawling
    Markdown discovery
    Do / Don't extraction
    Local LLM synthesis through Ollama

Output:

    AGENTS.md
    SOURCES.md
    VERSION.md
    GENERATION.json

    skills/
        <skill>/
            SKILL.md
            references.md

    source/
        raw crawled source material

    llms/
        llms.txt
        generated LLM-friendly source indexes

    nhs-agent-knowledge.zip

Install:

    python3 -m pip install requests beautifulsoup4

Install Ollama:

    https://ollama.com/

Example model:

    ollama pull qwen3:14b

Run:

    python3 build-nhs-agent-knowledge.py

Example:

    python3 build-nhs-agent-knowledge.py \
        --model qwen3:14b \
        --max-pages 500 \
        --output ./nhs-agent-build \
        --force
"""


from __future__ import annotations

import argparse
import hashlib
import json
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
from urllib.parse import (
    urljoin,
    urldefrag,
    urlparse,
)

import requests
from bs4 import BeautifulSoup


# ============================================================================
# Configuration
# ============================================================================

NHSBSA_ROOT = (
    "https://nhsbsa.github.io/"
    "nhsbsa-digital-playbook/"
)

NHSBSA_DEVELOPMENT = (
    NHSBSA_ROOT
    + "development/"
)

NHS_SERVICE_MANUAL_ROOT = (
    "https://service-manual.nhs.uk/"
)

NHS_DESIGN_SYSTEM = (
    NHS_SERVICE_MANUAL_ROOT
    + "design-system/"
)

OLLAMA_URL = (
    "http://localhost:11434"
)

DEFAULT_MODEL = (
    "qwen3:14b"
)

REQUEST_TIMEOUT = 30
OLLAMA_TIMEOUT = 900
CRAWL_DELAY = 0.2

USER_AGENT = (
    "NHS-Agent-Knowledge-Builder/2.0 "
    "(documentation and llms.txt crawler)"
)


# ============================================================================
# Site configuration
# ============================================================================

SITES = {
    "nhsbsa-playbook": {
        "name": "NHSBSA Digital Playbook",
        "root": NHSBSA_ROOT,
        "crawl_roots": [
            NHSBSA_DEVELOPMENT,
        ],
        "hosts": {
            "nhsbsa.github.io",
        },
    },
    "nhs-service-manual": {
        "name": "NHS Digital Service Manual",
        "root": NHS_SERVICE_MANUAL_ROOT,
        "crawl_roots": [
            NHS_DESIGN_SYSTEM,
        ],
        "hosts": {
            "service-manual.nhs.uk",
        },
    },
}


# ============================================================================
# Skills
# ============================================================================

SKILLS = {
    "coding": "Coding and engineering practices",
    "secure-development": "Secure development",
    "personal-data": "Personal data and privacy",
    "secrets-detection": "Secrets and credentials",
    "git": "Git and source control",
    "git-history-rewrite": "Git history rewriting",
    "testing": "Testing",
    "static-analysis": "Static analysis and code quality",
    "peer-review": "Peer review",
    "logging": "Logging and observability",
    "patching": "Dependencies and patching",
    "release-adoption": "Release and technology adoption",
    "apis": "APIs",
    "frontend": "Frontend development",
    "accessibility": "Accessibility",
    "design-system": "NHS design system",
    "design-principles": "NHS design principles",
    "components": "NHS design system components",
    "patterns": "NHS design system patterns",
    "content": "NHS digital content",
    "forms": "Forms and transactional interfaces",
    "navigation": "Navigation",
    "responsive-design": "Responsive design",
    "service-design": "Service design",
    "prototyping": "Prototyping",
    "production-frontend": "Production frontend implementation",
    "dos-and-donts": "Do and Don't guidance",
    "java": "Java",
    "nodejs": "Node.js",
}


KEYWORDS = {
    "secure-development": [
        "security",
        "secure",
        "owasp",
        "ncsc",
        "vulnerability",
    ],
    "personal-data": [
        "personal data",
        "personal information",
        "data protection",
        "pii",
    ],
    "secrets-detection": [
        "secret",
        "credential",
        "password",
        "token",
        "gitleaks",
    ],
    "testing": [
        "test",
        "testing",
        "unit test",
        "integration test",
    ],
    "accessibility": [
        "accessibility",
        "accessible",
        "screen reader",
        "keyboard",
        "wcag",
        "assistive",
    ],
    "design-system": [
        "design system",
        "nhs design system",
        "nhs.uk frontend",
    ],
    "components": [
        "component",
        "components",
    ],
    "patterns": [
        "pattern",
        "patterns",
    ],
    "design-principles": [
        "design principle",
        "design principles",
    ],
    "content": [
        "content",
        "content guide",
        "plain english",
        "reading age",
    ],
    "forms": [
        "form",
        "forms",
        "input",
        "checkbox",
        "radio",
        "error message",
        "error summary",
    ],
    "navigation": [
        "navigation",
        "breadcrumb",
        "pagination",
        "skip link",
        "back link",
    ],
    "responsive-design": [
        "responsive",
        "mobile",
        "desktop",
        "viewport",
    ],
    "frontend": [
        "frontend",
        "front end",
        "css",
        "html",
        "javascript",
    ],
    "production-frontend": [
        "production code",
        "npm",
        "nunjucks",
        "nhs.uk frontend",
    ],
    "prototyping": [
        "prototype",
        "prototyping",
    ],
    "service-design": [
        "service design",
        "user needs",
        "service",
        "journey",
    ],
    "dos-and-donts": [
        "do and don't",
        "do and dont",
        "dos and don'ts",
        "do not",
    ],
    "apis": [
        "api",
        "rest",
        "endpoint",
    ],
    "patching": [
        "dependency",
        "dependencies",
        "patch",
        "vulnerability",
        "npm",
    ],
    "release-adoption": [
        "adoption",
        "release",
        "deprecation",
        "decommission",
    ],
    "git": [
        "git",
        "branch",
        "pull request",
        "merge",
    ],
    "peer-review": [
        "peer review",
        "code review",
        "pull request",
        "merge request",
    ],
    "static-analysis": [
        "sonarqube",
        "static analysis",
        "quality gate",
    ],
    "logging": [
        "logging",
        "logs",
        "audit",
        "monitoring",
    ],
    "java": [
        "java",
        "spring",
        "maven",
    ],
    "nodejs": [
        "node.js",
        "nodejs",
        "npm",
    ],
}


# URL-specific classification takes precedence.

URL_RULES = {
    "/design-system/components/": "components",
    "/design-system/patterns/": "patterns",
    "/design-system/design-principles": "design-principles",
    "/design-system/production": "production-frontend",
    "/design-system/prototyping": "prototyping",
    "/design-system/": "design-system",
    "/development/": "coding",
}


RELATED = {
    "design-system": [
        "components",
        "patterns",
        "accessibility",
        "design-principles",
        "frontend",
    ],
    "components": [
        "design-system",
        "accessibility",
        "dos-and-donts",
        "frontend",
    ],
    "patterns": [
        "components",
        "design-system",
        "accessibility",
        "content",
    ],
    "accessibility": [
        "design-system",
        "components",
        "patterns",
        "content",
        "frontend",
    ],
    "content": [
        "accessibility",
        "components",
        "patterns",
        "forms",
    ],
    "frontend": [
        "design-system",
        "accessibility",
        "testing",
        "secure-development",
    ],
    "production-frontend": [
        "frontend",
        "design-system",
        "components",
        "accessibility",
        "testing",
    ],
    "secure-development": [
        "personal-data",
        "secrets-detection",
        "testing",
        "logging",
    ],
    "testing": [
        "accessibility",
        "static-analysis",
        "peer-review",
    ],
}


# ============================================================================
# Data classes
# ============================================================================

@dataclass
class Page:
    site: str
    url: str
    title: str
    headings: list[str]
    content: str
    links: list[str]
    dos: list[str]
    donts: list[str]
    markdown_url: str | None = None
    source_type: str = "html"


@dataclass
class LLMDocument:
    site: str
    url: str
    title: str
    content: str
    source_type: str


# ============================================================================
# HTTP
# ============================================================================

session = requests.Session()

session.headers.update(
    {
        "User-Agent": USER_AGENT,
        "Accept": (
            "text/html,"
            "application/xhtml+xml,"
            "text/markdown,"
            "text/plain"
        ),
    }
)


def fetch(
    url: str,
    accept: str | None = None,
) -> requests.Response:

    headers = {}

    if accept:
        headers["Accept"] = accept

    response = session.get(
        url,
        headers=headers,
        timeout=REQUEST_TIMEOUT,
    )

    response.raise_for_status()

    return response


# ============================================================================
# URL handling
# ============================================================================

def normalise_url(
    url: str,
    allowed_hosts: set[str],
) -> str | None:

    url, _ = urldefrag(url)

    parsed = urlparse(url)

    if parsed.scheme not in {
        "http",
        "https",
    }:
        return None

    if parsed.netloc not in allowed_hosts:
        return None

    path = parsed.path

    ignored = [
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
    ]

    if any(
        path.lower().endswith(ext)
        for ext in ignored
    ):
        return None

    if (
        not path.endswith("/")
        and "." not in path.split("/")[-1]
    ):
        path += "/"

    return (
        f"{parsed.scheme}://"
        f"{parsed.netloc}"
        f"{path}"
    )


# ============================================================================
# llms.txt discovery
# ============================================================================

def candidate_llms_urls(
    root: str,
) -> list[str]:

    parsed = urlparse(root)

    path = parsed.path

    if not path.endswith("/"):
        path += "/"

    candidates = []

    # Most specific location first.
    candidates.append(
        urljoin(
            root,
            "llms.txt",
        )
    )

    # Site root.
    candidates.append(
        f"{parsed.scheme}://"
        f"{parsed.netloc}/llms.txt"
    )

    # Normalise duplicates.
    return list(
        dict.fromkeys(candidates)
    )


def discover_llms_txt(
    site: dict,
) -> list[tuple[str, str]]:

    discovered = []

    checked = set()

    roots = [
        site["root"],
        *site["crawl_roots"],
    ]

    for root in roots:

        for candidate in candidate_llms_urls(
            root
        ):

            if candidate in checked:
                continue

            checked.add(candidate)

            try:

                response = fetch(
                    candidate,
                    accept=(
                        "text/plain,"
                        "text/markdown,"
                        "text/*"
                    ),
                )

                text = response.text

                if (
                    response.status_code == 200
                    and text.strip()
                ):

                    discovered.append(
                        (
                            candidate,
                            text,
                        )
                    )

                    print(
                        f"  found llms.txt: "
                        f"{candidate}"
                    )

            except Exception:
                pass

    return discovered


# ============================================================================
# llms.txt parser
# ============================================================================

def parse_llms_txt(
    url: str,
    text: str,
) -> list[str]:

    """
    Parse Markdown links from an llms.txt document.

    The llms.txt proposal specifies H1, optional blockquote/context,
    then H2 sections containing Markdown file lists.

    We deliberately retain all links and let the normal crawler decide
    whether a link belongs to the permitted site/path.
    """

    links = []

    pattern = re.compile(
        r"\[[^\]]+\]\(([^)]+)\)"
    )

    for match in pattern.finditer(
        text
    ):

        target = match.group(1)

        target = urljoin(
            url,
            target,
        )

        target, _ = urldefrag(
            target
        )

        if target not in links:
            links.append(target)

    return links


# ============================================================================
# HTML parsing
# ============================================================================

def clean(
    text: str,
) -> str:

    return re.sub(
        r"\s+",
        " ",
        text,
    ).strip()


def extract_dos_and_donts(
    soup: BeautifulSoup,
) -> tuple[list[str], list[str]]:

    dos = []
    donts = []

    # Detect explicit Do / Don't headings.
    headings = soup.find_all(
        ["h2", "h3", "h4"]
    )

    for heading in headings:

        heading_text = clean(
            heading.get_text(
                " ",
                strip=True,
            )
        ).lower()

        is_do = (
            "do" in heading_text
            and "don't" not in heading_text
            and "dont" not in heading_text
        )

        is_dont = (
            "don't" in heading_text
            or "dont" in heading_text
            or "do not" in heading_text
        )

        if not (
            is_do or is_dont
        ):
            continue

        # Collect nearby list items until next heading.
        for sibling in heading.find_all_next():

            if sibling is heading:
                continue

            if sibling.name in [
                "h1",
                "h2",
                "h3",
                "h4",
            ]:
                break

            if sibling.name == "li":

                text = clean(
                    sibling.get_text(
                        " ",
                        strip=True,
                    )
                )

                if not text:
                    continue

                if is_dont:
                    donts.append(
                        text
                    )
                else:
                    dos.append(
                        text
                    )

    # Also recognise textual forms such as:
    #
    # "Do:"
    # "Don't:"
    #
    text = soup.get_text(
        "\n",
        strip=True,
    )

    lines = [
        clean(line)
        for line in text.splitlines()
    ]

    mode = None

    for line in lines:

        lower = line.lower()

        if lower in {
            "do",
            "dos",
            "do:",
            "dos:",
        }:

            mode = "do"
            continue

        if lower in {
            "don't",
            "dont",
            "don'ts",
            "donts",
            "don't:",
            "dont:",
        }:

            mode = "dont"
            continue

        if mode and len(line) > 3:

            if line.startswith(
                ("•", "-", "*")
            ):

                value = re.sub(
                    r"^[•\-*]\s*",
                    "",
                    line,
                )

                if mode == "do":
                    dos.append(value)
                else:
                    donts.append(value)

    dos = list(
        dict.fromkeys(dos)
    )

    donts = list(
        dict.fromkeys(donts)
    )

    return dos, donts


def html_to_structured_text(
    soup: BeautifulSoup,
) -> str:

    root = (
        soup.find("main")
        or soup.find("article")
        or soup.body
        or soup
    )

    chunks = []

    for element in root.find_all(
        [
            "h1",
            "h2",
            "h3",
            "h4",
            "h5",
            "p",
            "li",
            "pre",
            "blockquote",
            "table",
        ]
    ):

        if element.name == "table":

            rows = []

            for tr in element.find_all(
                "tr"
            ):

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

            value = element.get_text(
                "\n",
                strip=True,
            )

            if value:
                chunks.append(
                    "```text\n"
                    + value
                    + "\n```"
                )

            continue

        value = clean(
            element.get_text(
                " ",
                strip=True,
            )
        )

        if not value:
            continue

        if element.name.startswith("h"):

            level = int(
                element.name[1]
            )

            chunks.append(
                f"{'#' * level} {value}"
            )

        elif element.name == "li":

            chunks.append(
                f"- {value}"
            )

        elif element.name == "blockquote":

            chunks.append(
                f"> {value}"
            )

        else:

            chunks.append(value)

    return "\n\n".join(
        chunks
    )


def parse_html_page(
    site_name: str,
    url: str,
    html: str,
) -> Page:

    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    # Preserve links before deleting navigation.
    links = []

    for anchor in soup.find_all(
        "a",
        href=True,
    ):

        links.append(
            urljoin(
                url,
                anchor["href"],
            )
        )

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
            headings.append(
                value
            )

    dos, donts = (
        extract_dos_and_donts(
            soup
        )
    )

    # Remove implementation noise after extracting links and Do/Don't data.
    for element in soup(
        [
            "script",
            "style",
            "noscript",
            "svg",
        ]
    ):
        element.decompose()

    content = html_to_structured_text(
        soup
    )

    markdown_url = discover_markdown_url(
        url,
        soup,
    )

    return Page(
        site=site_name,
        url=url,
        title=title,
        headings=list(
            dict.fromkeys(
                headings
            )
        ),
        content=content,
        links=list(
            dict.fromkeys(
                links
            )
        ),
        dos=dos,
        donts=donts,
        markdown_url=markdown_url,
    )


# ============================================================================
# Markdown discovery
# ============================================================================

def discover_markdown_url(
    url: str,
    soup: BeautifulSoup,
) -> str | None:

    # First honour explicit rel=alternate metadata.
    for link in soup.find_all(
        "link",
        href=True,
    ):

        rel = [
            str(x).lower()
            for x in link.get(
                "rel",
                [],
            )
        ]

        link_type = (
            link.get(
                "type",
                ""
            )
            or ""
        ).lower()

        if (
            "alternate" in rel
            and link_type
            == "text/markdown"
        ):

            return urljoin(
                url,
                link["href"],
            )

    # Then try the common llms.txt conventions.
    candidates = [
        url.rstrip("/")
        + ".md",
        url.rstrip("/")
        + "/index.md",
        url.rstrip("/")
        + ".html.md",
    ]

    for candidate in candidates:

        try:

            response = fetch(
                candidate,
                accept="text/markdown,text/plain",
            )

            if (
                response.status_code
                == 200
                and response.text.strip()
            ):

                return candidate

        except Exception:
            continue

    return None


# ============================================================================
# Crawl
# ============================================================================

def crawl_site(
    site_key: str,
    site: dict,
    max_pages: int,
) -> tuple[
    list[Page],
    list[tuple[str, str]],
]:

    print()
    print(
        "=" * 70
    )
    print(
        f"Crawling: {site['name']}"
    )
    print(
        "=" * 70
    )

    llms_files = discover_llms_txt(
        site
    )

    queue = deque()

    for root in site[
        "crawl_roots"
    ]:

        queue.append(root)

    # llms.txt links are added after parsing.
    visited = set()
    pages = []

    while (
        queue
        and len(pages) < max_pages
    ):

        url = queue.popleft()

        url = normalise_url(
            url,
            site["hosts"],
        )

        if not url:
            continue

        # Do not crawl outside the intended area.
        allowed = False

        for root in site[
            "crawl_roots"
        ]:

            if url.startswith(root):
                allowed = True
                break

        if not allowed:
            continue

        if url in visited:
            continue

        visited.add(url)

        print(
            f"[{len(pages) + 1:03d}] {url}"
        )

        try:

            response = fetch(
                url
            )

            content_type = (
                response.headers.get(
                    "content-type",
                    "",
                )
                .lower()
            )

            if "html" not in content_type:
                continue

            page = parse_html_page(
                site_key,
                url,
                response.text,
            )

            pages.append(page)

            # Add regular links.
            for link in page.links:

                normalised = normalise_url(
                    link,
                    site["hosts"],
                )

                if not normalised:
                    continue

                for root in site[
                    "crawl_roots"
                ]:

                    if normalised.startswith(
                        root
                    ):
                        if (
                            normalised
                            not in visited
                        ):
                            queue.append(
                                normalised
                            )
                        break

            # Add discovered Markdown version.
            if page.markdown_url:

                markdown_normalised = (
                    normalise_url(
                        page.markdown_url,
                        site["hosts"],
                    )
                )

                if markdown_normalised:
                    page.markdown_url = (
                        markdown_normalised
                    )

        except Exception as exc:

            print(
                f"    ERROR: {exc}"
            )

        time.sleep(
            CRAWL_DELAY
        )

    # Expand links discovered through llms.txt.
    llms_links = []

    for llms_url, text in (
        llms_files
    ):

        links = parse_llms_txt(
            llms_url,
            text,
        )

        for link in links:

            normalised = normalise_url(
                link,
                site["hosts"],
            )

            if not normalised:
                continue

            for root in site[
                "crawl_roots"
            ]:

                if normalised.startswith(
                    root
                ):

                    if (
                        normalised
                        not in visited
                    ):

                        queue.append(
                            normalised
                        )

                    llms_links.append(
                        normalised
                    )

                    break

    # Crawl llms-discovered pages, subject to max-pages.
    while (
        queue
        and len(pages) < max_pages
    ):

        url = queue.popleft()

        url = normalise_url(
            url,
            site["hosts"],
        )

        if not url:
            continue

        if url in visited:
            continue

        visited.add(url)

        print(
            f"[LLMS {len(pages) + 1:03d}] "
            f"{url}"
        )

        try:

            response = fetch(
                url
            )

            if (
                "html"
                not in response.headers.get(
                    "content-type",
                    "",
                ).lower()
            ):
                continue

            page = parse_html_page(
                site_key,
                url,
                response.text,
            )

            pages.append(page)

        except Exception as exc:

            print(
                f"    ERROR: {exc}"
            )

        time.sleep(
            CRAWL_DELAY
        )

    return (
        pages,
        llms_files,
    )


# ============================================================================
# Classification
# ============================================================================

def classify_page(
    page: Page,
) -> str | None:

    path = urlparse(
        page.url
    ).path.lower()

    for fragment, skill in (
        URL_RULES.items()
    ):

        if fragment in path:

            # More specific paths should win.
            return skill

    text = (
        page.title
        + "\n"
        + "\n".join(
            page.headings
        )
        + "\n"
        + page.content[:10000]
    ).lower()

    # Do/Don't pages get their own skill,
    # but still appear in their subject-matter skill.
    if page.dos or page.donts:

        if (
            "component" in text
            or "pattern" in text
        ):
            return "dos-and-donts"

    scores = {}

    for skill, keywords in (
        KEYWORDS.items()
    ):

        score = 0

        for keyword in keywords:

            score += text.count(
                keyword
            )

        if score:
            scores[skill] = score

    if not scores:
        return None

    return max(
        scores,
        key=scores.get,
    )


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

    # Important: Do/Don't content is cross-cutting.
    # Add pages with explicit Do/Don't content to
    # the dedicated skill without removing them
    # from their primary skill.

    for page in pages:

        if (
            page.dos
            or page.donts
        ):

            if page not in grouped[
                "dos-and-donts"
            ]:

                grouped[
                    "dos-and-donts"
                ].append(
                    page
                )

    return dict(grouped)


# ============================================================================
# Source representation
# ============================================================================

def page_to_llm_document(
    page: Page,
) -> LLMDocument:

    parts = [
        f"# {page.title}",
        "",
        f"Source URL: {page.url}",
        f"Source site: {page.site}",
        "",
    ]

    if page.markdown_url:

        parts.extend(
            [
                "LLM-friendly Markdown:",
                page.markdown_url,
                "",
            ]
        )

    if page.headings:

        parts.extend(
            [
                "## Headings",
                "",
                *(
                    f"- {heading}"
                    for heading
                    in page.headings
                ),
                "",
            ]
        )

    if page.dos:

        parts.extend(
            [
                "## Explicit DO guidance",
                "",
                *(
                    f"- {item}"
                    for item
                    in page.dos
                ),
                "",
            ]
        )

    if page.donts:

        parts.extend(
            [
                "## Explicit DON'T guidance",
                "",
                *(
                    f"- {item}"
                    for item
                    in page.donts
                ),
                "",
            ]
        )

    parts.extend(
        [
            "## Source content",
            "",
            page.content,
        ]
    )

    return LLMDocument(
        site=page.site,
        url=page.url,
        title=page.title,
        content="\n".join(
            parts
        ),
        source_type=page.source_type,
    )


# ============================================================================
# Ollama
# ============================================================================

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
            "Ollama is not available. "
            "Run `ollama serve` first."
        ) from exc

    models = response.json().get(
        "models",
        []
    )

    available = [
        item.get(
            "name",
            "",
        )
        for item in models
    ]

    if model not in available:

        raise RuntimeError(
            f"Model '{model}' is not installed.\n"
            f"Run: ollama pull {model}\n\n"
            "Available models:\n"
            + "\n".join(
                available
            )
        )


def ollama(
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

    result = response.json().get(
        "response",
        "",
    )

    if not result.strip():
        raise RuntimeError(
            "Ollama returned an empty response."
        )

    return result.strip()


# ============================================================================
# LLM prompt
# ============================================================================

SYSTEM_PROMPT = r"""
You are an expert technical writer creating instructions for AI coding
agents working on NHS digital services.

You are given source material from:

1. The NHS Business Services Authority Digital Playbook.
2. The NHS England Digital Service Manual.

The source material is authoritative for the knowledge pack.

Your job is to transform the source into detailed operational instructions
for an AI coding agent.

THIS IS NOT A GENERAL SUMMARY.

The agent must be able to use the resulting SKILL.md while implementing,
reviewing or modifying a service.

SOURCE FIDELITY

- Never invent NHS policy.
- Never invent requirements.
- Never invent numerical thresholds.
- Never invent approval processes.
- Never invent accessibility criteria.
- Never invent exceptions.
- Never invent implementation APIs.
- Never convert an example into a requirement.
- Never convert a recommendation into a mandatory requirement.
- Preserve explicit exceptions.
- Preserve exact names of NHS components.
- Preserve exact names of technologies and tools.
- Preserve exact numerical values.
- Preserve source URLs.

If the source is ambiguous, say so.

REQUIREMENT STRENGTH

Clearly distinguish:

MUST / REQUIRED
SHOULD / RECOMMENDED
MAY / OPTIONAL

DO / DON'T

Every skill should contain explicit practical guidance.

"DO" means a source-backed action the agent should take.

"DON'T" means a source-backed action the agent should avoid.

Do not create a "don't" simply by negating a recommendation unless the
source clearly supports that interpretation.

Where the source contains explicit NHS Do and Don't guidance, preserve it
faithfully.

AGENT BEHAVIOUR

The resulting document should tell the agent:

- when this skill applies
- when it does not apply
- what to inspect before making changes
- what implementation approach to use
- what to avoid
- how to make decisions
- what to test
- what accessibility concerns exist
- what security/privacy concerns exist
- what quality gates apply
- when to involve another skill
- what exceptions exist
- what the final checklist is

NHS DESIGN SYSTEM

For design-system skills:

- prefer existing NHS styles, components and patterns where applicable
- distinguish components from patterns
- preserve documented usage constraints
- preserve "when to use"
- preserve "when not to use"
- preserve accessibility guidance
- preserve implementation guidance
- do not invent new NHS components
- do not imply that community resources are NHS-supported unless the source
  explicitly says so

SERVICE MANUAL

The Service Manual contains guidance for designing and building NHS
services. Treat its component, pattern, accessibility and design guidance
as source material, not as generic web-development advice.

SOURCE TRACEABILITY

Every major requirement must be traceable to a source URL.

Use a final section:

## Authoritative sources

with Markdown links to the relevant source pages.

OUTPUT

Return ONLY Markdown.

Do not use Markdown fences around the document.

Do not provide commentary outside the document.
"""


def build_prompt(
    skill: str,
    pages: list[Page],
) -> str:

    title = SKILLS.get(
        skill,
        skill.replace(
            "-",
            " ",
        ).title(),
    )

    documents = []

    for number, page in enumerate(
        pages,
        start=1,
    ):

        document = page_to_llm_document(
            page
        )

        documents.append(
            f"""
================ SOURCE {number} ================

{document.content}

================ END SOURCE {number} ================
"""
        )

    related = RELATED.get(
        skill,
        [],
    )

    related_lines = "\n".join(
        f"- `{item}`"
        for item in related
    ) or "- None identified"

    return f"""
{SYSTEM_PROMPT}

SKILL NAME

{skill}

SKILL TITLE

{title}

RELATED SKILLS

{related_lines}

SOURCE MATERIAL

{"".join(documents)}

Produce a detailed SKILL.md with EXACTLY these major sections:

# {title}

## Purpose

## When this skill applies

## When this skill does not apply

## NHS requirements

## Mandatory requirements

## Recommended practices

## Do

## Don't

## Detailed implementation guidance

## Decision rules

## Accessibility

## Security and data considerations

## Testing and quality gates

## Common failure modes

## Exceptions and deviations

## Agent completion checklist

## Related skills

## Authoritative sources

The document must be operational rather than descriptive.

For component and pattern material, explicitly capture:

- when to use
- when not to use
- implementation guidance
- accessibility considerations
- relevant Do/Don't guidance

Do not fabricate missing material.
"""


# ============================================================================
# Validation
# ============================================================================

REQUIRED_SECTIONS = [
    "Purpose",
    "When this skill applies",
    "When this skill does not apply",
    "NHS requirements",
    "Mandatory requirements",
    "Recommended practices",
    "Do",
    "Don't",
    "Detailed implementation guidance",
    "Decision rules",
    "Accessibility",
    "Security and data considerations",
    "Testing and quality gates",
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

    lower = content.lower()

    if not content.startswith(
        "# "
    ):
        errors.append(
            "Missing H1."
        )

    for section in (
        REQUIRED_SECTIONS
    ):

        if section.lower() not in lower:

            errors.append(
                f"Missing section: {section}"
            )

    if len(content) < 3000:

        errors.append(
            "Skill appears too short."
        )

    for page in pages:

        if page.url not in content:

            errors.append(
                f"Missing source URL: {page.url}"
            )

    return errors


# ============================================================================
# Root AGENTS.md
# ============================================================================

def build_agents_md(
    grouped: dict[str, list[Page]],
    generated: str,
) -> str:

    lines = [
        "# AGENTS.md",
        "",
        "# NHS Agent Engineering Guidance",
        "",
        "This repository contains an agent-oriented knowledge pack derived "
        "from the NHSBSA Digital Playbook and NHS England Digital Service "
        "Manual.",
        "",
        "## Source hierarchy",
        "",
        "Use the original NHS source pages as authoritative.",
        "",
        "Generated skills are structured interpretations of those sources.",
        "If a generated skill conflicts with an authoritative source, "
        "the authoritative source wins.",
        "",
        "## Before changing code",
        "",
        "The agent MUST:",
        "",
        "1. Identify the type of change.",
        "2. Load all relevant skills.",
        "3. Read the complete applicable SKILL.md files.",
        "4. Inspect the existing implementation.",
        "5. Follow mandatory NHS requirements.",
        "6. Apply applicable design-system components and patterns.",
        "7. Check accessibility requirements.",
        "8. Check security and personal-data implications.",
        "9. Add or update tests.",
        "10. Run applicable quality gates.",
        "11. Review the final change against the skill completion checklist.",
        "",
        "## Design-system rule",
        "",
        "When building an NHS user interface, first check whether the NHS "
        "design system already provides a suitable style, component or "
        "pattern.",
        "",
        "Do not create a bespoke solution merely because it is convenient.",
        "",
        "## Component rule",
        "",
        "Before implementing a UI component:",
        "",
        "- check `skills/components/SKILL.md`",
        "- check `skills/design-system/SKILL.md`",
        "- check `skills/accessibility/SKILL.md`",
        "- check the relevant component source page",
        "",
        "## Pattern rule",
        "",
        "Before implementing a recurring user journey or interaction:",
        "",
        "- check `skills/patterns/SKILL.md`",
        "- check relevant component skills",
        "- check accessibility guidance",
        "",
        "## Do / Don't rule",
        "",
        "Do not treat generated generic advice as NHS policy.",
        "Use the explicit Do and Don't guidance extracted from the NHS "
        "Service Manual and NHSBSA Playbook.",
        "",
        "## Accessibility rule",
        "",
        "Accessibility is not an optional enhancement. Any user-interface "
        "change must consider the applicable NHS accessibility guidance.",
        "",
        "Load:",
        "",
        "`skills/accessibility/SKILL.md`",
        "",
        "for UI changes.",
        "",
        "## Security rule",
        "",
        "Security-sensitive changes must load:",
        "",
        "`skills/secure-development/SKILL.md`",
        "",
        "and any relevant specialist security skills.",
        "",
        "## Personal-data rule",
        "",
        "If a change handles personal data, load:",
        "",
        "`skills/personal-data/SKILL.md`",
        "",
        "## Dependency rule",
        "",
        "Before changing dependencies or runtime versions, load:",
        "",
        "- `skills/patching/SKILL.md`",
        "- `skills/release-adoption/SKILL.md`",
        "",
        "## Git rule",
        "",
        "Never rewrite shared history unless the specific Git-history "
        "guidance applies.",
        "",
        "## Review rule",
        "",
        "Follow the peer-review guidance for production changes.",
        "",
        "## Skill catalogue",
        "",
    ]

    for skill in sorted(
        grouped
    ):

        title = SKILLS.get(
            skill,
            skill.replace(
                "-",
                " ",
            ).title(),
        )

        lines.append(
            f"- `{skill}` — {title} — "
            f"`skills/{skill}/SKILL.md`"
        )

    lines.extend(
        [
            "",
            "## Sources",
            "",
            "- `SOURCES.md` — complete source manifest",
            "- `source/` — crawled source material",
            "- `llms/` — llms.txt-derived navigation material",
            "",
            f"Generated: {generated}",
            "",
        ]
    )

    return "\n".join(
        lines
    )


# ============================================================================
# Source manifest
# ============================================================================

def build_sources(
    pages: list[Page],
    llms_files: list[tuple[str, str]],
    generated: str,
) -> str:

    lines = [
        "# Source Manifest",
        "",
        f"Generated: {generated}",
        "",
        f"HTML pages crawled: {len(pages)}",
        "",
        "## llms.txt files",
        "",
    ]

    for url, _ in llms_files:

        lines.append(
            f"- {url}"
        )

    lines.extend(
        [
            "",
            "## Crawled pages",
            "",
        ]
    )

    for page in sorted(
        pages,
        key=lambda item: item.url,
    ):

        lines.append(
            f"- [{page.title or page.url}]"
            f"({page.url})"
        )

        if page.markdown_url:

            lines.append(
                f"  - Markdown: "
                f"{page.markdown_url}"
            )

        if page.dos:

            lines.append(
                f"  - Explicit Do items: "
                f"{len(page.dos)}"
            )

        if page.donts:

            lines.append(
                f"  - Explicit Don't items: "
                f"{len(page.donts)}"
            )

    return "\n".join(
        lines
    ) + "\n"


# ============================================================================
# Generated llms.txt
# ============================================================================

def build_local_llms_txt(
    pages: list[Page],
    generated: str,
) -> str:

    lines = [
        "# NHS Agent Knowledge Pack",
        "",
        "> LLM-oriented index of NHSBSA Digital Playbook and NHS England "
        "Digital Service Manual material collected by this build.",
        "",
        "This file is generated locally. The authoritative source remains "
        "the original NHS websites.",
        "",
        f"Generated: {generated}",
        "",
        "## NHSBSA Digital Playbook",
        "",
    ]

    for page in pages:

        if page.site != (
            "nhsbsa-playbook"
        ):
            continue

        lines.append(
            f"- [{page.title or page.url}]"
            f"({page.url}): "
            "NHSBSA Playbook source"
        )

    lines.extend(
        [
            "",
            "## NHS England Digital Service Manual",
            "",
        ]
    )

    for page in pages:

        if page.site != (
            "nhs-service-manual"
        ):
            continue

        description = (
            "NHS Service Manual source"
        )

        if page.dos or page.donts:

            description += (
                "; contains explicit Do/Don't guidance"
            )

        lines.append(
            f"- [{page.title or page.url}]"
            f"({page.url}): "
            f"{description}"
        )

    return "\n".join(
        lines
    ) + "\n"


# ============================================================================
# Build
# ============================================================================

def build(
    output: Path,
    model: str,
    max_pages: int,
    no_llm: bool,
    force: bool,
) -> None:

    bundle = (
        output
        / "nhs-agent-knowledge"
    )

    if bundle.exists():

        if not force:

            raise RuntimeError(
                f"{bundle} exists. "
                "Use --force to replace it."
            )

        shutil.rmtree(
            bundle
        )

    bundle.mkdir(
        parents=True
    )

    # ------------------------------------------------------------------------
    # Crawl both sources
    # ------------------------------------------------------------------------

    all_pages = []
    all_llms = []

    for site_key, site in (
        SITES.items()
    ):

        pages, llms_files = crawl_site(
            site_key,
            site,
            max_pages,
        )

        all_pages.extend(
            pages
        )

        all_llms.extend(
            llms_files
        )

    # De-duplicate.
    unique_pages = {}

    for page in all_pages:

        unique_pages[
            page.url
        ] = page

    pages = list(
        unique_pages.values()
    )

    print()
    print(
        f"Total unique pages: {len(pages)}"
    )

    # ------------------------------------------------------------------------
    # Save raw source
    # ------------------------------------------------------------------------

    source_dir = (
        bundle
        / "source"
    )

    source_dir.mkdir()

    for index, page in enumerate(
        pages,
        start=1,
    ):

        digest = hashlib.sha1(
            page.url.encode(
                "utf-8"
            )
        ).hexdigest()[:10]

        slug = re.sub(
            r"[^a-zA-Z0-9]+",
            "-",
            urlparse(
                page.url
            ).path,
        ).strip("-")

        filename = (
            f"{index:04d}-"
            f"{slug[:90]}-"
            f"{digest}.md"
        )

        content = (
            f"# {page.title}\n\n"
            f"Source URL: {page.url}\n\n"
        )

        if page.dos:

            content += (
                "## Explicit Do guidance\n\n"
                + "\n".join(
                    f"- {item}"
                    for item in page.dos
                )
                + "\n\n"
            )

        if page.donts:

            content += (
                "## Explicit Don't guidance\n\n"
                + "\n".join(
                    f"- {item}"
                    for item in page.donts
                )
                + "\n\n"
            )

        content += (
            "## Source content\n\n"
            + page.content
            + "\n"
        )

        (
            source_dir
            / filename
        ).write_text(
            content,
            encoding="utf-8",
        )

    # ------------------------------------------------------------------------
    # Save llms.txt material
    # ------------------------------------------------------------------------

    llms_dir = (
        bundle
        / "llms"
    )

    llms_dir.mkdir()

    for index, (
        url,
        text,
    ) in enumerate(
        all_llms,
        start=1,
    ):

        (
            llms_dir
            / f"{index:02d}-llms.txt"
        ).write_text(
            f"Source: {url}\n\n"
            + text,
            encoding="utf-8",
        )

    generated = datetime.now(
        timezone.utc
    ).strftime(
        "%Y-%m-%d %H:%M UTC"
    )

    (
        llms_dir
        / "llms.txt"
    ).write_text(
        build_local_llms_txt(
            pages,
            generated,
        ),
        encoding="utf-8",
    )

    # ------------------------------------------------------------------------
    # Group skills
    # ------------------------------------------------------------------------

    grouped = group_pages(
        pages
    )

    print()
    print(
        "Skills:"
    )

    for skill, skill_pages in sorted(
        grouped.items()
    ):

        print(
            f"  {skill:30} "
            f"{len(skill_pages)} source pages"
        )

    # ------------------------------------------------------------------------
    # Ollama
    # ------------------------------------------------------------------------

    if not no_llm:

        print()
        print(
            f"Checking Ollama: {model}"
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

    manifest = {}

    for skill, skill_pages in sorted(
        grouped.items()
    ):

        print()
        print(
            f"Generating: {skill}"
        )

        skill_dir = (
            skills_dir
            / skill
        )

        skill_dir.mkdir(
            parents=True
        )

        if no_llm:

            content = (
                f"# {SKILLS[skill]}\n\n"
                "## Purpose\n\n"
                "Source-backed material is available "
                "in the references below.\n\n"
                "## Authoritative sources\n\n"
                + "\n".join(
                    f"- {p.url}"
                    for p in skill_pages
                )
                + "\n"
            )

        else:

            prompt = build_prompt(
                skill,
                skill_pages,
            )

            content = ollama(
                model,
                prompt,
            )

        errors = validate_skill(
            content,
            skill_pages,
        )

        if errors and not no_llm:

            print(
                "  Initial validation failed:"
            )

            for error in errors:

                print(
                    f"    - {error}"
                )

            print(
                "  Running corrective generation..."
            )

            correction = f"""
The generated SKILL.md failed validation.

Errors:

{chr(10).join(
    f"- {error}"
    for error in errors
)}

Regenerate the complete document.

You MUST preserve all source-backed requirements.

You MUST include every source URL.

You MUST include explicit:

## Do

## Don't

sections.

Return only the complete corrected Markdown.

SOURCE MATERIAL

{build_prompt(
    skill,
    skill_pages,
)}
"""

            content = ollama(
                model,
                correction,
            )

            errors = validate_skill(
                content,
                skill_pages,
            )

        (
            skill_dir
            / "SKILL.md"
        ).write_text(
            content.strip()
            + "\n",
            encoding="utf-8",
        )

        references = (
            skill_dir
            / "references.md"
        )

        reference_lines = [
            "# Authoritative References",
            "",
        ]

        for page in skill_pages:

            reference_lines.append(
                f"- [{page.title or page.url}]"
                f"({page.url})"
            )

            if page.markdown_url:

                reference_lines.append(
                    f"  - Markdown: "
                    f"{page.markdown_url}"
                )

        references.write_text(
            "\n".join(
                reference_lines
            )
            + "\n",
            encoding="utf-8",
        )

        manifest[skill] = {
            "source_pages": len(
                skill_pages
            ),
            "validation_errors": errors,
        }

    # ------------------------------------------------------------------------
    # Root documentation
    # ------------------------------------------------------------------------

    (
        bundle
        / "AGENTS.md"
    ).write_text(
        build_agents_md(
            grouped,
            generated,
        ),
        encoding="utf-8",
    )

    (
        bundle
        / "SOURCES.md"
    ).write_text(
        build_sources(
            pages,
            all_llms,
            generated,
        ),
        encoding="utf-8",
    )

    urls = "\n".join(
        sorted(
            page.url
            for page in pages
        )
    )

    digest = hashlib.sha256(
        urls.encode(
            "utf-8"
        )
    ).hexdigest()

    (
        bundle
        / "VERSION.md"
    ).write_text(
        f"""# Knowledge Pack Version

Generated: {generated}

HTML pages: {len(pages)}

llms.txt files discovered: {len(all_llms)}

Source URL manifest SHA-256:

`{digest}`

## Authority

The authoritative material remains the original:

- NHSBSA Digital Playbook:
  https://nhsbsa.github.io/nhsbsa-digital-playbook/

- NHS England Digital Service Manual:
  https://service-manual.nhs.uk/

Generated skills are derived guidance and must not override the original
source material.
""",
        encoding="utf-8",
    )

    (
        bundle
        / "GENERATION.json"
    ).write_text(
        json.dumps(
            {
                "generated": generated,
                "model": (
                    None
                    if no_llm
                    else model
                ),
                "ollama": (
                    None
                    if no_llm
                    else OLLAMA_URL
                ),
                "pages": len(
                    pages
                ),
                "llms_txt_files": len(
                    all_llms
                ),
                "skills": manifest,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    # ------------------------------------------------------------------------
    # ZIP
    # ------------------------------------------------------------------------

    zip_path = (
        output
        / "nhs-agent-knowledge.zip"
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
    print(
        "=" * 70
    )
    print(
        "BUILD COMPLETE"
    )
    print(
        "=" * 70
    )
    print()
    print(
        f"Directory: {bundle}"
    )
    print(
        f"ZIP:       {zip_path}"
    )
    print(
        f"Pages:     {len(pages)}"
    )
    print(
        f"llms.txt:  {len(all_llms)}"
    )
    print(
        f"Skills:    {len(grouped)}"
    )
    print()


# ============================================================================
# CLI
# ============================================================================

def main() -> int:

    parser = argparse.ArgumentParser(
        description=(
            "Build NHSBSA + NHS Service Manual "
            "agent knowledge pack."
        )
    )

    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=(
            "Ollama model "
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
        default=500,
        help=(
            "Maximum pages per site "
            "(default: 500)"
        ),
    )

    parser.add_argument(
        "--no-llm",
        action="store_true",
        help=(
            "Only crawl and extract sources; "
            "do not generate skills."
        ),
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help=(
            "Replace an existing build."
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
            no_llm=args.no_llm,
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
