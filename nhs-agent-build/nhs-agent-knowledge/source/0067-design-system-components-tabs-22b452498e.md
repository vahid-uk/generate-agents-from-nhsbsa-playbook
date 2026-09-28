# Tabs – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/tabs/

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

# Content presentation – Tabs

The tabs component lets users navigate between related sections of content, displaying 1 section at a time.

- HTML code for tabs

- Nunjucks code for tabs

```text
<
div
class
=
"nhsuk-tabs"
data-module
=
"nhsuk-tabs"
>
<
h2
class
=
"nhsuk-tabs__heading"
>
Contents
</
h2
>
<
ul
class
=
"nhsuk-tabs__list"
>
<
li
class
=
"nhsuk-tabs__list-item nhsuk-tabs__list-item--selected"
>
<
a
class
=
"nhsuk-tabs__tab"
href
=
"#past-day"
>
Past day
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
"nhsuk-tabs__list-item"
>
<
a
class
=
"nhsuk-tabs__tab"
href
=
"#past-week"
>
Past week
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
"nhsuk-tabs__list-item"
>
<
a
class
=
"nhsuk-tabs__tab"
href
=
"#past-month"
>
Past month
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
"nhsuk-tabs__list-item"
>
<
a
class
=
"nhsuk-tabs__tab"
href
=
"#past-year"
>
Past year
</
a
>
</
li
>
</
ul
>
<
div
class
=
"nhsuk-tabs__panel"
id
=
"past-day"
>
<
table
class
=
"nhsuk-table"
>
<
caption
class
=
"nhsuk-table__caption"
>
Past day
</
caption
>
<
thead
class
=
"nhsuk-table__head"
>
<
tr
class
=
"nhsuk-table__row"
>
<
th
class
=
"nhsuk-table__header"
scope
=
"col"
>
Case manager
</
th
>
<
th
class
=
"nhsuk-table__header nhsuk-table__header--numeric"
scope
=
"col"
>
Cases opened
</
th
>
<
th
class
=
"nhsuk-table__header nhsuk-table__header--numeric"
scope
=
"col"
>
Cases closed
</
th
>
</
tr
>
</
thead
>
<
tbody
class
=
"nhsuk-table__body"
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
David Francis
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
3
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
0
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Paul Farmer
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
1
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
0
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Rita Patel
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
2
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
0
</
td
>
</
tr
>
</
tbody
>
</
table
>
</
div
>
<
div
class
=
"nhsuk-tabs__panel nhsuk-tabs__panel--hidden"
id
=
"past-week"
>
<
table
class
=
"nhsuk-table"
>
<
caption
class
=
"nhsuk-table__caption"
>
Past week
</
caption
>
<
thead
class
=
"nhsuk-table__head"
>
<
tr
class
=
"nhsuk-table__row"
>
<
th
class
=
"nhsuk-table__header"
scope
=
"col"
>
Case manager
</
th
>
<
th
class
=
"nhsuk-table__header nhsuk-table__header--numeric"
scope
=
"col"
>
Cases opened
</
th
>
<
th
class
=
"nhsuk-table__header nhsuk-table__header--numeric"
scope
=
"col"
>
Cases closed
</
th
>
</
tr
>
</
thead
>
<
tbody
class
=
"nhsuk-table__body"
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
David Francis
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
24
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
18
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Paul Farmer
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
16
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
20
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Rita Patel
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
24
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
27
</
td
>
</
tr
>
</
tbody
>
</
table
>
</
div
>
<
div
class
=
"nhsuk-tabs__panel nhsuk-tabs__panel--hidden"
id
=
"past-month"
>
<
table
class
=
"nhsuk-table"
>
<
caption
class
=
"nhsuk-table__caption"
>
Past month
</
caption
>
<
thead
class
=
"nhsuk-table__head"
>
<
tr
class
=
"nhsuk-table__row"
>
<
th
class
=
"nhsuk-table__header"
scope
=
"col"
>
Case manager
</
th
>
<
th
class
=
"nhsuk-table__header nhsuk-table__header--numeric"
scope
=
"col"
>
Cases opened
</
th
>
<
th
class
=
"nhsuk-table__header nhsuk-table__header--numeric"
scope
=
"col"
>
Cases closed
</
th
>
</
tr
>
</
thead
>
<
tbody
class
=
"nhsuk-table__body"
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
David Francis
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
98
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
95
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Paul Farmer
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
122
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
131
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Rita Patel
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
126
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
142
</
td
>
</
tr
>
</
tbody
>
</
table
>
</
div
>
<
div
class
=
"nhsuk-tabs__panel nhsuk-tabs__panel--hidden"
id
=
"past-year"
>
<
table
class
=
"nhsuk-table"
>
<
caption
class
=
"nhsuk-table__caption"
>
Past year
</
caption
>
<
thead
class
=
"nhsuk-table__head"
>
<
tr
class
=
"nhsuk-table__row"
>
<
th
class
=
"nhsuk-table__header"
scope
=
"col"
>
Case manager
</
th
>
<
th
class
=
"nhsuk-table__header nhsuk-table__header--numeric"
scope
=
"col"
>
Cases opened
</
th
>
<
th
class
=
"nhsuk-table__header nhsuk-table__header--numeric"
scope
=
"col"
>
Cases closed
</
th
>
</
tr
>
</
thead
>
<
tbody
class
=
"nhsuk-table__body"
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
David Francis
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
1380
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
1472
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Paul Farmer
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
1129
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
1083
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Rita Patel
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
1539
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
1265
</
td
>
</
tr
>
</
tbody
>
</
table
>
</
div
>
</
div
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the tabs component.
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each tab item and panel, separated by - . Defaults to the id option value.
Name title | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the visuallyHiddenText option.
Name visually Hidden Text | Type string | Description Visually hidden heading for the tabs contents list items. Defaults to "Contents" .
Name items | Type array | Description Required. Array of tab items. See macro options for items .
Name classes | Type string | Description Classes to add to the tabs component.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the tabs components.

Name | Type | Description
Name id | Type string | Description Required. Specific id attribute for the tab item. If omitted, then idPrefix string is required instead.
Name label | Type string | Description Required. The text label of a tab item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the tab.
Name panel | Type object | Description Required. Content for the tab panel. See macro options for items panel .

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text for the tab panel. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the tab panel. If html is provided, the text option will be ignored.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the tab panel.

```text
{%
from
"tabs/macro.njk"
import
tabs
%}
{%
from
"tables/macro.njk"
import
table
%}
{%
set
pastDayContent
%}
{{
table
({
caption
:
"Past day"
,
head
: [
      {
text
:
"Case manager"
},
      {
text
:
"Cases opened"
,
format
:
"numeric"
},
      {
text
:
"Cases closed"
,
format
:
"numeric"
}
    ],
rows
: [
      [
        {
text
:
"David Francis"
},
        {
text
:
"3"
,
format
:
"numeric"
},
        {
text
:
"0"
,
format
:
"numeric"
}
      ],
      [
        {
text
:
"Paul Farmer"
},
        {
text
:
"1"
,
format
:
"numeric"
},
        {
text
:
"0"
,
format
:
"numeric"
}
      ],
      [
        {
text
:
"Rita Patel"
},
        {
text
:
"2"
,
format
:
"numeric"
},
        {
text
:
"0"
,
format
:
"numeric"
}
      ]
    ]
  })
}}
{%
endset
-%}
{%
set
pastWeekContent
%}
{{
table
({
caption
:
"Past week"
,
head
: [
      {
text
:
"Case manager"
},
      {
text
:
"Cases opened"
,
format
:
"numeric"
},
      {
text
:
"Cases closed"
,
format
:
"numeric"
}
    ],
rows
: [
      [
        {
text
:
"David Francis"
},
        {
text
:
"24"
,
format
:
"numeric"
},
        {
text
:
"18"
,
format
:
"numeric"
}
      ],
      [
        {
text
:
"Paul Farmer"
},
        {
text
:
"16"
,
format
:
"numeric"
},
        {
text
:
"20"
,
format
:
"numeric"
}
      ],
      [
        {
text
:
"Rita Patel"
},
        {
text
:
"24"
,
format
:
"numeric"
},
        {
text
:
"27"
,
format
:
"numeric"
}
      ]
    ]
  })
}}
{%
endset
-%}
{%
set
pastMonthContent
%}
{{
table
({
caption
:
"Past month"
,
head
: [
      {
text
:
"Case manager"
},
      {
text
:
"Cases opened"
,
format
:
"numeric"
},
      {
text
:
"Cases closed"
,
format
:
"numeric"
}
    ],
rows
: [
      [
        {
text
:
"David Francis"
},
        {
text
:
"98"
,
format
:
"numeric"
},
        {
text
:
"95"
,
format
:
"numeric"
}
      ],
      [
        {
text
:
"Paul Farmer"
},
        {
text
:
"122"
,
format
:
"numeric"
},
        {
text
:
"131"
,
format
:
"numeric"
}
      ],
      [
        {
text
:
"Rita Patel"
},
        {
text
:
"126"
,
format
:
"numeric"
},
        {
text
:
"142"
,
format
:
"numeric"
}
      ]
    ]
  })
}}
{%
endset
-%}
{%
set
pastYearContent
%}
{{
table
({
caption
:
"Past year"
,
head
: [
      {
text
:
"Case manager"
},
      {
text
:
"Cases opened"
,
format
:
"numeric"
},
      {
text
:
"Cases closed"
,
format
:
"numeric"
}
    ],
rows
: [
      [
        {
text
:
"David Francis"
},
        {
text
:
"1380"
,
format
:
"numeric"
},
        {
text
:
"1472"
,
format
:
"numeric"
}
      ],
      [
        {
text
:
"Paul Farmer"
},
        {
text
:
"1129"
,
format
:
"numeric"
},
        {
text
:
"1083"
,
format
:
"numeric"
}
      ],
      [
        {
text
:
"Rita Patel"
},
        {
text
:
"1539"
,
format
:
"numeric"
},
        {
text
:
"1265"
,
format
:
"numeric"
}
      ]
    ]
  })
}}
{%
endset
-%}
{{
tabs
({
items
: [
  {
label
:
"Past day"
,
id
:
"past-day"
,
panel
: {
html
: pastDayContent
      }
    },
    {
label
:
"Past week"
,
id
:
"past-week"
,
panel
: {
html
: pastWeekContent
      }
    },
    {
label
:
"Past month"
,
id
:
"past-month"
,
panel
: {
html
: pastMonthContent
      }
    },
    {
label
:
"Past year"
,
id
:
"past-year"
,
panel
: {
html
: pastYearContent
      }
    }
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## When to use tabs

Tabs can be a helpful way of letting users quickly switch between related information if:

- your content can be usefully separated into clearly labelled sections

- the 1st section is more relevant than the others for most users

- users will not need to view all the sections at once

Tabs can work well for people who use a service regularly, for example, staff using a patient record system. Their need to perform tasks quickly may be greater than their need for simplicity of first-time use.

Test your content without tabs first. Consider if it's better to:

- simplify and reduce the amount of content

- split the content across multiple pages

- keep the content on a single page, separated by headings

- use a table of contents to let users navigate quickly to specific sections of content

## When not to use tabs

Do not use the tabs component if the total amount of content the tabs contain will make the page slow to load. For this reason, do not use the tabs component as a form of page navigation.

Tabs hide content from users and not everyone will notice them or understand how they work.

Do not use tabs if your users might need to:

- read through all of the content in order, for example, to understand a step-by-step process

- compare information in different tabs, because having to memorise information and switch backwards and forwards can be difficult

## Decide between using tabs, expanders and the details component

Tabs, expanders , and details all hide sections of content which a user can choose to reveal.

If you decide to use 1 of these components, consider if:

- the user needs to view more than 1 section at a time – if not, use tabs

- the user needs to switch quickly between sections – tabs can show content without pushing other sections down the page, unlike expanders

- you have 7 or more sections of content – tabs are arranged horizontally, so may not work well, while expanders are arranged vertically

- there are only 1 or 2 sections of short, less important content – the details component is more suitable as it's visually smaller and less prominent than an expander or tabs

## How to use tabs

There are 2 ways to use the tabs component. You can use HTML or, if you're using Nunjucks or the NHS.UK Prototype Kit , you can use the Nunjucks macro.

### Use clear labels

Tabs hide content, so the tab labels need to make it very clear what they link to. Otherwise users will not know if they need to click on them.

If you struggle to come up with clear labels, it might be because the way you've separated the content is not clear.

### Order the tabs according to user needs

The 1st tab should be the most commonly needed section. Arrange the other tabs in the order that makes most sense for your users.

### Do not disable tabs

Disabling elements is normally confusing for users. If there is no content for a tab, either remove the tab or, if that would be confusing for your users, explain why there is no content when the tab is selected.

### Avoid tabs that wrap over more than 1 line

If you use too many tabs or they have long labels then they may wrap over more than 1 line. This makes it harder for users to see the connection between the selected tab and its content.

## Accessibility

Keyboard users should be able to move focus between tabs using arrow keys and select a tab by pressing enter.

Screen reader users should hear which tab is currently focused, how many tabs there are and whether the current tab is open.

## Progressive enhancement

The tabs component uses progressive enhancement and requires JavaScript for enhanced functionality.

When JavaScript is not available, users will see the tabbed content on a single page, in order from 1st to last, with a table of contents that links to each of the sections.

This is also how the component currently behaves on small screens, but more research is needed on this.

## Research and testing

The Government Digital Service (GDS) developed and tested the tabs component. Several NHS services are using tabs but we need to know more about how they test with users.

For example, we need to know:

- which types of services tabs work best in

- that this approach to tabs is the best option for screen reader users and sighted keyboard users

- how this component should behave on small screen sizes

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
