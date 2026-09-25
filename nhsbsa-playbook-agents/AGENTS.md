# AGENTS.md — NHSBSA Digital, Data and Technology

This repository follows the engineering guidance published in the
NHS Business Services Authority Digital, Data and Technology Playbook.

Before making changes, identify which of the skills below apply and read
the corresponding `SKILL.md` files.

## Skills

### Code and design
- `skills/style-guides/SKILL.md` — language and repository code style
- `skills/coding/SKILL.md` — coding principles, clean code and application design
- `skills/naming-conventions/SKILL.md` — names, casing, repositories and branches
- `skills/technologies/SKILL.md` — supported languages, frameworks and platforms
- `skills/java/SKILL.md` — Java and Spring guidance
- `skills/nodejs/SKILL.md` — Node.js and JavaScript/TypeScript guidance

### Security and data
- `skills/secure-development/SKILL.md` — secure development baseline
- `skills/personal-data/SKILL.md` — handling personal and confidential data
- `skills/secrets-detection/SKILL.md` — detecting and handling secrets
- `skills/git-history-rewrite/SKILL.md` — controlled destructive Git history rewrites
- `skills/security-headers/SKILL.md` — HTTP security headers
- `skills/content-security-policy/SKILL.md` — CSP
- `skills/logging/SKILL.md` — application logging and monitoring

### Quality and delivery
- `skills/testing/SKILL.md` — unit, integration and TDD
- `skills/static-analysis/SKILL.md` — SonarQube and quality gates
- `skills/peer-review/SKILL.md` — mandatory peer review
- `skills/git/SKILL.md` — Git workflow and branching
- `skills/apis/SKILL.md` — API standards
- `skills/frontends/SKILL.md` — frontend accessibility and design systems
- `skills/repository-files/SKILL.md` — mandatory repository documentation
- `skills/readmes/SKILL.md` — README structure and content

### Dependencies and releases
- `skills/patching/SKILL.md` — dependency management and application patching
- `skills/release-adoption/SKILL.md` — runtime/framework release adoption

### Licensing
- `skills/licensing/SKILL.md` — Apache 2 and OGL v3 licensing

## General agent behaviour

1. Prefer the smallest change that solves the problem.
2. Follow the existing repository conventions where they are consistent with
   these standards.
3. Do not introduce unnecessary dependencies.
4. Never commit secrets, credentials, personal data or generated binaries.
5. Add or update automated tests for behavioural changes.
6. Run applicable quality checks before considering work complete.
7. Changes to production code must go through peer review.
8. Keep documentation and repository metadata current.
9. For security-sensitive work, consult the relevant security skill before
   making changes.
10. When this guidance conflicts with a project-specific approved decision,
    follow the approved project decision and document the deviation.

## Source

NHSBSA Digital, Data and Technology Playbook:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/

The skills in this directory are concise agent-oriented interpretations of
the source guidance. They are not replacements for the authoritative
NHSBSA pages.
