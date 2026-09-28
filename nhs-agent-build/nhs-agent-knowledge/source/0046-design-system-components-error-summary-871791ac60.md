# Error summary – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/error-summary/

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

# Form elements – Error summary

Include an error summary at the top of a page to summarise any mistakes a user has made.

- HTML code for error summary

- Nunjucks code for error summary

```text
<
div
class
=
"nhsuk-error-summary"
data-module
=
"nhsuk-error-summary"
>
<
div
role
=
"alert"
>
<
h2
class
=
"nhsuk-error-summary__heading"
>
There is a problem
</
h2
>
<
div
class
=
"nhsuk-error-summary__body"
>
<
p
>
Describe the errors and how to correct them
</
p
>
<
ul
class
=
"nhsuk-list nhsuk-error-summary__list"
>
<
li
>
<
a
href
=
"#example-error-1"
>
Date of birth must be in the past
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
</
div
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the error summary.
Name heading | Type object | Description Required. Heading of the error summary component. See macro options for heading .
Name title Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.text option.
Name title Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name description | Type object | Description Description of the errors. See macro options for description .
Name description Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.text option.
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire error summary component in a call block.
Name error List | Type array | Description A list of errors to include in the error summary. See macro options for error List .
Name disable Auto Focus | Type boolean | Description Prevent moving focus to the error summary when the page loads.
Name classes | Type string | Description Classes to add to the error-summary container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error-summary container.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use for the description of the errors. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use for the description of the errors. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the error summary body.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error summary body.

Name | Type | Description
Name href | Type string | Description The error href attribute. If set, the error will become a link.
Name text | Type string | Description Required. If html is set, this is not required. Text for the error link item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the error link item. If html is provided, the text option will be ignored.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error link.

```text
{%
from
"error-summary/macro.njk"
import
errorSummary
%}
{{
errorSummary
({
heading
:
"There is a problem"
,
description
:
"Describe the errors and how to correct them"
,
errorList
: [
    {
text
:
"Date of birth must be in the past"
,
href
:
"#example-error-1"
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## When to use an error summary

When a user makes a mistake, you must show an error summary at the top of the page as well as an error message next to each answer that contains an error.

Always show an error summary when there is a validation error, even if there's only 1 mistake.

## How to use an error summary

You must:

- add "Error: " to the beginning of the <title> so screen readers read it out as soon as possible

- show an error summary at the top of a page

- move the keyboard focus to the error summary (the NHS.UK frontend JavaScript will do this for you)

- include the heading "There is a problem"

- link to each of the answers that have validation errors

- show the same error messages next to the inputs with errors

Follow GOV.UK Design System guidance on writing good error messages .

### Linking from the error summary to each answer

You must link the errors in the error summary to the answer they relate to.

For questions that require a user to answer using a single field, like a select, textarea or text input, link to the field.

- HTML code for error summary link input

- Nunjucks code for error summary link input

```text
<
div
class
=
"nhsuk-error-summary"
data-module
=
"nhsuk-error-summary"
>
<
div
role
=
"alert"
>
<
h2
class
=
"nhsuk-error-summary__heading"
>
There is a problem
</
h2
>
<
div
class
=
"nhsuk-error-summary__body"
>
<
ul
class
=
"nhsuk-list nhsuk-error-summary__list"
>
<
li
>
<
a
href
=
"#name"
>
Enter your full name
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
</
div
>
<
h1
class
=
"nhsuk-heading-l"
>
Your details
</
h1
>
<
div
class
=
"nhsuk-form-group nhsuk-form-group--error"
>
<
label
class
=
"nhsuk-label"
for
=
"name"
>
Full name
</
label
>
<
span
class
=
"nhsuk-error-message"
id
=
"name-error"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Error:
</
span
>
Enter your full name
</
span
>
<
input
class
=
"nhsuk-input nhsuk-input--error"
id
=
"name"
name
=
"name"
type
=
"text"
aria-describedby
=
"name-error"
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
Name id | Type string | Description The ID of the error summary.
Name heading | Type object | Description Required. Heading of the error summary component. See macro options for heading .
Name title Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.text option.
Name title Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name description | Type object | Description Description of the errors. See macro options for description .
Name description Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.text option.
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire error summary component in a call block.
Name error List | Type array | Description A list of errors to include in the error summary. See macro options for error List .
Name disable Auto Focus | Type boolean | Description Prevent moving focus to the error summary when the page loads.
Name classes | Type string | Description Classes to add to the error-summary container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error-summary container.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use for the description of the errors. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use for the description of the errors. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the error summary body.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error summary body.

Name | Type | Description
Name href | Type string | Description The error href attribute. If set, the error will become a link.
Name text | Type string | Description Required. If html is set, this is not required. Text for the error link item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the error link item. If html is provided, the text option will be ignored.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error link.

```text
{%
from
"error-summary/macro.njk"
import
errorSummary
%}
{%
from
"input/macro.njk"
import
input
%}
{{
errorSummary
({
titleText
:
"There is a problem"
,
errorList
: [
    {
text
:
"Enter your full name"
,
href
:
"#name"
}
  ]
})
}}
<
h1
class
=
"nhsuk-heading-l"
>
Your details
</
h1
>
{{
input
({
label
: {
text
:
"Full name"
},
errorMessage
: {
text
:
"Enter your full name"
},
id
:
"name"
,
name
:
"name"
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

When a user has to enter their answer into multiple fields, such as the day, month and year fields in the date input component, link to the 1st field that contains an error.

If you do not know which field contains an error, link to the 1st field.

- HTML code for error summary link multiple input

- Nunjucks code for error summary link multiple input

```text
<
div
class
=
"nhsuk-error-summary"
data-module
=
"nhsuk-error-summary"
>
<
div
role
=
"alert"
>
<
h2
class
=
"nhsuk-error-summary__heading"
>
There is a problem
</
h2
>
<
div
class
=
"nhsuk-error-summary__body"
>
<
ul
class
=
"nhsuk-list nhsuk-error-summary__list"
>
<
li
>
<
a
href
=
"#dob-errors-year"
>
Date of birth must include a year
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
</
div
>
<
div
class
=
"nhsuk-form-group nhsuk-form-group--error"
>
<
fieldset
class
=
"nhsuk-fieldset"
role
=
"group"
aria-describedby
=
"dob-errors-hint dob-errors-error"
>
<
legend
class
=
"nhsuk-fieldset__legend nhsuk-fieldset__legend--l"
>
<
h1
class
=
"nhsuk-fieldset__heading"
>
What is your date of birth?
</
h1
>
</
legend
>
<
div
class
=
"nhsuk-hint"
id
=
"dob-errors-hint"
>
For example, 15 3 1984
</
div
>
<
span
class
=
"nhsuk-error-message"
id
=
"dob-errors-error"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Error:
</
span
>
Date of birth must include a year
</
span
>
<
div
class
=
"nhsuk-date-input"
id
=
"dob-errors"
>
<
div
class
=
"nhsuk-date-input__item"
>
<
div
class
=
"nhsuk-form-group"
>
<
label
class
=
"nhsuk-label nhsuk-date-input__label"
for
=
"dob-errors-day"
>
Day
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--width-2 nhsuk-date-input__input"
id
=
"dob-errors-day"
name
=
"day"
type
=
"text"
value
=
"15"
inputmode
=
"numeric"
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
"nhsuk-date-input__item"
>
<
div
class
=
"nhsuk-form-group"
>
<
label
class
=
"nhsuk-label nhsuk-date-input__label"
for
=
"dob-errors-month"
>
Month
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--width-2 nhsuk-date-input__input"
id
=
"dob-errors-month"
name
=
"month"
type
=
"text"
value
=
"3"
inputmode
=
"numeric"
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
"nhsuk-date-input__item"
>
<
div
class
=
"nhsuk-form-group nhsuk-form-group--error"
>
<
label
class
=
"nhsuk-label nhsuk-date-input__label"
for
=
"dob-errors-year"
>
Year
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--error nhsuk-input--width-4 nhsuk-date-input__input"
id
=
"dob-errors-year"
name
=
"year"
type
=
"text"
inputmode
=
"numeric"
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
fieldset
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
Name id | Type string | Description The ID of the error summary.
Name heading | Type object | Description Required. Heading of the error summary component. See macro options for heading .
Name title Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.text option.
Name title Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name description | Type object | Description Description of the errors. See macro options for description .
Name description Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.text option.
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire error summary component in a call block.
Name error List | Type array | Description A list of errors to include in the error summary. See macro options for error List .
Name disable Auto Focus | Type boolean | Description Prevent moving focus to the error summary when the page loads.
Name classes | Type string | Description Classes to add to the error-summary container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error-summary container.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use for the description of the errors. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use for the description of the errors. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the error summary body.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error summary body.

Name | Type | Description
Name href | Type string | Description The error href attribute. If set, the error will become a link.
Name text | Type string | Description Required. If html is set, this is not required. Text for the error link item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the error link item. If html is provided, the text option will be ignored.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error link.

```text
{%
from
"error-summary/macro.njk"
import
errorSummary
%}
{%
from
"date-input/macro.njk"
import
dateInput
%}
{{
errorSummary
({
titleText
:
"There is a problem"
,
errorList
: [
    {
text
:
"Date of birth must include a year"
,
href
:
"#dob-errors-year"
}
  ]
})
}}
{{
dateInput
({
fieldset
: {
legend
: {
text
:
"What is your date of birth?"
,
size
:
"l"
,
isPageHeading
:
true
}
  },
hint
: {
text
:
"For example, 15 3 1984"
},
errorMessage
: {
text
:
"Date of birth must include a year"
},
id
:
"dob-errors"
,
day
: {
width
:
2
,
value
:
"15"
},
month
: {
width
:
2
,
value
:
"3"
},
year
: {
width
:
4
,
error
:
true
}
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

For questions that require a user to select one or more options from a list using radios or checkboxes, link to the 1st radio or checkbox.

- HTML code for error summary link options

- Nunjucks code for error summary link options

```text
<
div
class
=
"nhsuk-error-summary"
data-module
=
"nhsuk-error-summary"
>
<
div
role
=
"alert"
>
<
h2
class
=
"nhsuk-error-summary__heading"
>
There is a problem
</
h2
>
<
div
class
=
"nhsuk-error-summary__body"
>
<
ul
class
=
"nhsuk-list nhsuk-error-summary__list"
>
<
li
>
<
a
href
=
"#contact"
>
Select how you want to be contacted
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
</
div
>
<
div
class
=
"nhsuk-form-group nhsuk-form-group--error"
>
<
fieldset
class
=
"nhsuk-fieldset"
aria-describedby
=
"contact-hint contact-error"
>
<
legend
class
=
"nhsuk-fieldset__legend nhsuk-fieldset__legend--l"
>
<
h1
class
=
"nhsuk-fieldset__heading"
>
How do you want to be contacted about this?
</
h1
>
</
legend
>
<
div
class
=
"nhsuk-hint"
id
=
"contact-hint"
>
Select all options that are relevant to you
</
div
>
<
span
class
=
"nhsuk-error-message"
id
=
"contact-error"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Error:
</
span
>
Select how you want to be contacted
</
span
>
<
div
class
=
"nhsuk-checkboxes"
data-module
=
"nhsuk-checkboxes"
>
<
div
class
=
"nhsuk-checkboxes__item"
>
<
input
class
=
"nhsuk-checkboxes__input"
id
=
"contact"
name
=
"contact"
type
=
"checkbox"
value
=
"email"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"contact"
>
Email
</
label
>
</
div
>
<
div
class
=
"nhsuk-checkboxes__item"
>
<
input
class
=
"nhsuk-checkboxes__input"
id
=
"contact-2"
name
=
"contact"
type
=
"checkbox"
value
=
"phone"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"contact-2"
>
Phone
</
label
>
</
div
>
<
div
class
=
"nhsuk-checkboxes__item"
>
<
input
class
=
"nhsuk-checkboxes__input"
id
=
"contact-3"
name
=
"contact"
type
=
"checkbox"
value
=
"text message"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"contact-3"
>
Text message
</
label
>
</
div
>
</
div
>
</
fieldset
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
Name id | Type string | Description The ID of the error summary.
Name heading | Type object | Description Required. Heading of the error summary component. See macro options for heading .
Name title Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.text option.
Name title Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name description | Type object | Description Description of the errors. See macro options for description .
Name description Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.text option.
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire error summary component in a call block.
Name error List | Type array | Description A list of errors to include in the error summary. See macro options for error List .
Name disable Auto Focus | Type boolean | Description Prevent moving focus to the error summary when the page loads.
Name classes | Type string | Description Classes to add to the error-summary container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error-summary container.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use for the description of the errors. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use for the description of the errors. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the error summary body.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error summary body.

Name | Type | Description
Name href | Type string | Description The error href attribute. If set, the error will become a link.
Name text | Type string | Description Required. If html is set, this is not required. Text for the error link item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the error link item. If html is provided, the text option will be ignored.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error link.

```text
{%
from
"error-summary/macro.njk"
import
errorSummary
%}
{%
from
"checkboxes/macro.njk"
import
checkboxes
%}
{{
errorSummary
({
titleText
:
"There is a problem"
,
errorList
: [
    {
text
:
"Select how you want to be contacted"
,
href
:
"#contact"
}
  ]
})
}}
{{
checkboxes
({
fieldset
: {
legend
: {
text
:
"How do you want to be contacted about this?"
,
size
:
"l"
,
isPageHeading
:
true
}
  },
hint
: {
text
:
"Select all options that are relevant to you"
},
errorMessage
: {
text
:
"Select how you want to be contacted"
},
idPrefix
:
"contact"
,
name
:
"contact"
,
items
: [
    {
value
:
"email"
,
text
:
"Email"
,
id
:
"contact"
},
    {
value
:
"phone"
,
text
:
"Phone"
},
    {
value
:
"text message"
,
text
:
"Text message"
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Where to put the error summary

Put the error summary at the top of the main container. If your page includes breadcrumbs or a back link, place it below these, but above the <h1> .

- HTML code for error summary placement

- Nunjucks code for error summary placement

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
form
action
=
"/form-handler"
method
=
"post"
novalidate
>
<
div
class
=
"nhsuk-error-summary"
data-module
=
"nhsuk-error-summary"
>
<
div
role
=
"alert"
>
<
h2
class
=
"nhsuk-error-summary__heading"
>
There is a problem
</
h2
>
<
div
class
=
"nhsuk-error-summary__body"
>
<
ul
class
=
"nhsuk-list nhsuk-error-summary__list"
>
<
li
>
<
a
href
=
"#dob-errors-year"
>
Date of birth must include a year
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
</
div
>
<
div
class
=
"nhsuk-form-group nhsuk-form-group--error"
>
<
fieldset
class
=
"nhsuk-fieldset"
role
=
"group"
aria-describedby
=
"dob-errors-hint dob-errors-error"
>
<
legend
class
=
"nhsuk-fieldset__legend nhsuk-fieldset__legend--l"
>
<
h1
class
=
"nhsuk-fieldset__heading"
>
What is your date of birth?
</
h1
>
</
legend
>
<
div
class
=
"nhsuk-hint"
id
=
"dob-errors-hint"
>
For example, 15 3 1984
</
div
>
<
span
class
=
"nhsuk-error-message"
id
=
"dob-errors-error"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Error:
</
span
>
Date of birth must include a year
</
span
>
<
div
class
=
"nhsuk-date-input"
id
=
"dob-errors"
>
<
div
class
=
"nhsuk-date-input__item"
>
<
div
class
=
"nhsuk-form-group"
>
<
label
class
=
"nhsuk-label nhsuk-date-input__label"
for
=
"dob-errors-day"
>
Day
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--width-2 nhsuk-date-input__input"
id
=
"dob-errors-day"
name
=
"day"
type
=
"text"
value
=
"15"
inputmode
=
"numeric"
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
"nhsuk-date-input__item"
>
<
div
class
=
"nhsuk-form-group"
>
<
label
class
=
"nhsuk-label nhsuk-date-input__label"
for
=
"dob-errors-month"
>
Month
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--width-2 nhsuk-date-input__input"
id
=
"dob-errors-month"
name
=
"month"
type
=
"text"
value
=
"3"
inputmode
=
"numeric"
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
"nhsuk-date-input__item"
>
<
div
class
=
"nhsuk-form-group nhsuk-form-group--error"
>
<
label
class
=
"nhsuk-label nhsuk-date-input__label"
for
=
"dob-errors-year"
>
Year
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--error nhsuk-input--width-4 nhsuk-date-input__input"
id
=
"dob-errors-year"
name
=
"year"
type
=
"text"
inputmode
=
"numeric"
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
fieldset
>
</
div
>
<
button
class
=
"nhsuk-button"
data-module
=
"nhsuk-button"
type
=
"submit"
>
Continue
</
button
>
</
form
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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the error summary.
Name heading | Type object | Description Required. Heading of the error summary component. See macro options for heading .
Name title Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.text option.
Name title Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name description | Type object | Description Description of the errors. See macro options for description .
Name description Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.text option.
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire error summary component in a call block.
Name error List | Type array | Description A list of errors to include in the error summary. See macro options for error List .
Name disable Auto Focus | Type boolean | Description Prevent moving focus to the error summary when the page loads.
Name classes | Type string | Description Classes to add to the error-summary container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error-summary container.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use for the description of the errors. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use for the description of the errors. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the error summary body.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error summary body.

Name | Type | Description
Name href | Type string | Description The error href attribute. If set, the error will become a link.
Name text | Type string | Description Required. If html is set, this is not required. Text for the error link item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the error link item. If html is provided, the text option will be ignored.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error link.

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
"date-input/macro.njk"
import
dateInput
%}
{%
from
"error-summary/macro.njk"
import
errorSummary
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
<
form
action
=
"/form-handler"
method
=
"post"
novalidate
>
{{
errorSummary
({
titleText
:
"There is a problem"
,
errorList
: [
            {
text
:
"Date of birth must include a year"
,
href
:
"#dob-errors-year"
}
          ]
        })
}}
{{
dateInput
({
fieldset
: {
legend
: {
text
:
"What is your date of birth?"
,
size
:
"l"
,
isPageHeading
:
true
}
          },
hint
: {
text
:
"For example, 15 3 1984"
},
errorMessage
: {
text
:
"Date of birth must include a year"
},
id
:
"dob-errors"
,
day
: {
width
:
2
,
value
:
"15"
},
month
: {
width
:
2
,
value
:
"3"
},
year
: {
width
:
4
,
error
:
true
}
        })
}}
{{
button
({
text
:
"Continue"
})
}}
</
form
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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## Research

GOV.UK research on error summaries showed users:

- understood what went wrong

- knew how to fix the problem

- were able to recover from the error

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: November 2025
