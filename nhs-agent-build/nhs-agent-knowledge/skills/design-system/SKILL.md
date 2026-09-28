# NHS Design System

---

## Purpose

The purpose of the NHS Design System is to ensure a consistent, accessible, and user-centered visual identity across all NHS services in England. By standardizing the use of the NHS Frutiger font, the system enhances brand recognition, improves user experience (UX), and ensures compliance with accessibility and licensing requirements. This consistency is critical for maintaining trust, reducing confusion, and ensuring that all digital and printed materials align with NHS branding guidelines.

---

## When this skill applies

This skill applies to **all NHS organizations in England** that are required to use the NHS Frutiger font in their digital and printed materials. It is particularly relevant for:

- Designing websites, apps, or digital platforms for NHS services.
- Creating marketing, communication, or informational materials (e.g., leaflets, posters, reports).
- Developing internal tools, signage, or publications where the NHS brand must be represented.

It applies to both **new projects** and **existing systems** that require rebranding or updates to align with current NHS standards.

---

## When this skill does not apply

This skill does **not apply** to:

- Non-NHS organizations (e.g., private sector companies, charities, or non-healthcare entities).
- Projects outside the scope of NHS England (e.g., international NHS bodies, devolved administrations in Scotland, Wales, or Northern Ireland).
- Use cases where the Frutiger font is **not required** (e.g., internal tools not facing the public or legacy systems with no rebranding mandate).

---

## NHS Requirements

The NHS requires that all licensed users of the Frutiger font comply with the following:

1. **Font Licensing**: Only use the 3 licensed weights (Frutiger 65 Bold, 55 Roman, and 45 Light for non-applications).
2. **Usage Scope**: Apply the font to **digital and printed materials** for NHS services in England.
3. **Accessibility**: Ensure the font is used in a way that supports readability for all users, including those with visual impairments.
4. **Compliance**: Adhere to the terms of the NHS England licence, including not sharing the font with unlicensed organizations.

---

## Mandatory Requirements

- **Licensing**: A single representative from each NHS organization must register for the free NHS England licence to access the font.
- **Font Weights**: Use only **Frutiger 65 Bold**, **55 Roman**, and **45 Light** (45 Light is **not permitted in apps**).
- **No Unauthorized Use**: Do not use **italic versions**, **unlicensed weights**, or any other Frutiger variants without purchasing a commercial licence.
- **No Redistribution**: The font files must not be shared outside the licensed organization.

---

## Recommended Practices

- **Consistency**: Use the same font weights across all materials for a unified look.
- **Accessibility**: Prioritize **Frutiger 55 Roman** for body text to ensure readability.
- **Testing**: Verify that the font displays correctly on all devices and screen sizes.
- **Documentation**: Maintain a record of font usage and licence compliance within the organization.

---

## Do

- **Use the licensed weights**: Always use **Frutiger 65 Bold**, **55 Roman**, or **45 Light** (for non-apps).
- **Register for a licence**: Ensure your organization has a valid NHS England licence.
- **Host the font locally or use hosted files**: Avoid embedding the font in third-party platforms without licence.
- **Test for accessibility**: Confirm that the font is legible for users with visual impairments (e.g., use sufficient contrast with background colors).

---

## Don't

- **Don't use unlicensed weights**: Avoid **Frutiger Italic**, **45 Light in apps**, or any other unlicensed variants.
- **Don't redistribute font files**: Share the font only within the licensed organization.
- **Don't use the font for non-NHS purposes**: Avoid using it in private sector or non-healthcare projects.
- **Don't assume all weights are available**: Always check the licence terms before using a font.

---

## Detailed Implementation Guidance

### Step-by-Step Process

1. **Register for a Licence**:
   - Visit the NHS England registration page.
   - Provide your organisation’s ODS code and confirm you have authority to register.
   - Download the font files or link to hosted versions.

2. **Implement the Font**:
   - For **digital use**: Add the font to your CSS via `@import` or `@font-face`.
     ```css
     @import url('https://nhs.fonts.com/frutiger/55roman.css');
     body {
       font-family: 'Frutiger 55 Roman', sans-serif;
     }
     ```
   - For **print use**: Install the font locally and embed it in your design tools (e.g., Adobe Illustrator).

3. **Verify Compliance**:
   - Ensure the font is only used in **NHS-related materials**.
   - Confirm that **italic or unlicensed weights** are not present.

4. **Test Accessibility**:
   - Use tools like **WebAIM Contrast Checker** to ensure text is legible on all backgrounds.
   - Avoid low-contrast combinations (e.g., light gray on white).

---

## Decision Rules

- **Use Frutiger 65 Bold** for headings and titles.
- **Use Frutiger 55 Roman** for body text and subheadings.
- **Avoid Frutiger 45 Light** in apps; use it only for print.
- **Reject requests** to use unlicensed weights or italic variants.
- **Consult the NHS England licence** before using the font in non-English NHS contexts.

---

## Accessibility

- **Font Size**: Ensure text is at least **16px** for body text.
- **Contrast**: Use high-contrast color combinations (e.g., dark text on light backgrounds).
- **Readability**: Avoid using **Frutiger 45 Light** for long paragraphs; it may reduce legibility for users with dyslexia.
- **Testing**: Use tools like **Pleiades** (NHS accessibility testing platform) to validate font usage.

---

## Security and Data Considerations

- **Licence Management**: Store the font licence details securely (e.g., in a password-protected internal repository).
- **Font Files**: Do not share font files externally without explicit NHS England approval.
- **Audit Trails**: Maintain logs of font usage to ensure compliance with licence terms.

---

## Testing and Quality Gates

- **Font Validation**: Verify that the correct weights are used in all materials.
- **Accessibility Testing**: Ensure legibility on screens, printers, and mobile devices.
- **Compliance Check**: Confirm that no unlicensed weights or italic variants are present.
- **Peer Review**: Have a colleague or designer review all materials for adherence to the NHS Design System.

---

## Common Failure Modes

1. **Using Unlicensed Weights**: Accidentally using **Frutiger Italic** or **45 Light in apps**.
   - **Solution**: Implement a pre-publishing check for font weights using automated tools.

2. **Incorrect Font Licensing**: Failing to register for the licence.
   - **Solution**: Train staff on the registration process and mandate compliance checks.

3. **Low Contrast**: Using light text on light backgrounds.
   - **Solution**: Use NHS-approved color palettes and test with accessibility tools.

---

## Exceptions and Deviations

- **Non-English NHS Organisations**: Devolved administrations (e.g., Scotland, Wales, Northern Ireland) may use their own fonts.
- **Legacy Systems**: Older systems not requiring rebranding may continue using existing fonts.
- **Special Cases**: For projects requiring **italic fonts**, purchase a commercial licence or use alternative fonts.

---

## Agent Completion Checklist

- [ ] Registered for the NHS England font licence.
- [ ] Used only licensed Frutiger weights (65 Bold, 55 Roman, 45 Light for print).
- [ ] Avoided unlicensed weights (italic, 45 Light for apps).
- [ ] Verified font usage compliance with accessibility guidelines.
- [ ] Conducted peer reviews for all materials.
- [ ] Documented font usage and licence compliance internally.

---

## Related Skills

- **NHS Branding Guidelines**: Ensuring alignment with overall NHS identity standards.
- **Accessibility Standards**: Adhering to WCAG 2.1 for digital and print materials.
- **Typography Best Practices**: Choosing appropriate font weights for readability.
- **Licence Management**: Tracking and managing software licenses for compliance.

---

## Authoritative Sources

- [NHS England Font Licence Terms](https://www.nhs.uk/font-licence)
- [NHS Identity Guidelines](https://www.nhs.uk/identity-guidelines)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Pleiades Accessibility Testing Platform](https://pleiades.nhs.uk/)

--- 

This document ensures that all NHS organisations in England use the Frutiger font in a consistent, compliant, and accessible manner. By following these guidelines, organisations uphold the NHS brand, protect licensing terms, and prioritise user experience.
