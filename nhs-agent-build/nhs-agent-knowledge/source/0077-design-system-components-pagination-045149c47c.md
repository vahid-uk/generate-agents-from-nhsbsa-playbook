# Pagination – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/pagination/

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

# Navigation – Pagination

Use pagination to help users navigate forwards and backwards through a series of pages.

- HTML code for pagination numbered

- Nunjucks code for pagination numbered

```text
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
a
href
=
"#"
class
=
"nhsuk-pagination__previous"
rel
=
"prev"
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
</
a
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
"Page 1"
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
"nhsuk-pagination__item nhsuk-pagination__item--ellipsis"
>
&ctdot;
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
"Page 8"
>
8
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
"Page 9"
>
9
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
"Page 10"
aria-current
=
"page"
>
10
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
"Page 11"
>
11
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
"Page 12"
>
12
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
"nhsuk-pagination__item nhsuk-pagination__item--ellipsis"
>
&ctdot;
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
"Page 42"
>
42
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
href
:
"#"
},
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
},
    {
ellipsis
:
true
},
    {
number
:
8
,
href
:
"#"
},
    {
number
:
9
,
href
:
"#"
},
    {
number
:
10
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
11
,
href
:
"#"
},
    {
number
:
12
,
href
:
"#"
},
    {
ellipsis
:
true
},
    {
number
:
42
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

## When to use pagination

Use pagination at the bottom of the page to help users navigate forwards and backwards through a series of related pages. For example, pages of search results or information about a health condition that's divided into multiple web pages.

Consider using pagination when:

- showing all the content on a single page makes the page take too long to load or read

- most users only need the content on the 1st page or 1st few pages

Use pagination rather than the "infinite scroll" technique which automatically loads content when the user approaches the bottom of the page. This causes problems for keyboard users.

## When not to use pagination

Only break up content onto separate pages if it improves the performance or usability of your service.

Do not use pagination on pages which are not grouped together or "related" as this is likely to confuse users.

Do not use pagination to navigate through a multi-page form. We use other components instead, including:

- buttons (usually a "Continue" button) to move forward back link to navigate back

- back link to navigate back

## How to use pagination

Add the pagination component after the content on each page that you're paginating.

Do not show pagination if there's only 1 page of content.

Redirect users to the 1st page if they enter a URL of a page that no longer exists.

### For navigating between content pages

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

Use pagination at the bottom of pages of content to allow users to navigate around a topic that's divided into multiple pages (up to 8 pages).

If you're using pagination at the bottom of content pages, you should also use a contents list at the top of the page. The 2 components make up the mini-hub pattern .

Use the word "Previous" with an arrow left and a link to the previous page and the word "Next" with an arrow right and a link to the next page. Use the same page titles as in the contents list.

### For navigating between pages of items

Use numbered pagination if users need to navigate through pages of similar items. For example, a list of search results or a list of cases in a case working system.

Decide the maximum number of items to show on each page based on the context of your service and the amount of content for each item.

- HTML code for pagination numbered second

- Nunjucks code for pagination numbered second

```text
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
a
href
=
"#"
class
=
"nhsuk-pagination__previous"
rel
=
"prev"
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
</
a
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
"Page 1"
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
"nhsuk-pagination__item nhsuk-pagination__item--ellipsis"
>
&ctdot;
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
"Page 8"
>
8
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
"Page 9"
>
9
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
"Page 10"
aria-current
=
"page"
>
10
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
"Page 11"
>
11
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
"Page 12"
>
12
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
"nhsuk-pagination__item nhsuk-pagination__item--ellipsis"
>
&ctdot;
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
"Page 42"
>
42
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
href
:
"#"
},
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
},
    {
ellipsis
:
true
},
    {
number
:
8
,
href
:
"#"
},
    {
number
:
9
,
href
:
"#"
},
    {
number
:
10
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
11
,
href
:
"#"
},
    {
number
:
12
,
href
:
"#"
},
    {
ellipsis
:
true
},
    {
number
:
42
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

Show the page number in the page <title> so that screen reader users know they've navigated to a different page. For example, "Search results (page 1 of 4)".

The pagination should always show the page numbers for:

- the current page

- the page before the current page

- the page after the current page

- 1st and last pages

For larger screens, you can show the page numbers for 2 or more pages before and after the current page.

Use ellipses (…) to show gaps in the page numbering. For example:

- [1] 2 … 100

- 1 [2] 3 … 100

- 1 2 [3] 4 … 100

- 1 2 3 [4] 5 … 100

- 1 … 4 [5] 6 … 100

- 1 … 97 [98] 99 100

- 1 … 98 [99] 100

- 1 … 99 [100]

#### 1st and last pages

Do not show the previous page link on the 1st page and do not show the next page link on the last page.

- HTML code for pagination numbered first page

- Nunjucks code for pagination numbered first page

```text
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
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

- HTML code for pagination numbered last page

- Nunjucks code for pagination numbered last page

```text
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
a
href
=
"#"
class
=
"nhsuk-pagination__previous"
rel
=
"prev"
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
</
a
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
"Page 1"
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
"Page 3"
aria-current
=
"page"
>
3
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
,
current
:
true
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Accessibility

The pagination components are surrounded by a <nav> element to show that they are navigation links. This element has an aria-label attribute with the value Pagination . Screen readers that support this attribute will read this.

There is also a visually hidden heading title pagination which will be read by screen readers as a heading to the links.

If the link describes the current page that you are on, then it has the aria-current="page" value to indicate to screen readers that this is the case.

## Research

### Content page navigation

We tested content page pagination in grouped information pages in 3 labs in 2018. We have not tested it in forms.

4 out of 5 users, including a user with a very low level of digital skill, used pagination to navigate through the pages. They understood that it was associated with the navigation at the top of the page.

Users found that the pagination reflected the way they read content and their mental model of the structure of the content.

### Numbered page navigation

GOV.UK based their component for navigating between pages of items on similar ones developed and used successfully by the Government Digital Service, Ministry of Justice and the Home Office.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
