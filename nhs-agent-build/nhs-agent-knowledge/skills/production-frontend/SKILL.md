# Production frontend implementation

## Purpose  
Implement frontend components using NHS.UK frontend guidelines to ensure accessibility, consistency, and security in digital services. Focus on user-centered design, inclusive practices, and adherence to NHS principles.

## When this skill applies  
- When developing NHS frontend components (e.g., buttons, forms, navigation).  
- When using the `button` macro from NHS.UK frontend to ensure accessibility and consistency.  
- When aligning with NHS design principles (e.g., putting people at the heart of design, inclusivity, and simplicity).  

## When this skill does not apply  
- When the component is not part of the NHS.UK frontend library.  
- When a specific requirement (e.g., legacy system integration) conflicts with NHS guidelines.  
- When the component is not user-facing (e.g., internal admin tools).  

## NHS requirements  
- Follow the 10 NHS design principles (e.g., inclusivity, simplicity, trust, environmental responsibility).  
- Ensure components are accessible (WCAG 2.1 AA compliance).  
- Use NHS.UK frontend v10.5.0 or later.  

## Mandatory requirements  
- Use NHS.UK frontend components and macros (e.g., `button` macro).  
- Adhere to accessibility standards (e.g., ARIA labels, keyboard navigation).  
- Validate HTML and CSS against NHS.UK frontend guidelines.  

## Recommended practices  
- Use Nunjucks macros for reusable components (e.g., `button` macro).  
- Keep code up to date with NHS.UK frontend releases.  
- Document design decisions and rationale.  

## Do  
- Use the `button` macro with `text` and `icon` parameters (e.g., `button({ text: "Continue", icon: { name: "arrow-right" } })`).  
- Test components with real users and assistive technologies.  
- Follow NHS.UK frontend documentation for icon placement (e.g., `placement: "start"` or `"end"`).  

## Don't  
- Avoid using custom HTML for components (e.g., hardcoding `<button>` elements).  
- Do not ignore accessibility checks (e.g., missing ARIA labels).  
- Do not bypass NHS.UK frontend guidelines for convenience.  

## Detailed implementation guidance  
- **Button macro**:  
  - Use `text` for screen reader accessibility.  
  - Add `icon` with `name` (e.g., `"search"`) or `html` (e.g., `<svg>...</svg>`).  
  - Set `placement` to `"start"` or `"end"` for icon positioning.  
- **Nunjucks configuration**:  
  - For NHS.UK frontend v10.x:  
    ```text  
    nunjucks.configure([  
      'node_modules/nhsuk-frontend/dist/nhsuk/components',  
      'node_modules/nhsuk-frontend/dist/nhsuk/macros'  
    ])  
    ```  
  - For v9.x:  
    ```text  
    nunjucks.configure([  
      'node_modules/nhsuk-frontend/packages/components',  
      'node_modules/nhsuk-frontend/packages/macros'  
    ])  
    ```  

## Decision rules  
- Use the `button` macro for all interactive elements (e.g., submit, cancel).  
- Ensure icons are contextually relevant (e.g., `"plus"` for "Add", `"minus"` for "Remove").  
- Validate against NHS.UK frontend accessibility and usability guidelines.  

## Accessibility  
- Ensure `text` is visible to screen readers (e.g., no empty `text` when using icons).  
- Use `aria-label` for icons when `text` is absent.  
- Test keyboard navigation (e.g., focus states, tab order).  

## Security and data considerations  
- Avoid XSS vulnerabilities by sanitizing user inputs.  
- Use HTTPS for all external resources (e.g., icons, fonts).  
- Sanitize HTML inputs to prevent injection attacks.  

## Testing and quality gates  
- **Manual testing**:  
  - Test with screen readers (e.g., NVDA, JAWS).  
  - Validate keyboard navigation (e.g., tab, enter, space).  
- **Automated testing**:  
  - Use axe or similar tools for accessibility checks.  
  - Run linters (e.g., ESLint, Stylelint) for code quality.  
- **Code reviews**:  
  - Verify adherence to NHS.UK frontend guidelines.  
  - Confirm compliance with accessibility and security standards.  

## Common failure modes  
- Missing `text` in buttons with icons (e.g., screen readers cannot interpret the button).  
- Incorrect icon placement (e.g., `"start"` instead of `"end"` for contextual clarity).  
- Security vulnerabilities (e.g., unescaped HTML in `html` parameters).  

## Exceptions and deviations  
- **Allowed exceptions**:  
  - When a component is not available in NHS.UK frontend (e.g., custom animations).  
  - When a requirement conflicts with NHS guidelines (e.g., legacy system constraints).  
- **Documentation**:  
  - Record exceptions in a traceability matrix.  
  - Obtain approval from the NHS.UK frontend team.  

## Agent completion checklist  
- [ ] Used `button` macro with `text` and `icon` parameters.  
- [ ] Validated accessibility (e.g., screen reader testing, ARIA labels).  
- [ ] Configured Nunjucks paths for NHS.UK frontend.  
- [ ] Tested with real users and assistive technologies.  
- [ ] Documented design decisions and exceptions.  

## Related skills  
- NHS.UK frontend component development.  
- Accessibility testing (WCAG 2.1 AA).  
- Security practices (XSS prevention, HTTPS).  

## Authoritative sources  
- [NHS.UK frontend documentation](https://nhsuk.github.io/nhsuk-frontend/)  
- [WCAG 2.1 AA guidelines](https://www.w3.org/WAI/WCAG21/quickref/)  
- [Nunjucks templating documentation](https://mozilla.github.io/nunjucks/)
