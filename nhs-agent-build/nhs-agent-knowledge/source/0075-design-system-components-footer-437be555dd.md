# Footer – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/footer/

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

# Navigation – Footer

Use the footer to show users they are on an NHS service and to help them find links they expect at the bottom of our pages.

- HTML code for footer

- Nunjucks code for footer

```text
<
footer
class
=
"nhsuk-footer"
role
=
"contentinfo"
>
<
div
class
=
"nhsuk-width-container"
>
<
div
class
=
"nhsuk-footer__meta"
>
<
h2
class
=
"nhsuk-u-visually-hidden"
>
Support links
</
h2
>
<
ul
class
=
"nhsuk-footer__list"
>
<
li
class
=
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Accessibility statement
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Contact us
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Cookies
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Privacy policy
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Terms and conditions
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
p
class
=
"nhsuk-body-s"
>
© NHS England
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
footer
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the footer.
Name columns | Type integer | Description Number of columns to display per row in the navigation section of the footer – 4 , 3 , 2 or 1 . Defaults to 4 .
Name navigation | Type object | Description The navigation section of the footer before the copyright information. Alternatively supports an array of navigation objects. See macro options for navigation .
Name meta | Type object | Description The meta section of the footer after any navigation, before the copyright information. See macro options for meta .
Name copyright | Type object | Description The copyright information in the footer component, this defaults to "© NHS England" . See macro options for copyright .
Name container Classes | Type string | Description Classes to add to the footer container, useful if you want to make the footer fixed width.
Name classes | Type string | Description Classes to add to the footer container.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire footer component in a call block.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the footer container.

Name | Type | Description
Name heading | Type object | Description Heading for group of footer navigation links. See macro options for navigation heading .
Name title | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the navigation.heading.text option.
Name text | Type string | Description Optional text to use within each navigation section column. If html is provided, the text option will be ignored.
Name html | Type string | Description Optional HTML to use within each navigation section column. If html is provided, the text option will be ignored.
Name width | Type string | Description Width of each navigation section column in the footer. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Defaults to "one-quarter" .
Name items | Type array | Description Contains the array of footer navigation link items for this group. See macro options for navigation items .

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the heading.
Name href | Type string | Description If set, the heading will become a link.
Name caption | Type object | Description Optional caption for the heading. See macro options for caption .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name href | Type string | Description Required. Footer navigation link href attribute.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each footer navigation link. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each footer navigation link. If html is provided, the text option will be ignored.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the footer navigation link.

Name | Type | Description
Name visually Hidden Text | Type string | Description Visually hidden heading for meta items links. Defaults to "Support links" .
Name visually Hidden Title | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the meta.visuallyHiddenText option.
Name html | Type string | Description HTML to add to the meta section of the footer, which will appear below any links specified using meta items .
Name text | Type string | Description Text to add to the meta section of the footer, which will appear below any links specified using meta items . If meta html is specified, this option is ignored.
Name items | Type array | Description Contains the array of key policy footer link items. See macro options for meta items .

Name | Type | Description
Name href | Type string | Description Required. Footer meta link href attribute.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each footer meta link. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each footer meta link. If html is provided, the text option will be ignored.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the footer meta link.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. If html is provided, the text option will be ignored. If neither are provided, "© NHS England" is used.
Name html | Type string | Description Required. If text is set, this is not required. If html is provided, the text option will be ignored. If neither are provided, "© NHS England" is used.

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
"footer/macro.njk"
import
footer
%}
{{
footer
({
meta
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
"Accessibility statement"
},
      {
href
:
"#"
,
text
:
"Contact us"
},
      {
href
:
"#"
,
text
:
"Cookies"
},
      {
href
:
"#"
,
text
:
"Privacy policy"
},
      {
href
:
"#"
,
text
:
"Terms and conditions"
}
    ]
  }
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## When to use the footer

Use the footer at the bottom of every page of your website or service but not on a mobile app.

## How to use the footer

### Footer with key links only

- HTML code for footer second

- Nunjucks code for footer second

```text
<
footer
class
=
"nhsuk-footer"
role
=
"contentinfo"
>
<
div
class
=
"nhsuk-width-container"
>
<
div
class
=
"nhsuk-footer__meta"
>
<
h2
class
=
"nhsuk-u-visually-hidden"
>
Support links
</
h2
>
<
ul
class
=
"nhsuk-footer__list"
>
<
li
class
=
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Accessibility statement
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Contact us
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Cookies
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Privacy policy
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Terms and conditions
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
p
class
=
"nhsuk-body-s"
>
© NHS England
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
footer
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the footer.
Name columns | Type integer | Description Number of columns to display per row in the navigation section of the footer – 4 , 3 , 2 or 1 . Defaults to 4 .
Name navigation | Type object | Description The navigation section of the footer before the copyright information. Alternatively supports an array of navigation objects. See macro options for navigation .
Name meta | Type object | Description The meta section of the footer after any navigation, before the copyright information. See macro options for meta .
Name copyright | Type object | Description The copyright information in the footer component, this defaults to "© NHS England" . See macro options for copyright .
Name container Classes | Type string | Description Classes to add to the footer container, useful if you want to make the footer fixed width.
Name classes | Type string | Description Classes to add to the footer container.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire footer component in a call block.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the footer container.

Name | Type | Description
Name heading | Type object | Description Heading for group of footer navigation links. See macro options for navigation heading .
Name title | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the navigation.heading.text option.
Name text | Type string | Description Optional text to use within each navigation section column. If html is provided, the text option will be ignored.
Name html | Type string | Description Optional HTML to use within each navigation section column. If html is provided, the text option will be ignored.
Name width | Type string | Description Width of each navigation section column in the footer. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Defaults to "one-quarter" .
Name items | Type array | Description Contains the array of footer navigation link items for this group. See macro options for navigation items .

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the heading.
Name href | Type string | Description If set, the heading will become a link.
Name caption | Type object | Description Optional caption for the heading. See macro options for caption .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name href | Type string | Description Required. Footer navigation link href attribute.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each footer navigation link. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each footer navigation link. If html is provided, the text option will be ignored.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the footer navigation link.

Name | Type | Description
Name visually Hidden Text | Type string | Description Visually hidden heading for meta items links. Defaults to "Support links" .
Name visually Hidden Title | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the meta.visuallyHiddenText option.
Name html | Type string | Description HTML to add to the meta section of the footer, which will appear below any links specified using meta items .
Name text | Type string | Description Text to add to the meta section of the footer, which will appear below any links specified using meta items . If meta html is specified, this option is ignored.
Name items | Type array | Description Contains the array of key policy footer link items. See macro options for meta items .

Name | Type | Description
Name href | Type string | Description Required. Footer meta link href attribute.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each footer meta link. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each footer meta link. If html is provided, the text option will be ignored.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the footer meta link.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. If html is provided, the text option will be ignored. If neither are provided, "© NHS England" is used.
Name html | Type string | Description Required. If text is set, this is not required. If html is provided, the text option will be ignored. If neither are provided, "© NHS England" is used.

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
"footer/macro.njk"
import
footer
%}
{{
footer
({
meta
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
"Accessibility statement"
},
      {
href
:
"#"
,
text
:
"Contact us"
},
      {
href
:
"#"
,
text
:
"Cookies"
},
      {
href
:
"#"
,
text
:
"Privacy policy"
},
      {
href
:
"#"
,
text
:
"Terms and conditions"
}
    ]
  }
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Add links to policies and other meta information about your service, such as: accessibility contact details cookies privacy policy terms and conditions Keep links to a minimum, especially in a transactional journey. Too many links can distract users. Link to specific policies for the transaction, if appropriate. If your total number of links is less than 7, arrange them horizontally in lines. If you include links to "help" pages in a footer, make sure to place those links consistently in the footer content. Also make sure that "help" links always work in a similar way across each page. Footer with navigation links If your users need lots of footer links to help them navigate a complex information architecture, include navigation links and arrange the links in columns. The navigation links give users another route to the most visited content on the site. They act as a safety net for users who have not found content through the main navigation. There is a line below the columns to separate them from the meta information, for example the copyright notice. Open this example in a new tab : footer columns HTML code for footer columns Nunjucks code for footer columns HTML code for footer columns Copy code < footer class = "nhsuk-footer" role = "contentinfo" > < div class = "nhsuk-width-container" > < div class = "nhsuk-footer__navigation nhsuk-grid-row" > < div class = "nhsuk-grid-column-one-quarter" > < ul class = "nhsuk-footer__list" > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Home </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Health A to Z </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > NHS services </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Live Well </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Mental health </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Care and support </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Accessibility statement </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Pregnancy </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > COVID-19 </ a > </ li > </ ul > </ div > < div class = "nhsuk-grid-column-one-quarter" > < ul class = "nhsuk-footer__list" > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > NHS App </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Find my NHS number </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > View your GP health records </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > View your test results </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > About the NHS </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Healthcare abroad </ a > </ li > </ ul > </ div > < div class = "nhsuk-grid-column-one-quarter" > < ul class = "nhsuk-footer__list" > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Other NHS websites </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Profile editor login </ a > </ li > </ ul > </ div > < div class = "nhsuk-grid-column-one-quarter" > < ul class = "nhsuk-footer__list" > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > About us </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Give us feedback </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Accessibility statement </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Our policies </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Cookies </ a > </ li > </ ul > </ div > </ div > < div class = "nhsuk-footer__meta" > < p class = "nhsuk-body-s" > © Crown copyright </ p > </ div > </ div > </ footer > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : footer columns Nunjucks code for footer columns Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the footer. Name columns Type integer Description Number of columns to display per row in the navigation section of the footer – 4 , 3 , 2 or 1 . Defaults to 4 . Name navigation Type object Description The navigation section of the footer before the copyright information. Alternatively supports an array of navigation objects. See macro options for navigation . Name meta Type object Description The meta section of the footer after any navigation, before the copyright information. See macro options for meta . Name copyright Type object Description The copyright information in the footer component, this defaults to "© NHS England" . See macro options for copyright . Name container Classes Type string Description Classes to add to the footer container, useful if you want to make the footer fixed width. Name classes Type string Description Classes to add to the footer container. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire footer component in a call block. Name attributes Type object Description HTML attributes (for example data attributes) to add to the footer container. Options for navigation object Name Type Description Name heading Type object Description Heading for group of footer navigation links. See macro options for navigation heading . Name title Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the navigation.heading.text option. Name text Type string Description Optional text to use within each navigation section column. If html is provided, the text option will be ignored. Name html Type string Description Optional HTML to use within each navigation section column. If html is provided, the text option will be ignored. Name width Type string Description Width of each navigation section column in the footer. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Defaults to "one-quarter" . Name items Type array Description Contains the array of footer navigation link items for this group. See macro options for navigation items . Options for navigation heading component Name Type Description Name id Type string Description The ID of the heading. Name text Type string Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the heading. Name href Type string Description If set, the heading will become a link. Name caption Type object Description Optional caption for the heading. See macro options for caption . Name classes Type string Description Classes to add to the heading. Name attributes Type object Description HTML attributes (for example data attributes) to add to the heading. Options for navigation items array objects Name Type Description Name href Type string Description Required. Footer navigation link href attribute. Name text Type string Description Required. If html is set, this is not required. Text to use within each footer navigation link. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within each footer navigation link. If html is provided, the text option will be ignored. Name attributes Type object Description HTML attributes (for example data attributes) to add to the footer navigation link. Options for meta object Name Type Description Name visually Hidden Text Type string Description Visually hidden heading for meta items links. Defaults to "Support links" . Name visually Hidden Title Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the meta.visuallyHiddenText option. Name html Type string Description HTML to add to the meta section of the footer, which will appear below any links specified using meta items . Name text Type string Description Text to add to the meta section of the footer, which will appear below any links specified using meta items . If meta html is specified, this option is ignored. Name items Type array Description Contains the array of key policy footer link items. See macro options for meta items . Options for meta items array objects Name Type Description Name href Type string Description Required. Footer meta link href attribute. Name text Type string Description Required. If html is set, this is not required. Text to use within each footer meta link. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within each footer meta link. If html is provided, the text option will be ignored. Name attributes Type object Description HTML attributes (for example data attributes) to add to the footer meta link. Options for copyright object Name Type Description Name text Type string Description Required. If html is set, this is not required. If html is provided, the text option will be ignored. If neither are provided, "© NHS England" is used. Name html Type string Description Required. If text is set, this is not required. If html is provided, the text option will be ignored. If neither are provided, "© NHS England" is used. Options for caption component Name Type Description Name id Type string Description The ID of the caption. Name element Type string Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" . Name text Type string Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block. Name placement Type string Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" . Name size Type string Description Size of the caption – "m" , "l" , "xl" or "xxl" . Name classes Type string Description Classes to add to the caption. Name attributes Type object Description HTML attributes (for example data attributes) to add to the caption. Copy code {% from "footer/macro.njk" import footer %} {{ footer ({ copyright : { text : "© Crown copyright" }, navigation : [ { items : [ { href : "#" , text : "Home" }, { href : "#" , text : "Health A to Z" }, { href : "#" , text : "NHS services" }, { href : "#" , text : "Live Well" }, { href : "#" , text : "Mental health" }, { href : "#" , text : "Care and support" }, { href : "#" , text : "Accessibility statement" }, { href : "#" , text : "Pregnancy" }, { href : "#" , text : "COVID-19" } ] }, { items : [ { href : "#" , text : "NHS App" }, { href : "#" , text : "Find my NHS number" }, { href : "#" , text : "View your GP health records" }, { href : "#" , text : "View your test results" }, { href : "#" , text : "About the NHS" }, { href : "#" , text : "Healthcare abroad" } ] }, { items : [ { href : "#" , text : "Other NHS websites" }, { href : "#" , text : "Profile editor login" } ] }, { items : [ { href : "#" , text : "About us" }, { href : "#" , text : "Give us feedback" }, { href : "#" , text : "Accessibility statement" }, { href : "#" , text : "Our policies" }, { href : "#" , text : "Cookies" } ] } ] }) }} Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : footer columns Copyright Your copyright statement must reflect the ownership of your website or service. The NHS website is (c) Crown copyright but the NHS generally does not have Crown status. The service manual footer, for example, says (c) NHS England. Include a reference to the Open Government Licence if your organisation or service encourages people to reuse and adapt its information under the licence. Contact your legal team for advice. Help us improve this guidance Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public. Feed back or share insights on GitHub Read more about how to feed back or share insights . If you have any questions, get in touch with the service manual team. Updates to this page Updated: June 2026

- accessibility

- contact details

- cookies

- privacy policy

- terms and conditions

Keep links to a minimum, especially in a transactional journey. Too many links can distract users. Link to specific policies for the transaction, if appropriate.

If your total number of links is less than 7, arrange them horizontally in lines.

If you include links to "help" pages in a footer, make sure to place those links consistently in the footer content. Also make sure that "help" links always work in a similar way across each page.

### Footer with navigation links

If your users need lots of footer links to help them navigate a complex information architecture, include navigation links and arrange the links in columns.

The navigation links give users another route to the most visited content on the site. They act as a safety net for users who have not found content through the main navigation.

There is a line below the columns to separate them from the meta information, for example the copyright notice.

- HTML code for footer columns

- Nunjucks code for footer columns

```text
<
footer
class
=
"nhsuk-footer"
role
=
"contentinfo"
>
<
div
class
=
"nhsuk-width-container"
>
<
div
class
=
"nhsuk-footer__navigation nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-one-quarter"
>
<
ul
class
=
"nhsuk-footer__list"
>
<
li
class
=
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
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
<
li
class
=
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
NHS services
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Live Well
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Mental health
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Care and support
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Accessibility statement
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Pregnancy
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
COVID-19
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
div
>
<
div
class
=
"nhsuk-grid-column-one-quarter"
>
<
ul
class
=
"nhsuk-footer__list"
>
<
li
class
=
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
NHS App
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Find my NHS number
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
View your GP health records
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
View your test results
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
About the NHS
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Healthcare abroad
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
div
>
<
div
class
=
"nhsuk-grid-column-one-quarter"
>
<
ul
class
=
"nhsuk-footer__list"
>
<
li
class
=
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Other NHS websites
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Profile editor login
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
div
>
<
div
class
=
"nhsuk-grid-column-one-quarter"
>
<
ul
class
=
"nhsuk-footer__list"
>
<
li
class
=
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
About us
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Give us feedback
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Accessibility statement
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Our policies
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Cookies
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
div
>
</
div
>
<
div
class
=
"nhsuk-footer__meta"
>
<
p
class
=
"nhsuk-body-s"
>
© Crown copyright
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
footer
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the footer.
Name columns | Type integer | Description Number of columns to display per row in the navigation section of the footer – 4 , 3 , 2 or 1 . Defaults to 4 .
Name navigation | Type object | Description The navigation section of the footer before the copyright information. Alternatively supports an array of navigation objects. See macro options for navigation .
Name meta | Type object | Description The meta section of the footer after any navigation, before the copyright information. See macro options for meta .
Name copyright | Type object | Description The copyright information in the footer component, this defaults to "© NHS England" . See macro options for copyright .
Name container Classes | Type string | Description Classes to add to the footer container, useful if you want to make the footer fixed width.
Name classes | Type string | Description Classes to add to the footer container.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire footer component in a call block.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the footer container.

Name | Type | Description
Name heading | Type object | Description Heading for group of footer navigation links. See macro options for navigation heading .
Name title | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the navigation.heading.text option.
Name text | Type string | Description Optional text to use within each navigation section column. If html is provided, the text option will be ignored.
Name html | Type string | Description Optional HTML to use within each navigation section column. If html is provided, the text option will be ignored.
Name width | Type string | Description Width of each navigation section column in the footer. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Defaults to "one-quarter" .
Name items | Type array | Description Contains the array of footer navigation link items for this group. See macro options for navigation items .

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the heading.
Name href | Type string | Description If set, the heading will become a link.
Name caption | Type object | Description Optional caption for the heading. See macro options for caption .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name href | Type string | Description Required. Footer navigation link href attribute.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each footer navigation link. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each footer navigation link. If html is provided, the text option will be ignored.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the footer navigation link.

Name | Type | Description
Name visually Hidden Text | Type string | Description Visually hidden heading for meta items links. Defaults to "Support links" .
Name visually Hidden Title | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the meta.visuallyHiddenText option.
Name html | Type string | Description HTML to add to the meta section of the footer, which will appear below any links specified using meta items .
Name text | Type string | Description Text to add to the meta section of the footer, which will appear below any links specified using meta items . If meta html is specified, this option is ignored.
Name items | Type array | Description Contains the array of key policy footer link items. See macro options for meta items .

Name | Type | Description
Name href | Type string | Description Required. Footer meta link href attribute.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each footer meta link. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each footer meta link. If html is provided, the text option will be ignored.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the footer meta link.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. If html is provided, the text option will be ignored. If neither are provided, "© NHS England" is used.
Name html | Type string | Description Required. If text is set, this is not required. If html is provided, the text option will be ignored. If neither are provided, "© NHS England" is used.

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
"footer/macro.njk"
import
footer
%}
{{
footer
({
copyright
: {
text
:
"© Crown copyright"
},
navigation
: [
    {
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
},
        {
href
:
"#"
,
text
:
"NHS services"
},
        {
href
:
"#"
,
text
:
"Live Well"
},
        {
href
:
"#"
,
text
:
"Mental health"
},
        {
href
:
"#"
,
text
:
"Care and support"
},
        {
href
:
"#"
,
text
:
"Accessibility statement"
},
        {
href
:
"#"
,
text
:
"Pregnancy"
},
        {
href
:
"#"
,
text
:
"COVID-19"
}
      ]
    },
    {
items
: [
        {
href
:
"#"
,
text
:
"NHS App"
},
        {
href
:
"#"
,
text
:
"Find my NHS number"
},
        {
href
:
"#"
,
text
:
"View your GP health records"
},
        {
href
:
"#"
,
text
:
"View your test results"
},
        {
href
:
"#"
,
text
:
"About the NHS"
},
        {
href
:
"#"
,
text
:
"Healthcare abroad"
}
      ]
    },
    {
items
: [
        {
href
:
"#"
,
text
:
"Other NHS websites"
},
        {
href
:
"#"
,
text
:
"Profile editor login"
}
      ]
    },
    {
items
: [
        {
href
:
"#"
,
text
:
"About us"
},
        {
href
:
"#"
,
text
:
"Give us feedback"
},
        {
href
:
"#"
,
text
:
"Accessibility statement"
},
        {
href
:
"#"
,
text
:
"Our policies"
},
        {
href
:
"#"
,
text
:
"Cookies"
}
      ]
    }
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Copyright

Your copyright statement must reflect the ownership of your website or service. The NHS website is (c) Crown copyright but the NHS generally does not have Crown status. The service manual footer, for example, says (c) NHS England.

Include a reference to the Open Government Licence if your organisation or service encourages people to reuse and adapt its information under the licence.

Contact your legal team for advice.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
