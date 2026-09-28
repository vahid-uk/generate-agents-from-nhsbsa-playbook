# Hub page – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/patterns/hub-page/

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

# Pages – Hub page

Hub pages use cards to help users navigate to the content they need.

- HTML code for hub page example

- Nunjucks code for hub page example

```text
<
div
class
=
"nhsuk-width-container"
>
<
nav
class
=
"nhsuk-breadcrumb"
aria-label
=
"Breadcrumb"
>
<
ol
class
=
"nhsuk-breadcrumb__list"
>
<
li
class
=
"nhsuk-breadcrumb__list-item"
>
<
a
class
=
"nhsuk-breadcrumb__link"
href
=
"#"
>
Home
</
a
>
</
li
>
</
ol
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
<
span
class
=
"nhsuk-u-visually-hidden"
>
Back to
</
span
>
Home
</
a
>
</
nav
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
h1
class
=
"nhsuk-heading-xl"
>
NHS services
</
h1
>
<
p
class
=
"nhsuk-body-l"
>
Find out about NHS services such as GPs, pharmacies and hospitals, services near you, and online services to manage your health
</
p
>
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-third nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable"
>
<
div
class
=
"nhsuk-card__content"
>
<
h5
class
=
"nhsuk-card__heading nhsuk-heading-xs"
>
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
Order a repeat prescription
</
a
>
</
h5
>
</
div
>
</
div
>
</
li
>
</
ul
>
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable nhsuk-card--primary"
>
<
div
class
=
"nhsuk-card__content"
>
<
h2
class
=
"nhsuk-card__heading nhsuk-heading-m"
>
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
GPs
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
About GP services, including how to find and register with a local GP and how to book an appointment
</
p
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--chevron-right-circle"
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
"M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-.3 5.8a1 1 0 1 0-1.5 1.4l2.9 2.8-2.9 2.8a1 1 0 0 0 1.5 1.4l3.5-3.5c.4-.4.4-1 0-1.4Z"
/>
</
svg
>
</
div
>
</
div
>
</
li
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable nhsuk-card--primary"
>
<
div
class
=
"nhsuk-card__content"
>
<
h2
class
=
"nhsuk-card__heading nhsuk-heading-m"
>
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
Hospitals
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
About NHS hospitals, booking and changing appointments with the NHS e-Referral Service and going into hospital
</
p
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--chevron-right-circle"
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
"M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-.3 5.8a1 1 0 1 0-1.5 1.4l2.9 2.8-2.9 2.8a1 1 0 0 0 1.5 1.4l3.5-3.5c.4-.4.4-1 0-1.4Z"
/>
</
svg
>
</
div
>
</
div
>
</
li
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable nhsuk-card--primary"
>
<
div
class
=
"nhsuk-card__content"
>
<
h2
class
=
"nhsuk-card__heading nhsuk-heading-m"
>
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
Dentists
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
About NHS dental services, how to find an NHS dentist and how much treatment costs
</
p
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--chevron-right-circle"
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
"M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-.3 5.8a1 1 0 1 0-1.5 1.4l2.9 2.8-2.9 2.8a1 1 0 0 0 1.5 1.4l3.5-3.5c.4-.4.4-1 0-1.4Z"
/>
</
svg
>
</
div
>
</
div
>
</
li
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable nhsuk-card--primary"
>
<
div
class
=
"nhsuk-card__content"
>
<
h2
class
=
"nhsuk-card__heading nhsuk-heading-m"
>
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
Prescriptions
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
Find out about prescriptions including charges, repeat prescriptions and if you can get free prescriptions
</
p
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--chevron-right-circle"
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
"M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-.3 5.8a1 1 0 1 0-1.5 1.4l2.9 2.8-2.9 2.8a1 1 0 0 0 1.5 1.4l3.5-3.5c.4-.4.4-1 0-1.4Z"
/>
</
svg
>
</
div
>
</
div
>
</
li
>
</
ul
>
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable nhsuk-card--secondary"
>
<
div
class
=
"nhsuk-card__content"
>
<
h2
class
=
"nhsuk-card__heading nhsuk-heading-m"
>
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
Services A to Z
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
Use our service finder to find other health services
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
li
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable nhsuk-card--secondary"
>
<
div
class
=
"nhsuk-card__content"
>
<
h2
class
=
"nhsuk-card__heading nhsuk-heading-m"
>
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
Online services
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
Get your NHS number and find out how to view test results online
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
li
>
</
ul
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
"card/macro.njk"
import
card
%}
{%
from
"breadcrumb/macro.njk"
import
breadcrumb
%}
{%
block
beforeContent
%}
{{
breadcrumb
({
items
: [
      {
href
:
"#"
,
text
:
"Home"
}
    ]
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
h1
class
=
"nhsuk-heading-xl"
>
NHS services
</
h1
>
<
p
class
=
"nhsuk-body-l"
>
Find out about NHS services such as GPs, pharmacies and hospitals, services near you, and online services to manage your health
</
p
>
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-third nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"Order a repeat prescription"
,
size
:
"xs"
,
level
:
5
},
href
:
"#"
,
clickable
:
true
})
}}
</
li
>
</
ul
>
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"GPs"
,
size
:
"m"
},
description
:
"About GP services, including how to find and register with a local GP and how to book an appointment"
,
href
:
"#"
,
clickable
:
true
,
variant
:
"primary"
})
}}
</
li
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"Hospitals"
,
size
:
"m"
},
description
:
"About NHS hospitals, booking and changing appointments with the NHS e-Referral Service and going into hospital"
,
href
:
"#"
,
clickable
:
true
,
variant
:
"primary"
})
}}
</
li
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"Dentists"
,
size
:
"m"
},
description
:
"About NHS dental services, how to find an NHS dentist and how much treatment costs"
,
href
:
"#"
,
clickable
:
true
,
variant
:
"primary"
})
}}
</
li
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"Prescriptions"
,
size
:
"m"
},
description
:
"Find out about prescriptions including charges, repeat prescriptions and if you can get free prescriptions"
,
href
:
"#"
,
clickable
:
true
,
variant
:
"primary"
})
}}
</
li
>
</
ul
>
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"Services A to Z"
,
size
:
"m"
},
description
:
"Use our service finder to find other health services"
,
href
:
"#"
,
clickable
:
true
,
variant
:
"secondary"
})
}}
</
li
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"Online services"
,
size
:
"m"
},
description
:
"Get your NHS number and find out how to view test results online"
,
href
:
"#"
,
clickable
:
true
,
variant
:
"secondary"
})
}}
</
li
>
</
ul
>
{%
endblock
%}
```

## When to use this pattern

Use clickable cards on hub pages to signpost groupings of related content and help users find the content they need.

Hub pages work well on large websites. For smaller sites, other components may be enough, for example:

- header navigation

- a mini-hub

- a simple list of links

## When not to use this pattern

Do not use this pattern as a substitute for a clear information architecture. Use the header component, for example, to provide consistent navigation.

Do not use cards to help users navigate a transactional journey. But you may use them to help people find your service start page .

## How this pattern works

This pattern uses 3 types of clickable card, the:

- top task card

- primary card with chevron

- secondary card

Hub pages should include primary cards. They do not need to include top task cards or secondary cards.

Group cards to show a collection of related topics. Prioritise the cards so the content users need most comes first.

Use different card styles to help users understand the importance of different groups of cards.

### Top task card

- HTML code for hub page top task

- Nunjucks code for hub page top task

```text
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-third nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable"
>
<
div
class
=
"nhsuk-card__content"
>
<
h5
class
=
"nhsuk-card__heading nhsuk-heading-xs"
>
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
Order a repeat prescription
</
a
>
</
h5
>
</
div
>
</
div
>
</
li
>
</
ul
>
```

```text
{%
from
"card/macro.njk"
import
card
%}
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-third nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"Order a repeat prescription"
,
size
:
"xs"
,
level
:
5
},
href
:
"#"
,
clickable
:
true
})
}}
</
li
>
</
ul
>
```

Top task cards are small clickable cards.

Use them at the top of hub pages above other cards (such as primary cards) to help users quickly access specific information or tasks buried deeper in the navigation. Use them as shortcuts to content or services that are popular with users or meet an important business need.

If you want to link to a page just below the hub page, use a primary card instead.

Do not use more than 3 top tasks on a hub page.

### Primary card with chevron

- HTML code for hub page primary card

- Nunjucks code for hub page primary card

```text
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-two-thirds nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable nhsuk-card--primary"
>
<
div
class
=
"nhsuk-card__content"
>
<
h2
class
=
"nhsuk-card__heading nhsuk-heading-m"
>
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
GPs
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
About GP services, including how to find and register with a local GP and how to book an appointment
</
p
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--chevron-right-circle"
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
"M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-.3 5.8a1 1 0 1 0-1.5 1.4l2.9 2.8-2.9 2.8a1 1 0 0 0 1.5 1.4l3.5-3.5c.4-.4.4-1 0-1.4Z"
/>
</
svg
>
</
div
>
</
div
>
</
li
>
</
ul
>
```

```text
{%
from
"card/macro.njk"
import
card
%}
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-two-thirds nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"GPs"
,
size
:
"m"
},
description
:
"About GP services, including how to find and register with a local GP and how to book an appointment"
,
href
:
"#"
,
clickable
:
true
,
variant
:
"primary"
})
}}
</
li
>
</
ul
>
```

Use primary cards on hub pages to signpost groups of information that are important to users.

You can include a primary card that links to a single page at a lower level if other primary cards on the same hub page link to groups of content.

The chevron icon (from our icon set ) helps users know the card will take them to more content. The size of the card helps them understand that the topics these cards link to are more frequently visited or more important than topics signposted by secondary cards.

Include a heading with a link and descriptive text.

### Secondary card

- HTML code for hub page secondary card

- Nunjucks code for hub page secondary card

```text
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-two-thirds nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable nhsuk-card--secondary"
>
<
div
class
=
"nhsuk-card__content"
>
<
h2
class
=
"nhsuk-card__heading nhsuk-heading-m"
>
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
Services A to Z
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
Use our service finder to find other health services
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
li
>
</
ul
>
```

```text
{%
from
"card/macro.njk"
import
card
%}
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-two-thirds nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"Services A to Z"
,
size
:
"m"
},
description
:
"Use our service finder to find other health services"
,
href
:
"#"
,
clickable
:
true
,
variant
:
"secondary"
})
}}
</
li
>
</
ul
>
```

Use secondary cards on hub pages to signpost groups of information on less important topics. Use them below primary cards which signpost important information.

Secondary cards have less visual impact than top tasks or primary cards.

Include a heading with a link and descriptive text.

## Research

We tested these 3 card variations as part of an iterative process to improve the NHS website's information architecture and navigation patterns.

We tested the cards in usability sessions and monitored analytics to understand how successful they were.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: April 2026
