# Prototyping

## Purpose  
Implement the NHS.UK frontend button component to create accessible, consistent, and semantically correct buttons for user interactions, including primary actions, links, and form submissions.

---

## When this skill applies  
Use this skill when:  
- Creating buttons for primary actions (e.g., "Continue," "Submit").  
- Designing buttons with specific variants (e.g., "brand," "secondary").  
- Implementing buttons with icons (e.g., search, arrow-right).  
- Ensuring compliance with NHS.UK frontend accessibility and design standards.  

---

## When this skill does not apply  
Avoid using this skill for:  
- Non-interactive elements (e.g., decorative graphics).  
- Buttons that require custom styling outside NHS.UK frontend guidelines.  
- Situations where the button’s purpose is unclear or ambiguous.  

---

## NHS requirements  
- Adhere to NHS.UK frontend accessibility standards (WCAG 2.1 AA/AAA).  
- Use semantic HTML and ARIA attributes where necessary.  
- Follow NHS.UK design system guidelines for color, spacing, and typography.  

---

## Mandatory requirements  
- **Text or HTML**: Provide either `text` or `html` (required).  
- **Variant**: Use a valid variant (`brand`, `login`, `reverse`, `secondary`, `secondary-solid`, `warning`).  
- **Accessibility**: Ensure buttons with icons include `ariaLabel` for screen readers.  

---

## Recommended practices  
- Use `text` over `html` for simplicity unless custom HTML is required.  
- Prefer `button` type for interactive elements; use `a` for links.  
- Use `small` variant for compact buttons in tight spaces.  
- Sanitize HTML input if using the `html` option to prevent XSS.  

---

## Do  
- Use the `button` macro with Nunjucks templates.  
- Include `ariaLabel` when using icons.  
- Test buttons with keyboard navigation and screen readers.  
- Apply `variant` to match design system requirements.  
- Use `preventDoubleClick` for submit buttons to avoid form submission errors.  

---

## Don't  
- Use deprecated options like `element` (replaced in v10.6.0).  
- Omit required `text` or `html` fields.  
- Hardcode styles; rely on NHS.UK frontend classes.  
- Ignore accessibility attributes (e.g., `ariaLabel`).  
- Use `html` without sanitizing user input.  

---

## Detailed implementation guidance  
1. **Import the macro**:  
   ```nunjucks
   {% from "button/macro.njk" import button %}
   ```  
2. **Basic usage**:  
   ```nunjucks
   {{ button({ text: "Continue" }) }}
   ```  
3. **With icon**:  
   ```nunjucks
   {{ button({
     text: "Search",
     icon: { name: "search", placement: "start" }
   }) }}
   ```  
4. **Custom variant**:  
   ```nunjucks
   {{ button({ text: "Submit", variant: "brand" }) }}
   ```  

---

## Decision rules  
- Use `button` for form actions; use `a` for navigation links.  
- Prioritize `text` over `html` unless custom markup is required.  
- Choose `variant` based on context (e.g., `brand` for primary CTA, `secondary` for secondary actions).  
- Use `small` for buttons in tight spaces (e.g., modals, dialogs).  

---

## Accessibility  
- Ensure all buttons have a clear purpose and are labeled appropriately.  
- Use `ariaLabel` for buttons with icons (e.g., `ariaLabel: "Search"`) to describe the icon.  
- Ensure keyboard focus is visible and functional.  
- Avoid relying solely on color to convey button state (e.g., use text labels for "disabled").  

---

## Security and data considerations  
- Sanitize HTML input if using the `html` option to prevent XSS attacks.  
- Avoid using user-provided content in `html` without validation.  
- Ensure `href` and `name` attributes are correctly set for links.  

---

## Testing and quality gates  
- **Automated tests**: Validate HTML structure, ARIA attributes, and variant classes.  
- **Manual checks**:  
  - Test keyboard navigation (Tab, Enter).  
  - Verify screen reader announcements for icons and labels.  
  - Confirm visual consistency across browsers and devices.  
- **Accessibility tools**: Use Lighthouse or axe to audit for WCAG compliance.  

---

## Common failure modes  
- Missing `text` or `html` fields.  
- Using deprecated options like `element`.  
- Incorrect `variant` usage (e.g., `brand` for non-CTA buttons).  
- Forgetting `ariaLabel` for icon-only buttons.  
- Unsanitized HTML leading to XSS vulnerabilities.  

---

## Exceptions and deviations  
- **Custom variants**: Deviate from standard variants only with explicit approval from the design system team.  
- **Non-semantic HTML**: Use `html` only when required by third-party integrations (e.g., embedded forms).  

---

## Agent completion checklist  
- [ ] Used the `button` macro with Nunjucks.  
- [ ] Included required `text` or `html`.  
- [ ] Applied appropriate `variant` and `small` if needed.  
- [ ] Added `ariaLabel` for icon-only buttons.  
- [ ] Tested with keyboard and screen readers.  
- [ ] Validated HTML and ARIA attributes.  

---

## Related skills  
- **Form components**: For input fields, labels, and validation.  
- **Icons**: For embedding SVGs in buttons.  
- **Links**: For non-interactive navigation.  

---

## Authoritative sources  
- [NHS.UK frontend button documentation](https://nhsuk.github.io/nhsuk-frontend/components/button/)  
- [NHS.UK accessibility guidelines](https://www.nhs.uk/our-organisation-and-staff/our-organisation/our-website/accessibility/)  
- [WCAG 2.1 AA/AAA standards](https://www.w3.org/WAI/standards-guidelines/wcag/)
