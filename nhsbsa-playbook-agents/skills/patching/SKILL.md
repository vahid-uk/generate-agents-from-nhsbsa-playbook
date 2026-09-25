# Application Patching

Keep runtimes and dependencies current.

Requirements:

- Use a dependency management system.
- Declare dependency versions explicitly.
- Do not commit binaries into source control.
- Regularly update dependencies and runtimes.
- Treat patching as routine vulnerability management.
- Respond promptly to vulnerable dependencies.
- Keep framework/library APIs current where practical.

Approved dependency-management approaches documented by NHSBSA include:

- Java: Maven / `pom.xml`
- Node.js: NPM / `package.json`
- Python: Pip / `pyproject.toml`
- Ruby: Bundler / `Gemfile`

Use isolated environments for Python and Ruby dependencies.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/technologies/tech-patching/
