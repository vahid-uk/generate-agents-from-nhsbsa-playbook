# NHS design system patterns  

## Purpose  
Ensure consistency, usability, and accessibility in NHS service design by applying standardized patterns and components.  

## When this skill applies  
- Designing start pages, forms, or interactive elements for NHS services.  
- Developing digital tools, apps, or websites that align with NHS design principles.  
- Collaborating on cross-service components (e.g., buttons, navigation, error messages).  

## When this skill does not apply  
- Non-NHS contexts (e.g., private healthcare, non-clinical services).  
- Situations where legal, regulatory, or safety requirements explicitly override patterns.  

## NHS requirements  
- Adherence to NHS design system patterns (e.g., start pages, buttons, forms).  
- Integration of accessibility, security, and user-centered design principles.  
- Alignment with NHS values (e.g., equity, transparency, sustainability).  

## Mandatory requirements  
1. **Start page pattern**  
   - Use a "Start now" button as the primary call-to-action.  
   - Keep the start page brief, focusing on the main task.  

2. **Accessibility**  
   - Ensure screen reader compatibility and keyboard navigation.  
   - Use semantic HTML and ARIA labels where necessary.  

3. **Security and data**  
   - Protect user data with encryption and secure authentication.  
   - Comply with GDPR and NHS data policies.  

## Recommended practices  
- **Use a CMS for updates**: Allow non-developers to edit content.  
- **Set clear URLs**: Embed start pages in the NHS website structure.  
- **Avoid overloading start pages**: Limit information to essential details.  

## Do  
- Use a "Start now" button for all service start pages.  
- Keep start pages concise and focused on the user’s goal.  
- Test patterns with real users and accessibility tools.  

## Don't  
- Overload start pages with eligibility criteria or lengthy explanations.  
- Use action links instead of buttons for primary calls to action.  
- Ignore accessibility guidelines (e.g., skip links, alt text).  

## Detailed implementation guidance  
### Start page pattern  
- **When to use**: As the first screen for a service or task.  
- **When not to use**: For internal tools or non-public-facing services.  
- **Implementation**:  
  - Place the "Start now" button above the fold.  
  - Use clear headings and minimal text.  
  - Include links to policy or contact information in the footer.  
- **Accessibility**:  
  - Ensure the button is keyboard-focusable and screen-reader-friendly.  
  - Avoid relying on color alone to convey information.  

### Buttons  
- **When to use**: For primary actions (e.g., "Start now," "Submit").  
- **When not to use**: For secondary or non-essential actions.  
- **Implementation**:  
  - Use consistent sizing, spacing, and color.  
  - Label buttons with clear, action-oriented verbs.  
- **Accessibility**:  
  - Use `button` elements with `aria-label` if text is not visible.  
  - Ensure contrast meets WCAG 2.1 standards.  

## Decision rules  
- **Start page**: Use only if the service requires a multi-step process.  
- **Buttons**: Prioritize "Start now" for all public-facing services.  
- **Accessibility**: Always test with screen readers and color contrast tools.  

## Accessibility  
- Ensure all components are compatible with assistive technologies.  
- Use semantic HTML (e.g., `<button>`, `<form>`, `<label>`).  
- Provide alternative text for non-text content (e.g., icons, images).  

## Security and data considerations  
- Encrypt sensitive data in transit and at rest.  
- Use NHS-approved authentication methods (e.g., OAuth, SSO).  
- Regularly audit for vulnerabilities (e.g., XSS, SQL injection).  

## Testing and quality gates  
- Conduct user testing with diverse groups (including people with disabilities).  
- Validate accessibility with tools like axe or Lighthouse.  
- Peer review all components for compliance with NHS design system standards.  

## Common failure modes  
- Overcomplicating start pages with unnecessary information.  
- Ignoring accessibility guidelines, leading to poor user experience.  
- Failing to test patterns with real users, resulting in usability issues.  

## Exceptions and deviations  
- **Allowed deviations**:  
  - Use context-specific verbs (e.g., "Book now") if research supports it.  
  - Adjust start page length for complex services with clear justification.  
- **Approval required**: Deviations must be documented and approved by the NHS design team.  

## Agent completion checklist  
- [ ] Used "Start now" button for all public-facing services.  
- [ ] Tested components with accessibility tools and users.  
- [ ] Ensured compliance with NHS design system patterns.  
- [ ] Included policy and contact links in the footer.  
- [ ] Validated security and data practices.  

## Related skills  
- User experience (UX) design  
- Service design  
- Accessibility standards (WCAG)  
- Data protection and privacy  

## Authoritative sources  
- [NHS Design System Patterns](https://www.nhs.uk/design-system/patterns/)  
- [GOV.UK Design System](https://design-system.service.gov.uk/)  
- [NHS Digital Accessibility Guidelines](https://www.nhs.uk/using-the-nhs/online-services/accessibility/)  

---  
*Note: This document is based on the NHS design system patterns and must be updated as new guidelines are released.*
