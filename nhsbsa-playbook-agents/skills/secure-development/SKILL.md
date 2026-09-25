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
