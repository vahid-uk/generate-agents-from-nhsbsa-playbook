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
