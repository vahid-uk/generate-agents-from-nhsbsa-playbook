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
