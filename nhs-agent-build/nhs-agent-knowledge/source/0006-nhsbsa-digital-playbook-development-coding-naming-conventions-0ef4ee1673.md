# Naming conventions - NHSBSA Digital, Data and Technology Playbook - NHSBSA

Source URL: https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-naming-conventions/

## Source content

## Contents

- Terms Abbreviations Case

- Abbreviations

- Case

- Git Git Repositories Git branches Gitlab groups Merge/Pull Requests Commit messages

- Git Repositories

- Git branches

- Gitlab groups

- Merge/Pull Requests

- Commit messages

- Languages Java

- Java

- Package managers and build tools Maven NPM

- Maven

- NPM

# Naming conventions

It is important to adopt a naming convention:

- to clarify intent

- to group similar items

## Terms

Terms used in the naming conventions are:

Term | Description | example
Department | The department that owns the service | citizen corporate primary-care workforce ddat - Data, Digital & Technology dhsc - Department of Health and Social Care
Service line | For grouping within a Department | hwhc - Help with Health Costs ohs - Overseas Healthcare Services
Service | The actual Service being delivered | lis - Low Income Scheme ihs - Immigration Health Surcharge
Function | The operational function of a repository or component | apply for an application form dwp for an integration layer with Department for Works and Pensions
Type | The type of component, repository or change | For components: ui for a web frontend api for an RESTful API lambda for an AWS lambda prototype for prototype code poc for proof of concept For infrastructure: config for externalised configuration tf for terraform For tests: acceptance-test api-test accessibility-test performance-test security-test manual-test For managed changes: hotfix develop
Change ID | The identifier for a change, usually a Jira ticket such as a story, task, sub-task or bug | LISD-1234 as an example task in the Low Income Scheme service

- citizen

- corporate

- primary-care

- workforce

- ddat - Data, Digital & Technology

- dhsc - Department of Health and Social Care

- hwhc - Help with Health Costs

- ohs - Overseas Healthcare Services

- lis - Low Income Scheme

- ihs - Immigration Health Surcharge

- apply for an application form

- dwp for an integration layer with Department for Works and Pensions

- ui for a web frontend

- api for an RESTful API

- lambda for an AWS lambda

- prototype for prototype code

- poc for proof of concept

- config for externalised configuration

- tf for terraform

- acceptance-test

- api-test

- accessibility-test

- performance-test

- security-test

- manual-test

- hotfix

- develop

- LISD-1234 as an example task in the Low Income Scheme service

### Abbreviations

Service delivery teams often adopt short form or abbreviations of names. For example, the Maternity Exemption Certificate service is shorted to Matex, Immigration Health Surcharge is abbreviated to IHS. It is ok to use the short form for internal names such as code modules or system urls.

Use long form names whenever the content may be used outside of the service team. This includes service URLs, public hosted code repository names and READMEs.

### Case

Different case standards should be applied depending on usage:

- Natural - Using natural language standard, with spaces to separate words and capitals for initial letter and proper nouns

- kebab-case - All lower case with dashes to separate words

- CamelCase - Initial letters in words are uppercased, with no separators. First letter may be upper or lower.

- snake_case - All lower case with underscores to separate words

For all cases except natural , acronyms should be lowercased and treated as a single word.

## Git

### Git Repositories

Git repositories should be kebab-case with this convention:

> {optional service-line}-{service}-{function}-{type}

{optional service-line}-{service}-{function}-{type}

Gitlab and Github hosted repository names should use unabbreviated natural case.

### Git branches

All branches should be kebab-case , although change ID should be uppercase

- The mainline branch should be named main .

The mainline branch should be named main .

- release candidate branches should follow the convention: develop-{version} or hotfix-{version}

release candidate branches should follow the convention:

> develop-{version} or hotfix-{version}

develop-{version} or hotfix-{version}

- change candidate branches should follow the convention: {change ID}-{brief description} Descriptions should be kept brief, not exceeding 50 characters.

change candidate branches should follow the convention:

> {change ID}-{brief description}

{change ID}-{brief description}

Descriptions should be kept brief, not exceeding 50 characters.

See Git branching guidance for a more detailed explanation of Git branch naming

### Gitlab groups

Repositories in Gitlab should be organised into ‘groups’. Use unabbreviated natural case for the human readable form, and kebab-case for the URL with this convention:

> {department}/{service-line}/{service}

{department}/{service-line}/{service}

### Merge/Pull Requests

Merge/pull requests should be raised with natural case and this convention:

> {change ID} - {brief description}

{change ID} - {brief description}

### Commit messages

Commit messages should be natural case and follow this convention:

> {change ID} {brief description} i.e HMOD-0001 added check your answers page

{change ID} {brief description} i.e HMOD-0001 added check your answers page

Its fine to use NO-JIRA as the change ID if the change is a non-functional change, for example if its just updating the README file.

Commit message regex: ([A-Z]{3,4}\-([0-9]+)|Merge|Merging|NO-JIRA)[ ][a-z][a-zA-Z0-9 ]*

## Languages

For language constructs refer to the standard language style guides .

### Java

Java packages should be all lower case concatenated with this convention:

> uk.nhs.nhsbsa.{service}.{function}

uk.nhs.nhsbsa.{service}.{function}

Libraries may omit the service when shared across multiple services.

## Package managers and build tools

### Maven

Maven group id should be kebab-case with this convention:

> uk.nhs.nhsbsa.{optional department}.{optional service-line}.{service}

uk.nhs.nhsbsa.{optional department}.{optional service-line}.{service}

Maven artifact id should follow kebab-case and this convention:

> {optional service-line}-{service}-{function}-{type}

{optional service-line}-{service}-{function}-{type}

Unit tests run by Maven Surefire plugin should follow the convention:

> *Test.java

*Test.java

Integration tests run by Maven Failsafe plugin should follow the convention:

> *IT.java

*IT.java

### NPM

Package.json name should be kebab-case with this convention:

> @nhsbsa/{optional service-line}-{service}-{function}-{type}

@nhsbsa/{optional service-line}-{service}-{function}-{type}

## Improve the playbook

If you spot anything factually incorrect with this page or have ideas for improvement, please share your suggestions.

Before you start, you will need a GitHub account . Github is an open forum where we collect feedback.

Published: 18 November 2024

Last reviewed: 6 May 2023

Next review due: 6 May 2024
