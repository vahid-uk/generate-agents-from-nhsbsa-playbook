#!/usr/bin/env bash
set -euo pipefail

ROOT="nhsbsa-playbook-agents"

rm -rf "$ROOT"
mkdir -p "$ROOT/skills"

cat > "$ROOT/AGENTS.md" <<'EOF'
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
EOF

cat > "$ROOT/SOURCES.md" <<'EOF'
# Sources

Primary index:

https://nhsbsa.github.io/nhsbsa-digital-playbook/development/

Development pages:

- https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-style-guide/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-licences/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-securely/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-naming-conventions/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-logging/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/development/dev-tests/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-quality-assurance/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-peer-review/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/development/dev-git/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-apis/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-frontend/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/development/dev-documentation/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/development/dev-documentation-readme/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-securely-personal-data/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-secrets-detection/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-git-rewrite-history/

Technology pages:

- https://nhsbsa.github.io/nhsbsa-digital-playbook/technologies/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/technologies/tech-patching/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/technologies/tech-release-adoption-schedule/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/technologies/tech-java/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/technologies/tech-node/

Security pages:

- https://nhsbsa.github.io/nhsbsa-digital-playbook/security/security-headers/
- https://nhsbsa.github.io/nhsbsa-digital-playbook/security/content-security-policy/

Crawled: 25 September 2026.

This bundle intentionally summarises the guidance rather than reproducing
the source pages verbatim.
EOF

write_skill() {
  local name="$1"
  mkdir -p "$ROOT/skills/$name"
  cat > "$ROOT/skills/$name/SKILL.md"
}

write_skill style-guides <<'EOF'
# Style Guides

Apply a consistent language-specific style guide across the codebase.

- Prefer the applicable Google Style Guide for HTML/CSS, Java, JavaScript,
  Python, Bash, R and Ruby.
- Follow NHSBSA-specific standards where one exists.
- Prefer repository-wide consistency over applying formatting piecemeal.
- Configure the IDE and automated formatters where practical.
- If introducing a style standard into an existing codebase, treat the
  migration as a deliberate technical-debt task.
- Avoid mixing functional changes with large formatting-only changes.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-style-guide/
EOF

write_skill licensing <<'EOF'
# Licensing

Every produced or used software/code repository must have an appropriate
licence.

For NHSBSA code:

- Use Apache License 2.0.
- Include the full licence text in `LICENCE` or `LICENCE.md`.
- Use British spelling: `LICENCE`, not `LICENSE`.
- Include the Crown Copyright notice as appropriate.
- Put machine-readable licence metadata in project descriptors.
- NPM should use the SPDX `Apache-2.0` identifier.
- Published content uses Open Government Licence v3.
- User interfaces publishing OGL-covered content should link to the OGL v3
  agreement in the footer.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-licences/
EOF

write_skill coding <<'EOF'
# Coding

Write code that is understandable, maintainable and appropriately simple.

Apply:

- DRY where duplication represents the same concept.
- KISS: avoid unnecessary complexity.
- SOLID principles where they improve maintainability.
- Least privilege.
- Defensive/error-aware design.
- Appropriate software design patterns rather than patterns for their own sake.
- Clean-code practices.
- Refactoring when code smells identify maintainability problems.

Production applications should follow 12-factor principles where applicable:

- explicit dependencies
- environment-based configuration
- external backing services
- separated build/release/run stages
- stateless processes
- port binding
- process-based scaling
- fast startup and graceful shutdown
- development/production parity
- logs as event streams

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding/
EOF

write_skill secure-development <<'EOF'
# Secure Development

Security is a responsibility of everyone involved in development.

Before implementing production code:

- Consider security requirements explicitly.
- Follow NCSC secure-development principles.
- Understand OWASP Top 10 risks.
- Apply OWASP proactive controls.
- Validate all input.
- Encode/escape output appropriately.
- Use established security frameworks and libraries.
- Protect databases and other backing services.
- Implement appropriate identity and access controls.
- Protect data in transit and at rest.
- Implement useful security logging and monitoring.
- Handle errors and exceptions safely.
- Keep dependencies current.
- Do not commit secrets.
- Ensure repository and build/deployment controls are appropriate.

Relevant risks include broken access control, cryptographic failures,
injection, insecure design, security misconfiguration, vulnerable
dependencies, authentication failures, integrity failures, logging failures
and SSRF.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-securely/
EOF

write_skill naming-conventions <<'EOF'
# Naming Conventions

Names should communicate intent and allow related components to be grouped.

Use the NHSBSA naming model where applicable:

`{optional service-line}-{service}-{function}-{type}`

Typical component types include:

- `ui`
- `api`
- `lambda`
- `prototype`
- `poc`
- `config`
- `tf`

Test types include:

- `acceptance-test`
- `api-test`
- `accessibility-test`
- `performance-test`
- `security-test`
- `manual-test`

Use:

- `kebab-case` for repositories and branches where specified.
- `CamelCase` / `camelCase` according to language conventions.
- `snake_case` where the language/project requires it.
- Natural, unabbreviated names for externally visible repository names and
  public documentation.

Branches should use `main` for the production mainline and keep change
descriptions brief.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-naming-conventions/
EOF

write_skill logging <<'EOF'
# Logging

Log enough information to support:

- production troubleshooting
- application monitoring
- profiling
- security monitoring
- carefully controlled audit requirements
- operational management information

Rules:

- Do not log personal data unless there is a specific justified requirement.
- Never log secrets, passwords or credentials.
- Treat logs as operational event streams.
- Use appropriate log levels.
- Ensure security events are observable.
- Do not treat logs as the authoritative business data store.
- Review production logs before go-live.
- Review logs after releases for accidental sensitive-data leakage.
- Follow OWASP secure logging guidance and applicable NHSBSA monitoring
  standards.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-logging/
EOF

write_skill patching <<'EOF'
# Application Patching

Keep runtimes and dependencies current.

Requirements:

- Use a dependency management system.
- Declare dependency versions explicitly.
- Do not commit binaries into source control.
- Regularly update dependencies and runtimes.
- Treat patching as routine vulnerability management.
- Respond promptly to vulnerable dependencies.
- Keep framework/library APIs current where practical.

Approved dependency-management approaches documented by NHSBSA include:

- Java: Maven / `pom.xml`
- Node.js: NPM / `package.json`
- Python: Pip / `pyproject.toml`
- Ruby: Bundler / `Gemfile`

Use isolated environments for Python and Ruby dependencies.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/technologies/tech-patching/
EOF

write_skill release-adoption <<'EOF'
# Release Adoption

Use the NHSBSA release lifecycle:

1. PENDING — release exists but is not yet assessed.
2. ASSESS — understand migration impact and risks.
3. ADOPT — migrate according to the adoption schedule.
4. DEPRECATE — move away from the version.
5. DECOMMISSION — do not use; migration deadline has passed.

For Node.js:

- Use NVM during development.
- Commit an `.nvmrc` specifying the project Node version.
- Follow the Node.js release lifecycle.
- Adopt at the active-LTS stage unless an approved decision says otherwise.
- Do not remain on decommissioned versions.

Always check the current NHSBSA schedule before making a runtime-version
decision because the schedule changes over time.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/technologies/tech-release-adoption-schedule/
EOF

write_skill testing <<'EOF'
# Testing

Developers are responsible for testing the code they write.

At minimum:

- Unit test isolated functionality.
- Integration test functionality involving external resources.
- Test against dependencies representative of production.
- Use appropriate mocks for external APIs where necessary.
- Do not duplicate full-stack acceptance testing unnecessarily.

NHSBSA encourages Test Driven Development:

1. Red — write a failing test describing the next behaviour.
2. Green — implement only enough production code to pass.
3. Refactor — improve the implementation while keeping tests passing.

Keep tests focused and maintainable.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/dev-tests/
EOF

write_skill static-analysis <<'EOF'
# Static Code Analysis

Use SonarQube as the standard static-analysis quality gate where applicable.

Requirements:

- Run the applicable NHSBSA language quality profile.
- Treat BLOCKER and CRITICAL issues as release/build blockers.
- Maintain at least 80% test coverage where the NHSBSA quality gate applies.
- Address lower-severity issues rather than allowing technical debt to
  accumulate.
- Keep analysis integrated with CI rather than relying only on local checks.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-quality-assurance/
EOF

write_skill peer-review <<'EOF'
# Peer Review

Production-code peer review is mandatory under the NHSBSA guidance unless
an agreed exception exists.

Workflow:

1. Create a topic branch from `main`.
2. Make focused changes.
3. Push branches regularly.
4. Create a merge/pull request.
5. Have another developer review the change.
6. Address review comments.
7. Obtain approval.
8. Merge only after required checks pass.

Keep changes:

- small
- focused
- easy to understand
- free from unrelated formatting
- covered by appropriate tests

The build and quality checks must pass before approval.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-peer-review/
EOF

write_skill git <<'EOF'
# Git

Git conventions must be documented by the project.

Core rules:

- `main` represents production.
- Document the project's branching strategy and controls.
- Record deviations from standard approaches as decisions with rationale.
- Prefer logical, focused commits.
- Avoid mixing unrelated changes.
- Push work regularly.
- Use merge requests/pull requests for review.
- Use rebasing and force pushes cautiously.
- Never rewrite shared history without following the dedicated history-rewrite
  process.
- Keep secrets and personal data out of Git.

Use the repository's documented branching strategy consistently.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/dev-git/
EOF

write_skill apis <<'EOF'
# APIs

Follow UK Government API technical/data standards and API design guidance.

When designing or changing an API:

- use clear resource and operation semantics
- define and document request/response contracts
- consider validation and error behaviour
- consider backwards compatibility
- protect authentication and authorisation boundaries
- avoid exposing unnecessary data
- document API behaviour for consumers

Authoritative references:

https://www.gov.uk/guidance/gds-api-technical-and-data-standards
https://www.gov.uk/guidance/gds-api-design-guidance

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-apis/
EOF

write_skill frontends <<'EOF'
# Frontends

Accessibility is a fundamental frontend requirement.

Use:

- semantic HTML
- appropriate ARIA for interactive controls
- progressive enhancement
- interfaces that remain useful without unnecessary client-side JavaScript
- NHS Design System and NHS frontend packages where appropriate
- Government Design System where Government branding/patterns are required

Prefer established, user-tested NHS/Government patterns.

If a new pattern is genuinely required:

- validate it through user research/testing
- document why the standard pattern is insufficient
- feed successful patterns back into the relevant design system/package.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-frontend/
EOF

write_skill repository-files <<'EOF'
# Standard Repository Files

Repositories should maintain a minimum documentation baseline.

Mandatory files include:

- `README.md`
- `CODE_OF_CONDUCT.md`
- `CONTRIBUTING.MD`
- `LICENCE.txt`
- `SECURITY.md`
- `SECRETS.md`

Common optional file:

- `CHANGELOG.md`

The README should explain the repository purpose and how to build, run and
use it.

Use Apache 2.0 for code and OGL v3 for applicable published content.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/dev-documentation/
EOF

write_skill readmes <<'EOF'
# README Files

A repository README should allow a new developer or operator to understand
the project without relying on tribal knowledge.

At minimum document:

- what the project does
- why it exists
- prerequisites
- how to install dependencies
- how to build
- how to run locally
- how to test
- configuration requirements
- deployment/use information where relevant
- links to deeper documentation
- contribution information where appropriate

Keep instructions accurate and update them when development workflows change.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/dev-documentation-readme/
EOF

write_skill technologies <<'EOF'
# Technologies

Use the NHSBSA technology landscape as the default reference when choosing
technology.

Documented technologies include:

- Java / Spring
- Node.js / JavaScript / TypeScript
- Python, currently subject to assessment/approval for some uses
- PostgreSQL / AWS RDS
- DynamoDB
- Redis
- AWS
- Azure
- legacy WebSphere and Oracle estates

Prefer existing organisational capability and established platform patterns
over introducing unnecessary technology.

For runtime versions, also consult `release-adoption/SKILL.md`.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/technologies/
EOF

write_skill java <<'EOF'
# Java

Java is a core NHSBSA language.

Where applicable:

- use Spring Boot for standalone applications
- use Spring MVC for web applications and REST services
- use Spring Data JPA for ORM/data access
- use Spring Integration and Spring Batch where appropriate
- manage dependencies using Maven and `pom.xml`
- follow the applicable Java style guide
- keep Java runtime versions aligned with the current release-adoption schedule

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/technologies/tech-java/
EOF

write_skill nodejs <<'EOF'
# Node.js

Node.js is used extensively for newer frontends and Lambda implementations.

Requirements:

- use NVM for development
- commit `.nvmrc`
- use NPM/package.json for dependency management
- use JavaScript or TypeScript consistently with the project
- keep Node versions aligned with the current NHSBSA release-adoption schedule
- use NHS/Government frontend packages for applicable frontend work
- do not commit generated dependency binaries into source control

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/technologies/tech-node/
EOF

write_skill personal-data <<'EOF'
# Coding With Personal Data

Minimise personal data.

Before storing or transmitting personal data, ask:

1. Is the data genuinely required?
2. Is it being sent to an authorised location?
3. Is it protected in transit and storage?
4. Is it being used for the stated/intended purpose?
5. Is its retention period defined?

Never casually put personal data into:

- logs
- URLs
- analytics systems
- source code
- test fixtures
- error messages

Pay particular attention to NHS numbers, identifiers, contact details,
location information, health information and other potentially identifying
combinations.

Do not log personal data simply because debug logging is convenient.

Ensure stored data is deleted according to the applicable retention schedule,
including abandoned/incomplete application data.

Use anonymisation or pseudonymisation deliberately and understand the
difference between the two.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-securely-personal-data/
EOF

write_skill secrets-detection <<'EOF'
# Secrets Detection

Never commit secrets to source control.

Treat as secrets, where applicable:

- passwords
- API keys
- credentials
- SSH keys
- client certificates
- encryption keys
- CI/CD credentials
- sensitive internal infrastructure details

Use:

- Gitleaks
- NHSBSA Gitleaks configuration
- pre-commit hooks
- GitLab secret detection

If a secret is committed:

1. Treat it as compromised.
2. Revoke/rotate it immediately.
3. Raise the required security incident.
4. Assess impact.
5. Only then consider whether Git history must be rewritten.

False positives must be handled through the documented Gitleaks mechanisms.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-secrets-detection/
EOF

write_skill git-history-rewrite <<'EOF'
# Git History Rewriting

Destructive history rewriting is exceptional and must be carefully controlled.

Before rewriting shared history:

- consult the professional lead
- consult Information Security/Security Operations
- assess all affected branches
- communicate with contributors and affected parties
- raise the required security incident where applicable
- create a safe backup
- script the rewrite
- peer review the script
- perform a dry run on a fresh clone
- verify the resulting history
- force-push all required branches and tags only when authorised
- require contributors to re-clone after the production rewrite

Use `git-filter-repo` for history rewriting.

Do not use obsolete `git filter-branch` or BFG for this process.

Do not use this procedure for normal topic-branch squashing or rebasing.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-git-rewrite-history/
EOF

write_skill security-headers <<'EOF'
# Security Headers

Use HTTP response security headers to reduce common browser-side security
risks.

When changing headers:

- understand the security purpose of each header
- avoid weakening existing protections without documented justification
- test headers in the actual deployment environment
- consider browser compatibility
- coordinate header changes with CSP and frontend behaviour
- do not treat headers as a substitute for secure application design

Refer to the authoritative NHSBSA security-headers guidance for the current
required header set and values.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/security/security-headers/
EOF

write_skill content-security-policy <<'EOF'
# Content Security Policy

Use Content Security Policy (CSP) as a modern browser-side defence.

When implementing CSP:

- start from the application's actual resource requirements
- minimise allowed sources
- avoid unnecessarily broad directives
- understand scripts, styles, images, fonts, frames and connections used
- test CSP against every supported user journey
- avoid weakening CSP simply to make third-party scripts work
- review CSP whenever frontend dependencies or external services change

CSP should complement, not replace, secure server-side controls, input
validation, output encoding and appropriate authentication/authorisation.

Refer to the authoritative NHSBSA CSP guidance for the current policy and
deployment approach.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/security/content-security-policy/
EOF

echo
echo "Created $ROOT/"
echo
find "$ROOT" -type f | sort
echo
echo "To create the ZIP:"
echo "  zip -r ${ROOT}.zip ${ROOT}"

