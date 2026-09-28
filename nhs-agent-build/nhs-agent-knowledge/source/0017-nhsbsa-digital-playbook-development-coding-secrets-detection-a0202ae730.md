# Secrets detection - NHSBSA Digital, Data and Technology Playbook - NHSBSA

Source URL: https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-secrets-detection/

## Source content

## Contents

- What is a secret?

- Dealing with committed secrets Revoke keys immediately Rewriting history

- Revoke keys immediately

- Rewriting history

- Secrets detection tooling Add Gitleaks configuration Add a pre-commit hook Configure Gitlab secrets detection Ignore false positives

- Add Gitleaks configuration

- Add a pre-commit hook

- Configure Gitlab secrets detection

- Ignore false positives

# Secrets detection

Sensitive information, or ‘secrets’, such as API keys and credentials must not be checked into source control.

Anyone who commits to a repository must be aware of:

- What constitutes a secret within their service architecture

- How to deal with a secret mistakenly committed to a source code repository

- How to use secret detection tools effectively

## What is a secret?

A secret is confidential information that is required to deliver a software solution. It should only be accessible to authorised people under appropriate access control.

We advise all delivery teams to assess their specific build pipeline and deployment architecture to catalogue all the secrets that must be protected.

Consider the following:

- Build pipeline secrets SSH keys Tooling API keys (SonarQube, Saucelabs, etc) Internal topology Don’t expose information on internal topology when not necessary: Protocols Hostnames Ports

- SSH keys

- Tooling API keys (SonarQube, Saucelabs, etc)

- Internal topology Don’t expose information on internal topology when not necessary: Protocols Hostnames Ports

- Protocols

- Hostnames

- Ports

- Application runtime secrets Credentials Usernames Passwords API keys Client certificates Encryption keys

- Credentials Usernames Passwords API keys Client certificates

- Usernames

- Passwords

- API keys

- Client certificates

- Encryption keys

- Personally identifiable data If you are processing personal data, consider the risk of committing personally identifiable data

Risk assessment

A sensitive data risk assessment should be recorded in the project documentation site. It should catalogue service specific secrets, the secret detection rule IDs and remediation steps to take if the secret is ever leaked.

## Dealing with committed secrets

Raise a security incident with the Information Security team when you discover secrets committed to a repository. They will engage with the relevant stakeholders to assess the impact, agree remediation actions, and provide an audit trail.

### Revoke keys immediately

Do not wait for a response from Information Security before revoking keys.

From Government guidance

> If you accidentally publish a secret, you must revoke it and immediately provision new keys to the system. Once a secret has been published, you must assume that it is compromised no matter how quickly you are able to remove it as attackers have automated scanning tools that will pick up credential leaks immediately. This means you must make sure that your system allows for keys and credentials to be changed and rotated easily, and for secrets to be revoked.

If you accidentally publish a secret, you must revoke it and immediately provision new keys to the system. Once a secret has been published, you must assume that it is compromised no matter how quickly you are able to remove it as attackers have automated scanning tools that will pick up credential leaks immediately.

This means you must make sure that your system allows for keys and credentials to be changed and rotated easily, and for secrets to be revoked.

### Rewriting history

Destructive rewrite of published Git history must follow NHSBSA process

Consult with your professional lead and the security team.

Refer to our guidance on rewriting Git history .

## Secrets detection tooling

Use secrets detection tools to protect against mistaken commits, and to alert if they get pushed to the central repository.

- Gitleaks as our secrets detection tool

- NHSBSA Gitleaks configuration file with verified rules

- Pre-commit managed Git hooks to prevent local commits of secrets

- Gitlab-CI secrets detection to alert in case a local pre-commit git hook has not prevented the commit

### Add Gitleaks configuration

To use the NHSBSA Gitleaks definitions:

- Copy the nhsbsa-gitleaks.toml config file into your project

```text
wget
https://gitlab.com/nhsbsa/platform-services/gitleaks/gitleaks-nhsbsa/-/raw/main/gitleaks-nhsbsa.toml
```

- Create a project specific gitleaks.toml file and configure it to extend the NHSBSA file

```text
title
=
"<project-name> gitleaks config"
[
extend
]
path
=
"gitleaks-nhsbsa.toml"
```

### Add a pre-commit hook

- Install pre-commit

- Install Gitleaks

- Add a .pre-commit-config.yaml configuration file:

```text
repos
:
-
repo
:
local
hooks
:
-
id
:
gitleaks
name
:
Detect hardcoded secrets
description
:
Detect hardcoded secrets using Gitleaks
entry
:
gitleaks protect
-
-
config="gitleaks.toml"
-
-
verbose
-
-
redact
-
-
staged
language
:
system
pass_filenames
:
false
```

- Every contributor must install the Git hook using pre-commit:

```text
pre-commit
install
```

### Configure Gitlab secrets detection

- Include Gitleaks secret detection job template in gitlab-ci.yml

```text
include
:
-
template
:
Security/Secret
-
Detection.gitlab
-
ci.yml
secret_detection
:
variables
:
SECRET_DETECTION_HISTORIC_SCAN
:
"true"
```

- Instruct secrets detection analyzer to use the project specific Gitleaks config toml file Create a file .gitlab/secret-detection-ruleset.toml

```text
[
secrets
]
description = 'secrets custom rules configuration'
[
[
secrets.passthrough
]
]
type  = "file"
target = "gitleaks.toml"
value = "gitleaks.toml"
```

### Ignore false positives

Detected secrets can be ignored in different ways:

- Secrets in history Add the fingerprint to a .gitleaksignore file.

Secrets in history Add the fingerprint to a .gitleaksignore file.

- Uncommitted false positives Add a comment to the offending line with the gitleaks:allow keyword.

Uncommitted false positives Add a comment to the offending line with the gitleaks:allow keyword.

See Gitleaks README for further information

## Improve the playbook

If you spot anything factually incorrect with this page or have ideas for improvement, please share your suggestions.

Before you start, you will need a GitHub account . Github is an open forum where we collect feedback.

Published: 11 September 2026
