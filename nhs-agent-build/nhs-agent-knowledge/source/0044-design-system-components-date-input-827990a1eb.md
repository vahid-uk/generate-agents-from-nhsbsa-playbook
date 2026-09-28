# Date input – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/date-input/

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

# Form elements – Date input

Use date input to help users enter a date, like an appointment date.

- HTML code for date input

- Nunjucks code for date input

```text
<
div
class
=
"nhsuk-form-group"
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
"appointment-date-hint"
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
When was your appointment?
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
"appointment-date-hint"
>
For example, 18 8 2026
</
div
>
<
div
class
=
"nhsuk-date-input"
id
=
"appointment-date"
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
"appointment-date-day"
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
"appointment-date-day"
name
=
"appointmentDate[day]"
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
"appointment-date-month"
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
"appointment-date-month"
name
=
"appointmentDate[month]"
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
"appointment-date-year"
>
Year
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--width-4 nhsuk-date-input__input"
id
=
"appointment-date-year"
name
=
"appointmentDate[year]"
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description Required. This is used for the main component and to compose the id attribute for each item.
Name name Prefix | Type string | Description Optional prefix. This is used to prefix each date input name attribute, wrapped in [ and ] – for example, namePrefix: "dob" will output the name attributes dob[day] , dob[month] and dob[year] respectively.
Name items | Type array | Description The inputs within the date input component. The input.errorMessage and input.hint options are not supported. See items macro options using input component macro .
Name hint | Type object | Description Can be used to add a hint to the date input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the date input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the date input component. See macro options for form Group .
Name fieldset | Type object | Description Can be used to add a fieldset to the date input component. The fieldset.html option is not supported. See macro options for fieldset .
Name day | Type object | Description Can be used to customise the day input within the date input component. The input.formGroup and input.inputWrapper options are not supported. See day macro options using input component macro .
Name month | Type object | Description Can be used to customise the month input within the date input component. The input.formGroup and input.inputWrapper options are not supported. See month macro options using input component macro .
Name year | Type object | Description Can be used to customise the year input within the date input component. The input.formGroup and input.inputWrapper options are not supported. See year macro options using input component macro .
Name values | Type object | Description An optional object used to specify value attributes for the inputs within the date input component without setting items . See macro options for values .
Name disabled | Type boolean | Description If true , inputs used by the date input component will be disabled.
Name classes | Type string | Description Classes to add to the date input container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the date input container.

Name | Type | Description
Name name | Type string | Description Required. Item-specific name attribute. Defaults to "day" , "month" or "year" .
Name label | Type object | Description Item-specific label. The label.size and label.heading options are not supported. Defaults to the name option capitalised. See macro options for label .
Name error | Type boolean | Description If set to true , show a red border on the item input.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before the inputs used by the date input component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after the inputs used by the date input component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the inputs. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the inputs. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the inputs. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the inputs. If html is provided, the text option will be ignored.

Name | Type | Description
Name name | Type string | Description The name attribute for the day input. Defaults to "day" .
Name value | Type string | Description The value attribute for the day input.
Name label | Type object | Description The label used by the day input. The label.size and label.heading options are not supported. Defaults to the name option capitalised. See macro options for label .
Name error | Type boolean | Description If set to true , show a red border on the day input.

Name | Type | Description
Name name | Type string | Description The name attribute for the month input. Defaults to "month" .
Name value | Type string | Description The value attribute for the month input.
Name label | Type object | Description The label used by the month input. The label.size and label.heading options are not supported. Defaults to the name option capitalised. See macro options for label .
Name error | Type boolean | Description If set to true , show a red border on the month input.

Name | Type | Description
Name name | Type string | Description The name attribute for the year input. Defaults to "year" .
Name value | Type string | Description The value attribute for the year input.
Name label | Type object | Description The label used by the year input. The label.size and label.heading options are not supported. Defaults to the name option capitalised. See macro options for label .
Name error | Type boolean | Description If set to true , show a red border on the year input.

Name | Type | Description
Name day | Type string | Description The value attribute for the day input.
Name month | Type string | Description The value attribute for the month input.
Name year | Type string | Description The value attribute for the year input.

Name | Type | Description
Name id | Type string | Description The ID of the label.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the label. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire label component in a call block.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the label.
Name caption | Type object | Description Optional caption for the label. See macro options for caption .
Name for | Type string | Description The label for attribute, the ID of the input the label is associated with.
Name heading | Type object | Description Whether the label also acts as a heading. See macro options for heading .
Name is Page Heading | Type boolean | Description Deprecated in 10.6.1 (see GitHub) . Replaced by the heading option.
Name size | Type string | Description Size of the label – "s" , "m" , "l" or "xl" .
Name classes | Type string | Description Classes to add to the label tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the label tag.

```text
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
"When was your appointment?"
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
"For example, 18 8 2026"
},
id
:
"appointment-date"
,
namePrefix
:
"appointmentDate"
,
day
: {
width
:
2
},
month
: {
width
:
2
},
year
: {
width
:
4
}
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

## When to use date input

We follow the GOV.UK Design System. Use date input when you're asking users for a date they already know.

## When not to use date input

Do not use date input if users are unlikely to know the exact date you're asking about.

## How to use date input

Date input consists of 3 fields to let users enter a day, month and year.

Group the 3 date fields together in a <fieldset> with a <legend> that describes them. You can see an example at the top of this page. The legend is usually a question, like "When was your appointment?".

If you are asking just 1 question per page as we recommend, you can set the contents of the <legend> as the page heading. This is good practice as it means that screen reader users will only hear the contents once.

Read more on the GOV.UK Design System about how to ask users for dates and making labels and legends headings .

## Using the autocomplete attribute

If you are asking the user for their own date of birth, use the autocomplete attributes. This lets some browsers autofill the information if the user has entered it previously.

You'll need to do this to meet WCAG 2.2 success criterion 1.3.5: Identify input purpose, level AA .

Set the autocomplete attribute on the 3 fields to bday-day , bday-month and bday-year . See how to do this in the HTML and Nunjucks tabs in the following example.

- HTML code for date input your date of birth

- Nunjucks code for date input your date of birth

```text
<
div
class
=
"nhsuk-form-group"
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
"date-of-birth-hint"
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
"date-of-birth-hint"
>
For example, 15 3 1984
</
div
>
<
div
class
=
"nhsuk-date-input"
id
=
"date-of-birth"
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
"date-of-birth-day"
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
"date-of-birth-day"
name
=
"dateOfBirth[day]"
type
=
"text"
autocomplete
=
"bday-day"
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
"date-of-birth-month"
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
"date-of-birth-month"
name
=
"dateOfBirth[month]"
type
=
"text"
autocomplete
=
"bday-month"
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
"date-of-birth-year"
>
Year
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--width-4 nhsuk-date-input__input"
id
=
"date-of-birth-year"
name
=
"dateOfBirth[year]"
type
=
"text"
autocomplete
=
"bday-year"
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description Required. This is used for the main component and to compose the id attribute for each item.
Name name Prefix | Type string | Description Optional prefix. This is used to prefix each date input name attribute, wrapped in [ and ] – for example, namePrefix: "dob" will output the name attributes dob[day] , dob[month] and dob[year] respectively.
Name items | Type array | Description The inputs within the date input component. The input.errorMessage and input.hint options are not supported. See items macro options using input component macro .
Name hint | Type object | Description Can be used to add a hint to the date input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the date input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the date input component. See macro options for form Group .
Name fieldset | Type object | Description Can be used to add a fieldset to the date input component. The fieldset.html option is not supported. See macro options for fieldset .
Name day | Type object | Description Can be used to customise the day input within the date input component. The input.formGroup and input.inputWrapper options are not supported. See day macro options using input component macro .
Name month | Type object | Description Can be used to customise the month input within the date input component. The input.formGroup and input.inputWrapper options are not supported. See month macro options using input component macro .
Name year | Type object | Description Can be used to customise the year input within the date input component. The input.formGroup and input.inputWrapper options are not supported. See year macro options using input component macro .
Name values | Type object | Description An optional object used to specify value attributes for the inputs within the date input component without setting items . See macro options for values .
Name disabled | Type boolean | Description If true , inputs used by the date input component will be disabled.
Name classes | Type string | Description Classes to add to the date input container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the date input container.

Name | Type | Description
Name name | Type string | Description Required. Item-specific name attribute. Defaults to "day" , "month" or "year" .
Name label | Type object | Description Item-specific label. The label.size and label.heading options are not supported. Defaults to the name option capitalised. See macro options for label .
Name error | Type boolean | Description If set to true , show a red border on the item input.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before the inputs used by the date input component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after the inputs used by the date input component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the inputs. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the inputs. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the inputs. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the inputs. If html is provided, the text option will be ignored.

Name | Type | Description
Name name | Type string | Description The name attribute for the day input. Defaults to "day" .
Name value | Type string | Description The value attribute for the day input.
Name label | Type object | Description The label used by the day input. The label.size and label.heading options are not supported. Defaults to the name option capitalised. See macro options for label .
Name error | Type boolean | Description If set to true , show a red border on the day input.

Name | Type | Description
Name name | Type string | Description The name attribute for the month input. Defaults to "month" .
Name value | Type string | Description The value attribute for the month input.
Name label | Type object | Description The label used by the month input. The label.size and label.heading options are not supported. Defaults to the name option capitalised. See macro options for label .
Name error | Type boolean | Description If set to true , show a red border on the month input.

Name | Type | Description
Name name | Type string | Description The name attribute for the year input. Defaults to "year" .
Name value | Type string | Description The value attribute for the year input.
Name label | Type object | Description The label used by the year input. The label.size and label.heading options are not supported. Defaults to the name option capitalised. See macro options for label .
Name error | Type boolean | Description If set to true , show a red border on the year input.

Name | Type | Description
Name day | Type string | Description The value attribute for the day input.
Name month | Type string | Description The value attribute for the month input.
Name year | Type string | Description The value attribute for the year input.

Name | Type | Description
Name id | Type string | Description The ID of the label.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the label. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire label component in a call block.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the label.
Name caption | Type object | Description Optional caption for the label. See macro options for caption .
Name for | Type string | Description The label for attribute, the ID of the input the label is associated with.
Name heading | Type object | Description Whether the label also acts as a heading. See macro options for heading .
Name is Page Heading | Type boolean | Description Deprecated in 10.6.1 (see GitHub) . Replaced by the heading option.
Name size | Type string | Description Size of the label – "s" , "m" , "l" or "xl" .
Name classes | Type string | Description Classes to add to the label tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the label tag.

```text
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
id
:
"date-of-birth"
,
namePrefix
:
"dateOfBirth"
,
day
: {
width
:
2
,
autocomplete
:
"bday-day"
},
month
: {
width
:
2
,
autocomplete
:
"bday-month"
},
year
: {
width
:
4
,
autocomplete
:
"bday-year"
}
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

## Error messages

Style error messages like this.

- HTML code for date input with errors

- Nunjucks code for date input with errors

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
"appointment-date-hint appointment-date-error"
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
When was your appointment?
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
"appointment-date-hint"
>
For example, 18 8 2026
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
"appointment-date-error"
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
Enter your appointment date
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
"appointment-date"
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
"appointment-date-day"
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
"appointment-date-day"
name
=
"appointmentDate[day]"
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
"appointment-date-month"
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
"appointment-date-month"
name
=
"appointmentDate[month]"
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
"appointment-date-year"
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
"appointment-date-year"
name
=
"appointmentDate[year]"
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description Required. This is used for the main component and to compose the id attribute for each item.
Name name Prefix | Type string | Description Optional prefix. This is used to prefix each date input name attribute, wrapped in [ and ] – for example, namePrefix: "dob" will output the name attributes dob[day] , dob[month] and dob[year] respectively.
Name items | Type array | Description The inputs within the date input component. The input.errorMessage and input.hint options are not supported. See items macro options using input component macro .
Name hint | Type object | Description Can be used to add a hint to the date input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the date input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the date input component. See macro options for form Group .
Name fieldset | Type object | Description Can be used to add a fieldset to the date input component. The fieldset.html option is not supported. See macro options for fieldset .
Name day | Type object | Description Can be used to customise the day input within the date input component. The input.formGroup and input.inputWrapper options are not supported. See day macro options using input component macro .
Name month | Type object | Description Can be used to customise the month input within the date input component. The input.formGroup and input.inputWrapper options are not supported. See month macro options using input component macro .
Name year | Type object | Description Can be used to customise the year input within the date input component. The input.formGroup and input.inputWrapper options are not supported. See year macro options using input component macro .
Name values | Type object | Description An optional object used to specify value attributes for the inputs within the date input component without setting items . See macro options for values .
Name disabled | Type boolean | Description If true , inputs used by the date input component will be disabled.
Name classes | Type string | Description Classes to add to the date input container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the date input container.

Name | Type | Description
Name name | Type string | Description Required. Item-specific name attribute. Defaults to "day" , "month" or "year" .
Name label | Type object | Description Item-specific label. The label.size and label.heading options are not supported. Defaults to the name option capitalised. See macro options for label .
Name error | Type boolean | Description If set to true , show a red border on the item input.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before the inputs used by the date input component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after the inputs used by the date input component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the inputs. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the inputs. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the inputs. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the inputs. If html is provided, the text option will be ignored.

Name | Type | Description
Name name | Type string | Description The name attribute for the day input. Defaults to "day" .
Name value | Type string | Description The value attribute for the day input.
Name label | Type object | Description The label used by the day input. The label.size and label.heading options are not supported. Defaults to the name option capitalised. See macro options for label .
Name error | Type boolean | Description If set to true , show a red border on the day input.

Name | Type | Description
Name name | Type string | Description The name attribute for the month input. Defaults to "month" .
Name value | Type string | Description The value attribute for the month input.
Name label | Type object | Description The label used by the month input. The label.size and label.heading options are not supported. Defaults to the name option capitalised. See macro options for label .
Name error | Type boolean | Description If set to true , show a red border on the month input.

Name | Type | Description
Name name | Type string | Description The name attribute for the year input. Defaults to "year" .
Name value | Type string | Description The value attribute for the year input.
Name label | Type object | Description The label used by the year input. The label.size and label.heading options are not supported. Defaults to the name option capitalised. See macro options for label .
Name error | Type boolean | Description If set to true , show a red border on the year input.

Name | Type | Description
Name day | Type string | Description The value attribute for the day input.
Name month | Type string | Description The value attribute for the month input.
Name year | Type string | Description The value attribute for the year input.

Name | Type | Description
Name id | Type string | Description The ID of the label.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the label. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire label component in a call block.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the label.
Name caption | Type object | Description Optional caption for the label. See macro options for caption .
Name for | Type string | Description The label for attribute, the ID of the input the label is associated with.
Name heading | Type object | Description Whether the label also acts as a heading. See macro options for heading .
Name is Page Heading | Type boolean | Description Deprecated in 10.6.1 (see GitHub) . Replaced by the heading option.
Name size | Type string | Description Size of the label – "s" , "m" , "l" or "xl" .
Name classes | Type string | Description Classes to add to the label tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the label tag.

```text
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
"When was your appointment?"
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
"For example, 18 8 2026"
},
errorMessage
: {
text
:
"Enter your appointment date"
},
id
:
"appointment-date"
,
namePrefix
:
"appointmentDate"
,
day
: {
width
:
2
},
month
: {
width
:
2
},
year
: {
width
:
4
}
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Follow:

- our guidance on error messages

- GOV.UK guidance on error messages for date inputs

## Research

Our date input is based on the component in the GOV.UK Design System . GOV.UK says that they need to do more research to understand if users struggle to enter months as numbers and whether it's more helpful to let them enter months as text.

If you've used this component, get in touch to share your user research findings.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: April 2026
