# Prototyping: NHS.UK Button Component Implementation

## Purpose  
Deliver a reusable, accessible, and consistent button component that improves user experience through standardized design, ensures compliance with NHS.UK frontend guidelines, and supports both functional and accessibility requirements across digital services. The component must enable clear user actions, reduce cognitive load, and adhere to WCAG 2.1 AA/AAA standards.

---

## When this skill applies  
Use this skill for:  
- **Form interactions** (submit, reset, custom actions)  
- **Navigation links** requiring semantic meaning beyond simple text (e.g., "Continue", "Save changes")  
- **Call-to-action buttons** (e.g., "Book an appointment", "Download document")  
- **Secondary actions** (e.g., "Cancel", "Back")  
- **Buttons with icons** (e.g., search, filter, expand)  
- **Accessibility-critical scenarios** (e.g., screen reader support, keyboard navigation)  

**Example use cases**:  
1. A "Submit application" button in a multi-step form  
2. A "View results" link styled as a button for consistency with other CTA elements  
3. A "Print" button with an icon for users with visual impairments  

---

## When this skill does not apply  
Avoid using this component for:  
- **Simple text links** that do not require semantic emphasis (use `<a>` tags instead)  
- **Radio/checkbox inputs** (use `<input type="radio">` or `<input type="checkbox">`)  
- **Form labels** (use `<label>` elements with `for` attributes)  
- **Buttons that require complex animations** (custom JavaScript required)  
- **Non-interactive elements** (e.g., decorative icons, dividers)  

**Example anti-patterns**:  
- Using a button for "Learn more" when the action is purely informational  
- Applying variants like "brand" to non-CTA elements (e.g., "Close" in a modal)  

---

## NHS Requirements  
Compliance with [NHS.UK frontend guidelines](https://nhsuk.github.io/nhsuk-frontend/components/button/):  
- **Semantic HTML**: Use `<button>` for form actions, `<a>` for navigation  
- **Design system alignment**: Adhere to colour, spacing, and typography standards  
- **Accessibility**: Keyboard focus, ARIA attributes, contrast ratios (minimum 4.5:1)  
- **Responsive design**: Support for mobile, desktop, and high-contrast modes  
- **Consistency**: Use predefined variants (e.g., "brand", "secondary")  

---

## Mandatory Requirements  
1. **HTML Element Selection**:  
   - Use `<button>` for form actions (`type="submit"`, `type="reset"`)  
   - Use `<a>` for navigation (set `href` and `type="button"`)  
2. **Accessibility Attributes**:  
   - `aria-label` for icon-only buttons  
   - `aria-describedby` for buttons requiring additional context  
3. **Required Attributes**:  
   - `text` or `html` for visible content  
   - `variant` for styling (e.g., "brand", "secondary")  
   - `icon` for icon placement (start/end) if used  
4. **Validation**:  
   - Ensure `href` is properly escaped if used  
   - Verify `preventDoubleClick` is enabled for submit actions  

---

## Recommended Practices  
- **Use consistent variants**:  
  - `brand`: Primary CTA (e.g., "Submit")  
  - `secondary`: Secondary actions (e.g., "Cancel")  
  - `reverse`: Inverted text/background for contrast (e.g., "Back")  
- **Prioritize text over icons**:  
  - Icons should supplement, not replace, text (use `aria-label` for screen readers)  
  - Avoid icon-only buttons unless context is clear (e.g., "Close" with an "X" icon)  
- **Optimize for mobile**:  
  - Use `small` variant for tight spaces (e.g., modals, dialogs)  
  - Ensure touch targets are ≥44px in size  
- **Avoid overloading**:  
  - Do not use more than one icon per button  
  - Limit text to 20 characters for small variants  

---

## Do  
✅ **Use Nunjucks macros for consistency**  
```nunjucks
{% from "button/macro.njk" import button %}
{{ button({ text: "Save changes", variant: "brand" }) }}
```  

✅ **Include ARIA labels for icon-only buttons**  
```nunjucks
{{ button({
  html: "<svg>...</svg>",
  ariaLabel: "Search"
}) }}
```  

✅ **Prevent double-clicks on form submissions**  
```nunjucks
{{ button({
  text: "Submit",
  preventDoubleClick: true
}) }}
```  

✅ **Use `href` for navigation links**  
```nunjucks
{{ button({
  text: "View results",
  href: "/results"
}) }}
```  

✅ **Apply variants for semantic meaning**  
```nunjucks
{{ button({ text: "Cancel", variant: "secondary" }) }}
```  

---

## Don't  
❌ **Do not use `<input type="button">`** (use `<button>` instead)  
❌ **Do not omit `aria-label` for icon-only buttons**  
❌ **Do not mix text and icons without spacing** (add `margin` or `padding` in CSS)  
❌ **Do not use `variant: "brand"` for non-CTA actions** (e.g., "Close" in a modal)  
❌ **Do not use `href` with `type: "submit"`** (conflicts with form submission logic)  

---

## Detailed Implementation Guidance  

### Step-by-Step Workflow  
1. **Choose the correct HTML element**:  
   - Use `<button>` for form actions (default `type: "submit"`)  
   - Use `<a>` for navigation (set `href` and `type: "button"`)  

2. **Define content**:  
   - Use `text` for plain text  
   - Use `html` for complex markup (e.g., icons, SVGs)  

3. **Add variants for styling**:  
   ```nunjucks
   {{ button({
     text: "Book now",
     variant: "brand"
   }) }}
   ```  

4. **Add icons (if needed)**:  
   ```nunjucks
   {{ button({
     text: "Search",
     icon: {
       name: "search"
     }
   }) }}
   ```  

5. **Set accessibility attributes**:  
   ```nunjucks
   {{ button({
     html: "<svg>...</svg>",
     ariaLabel: "Filter results"
   }) }}
   ```  

6. **Enable preventDoubleClick for form submissions**:  
   ```nunjucks
   {{ button({
     text: "Submit",
     preventDoubleClick: true
   }) }}
   ```  

7. **Use small variants for tight spaces**:  
   ```nunjucks
   {{ button({
     text: "Next",
     small: true
   }) }}
   ```  

---

## Decision Rules  
- **Use `button` vs `a`**:  
  - Use `button` for actions that change state (e.g., form submission)  
  - Use `a` for navigation to other pages  
- **Variant selection**:  
  - `brand`: Primary action (e.g., "Continue")  
  - `secondary`: Secondary action (e.g., "Cancel")  
  - `reverse`: Inverted for contrast (e.g., "Back" in dark modals)  
- **Icon placement**:  
  - Use `start` for icons before text (e.g., "Search" with magnifying glass)  
  - Use `end` for icons after text (e.g., "Save as PDF" with document icon)  

---

## Accessibility  
- **Keyboard navigation**: Ensure focus states are visible and actionable  
- **Screen readers**: Use `aria-label` for icon-only buttons  
- **Contrast**: Use NHS.UK's brand colours (e.g., `#005EB8` for brand buttons)  
- **Focus order**: Ensure buttons appear in logical tab order  
- **No keyboard traps**: Avoid disabling buttons in a way that prevents navigation  

---

## Security and Data Considerations  
- **Prevent double-clicks**: Use `preventDoubleClick: true` for form submissions  
- **Secure `href` usage**: Escape special characters in URLs (e.g., `&` becomes `&amp;`)  
- **Avoid XSS**: Sanitize `html` input if user-generated content is used  
- **Track analytics**: Add `data-*` attributes for analytics tracking (e.g., `data-tracking-id="submit-button"`)  

---

## Testing and Quality Gates  
1. **Accessibility checks**:  
   - Use axe.js or Lighthouse to validate ARIA attributes  
   - Test keyboard navigation (Tab, Enter, Space)  
2. **Cross-browser compatibility**:  
   - Test in Chrome, Firefox, Safari, and Edge  
   - Ensure consistent styling on mobile and desktop  
3. **Responsive design**:  
   - Verify `small` variant works on mobile  
   - Ensure icons are legible at all screen sizes  
4. **Edge cases**:  
   - Test disabled buttons (grayed out, non-interactive)  
   - Validate `href` with and without `type: "button"`  

---

## Common Failure Modes  
- **Missing ARIA labels**: Icon-only buttons fail screen reader tests  
- **Incorrect variant usage**: `brand` used for non-CTA actions (e.g., "Close")  
- **Double-click issues**: Submit buttons causing duplicate form submissions  
- **Color contrast failures**: Text not meeting 4.5:1 ratio on light backgrounds  
- **Overlapping icons**: Text and icons not spaced properly  

---

## Exceptions and Deviations  
- **Custom variants**: Request approval for non-standard variants (e.g., "error")  
- **Non-NHS styles**: Use `classes` to override default styles if necessary  
- **Legacy systems**: Use `!important` sparingly for CSS overrides  

---

## Agent Completion Checklist  
- [ ] Used correct HTML element (`button`/`a`)  
- [ ] Applied appropriate variant (e.g., `brand`, `secondary`)  
- [ ] Added `aria-label` for icon-only buttons  
- [ ] Enabled `preventDoubleClick` for form submits  
- [ ] Tested keyboard navigation and focus states  
- [ ] Verified contrast ratios meet WCAG standards  
- [ ] Included `href` for navigation links  
- [ ] Used `small` variant for tight spaces  
- [ ] Added `icon` with correct placement (start/end)  
- [ ] Escaped `href` values (e.g., `&amp;`)  

---

## Related Skills  
- [NHS.UK Form Inputs](https://nhsuk.github.io/nhsuk-frontend/components/input/)  
- [NHS.UK Links](https://nhsuk.github.io/nhsuk-frontend/components/link/)  
- [NHS.UK Modals](https://nhsuk.github.io/nhsuk-frontend/components/modal/)  

---

## Authoritative Sources  
1. [NHS.UK Frontend Button Documentation](https://nhsuk.github.io/nhsuk-frontend/components/button/)  
2. [WCAG 2.1 AA/AAA Standards](https://www.w3.org/TR/WCAG21/)  
3. [GOV.UK Design System](https://design-system.service.gov.uk/)  
4. [Nunjucks Macro Syntax Guide](https://mozilla.github.io/nunjucks/)
