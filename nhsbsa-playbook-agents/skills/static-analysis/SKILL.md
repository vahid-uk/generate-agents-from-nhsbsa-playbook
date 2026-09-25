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
