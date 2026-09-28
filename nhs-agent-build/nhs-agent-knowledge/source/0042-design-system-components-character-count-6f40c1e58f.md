# Character count – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/character-count/

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

# Form elements – Character count

Help users know how much text they can enter when there is a limit on the number of characters.

- HTML code for character count

- Nunjucks code for character count

```text
<
div
class
=
"nhsuk-form-group nhsuk-character-count"
data-module
=
"nhsuk-character-count"
data-maxlength
=
"200"
data-count-type
=
"characters"
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
"more-detail"
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
"more-detail-hint"
>
For example, if you use crutches, sticks, or a walking frame
</
div
>
<
textarea
class
=
"nhsuk-textarea nhsuk-js-character-count"
id
=
"more-detail"
name
=
"moreDetail"
rows
=
"5"
aria-describedby
=
"more-detail-info more-detail-hint"
>
</
textarea
>
<
div
class
=
"nhsuk-hint nhsuk-character-count__message"
id
=
"more-detail-info"
>
You can enter up to 200 characters
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
Name id | Type string | Description The ID of the textarea. Defaults to the value of name .
Name name | Type string | Description Required. The name of the textarea, which is submitted with the form data.
Name rows | Type string | Description Optional number of textarea rows (default is 5 rows).
Name value | Type string | Description Optional initial value of the textarea.
Name maxlength | Type string | Description Required. The maximum number of characters (or words if countType is set to "words" ).
Name maxwords | Type string | Description Deprecated in 10.5.0 (see GitHub) . Required. Replaced by the maxlength and countType: "words" options.
Name count Type | Type string | Description The count type used to count the text – "length" or "words" . Defaults to "length" .
Name threshold | Type string | Description The percentage value of the limit at which point the count message is displayed. If this attribute is set, the count message will be hidden by default.
Name label | Type object | Description Required. The label used by the character count component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to the character count component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the character count component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the character count component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the textarea.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the textarea.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the character count.
Name disabled | Type boolean | Description If true , textarea will be disabled.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "street-address" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name count Message | Type object | Description Additional options for the count message used by the character count component. See macro options for count Message .
Name textarea Description Text | Type string | Description Message made available to assistive technologies to describe that the component accepts only a limited amount of content. It is visible on the page if countType is not supported or JavaScript is unavailable. The component will replace the %{count} placeholder with the value of the maxlength option.
Name characters Under Limit Text | Type object | Description Message displayed when the number of characters is under the configured maximum, maxlength . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of remaining characters. Our pluralisation rules apply to this macro option
Name characters At Limit Text | Type string | Description Message displayed when the number of characters reaches the configured maximum, maxlength . This message is displayed visually and through assistive technologies.
Name characters Over Limit Text | Type object | Description Message displayed when the number of characters is over the configured maximum, maxlength . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of characters above the maximum. Our pluralisation rules apply to this macro option
Name words Under Limit Text | Type object | Description Message displayed when the number of words is under the configured maximum, maxlength with countType: "words" . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of remaining words. Our pluralisation rules apply to this macro option
Name words At Limit Text | Type string | Description Message displayed when the number of words reaches the configured maximum, maxlength with countType: "words" . This message is displayed visually and through assistive technologies.
Name words Over Limit Text | Type object | Description Message displayed when the number of words is over the configured maximum, maxlength with countType: "words" . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of words above the maximum. Our pluralisation rules apply to this macro option

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the textarea used by the character count component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the textarea used by the character count component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the textarea. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the textarea. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the textarea. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the textarea. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the count message.

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
"character-count/macro.njk"
import
characterCount
%}
{{
characterCount
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
"more-detail"
,
name
:
"moreDetail"
,
maxlength
:
200
,
countType
:
"characters"
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

## When to use character count

Always test your service without a character count first.

Do not use the character count component unless there is a good reason for limiting the number of characters users can enter. For example, if there is:

- evidence that users are likely to enter more information than they need to

- a legal or technical reason that means an entry must be no more than a certain number of characters

## When not to use character count

If your users keep hitting the character limit imposed by the backend of your service, try to increase the limit rather than use a character count.

### Important: Before using character count

Consider the risks around using open text boxes, especially in public services. Read about when to use textarea .

## How to use character count

### How it works

The component tells users how many characters they have remaining as they type into a textarea with a character limit.

Users will get updates at a pace that works best for the way they interact with the textarea. This means:

- sighted users will see a count message that updates as they type

- screen reader users will hear the count announcement when they stop typing

This component does not stop the user entering information. The user can enter more than the character limit, but they're told they've entered too many characters. This lets them type or copy and paste their full answer, then edit it down.

The count message appears below the textarea so that:

- it's clearly separate from any hint text or error message above the textarea

- if it's below the visible screen area, users will still see it again when they scroll down to send their response

### Consider if a word count is more helpful

In some cases it may be more helpful to show a word count. For example, if your question requires a longer answer.

Do this by setting data-count-type="words" and data-maxlength in the component markup. For example, data-maxlength="150" will set a word limit of 150.

- HTML code for character count word count

- Nunjucks code for character count word count

```text
<
div
class
=
"nhsuk-form-group nhsuk-character-count"
data-module
=
"nhsuk-character-count"
data-maxlength
=
"150"
data-count-type
=
"words"
>
<
label
class
=
"nhsuk-label nhsuk-label--l"
for
=
"more-detail"
>
Enter a job description
</
label
>
<
textarea
class
=
"nhsuk-textarea nhsuk-js-character-count"
id
=
"more-detail"
name
=
"moreDetail"
rows
=
"5"
aria-describedby
=
"more-detail-info"
>
</
textarea
>
<
div
class
=
"nhsuk-hint nhsuk-character-count__message"
id
=
"more-detail-info"
>
You can enter up to 150 words
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
Name id | Type string | Description The ID of the textarea. Defaults to the value of name .
Name name | Type string | Description Required. The name of the textarea, which is submitted with the form data.
Name rows | Type string | Description Optional number of textarea rows (default is 5 rows).
Name value | Type string | Description Optional initial value of the textarea.
Name maxlength | Type string | Description Required. The maximum number of characters (or words if countType is set to "words" ).
Name maxwords | Type string | Description Deprecated in 10.5.0 (see GitHub) . Required. Replaced by the maxlength and countType: "words" options.
Name count Type | Type string | Description The count type used to count the text – "length" or "words" . Defaults to "length" .
Name threshold | Type string | Description The percentage value of the limit at which point the count message is displayed. If this attribute is set, the count message will be hidden by default.
Name label | Type object | Description Required. The label used by the character count component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to the character count component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the character count component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the character count component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the textarea.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the textarea.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the character count.
Name disabled | Type boolean | Description If true , textarea will be disabled.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "street-address" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name count Message | Type object | Description Additional options for the count message used by the character count component. See macro options for count Message .
Name textarea Description Text | Type string | Description Message made available to assistive technologies to describe that the component accepts only a limited amount of content. It is visible on the page if countType is not supported or JavaScript is unavailable. The component will replace the %{count} placeholder with the value of the maxlength option.
Name characters Under Limit Text | Type object | Description Message displayed when the number of characters is under the configured maximum, maxlength . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of remaining characters. Our pluralisation rules apply to this macro option
Name characters At Limit Text | Type string | Description Message displayed when the number of characters reaches the configured maximum, maxlength . This message is displayed visually and through assistive technologies.
Name characters Over Limit Text | Type object | Description Message displayed when the number of characters is over the configured maximum, maxlength . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of characters above the maximum. Our pluralisation rules apply to this macro option
Name words Under Limit Text | Type object | Description Message displayed when the number of words is under the configured maximum, maxlength with countType: "words" . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of remaining words. Our pluralisation rules apply to this macro option
Name words At Limit Text | Type string | Description Message displayed when the number of words reaches the configured maximum, maxlength with countType: "words" . This message is displayed visually and through assistive technologies.
Name words Over Limit Text | Type object | Description Message displayed when the number of words is over the configured maximum, maxlength with countType: "words" . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of words above the maximum. Our pluralisation rules apply to this macro option

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the textarea used by the character count component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the textarea used by the character count component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the textarea. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the textarea. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the textarea. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the textarea. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the count message.

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
"character-count/macro.njk"
import
characterCount
%}
{{
characterCount
({
label
: {
text
:
"Enter a job description"
,
size
:
"l"
},
id
:
"more-detail"
,
name
:
"moreDetail"
,
maxlength
:
150
,
countType
:
"words"
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### Avoid narrow limits

When using a character count, try to set the limit higher than most users will need. Find out what this is by doing user research and data analysis.

If the limit is much higher than most users are likely to reach, you can choose to only display the message after a user has entered a certain amount.

To do this, set a threshold in the component markup. For example, data-threshold="75" will show the count message only when users have entered 75% of the limit.

Screen reader users will hear the character limit when they first interact with a textarea using the threshold option. Sighted users will not see anything until the count message is shown, though you might choose to include the character limit in the hint text.

- HTML code for character count threshold

- Nunjucks code for character count threshold

```text
<
div
class
=
"nhsuk-form-group nhsuk-character-count"
data-module
=
"nhsuk-character-count"
data-maxlength
=
"112"
data-threshold
=
"75"
data-count-type
=
"characters"
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
"threshold"
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
"threshold-hint"
>
For example, if you use crutches, sticks, or a walking frame
</
div
>
<
textarea
class
=
"nhsuk-textarea nhsuk-js-character-count"
id
=
"threshold"
name
=
"threshold"
rows
=
"5"
aria-describedby
=
"threshold-info threshold-hint"
>
Type another letter into this field after this message to see the threshold feature
</
textarea
>
<
div
class
=
"nhsuk-hint nhsuk-character-count__message"
id
=
"threshold-info"
>
You can enter up to 112 characters
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
Name id | Type string | Description The ID of the textarea. Defaults to the value of name .
Name name | Type string | Description Required. The name of the textarea, which is submitted with the form data.
Name rows | Type string | Description Optional number of textarea rows (default is 5 rows).
Name value | Type string | Description Optional initial value of the textarea.
Name maxlength | Type string | Description Required. The maximum number of characters (or words if countType is set to "words" ).
Name maxwords | Type string | Description Deprecated in 10.5.0 (see GitHub) . Required. Replaced by the maxlength and countType: "words" options.
Name count Type | Type string | Description The count type used to count the text – "length" or "words" . Defaults to "length" .
Name threshold | Type string | Description The percentage value of the limit at which point the count message is displayed. If this attribute is set, the count message will be hidden by default.
Name label | Type object | Description Required. The label used by the character count component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to the character count component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the character count component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the character count component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the textarea.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the textarea.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the character count.
Name disabled | Type boolean | Description If true , textarea will be disabled.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "street-address" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name count Message | Type object | Description Additional options for the count message used by the character count component. See macro options for count Message .
Name textarea Description Text | Type string | Description Message made available to assistive technologies to describe that the component accepts only a limited amount of content. It is visible on the page if countType is not supported or JavaScript is unavailable. The component will replace the %{count} placeholder with the value of the maxlength option.
Name characters Under Limit Text | Type object | Description Message displayed when the number of characters is under the configured maximum, maxlength . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of remaining characters. Our pluralisation rules apply to this macro option
Name characters At Limit Text | Type string | Description Message displayed when the number of characters reaches the configured maximum, maxlength . This message is displayed visually and through assistive technologies.
Name characters Over Limit Text | Type object | Description Message displayed when the number of characters is over the configured maximum, maxlength . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of characters above the maximum. Our pluralisation rules apply to this macro option
Name words Under Limit Text | Type object | Description Message displayed when the number of words is under the configured maximum, maxlength with countType: "words" . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of remaining words. Our pluralisation rules apply to this macro option
Name words At Limit Text | Type string | Description Message displayed when the number of words reaches the configured maximum, maxlength with countType: "words" . This message is displayed visually and through assistive technologies.
Name words Over Limit Text | Type object | Description Message displayed when the number of words is over the configured maximum, maxlength with countType: "words" . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of words above the maximum. Our pluralisation rules apply to this macro option

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the textarea used by the character count component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the textarea used by the character count component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the textarea. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the textarea. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the textarea. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the textarea. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the count message.

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
"character-count/macro.njk"
import
characterCount
%}
{{
characterCount
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
"threshold"
,
name
:
"threshold"
,
value
:
"Type another letter into this field after this message to see the threshold feature"
,
maxlength
:
112
,
threshold
:
75
,
countType
:
"characters"
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### If you're asking more than 1 question on the page

If you're asking more than 1 question on the page, do not set the contents of the <label> as the page heading. Follow the guidance on asking multiple questions in the question pages pattern .

- HTML code for character count without heading

- Nunjucks code for character count without heading

```text
<
div
class
=
"nhsuk-form-group nhsuk-character-count"
data-module
=
"nhsuk-character-count"
data-maxlength
=
"150"
data-count-type
=
"characters"
>
<
label
class
=
"nhsuk-label"
for
=
"more-detail"
>
Provide more detail about how you move about (your mobility)
</
label
>
<
textarea
class
=
"nhsuk-textarea nhsuk-js-character-count"
id
=
"more-detail"
name
=
"moreDetail"
rows
=
"5"
aria-describedby
=
"more-detail-info"
>
</
textarea
>
<
div
class
=
"nhsuk-hint nhsuk-character-count__message"
id
=
"more-detail-info"
>
You can enter up to 150 characters
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
Name id | Type string | Description The ID of the textarea. Defaults to the value of name .
Name name | Type string | Description Required. The name of the textarea, which is submitted with the form data.
Name rows | Type string | Description Optional number of textarea rows (default is 5 rows).
Name value | Type string | Description Optional initial value of the textarea.
Name maxlength | Type string | Description Required. The maximum number of characters (or words if countType is set to "words" ).
Name maxwords | Type string | Description Deprecated in 10.5.0 (see GitHub) . Required. Replaced by the maxlength and countType: "words" options.
Name count Type | Type string | Description The count type used to count the text – "length" or "words" . Defaults to "length" .
Name threshold | Type string | Description The percentage value of the limit at which point the count message is displayed. If this attribute is set, the count message will be hidden by default.
Name label | Type object | Description Required. The label used by the character count component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to the character count component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the character count component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the character count component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the textarea.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the textarea.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the character count.
Name disabled | Type boolean | Description If true , textarea will be disabled.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "street-address" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name count Message | Type object | Description Additional options for the count message used by the character count component. See macro options for count Message .
Name textarea Description Text | Type string | Description Message made available to assistive technologies to describe that the component accepts only a limited amount of content. It is visible on the page if countType is not supported or JavaScript is unavailable. The component will replace the %{count} placeholder with the value of the maxlength option.
Name characters Under Limit Text | Type object | Description Message displayed when the number of characters is under the configured maximum, maxlength . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of remaining characters. Our pluralisation rules apply to this macro option
Name characters At Limit Text | Type string | Description Message displayed when the number of characters reaches the configured maximum, maxlength . This message is displayed visually and through assistive technologies.
Name characters Over Limit Text | Type object | Description Message displayed when the number of characters is over the configured maximum, maxlength . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of characters above the maximum. Our pluralisation rules apply to this macro option
Name words Under Limit Text | Type object | Description Message displayed when the number of words is under the configured maximum, maxlength with countType: "words" . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of remaining words. Our pluralisation rules apply to this macro option
Name words At Limit Text | Type string | Description Message displayed when the number of words reaches the configured maximum, maxlength with countType: "words" . This message is displayed visually and through assistive technologies.
Name words Over Limit Text | Type object | Description Message displayed when the number of words is over the configured maximum, maxlength with countType: "words" . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of words above the maximum. Our pluralisation rules apply to this macro option

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the textarea used by the character count component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the textarea used by the character count component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the textarea. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the textarea. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the textarea. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the textarea. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the count message.

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
"character-count/macro.njk"
import
characterCount
%}
{{
characterCount
({
label
: {
text
:
"Provide more detail about how you move about (your mobility)"
},
id
:
"more-detail"
,
name
:
"moreDetail"
,
maxlength
:
150
,
countType
:
"characters"
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### Error messages

Style error messages like this.

- HTML code for character count error

- Nunjucks code for character count error

```text
<
div
class
=
"nhsuk-form-group nhsuk-form-group--error nhsuk-character-count"
data-module
=
"nhsuk-character-count"
data-maxlength
=
"350"
data-count-type
=
"characters"
>
<
label
class
=
"nhsuk-label nhsuk-label--l"
for
=
"exceeding"
>
Enter a job description
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
"exceeding-error"
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
Job description must be 350 characters or less
</
span
>
<
textarea
class
=
"nhsuk-textarea nhsuk-textarea--error nhsuk-js-character-count"
id
=
"exceeding"
name
=
"exceedingCharacters"
rows
=
"5"
aria-describedby
=
"exceeding-info exceeding-error"
>
A content designer works on the end-to-end journey of a service to help users complete their goal and government deliver a policy intent. Their work may involve the creation of, or change to, a transaction, product or single piece of content that stretches across digital and offline channels. They make sure appropriate content is shown to a user in the right place and in the best format.
</
textarea
>
<
div
class
=
"nhsuk-hint nhsuk-character-count__message"
id
=
"exceeding-info"
>
You can enter up to 350 characters
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
Name id | Type string | Description The ID of the textarea. Defaults to the value of name .
Name name | Type string | Description Required. The name of the textarea, which is submitted with the form data.
Name rows | Type string | Description Optional number of textarea rows (default is 5 rows).
Name value | Type string | Description Optional initial value of the textarea.
Name maxlength | Type string | Description Required. The maximum number of characters (or words if countType is set to "words" ).
Name maxwords | Type string | Description Deprecated in 10.5.0 (see GitHub) . Required. Replaced by the maxlength and countType: "words" options.
Name count Type | Type string | Description The count type used to count the text – "length" or "words" . Defaults to "length" .
Name threshold | Type string | Description The percentage value of the limit at which point the count message is displayed. If this attribute is set, the count message will be hidden by default.
Name label | Type object | Description Required. The label used by the character count component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to the character count component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the character count component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the character count component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the textarea.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the textarea.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the character count.
Name disabled | Type boolean | Description If true , textarea will be disabled.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "street-address" . See the Autofill section in the HTML standard for a full list of attributes that can be used.
Name count Message | Type object | Description Additional options for the count message used by the character count component. See macro options for count Message .
Name textarea Description Text | Type string | Description Message made available to assistive technologies to describe that the component accepts only a limited amount of content. It is visible on the page if countType is not supported or JavaScript is unavailable. The component will replace the %{count} placeholder with the value of the maxlength option.
Name characters Under Limit Text | Type object | Description Message displayed when the number of characters is under the configured maximum, maxlength . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of remaining characters. Our pluralisation rules apply to this macro option
Name characters At Limit Text | Type string | Description Message displayed when the number of characters reaches the configured maximum, maxlength . This message is displayed visually and through assistive technologies.
Name characters Over Limit Text | Type object | Description Message displayed when the number of characters is over the configured maximum, maxlength . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of characters above the maximum. Our pluralisation rules apply to this macro option
Name words Under Limit Text | Type object | Description Message displayed when the number of words is under the configured maximum, maxlength with countType: "words" . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of remaining words. Our pluralisation rules apply to this macro option
Name words At Limit Text | Type string | Description Message displayed when the number of words reaches the configured maximum, maxlength with countType: "words" . This message is displayed visually and through assistive technologies.
Name words Over Limit Text | Type object | Description Message displayed when the number of words is over the configured maximum, maxlength with countType: "words" . This message is displayed visually and through assistive technologies. The component will replace the %{count} placeholder with the number of words above the maximum. Our pluralisation rules apply to this macro option

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the textarea used by the character count component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the textarea used by the character count component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the textarea. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the textarea. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the textarea. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the textarea. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the count message.

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
"character-count/macro.njk"
import
characterCount
%}
{{
characterCount
({
label
: {
text
:
"Enter a job description"
,
size
:
"l"
},
errorMessage
: {
text
:
"Job description must be 350 characters or less"
},
id
:
"exceeding"
,
name
:
"exceedingCharacters"
,
value
:
"A content designer works on the end-to-end journey of a service to help users complete their goal and government deliver a policy intent. Their work may involve the creation of, or change to, a transaction, product or single piece of content that stretches across digital and offline channels. They make sure appropriate content is shown to a user in the right place and in the best format."
,
maxlength
:
350
,
countType
:
"characters"
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

If a user tries to send their response with too many characters, you must show an error message above the field as well as the count message below it.

The error message tells users what went wrong and how to fix it. The count message provides live feedback and updates as a user types.

The input shows a red border only when the user tries to enter more than the character limit. If the number of characters is within the limit, the input does not show this border even when there's been an error. We felt it might cause the user difficulty if the border disappeared once they started typing.

Make sure errors follow GOV.UK guidance on writing error messages and have specific error messages for specific error states.

#### If the input is empty

Say "Enter [whatever it is]".

For example, "Enter a summary".

#### If the input is too long

Say "[whatever it is] must be [number] characters or less".

For example, "Summary must be 400 characters or less".

## Progressive enhancement

The character count component uses progressive enhancement and requires JavaScript for enhanced functionality.

When JavaScript is not available, users will see a static message in place of the count message, telling them how many characters or words they can enter.

## Research and testing

The Government Digital Service (GDS) developed and tested the character count component. Several NHS services are using a character count but we need to know more about how it tests with users.

### Known issues and gaps

In Internet Explorer 11, JAWS will ignore any set threshold and announce the character count, even if the user entered less than the threshold.

In Chrome version 99, JAWS will not announce the hint or character count of a pre-populated textarea. This is a known issue for the developer of JAWS (FreedomScientific GitHub issue) .

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: August 2026
