# Production frontend implementation  

## Purpose  
Ensure consistent, secure, and accessible frontend implementation for NHS digital services using the NHS.UK frontend library and Nunjucks macros. This skill ensures alignment with NHS design principles, accessibility standards, and security requirements while enabling scalable, maintainable code.  

---

## When this skill applies  
This skill applies when:  
- Building new NHS digital services or components that require consistent UI/UX patterns.  
- Integrating frontend components (e.g., buttons, forms, navigation) into applications using the NHS.UK frontend library.  
- Implementing design systems or reusable patterns that adhere to NHS accessibility and usability standards.  
- Updating legacy systems to use the NHS.UK frontend library for compliance with current guidelines.  

**Example**: When developing a patient portal for NHS services, this skill ensures buttons, forms, and icons are implemented using NHS.UK frontend components for consistency.  

---

## When this skill does not apply  
This skill does not apply when:  
- Developing non-NHS services (e.g., third-party tools not integrated with NHS systems).  
- Using frontend frameworks or libraries unrelated to the NHS.UK frontend ecosystem (e.g., React, Vue.js without NHS.UK components).  
- Implementing custom UI elements outside the scope of NHS.UK frontend patterns (e.g., bespoke animations or non-standard layouts).  

**Example**: A private healthcare provider’s internal tool using Bootstrap would not require this skill.  

---

## NHS requirements  
- Compliance with NHS design principles (e.g., inclusivity, simplicity, trust, and environmental sustainability).  
- Adherence to the NHS.UK frontend versioning and component standards (v9.x or v10.x).  
- Accessibility compliance (WCAG 2.1 AA/AAA standards, screen reader compatibility).  
- Security measures (e.g., avoiding inline HTML in macros, secure data handling).  
- Environmental impact considerations (e.g., reusing resources, minimizing component bloat).  

---

## Mandatory requirements  
1. **Use NHS.UK frontend v10.x or v9.x**: Ensure the correct version is installed and configured.  
2. **Implement Nunjucks macros**: All components must use macros from the NHS.UK frontend library.  
3. **Follow accessibility guidelines**: All components must pass automated and manual accessibility tests.  
4. **Secure data handling**: Avoid HTML arguments in macros during production; escape user input.  
5. **Version control**: Track changes in the NHS.UK frontend library and update dependencies regularly.  

---

## Recommended practices  
- **Use Nunjucks macros for all components**: This ensures consistency and reduces manual HTML errors.  
- **Keep code modular**: Reuse macros across projects to maintain a shared design system.  
- **Test early and often**: Use automated tools (e.g., axe, Lighthouse) for accessibility and performance.  
- **Document implementation steps**: Provide clear guidance for developers on how to use macros.  
- **Collaborate with designers**: Ensure components align with NHS design principles and user research.  

---

## Do  
- **Use NHS.UK frontend macros**:  
  ```nunjucks  
  {% from "nhsuk/components/button/macro.njk" import button %}  
  {{ button({ text: "Continue", classes: "nhsuk-button--secondary" }) }}  
  ```  
- **Follow the correct configuration paths**:  
  ```javascript  
  nunjucks.configure([  
    'node_modules/nhsuk-frontend/dist/nhsuk/components',  
    'node_modules/nhsuk-frontend/dist/nhsuk/macros'  
  ]);  
  ```  
- **Test components with real users**: Conduct usability testing for edge cases (e.g., screen reader compatibility).  
- **Update libraries regularly**: Check the [NHS.UK frontend changelog](https://github.com/nhsuk/nhsuk-frontend/releases) for updates.  

---

## Don't  
- **Avoid writing raw HTML for components**: Use macros instead to ensure consistency.  
  ❌ Incorrect:  
  ```html  
  <button class="nhsuk-button">Submit</button>  
  ```  
  ✅ Correct:  
  ```nunjucks  
  {{ button({ text: "Submit" }) }}  
  ```  
- **Don’t use HTML arguments in production**: This can introduce security risks.  
  ❌ Incorrect:  
  ```nunjucks  
  {{ button({ html: "<strong>Submit</strong>" }) }}  
  ```  
- **Don’t ignore accessibility checks**: Skip automated tools or manual testing.  
- **Don’t hardcode versions**: Always use package managers (e.g., npm, yarn) to manage dependencies.  

---

## Detailed implementation guidance  
### Step 1: Setup NHS.UK frontend  
1. Install the library:  
   ```bash  
   npm install nhsuk-frontend  
   ```  
2. Configure Nunjucks paths:  
   ```javascript  
   const nunjucks = require('nunjucks');  
   nunjucks.configure([  
     'node_modules/nhsuk-frontend/dist/nhsuk/components',  
     'node_modules/nhsuk-frontend/dist/nhsuk/macros'  
   ], { autoescape: true });  
   ```  

### Step 2: Use macros for components  
- **Button with icon**:  
  ```nunjucks  
  {% from "nhsuk/components/button/macro.njk" import button %}  
  {{ button({  
    text: "Download PDF",  
    icon: "download",  
    icon_placement: "end"  
  }) }}  
  ```  
- **Form input**:  
  ```nunjucks  
  {% from "nhsuk/components/input/macro.njk" import input %}  
  {{ input({  
    label: "Name",  
    id: "name",  
    classes: "nhsuk-input--width-20"  
  }) }}  
  ```  

### Step 3: Test and validate  
- **Accessibility**: Use axe or Lighthouse to scan for WCAG compliance.  
- **Performance**: Minify CSS/JS and use lazy loading for images.  
- **Cross-browser testing**: Validate components in Chrome, Firefox, Safari, and Edge.  

---

## Decision rules  
- **Use v10.x for new projects**: Prioritize the latest stable version for features and security.  
- **Use v9.x for legacy systems**: Only if upgrading introduces breaking changes.  
- **Prioritize accessibility**: Always include ARIA attributes (e.g., `aria-label`, `role`).  
- **Avoid custom styling**: Use NHS.UK classes (e.g., `nhsuk-button--secondary`) instead of overriding CSS.  

---

## Accessibility  
- **Semantic HTML**: Use `<button>`, `<input>`, and `<label>` tags as per macros.  
- **Keyboard navigation**: Ensure components are operable via keyboard (e.g., focus states).  
- **Screen reader compatibility**: Add `aria-live` regions for dynamic content updates.  
- **Color contrast**: Use NHS.UK color palettes (e.g., `nhsuk-color--text` for sufficient contrast).  

---

## Security and data considerations  
- **Escape user input**: Use `{% autoescape %}` in Nunjucks to prevent XSS attacks.  
- **Avoid inline HTML**: Replace with macros for secure rendering.  
- **Secure dependencies**: Regularly update the NHS.UK frontend library to patch vulnerabilities.  
- **Data validation**: Sanitize inputs in forms to prevent SQL injection or other attacks.  

---

## Testing and quality gates  
1. **Unit tests**: Write tests for macros using Jest or Mocha.  
   ```javascript  
   test('Button macro renders correctly', () => {  
     const result = render(button({ text: "Submit" }));  
     expect(result).toContain('<button class="nhsuk-button">Submit</button>');  
   });  
   ```  
2. **Accessibility checks**: Use axe-core in CI pipelines.  
3. **Code reviews**: Ensure macros follow NHS.UK patterns.  
4. **Performance checks**: Use Lighthouse to validate load times and resource usage.  

---

## Common failure modes  
- **Incorrect macro configuration**: Missing `from` imports or incorrect paths.  
  **Fix**: Verify `nunjucks.configure()` paths match the installed version (v9.x or v10.x).  
- **Accessibility failures**: Missing labels or incorrect ARIA attributes.  
  **Fix**: Use the `label` and `hint` parameters in macros.  
- **Security vulnerabilities**: Inline HTML in macros.  
  **Fix**: Replace with `text` or `html` (only for safe, pre-sanitized content).  

---

## Exceptions and deviations  
- **Custom components**: If a component is not available in NHS.UK frontend, create a custom macro and document it in the design system.  
- **Version conflicts**: If a legacy system requires v9.x, document the reason and plan for migration.  
- **Third-party tools**: Use NHS.UK frontend for core components but allow custom tools for non-core features (e.g., analytics).  

---

## Agent completion checklist  
- [ ] Installed NHS.UK frontend via npm/yarn.  
- [ ] Configured Nunjucks paths for v10.x or v9.x.  
- [ ] Used macros for all components (no raw HTML).  
- [ ] Conducted accessibility tests (axe/Lighthouse).  
- [ ] Escaped user input and avoided inline HTML.  
- [ ] Updated dependencies to the latest version.  
- [ ] Documented custom macros or deviations.  

---

## Related skills  
- **NHS design principles**: Ensures alignment with inclusivity, trust, and simplicity.  
- **Accessibility implementation**: Focuses on WCAG compliance and screen reader support.  
- **Security best practices**: Covers data handling and XSS prevention.  

---

## Authoritative sources  
- [NHS.UK frontend documentation](https://nhsuk.github.io/nhsuk-frontend/)  
- [NHS.UK frontend changelog](https://github.com/nhsuk/nhsuk-frontend/releases)  
- [WCAG 2.1 guidelines](https://www.w3.org/TR/WCAG21/)  
- [Nunjucks documentation](https://mozilla.github.io/nunjucks/)  

--- 

This document ensures operational compliance with NHS frontend standards, security, and accessibility while providing actionable guidance for developers.
