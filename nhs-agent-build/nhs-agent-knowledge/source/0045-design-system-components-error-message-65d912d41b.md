# Error message – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/error-message/

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

# Form elements – Error message

Use an error message when there is a validation error. Explain what went wrong and how to fix it.

- HTML code for error message in context

- Nunjucks code for error message in context

```text
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
"dob-day-error-hint dob-day-error-error"
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
"dob-day-error-hint"
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
"dob-day-error-error"
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
Date of birth must be in the past
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
"dob-day-error"
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
"dob-day-error-day"
>
Day
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--error nhsuk-input--width-2 nhsuk-date-input__input"
id
=
"dob-day-error-day"
name
=
"dob-day-error[day]"
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
"nhsuk-form-group nhsuk-form-group--error"
>
<
label
class
=
"nhsuk-label nhsuk-date-input__label"
for
=
"dob-day-error-month"
>
Month
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--error nhsuk-input--width-2 nhsuk-date-input__input"
id
=
"dob-day-error-month"
name
=
"dob-day-error[month]"
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
"dob-day-error-year"
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
"dob-day-error-year"
name
=
"dob-day-error[year]"
type
=
"text"
value
=
"2084"
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
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the error message. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the error message. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire error message component in a call block.
Name id | Type string | Description The id attribute to add to the error message <span> tag.
Name classes | Type string | Description Classes to add to the error message <span> tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error message <span> tag.
Name visually Hidden Text | Type string | Description A visually hidden prefix used before the error message. Defaults to "Error" .

```text
{%
from
"error-message/macro.njk"
import
errorMessage
%}
{%
from
"date-input/macro.njk"
import
dateInput
%}
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
"Date of birth must be in the past"
},
id
:
"dob-day-error"
,
namePrefix
:
"dob-day-error"
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
value
:
"2084"
}
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## When to use error messages

Use the error message component when there is a validation error. For example when:

- you need to tell the user to choose an option before continuing

- you need the user to correct or change their input to match what your system can accept

Follow our guidance on how to write good questions for forms and make them easy to use so that users never see an error message.

## When not to use error messages

Only display an error when someone tries to move to the next part of the service. Do not show error messages:

- when users select or tab to a field

- as they are typing

- when they move away from a field

Do not use error messages to tell users that they are not eligible or do not have permission to do something. Instead, take them to a screen that:

- explains why you cannot accept the entry or selection

- tells them what to do next

- includes a way to leave the transaction

## How to use error messages

For each error:

- put the message in an error summary at the top of the page the user is on — linking to the answer that has the validation error

- put the message in red after the question text and hint text

- use a red border to visually connect the message and the question it belongs to

- if the error relates to specific text fields in the question, give these a red border as well

Do not clear any form fields when adding error messages. Keeping information that caused errors helps users to:

- see what went wrong

- edit their previous answer

- avoid re-entering information

To help screen reader users, the error message component includes a hidden "Error:" before the error message. These users will hear, for example, "Error: Date of birth must be in the past".

```text
<
span
class
=
"nhsuk-error-message"
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
Date of birth must be in the past
</
span
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### If you're using a legend

This is how we use an error message with a legend , for example with radios or checkboxes .

- HTML code for error message radios

- Nunjucks code for error message radios

```text
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
"example-error-hint example-error-error"
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
Have you changed your name?
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
"example-error-hint"
>
This includes changing your last name or spelling your name differently
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
"example-error-error"
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
Select yes if you have changed your name
</
span
>
<
div
class
=
"nhsuk-radios"
data-module
=
"nhsuk-radios"
>
<
div
class
=
"nhsuk-radios__item"
>
<
input
class
=
"nhsuk-radios__input"
id
=
"example-error"
name
=
"exampleError"
type
=
"radio"
value
=
"yes"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"example-error"
>
Yes
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
"nhsuk-radios__item"
>
<
input
class
=
"nhsuk-radios__input"
id
=
"example-error-2"
name
=
"exampleError"
type
=
"radio"
value
=
"no"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"example-error-2"
>
No
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
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the error message. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the error message. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire error message component in a call block.
Name id | Type string | Description The id attribute to add to the error message <span> tag.
Name classes | Type string | Description Classes to add to the error message <span> tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error message <span> tag.
Name visually Hidden Text | Type string | Description A visually hidden prefix used before the error message. Defaults to "Error" .

```text
{%
from
"radios/macro.njk"
import
radios
%}
{{
radios
({
fieldset
: {
legend
: {
text
:
"Have you changed your name?"
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
"This includes changing your last name or spelling your name differently"
},
errorMessage
: {
text
:
"Select yes if you have changed your name"
},
idPrefix
:
"example-error"
,
name
:
"exampleError"
,
items
: [
    {
value
:
"yes"
,
text
:
"Yes"
},
    {
value
:
"no"
,
text
:
"No"
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### If you're using a label

This is how we use an error message with a label, for example, with text input .

- HTML code for error message input

- Nunjucks code for error message input

```text
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
"example"
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
"example-error"
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
"example"
name
=
"example"
type
=
"text"
aria-describedby
=
"example-error"
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
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the error message. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the error message. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire error message component in a call block.
Name id | Type string | Description The id attribute to add to the error message <span> tag.
Name classes | Type string | Description Classes to add to the error message <span> tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error message <span> tag.
Name visually Hidden Text | Type string | Description A visually hidden prefix used before the error message. Defaults to "Error" .

```text
{%
from
"input/macro.njk"
import
input
%}
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
"example"
,
name
:
"example"
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Using an error summary

Summarise all errors at the top of the page the user is on using an error summary . For example:

- HTML code for error message error summary placement

- Nunjucks code for error message error summary placement

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
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the error message. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the error message. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire error message component in a call block.
Name id | Type string | Description The id attribute to add to the error message <span> tag.
Name classes | Type string | Description Classes to add to the error message <span> tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error message <span> tag.
Name visually Hidden Text | Type string | Description A visually hidden prefix used before the error message. Defaults to "Error" .

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

- HTML code for error message error summary placement input

- Nunjucks code for error message error summary placement input

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
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the error message. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the error message. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire error message component in a call block.
Name id | Type string | Description The id attribute to add to the error message <span> tag.
Name classes | Type string | Description Classes to add to the error message <span> tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error message <span> tag.
Name visually Hidden Text | Type string | Description A visually hidden prefix used before the error message. Defaults to "Error" .

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

- HTML code for error message error summary placement multiple

- Nunjucks code for error message error summary placement multiple

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
"#first-name"
>
Enter your first name
</
a
>
</
li
>
<
li
>
<
a
href
=
"#last-name"
>
Enter your last name
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
"first-name"
>
First name
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
"first-name-error"
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
Enter your first name
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
"first-name"
name
=
"firstName"
type
=
"text"
aria-describedby
=
"first-name-error"
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
label
class
=
"nhsuk-label"
for
=
"last-name"
>
Last name
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
"last-name-error"
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
Enter your last name
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
"last-name"
name
=
"lastName"
type
=
"text"
aria-describedby
=
"last-name-error"
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
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the error message. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the error message. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire error message component in a call block.
Name id | Type string | Description The id attribute to add to the error message <span> tag.
Name classes | Type string | Description Classes to add to the error message <span> tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the error message <span> tag.
Name visually Hidden Text | Type string | Description A visually hidden prefix used before the error message. Defaults to "Error" .

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
"Enter your first  name"
,
href
:
"#first-name"
},
            {
text
:
"Enter your last name"
,
href
:
"#last-name"
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
"First name"
},
errorMessage
: {
text
:
"Enter your first name"
},
id
:
"first-name"
,
name
:
"firstName"
})
}}
{{
input
({
label
: {
text
:
"Last name"
},
errorMessage
: {
text
:
"Enter your last name"
},
id
:
"last-name"
,
name
:
"lastName"
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

### How to write error messages

Focus on telling users how to fix the problem rather than describing what's gone wrong. You may need to write more than 1 error message for each field. See the GOV.UK error message component for more guidance on writing good error messages .

Use standard messages for different components. The GOV.UK error message component also includes error message templates for common errors .

## Research

Research on error messages showed users:

- understood what went wrong

- knew how to fix the problem

- were able to recover from the error

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
