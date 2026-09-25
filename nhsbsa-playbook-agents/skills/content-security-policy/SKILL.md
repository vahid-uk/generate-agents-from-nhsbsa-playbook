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
