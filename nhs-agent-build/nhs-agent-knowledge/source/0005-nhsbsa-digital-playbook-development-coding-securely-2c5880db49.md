# Secure development - NHSBSA Digital, Data and Technology Playbook - NHSBSA

Source URL: https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-securely/

## Source content

## Contents

- NCSC guidance

- OWASP Top ten web application risks Top ten proactive controls

- Top ten web application risks

- Top ten proactive controls

- References

# Secure development

## NCSC guidance

We follow NCSC’s 8 principles of secure development and deployment .

- Secure development is everyone’s concern Software Development candidates should expect to be asked about security risks and secure coding techniques during interview All NHSBSA staff undergo mandatory training on security and data protection

Secure development is everyone’s concern

- Software Development candidates should expect to be asked about security risks and secure coding techniques during interview

- All NHSBSA staff undergo mandatory training on security and data protection

- Keep your security knowledge sharp You should understand the OWASP top 10 web application security risks and OWASP top 10 proactive controls We are committed to the continuing professional development of our staff, with access to training resources and a dedicated 4 hours every 2 weeks for self-directed learning

Keep your security knowledge sharp

- You should understand the OWASP top 10 web application security risks and OWASP top 10 proactive controls

- We are committed to the continuing professional development of our staff, with access to training resources and a dedicated 4 hours every 2 weeks for self-directed learning

- Produce clean & maintainable code Naming conventions Coding guidance Logging guidance Guidance for coding with Personal Data . Testing by developers Peer review Code quality assurance

Produce clean & maintainable code

- Naming conventions

- Coding guidance

- Logging guidance

- Guidance for coding with Personal Data .

- Testing by developers

- Peer review

- Code quality assurance

- Secure your development environment TODO - Development environment

Secure your development environment TODO - Development environment

- Protect your code repository TODO - Git repo access control

Protect your code repository TODO - Git repo access control

- Secure the build and deployment pipeline TODO - CI/CD

Secure the build and deployment pipeline TODO - CI/CD

- Continually test your security TODO - ITHC

Continually test your security TODO - ITHC

- Plan for security flaws

Plan for security flaws

## OWASP

### Top ten web application risks

Production code must be written with an understanding of common security risks as defined in the latest OWASP Top 10 web application security risks

- A01:2021-Broken Access Control

- A02:2021-Cryptographic Failures

- A03:2021-Injection

- A04:2021-Insecure Design

- A05:2021-Security Misconfiguration

- A06:2021-Vulnerable and Outdated Components

- A07:2021-Identification and Authentication Failures

- A08:2021-Software and Data Integrity Failures

- A09:2021-Security Logging and Monitoring Failures

- A10:2021-Server-Side Request Forgery

### Top ten proactive controls

Production code must be written in accordance with good security practices as defined in the OWASP top 10 proactive controls

- C1: Define Security Requirements

- C2: Leverage Security Frameworks and Libraries

- C3: Secure Database Access

- C4: Encode and Escape Data

- C5: Validate All Inputs

- C6: Implement Digital Identity

- C7: Enforce Access Controls

- C8: Protect Data Everywhere

- C9: Implement Security Logging and Monitoring

- C10: Handle All Errors and Exceptions

## References

- NCSC 8 principles of secure development and deployment

- OWASP Top 10 web application security risks

- OWASP top 10 proactive controls

## Related articles

- Security Security is everyone’s responsibility 23 January 2025

## Security

Security is everyone’s responsibility

- Coding with personal data 1 July 2022

## Coding with personal data

- Application patching REVIEW Keeping our software up to date with the latest versions of dependant libraries and runtimes 13 January 2024

## Application patching

Keeping our software up to date with the latest versions of dependant libraries and runtimes

- Secrets detection REVIEW Avoid committing ‘secrets’ such as API keys into source control 11 September 2026

## Secrets detection

Avoid committing ‘secrets’ such as API keys into source control

- Rewriting Git history REVIEW Removing sensitive data such as non-revokable secrets or contributor identities from Git 11 September 2026

## Rewriting Git history

Removing sensitive data such as non-revokable secrets or contributor identities from Git

- Security headers REVIEW Use HTTP headers to protect our users 11 September 2026

## Security headers

Use HTTP headers to protect our users

- Content Security Policy REVIEW Use CSP as the modern approach to securing our web applications 11 September 2026

## Content Security Policy

Use CSP as the modern approach to securing our web applications

## Improve the playbook

If you spot anything factually incorrect with this page or have ideas for improvement, please share your suggestions.

Before you start, you will need a GitHub account . Github is an open forum where we collect feedback.

Published: 11 September 2026

Last reviewed: 6 May 2023

Next review due: 6 May 2024
