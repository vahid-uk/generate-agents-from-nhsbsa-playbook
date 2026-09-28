# NHS Design System Patterns  

## Purpose  
The NHS Design System Patterns provide a standardized framework for creating consistent, user-centered digital services across the National Health Service (NHS). These patterns ensure that services are accessible, efficient, and aligned with user needs while adhering to NHS principles such as inclusivity, simplicity, and trust. By following these patterns, teams can improve user experience, reduce duplication of effort, and ensure compliance with regulatory and accessibility requirements.  

## When this skill applies  
This skill applies to:  
- Designing new NHS digital services (e.g., online booking systems, patient portals, or appointment scheduling tools).  
- Redesigning existing NHS services to align with current design standards.  
- Integrating components into larger NHS systems where consistency and usability are critical (e.g., shared patient records or telehealth platforms).  
- Projects requiring compliance with NHS accessibility and data protection standards.  

## When this skill does not apply  
This skill does not apply to:  
- Non-digital services (e.g., in-person consultations or paper-based processes).  
- Projects outside the NHS context (e.g., private healthcare providers or non-UK healthcare systems).  
- Situations where rapid prototyping or experimental features are required without adherence to formal design patterns.  

---

## NHS Requirements  
To comply with NHS design principles, the following must be met:  
1. **User-centered design**: Services must prioritize user needs through research and testing.  
2. **Accessibility**: Ensure services are usable by people with disabilities, including screen readers, color contrast, and keyboard navigation.  
3. **Consistency**: Use standardized components and patterns (e.g., buttons, forms, and navigation) across all NHS services.  
4. **Trust and security**: Protect user data and ensure transparency in service operations.  
5. **Simplicity**: Avoid unnecessary complexity in user journeys and interfaces.  

## Mandatory Requirements  
- All services must include a **start page** with a clear "Start now" button as the primary call-to-action.  
- Services must provide **accessible links** to policy, privacy notices, and contact information.  
- All forms must follow **GOV.UK design standards** for validation, error messages, and labels.  
- Services must be **responsive** and functional on mobile devices.  
- Data handling must comply with **NHS digital security and privacy guidelines**.  

## Recommended Practices  
- Use the **start page pattern** to guide users to the next step without overwhelming them with information.  
- Conduct **user testing** with diverse groups, including people with disabilities, to validate design choices.  
- Regularly update the start page to reflect service changes (e.g., new eligibility criteria or availability).  
- Avoid **overloading** the start page with text or options; keep it concise and focused on the primary action.  
- Use **plain language** for all content to ensure clarity and reduce user confusion.  

---

## Do  
- **Use the "Start now" button** as the primary action on the start page.  
- **Test with real users** to identify accessibility and usability issues.  
- **Include a footer** with links to privacy policies, contact details, and service-specific information.  
- **Break down complex tasks** into smaller steps (e.g., using a multi-step form for booking an appointment).  
- **Provide clear error messages** for forms, explaining how to correct mistakes.  

## Don't  
- **Do not use action links** (e.g., "Book now") on the start page instead of buttons.  
- **Do not hide critical information** (e.g., eligibility criteria) on the start page.  
- **Do not assume user knowledge** about NHS processes or terminology.  
- **Do not use non-standard components** (e.g., custom buttons or fonts) that deviate from the NHS Design System.  
- **Do not skip accessibility checks** during testing or deployment.  

---

## Detailed Implementation Guidance  
### Start Page Implementation  
1. **Structure the start page**:  
   - Place the "Start now" button prominently at the top of the page.  
   - Include a brief description of the service (e.g., "Book a hospital appointment").  
   - Add a short paragraph explaining what the service does and who it’s for.  
2. **Add necessary links**:  
   - Include a footer with links to:  
     - Privacy policy  
     - Terms and conditions  
     - Contact details (e.g., a helpdesk email or phone number)  
3. **Ensure accessibility**:  
   - Use semantic HTML for buttons and links (e.g., `<button>` for the "Start now" action).  
   - Add `alt` text for images and ensure sufficient color contrast.  
4. **Test with users**:  
   - Conduct usability tests with people using screen readers and magnification tools.  
   - Verify that the "Start now" button is the first focusable element on the page.  

### Example Code Snippet for Start Page  
```html
<div class="nhs-start-page">
  <h1>Book a hospital appointment</h1>
  <p>This service helps you book an appointment at your local NHS hospital.</p>
  <button class="nhs-button--primary" aria-label="Start booking an appointment">Start now</button>
  <footer>
    <p><a href="/privacy-policy">Privacy policy</a> | <a href="/contact">Contact us</a></p>
  </footer>
</div>
```  

---

## Decision Rules  
- **When to use the start page pattern**:  
  - When the service requires user input (e.g., booking, registration, or eligibility checks).  
  - When the service has multiple steps (e.g., forms, questionnaires, or multi-step processes).  
- **When not to use the start page pattern**:  
  - For emergency services where immediate action is required (e.g., 999 call systems).  
  - For internal NHS tools not accessed by the general public (e.g., staff dashboards).  

---

## Accessibility  
- **Screen reader compatibility**:  
  - Ensure all interactive elements (buttons, links) are labeled correctly.  
  - Use ARIA attributes (e.g., `aria-label`, `aria-describedby`) for non-text elements.  
- **Keyboard navigation**:  
  - Ensure the "Start now" button is reachable via the Tab key and has a visible focus state.  
- **Text size and contrast**:  
  - Use high-contrast colors (e.g., black text on white background) for readability.  
  - Avoid small font sizes (minimum 16px for body text).  

---

## Security and Data Considerations  
- **Data protection**:  
  - Encrypt user data in transit and at rest (e.g., using HTTPS and AES-256 encryption).  
  - Avoid storing sensitive data (e.g., medical records) on client-side devices unless necessary.  
- **Authentication**:  
  - Use NHS login systems (e.g., the NHS App or SPID) for secure user identification.  
  - Implement multi-factor authentication (MFA) for sensitive services.  

---

## Testing and Quality Gates  
- **User testing**:  
  - Conduct at least two rounds of usability testing with diverse user groups.  
  - Validate that the "Start now" button is the first actionable element on the page.  
- **Accessibility checks**:  
  - Use tools like axe or WAVE to audit for WCAG compliance.  
  - Test with screen readers (e.g., NVDA, JAWS) and magnification tools.  
- **Compliance checks**:  
  - Verify that all links in the footer are functional and relevant.  
  - Ensure forms follow GOV.UK validation standards (e.g., error messages, required fields).  

---

## Common Failure Modes  
1. **Overloading the start page with text**:  
   - **Solution**: Use a brief summary and move detailed information to subsequent steps.  
2. **Missing accessibility checks**:  
   - **Solution**: Integrate automated testing tools and manual testing with users.  
3. **Non-standard components**:  
   - **Solution**: Use NHS-approved design system components (e.g., buttons, forms).  

---

## Exceptions and Deviations  
- **Emergency services**:  
  - Deviate from the start page pattern if speed is critical (e.g., urgent care bookings).  
  - **Implementation**: Use a simplified interface with a single action button (e.g., "Get help now").  
- **Internal tools**:  
  - Exclude public-facing links (e.g., privacy policy) if the tool is for staff only.  

---

## Agent Completion Checklist  
- [ ] Start page includes a "Start now" button as the primary action.  
- [ ] Footer contains links to privacy policy and contact details.  
- [ ] All interactive elements are accessible (keyboard navigation, screen reader compatibility).  
- [ ] Forms follow GOV.UK validation and error handling standards.  
- [ ] User testing has been conducted with diverse groups.  
- [ ] Compliance with NHS design system patterns has been verified.  

---

## Related Skills  
- **NHS Design Principles** (e.g., inclusivity, simplicity, and trust).  
- **Accessibility Compliance** (e.g., WCAG 2.1 standards).  
- **Data Security** (e.g., NHS digital security frameworks).  
- **User Research** (e.g., conducting interviews and usability tests).  

---

## Authoritative Sources  
1. [NHS Digital Design System](https://www.nhs.uk/design-system/)  
2. [GOV.UK Design System](https://design-system.gov.uk/)  
3. [NHS Accessibility Standards](https://www.nhs.uk/using-the-nhs/accessible-information/)  
4. [WCAG 2.1 Guidelines](https://www.w3.org/TR/WCAG21/)  

--- 

This document ensures adherence to NHS design system patterns, improving user experience, accessibility, and compliance across digital services. By following these guidelines, teams can create consistent, secure, and user-friendly solutions that align with NHS values.
