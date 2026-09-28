# Coding and Engineering Practices: Testing and Quality Assurance

## Purpose  
Ensure the production of high-quality, maintainable, and reliable software through rigorous testing practices. This skill emphasizes writing tests that verify correctness, detect regressions, and improve code clarity. It aligns with NHSBSA Digital, Data and Technology Playbook principles, ensuring software meets functional and non-functional requirements, adheres to accessibility standards, and is maintainable over time.

---

## When This Skill Applies  
This skill applies in the following scenarios:  
- **New feature development**: Writing tests to validate functionality before deployment.  
- **Code refactoring**: Ensuring refactored code retains existing behavior.  
- **Legacy code maintenance**: Adding tests to untested legacy systems to improve reliability.  
- **Integration with third-party systems**: Verifying compatibility and edge cases.  
- **Automated CI/CD pipelines**: Ensuring tests are part of the deployment process for early defect detection.  

**Example**: When implementing a new API endpoint for patient data retrieval, unit tests should validate correct response formats, error handling, and data validation.  

---

## When This Skill Does Not Apply  
This skill is not applicable in:  
- **Non-functional requirements**: Testing performance, scalability, or security may fall under separate quality gates (see "Security and Data Considerations").  
- **Design discussions**: High-level architectural decisions are outside the scope of unit or integration testing.  
- **Documentation**: READMEs and user guides require different verification methods (e.g., peer review).  

---

## NHS Requirements  
NHSBSA mandates:  
- All code must be **testable** and **maintainable**.  
- Tests must be **clear**, **repeatable**, and **self-contained**.  
- Test coverage must meet **minimum thresholds** (e.g., 80% for core business logic).  
- All repositories must include a **README** with test instructions (see [NHSBSA Playbook: Writing READMEs](https://nhsbsa.github.io/nhsbsa-digital-playbook/development/dev-documentation-readme/)).  

---

## Mandatory Requirements  
- **Unit tests for all new functionality**: Ensure individual components (e.g., classes, methods) are isolated and verified.  
- **Integration tests for critical paths**: Validate interactions between modules or external services.  
- **Test-driven development (TDD)**: Write tests before implementing code to define expected behavior.  
- **Code coverage reporting**: Use tools like JaCoCo (Java) or Istanbul (JavaScript) to measure coverage.  
- **Automated test execution**: Integrate tests into CI/CD pipelines (e.g., GitHub Actions, Jenkins).  

---

## Recommended Practices  
- **Use TDD**: Write failing tests first, then implement code to make them pass.  
- **Write readable assertions**: Use matchers (e.g., `assertEquals`, `assertThat`) instead of raw equality checks.  
- **Avoid brittle tests**: Focus on behavior, not implementation details (e.g., test logic, not private method calls).  
- **Structure READMEs clearly**: Include a "Test your documentation" section with step-by-step instructions.  

---

## Do  
- ✅ **Write tests for all public methods**:  
  ```java
  // Example: Unit test for a method that calculates BMI
  @Test
  public void testCalculateBMI() {
      assertEquals(25.0, BMIcalculator.calculateBMI(70, 1.75), 0.01); // 70 kg, 1.75 m
  }
  ```  
- ✅ **Use integration tests for external services**:  
  ```python
  # Example: Test API call to a healthcare data source
  def test_get_patient_data():
      response = fetch_patient_data(patient_id="12345")
      assert response.status_code == 200
      assert "name" in response.json()
  ```  
- ✅ **Include edge cases**:  
  ```javascript
  // Test for empty input
  test("empty input returns error", () => {
    const result = validateInput("");
    expect(result).toBe("Input cannot be empty");
  });
  ```  

---

## Don't  
- ❌ **Avoid testing implementation details**:  
  ```java
  // Poor: Tests private methods directly
  @Test
  public void testPrivateMethod() {
      MyClass obj = new MyClass();
      assertEquals(10, obj.calculateInternalValue()); // Avoid testing private logic
  }
  ```  
- ❌ **Write brittle assertions**:  
  ```python
  # Poor: Hardcoded string comparisons
  assert response.text() == "Welcome to the NHS Portal"  # Fails if UI text changes
  ```  
- ❌ **Ignore test failures**:  
  ```bash
  # Example: Skipping test due to a known issue
  # ❌ DO NOT do this
  @Ignore("Known issue: https://github.com/issue/123")
  @Test
  public void testFailingFeature() { ... }
  ```  

---

## Detailed Implementation Guidance  
### Step-by-Step: Writing a Unit Test  
1. **Identify the component**: Choose a method or class to test (e.g., `calculateBMI()`).  
2. **Write a failing test**: Use a testing framework (JUnit, pytest, etc.).  
3. **Implement the code**: Make the test pass by writing the method.  
4. **Refactor**: Improve code structure without changing behavior.  
5. **Repeat**: Add more tests for edge cases (e.g., zero weight, null inputs).  

**Example**:  
```python
# Test for division by zero in a math function
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```  

### Test Structure  
- **Setup**: Use `setUp()` to initialize mocks or dependencies.  
- **Teardown**: Clean up resources (e.g., close database connections).  
- **Assertions**: Use `assert` statements with matchers (e.g., `assertThat(actual, equalTo(expected))`).  

---

## Decision Rules  
- **Use mocks for external dependencies**:  
  ```java
  // Mock a database call
  @Mock
  private DatabaseService databaseService;
  ```  
- **Use integration tests for critical paths**: Verify interactions with real databases or APIs.  
- **Prioritize test isolation**: Use mocking frameworks (e.g., Mockito, Sinon) to decouple tests.  

---

## Accessibility  
- **Test for accessibility standards**: Use tools like [axe](https://www.deque.com/axe/) to verify UI components meet WCAG 2.1 guidelines.  
- **Example**: Ensure form labels are associated with input fields.  
- **Avoid**:  
  ```html
  <!-- Poor: Missing label -->
  <input type="text" id="username" />
  ```  
  **Fix**:  
  ```html
  <!-- Good: Label associated with input -->
  <label for="username">Username:</label>
  <input type="text" id="username" />
  ```  

---

## Security and Data Considerations  
- **Test data validation**: Ensure inputs are sanitized to prevent SQL injection or XSS.  
  ```python
  # Example: Sanitize user input
  def sanitize_input(input_text):
      return input_text.replace("<", "&lt;").replace(">", "&gt;")
  ```  
- **Use secure defaults**: Avoid hardcoding secrets (e.g., API keys) in tests.  
- **Test authentication**: Verify role-based access controls.  

---

## Testing and Quality Gates  
- **Automate testing**: Integrate tests into CI/CD pipelines (e.g., GitHub Actions).  
- **Enforce coverage thresholds**: Use JaCoCo or Istanbul to ensure minimum coverage.  
- **Peer reviews**: Validate test quality during code reviews.  

---

## Common Failure Modes  
- **Brittle tests**: Fail due to minor code changes (e.g., string literals).  
  **Fix**: Use matchers and focus on behavior.  
- **Missing edge cases**: Tests pass for normal inputs but fail for edge cases (e.g., zero, null).  
  **Fix**: Write tests for all possible inputs.  
- **Unreliable tests**: Tests fail intermittently due to timing or external dependencies.  
  **Fix**: Use mocks and retry mechanisms.  

---

## Exceptions and Deviations  
- **Legacy code**: Existing untested legacy systems may require a phased approach to add tests.  
- **Third-party libraries**: Use integration tests for compatibility but avoid testing library internals.  

---

## Agent Completion Checklist  
- [ ] All new code has unit tests.  
- [ ] Integration tests cover critical paths.  
- [ ] README includes test instructions.  
- [ ] Test coverage meets 80% threshold.  
- [ ] No brittle assertions in tests.  
- [ ] Accessibility tests pass for UI components.  
- [ ] Security tests validate input sanitization.  

---

## Related Skills  
- **Code Review**: Ensures test quality and adherence to standards.  
- **CI/CD Pipeline Configuration**: Automates test execution.  
- **Documentation**: Provides test instructions in READMEs.  

---

## Authoritative Sources  
1. [NHSBSA Digital, Data and Technology Playbook](https://nhsbsa.github.io/nhsbsa-digital-playbook/development/dev-documentation-readme/)  
2. [Modern Best Practices for Testing in Java](https://example.com/testing-in-java)  
3. [JUnit 5 User Guide](https://junit.org/junit5/docs/current/user-guide/)  
4. [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)  
5. [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)  

--- 

This document ensures adherence to NHSBSA standards, promotes test-driven development, and mitigates risks through rigorous testing practices.
