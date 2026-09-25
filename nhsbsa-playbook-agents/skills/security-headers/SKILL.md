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
