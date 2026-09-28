# Table – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/table/

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

# Content presentation – Table

Use a table to make it easier for users to scan and compare data or information.

We have 6 kinds of table:

- basic

- compact

- striped

- responsive

- scrolling

- sortable

The page also explains how to:

- use word breaks in a table

- display missing data

- display tables on dark backgrounds

## When to use a table

Use a table to:

- present data or information that can be organised in a structured way

- make it easy for users to scan and compare information and understand relationships between data

Aim to present a minimum of data. If you have a lot of data, try to organise it into multiple tables or multiple pages.

## When not to use a table

Use tables with caution. They may not be the best way to present information, especially for the public and on mobile screens. In staff services, complex data tables can lead to cognitive overload, a poor user experience and performance issues.

There may be better ways to meet users' needs, for example:

- a plain English summary with headings and lists

- an expander

- tabs

Check this in your user research.

Do not use a table to lay out content on a page. Use the grid system instead.

## Basic table

### 2 column table

- HTML code for table basic

- Nunjucks code for table basic

```text
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
Skin symptoms and possible causes
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
Skin symptoms
</
th
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
Possible cause
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Blisters on lips or around the mouth
</
th
>
<
td
class
=
"nhsuk-table__cell"
>
Cold sores
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Itchy, dry, cracked, sore
</
th
>
<
td
class
=
"nhsuk-table__cell"
>
Eczema
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Itchy blisters
</
th
>
<
td
class
=
"nhsuk-table__cell"
>
Shingles, chickenpox
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the table.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. Array of table rows and cells. See macro options for rows .
Name head | Type array | Description Array of table head cells. See macro options for head .
Name caption | Type object | Description Table caption. See macro options for caption .
Name caption Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option.
Name caption Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option.
Name first Cell Is Header | Type boolean | Description If set to true , first cell in table row will be a th instead of a td .
Name compact | Type boolean | Description If set to true , vertical padding will be reduced for table cells.
Name responsive | Type boolean | Description If set to true , responsive table classes will be applied.
Name scroll | Type boolean | Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options.
Name striped | Type boolean | Description If set to true , striped background colours will be applied to table rows.
Name variant | Type string | Description Optional variant of table. You can use only "reverse" or empty values with this option.
Name card | Type object | Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card .
Name panel | Type boolean | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option.
Name panel Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option.
Name heading | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option.
Name heading Level | Type integer | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option.
Name classes | Type string | Description Classes to add to the table container.
Name table Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table container.
Name ascending Text | Type string | Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" .
Name descending Text | Type string | Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" .
Name sort Announcement Text | Type string | Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table cell.
Name header | Type string | Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option.
Name href | Type string | Description If set, the table cell will become a link.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name sort Value | Type string | Description Sort value text for cells in table rows.
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table cell.

Name | Type | Description
Name text | Type string | Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored.
Name html | Type string | Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table head cell.
Name href | Type string | Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table head cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table head cell.
Name sort | Type string | Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true .
Name sort Next | Type string | Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" .

Name | Type | Description
Name id | Type string | Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option.
Name text | Type string | Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" .
Name caption | Type object | Description Optional caption for the table caption. See macro options for caption .
Name size | Type string | Description Size of the table caption – "s" , "m" , "l" or "xl" .
Name classes | Type string | Description Classes to add to the table caption, for example "nhsuk-table__caption--l" .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table caption.

Name | Type | Description
Name id | Type string | Description The ID of the caption.
Name element | Type string | Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" .
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block.
Name placement | Type string | Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" .
Name size | Type string | Description Size of the caption – "m" , "l" , "xl" or "xxl" .
Name classes | Type string | Description Classes to add to the caption.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the caption.

```text
{%
from
"tables/macro.njk"
import
table
%}
{{
table
({
caption
:
"Skin symptoms and possible causes"
,
firstCellIsHeader
:
true
,
head
: [
    {
text
:
"Skin symptoms"
},
    {
text
:
"Possible cause"
}
  ],
rows
: [
    [
      {
text
:
"Blisters on lips or around the mouth"
},
      {
text
:
"Cold sores"
}
    ],
    [
      {
text
:
"Itchy, dry, cracked, sore"
},
      {
text
:
"Eczema"
}
    ],
    [
      {
text
:
"Itchy blisters"
},
      {
text
:
"Shingles, chickenpox"
}
    ]
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### 3 or more column table

If you have numeric data, right align the column header and cells to make it easier to compare numbers:

- in Nunjucks, add the format: "numeric" option to the column header

- for HTML, add the nhsuk-table__header--numeric class to the column header and nhsuk-table__cell--numeric class to the cells

If you have non-numeric data that you want to right align:

- in Nunjucks, add the align: "right" option to the column header

- for HTML, add the nhsuk-u-text-align-right override class to both the column header and cells

- HTML code for table 3 column

- Nunjucks code for table 3 column

```text
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
Prescription prepayment certificate (PPC) charges
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
Item
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
Current charge
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
New charge
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
3-month
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
£31.25
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
£32.05
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
12-month
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
£111.60
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
£114.50
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
HRT
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
£19.30
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
£19.80
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the table.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. Array of table rows and cells. See macro options for rows .
Name head | Type array | Description Array of table head cells. See macro options for head .
Name caption | Type object | Description Table caption. See macro options for caption .
Name caption Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option.
Name caption Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option.
Name first Cell Is Header | Type boolean | Description If set to true , first cell in table row will be a th instead of a td .
Name compact | Type boolean | Description If set to true , vertical padding will be reduced for table cells.
Name responsive | Type boolean | Description If set to true , responsive table classes will be applied.
Name scroll | Type boolean | Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options.
Name striped | Type boolean | Description If set to true , striped background colours will be applied to table rows.
Name variant | Type string | Description Optional variant of table. You can use only "reverse" or empty values with this option.
Name card | Type object | Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card .
Name panel | Type boolean | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option.
Name panel Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option.
Name heading | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option.
Name heading Level | Type integer | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option.
Name classes | Type string | Description Classes to add to the table container.
Name table Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table container.
Name ascending Text | Type string | Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" .
Name descending Text | Type string | Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" .
Name sort Announcement Text | Type string | Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table cell.
Name header | Type string | Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option.
Name href | Type string | Description If set, the table cell will become a link.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name sort Value | Type string | Description Sort value text for cells in table rows.
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table cell.

Name | Type | Description
Name text | Type string | Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored.
Name html | Type string | Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table head cell.
Name href | Type string | Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table head cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table head cell.
Name sort | Type string | Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true .
Name sort Next | Type string | Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" .

Name | Type | Description
Name id | Type string | Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option.
Name text | Type string | Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" .
Name caption | Type object | Description Optional caption for the table caption. See macro options for caption .
Name size | Type string | Description Size of the table caption – "s" , "m" , "l" or "xl" .
Name classes | Type string | Description Classes to add to the table caption, for example "nhsuk-table__caption--l" .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table caption.

Name | Type | Description
Name id | Type string | Description The ID of the caption.
Name element | Type string | Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" .
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block.
Name placement | Type string | Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" .
Name size | Type string | Description Size of the caption – "m" , "l" , "xl" or "xxl" .
Name classes | Type string | Description Classes to add to the caption.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the caption.

```text
{%
from
"tables/macro.njk"
import
table
%}
{{
table
({
caption
:
"Prescription prepayment certificate (PPC) charges"
,
firstCellIsHeader
:
true
,
head
: [
    {
text
:
"Item"
},
    {
text
:
"Current charge"
,
format
:
"numeric"
},
    {
text
:
"New charge"
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
"3-month"
},
      {
text
:
"£31.25"
},
      {
text
:
"£32.05"
}
    ],
    [
      {
text
:
"12-month"
},
      {
text
:
"£111.60"
},
      {
text
:
"£114.50"
}
    ],
    [
      {
text
:
"HRT"
},
      {
text
:
"£19.30"
},
      {
text
:
"£19.80"
}
    ]
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### When not to use a basic table

Do not use a basic table if your table content becomes squashed and hard to read on small screens. Use a responsive table instead.

## Compact table

Use a compact table when you have a lot of data to display. It reduces the vertical padding between rows, making it easier to scan the data.

If you're using Nunjucks, add the compact: true option. For HTML add the nhsuk-table--compact class to the table.

Try first to reduce the amount of data you display, for example by splitting it into multiple tables or combining columns. For example, showing a name and NHS number together in 1 column.

- HTML code for table compact

- Nunjucks code for table compact

```text
<
table
class
=
"nhsuk-table nhsuk-table--compact"
>
<
caption
class
=
"nhsuk-table__caption nhsuk-table__caption--m"
id
=
"vaccination-coverage-caption"
>
Childhood vaccination coverage by nation
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
Nation
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
2022 to 2023
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
2023 to 2024
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
2024 to 2025
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
England
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
91.80%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
91.22%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
91.30%
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Northern Ireland
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
93.10%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
91.80%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
91.00%
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Scotland
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
95.55%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.84%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.50%
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Wales
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.47%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.19%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.10%
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the table.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. Array of table rows and cells. See macro options for rows .
Name head | Type array | Description Array of table head cells. See macro options for head .
Name caption | Type object | Description Table caption. See macro options for caption .
Name caption Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option.
Name caption Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option.
Name first Cell Is Header | Type boolean | Description If set to true , first cell in table row will be a th instead of a td .
Name compact | Type boolean | Description If set to true , vertical padding will be reduced for table cells.
Name responsive | Type boolean | Description If set to true , responsive table classes will be applied.
Name scroll | Type boolean | Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options.
Name striped | Type boolean | Description If set to true , striped background colours will be applied to table rows.
Name variant | Type string | Description Optional variant of table. You can use only "reverse" or empty values with this option.
Name card | Type object | Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card .
Name panel | Type boolean | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option.
Name panel Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option.
Name heading | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option.
Name heading Level | Type integer | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option.
Name classes | Type string | Description Classes to add to the table container.
Name table Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table container.
Name ascending Text | Type string | Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" .
Name descending Text | Type string | Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" .
Name sort Announcement Text | Type string | Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table cell.
Name header | Type string | Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option.
Name href | Type string | Description If set, the table cell will become a link.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name sort Value | Type string | Description Sort value text for cells in table rows.
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table cell.

Name | Type | Description
Name text | Type string | Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored.
Name html | Type string | Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table head cell.
Name href | Type string | Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table head cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table head cell.
Name sort | Type string | Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true .
Name sort Next | Type string | Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" .

Name | Type | Description
Name id | Type string | Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option.
Name text | Type string | Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" .
Name caption | Type object | Description Optional caption for the table caption. See macro options for caption .
Name size | Type string | Description Size of the table caption – "s" , "m" , "l" or "xl" .
Name classes | Type string | Description Classes to add to the table caption, for example "nhsuk-table__caption--l" .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table caption.

Name | Type | Description
Name id | Type string | Description The ID of the caption.
Name element | Type string | Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" .
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block.
Name placement | Type string | Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" .
Name size | Type string | Description Size of the caption – "m" , "l" , "xl" or "xxl" .
Name classes | Type string | Description Classes to add to the caption.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the caption.

```text
{%
from
"tables/macro.njk"
import
table
%}
{{
table
({
caption
: {
id
:
"vaccination-coverage-caption"
,
text
:
"Childhood vaccination coverage by nation"
,
size
:
"m"
},
firstCellIsHeader
:
true
,
compact
:
true
,
scrollable
:
true
,
head
: [
    {
text
:
"Nation"
},
    {
text
:
"2022 to 2023"
,
format
:
"numeric"
},
    {
text
:
"2023 to 2024"
,
format
:
"numeric"
},
    {
text
:
"2024 to 2025"
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
"England"
},
      {
text
:
"91.80%"
},
      {
text
:
"91.22%"
},
      {
text
:
"91.30%"
}
    ],
    [
      {
text
:
"Northern Ireland"
},
      {
text
:
"93.10%"
},
      {
text
:
"91.80%"
},
      {
text
:
"91.00%"
}
    ],
    [
      {
text
:
"Scotland"
},
      {
text
:
"95.55%"
},
      {
text
:
"94.84%"
},
      {
text
:
"94.50%"
}
    ],
    [
      {
text
:
"Wales"
},
      {
text
:
"94.47%"
},
      {
text
:
"94.19%"
},
      {
text
:
"94.10%"
}
    ]
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## Striped table

Add striping (sometimes called zebra stripes) to tables with many rows and columns of data to help users distinguish between rows.

If you're using Nunjucks, add the striped: true option. For HTML add the nhsuk-table--striped class to the table.

- HTML code for table striped

- Nunjucks code for table striped

```text
<
table
class
=
"nhsuk-table nhsuk-table--striped"
>
<
caption
class
=
"nhsuk-table__caption nhsuk-table__caption--m"
id
=
"vaccination-coverage-caption"
>
Childhood vaccination coverage by nation
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
Nation
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
2022 to 2023
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
2023 to 2024
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
2024 to 2025
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
England
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
91.80%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
91.22%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
91.30%
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Northern Ireland
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
93.10%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
91.80%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
91.00%
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Scotland
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
95.55%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.84%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.50%
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Wales
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.47%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.19%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.10%
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the table.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. Array of table rows and cells. See macro options for rows .
Name head | Type array | Description Array of table head cells. See macro options for head .
Name caption | Type object | Description Table caption. See macro options for caption .
Name caption Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option.
Name caption Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option.
Name first Cell Is Header | Type boolean | Description If set to true , first cell in table row will be a th instead of a td .
Name compact | Type boolean | Description If set to true , vertical padding will be reduced for table cells.
Name responsive | Type boolean | Description If set to true , responsive table classes will be applied.
Name scroll | Type boolean | Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options.
Name striped | Type boolean | Description If set to true , striped background colours will be applied to table rows.
Name variant | Type string | Description Optional variant of table. You can use only "reverse" or empty values with this option.
Name card | Type object | Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card .
Name panel | Type boolean | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option.
Name panel Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option.
Name heading | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option.
Name heading Level | Type integer | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option.
Name classes | Type string | Description Classes to add to the table container.
Name table Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table container.
Name ascending Text | Type string | Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" .
Name descending Text | Type string | Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" .
Name sort Announcement Text | Type string | Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table cell.
Name header | Type string | Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option.
Name href | Type string | Description If set, the table cell will become a link.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name sort Value | Type string | Description Sort value text for cells in table rows.
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table cell.

Name | Type | Description
Name text | Type string | Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored.
Name html | Type string | Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table head cell.
Name href | Type string | Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table head cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table head cell.
Name sort | Type string | Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true .
Name sort Next | Type string | Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" .

Name | Type | Description
Name id | Type string | Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option.
Name text | Type string | Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" .
Name caption | Type object | Description Optional caption for the table caption. See macro options for caption .
Name size | Type string | Description Size of the table caption – "s" , "m" , "l" or "xl" .
Name classes | Type string | Description Classes to add to the table caption, for example "nhsuk-table__caption--l" .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table caption.

Name | Type | Description
Name id | Type string | Description The ID of the caption.
Name element | Type string | Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" .
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block.
Name placement | Type string | Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" .
Name size | Type string | Description Size of the caption – "m" , "l" , "xl" or "xxl" .
Name classes | Type string | Description Classes to add to the caption.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the caption.

```text
{%
from
"tables/macro.njk"
import
table
%}
{{
table
({
caption
: {
id
:
"vaccination-coverage-caption"
,
text
:
"Childhood vaccination coverage by nation"
,
size
:
"m"
},
firstCellIsHeader
:
true
,
striped
:
true
,
head
: [
    {
text
:
"Nation"
},
    {
text
:
"2022 to 2023"
,
format
:
"numeric"
},
    {
text
:
"2023 to 2024"
,
format
:
"numeric"
},
    {
text
:
"2024 to 2025"
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
"England"
},
      {
text
:
"91.80%"
},
      {
text
:
"91.22%"
},
      {
text
:
"91.30%"
}
    ],
    [
      {
text
:
"Northern Ireland"
},
      {
text
:
"93.10%"
},
      {
text
:
"91.80%"
},
      {
text
:
"91.00%"
}
    ],
    [
      {
text
:
"Scotland"
},
      {
text
:
"95.55%"
},
      {
text
:
"94.84%"
},
      {
text
:
"94.50%"
}
    ],
    [
      {
text
:
"Wales"
},
      {
text
:
"94.47%"
},
      {
text
:
"94.19%"
},
      {
text
:
"94.10%"
}
    ]
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## Responsive table

This table has a responsive layout. On large screens it displays horizontally but on small screens it stacks vertically.

Use a responsive table when your table becomes squashed and hard to read on small screens, 768px and smaller.

If you're using Nunjucks, add the responsive: true option. For HTML add the nhsuk-table--responsive class to the table and set the correct role attribute for each element of the table.

- HTML code for table responsive

- Nunjucks code for table responsive

```text
<
table
class
=
"nhsuk-table nhsuk-table--responsive"
role
=
"table"
>
<
caption
class
=
"nhsuk-table__caption"
>
Ibuprofen liquid dosages for children by age
</
caption
>
<
thead
class
=
"nhsuk-table__head"
role
=
"rowgroup"
>
<
tr
class
=
"nhsuk-table__row"
role
=
"row"
>
<
th
class
=
"nhsuk-table__header nhsuk-u-width-one-third"
scope
=
"col"
role
=
"columnheader"
>
Age
</
th
>
<
th
class
=
"nhsuk-table__header nhsuk-u-width-one-quarter"
scope
=
"col"
role
=
"columnheader"
>
How much?
</
th
>
<
th
class
=
"nhsuk-table__header"
scope
=
"col"
role
=
"columnheader"
>
How often?
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
role
=
"row"
>
<
th
class
=
"nhsuk-table__header"
scope
=
"row"
role
=
"rowheader"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
Age
</
span
>
<
span
>
3 to 5 months (weighing more than 5kg)
</
span
>
</
th
>
<
td
class
=
"nhsuk-table__cell"
role
=
"cell"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
How much?
</
span
>
2.5ml (50mg)
</
td
>
<
td
class
=
"nhsuk-table__cell"
role
=
"cell"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
How often?
</
span
>
Max 3 times in 24 hours
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
role
=
"row"
>
<
th
class
=
"nhsuk-table__header"
scope
=
"row"
role
=
"rowheader"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
Age
</
span
>
6 to 11 months
</
th
>
<
td
class
=
"nhsuk-table__cell"
role
=
"cell"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
How much?
</
span
>
2.5ml (50mg)
</
td
>
<
td
class
=
"nhsuk-table__cell"
role
=
"cell"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
How often?
</
span
>
Max 3 to 4 times in 24 hours
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
role
=
"row"
>
<
th
class
=
"nhsuk-table__header"
scope
=
"row"
role
=
"rowheader"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
Age
</
span
>
1 to 3 years
</
th
>
<
td
class
=
"nhsuk-table__cell"
role
=
"cell"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
How much?
</
span
>
5ml (100mg)
</
td
>
<
td
class
=
"nhsuk-table__cell"
role
=
"cell"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
How often?
</
span
>
Max 3 times in 24 hours
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
role
=
"row"
>
<
th
class
=
"nhsuk-table__header"
scope
=
"row"
role
=
"rowheader"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
Age
</
span
>
4 to 6 years
</
th
>
<
td
class
=
"nhsuk-table__cell"
role
=
"cell"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
How much?
</
span
>
7.5ml (150mg)
</
td
>
<
td
class
=
"nhsuk-table__cell"
role
=
"cell"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
How often?
</
span
>
Max 3 times in 24 hours
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
role
=
"row"
>
<
th
class
=
"nhsuk-table__header"
scope
=
"row"
role
=
"rowheader"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
Age
</
span
>
7 to 9 years
</
th
>
<
td
class
=
"nhsuk-table__cell"
role
=
"cell"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
How much?
</
span
>
10ml (200mg)
</
td
>
<
td
class
=
"nhsuk-table__cell"
role
=
"cell"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
How often?
</
span
>
Max 3 times in 24 hours
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
role
=
"row"
>
<
th
class
=
"nhsuk-table__header"
scope
=
"row"
role
=
"rowheader"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
Age
</
span
>
10 to 11 years
</
th
>
<
td
class
=
"nhsuk-table__cell"
role
=
"cell"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
How much?
</
span
>
15ml (300mg)
</
td
>
<
td
class
=
"nhsuk-table__cell"
role
=
"cell"
>
<
span
class
=
"nhsuk-table__heading"
aria-hidden
=
"true"
>
How often?
</
span
>
Max 3 times in 24 hours
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the table.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. Array of table rows and cells. See macro options for rows .
Name head | Type array | Description Array of table head cells. See macro options for head .
Name caption | Type object | Description Table caption. See macro options for caption .
Name caption Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option.
Name caption Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option.
Name first Cell Is Header | Type boolean | Description If set to true , first cell in table row will be a th instead of a td .
Name compact | Type boolean | Description If set to true , vertical padding will be reduced for table cells.
Name responsive | Type boolean | Description If set to true , responsive table classes will be applied.
Name scroll | Type boolean | Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options.
Name striped | Type boolean | Description If set to true , striped background colours will be applied to table rows.
Name variant | Type string | Description Optional variant of table. You can use only "reverse" or empty values with this option.
Name card | Type object | Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card .
Name panel | Type boolean | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option.
Name panel Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option.
Name heading | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option.
Name heading Level | Type integer | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option.
Name classes | Type string | Description Classes to add to the table container.
Name table Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table container.
Name ascending Text | Type string | Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" .
Name descending Text | Type string | Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" .
Name sort Announcement Text | Type string | Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table cell.
Name header | Type string | Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option.
Name href | Type string | Description If set, the table cell will become a link.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name sort Value | Type string | Description Sort value text for cells in table rows.
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table cell.

Name | Type | Description
Name text | Type string | Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored.
Name html | Type string | Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table head cell.
Name href | Type string | Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table head cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table head cell.
Name sort | Type string | Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true .
Name sort Next | Type string | Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" .

Name | Type | Description
Name id | Type string | Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option.
Name text | Type string | Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" .
Name caption | Type object | Description Optional caption for the table caption. See macro options for caption .
Name size | Type string | Description Size of the table caption – "s" , "m" , "l" or "xl" .
Name classes | Type string | Description Classes to add to the table caption, for example "nhsuk-table__caption--l" .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table caption.

Name | Type | Description
Name id | Type string | Description The ID of the caption.
Name element | Type string | Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" .
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block.
Name placement | Type string | Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" .
Name size | Type string | Description Size of the caption – "m" , "l" , "xl" or "xxl" .
Name classes | Type string | Description Classes to add to the caption.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the caption.

```text
{%
from
"tables/macro.njk"
import
table
%}
{{
table
({
caption
:
"Ibuprofen liquid dosages for children by age"
,
firstCellIsHeader
:
true
,
responsive
:
true
,
head
: [
    {
text
:
"Age"
,
width
:
"one-third"
},
    {
text
:
"How much?"
,
width
:
"one-quarter"
},
    {
text
:
"How often?"
}
  ],
rows
: [
    [
      {
html
:
"3 to 5 months (weighing more than 5kg)"
},
      {
text
:
"2.5ml (50mg)"
},
      {
text
:
"Max 3 times in 24 hours"
}
    ],
    [
      {
text
:
"6 to 11 months"
},
      {
text
:
"2.5ml (50mg)"
},
      {
text
:
"Max 3 to 4 times in 24 hours"
}
    ],
    [
      {
text
:
"1 to 3 years"
},
      {
text
:
"5ml (100mg)"
},
      {
text
:
"Max 3 times in 24 hours"
}
    ],
    [
      {
text
:
"4 to 6 years"
},
      {
text
:
"7.5ml (150mg)"
},
      {
text
:
"Max 3 times in 24 hours"
}
    ],
    [
      {
text
:
"7 to 9 years"
},
      {
text
:
"10ml (200mg)"
},
      {
text
:
"Max 3 times in 24 hours"
}
    ],
    [
      {
text
:
"10 to 11 years"
},
      {
text
:
"15ml (300mg)"
},
      {
text
:
"Max 3 times in 24 hours"
}
    ]
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### When not to use a responsive table

Do not use a responsive table if your content is easier to read and understand on a small screen in a non-stacked layout. Use a basic table instead. If you have too many columns to fit, use a scrolling table.

## Scrolling table

Add the scrolling container when your table has many columns and you cannot split it up or use a responsive table.

If you're using Nunjucks, add the scroll: true option. For HTML add the scrolling container from the example below.

- HTML code for table scrolling

- Nunjucks code for table scrolling

```text
<
div
class
=
"nhsuk-scroll"
data-module
=
"nhsuk-scroll"
>
<
div
class
=
"nhsuk-scroll__content"
role
=
"region"
aria-labelledby
=
"vaccination-coverage-caption"
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
"nhsuk-table__caption nhsuk-table__caption--m"
id
=
"vaccination-coverage-caption"
>
Childhood vaccination coverage by nation
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
Nation
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
2013 to 2014
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
2014 to 2015
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
2015 to 2016
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
2016 to 2017
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
2017 to 2018
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
2018 to 2019
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
2019 to 2020
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
2020 to 2021
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
2021 to 2022
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
2022 to 2023
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
2023 to 2024
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
2024 to 2025
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
England
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.34%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.23%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
93.56%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
93.41%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
93.12%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
92.09%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
92.57%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
92.04%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
91.84%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
91.80%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
91.22%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
91.30%
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Northern Ireland
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
97.48%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
96.84%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
97.22%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
97.04%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
96.20%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.52%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.45%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.53%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
93.52%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
93.10%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
91.80%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
91.00%
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Scotland
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
97.51%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
97.39%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
97.15%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
96.77%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
96.51%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
95.80%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
96.23%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
96.54%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
96.32%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
95.55%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.84%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.50%
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Wales
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
96.70%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
96.57%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
96.57%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
96.34%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
95.92%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
95.42%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
95.77%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
95.56%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
95.18%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.47%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.19%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.10%
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
Name id | Type string | Description The ID of the table.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. Array of table rows and cells. See macro options for rows .
Name head | Type array | Description Array of table head cells. See macro options for head .
Name caption | Type object | Description Table caption. See macro options for caption .
Name caption Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option.
Name caption Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option.
Name first Cell Is Header | Type boolean | Description If set to true , first cell in table row will be a th instead of a td .
Name compact | Type boolean | Description If set to true , vertical padding will be reduced for table cells.
Name responsive | Type boolean | Description If set to true , responsive table classes will be applied.
Name scroll | Type boolean | Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options.
Name striped | Type boolean | Description If set to true , striped background colours will be applied to table rows.
Name variant | Type string | Description Optional variant of table. You can use only "reverse" or empty values with this option.
Name card | Type object | Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card .
Name panel | Type boolean | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option.
Name panel Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option.
Name heading | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option.
Name heading Level | Type integer | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option.
Name classes | Type string | Description Classes to add to the table container.
Name table Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table container.
Name ascending Text | Type string | Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" .
Name descending Text | Type string | Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" .
Name sort Announcement Text | Type string | Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table cell.
Name header | Type string | Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option.
Name href | Type string | Description If set, the table cell will become a link.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name sort Value | Type string | Description Sort value text for cells in table rows.
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table cell.

Name | Type | Description
Name text | Type string | Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored.
Name html | Type string | Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table head cell.
Name href | Type string | Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table head cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table head cell.
Name sort | Type string | Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true .
Name sort Next | Type string | Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" .

Name | Type | Description
Name id | Type string | Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option.
Name text | Type string | Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" .
Name caption | Type object | Description Optional caption for the table caption. See macro options for caption .
Name size | Type string | Description Size of the table caption – "s" , "m" , "l" or "xl" .
Name classes | Type string | Description Classes to add to the table caption, for example "nhsuk-table__caption--l" .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table caption.

Name | Type | Description
Name id | Type string | Description The ID of the caption.
Name element | Type string | Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" .
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block.
Name placement | Type string | Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" .
Name size | Type string | Description Size of the caption – "m" , "l" , "xl" or "xxl" .
Name classes | Type string | Description Classes to add to the caption.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the caption.

```text
{%
from
"tables/macro.njk"
import
table
%}
{{
table
({
caption
: {
id
:
"vaccination-coverage-caption"
,
text
:
"Childhood vaccination coverage by nation"
,
size
:
"m"
},
firstCellIsHeader
:
true
,
scroll
:
true
,
head
: [
    {
text
:
"Nation"
},
    {
text
:
"2013 to 2014"
,
format
:
"numeric"
},
    {
text
:
"2014 to 2015"
,
format
:
"numeric"
},
    {
text
:
"2015 to 2016"
,
format
:
"numeric"
},
    {
text
:
"2016 to 2017"
,
format
:
"numeric"
},
    {
text
:
"2017 to 2018"
,
format
:
"numeric"
},
    {
text
:
"2018 to 2019"
,
format
:
"numeric"
},
    {
text
:
"2019 to 2020"
,
format
:
"numeric"
},
    {
text
:
"2020 to 2021"
,
format
:
"numeric"
},
    {
text
:
"2021 to 2022"
,
format
:
"numeric"
},
    {
text
:
"2022 to 2023"
,
format
:
"numeric"
},
    {
text
:
"2023 to 2024"
,
format
:
"numeric"
},
    {
text
:
"2024 to 2025"
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
"England"
},
      {
text
:
"94.34%"
},
      {
text
:
"94.23%"
},
      {
text
:
"93.56%"
},
      {
text
:
"93.41%"
},
      {
text
:
"93.12%"
},
      {
text
:
"92.09%"
},
      {
text
:
"92.57%"
},
      {
text
:
"92.04%"
},
      {
text
:
"91.84%"
},
      {
text
:
"91.80%"
},
      {
text
:
"91.22%"
},
      {
text
:
"91.30%"
}
    ],
    [
      {
text
:
"Northern Ireland"
},
      {
text
:
"97.48%"
},
      {
text
:
"96.84%"
},
      {
text
:
"97.22%"
},
      {
text
:
"97.04%"
},
      {
text
:
"96.20%"
},
      {
text
:
"94.52%"
},
      {
text
:
"94.45%"
},
      {
text
:
"94.53%"
},
      {
text
:
"93.52%"
},
      {
text
:
"93.10%"
},
      {
text
:
"91.80%"
},
      {
text
:
"91.00%"
}
    ],
    [
      {
text
:
"Scotland"
},
      {
text
:
"97.51%"
},
      {
text
:
"97.39%"
},
      {
text
:
"97.15%"
},
      {
text
:
"96.77%"
},
      {
text
:
"96.51%"
},
      {
text
:
"95.80%"
},
      {
text
:
"96.23%"
},
      {
text
:
"96.54%"
},
      {
text
:
"96.32%"
},
      {
text
:
"95.55%"
},
      {
text
:
"94.84%"
},
      {
text
:
"94.50%"
}
    ],
    [
      {
text
:
"Wales"
},
      {
text
:
"96.70%"
},
      {
text
:
"96.57%"
},
      {
text
:
"96.57%"
},
      {
text
:
"96.34%"
},
      {
text
:
"95.92%"
},
      {
text
:
"95.42%"
},
      {
text
:
"95.77%"
},
      {
text
:
"95.56%"
},
      {
text
:
"95.18%"
},
      {
text
:
"94.47%"
},
      {
text
:
"94.19%"
},
      {
text
:
"94.10%"
}
    ]
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

The example uses an nhsuk-scroll container to automatically toggle left or right shadows when scrolling.

```text
<
div
class
=
"nhsuk-scroll"
data-module
=
"nhsuk-scroll"
>
<
div
class
=
"nhsuk-scroll__content"
role
=
"region"
aria-labelledby
=
"table-caption-id"
>
```

## Sortable table

A sortable table lets users sort columns in ascending or descending order, alphabetically or numerically.

Ascending order (up arrow) arranges:

- numerical data from the lowest to the highest value

- text in alphabetical order A to Z

Descending order (down arrow) reverses this.

This table only sorts by 1 column at a time. Sortable columns show a double arrow until they're sorted. When users click in the column header of an unsorted column, it sorts and shows a single arrow. Clicking again toggles between ascending and descending.

- HTML code for table sortable

- Nunjucks code for table sortable

```text
<
table
class
=
"nhsuk-table nhsuk-table--sortable"
data-module
=
"nhsuk-table"
>
<
caption
class
=
"nhsuk-table__caption nhsuk-table__caption--m"
>
Childhood vaccination coverage
<
span
class
=
"nhsuk-u-visually-hidden"
>
(Column headers are sortable)
</
span
>
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
data-sort
aria-sort
=
"ascending"
>
Nation
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
data-sort
data-sort-next
=
"descending"
>
MMR
</
th
>
<
th
class
=
"nhsuk-table__header nhsuk-table__header--numeric nhsuk-u-nowrap"
scope
=
"col"
data-sort
data-sort-next
=
"descending"
>
6-in-1
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
data-sort
data-sort-next
=
"descending"
>
Rotavirus
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
England
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
83.7%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
92.8%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
88.8%
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Northern Ireland
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
86.4%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
94.6%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
88.0%
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Scotland
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
89.2%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
96.9%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
92.2%
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Wales
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
89.5%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
95.4%
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
92.0%
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the table.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. Array of table rows and cells. See macro options for rows .
Name head | Type array | Description Array of table head cells. See macro options for head .
Name caption | Type object | Description Table caption. See macro options for caption .
Name caption Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option.
Name caption Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option.
Name first Cell Is Header | Type boolean | Description If set to true , first cell in table row will be a th instead of a td .
Name compact | Type boolean | Description If set to true , vertical padding will be reduced for table cells.
Name responsive | Type boolean | Description If set to true , responsive table classes will be applied.
Name scroll | Type boolean | Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options.
Name striped | Type boolean | Description If set to true , striped background colours will be applied to table rows.
Name variant | Type string | Description Optional variant of table. You can use only "reverse" or empty values with this option.
Name card | Type object | Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card .
Name panel | Type boolean | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option.
Name panel Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option.
Name heading | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option.
Name heading Level | Type integer | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option.
Name classes | Type string | Description Classes to add to the table container.
Name table Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table container.
Name ascending Text | Type string | Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" .
Name descending Text | Type string | Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" .
Name sort Announcement Text | Type string | Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table cell.
Name header | Type string | Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option.
Name href | Type string | Description If set, the table cell will become a link.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name sort Value | Type string | Description Sort value text for cells in table rows.
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table cell.

Name | Type | Description
Name text | Type string | Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored.
Name html | Type string | Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table head cell.
Name href | Type string | Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table head cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table head cell.
Name sort | Type string | Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true .
Name sort Next | Type string | Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" .

Name | Type | Description
Name id | Type string | Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option.
Name text | Type string | Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" .
Name caption | Type object | Description Optional caption for the table caption. See macro options for caption .
Name size | Type string | Description Size of the table caption – "s" , "m" , "l" or "xl" .
Name classes | Type string | Description Classes to add to the table caption, for example "nhsuk-table__caption--l" .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table caption.

Name | Type | Description
Name id | Type string | Description The ID of the caption.
Name element | Type string | Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" .
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block.
Name placement | Type string | Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" .
Name size | Type string | Description Size of the caption – "m" , "l" , "xl" or "xxl" .
Name classes | Type string | Description Classes to add to the caption.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the caption.

```text
{%
from
"tables/macro.njk"
import
table
%}
{{
table
({
caption
: {
text
:
"Childhood vaccination coverage"
,
size
:
"m"
},
firstCellIsHeader
:
true
,
head
: [
    {
text
:
"Nation"
,
sort
:
"ascending"
},
    {
text
:
"MMR"
,
format
:
"numeric"
,
sort
:
true
,
sortNext
:
"descending"
},
    {
text
:
"6-in-1"
,
classes
:
"nhsuk-u-nowrap"
,
format
:
"numeric"
,
sort
:
true
,
sortNext
:
"descending"
},
    {
text
:
"Rotavirus"
,
format
:
"numeric"
,
sort
:
true
,
sortNext
:
"descending"
}
  ],
rows
: [
    [
      {
text
:
"England"
},
      {
text
:
"83.7%"
},
      {
text
:
"92.8%"
},
      {
text
:
"88.8%"
}
    ],
    [
      {
text
:
"Northern Ireland"
},
      {
text
:
"86.4%"
},
      {
text
:
"94.6%"
},
      {
text
:
"88.0%"
}
    ],
    [
      {
text
:
"Scotland"
},
      {
text
:
"89.2%"
},
      {
text
:
"96.9%"
},
      {
text
:
"92.2%"
}
    ],
    [
      {
text
:
"Wales"
},
      {
text
:
"89.5%"
},
      {
text
:
"95.4%"
},
      {
text
:
"92.0%"
}
    ]
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### When to use a sortable table

Use this table when users need to analyse and prioritise data.

### How to use a sortable table

Carry out user research to understand what your users need to do with the data and if a sortable table is the best way to meet their needs.

There are 2 ways to sort a table. You can:

- sort data that fits on 1 page

- sort more than 1 page of data

#### Sort data on 1 page

The sortable table component uses JavaScript to sort the data in the user's browser. Use it where you have only 1 page of data. Make sure your data has a suitable sort order if JavaScript does not run.

##### Sorting columns

By default when you click on the column header for an unsorted column, it will sort that column in ascending order. To apply descending order when clicked:

- in Nunjucks, add the sortNext: "descending" option to the column header

- for HTML, add the data-sort-next="descending" attribute to the column header

Typically users expect text to sort A to Z by default. With numbers, they often expect them to sort with the biggest number first.

Do not allow sorting on columns that cannot be meaningfully ordered, for example comments from users.

Do not add code to automatically save the sort order. Users may not expect this and it could add clinical risk.

A page refresh or navigation must return the page to its default sort order, unless you add functionality to allow users to save their sort order explicitly.

##### Sorting numbers

By default, columns will be sorted as text. To correctly order columns containing numbers: in Nunjucks, add the format: "numeric" option to the column header for HTML, add the nhsuk-table__header--numeric class to the column header and nhsuk-table__cell--numeric class to the cells Columns set to numeric will work correctly with most number symbols, including commas, decimals, percentages and currencies. Use numeric for dates. Overriding the default sort order You can override the default sort value to make the presented data easier for users to understand. For example: dates: 30 November 2026 sorted as 2026-11-30 months: January sorted as 01 January prefixes: The Whittington Hospital sorted as Whittington Hospital To override the default sort value: in Nunjucks, add the sortValue option to the table cell for HTML, add the data-sort-value attribute to the table cell Make sure to override the sort value for missing data . For example, setting sortValue: "£0" will sort the text "No data" consistently with other cells. In this example the default sort order is by amount spent (descending). Open this example in a new tab : table sortable custom Toggle JavaScript On | Off HTML code for table sortable custom Nunjucks code for table sortable custom HTML code for table sortable custom Copy code < table class = "nhsuk-table nhsuk-table--sortable" data-module = "nhsuk-table" > < caption class = "nhsuk-table__caption nhsuk-table__caption--m" > Organisations using the service < span class = "nhsuk-u-visually-hidden" > (Column headers are sortable) </ span > </ caption > < thead class = "nhsuk-table__head" > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header nhsuk-u-width-one-third" scope = "col" data-sort > Organisation </ th > < th class = "nhsuk-table__header" scope = "col" > ODS code </ th > < th class = "nhsuk-table__header nhsuk-u-text-align-right" scope = "col" data-sort data-sort-next = "descending" > Joined </ th > < th class = "nhsuk-table__header nhsuk-table__header--numeric" scope = "col" data-sort aria-sort = "descending" > Amount spent </ th > </ tr > </ thead > < tbody class = "nhsuk-table__body" > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "row" > Warrington and Halton Hospitals </ th > < td class = "nhsuk-table__cell" > RY2N0 </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" data-sort-value = "2024-07-18" > 18 July 2024 </ td > < td class = "nhsuk-table__cell nhsuk-table__cell--numeric" > £16,821 </ td > </ tr > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "row" data-sort-value = "Christie" > The Christie </ th > < td class = "nhsuk-table__cell" > J3P0W </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" data-sort-value = "2025-01-04" > 4 January 2025 </ td > < td class = "nhsuk-table__cell nhsuk-table__cell--numeric" > £12,013 </ td > </ tr > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "row" > University College London Hospitals </ th > < td class = "nhsuk-table__cell" > RRV00 </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" data-sort-value = "2025-12-02" > 2 December 2025 </ td > < td class = "nhsuk-table__cell nhsuk-table__cell--numeric" > £4,102 </ td > </ tr > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "row" data-sort-value = "Whittington Hospital" > The Whittington Hospital </ th > < td class = "nhsuk-table__cell" > RALWH </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" data-sort-value = "2022-08-21" > 21 August 2022 </ td > < td class = "nhsuk-table__cell nhsuk-table__cell--numeric nhsuk-u-secondary-text-colour" data-sort-value = "£0" > No data </ td > </ tr > </ tbody > </ table > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : table sortable custom Nunjucks code for table sortable custom Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the table. Name border Type boolean Description If set to false , remove separating borders from all rows. Name last Row Border Type boolean Description If set to false , remove separating border from the last row. Name rows Type array Description Required. Array of table rows and cells. See macro options for rows . Name head Type array Description Array of table head cells. See macro options for head . Name caption Type object Description Table caption. See macro options for caption . Name caption Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option. Name caption Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option. Name first Cell Is Header Type boolean Description If set to true , first cell in table row will be a th instead of a td . Name compact Type boolean Description If set to true , vertical padding will be reduced for table cells. Name responsive Type boolean Description If set to true , responsive table classes will be applied. Name scroll Type boolean Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options. Name striped Type boolean Description If set to true , striped background colours will be applied to table rows. Name variant Type string Description Optional variant of table. You can use only "reverse" or empty values with this option. Name card Type object Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card . Name panel Type boolean Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option. Name panel Classes Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option. Name heading Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option. Name heading Level Type integer Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option. Name classes Type string Description Classes to add to the table container. Name table Classes Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table container. Name ascending Text Type string Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" . Name descending Text Type string Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" . Name sort Announcement Text Type string Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value. Options for rows array objects Name Type Description Name text Type string Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the table cell. Name header Type string Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option. Name href Type string Description If set, the table cell will become a link. Name format Type string Description Specify format of a cell – "numeric" or "string" . Defaults to "string" Name sort Value Type string Description Sort value text for cells in table rows. Name colspan Type integer Description Specify how many columns a cell spans. Name rowspan Type integer Description Specify how many rows a cell spans. Name align Type string Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left" Name width Type string Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Name classes Type string Description Classes to add to the table cell. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table cell. Options for head array objects Name Type Description Name text Type string Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored. Name html Type string Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the table head cell. Name href Type string Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction. Name format Type string Description Specify format of a cell – "numeric" or "string" . Defaults to "string" Name colspan Type integer Description Specify how many columns a cell spans. Name rowspan Type integer Description Specify how many rows a cell spans. Name align Type string Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left" Name width Type string Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Name classes Type string Description Classes to add to the table head cell. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table head cell. Name sort Type string Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true . Name sort Next Type string Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" . Options for caption heading component Name Type Description Name id Type string Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option. Name text Type string Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" . Name caption Type object Description Optional caption for the table caption. See macro options for caption . Name size Type string Description Size of the table caption – "s" , "m" , "l" or "xl" . Name classes Type string Description Classes to add to the table caption, for example "nhsuk-table__caption--l" . Name attributes Type object Description HTML attributes (for example data attributes) to add to the table caption. Options for caption component Name Type Description Name id Type string Description The ID of the caption. Name element Type string Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" . Name text Type string Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block. Name placement Type string Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" . Name size Type string Description Size of the caption – "m" , "l" , "xl" or "xxl" . Name classes Type string Description Classes to add to the caption. Name attributes Type object Description HTML attributes (for example data attributes) to add to the caption. Copy code {% from "tables/macro.njk" import table %} {{ table ({ caption : { text : "Organisations using the service" , size : "m" }, firstCellIsHeader : true , head : [ { text : "Organisation" , width : "one-third" , sort : true }, { text : "ODS code" }, { text : "Joined" , align : "right" , sort : true , sortNext : "descending" }, { text : "Amount spent" , format : "numeric" , sort : "descending" } ], rows : [ [ { text : "Warrington and Halton Hospitals" }, { text : "RY2N0" }, { text : "18 July 2024" , sortValue : "2024-07-18" }, { text : "£16,821" } ], [ { text : "The Christie" , sortValue : "Christie" }, { text : "J3P0W" }, { text : "4 January 2025" , sortValue : "2025-01-04" }, { text : "£12,013" } ], [ { text : "University College London Hospitals" }, { text : "RRV00" }, { text : "2 December 2025" , sortValue : "2025-12-02" }, { text : "£4,102" } ], [ { text : "The Whittington Hospital" , sortValue : "Whittington Hospital" }, { text : "RALWH" }, { text : "21 August 2022" , sortValue : "2022-08-21" }, { text : "No data" , sortValue : "£0" , classes : "nhsuk-u-secondary-text-colour" } ] ] }) }} Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : table sortable custom Sort more than 1 page of data If your table is paginated, sorting should be applied server-side across all pages. Do not sort the current page only. Use server-side sorting by adding a link to the column header to navigate to a page with the table sorting already applied. You will need to: build your own server-side function return users to the first page of new results after sorting test with users This example shows a paginated table but it does not work in the browser. The functionality would need to be built server-side. Open this example in a new tab : table sortable server side last login descending HTML code for table sortable server side last login descending Nunjucks code for table sortable server side last login descending HTML code for table sortable server side last login descending Copy code < table class = "nhsuk-table nhsuk-table--sortable" > < caption class = "nhsuk-table__caption nhsuk-table__caption--m" > Users < span class = "nhsuk-u-visually-hidden" > (Column headers are sortable) </ span > </ caption > < thead class = "nhsuk-table__head" > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header nhsuk-u-width-one-half" scope = "col" data-sort > < a class = "nhsuk-link" href = "sortable-server-side" > Name </ a > </ th > < th class = "nhsuk-table__header nhsuk-u-text-align-right nhsuk-u-width-one-third nhsuk-u-nowrap" scope = "col" data-sort aria-sort = "descending" > < a class = "nhsuk-link" href = "sortable-server-side-last-login-ascending" > Last log in </ a > </ th > < th class = "nhsuk-table__header nhsuk-u-text-align-right" scope = "col" > < span class = "nhsuk-u-visually-hidden" > Action </ span > </ th > </ tr > </ thead > < tbody class = "nhsuk-table__body" > < tr class = "nhsuk-table__row" > < td class = "nhsuk-table__cell" > Ro Nkosi </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > 28 June 2026 </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > < a class = "nhsuk-link" href = "#" > Change < span class = "nhsuk-u-visually-hidden" > details for Ro Nkosi </ span > </ a > </ td > </ tr > < tr class = "nhsuk-table__row" > < td class = "nhsuk-table__cell" > Stellan Park </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > 20 June 2026 </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > < a class = "nhsuk-link" href = "#" > Change < span class = "nhsuk-u-visually-hidden" > details for Stellan Park </ span > </ a > </ td > </ tr > < tr class = "nhsuk-table__row" > < td class = "nhsuk-table__cell" > Tamsin Foley-Whitworth </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > 14 June 2026 </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > < a class = "nhsuk-link" href = "#" > Change < span class = "nhsuk-u-visually-hidden" > details for Tamsin Foley-Whitworth </ span > </ a > </ td > </ tr > < tr class = "nhsuk-table__row" > < td class = "nhsuk-table__cell" > Uta Brennan </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > 7 June 2026 </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > < a class = "nhsuk-link" href = "#" > Change < span class = "nhsuk-u-visually-hidden" > details for Uta Brennan </ span > </ a > </ td > </ tr > < tr class = "nhsuk-table__row" > < td class = "nhsuk-table__cell" > Val Cruz </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > 1 June 2026 </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > < a class = "nhsuk-link" href = "#" > Change < span class = "nhsuk-u-visually-hidden" > details for Val Cruz </ span > </ a > </ td > </ tr > < tr class = "nhsuk-table__row" > < td class = "nhsuk-table__cell" > Wendell Shaw </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > 25 May 2026 </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > < a class = "nhsuk-link" href = "#" > Change < span class = "nhsuk-u-visually-hidden" > details for Wendell Shaw </ span > </ a > </ td > </ tr > < tr class = "nhsuk-table__row" > < td class = "nhsuk-table__cell" > Xanthe Beaumont </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > 19 May 2026 </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > < a class = "nhsuk-link" href = "#" > Change < span class = "nhsuk-u-visually-hidden" > details for Xanthe Beaumont </ span > </ a > </ td > </ tr > < tr class = "nhsuk-table__row" > < td class = "nhsuk-table__cell" > Yolanda Pierce </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > 13 May 2026 </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > < a class = "nhsuk-link" href = "#" > Change < span class = "nhsuk-u-visually-hidden" > details for Yolanda Pierce </ span > </ a > </ td > </ tr > < tr class = "nhsuk-table__row" > < td class = "nhsuk-table__cell" > Zadie Munroe </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > 7 May 2026 </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > < a class = "nhsuk-link" href = "#" > Change < span class = "nhsuk-u-visually-hidden" > details for Zadie Munroe </ span > </ a > </ td > </ tr > < tr class = "nhsuk-table__row" > < td class = "nhsuk-table__cell" > Reuben Tate </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > 1 May 2026 </ td > < td class = "nhsuk-table__cell nhsuk-u-text-align-right" > < a class = "nhsuk-link" href = "#" > Change < span class = "nhsuk-u-visually-hidden" > details for Reuben Tate </ span > </ a > </ td > </ tr > </ tbody > </ table > < nav class = "nhsuk-pagination nhsuk-pagination--numbered" role = "navigation" aria-label = "Pagination" > < ul class = "nhsuk-pagination__list" > < li class = "nhsuk-pagination__item nhsuk-pagination__item--current" > < a class = "nhsuk-pagination__link" href = "#" aria-label = "Page 1" aria-current = "page" > 1 </ a > </ li > < li class = "nhsuk-pagination__item" > < a class = "nhsuk-pagination__link" href = "#" aria-label = "Page 2" > 2 </ a > </ li > < li class = "nhsuk-pagination__item" > < a class = "nhsuk-pagination__link" href = "#" aria-label = "Page 3" > 3 </ a > </ li > < li class = "nhsuk-pagination__item" > < a class = "nhsuk-pagination__link" href = "#" aria-label = "Page 4" > 4 </ a > </ li > < li class = "nhsuk-pagination__item" > < a class = "nhsuk-pagination__link" href = "#" aria-label = "Page 5" > 5 </ a > </ li > < li class = "nhsuk-pagination__item" > < a class = "nhsuk-pagination__link" href = "#" aria-label = "Page 6" > 6 </ a > </ li > </ ul > < a href = "#" class = "nhsuk-pagination__next" rel = "next" > < span class = "nhsuk-pagination__title" > Next < span class = "nhsuk-u-visually-hidden" > page </ span > </ span > < svg class = "nhsuk-icon nhsuk-icon--arrow-right" xmlns = "http://www.w3.org/2000/svg" viewBox = "0 0 24 24" width = "16" height = "16" focusable = "false" aria-hidden = "true" > < path d = "m14.7 6.3 5 5c.2.2.3.4.3.7 0 .3-.1.5-.3.7l-5 5a1 1 0 0 1-1.4-1.4l3.3-3.3H5a1 1 0 0 1 0-2h11.6l-3.3-3.3a1 1 0 1 1 1.4-1.4Z" /> </ svg > </ a > </ nav > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : table sortable server side last login descending Nunjucks code for table sortable server side last login descending Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the table. Name border Type boolean Description If set to false , remove separating borders from all rows. Name last Row Border Type boolean Description If set to false , remove separating border from the last row. Name rows Type array Description Required. Array of table rows and cells. See macro options for rows . Name head Type array Description Array of table head cells. See macro options for head . Name caption Type object Description Table caption. See macro options for caption . Name caption Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option. Name caption Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option. Name first Cell Is Header Type boolean Description If set to true , first cell in table row will be a th instead of a td . Name compact Type boolean Description If set to true , vertical padding will be reduced for table cells. Name responsive Type boolean Description If set to true , responsive table classes will be applied. Name scroll Type boolean Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options. Name striped Type boolean Description If set to true , striped background colours will be applied to table rows. Name variant Type string Description Optional variant of table. You can use only "reverse" or empty values with this option. Name card Type object Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card . Name panel Type boolean Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option. Name panel Classes Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option. Name heading Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option. Name heading Level Type integer Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option. Name classes Type string Description Classes to add to the table container. Name table Classes Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table container. Name ascending Text Type string Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" . Name descending Text Type string Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" . Name sort Announcement Text Type string Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value. Options for rows array objects Name Type Description Name text Type string Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the table cell. Name header Type string Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option. Name href Type string Description If set, the table cell will become a link. Name format Type string Description Specify format of a cell – "numeric" or "string" . Defaults to "string" Name sort Value Type string Description Sort value text for cells in table rows. Name colspan Type integer Description Specify how many columns a cell spans. Name rowspan Type integer Description Specify how many rows a cell spans. Name align Type string Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left" Name width Type string Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Name classes Type string Description Classes to add to the table cell. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table cell. Options for head array objects Name Type Description Name text Type string Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored. Name html Type string Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the table head cell. Name href Type string Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction. Name format Type string Description Specify format of a cell – "numeric" or "string" . Defaults to "string" Name colspan Type integer Description Specify how many columns a cell spans. Name rowspan Type integer Description Specify how many rows a cell spans. Name align Type string Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left" Name width Type string Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Name classes Type string Description Classes to add to the table head cell. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table head cell. Name sort Type string Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true . Name sort Next Type string Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" . Options for caption heading component Name Type Description Name id Type string Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option. Name text Type string Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" . Name caption Type object Description Optional caption for the table caption. See macro options for caption . Name size Type string Description Size of the table caption – "s" , "m" , "l" or "xl" . Name classes Type string Description Classes to add to the table caption, for example "nhsuk-table__caption--l" . Name attributes Type object Description HTML attributes (for example data attributes) to add to the table caption. Options for caption component Name Type Description Name id Type string Description The ID of the caption. Name element Type string Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" . Name text Type string Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block. Name placement Type string Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" . Name size Type string Description Size of the caption – "m" , "l" , "xl" or "xxl" . Name classes Type string Description Classes to add to the caption. Name attributes Type object Description HTML attributes (for example data attributes) to add to the caption. Copy code {% from "tables/macro.njk" import table %} {% from "pagination/macro.njk" import pagination %} {{ table ({ caption : { text : "Users" , size : "m" }, head : [ { text : "Name" , href : "sortable-server-side" , width : "one-half" , sort : true }, { text : "Last log in" , href : "sortable-server-side-last-login-ascending" , width : "one-third" , align : "right" , classes : "nhsuk-u-nowrap" , sort : "descending" }, { visuallyHiddenText : "Action" , align : "right" } ], rows : [ [ { text : "Ro Nkosi" }, { text : "28 June 2026" }, { text : "Change" , visuallyHiddenText : "details for Ro Nkosi" , href : "#" } ], [ { text : "Stellan Park" }, { text : "20 June 2026" }, { text : "Change" , visuallyHiddenText : "details for Stellan Park" , href : "#" } ], [ { text : "Tamsin Foley-Whitworth" }, { text : "14 June 2026" }, { text : "Change" , visuallyHiddenText : "details for Tamsin Foley-Whitworth" , href : "#" } ], [ { text : "Uta Brennan" }, { text : "7 June 2026" }, { text : "Change" , visuallyHiddenText : "details for Uta Brennan" , href : "#" } ], [ { text : "Val Cruz" }, { text : "1 June 2026" }, { text : "Change" , visuallyHiddenText : "details for Val Cruz" , href : "#" } ], [ { text : "Wendell Shaw" }, { text : "25 May 2026" }, { text : "Change" , visuallyHiddenText : "details for Wendell Shaw" , href : "#" } ], [ { text : "Xanthe Beaumont" }, { text : "19 May 2026" }, { text : "Change" , visuallyHiddenText : "details for Xanthe Beaumont" , href : "#" } ], [ { text : "Yolanda Pierce" }, { text : "13 May 2026" }, { text : "Change" , visuallyHiddenText : "details for Yolanda Pierce" , href : "#" } ], [ { text : "Zadie Munroe" }, { text : "7 May 2026" }, { text : "Change" , visuallyHiddenText : "details for Zadie Munroe" , href : "#" } ], [ { text : "Reuben Tate" }, { text : "1 May 2026" }, { text : "Change" , visuallyHiddenText : "details for Reuben Tate" , href : "#" } ] ] }) }} {{ pagination ({ next : { href : "#" }, items : [ { number : 1 , href : "#" , current : true }, { number : 2 , href : "#" }, { number : 3 , href : "#" }, { number : 4 , href : "#" }, { number : 5 , href : "#" }, { number : 6 , href : "#" } ] }) }} Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : table sortable server side last login descending Consider search and filter Filters reduce the amount of data so that users can focus on what they want. Search helps them find specific things they need. For example, search or filter may work better than sorting for: names NHS numbers or other codes medical conditions If your team is researching filtering, please feed back your findings via our community backlog issue on filtering a list (in GitHub) . Using word-breaks in a table To avoid very long words, such as email addresses, breaking the layout of a table, you can use word-breaks. To do this: in Nunjucks, add the class: "nhsuk-u-text-break-word" option to the table cell for HTML, add the nhsuk-u-text-break-word override class to the table cell Open this example in a new tab : table word break HTML code for table word break Nunjucks code for table word break HTML code for table word break Copy code < table class = "nhsuk-table" > < caption class = "nhsuk-table__caption nhsuk-table__caption--m" > Users </ caption > < thead class = "nhsuk-table__head" > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "col" > Name </ th > < th class = "nhsuk-table__header" scope = "col" > Email address </ th > </ tr > </ thead > < tbody class = "nhsuk-table__body" > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header nhsuk-u-text-break-word" scope = "row" > Aleksandrina Featherstonehaugh-Whitehead </ th > < td class = "nhsuk-table__cell nhsuk-u-text-break-word" > aleksandrina.featherstonehaughwhitehead23@folkestonepharmacy.test.com </ td > </ tr > </ tbody > </ table > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : table word break Nunjucks code for table word break Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the table. Name border Type boolean Description If set to false , remove separating borders from all rows. Name last Row Border Type boolean Description If set to false , remove separating border from the last row. Name rows Type array Description Required. Array of table rows and cells. See macro options for rows . Name head Type array Description Array of table head cells. See macro options for head . Name caption Type object Description Table caption. See macro options for caption . Name caption Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option. Name caption Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option. Name first Cell Is Header Type boolean Description If set to true , first cell in table row will be a th instead of a td . Name compact Type boolean Description If set to true , vertical padding will be reduced for table cells. Name responsive Type boolean Description If set to true , responsive table classes will be applied. Name scroll Type boolean Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options. Name striped Type boolean Description If set to true , striped background colours will be applied to table rows. Name variant Type string Description Optional variant of table. You can use only "reverse" or empty values with this option. Name card Type object Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card . Name panel Type boolean Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option. Name panel Classes Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option. Name heading Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option. Name heading Level Type integer Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option. Name classes Type string Description Classes to add to the table container. Name table Classes Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table container. Name ascending Text Type string Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" . Name descending Text Type string Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" . Name sort Announcement Text Type string Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value. Options for rows array objects Name Type Description Name text Type string Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the table cell. Name header Type string Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option. Name href Type string Description If set, the table cell will become a link. Name format Type string Description Specify format of a cell – "numeric" or "string" . Defaults to "string" Name sort Value Type string Description Sort value text for cells in table rows. Name colspan Type integer Description Specify how many columns a cell spans. Name rowspan Type integer Description Specify how many rows a cell spans. Name align Type string Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left" Name width Type string Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Name classes Type string Description Classes to add to the table cell. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table cell. Options for head array objects Name Type Description Name text Type string Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored. Name html Type string Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the table head cell. Name href Type string Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction. Name format Type string Description Specify format of a cell – "numeric" or "string" . Defaults to "string" Name colspan Type integer Description Specify how many columns a cell spans. Name rowspan Type integer Description Specify how many rows a cell spans. Name align Type string Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left" Name width Type string Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Name classes Type string Description Classes to add to the table head cell. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table head cell. Name sort Type string Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true . Name sort Next Type string Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" . Options for caption heading component Name Type Description Name id Type string Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option. Name text Type string Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" . Name caption Type object Description Optional caption for the table caption. See macro options for caption . Name size Type string Description Size of the table caption – "s" , "m" , "l" or "xl" . Name classes Type string Description Classes to add to the table caption, for example "nhsuk-table__caption--l" . Name attributes Type object Description HTML attributes (for example data attributes) to add to the table caption. Options for caption component Name Type Description Name id Type string Description The ID of the caption. Name element Type string Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" . Name text Type string Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block. Name placement Type string Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" . Name size Type string Description Size of the caption – "m" , "l" , "xl" or "xxl" . Name classes Type string Description Classes to add to the caption. Name attributes Type object Description HTML attributes (for example data attributes) to add to the caption. Copy code {% from "tables/macro.njk" import table %} {{ table ({ caption : { text : "Users" , size : "m" }, firstCellIsHeader : true , head : [ { text : "Name" }, { text : "Email address" } ], rows : [ [ { text : "Aleksandrina Featherstonehaugh-Whitehead" , classes : "nhsuk-u-text-break-word" }, { text : "aleksandrina.featherstonehaughwhitehead23@folkestonepharmacy.test.com" , classes : "nhsuk-u-text-break-word" } ] ] }) }} Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : table word break Find out more about word-breaks, with or without a hyphen, in breaking up long words in the typography section . Displaying missing data Do not leave empty cells in your table. The only exception can be the top left cell. If you have missing data, include some short text to explain why it's missing, such as: "No data" "Not applicable" "Not known" To distinguish missing data from other table content, make the text dark grey by adding the class: "nhsuk-u-secondary-text-colour" Nunjucks option to the table cell. For HTML set it via the class attribute. Open this example in a new tab : table missing data HTML code for table missing data Nunjucks code for table missing data HTML code for table missing data Copy code < table class = "nhsuk-table" > < caption class = "nhsuk-table__caption" > Vaccinations given </ caption > < thead class = "nhsuk-table__head" > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "col" > Date </ th > < th class = "nhsuk-table__header" scope = "col" > Vaccine </ th > < th class = "nhsuk-table__header" scope = "col" > Product </ th > </ tr > </ thead > < tbody class = "nhsuk-table__body" > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "row" > 10 July 2024 </ th > < td class = "nhsuk-table__cell" > RSV </ td > < td class = "nhsuk-table__cell" > Abrysvo </ td > </ tr > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "row" > 6 September 2023 </ th > < td class = "nhsuk-table__cell" > Flu </ td > < td class = "nhsuk-table__cell nhsuk-u-secondary-text-colour" > No data </ td > </ tr > </ tbody > </ table > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : table missing data Nunjucks code for table missing data Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the table. Name border Type boolean Description If set to false , remove separating borders from all rows. Name last Row Border Type boolean Description If set to false , remove separating border from the last row. Name rows Type array Description Required. Array of table rows and cells. See macro options for rows . Name head Type array Description Array of table head cells. See macro options for head . Name caption Type object Description Table caption. See macro options for caption . Name caption Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option. Name caption Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option. Name first Cell Is Header Type boolean Description If set to true , first cell in table row will be a th instead of a td . Name compact Type boolean Description If set to true , vertical padding will be reduced for table cells. Name responsive Type boolean Description If set to true , responsive table classes will be applied. Name scroll Type boolean Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options. Name striped Type boolean Description If set to true , striped background colours will be applied to table rows. Name variant Type string Description Optional variant of table. You can use only "reverse" or empty values with this option. Name card Type object Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card . Name panel Type boolean Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option. Name panel Classes Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option. Name heading Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option. Name heading Level Type integer Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option. Name classes Type string Description Classes to add to the table container. Name table Classes Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table container. Name ascending Text Type string Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" . Name descending Text Type string Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" . Name sort Announcement Text Type string Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value. Options for rows array objects Name Type Description Name text Type string Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the table cell. Name header Type string Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option. Name href Type string Description If set, the table cell will become a link. Name format Type string Description Specify format of a cell – "numeric" or "string" . Defaults to "string" Name sort Value Type string Description Sort value text for cells in table rows. Name colspan Type integer Description Specify how many columns a cell spans. Name rowspan Type integer Description Specify how many rows a cell spans. Name align Type string Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left" Name width Type string Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Name classes Type string Description Classes to add to the table cell. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table cell. Options for head array objects Name Type Description Name text Type string Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored. Name html Type string Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the table head cell. Name href Type string Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction. Name format Type string Description Specify format of a cell – "numeric" or "string" . Defaults to "string" Name colspan Type integer Description Specify how many columns a cell spans. Name rowspan Type integer Description Specify how many rows a cell spans. Name align Type string Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left" Name width Type string Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Name classes Type string Description Classes to add to the table head cell. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table head cell. Name sort Type string Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true . Name sort Next Type string Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" . Options for caption heading component Name Type Description Name id Type string Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option. Name text Type string Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" . Name caption Type object Description Optional caption for the table caption. See macro options for caption . Name size Type string Description Size of the table caption – "s" , "m" , "l" or "xl" . Name classes Type string Description Classes to add to the table caption, for example "nhsuk-table__caption--l" . Name attributes Type object Description HTML attributes (for example data attributes) to add to the table caption. Options for caption component Name Type Description Name id Type string Description The ID of the caption. Name element Type string Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" . Name text Type string Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block. Name placement Type string Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" . Name size Type string Description Size of the caption – "m" , "l" , "xl" or "xxl" . Name classes Type string Description Classes to add to the caption. Name attributes Type object Description HTML attributes (for example data attributes) to add to the caption. Copy code {% from "tables/macro.njk" import table %} {{ table ({ caption : "Vaccinations given" , firstCellIsHeader : true , head : [ { text : "Date" }, { text : "Vaccine" }, { text : "Product" } ], rows : [ [ { text : "10 July 2024" }, { text : "RSV" }, { text : "Abrysvo" } ], [ { text : "6 September 2023" }, { text : "Flu" }, { text : "No data" , classes : "nhsuk-u-secondary-text-colour" } ] ] }) }} Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : table missing data Tables on dark backgrounds To show tables with white text on dark backgrounds, add the variant: "reverse" option using Nunjucks. For HTML add the nhsuk-table--reverse class to the table. Make sure all users can see the table content. The background colour must have a contrast ratio of at least 4.5:1 with white to meet WCAG 2.2 success criterion 1.4.3 Contrast (minimum), level AA (W3C) . Open this example in a new tab : table reverse HTML code for table reverse Nunjucks code for table reverse HTML code for table reverse Copy code < table class = "nhsuk-table nhsuk-table--reverse" > < caption class = "nhsuk-table__caption" > Skin symptoms and possible causes </ caption > < thead class = "nhsuk-table__head" > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "col" > Skin symptoms </ th > < th class = "nhsuk-table__header" scope = "col" > Possible cause </ th > </ tr > </ thead > < tbody class = "nhsuk-table__body" > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "row" > Blisters on lips or around the mouth </ th > < td class = "nhsuk-table__cell" > Cold sores </ td > </ tr > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "row" > Itchy, dry, cracked, sore </ th > < td class = "nhsuk-table__cell" > Eczema </ td > </ tr > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "row" > Itchy blisters </ th > < td class = "nhsuk-table__cell" > Shingles, chickenpox </ td > </ tr > </ tbody > </ table > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : table reverse Nunjucks code for table reverse Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the table. Name border Type boolean Description If set to false , remove separating borders from all rows. Name last Row Border Type boolean Description If set to false , remove separating border from the last row. Name rows Type array Description Required. Array of table rows and cells. See macro options for rows . Name head Type array Description Array of table head cells. See macro options for head . Name caption Type object Description Table caption. See macro options for caption . Name caption Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option. Name caption Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option. Name first Cell Is Header Type boolean Description If set to true , first cell in table row will be a th instead of a td . Name compact Type boolean Description If set to true , vertical padding will be reduced for table cells. Name responsive Type boolean Description If set to true , responsive table classes will be applied. Name scroll Type boolean Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options. Name striped Type boolean Description If set to true , striped background colours will be applied to table rows. Name variant Type string Description Optional variant of table. You can use only "reverse" or empty values with this option. Name card Type object Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card . Name panel Type boolean Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option. Name panel Classes Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option. Name heading Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option. Name heading Level Type integer Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option. Name classes Type string Description Classes to add to the table container. Name table Classes Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table container. Name ascending Text Type string Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" . Name descending Text Type string Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" . Name sort Announcement Text Type string Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value. Options for rows array objects Name Type Description Name text Type string Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the table cell. Name header Type string Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option. Name href Type string Description If set, the table cell will become a link. Name format Type string Description Specify format of a cell – "numeric" or "string" . Defaults to "string" Name sort Value Type string Description Sort value text for cells in table rows. Name colspan Type integer Description Specify how many columns a cell spans. Name rowspan Type integer Description Specify how many rows a cell spans. Name align Type string Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left" Name width Type string Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Name classes Type string Description Classes to add to the table cell. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table cell. Options for head array objects Name Type Description Name text Type string Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored. Name html Type string Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the table head cell. Name href Type string Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction. Name format Type string Description Specify format of a cell – "numeric" or "string" . Defaults to "string" Name colspan Type integer Description Specify how many columns a cell spans. Name rowspan Type integer Description Specify how many rows a cell spans. Name align Type string Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left" Name width Type string Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Name classes Type string Description Classes to add to the table head cell. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table head cell. Name sort Type string Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true . Name sort Next Type string Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" . Options for caption heading component Name Type Description Name id Type string Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option. Name text Type string Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" . Name caption Type object Description Optional caption for the table caption. See macro options for caption . Name size Type string Description Size of the table caption – "s" , "m" , "l" or "xl" . Name classes Type string Description Classes to add to the table caption, for example "nhsuk-table__caption--l" . Name attributes Type object Description HTML attributes (for example data attributes) to add to the table caption. Options for caption component Name Type Description Name id Type string Description The ID of the caption. Name element Type string Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" . Name text Type string Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block. Name placement Type string Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" . Name size Type string Description Size of the caption – "m" , "l" , "xl" or "xxl" . Name classes Type string Description Classes to add to the caption. Name attributes Type object Description HTML attributes (for example data attributes) to add to the caption. Copy code {% from "tables/macro.njk" import table %} {{ table ({ caption : "Skin symptoms and possible causes" , firstCellIsHeader : true , variant : "reverse" , head : [ { text : "Skin symptoms" }, { text : "Possible cause" } ], rows : [ [ { text : "Blisters on lips or around the mouth" }, { text : "Cold sores" } ], [ { text : "Itchy, dry, cracked, sore" }, { text : "Eczema" } ], [ { text : "Itchy blisters" }, { text : "Shingles, chickenpox" } ] ] }) }} Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : table reverse Accessibility Follow WebAIM's guidance for tables and: give tables captions use the scope attribute to associate the data cells with the appropriate headers let the browser window determine the width of the table whenever possible, to reduce horizontal scrolling Table captions Use the <caption> element to describe a table in the same way you would use a heading. A caption helps users find, navigate and understand tables. Style table captions to match the visual hierarchy of your page's content. If you're using Nunjucks, add the size: "l" option to the caption. For HTML add the nhsuk-table__caption--l class to the caption. You can use sizes s , m , l , xl . Table headers Use table headers to tell users what the rows and columns represent. Sortable tables The sortable table tells screen reader users that it can be sorted. When the user sorts the table, it announces what the new sort order is. Research Basic table This table tested well with users of health information on the NHS website. Responsive table This table was tested at HM Revenue & Customs. Sortable table This table was developed by NHS England and tested in the Run breast screening in England and Manage vaccinations in schools services. There is an overlap between sortable tables and: search filter pagination We want to understand better how they can work together. We have not yet developed a responsive or scrolling sortable table. If you need a responsive sorting table, you could try adding a select component . Please feed back if you develop any of these or implement server-side sorting. Table in a card We have also included an example of a table in a card in the NHS.UK frontend (in GitHub) . We have not published it in this list of components yet because it needs more testing. Help us improve this guidance Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public. Feed back or share insights on GitHub Read more about how to feed back or share insights . If you have any questions, get in touch with the service manual team. Updates to this page Updated: August 2026

- in Nunjucks, add the format: "numeric" option to the column header

- for HTML, add the nhsuk-table__header--numeric class to the column header and nhsuk-table__cell--numeric class to the cells

Columns set to numeric will work correctly with most number symbols, including commas, decimals, percentages and currencies.

Use numeric for dates.

##### Overriding the default sort order

You can override the default sort value to make the presented data easier for users to understand.

For example:

- dates: 30 November 2026 sorted as 2026-11-30

- months: January sorted as 01 January

- prefixes: The Whittington Hospital sorted as Whittington Hospital

To override the default sort value:

- in Nunjucks, add the sortValue option to the table cell

- for HTML, add the data-sort-value attribute to the table cell

Make sure to override the sort value for missing data . For example, setting sortValue: "£0" will sort the text "No data" consistently with other cells.

In this example the default sort order is by amount spent (descending).

- HTML code for table sortable custom

- Nunjucks code for table sortable custom

```text
<
table
class
=
"nhsuk-table nhsuk-table--sortable"
data-module
=
"nhsuk-table"
>
<
caption
class
=
"nhsuk-table__caption nhsuk-table__caption--m"
>
Organisations using the service
<
span
class
=
"nhsuk-u-visually-hidden"
>
(Column headers are sortable)
</
span
>
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
"nhsuk-table__header nhsuk-u-width-one-third"
scope
=
"col"
data-sort
>
Organisation
</
th
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
ODS code
</
th
>
<
th
class
=
"nhsuk-table__header nhsuk-u-text-align-right"
scope
=
"col"
data-sort
data-sort-next
=
"descending"
>
Joined
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
data-sort
aria-sort
=
"descending"
>
Amount spent
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Warrington and Halton Hospitals
</
th
>
<
td
class
=
"nhsuk-table__cell"
>
RY2N0
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
data-sort-value
=
"2024-07-18"
>
18 July 2024
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
£16,821
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
data-sort-value
=
"Christie"
>
The Christie
</
th
>
<
td
class
=
"nhsuk-table__cell"
>
J3P0W
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
data-sort-value
=
"2025-01-04"
>
4 January 2025
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
£12,013
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
University College London Hospitals
</
th
>
<
td
class
=
"nhsuk-table__cell"
>
RRV00
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
data-sort-value
=
"2025-12-02"
>
2 December 2025
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric"
>
£4,102
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
data-sort-value
=
"Whittington Hospital"
>
The Whittington Hospital
</
th
>
<
td
class
=
"nhsuk-table__cell"
>
RALWH
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
data-sort-value
=
"2022-08-21"
>
21 August 2022
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-table__cell--numeric nhsuk-u-secondary-text-colour"
data-sort-value
=
"£0"
>
No data
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the table.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. Array of table rows and cells. See macro options for rows .
Name head | Type array | Description Array of table head cells. See macro options for head .
Name caption | Type object | Description Table caption. See macro options for caption .
Name caption Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option.
Name caption Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option.
Name first Cell Is Header | Type boolean | Description If set to true , first cell in table row will be a th instead of a td .
Name compact | Type boolean | Description If set to true , vertical padding will be reduced for table cells.
Name responsive | Type boolean | Description If set to true , responsive table classes will be applied.
Name scroll | Type boolean | Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options.
Name striped | Type boolean | Description If set to true , striped background colours will be applied to table rows.
Name variant | Type string | Description Optional variant of table. You can use only "reverse" or empty values with this option.
Name card | Type object | Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card .
Name panel | Type boolean | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option.
Name panel Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option.
Name heading | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option.
Name heading Level | Type integer | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option.
Name classes | Type string | Description Classes to add to the table container.
Name table Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table container.
Name ascending Text | Type string | Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" .
Name descending Text | Type string | Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" .
Name sort Announcement Text | Type string | Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table cell.
Name header | Type string | Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option.
Name href | Type string | Description If set, the table cell will become a link.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name sort Value | Type string | Description Sort value text for cells in table rows.
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table cell.

Name | Type | Description
Name text | Type string | Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored.
Name html | Type string | Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table head cell.
Name href | Type string | Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table head cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table head cell.
Name sort | Type string | Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true .
Name sort Next | Type string | Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" .

Name | Type | Description
Name id | Type string | Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option.
Name text | Type string | Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" .
Name caption | Type object | Description Optional caption for the table caption. See macro options for caption .
Name size | Type string | Description Size of the table caption – "s" , "m" , "l" or "xl" .
Name classes | Type string | Description Classes to add to the table caption, for example "nhsuk-table__caption--l" .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table caption.

Name | Type | Description
Name id | Type string | Description The ID of the caption.
Name element | Type string | Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" .
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block.
Name placement | Type string | Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" .
Name size | Type string | Description Size of the caption – "m" , "l" , "xl" or "xxl" .
Name classes | Type string | Description Classes to add to the caption.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the caption.

```text
{%
from
"tables/macro.njk"
import
table
%}
{{
table
({
caption
: {
text
:
"Organisations using the service"
,
size
:
"m"
},
firstCellIsHeader
:
true
,
head
: [
    {
text
:
"Organisation"
,
width
:
"one-third"
,
sort
:
true
},
    {
text
:
"ODS code"
},
    {
text
:
"Joined"
,
align
:
"right"
,
sort
:
true
,
sortNext
:
"descending"
},
    {
text
:
"Amount spent"
,
format
:
"numeric"
,
sort
:
"descending"
}
  ],
rows
: [
    [
      {
text
:
"Warrington and Halton Hospitals"
},
      {
text
:
"RY2N0"
},
      {
text
:
"18 July 2024"
,
sortValue
:
"2024-07-18"
},
      {
text
:
"£16,821"
}
    ],
    [
      {
text
:
"The Christie"
,
sortValue
:
"Christie"
},
      {
text
:
"J3P0W"
},
      {
text
:
"4 January 2025"
,
sortValue
:
"2025-01-04"
},
      {
text
:
"£12,013"
}
    ],
    [
      {
text
:
"University College London Hospitals"
},
      {
text
:
"RRV00"
},
      {
text
:
"2 December 2025"
,
sortValue
:
"2025-12-02"
},
      {
text
:
"£4,102"
}
    ],
    [
      {
text
:
"The Whittington Hospital"
,
sortValue
:
"Whittington Hospital"
},
      {
text
:
"RALWH"
},
      {
text
:
"21 August 2022"
,
sortValue
:
"2022-08-21"
},
      {
text
:
"No data"
,
sortValue
:
"£0"
,
classes
:
"nhsuk-u-secondary-text-colour"
}
    ]
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

#### Sort more than 1 page of data

If your table is paginated, sorting should be applied server-side across all pages. Do not sort the current page only.

Use server-side sorting by adding a link to the column header to navigate to a page with the table sorting already applied. You will need to:

- build your own server-side function

- return users to the first page of new results after sorting

- test with users

This example shows a paginated table but it does not work in the browser. The functionality would need to be built server-side.

- HTML code for table sortable server side last login descending

- Nunjucks code for table sortable server side last login descending

```text
<
table
class
=
"nhsuk-table nhsuk-table--sortable"
>
<
caption
class
=
"nhsuk-table__caption nhsuk-table__caption--m"
>
Users
<
span
class
=
"nhsuk-u-visually-hidden"
>
(Column headers are sortable)
</
span
>
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
"nhsuk-table__header nhsuk-u-width-one-half"
scope
=
"col"
data-sort
>
<
a
class
=
"nhsuk-link"
href
=
"sortable-server-side"
>
Name
</
a
>
</
th
>
<
th
class
=
"nhsuk-table__header nhsuk-u-text-align-right nhsuk-u-width-one-third nhsuk-u-nowrap"
scope
=
"col"
data-sort
aria-sort
=
"descending"
>
<
a
class
=
"nhsuk-link"
href
=
"sortable-server-side-last-login-ascending"
>
Last log in
</
a
>
</
th
>
<
th
class
=
"nhsuk-table__header nhsuk-u-text-align-right"
scope
=
"col"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Action
</
span
>
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
Ro Nkosi
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
>
28 June 2026
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
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
details for Ro Nkosi
</
span
>
</
a
>
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
Stellan Park
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
>
20 June 2026
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
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
details for Stellan Park
</
span
>
</
a
>
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
Tamsin Foley-Whitworth
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
>
14 June 2026
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
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
details for Tamsin Foley-Whitworth
</
span
>
</
a
>
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
Uta Brennan
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
>
7 June 2026
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
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
details for Uta Brennan
</
span
>
</
a
>
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
Val Cruz
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
>
1 June 2026
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
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
details for Val Cruz
</
span
>
</
a
>
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
Wendell Shaw
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
>
25 May 2026
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
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
details for Wendell Shaw
</
span
>
</
a
>
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
Xanthe Beaumont
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
>
19 May 2026
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
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
details for Xanthe Beaumont
</
span
>
</
a
>
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
Yolanda Pierce
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
>
13 May 2026
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
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
details for Yolanda Pierce
</
span
>
</
a
>
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
Zadie Munroe
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
>
7 May 2026
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
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
details for Zadie Munroe
</
span
>
</
a
>
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
Reuben Tate
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
>
1 May 2026
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-align-right"
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
details for Reuben Tate
</
span
>
</
a
>
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
<
nav
class
=
"nhsuk-pagination nhsuk-pagination--numbered"
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
"nhsuk-pagination__list"
>
<
li
class
=
"nhsuk-pagination__item nhsuk-pagination__item--current"
>
<
a
class
=
"nhsuk-pagination__link"
href
=
"#"
aria-label
=
"Page 1"
aria-current
=
"page"
>
1
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
"nhsuk-pagination__item"
>
<
a
class
=
"nhsuk-pagination__link"
href
=
"#"
aria-label
=
"Page 2"
>
2
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
"nhsuk-pagination__item"
>
<
a
class
=
"nhsuk-pagination__link"
href
=
"#"
aria-label
=
"Page 3"
>
3
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
"nhsuk-pagination__item"
>
<
a
class
=
"nhsuk-pagination__link"
href
=
"#"
aria-label
=
"Page 4"
>
4
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
"nhsuk-pagination__item"
>
<
a
class
=
"nhsuk-pagination__link"
href
=
"#"
aria-label
=
"Page 5"
>
5
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
"nhsuk-pagination__item"
>
<
a
class
=
"nhsuk-pagination__link"
href
=
"#"
aria-label
=
"Page 6"
>
6
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
a
href
=
"#"
class
=
"nhsuk-pagination__next"
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
nav
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the table.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. Array of table rows and cells. See macro options for rows .
Name head | Type array | Description Array of table head cells. See macro options for head .
Name caption | Type object | Description Table caption. See macro options for caption .
Name caption Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option.
Name caption Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option.
Name first Cell Is Header | Type boolean | Description If set to true , first cell in table row will be a th instead of a td .
Name compact | Type boolean | Description If set to true , vertical padding will be reduced for table cells.
Name responsive | Type boolean | Description If set to true , responsive table classes will be applied.
Name scroll | Type boolean | Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options.
Name striped | Type boolean | Description If set to true , striped background colours will be applied to table rows.
Name variant | Type string | Description Optional variant of table. You can use only "reverse" or empty values with this option.
Name card | Type object | Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card .
Name panel | Type boolean | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option.
Name panel Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option.
Name heading | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option.
Name heading Level | Type integer | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option.
Name classes | Type string | Description Classes to add to the table container.
Name table Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table container.
Name ascending Text | Type string | Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" .
Name descending Text | Type string | Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" .
Name sort Announcement Text | Type string | Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table cell.
Name header | Type string | Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option.
Name href | Type string | Description If set, the table cell will become a link.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name sort Value | Type string | Description Sort value text for cells in table rows.
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table cell.

Name | Type | Description
Name text | Type string | Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored.
Name html | Type string | Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table head cell.
Name href | Type string | Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table head cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table head cell.
Name sort | Type string | Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true .
Name sort Next | Type string | Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" .

Name | Type | Description
Name id | Type string | Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option.
Name text | Type string | Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" .
Name caption | Type object | Description Optional caption for the table caption. See macro options for caption .
Name size | Type string | Description Size of the table caption – "s" , "m" , "l" or "xl" .
Name classes | Type string | Description Classes to add to the table caption, for example "nhsuk-table__caption--l" .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table caption.

Name | Type | Description
Name id | Type string | Description The ID of the caption.
Name element | Type string | Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" .
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block.
Name placement | Type string | Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" .
Name size | Type string | Description Size of the caption – "m" , "l" , "xl" or "xxl" .
Name classes | Type string | Description Classes to add to the caption.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the caption.

```text
{%
from
"tables/macro.njk"
import
table
%}
{%
from
"pagination/macro.njk"
import
pagination
%}
{{
table
({
caption
: {
text
:
"Users"
,
size
:
"m"
},
head
: [
    {
text
:
"Name"
,
href
:
"sortable-server-side"
,
width
:
"one-half"
,
sort
:
true
},
    {
text
:
"Last log in"
,
href
:
"sortable-server-side-last-login-ascending"
,
width
:
"one-third"
,
align
:
"right"
,
classes
:
"nhsuk-u-nowrap"
,
sort
:
"descending"
},
    {
visuallyHiddenText
:
"Action"
,
align
:
"right"
}
  ],
rows
: [
    [
      {
text
:
"Ro Nkosi"
},
      {
text
:
"28 June 2026"
},
      {
text
:
"Change"
,
visuallyHiddenText
:
"details for Ro Nkosi"
,
href
:
"#"
}
    ],
    [
      {
text
:
"Stellan Park"
},
      {
text
:
"20 June 2026"
},
      {
text
:
"Change"
,
visuallyHiddenText
:
"details for Stellan Park"
,
href
:
"#"
}
    ],
    [
      {
text
:
"Tamsin Foley-Whitworth"
},
      {
text
:
"14 June 2026"
},
      {
text
:
"Change"
,
visuallyHiddenText
:
"details for Tamsin Foley-Whitworth"
,
href
:
"#"
}
    ],
    [
      {
text
:
"Uta Brennan"
},
      {
text
:
"7 June 2026"
},
      {
text
:
"Change"
,
visuallyHiddenText
:
"details for Uta Brennan"
,
href
:
"#"
}
    ],
    [
      {
text
:
"Val Cruz"
},
      {
text
:
"1 June 2026"
},
      {
text
:
"Change"
,
visuallyHiddenText
:
"details for Val Cruz"
,
href
:
"#"
}
    ],
    [
      {
text
:
"Wendell Shaw"
},
      {
text
:
"25 May 2026"
},
      {
text
:
"Change"
,
visuallyHiddenText
:
"details for Wendell Shaw"
,
href
:
"#"
}
    ],
    [
      {
text
:
"Xanthe Beaumont"
},
      {
text
:
"19 May 2026"
},
      {
text
:
"Change"
,
visuallyHiddenText
:
"details for Xanthe Beaumont"
,
href
:
"#"
}
    ],
    [
      {
text
:
"Yolanda Pierce"
},
      {
text
:
"13 May 2026"
},
      {
text
:
"Change"
,
visuallyHiddenText
:
"details for Yolanda Pierce"
,
href
:
"#"
}
    ],
    [
      {
text
:
"Zadie Munroe"
},
      {
text
:
"7 May 2026"
},
      {
text
:
"Change"
,
visuallyHiddenText
:
"details for Zadie Munroe"
,
href
:
"#"
}
    ],
    [
      {
text
:
"Reuben Tate"
},
      {
text
:
"1 May 2026"
},
      {
text
:
"Change"
,
visuallyHiddenText
:
"details for Reuben Tate"
,
href
:
"#"
}
    ]
  ]
})
}}
{{
pagination
({
next
: {
href
:
"#"
},
items
: [
    {
number
:
1
,
href
:
"#"
,
current
:
true
},
    {
number
:
2
,
href
:
"#"
},
    {
number
:
3
,
href
:
"#"
},
    {
number
:
4
,
href
:
"#"
},
    {
number
:
5
,
href
:
"#"
},
    {
number
:
6
,
href
:
"#"
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

#### Consider search and filter

Filters reduce the amount of data so that users can focus on what they want. Search helps them find specific things they need.

For example, search or filter may work better than sorting for:

- names

- NHS numbers or other codes

- medical conditions

If your team is researching filtering, please feed back your findings via our community backlog issue on filtering a list (in GitHub) . Using word-breaks in a table To avoid very long words, such as email addresses, breaking the layout of a table, you can use word-breaks. To do this: in Nunjucks, add the class: "nhsuk-u-text-break-word" option to the table cell for HTML, add the nhsuk-u-text-break-word override class to the table cell Open this example in a new tab : table word break HTML code for table word break Nunjucks code for table word break HTML code for table word break Copy code < table class = "nhsuk-table" > < caption class = "nhsuk-table__caption nhsuk-table__caption--m" > Users </ caption > < thead class = "nhsuk-table__head" > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "col" > Name </ th > < th class = "nhsuk-table__header" scope = "col" > Email address </ th > </ tr > </ thead > < tbody class = "nhsuk-table__body" > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header nhsuk-u-text-break-word" scope = "row" > Aleksandrina Featherstonehaugh-Whitehead </ th > < td class = "nhsuk-table__cell nhsuk-u-text-break-word" > aleksandrina.featherstonehaughwhitehead23@folkestonepharmacy.test.com </ td > </ tr > </ tbody > </ table > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : table word break Nunjucks code for table word break Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the table. Name border Type boolean Description If set to false , remove separating borders from all rows. Name last Row Border Type boolean Description If set to false , remove separating border from the last row. Name rows Type array Description Required. Array of table rows and cells. See macro options for rows . Name head Type array Description Array of table head cells. See macro options for head . Name caption Type object Description Table caption. See macro options for caption . Name caption Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option. Name caption Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option. Name first Cell Is Header Type boolean Description If set to true , first cell in table row will be a th instead of a td . Name compact Type boolean Description If set to true , vertical padding will be reduced for table cells. Name responsive Type boolean Description If set to true , responsive table classes will be applied. Name scroll Type boolean Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options. Name striped Type boolean Description If set to true , striped background colours will be applied to table rows. Name variant Type string Description Optional variant of table. You can use only "reverse" or empty values with this option. Name card Type object Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card . Name panel Type boolean Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option. Name panel Classes Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option. Name heading Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option. Name heading Level Type integer Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option. Name classes Type string Description Classes to add to the table container. Name table Classes Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table container. Name ascending Text Type string Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" . Name descending Text Type string Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" . Name sort Announcement Text Type string Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value. Options for rows array objects Name Type Description Name text Type string Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the table cell. Name header Type string Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option. Name href Type string Description If set, the table cell will become a link. Name format Type string Description Specify format of a cell – "numeric" or "string" . Defaults to "string" Name sort Value Type string Description Sort value text for cells in table rows. Name colspan Type integer Description Specify how many columns a cell spans. Name rowspan Type integer Description Specify how many rows a cell spans. Name align Type string Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left" Name width Type string Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Name classes Type string Description Classes to add to the table cell. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table cell. Options for head array objects Name Type Description Name text Type string Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored. Name html Type string Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the table head cell. Name href Type string Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction. Name format Type string Description Specify format of a cell – "numeric" or "string" . Defaults to "string" Name colspan Type integer Description Specify how many columns a cell spans. Name rowspan Type integer Description Specify how many rows a cell spans. Name align Type string Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left" Name width Type string Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Name classes Type string Description Classes to add to the table head cell. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table head cell. Name sort Type string Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true . Name sort Next Type string Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" . Options for caption heading component Name Type Description Name id Type string Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option. Name text Type string Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" . Name caption Type object Description Optional caption for the table caption. See macro options for caption . Name size Type string Description Size of the table caption – "s" , "m" , "l" or "xl" . Name classes Type string Description Classes to add to the table caption, for example "nhsuk-table__caption--l" . Name attributes Type object Description HTML attributes (for example data attributes) to add to the table caption. Options for caption component Name Type Description Name id Type string Description The ID of the caption. Name element Type string Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" . Name text Type string Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block. Name placement Type string Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" . Name size Type string Description Size of the caption – "m" , "l" , "xl" or "xxl" . Name classes Type string Description Classes to add to the caption. Name attributes Type object Description HTML attributes (for example data attributes) to add to the caption. Copy code {% from "tables/macro.njk" import table %} {{ table ({ caption : { text : "Users" , size : "m" }, firstCellIsHeader : true , head : [ { text : "Name" }, { text : "Email address" } ], rows : [ [ { text : "Aleksandrina Featherstonehaugh-Whitehead" , classes : "nhsuk-u-text-break-word" }, { text : "aleksandrina.featherstonehaughwhitehead23@folkestonepharmacy.test.com" , classes : "nhsuk-u-text-break-word" } ] ] }) }} Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : table word break Find out more about word-breaks, with or without a hyphen, in breaking up long words in the typography section . Displaying missing data Do not leave empty cells in your table. The only exception can be the top left cell. If you have missing data, include some short text to explain why it's missing, such as: "No data" "Not applicable" "Not known" To distinguish missing data from other table content, make the text dark grey by adding the class: "nhsuk-u-secondary-text-colour" Nunjucks option to the table cell. For HTML set it via the class attribute. Open this example in a new tab : table missing data HTML code for table missing data Nunjucks code for table missing data HTML code for table missing data Copy code < table class = "nhsuk-table" > < caption class = "nhsuk-table__caption" > Vaccinations given </ caption > < thead class = "nhsuk-table__head" > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "col" > Date </ th > < th class = "nhsuk-table__header" scope = "col" > Vaccine </ th > < th class = "nhsuk-table__header" scope = "col" > Product </ th > </ tr > </ thead > < tbody class = "nhsuk-table__body" > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "row" > 10 July 2024 </ th > < td class = "nhsuk-table__cell" > RSV </ td > < td class = "nhsuk-table__cell" > Abrysvo </ td > </ tr > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "row" > 6 September 2023 </ th > < td class = "nhsuk-table__cell" > Flu </ td > < td class = "nhsuk-table__cell nhsuk-u-secondary-text-colour" > No data </ td > </ tr > </ tbody > </ table > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : table missing data Nunjucks code for table missing data Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the table. Name border Type boolean Description If set to false , remove separating borders from all rows. Name last Row Border Type boolean Description If set to false , remove separating border from the last row. Name rows Type array Description Required. Array of table rows and cells. See macro options for rows . Name head Type array Description Array of table head cells. See macro options for head . Name caption Type object Description Table caption. See macro options for caption . Name caption Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option. Name caption Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option. Name first Cell Is Header Type boolean Description If set to true , first cell in table row will be a th instead of a td . Name compact Type boolean Description If set to true , vertical padding will be reduced for table cells. Name responsive Type boolean Description If set to true , responsive table classes will be applied. Name scroll Type boolean Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options. Name striped Type boolean Description If set to true , striped background colours will be applied to table rows. Name variant Type string Description Optional variant of table. You can use only "reverse" or empty values with this option. Name card Type object Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card . Name panel Type boolean Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option. Name panel Classes Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option. Name heading Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option. Name heading Level Type integer Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option. Name classes Type string Description Classes to add to the table container. Name table Classes Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table container. Name ascending Text Type string Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" . Name descending Text Type string Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" . Name sort Announcement Text Type string Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value. Options for rows array objects Name Type Description Name text Type string Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the table cell. Name header Type string Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option. Name href Type string Description If set, the table cell will become a link. Name format Type string Description Specify format of a cell – "numeric" or "string" . Defaults to "string" Name sort Value Type string Description Sort value text for cells in table rows. Name colspan Type integer Description Specify how many columns a cell spans. Name rowspan Type integer Description Specify how many rows a cell spans. Name align Type string Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left" Name width Type string Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Name classes Type string Description Classes to add to the table cell. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table cell. Options for head array objects Name Type Description Name text Type string Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored. Name html Type string Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the table head cell. Name href Type string Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction. Name format Type string Description Specify format of a cell – "numeric" or "string" . Defaults to "string" Name colspan Type integer Description Specify how many columns a cell spans. Name rowspan Type integer Description Specify how many rows a cell spans. Name align Type string Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left" Name width Type string Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Name classes Type string Description Classes to add to the table head cell. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table head cell. Name sort Type string Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true . Name sort Next Type string Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" . Options for caption heading component Name Type Description Name id Type string Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option. Name text Type string Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" . Name caption Type object Description Optional caption for the table caption. See macro options for caption . Name size Type string Description Size of the table caption – "s" , "m" , "l" or "xl" . Name classes Type string Description Classes to add to the table caption, for example "nhsuk-table__caption--l" . Name attributes Type object Description HTML attributes (for example data attributes) to add to the table caption. Options for caption component Name Type Description Name id Type string Description The ID of the caption. Name element Type string Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" . Name text Type string Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block. Name placement Type string Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" . Name size Type string Description Size of the caption – "m" , "l" , "xl" or "xxl" . Name classes Type string Description Classes to add to the caption. Name attributes Type object Description HTML attributes (for example data attributes) to add to the caption. Copy code {% from "tables/macro.njk" import table %} {{ table ({ caption : "Vaccinations given" , firstCellIsHeader : true , head : [ { text : "Date" }, { text : "Vaccine" }, { text : "Product" } ], rows : [ [ { text : "10 July 2024" }, { text : "RSV" }, { text : "Abrysvo" } ], [ { text : "6 September 2023" }, { text : "Flu" }, { text : "No data" , classes : "nhsuk-u-secondary-text-colour" } ] ] }) }} Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : table missing data Tables on dark backgrounds To show tables with white text on dark backgrounds, add the variant: "reverse" option using Nunjucks. For HTML add the nhsuk-table--reverse class to the table. Make sure all users can see the table content. The background colour must have a contrast ratio of at least 4.5:1 with white to meet WCAG 2.2 success criterion 1.4.3 Contrast (minimum), level AA (W3C) . Open this example in a new tab : table reverse HTML code for table reverse Nunjucks code for table reverse HTML code for table reverse Copy code < table class = "nhsuk-table nhsuk-table--reverse" > < caption class = "nhsuk-table__caption" > Skin symptoms and possible causes </ caption > < thead class = "nhsuk-table__head" > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "col" > Skin symptoms </ th > < th class = "nhsuk-table__header" scope = "col" > Possible cause </ th > </ tr > </ thead > < tbody class = "nhsuk-table__body" > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "row" > Blisters on lips or around the mouth </ th > < td class = "nhsuk-table__cell" > Cold sores </ td > </ tr > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "row" > Itchy, dry, cracked, sore </ th > < td class = "nhsuk-table__cell" > Eczema </ td > </ tr > < tr class = "nhsuk-table__row" > < th class = "nhsuk-table__header" scope = "row" > Itchy blisters </ th > < td class = "nhsuk-table__cell" > Shingles, chickenpox </ td > </ tr > </ tbody > </ table > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : table reverse Nunjucks code for table reverse Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the table. Name border Type boolean Description If set to false , remove separating borders from all rows. Name last Row Border Type boolean Description If set to false , remove separating border from the last row. Name rows Type array Description Required. Array of table rows and cells. See macro options for rows . Name head Type array Description Array of table head cells. See macro options for head . Name caption Type object Description Table caption. See macro options for caption . Name caption Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option. Name caption Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option. Name first Cell Is Header Type boolean Description If set to true , first cell in table row will be a th instead of a td . Name compact Type boolean Description If set to true , vertical padding will be reduced for table cells. Name responsive Type boolean Description If set to true , responsive table classes will be applied. Name scroll Type boolean Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options. Name striped Type boolean Description If set to true , striped background colours will be applied to table rows. Name variant Type string Description Optional variant of table. You can use only "reverse" or empty values with this option. Name card Type object Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card . Name panel Type boolean Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option. Name panel Classes Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option. Name heading Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option. Name heading Level Type integer Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option. Name classes Type string Description Classes to add to the table container. Name table Classes Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table container. Name ascending Text Type string Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" . Name descending Text Type string Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" . Name sort Announcement Text Type string Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value. Options for rows array objects Name Type Description Name text Type string Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the table cell. Name header Type string Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option. Name href Type string Description If set, the table cell will become a link. Name format Type string Description Specify format of a cell – "numeric" or "string" . Defaults to "string" Name sort Value Type string Description Sort value text for cells in table rows. Name colspan Type integer Description Specify how many columns a cell spans. Name rowspan Type integer Description Specify how many rows a cell spans. Name align Type string Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left" Name width Type string Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Name classes Type string Description Classes to add to the table cell. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table cell. Options for head array objects Name Type Description Name text Type string Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored. Name html Type string Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the table head cell. Name href Type string Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction. Name format Type string Description Specify format of a cell – "numeric" or "string" . Defaults to "string" Name colspan Type integer Description Specify how many columns a cell spans. Name rowspan Type integer Description Specify how many rows a cell spans. Name align Type string Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left" Name width Type string Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Name classes Type string Description Classes to add to the table head cell. Name attributes Type object Description HTML attributes (for example data attributes) to add to the table head cell. Name sort Type string Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true . Name sort Next Type string Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" . Options for caption heading component Name Type Description Name id Type string Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option. Name text Type string Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" . Name caption Type object Description Optional caption for the table caption. See macro options for caption . Name size Type string Description Size of the table caption – "s" , "m" , "l" or "xl" . Name classes Type string Description Classes to add to the table caption, for example "nhsuk-table__caption--l" . Name attributes Type object Description HTML attributes (for example data attributes) to add to the table caption. Options for caption component Name Type Description Name id Type string Description The ID of the caption. Name element Type string Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" . Name text Type string Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block. Name placement Type string Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" . Name size Type string Description Size of the caption – "m" , "l" , "xl" or "xxl" . Name classes Type string Description Classes to add to the caption. Name attributes Type object Description HTML attributes (for example data attributes) to add to the caption. Copy code {% from "tables/macro.njk" import table %} {{ table ({ caption : "Skin symptoms and possible causes" , firstCellIsHeader : true , variant : "reverse" , head : [ { text : "Skin symptoms" }, { text : "Possible cause" } ], rows : [ [ { text : "Blisters on lips or around the mouth" }, { text : "Cold sores" } ], [ { text : "Itchy, dry, cracked, sore" }, { text : "Eczema" } ], [ { text : "Itchy blisters" }, { text : "Shingles, chickenpox" } ] ] }) }} Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : table reverse Accessibility Follow WebAIM's guidance for tables and: give tables captions use the scope attribute to associate the data cells with the appropriate headers let the browser window determine the width of the table whenever possible, to reduce horizontal scrolling Table captions Use the <caption> element to describe a table in the same way you would use a heading. A caption helps users find, navigate and understand tables. Style table captions to match the visual hierarchy of your page's content. If you're using Nunjucks, add the size: "l" option to the caption. For HTML add the nhsuk-table__caption--l class to the caption. You can use sizes s , m , l , xl . Table headers Use table headers to tell users what the rows and columns represent. Sortable tables The sortable table tells screen reader users that it can be sorted. When the user sorts the table, it announces what the new sort order is. Research Basic table This table tested well with users of health information on the NHS website. Responsive table This table was tested at HM Revenue & Customs. Sortable table This table was developed by NHS England and tested in the Run breast screening in England and Manage vaccinations in schools services. There is an overlap between sortable tables and: search filter pagination We want to understand better how they can work together. We have not yet developed a responsive or scrolling sortable table. If you need a responsive sorting table, you could try adding a select component . Please feed back if you develop any of these or implement server-side sorting. Table in a card We have also included an example of a table in a card in the NHS.UK frontend (in GitHub) . We have not published it in this list of components yet because it needs more testing. Help us improve this guidance Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public. Feed back or share insights on GitHub Read more about how to feed back or share insights . If you have any questions, get in touch with the service manual team. Updates to this page Updated: August 2026

## Using word-breaks in a table

To avoid very long words, such as email addresses, breaking the layout of a table, you can use word-breaks. To do this:

- in Nunjucks, add the class: "nhsuk-u-text-break-word" option to the table cell

- for HTML, add the nhsuk-u-text-break-word override class to the table cell

- HTML code for table word break

- Nunjucks code for table word break

```text
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
"nhsuk-table__caption nhsuk-table__caption--m"
>
Users
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
Name
</
th
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
Email address
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
th
class
=
"nhsuk-table__header nhsuk-u-text-break-word"
scope
=
"row"
>
Aleksandrina Featherstonehaugh-Whitehead
</
th
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-text-break-word"
>
aleksandrina.featherstonehaughwhitehead23@folkestonepharmacy.test.com
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the table.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. Array of table rows and cells. See macro options for rows .
Name head | Type array | Description Array of table head cells. See macro options for head .
Name caption | Type object | Description Table caption. See macro options for caption .
Name caption Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option.
Name caption Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option.
Name first Cell Is Header | Type boolean | Description If set to true , first cell in table row will be a th instead of a td .
Name compact | Type boolean | Description If set to true , vertical padding will be reduced for table cells.
Name responsive | Type boolean | Description If set to true , responsive table classes will be applied.
Name scroll | Type boolean | Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options.
Name striped | Type boolean | Description If set to true , striped background colours will be applied to table rows.
Name variant | Type string | Description Optional variant of table. You can use only "reverse" or empty values with this option.
Name card | Type object | Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card .
Name panel | Type boolean | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option.
Name panel Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option.
Name heading | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option.
Name heading Level | Type integer | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option.
Name classes | Type string | Description Classes to add to the table container.
Name table Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table container.
Name ascending Text | Type string | Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" .
Name descending Text | Type string | Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" .
Name sort Announcement Text | Type string | Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table cell.
Name header | Type string | Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option.
Name href | Type string | Description If set, the table cell will become a link.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name sort Value | Type string | Description Sort value text for cells in table rows.
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table cell.

Name | Type | Description
Name text | Type string | Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored.
Name html | Type string | Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table head cell.
Name href | Type string | Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table head cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table head cell.
Name sort | Type string | Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true .
Name sort Next | Type string | Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" .

Name | Type | Description
Name id | Type string | Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option.
Name text | Type string | Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" .
Name caption | Type object | Description Optional caption for the table caption. See macro options for caption .
Name size | Type string | Description Size of the table caption – "s" , "m" , "l" or "xl" .
Name classes | Type string | Description Classes to add to the table caption, for example "nhsuk-table__caption--l" .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table caption.

Name | Type | Description
Name id | Type string | Description The ID of the caption.
Name element | Type string | Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" .
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block.
Name placement | Type string | Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" .
Name size | Type string | Description Size of the caption – "m" , "l" , "xl" or "xxl" .
Name classes | Type string | Description Classes to add to the caption.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the caption.

```text
{%
from
"tables/macro.njk"
import
table
%}
{{
table
({
caption
: {
text
:
"Users"
,
size
:
"m"
},
firstCellIsHeader
:
true
,
head
: [
    {
text
:
"Name"
},
    {
text
:
"Email address"
}
  ],
rows
: [
    [
      {
text
:
"Aleksandrina Featherstonehaugh-Whitehead"
,
classes
:
"nhsuk-u-text-break-word"
},
      {
text
:
"aleksandrina.featherstonehaughwhitehead23@folkestonepharmacy.test.com"
,
classes
:
"nhsuk-u-text-break-word"
}
    ]
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Find out more about word-breaks, with or without a hyphen, in breaking up long words in the typography section .

## Displaying missing data

Do not leave empty cells in your table. The only exception can be the top left cell. If you have missing data, include some short text to explain why it's missing, such as:

- "No data"

- "Not applicable"

- "Not known"

To distinguish missing data from other table content, make the text dark grey by adding the class: "nhsuk-u-secondary-text-colour" Nunjucks option to the table cell. For HTML set it via the class attribute.

- HTML code for table missing data

- Nunjucks code for table missing data

```text
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
Vaccinations given
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
Date
</
th
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
Vaccine
</
th
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
Product
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
10 July 2024
</
th
>
<
td
class
=
"nhsuk-table__cell"
>
RSV
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
Abrysvo
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
6 September 2023
</
th
>
<
td
class
=
"nhsuk-table__cell"
>
Flu
</
td
>
<
td
class
=
"nhsuk-table__cell nhsuk-u-secondary-text-colour"
>
No data
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the table.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. Array of table rows and cells. See macro options for rows .
Name head | Type array | Description Array of table head cells. See macro options for head .
Name caption | Type object | Description Table caption. See macro options for caption .
Name caption Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option.
Name caption Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option.
Name first Cell Is Header | Type boolean | Description If set to true , first cell in table row will be a th instead of a td .
Name compact | Type boolean | Description If set to true , vertical padding will be reduced for table cells.
Name responsive | Type boolean | Description If set to true , responsive table classes will be applied.
Name scroll | Type boolean | Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options.
Name striped | Type boolean | Description If set to true , striped background colours will be applied to table rows.
Name variant | Type string | Description Optional variant of table. You can use only "reverse" or empty values with this option.
Name card | Type object | Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card .
Name panel | Type boolean | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option.
Name panel Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option.
Name heading | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option.
Name heading Level | Type integer | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option.
Name classes | Type string | Description Classes to add to the table container.
Name table Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table container.
Name ascending Text | Type string | Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" .
Name descending Text | Type string | Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" .
Name sort Announcement Text | Type string | Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table cell.
Name header | Type string | Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option.
Name href | Type string | Description If set, the table cell will become a link.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name sort Value | Type string | Description Sort value text for cells in table rows.
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table cell.

Name | Type | Description
Name text | Type string | Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored.
Name html | Type string | Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table head cell.
Name href | Type string | Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table head cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table head cell.
Name sort | Type string | Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true .
Name sort Next | Type string | Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" .

Name | Type | Description
Name id | Type string | Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option.
Name text | Type string | Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" .
Name caption | Type object | Description Optional caption for the table caption. See macro options for caption .
Name size | Type string | Description Size of the table caption – "s" , "m" , "l" or "xl" .
Name classes | Type string | Description Classes to add to the table caption, for example "nhsuk-table__caption--l" .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table caption.

Name | Type | Description
Name id | Type string | Description The ID of the caption.
Name element | Type string | Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" .
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block.
Name placement | Type string | Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" .
Name size | Type string | Description Size of the caption – "m" , "l" , "xl" or "xxl" .
Name classes | Type string | Description Classes to add to the caption.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the caption.

```text
{%
from
"tables/macro.njk"
import
table
%}
{{
table
({
caption
:
"Vaccinations given"
,
firstCellIsHeader
:
true
,
head
: [
    {
text
:
"Date"
},
    {
text
:
"Vaccine"
},
    {
text
:
"Product"
}
  ],
rows
: [
    [
      {
text
:
"10 July 2024"
},
      {
text
:
"RSV"
},
      {
text
:
"Abrysvo"
}
    ],
    [
      {
text
:
"6 September 2023"
},
      {
text
:
"Flu"
},
      {
text
:
"No data"
,
classes
:
"nhsuk-u-secondary-text-colour"
}
    ]
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## Tables on dark backgrounds

To show tables with white text on dark backgrounds, add the variant: "reverse" option using Nunjucks. For HTML add the nhsuk-table--reverse class to the table.

Make sure all users can see the table content. The background colour must have a contrast ratio of at least 4.5:1 with white to meet WCAG 2.2 success criterion 1.4.3 Contrast (minimum), level AA (W3C) .

- HTML code for table reverse

- Nunjucks code for table reverse

```text
<
table
class
=
"nhsuk-table nhsuk-table--reverse"
>
<
caption
class
=
"nhsuk-table__caption"
>
Skin symptoms and possible causes
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
Skin symptoms
</
th
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
Possible cause
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Blisters on lips or around the mouth
</
th
>
<
td
class
=
"nhsuk-table__cell"
>
Cold sores
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Itchy, dry, cracked, sore
</
th
>
<
td
class
=
"nhsuk-table__cell"
>
Eczema
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
th
class
=
"nhsuk-table__header"
scope
=
"row"
>
Itchy blisters
</
th
>
<
td
class
=
"nhsuk-table__cell"
>
Shingles, chickenpox
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the table.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. Array of table rows and cells. See macro options for rows .
Name head | Type array | Description Array of table head cells. See macro options for head .
Name caption | Type object | Description Table caption. See macro options for caption .
Name caption Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.classes option.
Name caption Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the caption.size option.
Name first Cell Is Header | Type boolean | Description If set to true , first cell in table row will be a th instead of a td .
Name compact | Type boolean | Description If set to true , vertical padding will be reduced for table cells.
Name responsive | Type boolean | Description If set to true , responsive table classes will be applied.
Name scroll | Type boolean | Description If set to true , wrap a scrolling container around the table component. Scrolling tables require the caption.text and caption.id options.
Name striped | Type boolean | Description If set to true , striped background colours will be applied to table rows.
Name variant | Type string | Description Optional variant of table. You can use only "reverse" or empty values with this option.
Name card | Type object | Description Can be used to wrap a card around the table component. If any of these options are present, a card will wrap around the table. See macro options for card .
Name panel | Type boolean | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card option.
Name panel Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.classes option.
Name heading | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.text option.
Name heading Level | Type integer | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the card.heading.level option.
Name classes | Type string | Description Classes to add to the table container.
Name table Classes | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the classes option.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table container.
Name ascending Text | Type string | Description Text for columns in ascending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "ascending" .
Name descending Text | Type string | Description Text for columns in descending sort order, used to populate the %{direction} placeholder in sortAnnouncementText . Defaults to "descending" .
Name sort Announcement Text | Type string | Description Announcement made to screen reader users when a table column has been sorted. The component will replace the %{header} placeholder with the column header, and the %{direction} placeholder with the ascendingText or descendingText option value.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text for cells in table rows. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for cells in table rows. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table cell.
Name header | Type string | Description Deprecated in 10.6.0 (see GitHub) . Set automatically by table head cells in the head option.
Name href | Type string | Description If set, the table cell will become a link.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name sort Value | Type string | Description Sort value text for cells in table rows.
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table cell.

Name | Type | Description
Name text | Type string | Description If html is set, this is not required. Text for table head cells. If html is provided, the text option will be ignored.
Name html | Type string | Description If text is set, this is not required. HTML for table head cells. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the table head cell.
Name href | Type string | Description If set, the table header will become a link for server-side table sorting. Use sort to set the column sort direction.
Name format | Type string | Description Specify format of a cell – "numeric" or "string" . Defaults to "string"
Name colspan | Type integer | Description Specify how many columns a cell spans.
Name rowspan | Type integer | Description Specify how many rows a cell spans.
Name align | Type string | Description Specify the table head cell alignment – "left" , "centre" , or "right" . Defaults to "left"
Name width | Type string | Description Specify the table head cell width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the table head cell.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table head cell.
Name sort | Type string | Description The sort direction applied to the column using aria-sort – "ascending" , "descending" , "none" or true . To enable sorting without a default direction, set sort to "none" or true .
Name sort Next | Type string | Description The next sort direction applied to the column using aria-sort when clicked – "ascending" or "descending" . Defaults to "ascending" . If you set sort to "ascending" , sortNext defaults to "descending" .

Name | Type | Description
Name id | Type string | Description The ID of the table caption and the aria-labelledby attribute in the scrolling container. Defaults to the table id option suffixed with "-caption" . If neither are provided, the ID is generated from the caption text option.
Name text | Type string | Description Required. If html is set, this is not required. Text for the table caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the table caption. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Message made available to assistive technologies to describe that the table is sortable. Defaults to "Column headers are sortable" .
Name caption | Type object | Description Optional caption for the table caption. See macro options for caption .
Name size | Type string | Description Size of the table caption – "s" , "m" , "l" or "xl" .
Name classes | Type string | Description Classes to add to the table caption, for example "nhsuk-table__caption--l" .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the table caption.

Name | Type | Description
Name id | Type string | Description The ID of the caption.
Name element | Type string | Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" .
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block.
Name placement | Type string | Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" .
Name size | Type string | Description Size of the caption – "m" , "l" , "xl" or "xxl" .
Name classes | Type string | Description Classes to add to the caption.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the caption.

```text
{%
from
"tables/macro.njk"
import
table
%}
{{
table
({
caption
:
"Skin symptoms and possible causes"
,
firstCellIsHeader
:
true
,
variant
:
"reverse"
,
head
: [
    {
text
:
"Skin symptoms"
},
    {
text
:
"Possible cause"
}
  ],
rows
: [
    [
      {
text
:
"Blisters on lips or around the mouth"
},
      {
text
:
"Cold sores"
}
    ],
    [
      {
text
:
"Itchy, dry, cracked, sore"
},
      {
text
:
"Eczema"
}
    ],
    [
      {
text
:
"Itchy blisters"
},
      {
text
:
"Shingles, chickenpox"
}
    ]
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## Accessibility

Follow WebAIM's guidance for tables and:

- give tables captions

- use the scope attribute to associate the data cells with the appropriate headers

- let the browser window determine the width of the table whenever possible, to reduce horizontal scrolling

### Table captions

Use the <caption> element to describe a table in the same way you would use a heading. A caption helps users find, navigate and understand tables.

Style table captions to match the visual hierarchy of your page's content.

If you're using Nunjucks, add the size: "l" option to the caption. For HTML add the nhsuk-table__caption--l class to the caption.

You can use sizes s , m , l , xl .

### Table headers

Use table headers to tell users what the rows and columns represent.

### Sortable tables

The sortable table tells screen reader users that it can be sorted. When the user sorts the table, it announces what the new sort order is.

## Research

### Basic table

This table tested well with users of health information on the NHS website.

### Responsive table

This table was tested at HM Revenue & Customs.

### Sortable table

This table was developed by NHS England and tested in the Run breast screening in England and Manage vaccinations in schools services.

There is an overlap between sortable tables and:

- search

- filter

- pagination

We want to understand better how they can work together.

We have not yet developed a responsive or scrolling sortable table. If you need a responsive sorting table, you could try adding a select component .

Please feed back if you develop any of these or implement server-side sorting.

### Table in a card

We have also included an example of a table in a card in the NHS.UK frontend (in GitHub) . We have not published it in this list of components yet because it needs more testing.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: August 2026
