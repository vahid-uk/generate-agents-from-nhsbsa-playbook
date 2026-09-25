#!/usr/bin/env python3
"""
Build an agent-oriented NHSBSA Digital Playbook knowledge pack.

Usage:

    python3 build-nhsbsa-agents.py

Optional:

    python3 build-nhsbsa-agents.py --output ./output
    python3 build-nhsbsa-agents.py --max-pages 200

Requirements:

    pip install requests beautifulsoup4

Output:

    nhsbsa-playbook-agents/
    nhsbsa-playbook-agents.zip
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import sys
import time
import zipfile
from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse, urldefrag

import requests
from bs4 import BeautifulSoup


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ROOT_URL = "https://nhsbsa.github.io/nhsbsa-digital-playbook/development/"

SITE_HOST = "nhsbsa.github.io"
PLAYBOOK_PREFIX = "/nhsbsa-digital-playbook/"

USER_AGENT = (
    "nhsbsa-playbook-agent-builder/1.0 "
    "(documentation crawler; respectful crawl)"
)

DEFAULT_MAX_PAGES = 250
REQUEST_DELAY = 0.25
REQUEST_TIMEOUT = 30


# ---------------------------------------------------------------------------
# Skill classification
# ---------------------------------------------------------------------------

SKILL_RULES = [
    (
        "secure-development",
        [
            "coding-securely",
            "secure-development",
            "security",
        ],
    ),
    (
        "personal-data",
        [
            "personal-data",
            "personal",
        ],
    ),
    (
        "secrets-detection",
        [
            "secrets-detection",
            "secrets",
        ],
    ),
    (
        "git-history-rewrite",
        [
            "git-rewrite-history",
            "rewrite-history",
        ],
    ),
    (
        "security-headers",
        [
            "security-headers",
        ],
    ),
    (
        "content-security-policy",
        [
            "content-security-policy",
            "content-security",
        ],
    ),
    (
        "style-guides",
        [
            "coding-style-guide",
            "style-guide",
        ],
    ),
    (
        "licensing",
        [
            "coding-licences",
            "licences",
            "licensing",
        ],
    ),
    (
        "coding",
        [
            "/development/coding/",
            "/development/coding",
        ],
    ),
    (
        "naming-conventions",
        [
            "coding-naming-conventions",
            "naming-conventions",
        ],
    ),
    (
        "logging",
        [
            "coding-logging",
            "logging",
        ],
    ),
    (
        "testing",
        [
            "dev-tests",
            "testing",
        ],
    ),
    (
        "static-analysis",
        [
            "coding-quality-assurance",
            "quality-assurance",
            "static-analysis",
            "sonarqube",
        ],
    ),
    (
        "peer-review",
        [
            "coding-peer-review",
            "peer-review",
        ],
    ),
    (
        "git",
        [
            "dev-git",
            "/development/git",
        ],
    ),
    (
        "apis",
        [
            "coding-apis",
            "/development/apis",
            "api",
        ],
    ),
    (
        "frontends",
        [
            "coding-frontend",
            "frontend",
            "front-end",
        ],
    ),
    (
        "repository-files",
        [
            "dev-documentation",
            "repository",
            "documentation",
        ],
    ),
    (
        "readmes",
        [
            "dev-documentation-readme",
            "readme",
        ],
    ),
    (
        "patching",
        [
            "tech-patching",
            "patching",
        ],
    ),
    (
        "release-adoption",
        [
            "tech-release-adoption",
            "release-adoption",
        ],
    ),
    (
        "java",
        [
            "tech-java",
            "/technologies/java",
        ],
    ),
    (
        "nodejs",
        [
            "tech-node",
            "node-js",
            "nodejs",
        ],
    ),
    (
        "technologies",
        [
            "/technologies/",
            "/technologies",
        ],
    ),
]


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Page:
    url: str
    title: str
    headings: list[str]
    paragraphs: list[str]
    links: list[str]
    text: str


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

session = requests.Session()
session.headers.update({"User-Agent": USER_AGENT})


def fetch(url: str) -> str:
    response = session.get(
        url,
        timeout=REQUEST_TIMEOUT,
        allow_redirects=True,
    )

    response.raise_for_status()

    content_type = response.headers.get("content-type", "")
    if "text/html" not in content_type:
        raise ValueError(f"Not HTML: {content_type}")

    return response.text


# ---------------------------------------------------------------------------
# URL handling
# ---------------------------------------------------------------------------

def normalise_url(url: str) -> str | None:
    url, _fragment = urldefrag(url)

    parsed = urlparse(url)

    if parsed.scheme not in {"http", "https"}:
        return None

    if parsed.netloc != SITE_HOST:
        return None

    if not parsed.path.startswith(PLAYBOOK_PREFIX):
        return None

    # Ignore downloads and other non-page resources.
    ignored_extensions = {
        ".pdf",
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".svg",
        ".zip",
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
    }

    lower_path = parsed.path.lower()

    if any(lower_path.endswith(ext) for ext in ignored_extensions):
        return None

    # Normalise trailing slash.
    if not parsed.path.endswith("/"):
        path = parsed.path + "/"
    else:
        path = parsed.path

    return f"https://{parsed.netloc}{path}"


def is_internal_playbook_url(url: str) -> bool:
    return normalise_url(url) is not None


# ---------------------------------------------------------------------------
# HTML extraction
# ---------------------------------------------------------------------------

def clean_text(value: str) -> str:
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def parse_page(url: str, html: str) -> Page:
    soup = BeautifulSoup(html, "html.parser")

    for element in soup(
        [
            "script",
            "style",
            "noscript",
            "svg",
            "nav",
            "footer",
        ]
    ):
        element.decompose()

    title = ""

    if soup.title:
        title = clean_text(soup.title.get_text(" ", strip=True))

    headings = []

    for tag in soup.find_all(["h1", "h2", "h3", "h4"]):
        text = clean_text(tag.get_text(" ", strip=True))
        if text:
            headings.append(text)

    paragraphs = []

    for tag in soup.find_all(["p", "li"]):
        text = clean_text(tag.get_text(" ", strip=True))

        if not text:
            continue

        if len(text) < 20:
            continue

        paragraphs.append(text)

    links = []

    for anchor in soup.find_all("a", href=True):
        absolute = urljoin(url, anchor["href"])
        normalised = normalise_url(absolute)

        if normalised:
            links.append(normalised)

    # De-duplicate while retaining order.
    headings = list(dict.fromkeys(headings))
    paragraphs = list(dict.fromkeys(paragraphs))
    links = list(dict.fromkeys(links))

    body_text = "\n".join(paragraphs)

    return Page(
        url=url,
        title=title,
        headings=headings,
        paragraphs=paragraphs,
        links=links,
        text=body_text,
    )


# ---------------------------------------------------------------------------
# Crawling
# ---------------------------------------------------------------------------

def crawl(start_url: str, max_pages: int) -> list[Page]:
    queue = deque([normalise_url(start_url)])
    visited: set[str] = set()
    pages: list[Page] = []

    print()
    print("NHSBSA Playbook crawler")
    print("=======================")
    print(f"Starting URL: {start_url}")
    print(f"Maximum pages: {max_pages}")
    print()

    while queue and len(pages) < max_pages:
        url = queue.popleft()

        if not url:
            continue

        if url in visited:
            continue

        visited.add(url)

        print(f"[{len(pages) + 1:03d}] {url}")

        try:
            html = fetch(url)
            page = parse_page(url, html)
            pages.append(page)

            for link in page.links:
                if link not in visited:
                    queue.append(link)

        except Exception as exc:
            print(f"      WARNING: {exc}")

        time.sleep(REQUEST_DELAY)

    print()
    print(f"Crawled {len(pages)} pages.")

    return pages


# ---------------------------------------------------------------------------
# Skill classification
# ---------------------------------------------------------------------------

def classify_page(page: Page) -> str | None:
    url = page.url.lower()

    # Most specific rules first.
    for skill, patterns in SKILL_RULES:
        for pattern in patterns:
            if pattern in url:
                return skill

    title = page.title.lower()

    for skill, patterns in SKILL_RULES:
        for pattern in patterns:
            if pattern.replace("-", " ") in title:
                return skill

    return None


def group_pages(pages: list[Page]) -> dict[str, list[Page]]:
    grouped: dict[str, list[Page]] = {}

    for page in pages:
        skill = classify_page(page)

        if not skill:
            continue

        grouped.setdefault(skill, []).append(page)

    return grouped


# ---------------------------------------------------------------------------
# Agent guidance
# ---------------------------------------------------------------------------

GENERAL_AGENT_RULES = """
## Agent operating principles

The NHSBSA Playbook should be treated as engineering policy and guidance,
not merely as background documentation.

When a task matches this skill:

1. Read this entire skill before implementing the change.
2. Inspect the existing repository for local conventions.
3. Identify any related NHSBSA skills listed below.
4. Prefer existing approved patterns over introducing new technology.
5. Make the smallest coherent change.
6. Add or update tests for behavioural changes.
7. Run the applicable quality and security checks.
8. Do not bypass security, testing, review or release controls for convenience.
9. Record material deviations from the guidance.
10. Consult the authoritative source when this document is ambiguous or
    when the source contains time-sensitive information.
"""


SKILL_RELATIONSHIPS = {
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
    "security-headers": [
        "secure-development",
        "content-security-policy",
        "frontends",
    ],
    "content-security-policy": [
        "secure-development",
        "security-headers",
        "frontends",
    ],
    "coding": [
        "style-guides",
        "naming-conventions",
        "testing",
        "secure-development",
        "peer-review",
    ],
    "testing": [
        "coding",
        "static-analysis",
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
        "secure-development",
        "technologies",
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


def slug_to_title(slug: str) -> str:
    return slug.replace("-", " ").title()


def source_summary(page: Page) -> str:
    """
    Generate a useful, non-verbatim description from the page's structure.

    We deliberately don't copy the complete source page into the generated
    skill. The skill points the agent at the authoritative source.
    """

    sections = page.headings[:30]

    if not sections:
        return (
            "The source page does not expose a useful heading structure. "
            "Consult the authoritative source directly."
        )

    lines = [
        "The authoritative NHSBSA page covers the following subjects:",
        "",
    ]

    for heading in sections:
        lines.append(f"- {heading}")

    return "\n".join(lines)


def generate_skill(
    skill_name: str,
    pages: list[Page],
    crawl_date: str,
) -> str:
    primary = pages[0]

    related = SKILL_RELATIONSHIPS.get(skill_name, [])

    lines = []

    lines.append(f"# {slug_to_title(skill_name)}")
    lines.append("")
    lines.append(
        "This skill provides agent-oriented guidance derived from the "
        "NHSBSA Digital, Data and Technology Playbook."
    )
    lines.append("")

    lines.append("## When this skill applies")
    lines.append("")

    lines.append(
        f"Load this skill whenever a task involves "
        f"**{slug_to_title(skill_name).lower()}**."
    )
    lines.append("")

    lines.append(GENERAL_AGENT_RULES.strip())
    lines.append("")

    lines.append("## NHSBSA source coverage")
    lines.append("")
    lines.append(source_summary(primary))
    lines.append("")

    if len(pages) > 1:
        lines.append(
            "Additional pages discovered for this skill:"
        )
        lines.append("")

        for page in pages[1:]:
            lines.append(f"- {page.url}")

        lines.append("")

    lines.append("## Applying the guidance")
    lines.append("")

    lines.append(
        "Use the source headings above to determine which part of the "
        "Playbook applies to the current task. Do not infer that a heading "
        "is optional merely because it is not reproduced in this local "
        "summary."
    )
    lines.append("")

    lines.append(
        "Where the source defines a mandatory requirement, follow it unless "
        "an explicit NHSBSA-approved exception applies."
    )
    lines.append("")

    lines.append(
        "Where the source provides recommendations rather than mandatory "
        "requirements, consider the recommendation in the context of the "
        "repository, architecture, security requirements and delivery "
        "constraints."
    )
    lines.append("")

    lines.append("## Agent decision checklist")
    lines.append("")
    lines.append("- [ ] I read this skill before making the change.")
    lines.append("- [ ] I identified related NHSBSA skills.")
    lines.append("- [ ] I checked the existing repository conventions.")
    lines.append("- [ ] I considered security implications.")
    lines.append("- [ ] I considered personal-data implications.")
    lines.append("- [ ] I considered dependency/runtime implications.")
    lines.append("- [ ] I added or updated appropriate tests.")
    lines.append("- [ ] I ran applicable quality checks.")
    lines.append("- [ ] I have not introduced secrets.")
    lines.append("- [ ] I have not bypassed peer review or required quality gates.")
    lines.append("- [ ] I checked the authoritative source where necessary.")
    lines.append("")

    if related:
        lines.append("## Related skills")
        lines.append("")

        for skill in related:
            lines.append(f"- `../{skill}/SKILL.md`")

        lines.append("")

    lines.append("## Authoritative sources")
    lines.append("")

    for page in pages:
        lines.append(f"- {page.url}")

    lines.append("")

    lines.append("## Source status")
    lines.append("")
    lines.append(f"- Crawled: {crawl_date}")
    lines.append("- Source: NHSBSA Digital, Data and Technology Playbook")
    lines.append(
        "- This file is an agent-oriented interpretation and is not a "
        "replacement for the authoritative NHSBSA documentation."
    )
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Root AGENTS.md
# ---------------------------------------------------------------------------

def generate_agents(skill_names: list[str], crawl_date: str) -> str:
    lines = []

    lines.append("# AGENTS.md — NHSBSA Engineering Guidance")
    lines.append("")
    lines.append(
        "This repository contains an agent-oriented knowledge pack derived "
        "from the NHSBSA Digital, Data and Technology Playbook."
    )
    lines.append("")
    lines.append(
        "Authoritative source:"
    )
    lines.append(
        "https://nhsbsa.github.io/nhsbsa-digital-playbook/"
    )
    lines.append("")

    lines.append("## Mandatory agent behaviour")
    lines.append("")
    lines.append(
        "Before making a change, identify and read every applicable "
        "`skills/*/SKILL.md`."
    )
    lines.append("")
    lines.append(
        "Do not treat the absence of a skill as permission to ignore NHSBSA "
        "guidance. Consult the authoritative Playbook when required."
    )
    lines.append("")

    lines.append("## Always consider")
    lines.append("")
    lines.append("- coding")
    lines.append("- style-guides")
    lines.append("- testing")
    lines.append("- peer-review")
    lines.append("- git")
    lines.append("")

    lines.append("## Skill catalogue")
    lines.append("")

    for skill in sorted(skill_names):
        lines.append(f"- `skills/{skill}/SKILL.md`")

    lines.append("")

    lines.append("## Security")
    lines.append("")
    lines.append(
        "Security requirements take precedence over convenience. For "
        "security-sensitive work load `secure-development` and all relevant "
        "specialist security skills."
    )
    lines.append("")

    lines.append("## Personal data")
    lines.append("")
    lines.append(
        "Do not introduce personal data into source code, tests, URLs or "
        "logs without a justified and approved requirement."
    )
    lines.append("")

    lines.append("## Secrets")
    lines.append("")
    lines.append(
        "Never commit secrets. Load `secrets-detection` when credentials, "
        "keys, tokens or other secrets are involved."
    )
    lines.append("")

    lines.append("## Dependencies and runtimes")
    lines.append("")
    lines.append(
        "Load `patching` and `release-adoption` before making dependency or "
        "runtime-version decisions."
    )
    lines.append("")
    lines.append(
        "Runtime information is time-sensitive. Always consult the current "
        "NHSBSA release-adoption schedule."
    )
    lines.append("")

    lines.append("## Git")
    lines.append("")
    lines.append(
        "Production changes should follow the documented topic-branch and "
        "peer-review workflow. History rewriting is exceptional and must "
        "follow `git-history-rewrite`."
    )
    lines.append("")

    lines.append("## Quality")
    lines.append("")
    lines.append(
        "Do not declare work complete until applicable tests, static "
        "analysis and other project quality gates have passed."
    )
    lines.append("")

    lines.append("## Currentness")
    lines.append("")
    lines.append(
        f"This knowledge pack was generated on {crawl_date}."
    )
    lines.append("")
    lines.append(
        "The NHSBSA Playbook is authoritative. Some pages may have review "
        "dates in the past; that does not by itself invalidate published "
        "guidance."
    )
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# SOURCES.md
# ---------------------------------------------------------------------------

def generate_sources(
    pages: list[Page],
    grouped: dict[str, list[Page]],
    crawl_date: str,
) -> str:
    lines = []

    lines.append("# NHSBSA Playbook Sources")
    lines.append("")
    lines.append(f"Crawl date: {crawl_date}")
    lines.append("")
    lines.append(
        f"Total HTML pages crawled: {len(pages)}"
    )
    lines.append("")

    lines.append("## Skill mapping")
    lines.append("")

    for skill in sorted(grouped):
        lines.append(f"### {skill}")
        lines.append("")

        for page in grouped[skill]:
            lines.append(f"- {page.url}")

        lines.append("")

    lines.append("## All crawled pages")
    lines.append("")

    for page in sorted(pages, key=lambda item: item.url):
        lines.append(f"- {page.url}")

    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# VERSION.md
# ---------------------------------------------------------------------------

def generate_version(
    pages: list[Page],
    crawl_date: str,
) -> str:
    digest_input = "\n".join(
        sorted(page.url for page in pages)
    )

    digest = hashlib.sha256(
        digest_input.encode("utf-8")
    ).hexdigest()

    return f"""# Knowledge Pack Version

Generated: {crawl_date}

Pages crawled: {len(pages)}

URL manifest SHA-256:

`{digest}`

## Important

This pack is a generated derivative of the NHSBSA Digital, Data and
Technology Playbook.

The authoritative documentation remains:

https://nhsbsa.github.io/nhsbsa-digital-playbook/

Regenerate this pack periodically so that changes to the Playbook can be
identified.
"""


# ---------------------------------------------------------------------------
# Write files
# ---------------------------------------------------------------------------

def write_bundle(
    output_dir: Path,
    pages: list[Page],
    grouped: dict[str, list[Page]],
    crawl_date: str,
) -> Path:
    bundle = output_dir / "nhsbsa-playbook-agents"

    if bundle.exists():
        shutil.rmtree(bundle)

    skills_dir = bundle / "skills"
    skills_dir.mkdir(parents=True)

    skill_names = sorted(grouped.keys())

    (bundle / "AGENTS.md").write_text(
        generate_agents(skill_names, crawl_date),
        encoding="utf-8",
    )

    (bundle / "SOURCES.md").write_text(
        generate_sources(pages, grouped, crawl_date),
        encoding="utf-8",
    )

    (bundle / "VERSION.md").write_text(
        generate_version(pages, crawl_date),
        encoding="utf-8",
    )

    playbook = """# NHSBSA Digital and Technology Playbook

The NHSBSA Digital, Data and Technology Playbook is the authoritative source
for this knowledge pack.

https://nhsbsa.github.io/nhsbsa-digital-playbook/

The `skills/` directory contains agent-oriented guidance organised by subject.

Use `AGENTS.md` to determine which skills apply to a task.

Do not assume that this generated pack supersedes the authoritative NHSBSA
documentation. Where the local skill is ambiguous, consult the source page.
"""

    (bundle / "PLAYBOOK.md").write_text(
        playbook,
        encoding="utf-8",
    )

    for skill, skill_pages in sorted(grouped.items()):
        skill_dir = skills_dir / skill
        skill_dir.mkdir(parents=True)

        skill_file = skill_dir / "SKILL.md"

        skill_file.write_text(
            generate_skill(
                skill,
                skill_pages,
                crawl_date,
            ),
            encoding="utf-8",
        )

        references = skill_dir / "references.md"

        references.write_text(
            "# Authoritative References\n\n"
            + "\n".join(
                f"- {page.url}"
                for page in skill_pages
            )
            + "\n",
            encoding="utf-8",
        )

    return bundle


# ---------------------------------------------------------------------------
# ZIP
# ---------------------------------------------------------------------------

def create_zip(bundle: Path) -> Path:
    zip_path = bundle.parent / f"{bundle.name}.zip"

    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(
        zip_path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
    ) as archive:

        for file in bundle.rglob("*"):
            if not file.is_file():
                continue

            archive.write(
                file,
                file.relative_to(bundle.parent),
            )

    return zip_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build an NHSBSA Playbook agent knowledge pack."
    )

    parser.add_argument(
        "--output",
        default=".",
        help="Directory in which to create the bundle.",
    )

    parser.add_argument(
        "--max-pages",
        type=int,
        default=DEFAULT_MAX_PAGES,
        help="Maximum number of pages to crawl.",
    )

    args = parser.parse_args()

    output_dir = Path(args.output).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    crawl_date = datetime.now(
        timezone.utc
    ).strftime("%Y-%m-%d %H:%M UTC")

    try:
        pages = crawl(
            ROOT_URL,
            args.max_pages,
        )
    except KeyboardInterrupt:
        print("\nCrawl interrupted.")
        return 1

    if not pages:
        print("No pages were successfully crawled.")
        return 1

    grouped = group_pages(pages)

    print()
    print("Skills discovered")
    print("=================")

    for skill, skill_pages in sorted(grouped.items()):
        print(
            f"{skill:30} {len(skill_pages)} source page(s)"
        )

    print()

    bundle = write_bundle(
        output_dir,
        pages,
        grouped,
        crawl_date,
    )

    zip_path = create_zip(bundle)

    print("Build complete")
    print("==============")
    print()
    print(f"Bundle: {bundle}")
    print(f"ZIP:    {zip_path}")
    print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
