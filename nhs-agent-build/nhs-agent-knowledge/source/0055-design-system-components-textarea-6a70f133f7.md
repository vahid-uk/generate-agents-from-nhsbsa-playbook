# Textarea – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/textarea/

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

# Form elements – Textarea

Use textarea to let users enter more than 1 line of text.

- HTML code for textarea

- Nunjucks code for textarea

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
"example"
>
Can you provide more detail about how you move about (your mobility)?
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
"example-hint"
>
For example, if you use crutches, sticks, or a walking frame
</
div
>
<
textarea
class
=
"nhsuk-textarea"
id
=
"example"
name
=
"example"
rows
=
"5"
aria-describedby
=
"example-hint"
>
</
textarea
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
Name id | Type string | Description The ID of the textarea. Defaults to the value of name .
Name name | Type string | Description Required. The name of the textarea, which is submitted with the form data.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the textarea.
Name rows | Type string | Description Optional number of textarea rows (default is 5 rows).
Name value | Type string | Description Optional initial value of the textarea.
Name disabled | Type boolean | Description If true , textarea will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the textarea component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to the textarea component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the textarea component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the textarea component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the textarea.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "street-address" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the textarea.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the textarea used by the textarea component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the textarea used by the textarea component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the textarea. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the textarea. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the textarea. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the textarea. If html is provided, the text option will be ignored.

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
"textarea/macro.njk"
import
textarea
%}
{{
textarea
({
label
: {
text
:
"Can you provide more detail about how you move about (your mobility)?"
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
"For example, if you use crutches, sticks, or a walking frame"
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

## When to use textarea

Use textarea when you want users to enter multiple lines of text.

Use it when you are confident that users will:

- input the information you need

- not input information that could cause clinical or safeguarding concerns, for example, details of medical symptoms or harmful behaviour that your service is not designed to deal with

If you are not sure about this, talk with your clinical team.

### Important: Consider the risks

Before using textarea in public services, look at alternatives.

Textarea can cause problems as users may:

- find open questions difficult to answer

- input information that's difficult to analyse

- disclose personal information, for example, about their symptoms or situation and expect you to reply quickly

They may ignore messages in hint text such as "Do not include personal information like your name, date of birth or NHS number".

Consider other ways to collect the information you need. Use structured, closed questions if possible. For example, let users select from options using radios or checkboxes .

## When not to use textarea

If you want users to enter a single line answer, such as a phone number or name, use text input .

Only use textarea if your team has considered the alternatives and agreed that it's the best way to meet user and business needs.

## How to use textarea

### Understand and manage the risks

Users sometimes use open text boxes to report health concerns or difficult circumstances that are not relevant to your service, even if you ask them not to. Your team must monitor and respond to any clinical safety or safeguarding concerns.

If you cannot do this, it can leave:

- users in unsafe situations

- staff feeling stressed and uncertain what to do

- the organisation facing reputational harm or legal action for not acting on information

Read our guidance on making sure you need each question .

If you use textarea in a public service, make sure you:

- assess the risks

- talk with your clinical and legal teams

- if relevant, set expectations at the start that your service cannot respond to information about an individual's medical situation and signpost to GPs or 111

- make your question as specific as possible and consider setting a character limit

- put in place a process for monitoring and dealing with safety issues, including over weekends and holidays

- set up technical safeguards, for example to detect inappropriate content

Read more about managing clinical risk in NHS service standard 16: Make your service clinically safe .

### Label textareas

You must label textareas.

Do not use placeholder text for a label, as it disappears when users click inside the textarea.

Align labels above the textarea they refer to. Labels should be short, direct and written in sentence case. Do not use colons at the end of labels.

### Use the right size of textarea

Make the height of a textarea proportional to the amount of text you expect users to enter. You can set the height of a textarea by specifying the rows attribute.

- HTML code for textarea right size

- Nunjucks code for textarea right size

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
"example-right-size"
>
Provide a reason for continuing
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
"example-right-size-hint"
>
Explain the clinical decision for continuing despite a recent mammogram
</
div
>
<
textarea
class
=
"nhsuk-textarea"
id
=
"example-right-size"
name
=
"exampleRightSize"
rows
=
"3"
aria-describedby
=
"example-right-size-hint"
>
</
textarea
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
Name id | Type string | Description The ID of the textarea. Defaults to the value of name .
Name name | Type string | Description Required. The name of the textarea, which is submitted with the form data.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the textarea.
Name rows | Type string | Description Optional number of textarea rows (default is 5 rows).
Name value | Type string | Description Optional initial value of the textarea.
Name disabled | Type boolean | Description If true , textarea will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the textarea component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to the textarea component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the textarea component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the textarea component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the textarea.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "street-address" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the textarea.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the textarea used by the textarea component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the textarea used by the textarea component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the textarea. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the textarea. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the textarea. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the textarea. If html is provided, the text option will be ignored.

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
"textarea/macro.njk"
import
textarea
%}
{{
textarea
({
label
: {
text
:
"Provide a reason for continuing"
},
hint
: {
text
:
"Explain the clinical decision for continuing despite a recent mammogram"
},
rows
:
"3"
,
id
:
"example-right-size"
,
name
:
"exampleRightSize"
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

If you are using a large textarea in a public service, with or without character count , be aware that giving users more space may increase clinical risk.

### Using hint text

Use hint text to give users help in context , for example, tell users what information to include or not to include. But bear in mind that users may ignore this, especially in public services.

Read more about hint text .

### Do not disable copy and paste

Users will often need to copy and paste information into a textarea, so do not stop them doing this.

### Error messages

Style error messages like this.

- HTML code for textarea error

- Nunjucks code for textarea error

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
"example-error"
>
Provide a reason for continuing
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
Enter the clinical decision.
</
span
>
<
textarea
class
=
"nhsuk-textarea nhsuk-textarea--error"
id
=
"example-error"
name
=
"exampleError"
rows
=
"3"
aria-describedby
=
"example-error-error"
>
</
textarea
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
Name id | Type string | Description The ID of the textarea. Defaults to the value of name .
Name name | Type string | Description Required. The name of the textarea, which is submitted with the form data.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the textarea.
Name rows | Type string | Description Optional number of textarea rows (default is 5 rows).
Name value | Type string | Description Optional initial value of the textarea.
Name disabled | Type boolean | Description If true , textarea will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the textarea component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to the textarea component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the textarea component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the textarea component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the textarea.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "street-address" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the textarea.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the textarea used by the textarea component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the textarea used by the textarea component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the textarea. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the textarea. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the textarea. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the textarea. If html is provided, the text option will be ignored.

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
"textarea/macro.njk"
import
textarea
%}
{{
textarea
({
label
: {
text
:
"Provide a reason for continuing"
},
errorMessage
: {
text
:
"Enter the clinical decision."
},
rows
:
"3"
,
id
:
"example-error"
,
name
:
"exampleError"
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Follow:

- our guidance on error messages GOV.UK design system guidance on textarea error messages

- GOV.UK design system guidance on textarea error messages

## Research

We tested the textarea component on a "Register with a GP" prototype at 2 labs in December 2018. Users understood the purpose of the textarea and were able to use it.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: September 2025
