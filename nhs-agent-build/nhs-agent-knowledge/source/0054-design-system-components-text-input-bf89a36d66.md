# Text input – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/text-input/

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

# Form elements – Text input

Use text input to let users enter a single line of text.

- HTML code for text input

- Nunjucks code for text input

```text
<
div
class
=
"nhsuk-form-group"
>
<
h1
class
=
"nhsuk-label-wrapper"
>
<
label
class
=
"nhsuk-label nhsuk-label--l"
for
=
"full-name"
>
What is your full name?
</
label
>
</
h1
>
<
input
class
=
"nhsuk-input"
id
=
"full-name"
name
=
"fullName"
type
=
"text"
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
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name type | Type string | Description Type of input control, for example, an email input control. Defaults to "text" .
Name inputmode | Type string | Description Optional value for the inputmode attribute .
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the text input component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to a text input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the text input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the text input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the text input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the text input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "bday-day" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name pattern | Type string | Description Attribute to provide a regular expression pattern , used to match allowed character combinations for the input value.
Name placeholder | Type string | Description Attribute to provide placeholder text for the input.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the input.
Name autocapitalize | Type string | Description Optional field to enable or disable autocapitalisation of user input. See the Autocapitalization section in the HTML standard for a full list of values that can be used.
Name input Wrapper | Type object | Description If any of prefix , suffix , formGroup.beforeInput or formGroup.afterInput have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.

Name | Type | Description
Name text | Type string | Description Required. Required. If html is set, this is not required. Text to use within the prefix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. Required. If text is set, this is not required. HTML to use within the prefix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the prefix.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the prefix element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the suffix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the suffix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the suffix element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the suffix element.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the text input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the text input component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the wrapping element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the wrapping element.

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
"What is your full name?"
,
size
:
"l"
,
isPageHeading
:
true
},
id
:
"full-name"
,
name
:
"fullName"
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

## When to use the text input component

Use the text input component when you need users to enter text that's no longer than a single line, such as their name or phone number.

## When not to use the text input component

Do not use this component if you need users to enter longer answers that might span several lines. In this case, use the textarea component .

## How to use the text input component

### Give the text input a label

Give it a visible label. Do not use placeholder text for a label as it vanishes when users click on the text input.

Align labels above the text inputs they refer to. Labels should be short, direct and written in sentence case. Do not use colons at the end of labels.

#### If you're asking 1 question on the page

If you are asking just 1 question per page as we recommend, you can set the contents of the <label> as the page heading. This is good practice as it means that screen reader users will only hear the contents once.

Read more about how to make labels and legends headings on the GOV.UK Design System.

- HTML code for text input second

- Nunjucks code for text input second

```text
<
div
class
=
"nhsuk-form-group"
>
<
h1
class
=
"nhsuk-label-wrapper"
>
<
label
class
=
"nhsuk-label nhsuk-label--l"
for
=
"full-name"
>
What is your full name?
</
label
>
</
h1
>
<
input
class
=
"nhsuk-input"
id
=
"full-name"
name
=
"fullName"
type
=
"text"
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
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name type | Type string | Description Type of input control, for example, an email input control. Defaults to "text" .
Name inputmode | Type string | Description Optional value for the inputmode attribute .
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the text input component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to a text input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the text input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the text input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the text input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the text input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "bday-day" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name pattern | Type string | Description Attribute to provide a regular expression pattern , used to match allowed character combinations for the input value.
Name placeholder | Type string | Description Attribute to provide placeholder text for the input.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the input.
Name autocapitalize | Type string | Description Optional field to enable or disable autocapitalisation of user input. See the Autocapitalization section in the HTML standard for a full list of values that can be used.
Name input Wrapper | Type object | Description If any of prefix , suffix , formGroup.beforeInput or formGroup.afterInput have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.

Name | Type | Description
Name text | Type string | Description Required. Required. If html is set, this is not required. Text to use within the prefix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. Required. If text is set, this is not required. HTML to use within the prefix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the prefix.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the prefix element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the suffix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the suffix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the suffix element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the suffix element.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the text input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the text input component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the wrapping element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the wrapping element.

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
"What is your full name?"
,
size
:
"l"
,
isPageHeading
:
true
},
id
:
"full-name"
,
name
:
"fullName"
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

#### If you're asking more than 1 question on the page

If you're asking more than 1 question on the page, do not set the contents of the <label> as the page heading. Read more about asking multiple questions on question pages .

- HTML code for text input without heading

- Nunjucks code for text input without heading

```text
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
"nhsuk-label"
for
=
"full-name"
>
What is your full name?
</
label
>
<
input
class
=
"nhsuk-input"
id
=
"full-name"
name
=
"fullName"
type
=
"text"
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
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name type | Type string | Description Type of input control, for example, an email input control. Defaults to "text" .
Name inputmode | Type string | Description Optional value for the inputmode attribute .
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the text input component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to a text input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the text input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the text input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the text input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the text input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "bday-day" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name pattern | Type string | Description Attribute to provide a regular expression pattern , used to match allowed character combinations for the input value.
Name placeholder | Type string | Description Attribute to provide placeholder text for the input.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the input.
Name autocapitalize | Type string | Description Optional field to enable or disable autocapitalisation of user input. See the Autocapitalization section in the HTML standard for a full list of values that can be used.
Name input Wrapper | Type object | Description If any of prefix , suffix , formGroup.beforeInput or formGroup.afterInput have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.

Name | Type | Description
Name text | Type string | Description Required. Required. If html is set, this is not required. Text to use within the prefix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. Required. If text is set, this is not required. HTML to use within the prefix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the prefix.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the prefix element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the suffix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the suffix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the suffix element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the suffix element.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the text input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the text input component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the wrapping element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the wrapping element.

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
"What is your full name?"
},
id
:
"full-name"
,
name
:
"fullName"
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### Make text inputs the right size

Help users understand what they should enter by making text inputs the right size for the information you want them to give you.

By default, the width of text inputs is fluid and will fit the full width of the container they are placed into.

If you want to make the input smaller, you can either use a fixed width input, or use the width override classes to create a smaller, fluid width input .

#### Fixed width inputs

Use fixed width inputs for content that has a specific, known length. For example, postcode inputs should be postcode-sized and phone number inputs should be phone number-sized.

On fixed width inputs, the width will remain fixed on all screens unless it is wider than the viewport, in which case it will shrink to fit.

- HTML code for text input fixed width

- Nunjucks code for text input fixed width

```text
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
"nhsuk-label"
for
=
"input-width-20"
>
20 character width
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--width-20"
id
=
"input-width-20"
name
=
"inputWidth20"
type
=
"text"
>
</
div
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
"nhsuk-label"
for
=
"input-width-10"
>
10 character width
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--width-10"
id
=
"input-width-10"
name
=
"inputWidth10"
type
=
"text"
>
</
div
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
"nhsuk-label"
for
=
"input-width-5"
>
5 character width
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--width-5"
id
=
"input-width-5"
name
=
"inputWidth5"
type
=
"text"
>
</
div
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
"nhsuk-label"
for
=
"input-width-4"
>
4 character width
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--width-4"
id
=
"input-width-4"
name
=
"inputWidth4"
type
=
"text"
>
</
div
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
"nhsuk-label"
for
=
"input-width-3"
>
3 character width
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--width-3"
id
=
"input-width-3"
name
=
"inputWidth3"
type
=
"text"
>
</
div
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
"nhsuk-label"
for
=
"input-width-2"
>
2 character width
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--width-2"
id
=
"input-width-2"
name
=
"inputWidth2"
type
=
"text"
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
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name type | Type string | Description Type of input control, for example, an email input control. Defaults to "text" .
Name inputmode | Type string | Description Optional value for the inputmode attribute .
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the text input component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to a text input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the text input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the text input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the text input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the text input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "bday-day" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name pattern | Type string | Description Attribute to provide a regular expression pattern , used to match allowed character combinations for the input value.
Name placeholder | Type string | Description Attribute to provide placeholder text for the input.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the input.
Name autocapitalize | Type string | Description Optional field to enable or disable autocapitalisation of user input. See the Autocapitalization section in the HTML standard for a full list of values that can be used.
Name input Wrapper | Type object | Description If any of prefix , suffix , formGroup.beforeInput or formGroup.afterInput have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.

Name | Type | Description
Name text | Type string | Description Required. Required. If html is set, this is not required. Text to use within the prefix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. Required. If text is set, this is not required. HTML to use within the prefix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the prefix.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the prefix element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the suffix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the suffix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the suffix element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the suffix element.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the text input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the text input component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the wrapping element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the wrapping element.

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
"20 character width"
},
id
:
"input-width-20"
,
name
:
"inputWidth20"
,
width
:
20
})
}}
{{
input
({
label
: {
text
:
"10 character width"
},
id
:
"input-width-10"
,
name
:
"inputWidth10"
,
width
:
10
})
}}
{{
input
({
label
: {
text
:
"5 character width"
},
id
:
"input-width-5"
,
name
:
"inputWidth5"
,
width
:
5
})
}}
{{
input
({
label
: {
text
:
"4 character width"
},
id
:
"input-width-4"
,
name
:
"inputWidth4"
,
width
:
4
})
}}
{{
input
({
label
: {
text
:
"3 character width"
},
id
:
"input-width-3"
,
name
:
"inputWidth3"
,
width
:
3
})
}}
{{
input
({
label
: {
text
:
"2 character width"
},
id
:
"input-width-2"
,
name
:
"inputWidth2"
,
width
:
2
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

#### Fluid width inputs

Use the width override classes to reduce the width of an input in relation to its parent container, for example, to two-thirds.

Fluid width inputs will resize with the viewport.

- HTML code for text input fluid width

- Nunjucks code for text input fluid width

```text
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
"nhsuk-label"
for
=
"full"
>
Full width
</
label
>
<
input
class
=
"nhsuk-input nhsuk-u-width-full"
id
=
"full"
name
=
"full"
type
=
"text"
>
</
div
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
"nhsuk-label"
for
=
"three-quarters"
>
Three-quarters width
</
label
>
<
input
class
=
"nhsuk-input nhsuk-u-width-three-quarters"
id
=
"three-quarters"
name
=
"threeQuarters"
type
=
"text"
>
</
div
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
"nhsuk-label"
for
=
"two-thirds"
>
Two-thirds width
</
label
>
<
input
class
=
"nhsuk-input nhsuk-u-width-two-thirds"
id
=
"two-thirds"
name
=
"twoThirds"
type
=
"text"
>
</
div
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
"nhsuk-label"
for
=
"one-half"
>
One-half width
</
label
>
<
input
class
=
"nhsuk-input nhsuk-u-width-one-half"
id
=
"one-half"
name
=
"oneHalf"
type
=
"text"
>
</
div
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
"nhsuk-label"
for
=
"one-third"
>
One-third width
</
label
>
<
input
class
=
"nhsuk-input nhsuk-u-width-one-third"
id
=
"one-third"
name
=
"oneThird"
type
=
"text"
>
</
div
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
"nhsuk-label"
for
=
"one-quarter"
>
One-quarter width
</
label
>
<
input
class
=
"nhsuk-input nhsuk-u-width-one-quarter"
id
=
"one-quarter"
name
=
"oneQuarter"
type
=
"text"
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
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name type | Type string | Description Type of input control, for example, an email input control. Defaults to "text" .
Name inputmode | Type string | Description Optional value for the inputmode attribute .
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the text input component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to a text input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the text input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the text input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the text input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the text input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "bday-day" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name pattern | Type string | Description Attribute to provide a regular expression pattern , used to match allowed character combinations for the input value.
Name placeholder | Type string | Description Attribute to provide placeholder text for the input.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the input.
Name autocapitalize | Type string | Description Optional field to enable or disable autocapitalisation of user input. See the Autocapitalization section in the HTML standard for a full list of values that can be used.
Name input Wrapper | Type object | Description If any of prefix , suffix , formGroup.beforeInput or formGroup.afterInput have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.

Name | Type | Description
Name text | Type string | Description Required. Required. If html is set, this is not required. Text to use within the prefix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. Required. If text is set, this is not required. HTML to use within the prefix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the prefix.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the prefix element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the suffix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the suffix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the suffix element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the suffix element.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the text input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the text input component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the wrapping element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the wrapping element.

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
"Full width"
},
id
:
"full"
,
name
:
"full"
,
classes
:
"nhsuk-u-width-full"
})
}}
{{
input
({
label
: {
text
:
"Three-quarters width"
},
id
:
"three-quarters"
,
name
:
"threeQuarters"
,
classes
:
"nhsuk-u-width-three-quarters"
})
}}
{{
input
({
label
: {
text
:
"Two-thirds width"
},
id
:
"two-thirds"
,
name
:
"twoThirds"
,
classes
:
"nhsuk-u-width-two-thirds"
})
}}
{{
input
({
label
: {
text
:
"One-half width"
},
id
:
"one-half"
,
name
:
"oneHalf"
,
classes
:
"nhsuk-u-width-one-half"
})
}}
{{
input
({
label
: {
text
:
"One-third width"
},
id
:
"one-third"
,
name
:
"oneThird"
,
classes
:
"nhsuk-u-width-one-third"
})
}}
{{
input
({
label
: {
text
:
"One-quarter width"
},
id
:
"one-quarter"
,
name
:
"oneQuarter"
,
classes
:
"nhsuk-u-width-one-quarter"
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### Using hint text

You can use hint text to give users help in context , so they understand what they need to enter. For example, use it to tell users where to find information or how you will use their data. Read more about hint text .

- HTML code for text input hint text

- Nunjucks code for text input hint text

```text
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
"nhsuk-label"
for
=
"example-with-hint-text"
>
Enter a full postcode in England
</
label
>
<
div
class
=
"nhsuk-hint"
id
=
"example-with-hint-text-hint"
>
For example, LS1 1AB
</
div
>
<
input
class
=
"nhsuk-input nhsuk-input--width-10"
id
=
"example-with-hint-text"
name
=
"exampleWithHintText"
type
=
"text"
spellcheck
=
"false"
aria-describedby
=
"example-with-hint-text-hint"
autocomplete
=
"postal-code"
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
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name type | Type string | Description Type of input control, for example, an email input control. Defaults to "text" .
Name inputmode | Type string | Description Optional value for the inputmode attribute .
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the text input component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to a text input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the text input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the text input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the text input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the text input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "bday-day" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name pattern | Type string | Description Attribute to provide a regular expression pattern , used to match allowed character combinations for the input value.
Name placeholder | Type string | Description Attribute to provide placeholder text for the input.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the input.
Name autocapitalize | Type string | Description Optional field to enable or disable autocapitalisation of user input. See the Autocapitalization section in the HTML standard for a full list of values that can be used.
Name input Wrapper | Type object | Description If any of prefix , suffix , formGroup.beforeInput or formGroup.afterInput have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.

Name | Type | Description
Name text | Type string | Description Required. Required. If html is set, this is not required. Text to use within the prefix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. Required. If text is set, this is not required. HTML to use within the prefix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the prefix.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the prefix element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the suffix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the suffix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the suffix element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the suffix element.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the text input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the text input component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the wrapping element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the wrapping element.

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
"Enter a full postcode in England"
},
hint
: {
text
:
"For example, LS1 1AB"
},
id
:
"example-with-hint-text"
,
name
:
"exampleWithHintText"
,
width
:
10
,
autocomplete
:
"postal-code"
,
spellcheck
:
false
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### Asking for numbers

#### Whole numbers

If you're asking the user to enter a whole number, set the inputmode attribute to numeric to use the numeric keypad on devices with on-screen keyboards.

- HTML code for text input number

- Nunjucks code for text input number

```text
<
div
class
=
"nhsuk-form-group"
>
<
h1
class
=
"nhsuk-label-wrapper"
>
<
label
class
=
"nhsuk-label nhsuk-label--l"
for
=
"account-number"
>
What is your account number?
</
label
>
</
h1
>
<
div
class
=
"nhsuk-hint"
id
=
"account-number-hint"
>
Must be between 6 and 8 digits long
</
div
>
<
input
class
=
"nhsuk-input nhsuk-input--code nhsuk-input--width-10"
id
=
"account-number"
name
=
"accountNumber"
type
=
"text"
spellcheck
=
"false"
aria-describedby
=
"account-number-hint"
inputmode
=
"numeric"
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
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name type | Type string | Description Type of input control, for example, an email input control. Defaults to "text" .
Name inputmode | Type string | Description Optional value for the inputmode attribute .
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the text input component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to a text input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the text input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the text input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the text input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the text input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "bday-day" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name pattern | Type string | Description Attribute to provide a regular expression pattern , used to match allowed character combinations for the input value.
Name placeholder | Type string | Description Attribute to provide placeholder text for the input.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the input.
Name autocapitalize | Type string | Description Optional field to enable or disable autocapitalisation of user input. See the Autocapitalization section in the HTML standard for a full list of values that can be used.
Name input Wrapper | Type object | Description If any of prefix , suffix , formGroup.beforeInput or formGroup.afterInput have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.

Name | Type | Description
Name text | Type string | Description Required. Required. If html is set, this is not required. Text to use within the prefix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. Required. If text is set, this is not required. HTML to use within the prefix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the prefix.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the prefix element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the suffix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the suffix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the suffix element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the suffix element.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the text input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the text input component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the wrapping element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the wrapping element.

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
"What is your account number?"
,
size
:
"l"
,
isPageHeading
:
true
},
hint
: {
text
:
"Must be between 6 and 8 digits long"
},
id
:
"account-number"
,
name
:
"accountNumber"
,
width
:
10
,
code
:
true
,
inputmode
:
"numeric"
,
spellcheck
:
false
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

You should also follow the GOV.UK Design System guidance and turn off HTML5 validation to prevent browsers from validating the pattern attribute.

The GOV.UK Design System has specific guidance on how to ask for:

- dates

- telephone numbers

#### Decimal numbers

The GOV.UK Design System has guidance on asking for decimal numbers .

### Codes and sequences

Help the user visually check the code they've typed is correct by slightly increasing the spacing between characters. Do this by adding the nhsuk-input--code class to the input to make the input text use a monospace font. This is important if you're asking the user to enter a code or sequence they're unlikely to remember, such as an NHS number , booking reference or security code.

You do not need to do this for memorable information, such as phone numbers and postcodes.

- HTML code for text input codes and sequences

- Nunjucks code for text input codes and sequences

```text
<
div
class
=
"nhsuk-form-group"
>
<
h1
class
=
"nhsuk-label-wrapper"
>
<
label
class
=
"nhsuk-label nhsuk-label--l"
for
=
"nhs-number"
>
What is your NHS number?
</
label
>
</
h1
>
<
div
class
=
"nhsuk-hint"
id
=
"nhs-number-hint"
>
This is a 10 digit number (like
<
span
class
=
"nhsuk-u-nowrap"
>
999 123 4567
</
span
>
) that you can find on an NHS letter, prescription or in the NHS App
</
div
>
<
input
class
=
"nhsuk-input nhsuk-input--code nhsuk-input--width-10"
id
=
"nhs-number"
name
=
"nhs-number"
type
=
"text"
spellcheck
=
"false"
value
=
"999 123 4567"
aria-describedby
=
"nhs-number-hint"
inputmode
=
"numeric"
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
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name type | Type string | Description Type of input control, for example, an email input control. Defaults to "text" .
Name inputmode | Type string | Description Optional value for the inputmode attribute .
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the text input component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to a text input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the text input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the text input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the text input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the text input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "bday-day" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name pattern | Type string | Description Attribute to provide a regular expression pattern , used to match allowed character combinations for the input value.
Name placeholder | Type string | Description Attribute to provide placeholder text for the input.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the input.
Name autocapitalize | Type string | Description Optional field to enable or disable autocapitalisation of user input. See the Autocapitalization section in the HTML standard for a full list of values that can be used.
Name input Wrapper | Type object | Description If any of prefix , suffix , formGroup.beforeInput or formGroup.afterInput have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.

Name | Type | Description
Name text | Type string | Description Required. Required. If html is set, this is not required. Text to use within the prefix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. Required. If text is set, this is not required. HTML to use within the prefix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the prefix.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the prefix element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the suffix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the suffix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the suffix element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the suffix element.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the text input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the text input component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the wrapping element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the wrapping element.

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
"input/macro.njk"
import
input
%}
{%
set
dummyNhsNumber
=
"999 123 4567"
%}
{{
input
({
label
: {
text
:
"What is your NHS number?"
,
size
:
"l"
,
isPageHeading
:
true
},
hint
: {
html
:
'This is a 10 digit number (like <span class="nhsuk-u-nowrap">'
~ dummyNhsNumber ~
'</span>) that you can find on an NHS letter, prescription or in the NHS App'
},
id
:
"nhs-number"
,
name
:
"nhs-number"
,
value
: dummyNhsNumber,
width
:
10
,
code
:
true
,
inputmode
:
"numeric"
,
spellcheck
:
false
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### Prefixes and suffixes

Use prefixes and suffixes to help users enter things like currencies and measurements.

- HTML code for text input prefix and suffix

- Nunjucks code for text input prefix and suffix

```text
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
"nhsuk-label"
for
=
"cost-per-item"
>
Cost per item, in pounds
</
label
>
<
div
class
=
"nhsuk-input-wrapper"
>
<
div
class
=
"nhsuk-input-wrapper__prefix"
aria-hidden
=
"true"
>
£
</
div
>
<
input
class
=
"nhsuk-input nhsuk-input--width-5"
id
=
"cost-per-item"
name
=
"costPerItem"
type
=
"text"
spellcheck
=
"false"
>
<
div
class
=
"nhsuk-input-wrapper__suffix"
aria-hidden
=
"true"
>
per item
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name type | Type string | Description Type of input control, for example, an email input control. Defaults to "text" .
Name inputmode | Type string | Description Optional value for the inputmode attribute .
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the text input component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to a text input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the text input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the text input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the text input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the text input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "bday-day" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name pattern | Type string | Description Attribute to provide a regular expression pattern , used to match allowed character combinations for the input value.
Name placeholder | Type string | Description Attribute to provide placeholder text for the input.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the input.
Name autocapitalize | Type string | Description Optional field to enable or disable autocapitalisation of user input. See the Autocapitalization section in the HTML standard for a full list of values that can be used.
Name input Wrapper | Type object | Description If any of prefix , suffix , formGroup.beforeInput or formGroup.afterInput have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.

Name | Type | Description
Name text | Type string | Description Required. Required. If html is set, this is not required. Text to use within the prefix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. Required. If text is set, this is not required. HTML to use within the prefix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the prefix.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the prefix element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the suffix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the suffix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the suffix element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the suffix element.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the text input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the text input component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the wrapping element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the wrapping element.

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
"Cost per item, in pounds"
},
prefix
:
"£"
,
suffix
:
"per item"
,
id
:
"cost-per-item"
,
name
:
"costPerItem"
,
width
:
5
,
spellcheck
:
false
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Prefixes and suffixes are useful when there's a commonly understood symbol or abbreviation for the type of information you're asking for. Do not rely on prefixes or suffixes alone, because screen readers will not read them out.

If you need a specific type of information, say so in the input label or hint text as well. For example, put 'Cost, in pounds' in the input label and use the '£' symbol in the prefix.

Position prefixes and suffixes so that they're outside of their input. This is to avoid interfering with some browsers that might insert an icon into the input (for example to show or generate a password).

Some users may miss that the input already has a suffix or prefix, and enter a prefix or suffix into the input. Allow for this in your validation and do not show an error.

#### Text inputs with a prefix

- HTML code for text input prefix

- Nunjucks code for text input prefix

```text
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
"nhsuk-label"
for
=
"cost-pounds"
>
Cost in pounds
</
label
>
<
div
class
=
"nhsuk-input-wrapper"
>
<
div
class
=
"nhsuk-input-wrapper__prefix"
aria-hidden
=
"true"
>
£
</
div
>
<
input
class
=
"nhsuk-input nhsuk-input--width-5"
id
=
"cost-pounds"
name
=
"costPounds"
type
=
"text"
spellcheck
=
"false"
>
</
div
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
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name type | Type string | Description Type of input control, for example, an email input control. Defaults to "text" .
Name inputmode | Type string | Description Optional value for the inputmode attribute .
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the text input component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to a text input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the text input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the text input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the text input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the text input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "bday-day" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name pattern | Type string | Description Attribute to provide a regular expression pattern , used to match allowed character combinations for the input value.
Name placeholder | Type string | Description Attribute to provide placeholder text for the input.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the input.
Name autocapitalize | Type string | Description Optional field to enable or disable autocapitalisation of user input. See the Autocapitalization section in the HTML standard for a full list of values that can be used.
Name input Wrapper | Type object | Description If any of prefix , suffix , formGroup.beforeInput or formGroup.afterInput have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.

Name | Type | Description
Name text | Type string | Description Required. Required. If html is set, this is not required. Text to use within the prefix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. Required. If text is set, this is not required. HTML to use within the prefix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the prefix.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the prefix element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the suffix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the suffix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the suffix element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the suffix element.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the text input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the text input component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the wrapping element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the wrapping element.

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
"Cost in pounds"
},
prefix
:
"£"
,
id
:
"cost-pounds"
,
name
:
"costPounds"
,
width
:
5
,
spellcheck
:
false
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

#### Text inputs with a suffix

- HTML code for text input suffix

- Nunjucks code for text input suffix

```text
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
"nhsuk-label"
for
=
"weight"
>
Weight in kilograms
</
label
>
<
div
class
=
"nhsuk-input-wrapper"
>
<
input
class
=
"nhsuk-input nhsuk-input--width-5"
id
=
"weight"
name
=
"weight"
type
=
"text"
spellcheck
=
"false"
>
<
div
class
=
"nhsuk-input-wrapper__suffix"
aria-hidden
=
"true"
>
kg
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name type | Type string | Description Type of input control, for example, an email input control. Defaults to "text" .
Name inputmode | Type string | Description Optional value for the inputmode attribute .
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the text input component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to a text input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the text input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the text input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the text input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the text input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "bday-day" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name pattern | Type string | Description Attribute to provide a regular expression pattern , used to match allowed character combinations for the input value.
Name placeholder | Type string | Description Attribute to provide placeholder text for the input.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the input.
Name autocapitalize | Type string | Description Optional field to enable or disable autocapitalisation of user input. See the Autocapitalization section in the HTML standard for a full list of values that can be used.
Name input Wrapper | Type object | Description If any of prefix , suffix , formGroup.beforeInput or formGroup.afterInput have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.

Name | Type | Description
Name text | Type string | Description Required. Required. If html is set, this is not required. Text to use within the prefix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. Required. If text is set, this is not required. HTML to use within the prefix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the prefix.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the prefix element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the suffix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the suffix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the suffix element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the suffix element.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the text input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the text input component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the wrapping element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the wrapping element.

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
"Weight in kilograms"
},
suffix
:
"kg"
,
id
:
"weight"
,
name
:
"weight"
,
width
:
5
,
spellcheck
:
false
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### Error messages

Style error messages like this.

- HTML code for text input error

- Nunjucks code for text input error

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
"full-name"
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
"full-name-error"
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
"nhsuk-input nhsuk-input--error nhsuk-input--width-10"
id
=
"full-name"
name
=
"fullName"
type
=
"text"
aria-describedby
=
"full-name-error"
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
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name type | Type string | Description Type of input control, for example, an email input control. Defaults to "text" .
Name inputmode | Type string | Description Optional value for the inputmode attribute .
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the text input component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to a text input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the text input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the text input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the text input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the text input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "bday-day" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name pattern | Type string | Description Attribute to provide a regular expression pattern , used to match allowed character combinations for the input value.
Name placeholder | Type string | Description Attribute to provide placeholder text for the input.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the input.
Name autocapitalize | Type string | Description Optional field to enable or disable autocapitalisation of user input. See the Autocapitalization section in the HTML standard for a full list of values that can be used.
Name input Wrapper | Type object | Description If any of prefix , suffix , formGroup.beforeInput or formGroup.afterInput have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.

Name | Type | Description
Name text | Type string | Description Required. Required. If html is set, this is not required. Text to use within the prefix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. Required. If text is set, this is not required. HTML to use within the prefix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the prefix.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the prefix element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the suffix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the suffix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the suffix element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the suffix element.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the text input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the text input component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the wrapping element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the wrapping element.

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
"full-name"
,
name
:
"fullName"
,
width
:
10
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

#### If the input has a prefix or a suffix

- HTML code for text input error and prefix and suffix

- Nunjucks code for text input error and prefix and suffix

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
"cost-pounds"
>
Cost per item, in pounds
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
"cost-pounds-error"
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
Enter a cost per item, in pounds
</
span
>
<
div
class
=
"nhsuk-input-wrapper"
>
<
div
class
=
"nhsuk-input-wrapper__prefix"
aria-hidden
=
"true"
>
£
</
div
>
<
input
class
=
"nhsuk-input nhsuk-input--error nhsuk-input--width-5"
id
=
"cost-pounds"
name
=
"costPounds"
type
=
"text"
spellcheck
=
"false"
aria-describedby
=
"cost-pounds-error"
>
<
div
class
=
"nhsuk-input-wrapper__suffix"
aria-hidden
=
"true"
>
per item
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name type | Type string | Description Type of input control, for example, an email input control. Defaults to "text" .
Name inputmode | Type string | Description Optional value for the inputmode attribute .
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the text input component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to a text input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the text input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the text input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the text input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the text input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the text input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "bday-day" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name pattern | Type string | Description Attribute to provide a regular expression pattern , used to match allowed character combinations for the input value.
Name placeholder | Type string | Description Attribute to provide placeholder text for the input.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the input.
Name autocapitalize | Type string | Description Optional field to enable or disable autocapitalisation of user input. See the Autocapitalization section in the HTML standard for a full list of values that can be used.
Name input Wrapper | Type object | Description If any of prefix , suffix , formGroup.beforeInput or formGroup.afterInput have a value, a wrapping element is added around the input and inserted content. This object allows you to customise that wrapping element. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.

Name | Type | Description
Name text | Type string | Description Required. Required. If html is set, this is not required. Text to use within the prefix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. Required. If text is set, this is not required. HTML to use within the prefix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the prefix.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the prefix element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the suffix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the suffix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the suffix element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the suffix element.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the text input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the text input component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the wrapping element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the wrapping element.

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
"Cost per item, in pounds"
},
errorMessage
: {
text
:
"Enter a cost per item, in pounds"
},
prefix
:
"£"
,
suffix
:
"per item"
,
id
:
"cost-pounds"
,
name
:
"costPounds"
,
width
:
5
,
spellcheck
:
false
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Follow:

- our guidance on error messages GOV.UK guidance on error messages for text input

- GOV.UK guidance on error messages for text input

### Do not disable copy and paste

Users often need to copy and paste information into a text input, so do not stop them doing this.

## Research

If you've used text input, please share your user research findings.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: November 2025
