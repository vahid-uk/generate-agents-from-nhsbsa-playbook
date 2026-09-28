# NHS design system components

## Purpose  
Provide a skip link component to enable keyboard-only users to bypass repetitive navigation and jump directly to the main content of a page, improving accessibility for users with disabilities.

## When this skill applies  
- When creating NHS.UK pages that include a header with navigation links.  
- When ensuring compliance with GOV.UK Design System accessibility standards.  
- When implementing a skip link to improve keyboard navigation for users who cannot use a mouse.  

## When this skill does not apply  
- When the page lacks a header or navigation section.  
- When the main content is not marked with an `id="maincontent"` (the default target for the skip link).  
- When the skip link is not required by NHS.UK frontend guidelines (e.g., non-NHS.UK pages).  

## NHS requirements  
- All NHS.UK pages must include a skip link in the header.  
- The skip link must use the `nhsuk-skip-link` class and follow NHS.UK frontend 10.6.0+ standards.  
- The skip link must be visually hidden until activated by a keyboard.  

## Mandatory requirements  
- The skip link must be implemented using the `skipLink` macro from the NHS.UK frontend.  
- The `href` attribute must default to `#maincontent` (or explicitly set if the main content has a different ID).  
- The skip link must be placed in the header, immediately after the opening `<body>` tag.  

## Recommended practices  
- Use the `text` option to customize the skip link label (e.g., "Skip to main content").  
- Avoid relying on JavaScript for skip link functionality.  
- Ensure the skip link is the first focusable element on the page.  

## Do  
- Use the `skipLink` macro with the `href` attribute set to `#maincontent`.  
- Include the skip link in the header of every NHS.UK page.  
- Test the skip link with keyboard navigation (Tab key) to ensure it activates correctly.  
- Use the `classes` option to add custom styling if required.  

## Don't  
- Omit the skip link from NHS.UK pages.  
- Use JavaScript to hide or disable the skip link.  
- Set the `href` attribute to a non-existent or incorrect ID (e.g., `#main`).  
- Rely on visual cues alone to indicate the skip link's purpose.  

## Detailed implementation guidance  
1. **HTML structure**:  
   ```html
   <a class="nhsuk-skip-link" data-module="nhsuk-skip-link" href="#maincontent">Skip to main content</a>
   ```  
2. **Nunjucks macro**:  
   ```nunjucks
   {% from "skip-link/macro.njk" import skipLink %}
   {{ skipLink({ href: "#maincontent", text: "Skip to main content" }) }}
   ```  
3. **Customization**:  
   - Use the `html` option to inject custom HTML (e.g., icons).  
   - Add `classes` for styling (e.g., `nhsuk-skip-link--custom`).  

## Decision rules  
- **Use the skip link** if the page has a header with navigation links.  
- **Do not use the skip link** if the page lacks a header or main content section.  
- **Set `href` explicitly** if the main content has an ID other than `maincontent`.  

## Accessibility  
- The skip link must be focusable and visible when activated by a keyboard.  
- Screen readers must announce the skip link as a link to the main content.  
- Ensure the skip link is the first focusable element on the page.  

## Security and data considerations  
- Follow NHS.UK frontend guidelines for sanitizing HTML inputs (e.g., `html` option).  
- Avoid injecting untrusted user-generated content into the skip link.  

## Testing and quality gates  
- **Manual testing**:  
  - Tab through the page to ensure the skip link is the first focusable element.  
  - Verify the skip link jumps to the correct section (`#maincontent`).  
- **Automated testing**:  
  - Use axe or similar tools to check for accessibility violations (e.g., missing `aria-label`).  
  - Validate that the skip link is present on all NHS.UK pages.  

## Common failure modes  
- Missing the skip link on NHS.UK pages.  
- Incorrect `href` value (e.g., `#` or non-existent ID).  
- Skip link not being the first focusable element.  
- Using JavaScript to hide the skip link.  

## Exceptions and deviations  
- **Allowed deviations**:  
  - Non-NHS.UK pages may omit the skip link.  
  - Custom skip link implementations must still follow NHS.UK frontend guidelines.  

## Agent completion checklist  
- [ ] Skip link macro is imported and used correctly.  
- [ ] `href` attribute is set to `#maincontent` (or correct ID).  
- [ ] Skip link is the first focusable element on the page.  
- [ ] Accessibility checks (keyboard navigation, screen reader support) are passed.  
- [ ] Skip link is included in the header of all NHS.UK pages.  

## Related skills  
- Breadcrumbs  
- Header components  
- Footer navigation  
- Accessibility testing  

## Authoritative sources  
- [NHS.UK frontend skip-link documentation](https://nhsuk.github.io/nhsuk-frontend/components/skip-link/)  
- [GOV.UK Design System: Skip links](https://design-system.service.gov.uk/components/skip-link/)  
- [NHS.UK frontend 10.6.0+ release notes](https://github.com/nhsuk/nhsuk-frontend/releases/tag/v10.6.0)
