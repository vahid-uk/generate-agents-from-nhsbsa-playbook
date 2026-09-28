# Mini-hub – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/patterns/mini-hub/

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

# Pages – Mini-hub

Mini-hubs are a way of presenting a series of related pages about 1 topic, for example a health condition.

- HTML code for mini hub example

- Nunjucks code for mini hub example

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
Health A to Z
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
Health A to Z
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
"nhsuk-heading-xl"
>
What is AMD?
<
span
class
=
"nhsuk-caption-xl nhsuk-caption--bottom"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
–
</
span
>
Age-related macular degeneration (AMD)
</
span
>
</
h1
>
<
nav
class
=
"nhsuk-contents-list"
role
=
"navigation"
aria-label
=
"Pages in this guide"
>
<
h2
class
=
"nhsuk-u-visually-hidden"
>
Contents
</
h2
>
<
ol
class
=
"nhsuk-contents-list__list"
>
<
li
class
=
"nhsuk-contents-list__item"
aria-current
=
"page"
>
<
span
class
=
"nhsuk-contents-list__current"
>
What is AMD?
</
span
>
</
li
>
<
li
class
=
"nhsuk-contents-list__item"
>
<
a
class
=
"nhsuk-contents-list__link"
href
=
"#"
>
Symptoms
</
a
>
</
li
>
<
li
class
=
"nhsuk-contents-list__item"
>
<
a
class
=
"nhsuk-contents-list__link"
href
=
"#"
>
Getting diagnosed
</
a
>
</
li
>
<
li
class
=
"nhsuk-contents-list__item"
>
<
a
class
=
"nhsuk-contents-list__link"
href
=
"#"
>
Treatments
</
a
>
</
li
>
<
li
class
=
"nhsuk-contents-list__item"
>
<
a
class
=
"nhsuk-contents-list__link"
href
=
"#"
>
Living with AMD
</
a
>
</
li
>
</
ol
>
</
nav
>
<
ul
>
<
li
>
<
strong
>
Age-related macular degeneration (AMD) is a common condition that affects the middle part of your vision.
</
strong
>
It usually first affects people in their 50s and 60s.
</
li
>
<
li
>
<
strong
>
It doesn't cause total blindness.
</
strong
>
But it can make everyday activities like reading and recognising faces difficult.
</
li
>
<
li
>
<
strong
>
Without treatment, your vision may get worse.
</
strong
>
This can happen gradually over several years ("dry AMD"), or quickly over a few weeks or months ("wet AMD").
</
li
>
<
li
>
<
strong
>
The exact cause is unknown.
</
strong
>
It's been linked to smoking, high blood pressure, being overweight and having a family history of AMD.
</
li
>
</
ul
>
<
p
class
=
"nhsuk-body-s nhsuk-u-margin-top-7 nhsuk-u-secondary-text-colour"
>
Page last reviewed: 27 March 2018
<
br
>
Next review due: 27 March 2021
</
p
>
<
nav
class
=
"nhsuk-pagination"
role
=
"navigation"
aria-label
=
"Pagination"
>
<
ul
class
=
"nhsuk-list nhsuk-pagination__list"
>
<
li
class
=
"nhsuk-pagination-item--next"
>
<
a
class
=
"nhsuk-pagination__link nhsuk-pagination__link--next"
href
=
"#"
rel
=
"next"
>
<
span
class
=
"nhsuk-pagination__title"
>
Next
<
span
class
=
"nhsuk-u-visually-hidden"
>
page
</
span
>
</
span
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
:
</
span
>
<
span
class
=
"nhsuk-pagination__page"
>
Symptoms
</
span
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--arrow-right"
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
"m14.7 6.3 5 5c.2.2.3.4.3.7 0 .3-.1.5-.3.7l-5 5a1 1 0 0 1-1.4-1.4l3.3-3.3H5a1 1 0 0 1 0-2h11.6l-3.3-3.3a1 1 0 1 1 1.4-1.4Z"
/>
</
svg
>
</
a
>
</
li
>
</
ul
>
</
nav
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
"breadcrumb/macro.njk"
import
breadcrumb
%}
{%
from
"contents-list/macro.njk"
import
contentsList
%}
{%
from
"heading/macro.njk"
import
heading
%}
{%
from
"pagination/macro.njk"
import
pagination
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
},
      {
href
:
"#"
,
text
:
"Health A to Z"
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
heading
({
text
:
"What is AMD?"
,
caption
: {
html
:
'<span class="nhsuk-u-visually-hidden"> – </span>'
~
"Age-related macular degeneration (AMD)"
,
placement
:
"end"
},
size
:
"xl"
})
}}
{{
contentsList
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
"What is AMD?"
,
current
:
true
},
          {
href
:
"#"
,
text
:
"Symptoms"
},
          {
href
:
"#"
,
text
:
"Getting diagnosed"
}
          ,
          {
href
:
"#"
,
text
:
"Treatments"
}
          ,
          {
href
:
"#"
,
text
:
"Living with AMD"
}
        ]
      })
}}
<
ul
>
<
li
>
<
strong
>
Age-related macular degeneration (AMD) is a common condition that affects the middle part of your vision.
</
strong
>
It usually first affects people in their 50s and 60s.
</
li
>
<
li
>
<
strong
>
It doesn't cause total blindness.
</
strong
>
But it can make everyday activities like reading and recognising faces difficult.
</
li
>
<
li
>
<
strong
>
Without treatment, your vision may get worse.
</
strong
>
This can happen gradually over several years ("dry AMD"), or quickly over a few weeks or months ("wet AMD").
</
li
>
<
li
>
<
strong
>
The exact cause is unknown.
</
strong
>
It's been linked to smoking, high blood pressure, being overweight and having a family history of AMD.
</
li
>
</
ul
>
<
p
class
=
"nhsuk-body-s nhsuk-u-margin-top-7 nhsuk-u-secondary-text-colour"
>
Page last reviewed: 27 March 2018
<
br
>
Next review due: 27 March 2021
</
p
>
{{
pagination
({
next
: {
label
:
"Symptoms"
,
href
:
"#"
}
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

The mini-hub is made up of:

- a heading and sub-heading which sit at the top of the page

- a contents list component underneath the heading

- the pagination component which goes at the bottom of the page

## When to use this pattern

Use mini-hubs to present information on 1 complex topic spread over 2 to 8 pages.

We've found that mini-hubs help users understand complex topics, for example health conditions. They break the topic down into manageable chunks and help users digest the information in a way that meets their needs.

But this is not always the case. Test the pattern with your users to make sure that it works for your content.

## When not to use this pattern

Do not use mini-hubs:

- for pages that are about more than 1 topic

- in a transactional service

## Elements of the mini-hub

### Heading and sub-heading

Put an <h1> heading at the top of the page. The first thing in the <h1> heading should be the name of the page you're on, not the mini-hub topic.

Put the mini-hub topic underneath the page heading. We include it in the same <h1> with class="nhsuk-caption-xl nhsuk-caption--bottom" which makes it look like a sub-heading.

The page heading and topic are both part of the <h1> but the page heading looks more important than the topic. (We explain why we do this in the Research section on this page.)

In this example, "What is AMD?" is the heading for the page. "Age-related macular degeneration (AMD)" is the topic.

```text
<
h1
class
=
"nhsuk-heading-xl"
>
What is AMD?
<
span
class
=
"nhsuk-caption-xl nhsuk-caption--bottom"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
–
</
span
>
Age-related macular degeneration (AMD)
</
span
>
</
h1
>
```

### Contents list

Use a contents list at the top of the page, underneath the heading and sub-heading, to help users navigate around a small group of related pages (up to 8 pages), for example a group of pages about a specific health condition. The example on this page is based on an NHS website page about age-related macular degeneration (AMD).

- HTML code for contents list second

- Nunjucks code for contents list second

```text
<
nav
class
=
"nhsuk-contents-list"
role
=
"navigation"
aria-label
=
"Pages in this guide"
>
<
h2
class
=
"nhsuk-u-visually-hidden"
>
Contents
</
h2
>
<
ol
class
=
"nhsuk-contents-list__list"
>
<
li
class
=
"nhsuk-contents-list__item"
aria-current
=
"page"
>
<
span
class
=
"nhsuk-contents-list__current"
>
What is AMD?
</
span
>
</
li
>
<
li
class
=
"nhsuk-contents-list__item"
>
<
a
class
=
"nhsuk-contents-list__link"
href
=
"#"
>
Symptoms
</
a
>
</
li
>
<
li
class
=
"nhsuk-contents-list__item"
>
<
a
class
=
"nhsuk-contents-list__link"
href
=
"#"
>
Getting diagnosed
</
a
>
</
li
>
<
li
class
=
"nhsuk-contents-list__item"
>
<
a
class
=
"nhsuk-contents-list__link"
href
=
"#"
>
Treatments
</
a
>
</
li
>
<
li
class
=
"nhsuk-contents-list__item"
>
<
a
class
=
"nhsuk-contents-list__link"
href
=
"#"
>
Living with AMD
</
a
>
</
li
>
</
ol
>
</
nav
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the contents list.
Name items | Type array | Description Required. Array of contents list items objects. See macro options for items .
Name classes | Type string | Description Classes to add to the contents list container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the contents list container.
Name landmark Label | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the ariaLabel option.
Name aria Label | Type string | Description The accessible name for the navigation landmark that wraps the contents list. Defaults to "Pages in this guide" .
Name visually Hidden Text | Type string | Description Visually hidden heading for the contents list items. Defaults to "Contents" .

Name | Type | Description
Name href | Type string | Description Required. The contents list item href attribute. Required unless item.current is set.
Name current | Type boolean | Description Set to true to indicate the current page the user is on.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each contents list item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each contents list item. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the contents list item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the contents list item.

```text
{%
from
"contents-list/macro.njk"
import
contentsList
%}
{{
contentsList
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
"What is AMD?"
,
current
:
true
},
    {
href
:
"#"
,
text
:
"Symptoms"
},
    {
href
:
"#"
,
text
:
"Getting diagnosed"
}
    ,
    {
href
:
"#"
,
text
:
"Treatments"
}
    ,
    {
href
:
"#"
,
text
:
"Living with AMD"
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Pagination

Use pagination at the bottom of the page to help users navigate around a small group of related pages (up to 8 pages), for example a group of pages about a specific health condition.

- HTML code for pagination content pages

- Nunjucks code for pagination content pages

```text
<
nav
class
=
"nhsuk-pagination"
role
=
"navigation"
aria-label
=
"Pagination"
>
<
ul
class
=
"nhsuk-list nhsuk-pagination__list"
>
<
li
class
=
"nhsuk-pagination-item--previous"
>
<
a
class
=
"nhsuk-pagination__link nhsuk-pagination__link--prev"
href
=
"#"
rel
=
"prev"
>
<
span
class
=
"nhsuk-pagination__title"
>
Previous
<
span
class
=
"nhsuk-u-visually-hidden"
>
page
</
span
>
</
span
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
:
</
span
>
<
span
class
=
"nhsuk-pagination__page"
>
Treatments
</
span
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--arrow-left"
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
"M10.7 6.3c.4.4.4 1 0 1.4L7.4 11H19a1 1 0 0 1 0 2H7.4l3.3 3.3c.4.4.4 1 0 1.4a1 1 0 0 1-1.4 0l-5-5A1 1 0 0 1 4 12c0-.3.1-.5.3-.7l5-5a1 1 0 0 1 1.4 0Z"
/>
</
svg
>
</
a
>
</
li
>
<
li
class
=
"nhsuk-pagination-item--next"
>
<
a
class
=
"nhsuk-pagination__link nhsuk-pagination__link--next"
href
=
"#"
rel
=
"next"
>
<
span
class
=
"nhsuk-pagination__title"
>
Next
<
span
class
=
"nhsuk-u-visually-hidden"
>
page
</
span
>
</
span
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
:
</
span
>
<
span
class
=
"nhsuk-pagination__page"
>
Symptoms
</
span
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--arrow-right"
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
"m14.7 6.3 5 5c.2.2.3.4.3.7 0 .3-.1.5-.3.7l-5 5a1 1 0 0 1-1.4-1.4l3.3-3.3H5a1 1 0 0 1 0-2h11.6l-3.3-3.3a1 1 0 1 1 1.4-1.4Z"
/>
</
svg
>
</
a
>
</
li
>
</
ul
>
</
nav
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the pagination container.
Name items | Type array | Description The items within the pagination component. See macro options for items .
Name previous | Type object | Description A link to the previous page, if there is a previous page. See macro options for previous .
Name previous Url | Type string | Description Deprecated in 10.1.0 (see GitHub) . Replaced by the previous.href option.
Name previous Page | Type string | Description Deprecated in 10.1.0 (see GitHub) . Replaced by the previous.label.text option.
Name next | Type object | Description A link to the next page, if there is a next page. See macro options for next .
Name next Url | Type string | Description Deprecated in 10.1.0 (see GitHub) . Replaced by the next.href option.
Name next Page | Type string | Description Deprecated in 10.1.0 (see GitHub) . Replaced by the next.label.text option.
Name landmark Label | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the ariaLabel option.
Name aria Label | Type string | Description The accessible name for the navigation landmark that wraps the pagination. Defaults to "Pagination" .
Name classes | Type string | Description The classes you want to add to the pagination nav parent.
Name attributes | Type object | Description The HTML attributes (for example, data attributes) you want to add to the pagination nav parent.

Name | Type | Description
Name number | Type string | Description The pagination item text – usually a page number. Required unless the item is an ellipsis.
Name visually Hidden Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . The visually hidden label for the pagination item, which will be applied to an aria-label and announced by screen readers on the pagination item link. Should include page number. Defaults to, for example "Page 1". Replaced by the item.ariaLabel option.
Name aria Label | Type string | Description The accessible name for the pagination item, which will be applied to an aria-label and announced by screen readers on the pagination item link. Should include page number. Defaults to, for example "Page 1".
Name href | Type string | Description Required. The pagination item href attribute. Required unless the item is an ellipsis.
Name current | Type boolean | Description Set to true to indicate the current page the user is on.
Name ellipsis | Type boolean | Description Use this option if you want to specify an ellipsis at a given point between numbers. If you set this option as true , any other options for the item are ignored.
Name attributes | Type object | Description The HTML attributes (for example, data attributes) you want to add to the link.

Name | Type | Description
Name text | Type string | Description The text content of the link to the previous page. Defaults to "Previous page" , with 'page' being visually hidden. If html is provided, the text option will be ignored.
Name html | Type string | Description The HTML content of the link to the previous page. Defaults to "Previous page" , with 'page' being visually hidden. If html is provided, the text option will be ignored.
Name label Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the previous.label.text option.
Name label | Type object | Description The optional label that goes underneath the link to the previous page, providing further context for the user about where the link goes. See macro options for previous label .
Name href | Type string | Description Required. The previous page's URL.
Name attributes | Type object | Description The HTML attributes (for example, data attributes) you want to add to the link.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the label. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description The text content of the link to the next page. Defaults to "Next page" , with 'page' being visually hidden. If html is provided, the text option will be ignored.
Name html | Type string | Description The HTML content of the link to the next page. Defaults to "Next page" , with 'page' being visually hidden. If html is provided, the text option will be ignored.
Name label Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the next.label.text option.
Name label | Type object | Description The optional label that goes underneath the link to the next page, providing further context for the user about where the link goes. See macro options for next label .
Name href | Type string | Description Required. The next page's URL.
Name attributes | Type object | Description The HTML attributes (for example, data attributes) you want to add to the link.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the label. If html is provided, the text option will be ignored.

```text
{%
from
"pagination/macro.njk"
import
pagination
%}
{{
pagination
({
previous
: {
label
:
"Treatments"
,
href
:
"#"
},
next
: {
label
:
"Symptoms"
,
href
:
"#"
}
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## Research on this pattern

We developed the mini-hub pattern for NHS website pages about health conditions.

We tested our information about AMD with a range of users, including disabled people and people with low digital literacy. The Digital Accessibility Centre also tested the pattern.

We found that:

- the structure and labelling of the pages fitted users' mental model and helped them understand the structure of the content

- the active link formatting in the contents list helped users know where they were and, in some cases, it helped them choose the information that was relevant to them

- most users (including a user with very low digital skills) used the pagination to navigate through pages and knew it was related to the contents list at the top of the page

### Heading structure

At first we made the mini-hub topic the main <h1> heading but, when users navigated between pages, it was not obvious to them which page they were on. In some cases they did not realise they had moved between pages. It was only when we made the page heading into the larger <h1> heading that users were clear which page they were on.

We found that screen readers struggled to pronounce the heading and sub-heading together and that confused people. So we've used <span> tags around the headings in the <h1> to help screen readers read more naturally. We've also included <span class="nhsuk-u-visually-hidden">-</span> to add a natural pause.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: October 2025
