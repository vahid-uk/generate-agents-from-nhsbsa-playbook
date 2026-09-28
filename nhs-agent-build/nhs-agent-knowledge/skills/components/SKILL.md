# NHS Design System Components: Skip Link

## Purpose  
The skip link component enables keyboard users to bypass repetitive navigation and jump directly to the main content of a webpage. It is a critical accessibility feature required by the NHS.UK frontend and GOV.UK Design System standards. By providing a visible and focusable link, it ensures users who rely on keyboards or screen readers can navigate efficiently without repeatedly tabbing through headers, menus, or other repetitive elements.

---

## When This Skill Applies  
Use the skip link component in the following scenarios:  
1. **When a webpage contains a header with navigation elements** (e.g., menus, logos, or breadcrumbs) that users might need to bypass.  
2. **When the main content is positioned after the header** (typically within a `<main id="maincontent">` element).  
3. **On all NHS.UK frontend pages** as mandated by the Design System.  

**Example**:  
- A patient portal page with a top navigation bar.  
- A service landing page with a header and footer.  

---

## When This Skill Does Not Apply  
Avoid using the skip link component in the following cases:  
1. **When there is no header or navigation** that requires skipping.  
2. **When the main content is not marked up with an `id="maincontent"`** (the default target for the skip link).  
3. **For pages with dynamic content loading** (e.g., single-page applications) unless the main content is explicitly marked with an `id`.  

**Example**:  
- A static "About Us" page with no navigation.  
- A page using JavaScript to dynamically load content without a fixed `id="maincontent"`.  

---

## NHS Requirements  
- **Compliance with the NHS.UK frontend 10.6.0+**.  
- **Use of the `nhsuk-skip-link` class** for styling.  
- **Ensure the skip link is visually hidden** until it is focused.  
- **Follow GOV.UK accessibility standards** (e.g., keyboard focus, screen reader compatibility).  

**Code Example**:  
```html
<p class="nhsuk-body">
  To view the skip link, tab to this example, or click inside this example and press tab.
</p>
<a class="nhsuk-skip-link" data-module="nhsuk-skip-link" href="#maincontent">
  Skip to main content
</a>
```

---

## Mandatory Requirements  
1. **`href` Attribute**: Must point to `#maincontent` (default) or a valid `id` on the page.  
2. **Text/HTML Content**: Must include either `text` or `html` (but not both). Default is "Skip to main content".  
3. **Class**: Must include `nhsuk-skip-link` for correct styling.  
4. **Focusability**: Must be keyboard focusable and visually hidden until activated.  

**Example with Custom `href`**:  
```html
<a class="nhsuk-skip-link" data-module="nhsuk-skip-link" href="#section-2">
  Skip to section 2
</a>
```

---

## Recommended Practices  
- **Use the default text** ("Skip to main content") unless the page structure requires a different target.  
- **Position the skip link immediately after the opening `<body>` tag** to ensure it is the first focusable element.  
- **Test with screen readers and keyboard navigation** to confirm functionality.  
- **Avoid custom CSS** that overrides the default `nhsuk-skip-link` styling.  

**Custom Text Example**:  
```html
<a class="nhsuk-skip-link" data-module="nhsuk-skip-link" href="#maincontent">
  Skip to main content
</a>
```

---

## Do  
- **Use the skip link** on every NHS.UK frontend page.  
- **Follow the default `href="#maincontent"` convention**.  
- **Ensure the link is focusable and visible when activated**.  
- **Validate the skip link works with screen readers** (e.g., JAWS, NVDA).  

**Implementation Step**:  
1. Add the skip link immediately after the `<body>` tag.  
2. Assign `id="maincontent"` to the main content area.  
3. Test using a keyboard (Tab key) to activate the link.  

---

## Don't  
- **Do not remove or hide the skip link**.  
- **Avoid using JavaScript to hide the skip link** (it must be accessible).  
- **Do not change the `href` to a non-existent `id`** (e.g., `#footer`).  
- **Do not use custom HTML/CSS** that breaks the default behavior.  

**Common Mistake**:  
```html
<!-- ❌ Incorrect: Missing href -->
<a class="nhsuk-skip-link" data-module="nhsuk-skip-link">
  Skip to content
</a>
```

---

## Detailed Implementation Guidance  
### Step-by-Step Implementation  
1. **Add the skip link to the `<body>`**:  
   ```html
   <body>
     <a class="nhsuk-skip-link" data-module="nhsuk-skip-link" href="#maincontent">
       Skip to main content
     </a>
     <!-- Rest of the page -->
   </body>
   ```

2. **Ensure the main content has `id="maincontent"`**:  
   ```html
   <main id="maincontent" class="nhsuk-main-wrapper">
     <!-- Main content here -->
   </main>
   ```

3. **Use the Nunjucks macro** (if applicable):  
   ```nunjucks
   {% from "skip-link/macro.njk" import skipLink %}
   {{ skipLink({ href: "#maincontent", text: "Skip to main content" }) }}
   ```

4. **Add custom attributes if needed** (e.g., `data-*`):  
   ```html
   <a class="nhsuk-skip-link" data-module="nhsuk-skip-link" href="#maincontent" data-test="skip-link">
     Skip to main content
   </a>
   ```

---

## Decision Rules  
- **Default to `#maincontent`** unless the main content has a different `id`.  
- **Use the Nunjucks macro** for consistency with NHS.UK frontend.  
- **Always include the skip link** even if the page is minimal.  
- **Prioritize accessibility over visual design** (e.g., do not hide the link unless it is focusable).  

---

## Accessibility  
- **Keyboard focus**: The skip link must be the first focusable element on the page.  
- **Screen reader compatibility**: Use `aria-label` if the default text is insufficient.  
- **Contrast**: Ensure text meets WCAG 2.1 AA/AAA contrast ratios.  

**Example with `aria-label`**:  
```html
<a class="nhsuk-skip-link" data-module="nhsuk-skip-link" href="#maincontent" aria-label="Skip to main content">
  Skip to main content
</a>
```

---

## Security and Data Considerations  
- **Avoid dynamic `href` values** that could lead to invalid URLs (e.g., user input).  
- **Sanitize `html` content** if using the `html` option in macros.  
- **Prevent XSS vulnerabilities** by validating user-generated content.  

---

## Testing and Quality Gates  
1. **Keyboard navigation**: Tab to the skip link and verify it jumps to the correct section.  
2. **Screen reader test**: Confirm the link is announced correctly.  
3. **Visual inspection**: Ensure the link is hidden until focused.  
4. **Code review**: Check for correct `href`, `id`, and class attributes.  

**Verification Steps**:  
- Use tools like [axe](https://www.deque.com/axe/) for accessibility audits.  
- Validate HTML with the NHS.UK linter.  

---

## Common Failure Modes  
1. **Missing `id="maincontent"`**: The skip link fails to navigate to the correct section.  
2. **Incorrect `href`**: The link points to a non-existent `id`.  
3. **No focusable skip link**: The link is hidden via CSS, breaking accessibility.  
4. **Missing macro**: Custom HTML does not follow NHS.UK frontend conventions.  

**Fix for Missing `id`**:  
```html
<main id="maincontent">
  <!-- Main content -->
</main>
```

---

## Exceptions and Deviations  
- **Exception 1**: Pages without a header or main content.  
  - **Workaround**: Omit the skip link (not recommended; follow NHS.UK guidelines).  
- **Exception 2**: Dynamic content with no fixed `id`.  
  - **Workaround**: Use JavaScript to dynamically set `id="maincontent"`.  

---

## Agent Completion Checklist  
- [ ] Skip link added to `<body>`.  
- [ ] `href` points to `#maincontent` or valid `id`.  
- [ ] Text is "Skip to main content" or customised appropriately.  
- [ ] `nhsuk-skip-link` class applied.  
- [ ] Tested with keyboard and screen readers.  
- [ ] No custom CSS overrides default styling.  

---

## Related Skills  
- **Navigation Menus**: Ensure they are accessible and follow GOV.UK standards.  
- **Focus Management**: Use `tabindex` for dynamic content.  
- **ARIA Attributes**: Apply `aria-label` where needed.  

---

## Authoritative Sources  
1. [NHS.UK Design System – Skip Link](https://nhsuk.github.io/nhsuk-frontend/components/skip-link/)  
2. [GOV.UK Accessibility Standards](https://www.gov.uk/service-manual/design/accessibility)  
3. [W3C ARIA Guidelines](https://www.w3.org/TR/wai-aria/)  

This document ensures compliance with NHS.UK frontend and GOV.UK accessibility standards, providing a robust, accessible skip link implementation.
