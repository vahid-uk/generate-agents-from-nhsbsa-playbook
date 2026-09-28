# Decide when and where to get care (care cards) – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/patterns/help-users-decide-when-and-where-to-get-care/

## Source content

## Ask users for

- NHS numbers

## Help users to

- Check answers

- Complete multiple tasks

- Decide when and where to get care (care cards)

- Find British Sign Language content

- Know that a page is up to date

## Pages

- A to Z page

- Confirmation page

- Hub page

- Interruption page

- Mini-hub

- Question pages

- Start page

# Help users to – Decide when and where to get care (care cards)

Care cards help users identify and understand the care they need, who to contact and how quickly.

## When to use this pattern

Use this pattern if you need to tell users to take action to get medical advice or help.

## When not to use this pattern

Do not use this pattern:

- for information which is not about helping users understand the care they need now

- in question pages in a transactional journey

- to warn users about something – use a warning callout instead

- to stop users in a journey, unless it's to tell them to get medical help now – consider using an interruption page instead

- to signpost users to the start of a digital service – use an action link , for example, to find a pharmacy

- to point users to another organisation, like a charity – use inset text or just link from a line of text

- to give users a brief summary of content or a task, often with a link to more detail – use a card

## How it works

We have 3 care cards for 3 levels of care:

- non-urgent care card (blue)

- urgent care card (red)

- emergency care card (red and dark grey)

You can use more than 1 care card on a page, for example if people need different kinds of care depending on how severe their symptoms are.

Avoid having too many care cards on the page. We want to give essential information and reassure people, not to scare them. Only include more than 1 of each type if you can show a clear clinical or user need.

If you have 2 care cards close together, order them according to the likelihood and seriousness of symptoms. For example:

- for headaches, start with a non-urgent care card

- for head injury, start with an emergency care card

Be aware that users often overlook text between components, for example if you have:

- 2 care cards close together

- a care card near another component such as a warning callout

### Non-urgent care card (blue)

Use the non-urgent care card when you want users to contact a health professional such as their GP.

You can also use it to tell people to get advice from a pharmacist or to go to a clinic, for example for a chlamydia test.

- HTML code for help users decide when and where to get care non urgent

- Nunjucks code for help users decide when and where to get care non urgent

```text
<
div
class
=
"nhsuk-card nhsuk-card--care nhsuk-card--care--non-urgent"
>
<
div
class
=
"nhsuk-card__heading-container"
>
<
h2
class
=
"nhsuk-card__heading"
>
<
span
role
=
"text"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Non-urgent advice:
</
span
>
See a GP if:
</
span
>
</
h2
>
<
span
class
=
"nhsuk-card--care__arrow"
aria-hidden
=
"true"
>
</
span
>
</
div
>
<
div
class
=
"nhsuk-card__content"
>
<
ul
>
<
li
>
you're not sure it's chickenpox
</
li
>
<
li
>
you're breastfeeding and have chickenpox symptoms
</
li
>
</
ul
>
<
p
>
Contact the GP surgery before you go in and tell the receptionist you think it might be chickenpox.
</
p
>
</
div
>
</
div
>
```

```text
{%
from
"card/macro.njk"
import
card
%}
{%
set
cardDescriptionHtml
%}
<
ul
>
<
li
>
you're not sure it's chickenpox
</
li
>
<
li
>
you're breastfeeding and have chickenpox symptoms
</
li
>
</
ul
>
<
p
>
Contact the GP surgery before you go in and tell the receptionist you think it might be chickenpox.
</
p
>
{%
endset
%}
{{
card
({
heading
:
"See a GP if:"
,
description
: {
html
: cardDescriptionHtml
  },
variant
:
"non-urgent"
})
}}
```

### Urgent care card (red)

Use the urgent care card if you want users to act quickly but it's not an emergency.

You can, for example, use the urgent care card to tell people to:

- make an urgent GP appointment

- contact 111

- go to a walk-in centre or minor injuries centre

If appropriate, tell users to ask for an urgent appointment when they ring their GP practice. It can help make sure they see someone quickly.

- HTML code for help users decide when and where to get care urgent

- Nunjucks code for help users decide when and where to get care urgent

```text
<
div
class
=
"nhsuk-card nhsuk-card--care nhsuk-card--care--urgent"
>
<
div
class
=
"nhsuk-card__heading-container"
>
<
h2
class
=
"nhsuk-card__heading"
>
<
span
role
=
"text"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Urgent advice:
</
span
>
Ask for an urgent GP appointment or get help from NHS 111 if you have:
</
span
>
</
h2
>
<
span
class
=
"nhsuk-card--care__arrow"
aria-hidden
=
"true"
>
</
span
>
</
div
>
<
div
class
=
"nhsuk-card__content"
>
<
ul
>
<
li
>
pain in your eyes
</
li
>
<
li
>
changes to your vision, such as vision loss or blurred vision
</
li
>
<
li
>
very red eyes
</
li
>
</
ul
>
<
p
>
These can be signs of a more serious eye problem.
</
p
>
<
p
>
You can call 111 or
<
a
href
=
"#"
>
get help from 111 online
</
a
>
.
</
p
>
</
div
>
</
div
>
```

```text
{%
from
"card/macro.njk"
import
card
%}
{%
set
cardDescriptionHtml
%}
<
ul
>
<
li
>
pain in your eyes
</
li
>
<
li
>
changes to your vision, such as vision loss or blurred vision
</
li
>
<
li
>
very red eyes
</
li
>
</
ul
>
<
p
>
These can be signs of a more serious eye problem.
</
p
>
<
p
>
You can call 111 or
<
a
href
=
"#"
>
get help from 111 online
</
a
>
.
</
p
>
{%
endset
%}
{{
card
({
heading
:
"Ask for an urgent GP appointment or get help from NHS 111 if you have:"
,
description
: {
html
: cardDescriptionHtml
  },
variant
:
"urgent"
})
}}
```

### Emergency care card (red and dark grey)

If users need to get emergency help straight away, use the emergency care card. Depending on clinical advice, tell them to call 999 now, go to A&E now or mention both.

You can add an action link to help users find their nearest A&E. Do not include other links in an emergency care card.

Only use this card for emergencies.

- HTML code for help users decide when and where to get care emergency

- Nunjucks code for help users decide when and where to get care emergency

```text
<
div
class
=
"nhsuk-card nhsuk-card--care nhsuk-card--care--emergency"
>
<
div
class
=
"nhsuk-card__heading-container"
>
<
h2
class
=
"nhsuk-card__heading"
>
<
span
role
=
"text"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Immediate action required:
</
span
>
Call 999 or go to A
&amp;
E now if:
</
span
>
</
h2
>
<
span
class
=
"nhsuk-card--care__arrow"
aria-hidden
=
"true"
>
</
span
>
</
div
>
<
div
class
=
"nhsuk-card__content"
>
<
ul
>
<
li
>
you get sudden chest pain
</
li
>
<
li
>
you have severe difficulty breathing – you're gasping, choking or not able to get words out
</
li
>
<
li
>
you start coughing up blood
</
li
>
</
ul
>
<
a
class
=
"nhsuk-action-link nhsuk-action-link--reverse"
href
=
"#"
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--arrow-right-circle"
xmlns
=
"http://www.w3.org/2000/svg"
viewBox
=
"0 0 24 24"
width
=
"16"
height
=
"16"
focusable
=
"false"
aria-hidden
=
"true"
>
<
path
d
=
"M12 2a10 10 0 0 0-10 9h11.7l-4-4a1 1 0 0 1 1.5-1.4l5.6 5.7a1 1 0 0 1 0 1.4l-5.6 5.7a1 1 0 0 1-1.5 0 1 1 0 0 1 0-1.4l4-4H2A10 10 0 1 0 12 2z"
/>
</
svg
>
<
span
class
=
"nhsuk-action-link__text"
>
Find your nearest A
&amp;
E
</
span
>
</
a
>
</
div
>
</
div
>
```

```text
{%
from
"card/macro.njk"
import
card
%}
{%
from
"action-link/macro.njk"
import
actionLink
%}
{%
set
cardDescriptionHtml
%}
<
ul
>
<
li
>
you get sudden chest pain
</
li
>
<
li
>
you have severe difficulty breathing – you're gasping, choking or not able to get words out
</
li
>
<
li
>
you start coughing up blood
</
li
>
</
ul
>
{{
actionLink
({
text
:
"Find your nearest A&E"
,
href
:
"#"
,
variant
:
"reverse"
})
}}
{%
endset
%}
{{
card
({
heading
:
"Call 999 or go to A&E now if:"
,
description
: {
html
: cardDescriptionHtml
  },
variant
:
"emergency"
})
}}
```

## Care card content

### Use short clear headings

The card's heading should be 1 clear call to action. Use the format: "Call 111 if:" or "Speak to a GP if:" followed by a bulleted list in the body of the card.

People with visual disabilities may not recognise care cards by their colour. Use the card's heading to tell them what to do. This will also help people who are stressed or need to act quickly.

To help care cards stand out from other components, you can put them under a heading. For example, "When and where to get medical help".

If you have any text below a care card, screen reader users may assume that it's part of the care card, unless you give it its own heading.

Follow our guidance on headings , including heading structure.

### Keep the card content brief and specific

Try to keep bullet points short and to limit your list to the most likely symptoms or scenarios, but follow clinical advice. In an urgent care card, you can add a final catch-all bullet point such as "you or your child have any other symptoms you're worried about".

Avoid vague or subjective language. Instead of "a young child", for example, say "a child aged 5 years or younger".

### Put the detail in the body of the card

Do not overload the heading. Use the space in the body of the card, but keep it short.

Even if your care card includes only 1 symptom, use a bullet point under the "if:" in the heading. It's clearer than including a stand-alone sentence in the card.

It's also OK to have 2 colons, 1 in the heading and 1 in the body of the card, as in this example.

- HTML code for help users decide when and where to get care two colons

- Nunjucks code for help users decide when and where to get care two colons

```text
<
div
class
=
"nhsuk-card nhsuk-card--care nhsuk-card--care--emergency"
>
<
div
class
=
"nhsuk-card__heading-container"
>
<
h2
class
=
"nhsuk-card__heading"
>
<
span
role
=
"text"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Immediate action required:
</
span
>
Call 999 or go to A
&amp;
E if:
</
span
>
</
h2
>
<
span
class
=
"nhsuk-card--care__arrow"
aria-hidden
=
"true"
>
</
span
>
</
div
>
<
div
class
=
"nhsuk-card__content"
>
<
p
>
You've been exposed to very cold temperatures and:
</
p
>
<
ul
>
<
li
>
have hard, frozen skin
</
li
>
<
li
>
have swelling and loss of feeling in the affected area
</
li
>
<
li
>
have blisters filled with blood or a clear or milky fluid
</
li
>
<
li
>
you're constantly shivering, have slurred speech, slow breathing and are tired and confused
</
li
>
</
ul
>
<
a
class
=
"nhsuk-action-link nhsuk-action-link--reverse"
href
=
"#"
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--arrow-right-circle"
xmlns
=
"http://www.w3.org/2000/svg"
viewBox
=
"0 0 24 24"
width
=
"16"
height
=
"16"
focusable
=
"false"
aria-hidden
=
"true"
>
<
path
d
=
"M12 2a10 10 0 0 0-10 9h11.7l-4-4a1 1 0 0 1 1.5-1.4l5.6 5.7a1 1 0 0 1 0 1.4l-5.6 5.7a1 1 0 0 1-1.5 0 1 1 0 0 1 0-1.4l4-4H2A10 10 0 1 0 12 2z"
/>
</
svg
>
<
span
class
=
"nhsuk-action-link__text"
>
Find your nearest A
&amp;
E
</
span
>
</
a
>
</
div
>
</
div
>
```

```text
{%
from
"card/macro.njk"
import
card
%}
{%
from
"action-link/macro.njk"
import
actionLink
%}
{%
set
cardDescriptionHtml
%}
<
p
>
You've been exposed to very cold temperatures and:
</
p
>
<
ul
>
<
li
>
have hard, frozen skin
</
li
>
<
li
>
have swelling and loss of feeling in the affected area
</
li
>
<
li
>
have blisters filled with blood or a clear or milky fluid
</
li
>
<
li
>
you're constantly shivering, have slurred speech, slow breathing and are tired and confused
</
li
>
</
ul
>
{{
actionLink
({
text
:
"Find your nearest A&E"
,
href
:
"#"
,
variant
:
"reverse"
})
}}
{%
endset
%}
{{
card
({
heading
:
"Call 999 or go to A&E if:"
,
description
: {
html
: cardDescriptionHtml
  },
variant
:
"emergency"
})
}}
```

### Keep signposting simple

Ideally you should signpost to just 1 service in the heading but you can signpost to 2 (the top 2 services). If you need to, add more services at the end of the body of the care card.

## Accessibility

Each care card includes hidden text to make the level of urgency clear to people who use screen readers. This also helps people who use headings to navigate the page as the text is part of the heading.

<h3><span class="visually-hidden">Non-urgent advice</span> Speak to a GP if:<h3>

## Research

We tested care cards with 1 call to action, for example "Speak to a GP if:". We found that users scanning the page stopped to read the care cards and understood what action to take.

We tested the cards again in 2026 and updated the guidance about how the pattern works and writing care card content.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: August 2026
