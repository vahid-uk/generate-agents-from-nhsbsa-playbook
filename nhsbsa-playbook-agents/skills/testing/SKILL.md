# Testing

Developers are responsible for testing the code they write.

At minimum:

- Unit test isolated functionality.
- Integration test functionality involving external resources.
- Test against dependencies representative of production.
- Use appropriate mocks for external APIs where necessary.
- Do not duplicate full-stack acceptance testing unnecessarily.

NHSBSA encourages Test Driven Development:

1. Red — write a failing test describing the next behaviour.
2. Green — implement only enough production code to pass.
3. Refactor — improve the implementation while keeping tests passing.

Keep tests focused and maintainable.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/dev-tests/
