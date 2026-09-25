# Naming Conventions

Names should communicate intent and allow related components to be grouped.

Use the NHSBSA naming model where applicable:

`{optional service-line}-{service}-{function}-{type}`

Typical component types include:

- `ui`
- `api`
- `lambda`
- `prototype`
- `poc`
- `config`
- `tf`

Test types include:

- `acceptance-test`
- `api-test`
- `accessibility-test`
- `performance-test`
- `security-test`
- `manual-test`

Use:

- `kebab-case` for repositories and branches where specified.
- `CamelCase` / `camelCase` according to language conventions.
- `snake_case` where the language/project requires it.
- Natural, unabbreviated names for externally visible repository names and
  public documentation.

Branches should use `main` for the production mainline and keep change
descriptions brief.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-naming-conventions/
