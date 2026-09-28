# Expander – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/expander/

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

# Content presentation – Expander

Make a complex topic easier to digest by letting users reveal more detailed information only if they need it.

- HTML code for expander

- Nunjucks code for expander

```text
<
details
class
=
"nhsuk-details nhsuk-expander"
>
<
summary
class
=
"nhsuk-details__summary"
>
<
span
class
=
"nhsuk-details__summary-text"
>
Get your medical records
</
span
>
</
summary
>
<
div
class
=
"nhsuk-details__text"
>
<
p
>
You can see your GP records by:
</
p
>
<
ul
>
<
li
>
asking for them at your GP surgery
</
li
>
<
li
>
going online to see them (if you have signed up for
<
a
href
=
"/using-the-nhs/nhs-services/gps/gp-online-services/"
>
GP online services
</
a
>
)
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
details
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name summary | Type object | Description Summary element content (the visible part of the details element). See macro options for summary .
Name summary Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the summary.text option.
Name summary Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the summary.html option.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the disclosed part of the details element. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the disclosed part of the details element. If html is provided, the text option will be ignored.
Name id | Type string | Description The id to add to the details element.
Name open | Type boolean | Description If true , details element will be expanded.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire details component in a call block.
Name variant | Type string | Description Optional variant of details. You can use only "reverse" or empty values with this option.
Name classes | Type string | Description Classes to add to the details element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the details element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the summary element (the visible part of the details element). If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the summary element (the visible part of the details element). If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the summary element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the summary element.

```text
{%
from
"details/macro.njk"
import
details
%}
{%
call
details
({
summary
:
"Get your medical records"
,
classes
:
"nhsuk-expander"
}) %}
<
p
>
You can see your GP records by:
</
p
>
<
ul
>
<
li
>
asking for them at your GP surgery
</
li
>
<
li
>
going online to see them (if you have signed up for
<
a
href
=
"/using-the-nhs/nhs-services/gps/gp-online-services/"
>
GP online services
</
a
>
)
</
li
>
</
ul
>
{%
endcall
%}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## When to use expanders

There are 2 ways to let users reveal more information:

- details

- expander

Use expanders:

- on pages where users find the amount of information overwhelming – they break down information into bite size pieces which the user can "expand", when they're ready to do so

- for information for a wide audience, unlike the details component

- when you see a clear user need for them

Test your content without an expander first. It may be better to:

- simplify and reduce the amount of content

- split the content across multiple pages

- keep the content on a single page, separated by headings

- use a list of links to let users navigate quickly to specific sections of content

## When not to use an expander

Do not use an expander:

- if only some of your users will need the information – use details instead

- to give users help in forms – instead, add hint text as a part of other form inputs, such as text inputs , radios and checkboxes or use details

- on pages with other interactive elements, such as buttons or text input – there's a risk that expanders will distract users

- inside other patterns, for example to help users decide when and where to get care (care cards)

## How expanders work

The expander is a short link in a box that expands into more detailed text when a user clicks on it.

### More than 1 expander

It can work well to have several expanders. See the example below.

- HTML code for expander group

- Nunjucks code for expander group

```text
<
div
class
=
"nhsuk-expander-group"
>
<
details
class
=
"nhsuk-details nhsuk-expander"
>
<
summary
class
=
"nhsuk-details__summary"
>
<
span
class
=
"nhsuk-details__summary-text"
>
How to measure your blood glucose levels
</
span
>
</
summary
>
<
div
class
=
"nhsuk-details__text"
>
<
p
>
Testing your blood at home is quick and easy, although it can be uncomfortable. It does get better.
</
p
>
<
p
>
You would have been given:
</
p
>
<
ul
>
<
li
>
a blood glucose metre
</
li
>
<
li
>
small needles called lancets
</
li
>
<
li
>
a plastic pen to hold the lancets
</
li
>
<
li
>
small test strips
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
details
>
<
details
class
=
"nhsuk-details nhsuk-expander"
>
<
summary
class
=
"nhsuk-details__summary"
>
<
span
class
=
"nhsuk-details__summary-text"
>
When to check your blood glucose level
</
span
>
</
summary
>
<
div
class
=
"nhsuk-details__text"
>
<
p
>
Try to check your blood:
</
p
>
<
ul
>
<
li
>
before meals
</
li
>
<
li
>
2 to 3 hours after meals
</
li
>
<
li
>
before, during (take a break) and after exercise
</
li
>
</
ul
>
<
p
>
This helps you understand your blood glucose levels and how they're affected by meals and exercise. It should help you have more stable blood glucose levels.
</
p
>
</
div
>
</
details
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
Name summary | Type object | Description Summary element content (the visible part of the details element). See macro options for summary .
Name summary Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the summary.text option.
Name summary Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the summary.html option.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the disclosed part of the details element. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the disclosed part of the details element. If html is provided, the text option will be ignored.
Name id | Type string | Description The id to add to the details element.
Name open | Type boolean | Description If true , details element will be expanded.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire details component in a call block.
Name variant | Type string | Description Optional variant of details. You can use only "reverse" or empty values with this option.
Name classes | Type string | Description Classes to add to the details element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the details element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the summary element (the visible part of the details element). If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the summary element (the visible part of the details element). If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the summary element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the summary element.

```text
{%
from
"details/macro.njk"
import
details
%}
<
div
class
=
"nhsuk-expander-group"
>
{%
call
details
({
summary
:
"How to measure your blood glucose levels"
,
classes
:
"nhsuk-expander"
}) %}
<
p
>
Testing your blood at home is quick and easy, although it can be uncomfortable. It does get better.
</
p
>
<
p
>
You would have been given:
</
p
>
<
ul
>
<
li
>
a blood glucose metre
</
li
>
<
li
>
small needles called lancets
</
li
>
<
li
>
a plastic pen to hold the lancets
</
li
>
<
li
>
small test strips
</
li
>
</
ul
>
{%
endcall
%}
{%
call
details
({
summary
:
"When to check your blood glucose level"
,
classes
:
"nhsuk-expander"
}) %}
<
p
>
Try to check your blood:
</
p
>
<
ul
>
<
li
>
before meals
</
li
>
<
li
>
2 to 3 hours after meals
</
li
>
<
li
>
before, during (take a break) and after exercise
</
li
>
</
ul
>
<
p
>
This helps you understand your blood glucose levels and how they're affected by meals and exercise. It should help you have more stable blood glucose levels.
</
p
>
{%
endcall
%}
</
div
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Write clear link text

Make the link text short and descriptive so users can quickly work out if they need to click on it.

## Research

We tested several expanders in our information about type 1 diabetes where users felt overwhelmed by the amount of information. They tested well and seemed to meet users' emotional needs. We've also tested them on other pages about health and medicines.

If you've used this component, get in touch to share your user research findings .

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: August 2025
