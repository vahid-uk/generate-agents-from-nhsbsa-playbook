# File upload – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/file-upload/

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

# Form elements – File upload

Help users select and upload a file.

- HTML code for file upload

- Nunjucks code for file upload

```text
<
div
class
=
"nhsuk-form-group nhsuk-file-upload"
data-module
=
"nhsuk-file-upload"
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
"file-hint"
>
Upload a file
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
"nhsuk-file-upload__input"
id
=
"file-hint"
name
=
"file-hint"
type
=
"file"
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
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name disabled | Type boolean | Description If true , file input will be disabled.
Name multiple | Type boolean | Description If true , a user may select multiple files at the same time. The exact mechanism to do this differs depending on operating system.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the file upload component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to the file upload component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the file upload component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the file upload component. See macro options for form Group .
Name choose Files Button Class List | Type array | Description Classes to add to the button that opens the file picker. Default is ["nhsuk-button--secondary"] .
Name choose Files Button Text | Type string | Description The text of the button that opens the file picker. Default is "Choose file" .
Name drop Instruction Text | Type string | Description The text informing users they can drop files. Default is "or drop file" .
Name multiple Files Chosen Text | Type object | Description The text displayed when multiple files have been chosen by the user. The component will replace the %{count} placeholder with the number of files selected. Our pluralisation rules apply to this macro option .
Name no File Chosen Text | Type string | Description The text displayed when no file has been chosen by the user. Default is "No file chosen" .
Name entered Drop Zone Text | Type string | Description The text announced by assistive technology when user drags files and enters the drop zone. Default is "Entered drop zone" .
Name left Drop Zone Text | Type string | Description The text announced by assistive technology when user drags files and leaves the drop zone without dropping. Default is "Left drop zone" .
Name classes | Type string | Description Classes to add to the file upload component.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the file upload component.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the file upload component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the file upload component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

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
"file-upload/macro.njk"
import
fileUpload
%}
{{
fileUpload
({
label
: {
text
:
"Upload a file"
,
size
:
"l"
,
isPageHeading
:
true
},
name
:
"file-hint"
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

## When to use file upload

You should only ask users to upload something if it's critical to the delivery of your service.

Read a blog post about design tips for uploading things (GOV.UK) .

## How to use file upload

To upload a file, the user can either:

- use the "Choose file" button

- drag and drop a file into the file upload input area

### Let users reuse uploaded files

Make sure users can easily reuse a previously uploaded file within a single journey, unless doing so would be a major security or privacy concern.

For example, a user might need to upload a photo of their driving licence to prove their identity, and again to prove their address.

You can make it easier for the user to reuse a file by showing it as an option for the user to select. Consider users on public devices before choosing to make the file available to preview or download.

- HTML code for file upload second

- Nunjucks code for file upload second

```text
<
div
class
=
"nhsuk-form-group nhsuk-file-upload"
data-module
=
"nhsuk-file-upload"
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
"file-hint"
>
Upload a file
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
"nhsuk-file-upload__input"
id
=
"file-hint"
name
=
"file-hint"
type
=
"file"
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
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name disabled | Type boolean | Description If true , file input will be disabled.
Name multiple | Type boolean | Description If true , a user may select multiple files at the same time. The exact mechanism to do this differs depending on operating system.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the file upload component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to the file upload component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the file upload component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the file upload component. See macro options for form Group .
Name choose Files Button Class List | Type array | Description Classes to add to the button that opens the file picker. Default is ["nhsuk-button--secondary"] .
Name choose Files Button Text | Type string | Description The text of the button that opens the file picker. Default is "Choose file" .
Name drop Instruction Text | Type string | Description The text informing users they can drop files. Default is "or drop file" .
Name multiple Files Chosen Text | Type object | Description The text displayed when multiple files have been chosen by the user. The component will replace the %{count} placeholder with the number of files selected. Our pluralisation rules apply to this macro option .
Name no File Chosen Text | Type string | Description The text displayed when no file has been chosen by the user. Default is "No file chosen" .
Name entered Drop Zone Text | Type string | Description The text announced by assistive technology when user drags files and enters the drop zone. Default is "Entered drop zone" .
Name left Drop Zone Text | Type string | Description The text announced by assistive technology when user drags files and leaves the drop zone without dropping. Default is "Left drop zone" .
Name classes | Type string | Description Classes to add to the file upload component.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the file upload component.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the file upload component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the file upload component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

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
"file-upload/macro.njk"
import
fileUpload
%}
{{
fileUpload
({
label
: {
text
:
"Upload a file"
,
size
:
"l"
,
isPageHeading
:
true
},
name
:
"file-hint"
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### Changing the button text

You can change the text on the button and in the "No file chosen" message. This text is changeable so you can translate it or be specific about the file to upload.

Keep the text as short as possible. Screen reader users, for example, might find it difficult to use the component if the text is too long.

All the text in the component can be translated to match the language of the page content when JavaScript is running.

### Error messages

Style error messages like this.

- HTML code for file upload error message

- Nunjucks code for file upload error message

```text
<
div
class
=
"nhsuk-form-group nhsuk-form-group--error nhsuk-file-upload"
data-module
=
"nhsuk-file-upload"
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
"file-hint"
>
Upload a file
</
label
>
</
h1
>
<
span
class
=
"nhsuk-error-message"
id
=
"file-hint-error"
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
The CSV must be smaller than 2MB
</
span
>
<
input
class
=
"nhsuk-file-upload__input"
id
=
"file-hint"
name
=
"file-hint"
type
=
"file"
aria-describedby
=
"file-hint-error"
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
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name disabled | Type boolean | Description If true , file input will be disabled.
Name multiple | Type boolean | Description If true , a user may select multiple files at the same time. The exact mechanism to do this differs depending on operating system.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the file upload component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to the file upload component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the file upload component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the file upload component. See macro options for form Group .
Name choose Files Button Class List | Type array | Description Classes to add to the button that opens the file picker. Default is ["nhsuk-button--secondary"] .
Name choose Files Button Text | Type string | Description The text of the button that opens the file picker. Default is "Choose file" .
Name drop Instruction Text | Type string | Description The text informing users they can drop files. Default is "or drop file" .
Name multiple Files Chosen Text | Type object | Description The text displayed when multiple files have been chosen by the user. The component will replace the %{count} placeholder with the number of files selected. Our pluralisation rules apply to this macro option .
Name no File Chosen Text | Type string | Description The text displayed when no file has been chosen by the user. Default is "No file chosen" .
Name entered Drop Zone Text | Type string | Description The text announced by assistive technology when user drags files and enters the drop zone. Default is "Entered drop zone" .
Name left Drop Zone Text | Type string | Description The text announced by assistive technology when user drags files and leaves the drop zone without dropping. Default is "Left drop zone" .
Name classes | Type string | Description Classes to add to the file upload component.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the file upload component.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the file upload component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the file upload component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

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
"file-upload/macro.njk"
import
fileUpload
%}
{{
fileUpload
({
label
: {
text
:
"Upload a file"
,
size
:
"l"
,
isPageHeading
:
true
},
errorMessage
: {
text
:
"The CSV must be smaller than 2MB"
},
name
:
"file-hint"
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Make sure errors follow the guidance in the error message component and have specific error messages for specific error states.

#### If no file has been selected

Say "Select a [whatever they need to select]".

For example, "Select a report".

#### If the file is the wrong file type

Say "The selected file must be a [list of file types]".

For example, "The selected file must be a CSV" or "The selected file must be a JPG, BMP, PNG, TIF or PDF".

#### If the file is too big

Say "The selected file must be smaller than [largest file size]".

For example, "The selected file must be smaller than 2MB".

#### If the file is empty

Say "The selected file is empty". If the file contains a virus Say "The selected file contains a virus". If the file is password protected Say "The selected file is password protected". If there was a problem and the file was not uploaded Say "The selected file could not be uploaded – try again". If there is a limit on how many files the user can select Say "You can only select up to [highest number] files at the same time". For example, "You can only select up to 10 files at the same time". If the file is not in a template that must be used or the template has been changed Say "The selected file must use the template". Accessibility Users of Dragon, a speech recognition tool, may not be able to interact with the component until they have first interacted with another part of the page. For example they could click the mouse in an empty area or they could say "press tab" to move the focus. After that, the Dragon user should be able to interact successfully with the file upload component. If they need to use the component more than once (for example, to correct a mistake), they may need to perform another action again before using it. Progressive enhancement The file upload component uses progressive enhancement and requires JavaScript for enhanced functionality. When JavaScript is not available, users will see their browser's native file input. Open this example in a new tab : file upload without javascript Toggle JavaScript On | Off Research This component is based on GOV.UK's March 2025 file upload component. Help us improve this guidance Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public. Feed back or share insights on GitHub Read more about how to feed back or share insights . If you have any questions, get in touch with the service manual team. Updates to this page Updated: January 2026

#### If the file contains a virus

Say "The selected file contains a virus".

#### If the file is password protected

Say "The selected file is password protected".

#### If there was a problem and the file was not uploaded

Say "The selected file could not be uploaded – try again". If there is a limit on how many files the user can select Say "You can only select up to [highest number] files at the same time". For example, "You can only select up to 10 files at the same time". If the file is not in a template that must be used or the template has been changed Say "The selected file must use the template". Accessibility Users of Dragon, a speech recognition tool, may not be able to interact with the component until they have first interacted with another part of the page. For example they could click the mouse in an empty area or they could say "press tab" to move the focus. After that, the Dragon user should be able to interact successfully with the file upload component. If they need to use the component more than once (for example, to correct a mistake), they may need to perform another action again before using it. Progressive enhancement The file upload component uses progressive enhancement and requires JavaScript for enhanced functionality. When JavaScript is not available, users will see their browser's native file input. Open this example in a new tab : file upload without javascript Toggle JavaScript On | Off Research This component is based on GOV.UK's March 2025 file upload component. Help us improve this guidance Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public. Feed back or share insights on GitHub Read more about how to feed back or share insights . If you have any questions, get in touch with the service manual team. Updates to this page Updated: January 2026

#### If there is a limit on how many files the user can select

Say "You can only select up to [highest number] files at the same time".

For example, "You can only select up to 10 files at the same time".

#### If the file is not in a template that must be used or the template has been changed

Say "The selected file must use the template".

## Accessibility

Users of Dragon, a speech recognition tool, may not be able to interact with the component until they have first interacted with another part of the page. For example they could click the mouse in an empty area or they could say "press tab" to move the focus. After that, the Dragon user should be able to interact successfully with the file upload component.

If they need to use the component more than once (for example, to correct a mistake), they may need to perform another action again before using it.

## Progressive enhancement

The file upload component uses progressive enhancement and requires JavaScript for enhanced functionality.

When JavaScript is not available, users will see their browser's native file input.

## Research

This component is based on GOV.UK's March 2025 file upload component.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: January 2026
