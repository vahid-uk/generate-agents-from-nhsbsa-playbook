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
