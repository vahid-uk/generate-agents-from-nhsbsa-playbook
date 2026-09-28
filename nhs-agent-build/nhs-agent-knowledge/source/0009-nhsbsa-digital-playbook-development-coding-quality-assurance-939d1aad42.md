# Static code analysis - NHSBSA Digital, Data and Technology Playbook - NHSBSA

Source URL: https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-quality-assurance/

## Source content

## Contents

- SonarQube

- Thresholds

- References

# Static code analysis

## SonarQube

We use SonarQube as our standard static analysis tool and build breaker for deviations against code quality rules.

Production source code must be checked against the current NHSBSA static analysis rules profile where available for the specific language.

## Thresholds

The automated build will break for:

- Any BLOCKER or CRITICAL issues Production source code must not contain any issues that are considered BLOCKER or CRITICAL . Builds may allow issues at a lower severity to pass. All issues should be addressed to avoid a buildup of technical debt.

- Less than 80% test coverage Test coverage is measured through unit and integration testing

## References

- SonarQube issue definitions

- SonarQube metric definitions

## Improve the playbook

If you spot anything factually incorrect with this page or have ideas for improvement, please share your suggestions.

Before you start, you will need a GitHub account . Github is an open forum where we collect feedback.

Published: 3 June 2026

Last reviewed: 6 May 2023

Next review due: 6 May 2024
