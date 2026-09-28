# Interruption page – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/patterns/interruption-page/

## Explicit Do guidance

- HTML code for interruption page confirmation
- Nunjucks code for interruption page confirmation
- HTML code for interruption page second
- Nunjucks code for interruption page second

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

# Pages – Interruption page

If you need to pause a user's journey with important information, use an interruption page.

- HTML code for interruption page

- Nunjucks code for interruption page

```text
<
div
class
=
"nhsuk-width-container"
>
<
a
class
=
"nhsuk-back-link"
href
=
"#"
>
Back
</
a
>
<
main
class
=
"nhsuk-main-wrapper nhsuk-main-wrapper--s"
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
div
class
=
"nhsuk-panel nhsuk-panel--interruption"
>
<
h1
class
=
"nhsuk-panel__heading nhsuk-panel__heading--l"
>
Jodie Brown had a COVID-19 vaccine less than 3 months ago
</
h1
>
<
div
class
=
"nhsuk-panel__body"
>
<
p
>
They had a COVID-19 vaccine on 25 December 2025.
</
p
>
<
p
>
For most people, the minimum recommended gap between COVID-19 vaccine doses is 3 months.
</
p
>
<
div
class
=
"nhsuk-button-group"
>
<
a
class
=
"nhsuk-button nhsuk-button--reverse"
data-module
=
"nhsuk-button"
href
=
"#"
role
=
"button"
draggable
=
"false"
>
Continue anyway
</
a
>
<
a
href
=
"#"
>
Cancel
</
a
>
</
div
>
</
div
>
</
div
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
"back-link/macro.njk"
import
backLink
%}
{%
from
"button/macro.njk"
import
button
%}
{%
from
"panel/macro.njk"
import
panel
%}
{%
set
mainClasses
=
"nhsuk-main-wrapper--s"
%}
{%
block
beforeContent
%}
{{
backLink
({
href
:
"#"
,
text
:
"Back"
})
}}
{%
endblock
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
{%
set
panelHtml
%}
<
p
>
They had a COVID-19 vaccine on 25 December 2025.
</
p
>
<
p
>
For most people, the minimum recommended gap between COVID-19 vaccine doses is 3 months.
</
p
>
<
div
class
=
"nhsuk-button-group"
>
{{
button
({
text
:
"Continue anyway"
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
<
a
href
=
"#"
>
Cancel
</
a
>
</
div
>
{%
endset
%}
{{
panel
({
heading
: {
text
:
"Jodie Brown had a COVID-19 vaccine less than 3 months ago"
,
size
:
"l"
},
html
: panelHtml,
variant
:
"interruption"
})
}}
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

## When to use an interruption page

The interruption page is visually different from other components and patterns in order to draw a user's attention to something important.

Only use an interruption page when you need to make sure that the user is not about to make a mistake.

Use interruption pages sparingly. The more often a user sees them, the more likely they are to skip over the content.

Try using a regular page first, and only use the interruption page if you find in research that users are often missing the content. Please feed back any user research you do on this pattern.

For example use it to:

- ask users to check a likely mistake

- ask users to confirm something which cannot be undone

- warn professionals they are about to do something risky

### Check a likely mistake

If the user has entered some information which is likely to be a mistake, but is not impossible, you can use an interruption card to ask them to check if what they have entered is correct.

Unlike a validation error in an error summary , they can continue without changing their answer.

- HTML code for interruption page possible mistake

- Nunjucks code for interruption page possible mistake

```text
<
div
class
=
"nhsuk-width-container"
>
<
a
class
=
"nhsuk-back-link"
href
=
"#"
>
Back
</
a
>
<
main
class
=
"nhsuk-main-wrapper nhsuk-main-wrapper--s"
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
div
class
=
"nhsuk-panel nhsuk-panel--interruption"
>
<
h1
class
=
"nhsuk-panel__heading nhsuk-panel__heading--l"
>
Is your weight correct?
</
h1
>
<
div
class
=
"nhsuk-panel__body"
>
<
p
>
You entered your weight as
<
strong
>
21.4 kilograms
</
strong
>
. This is lower than expected.
</
p
>
<
div
class
=
"nhsuk-button-group"
>
<
a
class
=
"nhsuk-button nhsuk-button--reverse"
data-module
=
"nhsuk-button"
href
=
"#"
role
=
"button"
draggable
=
"false"
>
Yes, this is correct
</
a
>
<
a
href
=
"#"
>
Change my weight
</
a
>
</
div
>
</
div
>
</
div
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
"back-link/macro.njk"
import
backLink
%}
{%
from
"button/macro.njk"
import
button
%}
{%
from
"panel/macro.njk"
import
panel
%}
{%
set
mainClasses
=
"nhsuk-main-wrapper--s"
%}
{%
block
beforeContent
%}
{{
backLink
({
href
:
"#"
,
text
:
"Back"
})
}}
{%
endblock
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
{%
set
panelHtml
%}
<
p
>
You entered your weight as
<
strong
>
21.4 kilograms
</
strong
>
. This is lower than expected.
</
p
>
<
div
class
=
"nhsuk-button-group"
>
{{
button
({
text
:
"Yes, this is correct"
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
<
a
href
=
"#"
>
Change my weight
</
a
>
</
div
>
{%
endset
%}
{{
panel
({
heading
: {
text
:
"Is your weight correct?"
,
size
:
"l"
},
html
: panelHtml,
variant
:
"interruption"
})
}}
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

### Confirm something which cannot be undone

If the user is about to do something unusual which cannot be undone and could have serious consequences, such as cancelling a hospital appointment, you can use an interruption page to check with them first.

Do not use this pattern if the outcome is less serious, such as unsubscribing from notifications.

Do not use this pattern to ask a user to check all their answers as part of a regular journey. Use the check answers pattern instead.

- HTML code for interruption page confirmation

- Nunjucks code for interruption page confirmation

```text
<
div
class
=
"nhsuk-width-container"
>
<
a
class
=
"nhsuk-back-link"
href
=
"#"
>
Back
</
a
>
<
main
class
=
"nhsuk-main-wrapper nhsuk-main-wrapper--s"
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
div
class
=
"nhsuk-panel nhsuk-panel--interruption"
>
<
h1
class
=
"nhsuk-panel__heading nhsuk-panel__heading--l"
>
Confirm you want to cancel your hospital appointment
</
h1
>
<
div
class
=
"nhsuk-panel__body"
>
<
p
>
You will be able to reschedule your appointment for another time, but this may delay your treatment.
</
p
>
<
p
>
Cancelling your appointment cannot be undone.
</
p
>
<
div
class
=
"nhsuk-button-group"
>
<
a
class
=
"nhsuk-button nhsuk-button--reverse"
data-module
=
"nhsuk-button"
href
=
"#"
role
=
"button"
draggable
=
"false"
>
Cancel appointment
</
a
>
</
div
>
</
div
>
</
div
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
"back-link/macro.njk"
import
backLink
%}
{%
from
"button/macro.njk"
import
button
%}
{%
from
"panel/macro.njk"
import
panel
%}
{%
set
mainClasses
=
"nhsuk-main-wrapper--s"
%}
{%
block
beforeContent
%}
{{
backLink
({
href
:
"#"
,
text
:
"Back"
})
}}
{%
endblock
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
{%
set
panelHtml
%}
<
p
>
You will be able to reschedule your appointment for another time, but this may delay your treatment.
</
p
>
<
p
>
Cancelling your appointment cannot be undone.
</
p
>
<
div
class
=
"nhsuk-button-group"
>
{{
button
({
text
:
"Cancel appointment"
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
</
div
>
{%
endset
%}
{{
panel
({
heading
: {
text
:
"Confirm you want to cancel your hospital appointment"
,
size
:
"l"
},
html
: panelHtml,
variant
:
"interruption"
})
}}
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

### Warn professionals they are about to do something risky

In a staff-facing service you can use an interruption page to make professionals, for example clinicians, aware that they're doing something unusual and potentially risky, but that they can choose to go ahead based upon their professional judgement.

If the action should never be taken, you should prevent it from happening.

Use this warning sparingly.

- HTML code for interruption page second

- Nunjucks code for interruption page second

```text
<
div
class
=
"nhsuk-width-container"
>
<
a
class
=
"nhsuk-back-link"
href
=
"#"
>
Back
</
a
>
<
main
class
=
"nhsuk-main-wrapper nhsuk-main-wrapper--s"
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
div
class
=
"nhsuk-panel nhsuk-panel--interruption"
>
<
h1
class
=
"nhsuk-panel__heading nhsuk-panel__heading--l"
>
Jodie Brown had a COVID-19 vaccine less than 3 months ago
</
h1
>
<
div
class
=
"nhsuk-panel__body"
>
<
p
>
They had a COVID-19 vaccine on 25 December 2025.
</
p
>
<
p
>
For most people, the minimum recommended gap between COVID-19 vaccine doses is 3 months.
</
p
>
<
div
class
=
"nhsuk-button-group"
>
<
a
class
=
"nhsuk-button nhsuk-button--reverse"
data-module
=
"nhsuk-button"
href
=
"#"
role
=
"button"
draggable
=
"false"
>
Continue anyway
</
a
>
<
a
href
=
"#"
>
Cancel
</
a
>
</
div
>
</
div
>
</
div
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
"back-link/macro.njk"
import
backLink
%}
{%
from
"button/macro.njk"
import
button
%}
{%
from
"panel/macro.njk"
import
panel
%}
{%
set
mainClasses
=
"nhsuk-main-wrapper--s"
%}
{%
block
beforeContent
%}
{{
backLink
({
href
:
"#"
,
text
:
"Back"
})
}}
{%
endblock
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
{%
set
panelHtml
%}
<
p
>
They had a COVID-19 vaccine on 25 December 2025.
</
p
>
<
p
>
For most people, the minimum recommended gap between COVID-19 vaccine doses is 3 months.
</
p
>
<
div
class
=
"nhsuk-button-group"
>
{{
button
({
text
:
"Continue anyway"
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
<
a
href
=
"#"
>
Cancel
</
a
>
</
div
>
{%
endset
%}
{{
panel
({
heading
: {
text
:
"Jodie Brown had a COVID-19 vaccine less than 3 months ago"
,
size
:
"l"
},
html
: panelHtml,
variant
:
"interruption"
})
}}
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

## When not to use an interruption page

Do not use an interruption card to:

- highlight important text on a page of content – consider using inset text instead

- warn users on a page of long-form content – use a warning callout instead

- ask users to agree to terms of use or other legal terms

- display content that the user will see repeatedly

- show users they have completed a task – use a confirmation page instead

## How to use an interruption page

The interruption page uses the panel component with the addition of a nhsuk-panel--interruption class to make it blue. The button should have a nhsuk-button--reverse class to make it appear white.

Keep the content on the interruption page as brief as possible.

### Back links and cancel buttons

Include a back link at the top of the page to allow users to go back 1 step. Also allow users to use their browser back button.

If it's helpful to cancel the journey and jump back multiple steps or to a different part of the service, use an additional link grouped with the primary button. Label the link so that users know what will happen and where it will take them. To do this, add a <div class="nhsuk-button-group"> container to group the button and the link together.

Do not include a cancel link if it takes you back to the same page as the back link.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: May 2026
