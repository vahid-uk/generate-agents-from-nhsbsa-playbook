# Contents list – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/contents-list/

## Source content

## Form elements

- Buttons

- Character count

- Checkboxes

- Date input

- Error message

- Error summary

- Fieldset

- File upload

- Hint text

- Password input

- Radios

- Search input

- Select

- Text input

- Textarea

## Content presentation

- Card

- Details

- Do and Don't lists

- Expander

- Images

- Inset text

- Notification banners

- Panel

- Review date

- Summary list

- Table

- Tabs

- Tag

- Task list

- Warning callout

## Navigation

- Action link

- Back link

- Breadcrumbs

- Contents list

- Footer

- Header

- Pagination

- Skip link

# Navigation – Contents list

Use contents lists to help users to navigate through a series of related pages, for example about a health condition.

- HTML code for contents list

- Nunjucks code for contents list

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

## When to use a contents list

Use a contents list at the top of the page to help users to navigate around a small group of related pages (up to 8 pages), for example a group of pages about a specific health condition. The example on this page is based on an NHS website page about age-related macular degeneration (AMD).

If you're using a contents list, you should also use pagination at the bottom of the page. The 2 components make up the mini-hub pattern .

## When not to use a contents list

Do not use a contents list on pages which are not grouped together or "related" as this is likely confuse users.

Do not use pagination to navigate through a multi-page form. We use other components instead, including:

- buttons (usually a "Continue" button) to move forward back link to navigate back

- back link to navigate back

## How to use a contents list

Use the contents list at the top of the page together with pagination at the bottom of each page.

Keep links short and descriptive. Links that are too long (more than 2 lines) make it difficult for users to scan the list.

Page titles must reflect the subject of the page (for example, "Treatment"), with the overall subject of the section as the sub-header (for example, "Age-related macular degeneration (AMD)"). This is so users are clear where they have navigated to.

### Accessibility

The list of links is surrounded by a <nav> element to show that they are navigation links. This element has an aria-label attribute with the value Pages in this guide . Screen readers that support this attribute will read this out and that makes it clear what the list of links is.

There is also a visually hidden heading title Contents which screen readers will read as a heading to the links.

If the link describes the current page that you are on, then it has the aria-current="page" value to indicate to screen readers that this is the case.

## Research

We tested contents lists in grouped information pages, like the AMD page on the website, but not on forms.

Users understood and engaged with the contents list navigation and said that it fitted how they thought the content would be made up.

The active link formatting helped users know where they were.

Some users said that the page titles helped them orientate themselves, so they knew they were in the right place. Some felt that the links helped them understand what information there was and choose what was relevant to them.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: October 2025
