# AGENTS.md

# NHS Agent Engineering Guidance

This repository contains an agent-oriented knowledge pack derived from the NHSBSA Digital Playbook and NHS England Digital Service Manual.

## Source hierarchy

Use the original NHS source pages as authoritative.

Generated skills are structured interpretations of those sources.
If a generated skill conflicts with an authoritative source, the authoritative source wins.

## Before changing code

The agent MUST:

1. Identify the type of change.
2. Load all relevant skills.
3. Read the complete applicable SKILL.md files.
4. Inspect the existing implementation.
5. Follow mandatory NHS requirements.
6. Apply applicable design-system components and patterns.
7. Check accessibility requirements.
8. Check security and personal-data implications.
9. Add or update tests.
10. Run applicable quality gates.
11. Review the final change against the skill completion checklist.

## Design-system rule

When building an NHS user interface, first check whether the NHS design system already provides a suitable style, component or pattern.

Do not create a bespoke solution merely because it is convenient.

## Component rule

Before implementing a UI component:

- check `skills/components/SKILL.md`
- check `skills/design-system/SKILL.md`
- check `skills/accessibility/SKILL.md`
- check the relevant component source page

## Pattern rule

Before implementing a recurring user journey or interaction:

- check `skills/patterns/SKILL.md`
- check relevant component skills
- check accessibility guidance

## Do / Don't rule

Do not treat generated generic advice as NHS policy.
Use the explicit Do and Don't guidance extracted from the NHS Service Manual and NHSBSA Playbook.

## Accessibility rule

Accessibility is not an optional enhancement. Any user-interface change must consider the applicable NHS accessibility guidance.

Load:

`skills/accessibility/SKILL.md`

for UI changes.

## Security rule

Security-sensitive changes must load:

`skills/secure-development/SKILL.md`

and any relevant specialist security skills.

## Personal-data rule

If a change handles personal data, load:

`skills/personal-data/SKILL.md`

## Dependency rule

Before changing dependencies or runtime versions, load:

- `skills/patching/SKILL.md`
- `skills/release-adoption/SKILL.md`

## Git rule

Never rewrite shared history unless the specific Git-history guidance applies.

## Review rule

Follow the peer-review guidance for production changes.

## Skill catalogue

- `coding` — Coding and engineering practices — `skills/coding/SKILL.md`
- `components` — NHS design system components — `skills/components/SKILL.md`
- `design-principles` — NHS design principles — `skills/design-principles/SKILL.md`
- `design-system` — NHS design system — `skills/design-system/SKILL.md`
- `dos-and-donts` — Do and Don't guidance — `skills/dos-and-donts/SKILL.md`
- `patterns` — NHS design system patterns — `skills/patterns/SKILL.md`
- `production-frontend` — Production frontend implementation — `skills/production-frontend/SKILL.md`
- `prototyping` — Prototyping — `skills/prototyping/SKILL.md`

## Sources

- `SOURCES.md` — complete source manifest
- `source/` — crawled source material
- `llms/` — llms.txt-derived navigation material

Generated: 2026-09-28 13:37 UTC
