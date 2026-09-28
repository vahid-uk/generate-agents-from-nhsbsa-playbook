# Coding and engineering practices

## Purpose  
Ensure all NHSBSA Git repositories have clear, user-focused READMEs that help users understand, evaluate, use, and contribute to projects. READMEs must be written in plain English, avoid assumptions about prior knowledge, and follow a standardized structure.

---

## When this skill applies  
- For every NHSBSA Git repository.  
- When creating or updating documentation for public-facing projects.  

## When this skill does not apply  
- For internal-only tools or repositories not intended for external use.  
- For legacy systems where documentation is not required.  

---

## NHS requirements  
- All repositories must include a README.  
- READMEs must be written in plain English, avoiding jargon.  
- Technical terms must be defined for clarity.  
- No assumptions about prior knowledge of the project.  

---

## Mandatory requirements  
1. **README presence**: Every repository must have a README.  
2. **Template compliance**: Use the NHSBSA README template.  
3. **Testing**: Instructions must be tested before publication.  

---

## Recommended practices  
- Keep READMEs concise; move detailed documentation (e.g., API references) to a `docs/` folder.  
- Use clear headings and bullet points for readability.  
- Link to external resources (e.g., license files, contribution guidelines).  

---

## Do  
- Use plain English and define technical terms.  
- Test instructions with a team member before publishing.  
- Follow the NHSBSA README template structure.  
- Include sections: **About the project**, **Quick start**, **How to contribute**, **License**.  

## Don't  
- Use phrases like "just" or "simply" (assume no prior knowledge).  
- Assume users have prior knowledge of the project.  
- Overload READMEs with detailed technical information.  

---

## Detailed implementation guidance  
- **Structure**:  
  - **About the project**: Describe the purpose, scope, and audience.  
  - **Quick start**: Include steps to build and run the application.  
  - **How to contribute**: Outline contribution processes (e.g., GitHub workflows).  
  - **License**: Reference the project’s license file.  
- **Language**: Avoid markdown; use plain text with clear headings.  
- **Testing**: Validate instructions with a team member to ensure usability.  

---

## Decision rules  
- Use this skill for projects requiring external documentation.  
- Skip for internal-only tools or legacy systems without documentation requirements.  

---

## Accessibility  
- Ensure text is readable by users with disabilities (e.g., screen readers).  
- Use clear headings and avoid complex formatting.  
- Provide alt text for images or diagrams in the README.  

---

## Security and data considerations  
- Not applicable (no specific security requirements in the source material).  

---

## Testing and quality gates  
- **Test instructions**: Before publishing, verify that users can follow the README steps.  
- **Quality gate**: Ensure all mandatory sections are present and functional.  

---

## Common failure modes  
- **Overly verbose READMEs**: Move detailed content to `docs/`.  
- **Untested instructions**: Validate steps with a team member.  
- **Missing sections**: Ensure all mandatory sections (e.g., license) are included.  

---

## Exceptions and deviations  
- **Internal projects**: Not required to follow this skill.  
- **Legacy systems**: Documentation may not be mandatory.  

---

## Agent completion checklist  
- [ ] README exists for the repository.  
- [ ] README follows the NHSBSA template.  
- [ ] Instructions are tested and functional.  
- [ ] All mandatory sections are present.  
- [ ] Language is plain English with no jargon.  

---

## Related skills  
- Documentation writing.  
- Accessibility testing.  
- Testing and quality assurance.  

---

## Authoritative sources  
- [NHSBSA Digital, Data and Technology Playbook - Writing READMEs](https://nhsbsa.github.io/nhsbsa-digital-playbook/development/dev-documentation-readme/)
