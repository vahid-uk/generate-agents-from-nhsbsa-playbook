# Confirmation page – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/patterns/confirmation-page/

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

# Pages – Confirmation page

Use a confirmation page to show users they have completed a task.

- HTML code for confirmation page

- Nunjucks code for confirmation page

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
div
class
=
"nhsuk-panel"
>
<
h1
class
=
"nhsuk-panel__heading"
>
Booking complete
</
h1
>
<
div
class
=
"nhsuk-panel__body"
>
We have sent you a confirmation email
</
div
>
</
div
>
<
h2
class
=
"nhsuk-heading-m"
>
Your appointment details
</
h2
>
<
dl
class
=
"nhsuk-summary-list nhsuk-summary-list--no-border"
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
Site location
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
St George's Pharmacy
<
br
>
46 St George's Rd
<
br
>
Elephant and Castle
<
br
>
London
<
br
>
SE1 6ET
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
Date and time
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
Thursday 15 June at 9:10am
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
p
>
<
a
href
=
"#"
>
Tell us about your experience using this service
</
a
>
</
p
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
"panel/macro.njk"
import
panel
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
{{
panel
({
titleText
:
"Booking complete"
,
text
:
"We have sent you a confirmation email"
})
}}
<
h2
class
=
"nhsuk-heading-m"
>
Your appointment details
</
h2
>
{%
set
siteLocationHtml
%}
St George's Pharmacy
<
br
>
46 St George's Rd
<
br
>
Elephant and Castle
<
br
>
London
<
br
>
SE1 6ET
{%
endset
%}
{{
summaryList
({
border
:
false
,
rows
: [
          {
key
: {
text
:
"Site location"
},
value
: {
html
: siteLocationHtml
            }
          },
          {
key
: {
text
:
"Date and time"
},
value
: {
text
:
"Thursday 15 June at 9:10am"
}
          }
        ]
      })
}}
<
p
>
<
a
href
=
"#"
>
Tell us about your experience using this service
</
a
>
</
p
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

## When to use a confirmation page

You should use a confirmation page at the end of a transactional journey.

## How to use a confirmation page

Confirmation pages must include:

- a green confirmation panel , with a heading that confirms what the user has done

- details about what will happen next and when

You may also find a need to include:

- an application or reference number, if there is one – include this in the description text in the green panel

- instructions about other steps the user needs to take

- a summary of the details they have submitted

- a way to give feedback about the service

- links to more information or related services that may be helpful

### Explain any reference numbers

Tell people:

- what the reference number is

- why they need it

- if they should keep it (only show a number if people need to keep it)

## How not to use a confirmation page

Avoid including too many different components on a confirmation page. Research suggests they can overwhelm people.

## Accessibility

If you add any interactive elements, make sure the panel or focus state are still accessible.

## Research

In our research, people found the green panel at the top of the confirmation page reassuring. They quickly understood the key message. The left-aligned heading text tested well with people who had visual impairments and used screen readers.

We also tested the green panel with people who had colour blindness. They were able to read the text clearly. They were also able to recognise the shade of green and understood that this was a confirmation page.

Some people became confused about the next step when presented with several different components on a confirmation page. This was especially the case for people who used screen readers.

### Known gaps

We need more evidence to understand whether people:

- find it helpful to save the information on confirmation pages

- try to return to confirmation pages after completing their transaction

In testing, we used a confirmation page at the end of a GP appointment booking journey. Some people said they would take a screenshot of the confirmation page on their phone. GOV.UK found that some users bookmark and return to confirmation pages.

Some people wanted more reassurance that there was nothing more for them to do before their appointment. It may be helpful to say this in the content, when relevant.

We are also looking for more evidence about the green panel at the top of confirmation pages. Particularly:

- any issues with colour contrast

- suitability for people who use reverse colours or are sensitive to light

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: February 2025
