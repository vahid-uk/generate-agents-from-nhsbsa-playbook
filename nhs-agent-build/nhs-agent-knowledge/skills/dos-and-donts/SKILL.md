# Do and Don't guidance  

## Purpose  
This skill ensures alignment with the NHS design principles to deliver healthcare services that are inclusive, user-centered, secure, and sustainable. It provides actionable guidance for designing solutions that improve health outcomes, enhance patient experiences, and uphold the values of the NHS.  

## When this skill applies  
This skill applies to:  
- Designing new NHS services, digital tools, or healthcare interventions.  
- Improving existing NHS services to meet evolving user needs and clinical standards.  
- Collaborating across multidisciplinary teams (e.g., clinicians, designers, IT, and patient representatives).  
- Developing solutions for diverse populations (e.g., people with disabilities, elderly users, or those with complex health needs).  

## When this skill does not apply  
This skill does **not** apply to:  
- Projects outside the NHS context (e.g., private healthcare services, non-clinical tools).  
- Non-healthcare-related design work (e.g., infrastructure, non-medical software).  
- Situations where regulatory or legal requirements override design principles (e.g., emergency protocols requiring rapid deployment over iterative testing).  

## NHS requirements  
NHS services must:  
1. Be inclusive and accessible to all users.  
2. Align with clinical and user needs, avoiding unnecessary complexity.  
3. Prioritize trust through reliability and security.  
4. Integrate with existing healthcare infrastructure and workflows.  
5. Support sustainability, including environmental and resource efficiency.  

## Mandatory requirements  
- **Inclusivity**: Ensure services are usable by people with physical, mental health, social, cultural, or learning needs.  
- **Security**: Protect patient data and ensure systems are resilient against breaches.  
- **Testing**: Validate designs with real users and stakeholders.  
- **Transparency**: Document design decisions and share learning openly.  

## Recommended practices  
- Conduct user research with diverse groups, including underrepresented communities.  
- Use iterative prototyping and testing to refine solutions.  
- Collaborate with subject matter experts (e.g., clinicians, ethicists).  
- Document and share feedback, lessons learned, and design decisions.  

---

## Do  
### Inclusivity  
- **Do** design services that accommodate diverse needs (e.g., screen readers for visually impaired users, adjustable text sizes).  
  - *Example*: Use high-contrast color schemes and avoid relying on color alone to convey information.  
- **Do** involve people with lived experience in the design process (e.g., mental health service users in co-design workshops).  

### Context  
- **Do** map the entire user journey, including pre- and post-service interactions.  
  - *Example*: For a diabetes management app, design workflows for medication reminders, GP consultations, and follow-up care.  

### Trust  
- **Do** ensure systems are reliable, with clear data governance and privacy policies.  
  - *Example*: Use encryption for patient data and provide clear opt-in/opt-out mechanisms.  

### Simplicity  
- **Do** simplify complex processes (e.g., breaking down multi-step forms into smaller, logical steps).  
  - *Example*: A telehealth portal that avoids jargon and uses plain language.  

### Openness  
- **Do** share design outcomes and lessons learned to avoid duplication of effort.  
  - *Example*: Publish case studies on the NHS Digital platform.  

---

## Don't  
### Inclusivity  
- **Don't** assume all users have the same level of digital literacy or physical ability.  
  - *Pitfall*: Designing a mobile app without considering users with motor impairments.  
  - *Solution*: Test with users who have disabilities and use accessibility tools (e.g., screen readers).  

### Context  
- **Don't** focus only on isolated features (e.g., a standalone app without integration with GP systems).  
  - *Pitfall*: A mental health tracker that does not sync with care plans, leading to fragmented care.  
  - *Solution*: Map integrations with electronic health records (EHRs) and care pathways.  

### Trust  
- **Don't** compromise on data security to meet deadlines.  
  - *Pitfall*: Rushing to launch a tool without proper encryption, risking data breaches.  
  - *Solution*: Embed security requirements in early design stages (e.g., using ISO 27001-compliant practices).  

### Complexity  
- **Don't** overload users with unnecessary steps or information.  
  - *Pitfall*: A self-referral system with 20+ steps, leading to user drop-offs.  
  - *Solution*: Use user testing to identify and eliminate redundant steps.  

---

## Detailed implementation guidance  

### Step 1: Define User Needs  
- **Action**: Conduct user interviews, surveys, and workshops with diverse stakeholders.  
- **Example**: For a pain management app, interview patients, carers, and clinicians to identify key pain points.  
- **Verification**: Use affinity diagrams to prioritize needs (e.g., "ease of access" vs. "data privacy").  

### Step 2: Design for Inclusivity  
- **Action**: Follow the Web Content Accessibility Guidelines (WCAG) 2.1.  
- **Implementation Example**: Use ARIA labels for interactive elements and ensure keyboard navigation works for all users.  
- **Code Snippet**:  
  ```html  
  <button aria-label="Submit prescription request">Submit</button>  
  ```  

### Step 3: Test with Real Users  
- **Action**: Conduct usability testing with 10–15 representative users.  
- **Example**: Test a telehealth platform with elderly users to identify navigation barriers.  
- **Quality Check**: Use video recordings to analyze user behavior and gather feedback.  

### Step 4: Ensure Security  
- **Action**: Implement end-to-end encryption and regular penetration testing.  
- **Example**: Use HTTPS for data in transit and AES-256 for data at rest.  
- **Verification**: Obtain certifications like ISO 27001 or NHS Digital’s Cyber Essentials.  

---

## Decision rules  
- **Inclusivity**: Use the POUR principles (Perceivable, Operable, Understandable, Robust) from WCAG.  
- **Simplicity**: Apply the "KISS" principle (Keep It Simple, Stupid) to avoid overengineering.  
- **Testing**: Prioritize user testing over assumptions (e.g., validate with 3+ user personas).  

---

## Accessibility  
- **Guidelines**:  
  - Provide text alternatives for non-text content (e.g., alt text for images).  
  - Ensure sufficient color contrast (minimum 4.5:1 for normal text).  
  - Support keyboard-only navigation (e.g., tab order for form fields).  
- **Example**: A radiology portal that includes text transcripts for audio reports.  

---

## Security and data considerations  
- **Requirements**:  
  - Comply with the Data Protection Act 2018 and GDPR.  
  - Use role-based access controls (RBAC) to restrict data access.  
- **Implementation Example**:  
  ```python  
  # Pseudocode for RBAC  
  if user.role == "doctor":  
      allow_access_to("patient_records")  
  else:  
      deny_access()  
  ```  

---

## Testing and quality gates  
- **Quality Gates**:  
  - **Gate 1**: User research and personas validated.  
  - **Gate 2**: Prototypes tested with 10+ users.  
  - **Gate 3**: Security and accessibility audits completed.  
- **Tools**:  
  - Use tools like axe for accessibility testing.  
  - Conduct penetration testing with vendors like Cure53.  

---

## Common failure modes  
- **Failure**: Overlooking cultural needs (e.g., a tool that does not support minority languages).  
  - **Solution**: Engage community leaders to co-design solutions.  
- **Failure**: Poor integration with existing systems (e.g., a tool that duplicates EHR data).  
  - **Solution**: Map system interoperability standards (e.g., FHIR).  

---

## Exceptions and deviations  
- **Exception**: In emergencies, rapid deployment may override iterative testing.  
  - **Handling**: Document the deviation and plan for post-deployment reviews.  
- **Exception**: Limited data access for compliance (e.g., anonymized datasets).  
  - **Handling**: Use synthetic data for testing and obtain ethical approval.  

---

## Agent completion checklist  
- [ ] Conducted user research with diverse stakeholders.  
- [ ] Designed for inclusivity (WCAG compliance).  
- [ ] Tested with real users and iterated based on feedback.  
- [ ] Implemented security measures (encryption, RBAC).  
- [ ] Documented design decisions and shared outcomes.  

---

## Related skills  
- **User Experience (UX) Design**: Ensuring intuitive interfaces.  
- **Health Informatics**: Managing data workflows and interoperability.  
- **Cybersecurity**: Protecting data and systems.  

---

## Authoritative sources  
- [NHS Design Principles](https://www.nhs.uk/design)  
- [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/)  
- [NHS Digital Data Security and Protection Toolkit](https://www.nhs.uk/using-the-nhs/your-rights-and-responsibilities/data-security-and-privacy/)  

--- 

This document ensures alignment with NHS values, provides actionable steps, and avoids assumptions. It emphasizes user-centered design, security, and inclusivity while addressing edge cases and exceptions.
