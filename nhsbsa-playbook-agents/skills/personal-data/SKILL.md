# Coding With Personal Data

Minimise personal data.

Before storing or transmitting personal data, ask:

1. Is the data genuinely required?
2. Is it being sent to an authorised location?
3. Is it protected in transit and storage?
4. Is it being used for the stated/intended purpose?
5. Is its retention period defined?

Never casually put personal data into:

- logs
- URLs
- analytics systems
- source code
- test fixtures
- error messages

Pay particular attention to NHS numbers, identifiers, contact details,
location information, health information and other potentially identifying
combinations.

Do not log personal data simply because debug logging is convenient.

Ensure stored data is deleted according to the applicable retention schedule,
including abandoned/incomplete application data.

Use anonymisation or pseudonymisation deliberately and understand the
difference between the two.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-securely-personal-data/
