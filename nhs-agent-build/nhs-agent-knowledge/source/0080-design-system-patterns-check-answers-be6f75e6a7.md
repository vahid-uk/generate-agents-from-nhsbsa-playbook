# Check answers – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/patterns/check-answers/

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

# Help users to – Check answers

Use this pattern to let users check their answers before sending information to a service.

- HTML code for check answers example

- Nunjucks code for check answers example

```text
<
div
class
=
"nhsuk-width-container"
>
<
main
class
=
"nhsuk-main-wrapper"
id
=
"maincontent"
>
<
div
class
=
"nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-two-thirds"
>
<
h1
class
=
"nhsuk-heading-l"
>
Check your answers before sending your application
</
h1
>
<
h2
class
=
"nhsuk-heading-m"
>
Personal details
</
h2
>
<
dl
class
=
"nhsuk-summary-list"
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
NHS number
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
985 777 3456
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
NHS number
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Name
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
Kevin Francis
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
name
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Date of birth
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
15 March 1984
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
date of birth
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Home address
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
8 Bridgewater Place
<
br
>
Leeds
<
br
>
LS11 5BZ
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
home address
</
span
>
</
a
>
</
dd
>
</
div
>
</
dl
>
<
h2
class
=
"nhsuk-heading-m"
>
Medical details
</
h2
>
<
dl
class
=
"nhsuk-summary-list"
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Allergies
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
No allergies
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
allergies
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Conditions
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
Asthma
<
br
>
Disabilities, including physical and learning disabilities
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
conditions
</
span
>
</
a
>
</
dd
>
</
div
>
</
dl
>
<
h2
class
=
"nhsuk-heading-m"
>
Now send your application
</
h2
>
<
p
>
Your details will be sent to Rose Medical Practice to begin your registration.
</
p
>
<
form
action
=
"/form-handler"
method
=
"post"
novalidate
>
<
button
class
=
"nhsuk-button"
data-module
=
"nhsuk-button"
type
=
"submit"
>
Confirm and send
</
button
>
</
form
>
</
div
>
</
div
>
</
main
>
</
div
>
```

```text
{%
from
"button/macro.njk"
import
button
%}
{%
from
"summary-list/macro.njk"
import
summaryList
%}
{%
block
content
%}
<
div
class
=
"nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-two-thirds"
>
<
h1
class
=
"nhsuk-heading-l"
>
Check your answers before sending your application
</
h1
>
<
h2
class
=
"nhsuk-heading-m"
>
Personal details
</
h2
>
{{
summaryList
({
rows
: [
          {
key
: {
text
:
"NHS number"
},
value
: {
text
:
"985 777 3456"
},
actions
: {
items
: [
                {
href
:
"#"
,
text
:
"Change"
,
visuallyHiddenText
:
"NHS number"
}
              ]
            }
          },
          {
key
: {
text
:
"Name"
},
value
: {
text
:
"Kevin Francis"
},
actions
: {
items
: [
                {
href
:
"#"
,
text
:
"Change"
,
visuallyHiddenText
:
"name"
}
              ]
            }
          },
          {
key
: {
text
:
"Date of birth"
},
value
: {
html
:
"15 March 1984"
},
actions
: {
items
: [
                {
href
:
"#"
,
text
:
"Change"
,
visuallyHiddenText
:
"date of birth"
}
              ]
            }
          },
          {
key
: {
text
:
"Home address"
},
value
: {
html
:
"8 Bridgewater Place<br>Leeds<br>LS11 5BZ"
},
actions
: {
items
: [
                {
href
:
"#"
,
text
:
"Change"
,
visuallyHiddenText
:
"home address"
}
              ]
            }
          }
        ]
      })
}}
<
h2
class
=
"nhsuk-heading-m"
>
Medical details
</
h2
>
{{
summaryList
({
rows
: [
          {
key
: {
text
:
"Allergies"
},
value
: {
text
:
"No allergies"
},
actions
: {
items
: [
                {
href
:
"#"
,
text
:
"Change"
,
visuallyHiddenText
:
"allergies"
}
              ]
            }
          },
          {
key
: {
text
:
"Conditions"
},
value
: {
html
:
"Asthma <br> Disabilities, including physical and learning disabilities"
},
actions
: {
items
: [
                {
href
:
"#"
,
text
:
"Change"
,
visuallyHiddenText
:
"conditions"
}
              ]
            }
          }
        ]
      })
}}
<
h2
class
=
"nhsuk-heading-m"
>
Now send your application
</
h2
>
<
p
>
Your details will be sent to Rose Medical Practice to begin your registration.
</
p
>
<
form
action
=
"/form-handler"
method
=
"post"
novalidate
>
{{
button
({
text
:
"Confirm and send"
})
}}
</
form
>
</
div
>
</
div
>
{%
endblock
%}
```

This pattern uses a summary list component for each group of answers on the page.

## When to use this pattern

Show a single check answers page immediately before the confirmation screen for small to medium-size transactions.

When designing a very large transaction with multiple sections, it may help to include a check answers page at the end of each section.

This can be valuable for services where different users might be completing each section. You should test this approach with your users to find out if it's helpful.

## How this pattern works

Check answers pages help to:

- increase users' confidence as they can clearly see that they have completed all the sections and that their data has been captured

- reduce error rates as users are given a chance to notice and correct errors before sending data

### Choose the right layout for the page

Many services ask users for short answers, which are suitable for a layout that takes up two-thirds of the screen on desktop devices. For example, the "Check your answers before sending your application" page included in this guidance.

Using a two-thirds layout stops lines of text getting so long that the page becomes difficult to read. To learn more about line length, see " Layout ". It also means the links are closer to the other content on the page. Users with screen magnifiers are less likely to miss them.

However, if your service asks users for longer or more detailed answers, a full width layout may be more suitable.

### Make the page easy to understand

Use the page title to tell the user what they need to do, otherwise they might miss the "send" button at the end of the page.

On the page, you should also:

- make it clear the transaction will not be complete until a user confirms their information is correct

- break the content up into sections when you can

- only show sections that are relevant to users – for example, if they've said they do not have one or more health conditions, do not show them sections for questions they have not answered about health conditions

- rephrase questions if you need to – for example, you do not need to label every individual line of an address, and you can rewrite long questions as shorter statements

- make sure the "send" button clearly shows the action it performs – for example, "Confirm and send" if data is being sent somewhere, or "Confirm and save" if data is being updated, for example, in a staff-facing system

### Let users go back and change their answers

You should provide a "Change" link next to each section on your check answers page so that users can add or change the information. "Change" links contain hidden text to make them accessible to screen reader users. Update the hidden text to describe what each "Change" link is for.

The answers pages should look the same way they did when the user last used them, with information they have already entered pre-populated.

When they've finished, the "Continue" button should return them to the check answers page. They should not need to go through the rest of the transaction again.

If a user changes their response in a way that means you need to ask them more questions, do this before returning them to the check answers page.

If you have questions that are optional, let users know that they've skipped them without giving an answer by showing their response as "Not provided".

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
