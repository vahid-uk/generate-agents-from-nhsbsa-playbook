# Search input – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/search-input/

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

# Form elements – Search input

Use a search input to help users find something specific by entering a word, phrase or characters.

- HTML code for search input

- Nunjucks code for search input

```text
<
div
class
=
"nhsuk-form-group nhsuk-search-input"
>
<
label
class
=
"nhsuk-label nhsuk-label--s"
for
=
"example"
>
Search
</
label
>
<
div
class
=
"nhsuk-input-wrapper nhsuk-search-input__wrapper"
>
<
input
class
=
"nhsuk-input nhsuk-input--width-10 nhsuk-search-input__input"
id
=
"example"
name
=
"example"
type
=
"search"
autocomplete
=
"off"
>
<
button
class
=
"nhsuk-button nhsuk-button--icon nhsuk-button--small nhsuk-search-input__button"
data-module
=
"nhsuk-button"
type
=
"submit"
aria-label
=
"Search"
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--search"
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
"m20.7 18.9-4.1-4.1a7 7 0 1 0-1.4 1.4l4 4.1a1 1 0 0 0 1.5 0c.4-.4.4-1 0-1.4ZM6 10.6a5 5 0 1 1 10 0 5 5 0 0 1-10 0Z"
/>
</
svg
>
</
button
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
Name type | Type string | Description Type of input control, for example, an email input control. Defaults to "search" .
Name inputmode | Type string | Description Optional value for the inputmode attribute .
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the search input component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to a search input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the search input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the search input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the search input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the search input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the search input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "bday-day" . See the Autofill section in the HTML standard for a full list of attributes that can be used. Default is "off" .
Name placeholder | Type string | Description Attribute to provide placeholder text for the search input.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the search input.
Name autocapitalize | Type string | Description Optional field to enable or disable autocapitalisation of user input. See the Autocapitalization section in the HTML standard for a full list of values that can be used.
Name input Wrapper | Type object | Description Additional options for the wrapping element containing the search input component. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.
Name button | Type object | Description Optional object allowing customisation of the search button. See button macro options using button component macro .

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
Name before Input | Type object | Description Content to add before the input used by the search input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the search input component. See macro options for form Group after Input .

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
Name variant | Type string | Description Optional variant of search button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name classes | Type string | Description Classes to add to the search button.
Name aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when only an icon is used.
Name icon | Type object | Description Can be used to add an icon to the search button. See macro options for button icon .

Name | Type | Description
Name name | Type string | Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" .
Name html | Type string | Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored.
Name placement | Type string | Description Required. Placement of the icon within the button – "start" or "end" .

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
"search-input/macro.njk"
import
searchInput
%}
{{
searchInput
({
label
: {
text
:
"Search"
,
size
:
"s"
},
name
:
"example"
,
id
:
"example"
,
width
:
10
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

## When to use search input

Use the search input component to help users find a topic, person, task, place or other type of record when navigation alone is not practical.

You can enable search in the header component . Use this to provide a global search.

## When not to use search input

Do not rely on search in place of a well-structured information architecture and navigation.

## How to use search input

When a user types into the input, a cross icon button appears which allows users to clear the input. This is an enhancement for browsers that support it. Some browsers such as Firefox will not show it.

- HTML code for search input nhs number

- Nunjucks code for search input nhs number

```text
<
div
class
=
"nhsuk-form-group nhsuk-search-input"
>
<
label
class
=
"nhsuk-label nhsuk-label--m"
for
=
"example"
>
Search patients
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
"example-hint"
>
Search by name, NHS number, postcode, or date of birth
</
div
>
<
div
class
=
"nhsuk-input-wrapper nhsuk-search-input__wrapper"
>
<
input
class
=
"nhsuk-input nhsuk-input--width-10 nhsuk-search-input__input"
id
=
"example"
name
=
"example"
type
=
"search"
value
=
"LS1 4AP"
aria-describedby
=
"example-hint"
autocomplete
=
"off"
>
<
button
class
=
"nhsuk-button nhsuk-button--icon nhsuk-button--small nhsuk-search-input__button"
data-module
=
"nhsuk-button"
type
=
"submit"
aria-label
=
"Search"
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--search"
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
"m20.7 18.9-4.1-4.1a7 7 0 1 0-1.4 1.4l4 4.1a1 1 0 0 0 1.5 0c.4-.4.4-1 0-1.4ZM6 10.6a5 5 0 1 1 10 0 5 5 0 0 1-10 0Z"
/>
</
svg
>
</
button
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
Name type | Type string | Description Type of input control, for example, an email input control. Defaults to "search" .
Name inputmode | Type string | Description Optional value for the inputmode attribute .
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the search input component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to a search input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the search input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the search input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the search input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the search input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the search input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "bday-day" . See the Autofill section in the HTML standard for a full list of attributes that can be used. Default is "off" .
Name placeholder | Type string | Description Attribute to provide placeholder text for the search input.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the search input.
Name autocapitalize | Type string | Description Optional field to enable or disable autocapitalisation of user input. See the Autocapitalization section in the HTML standard for a full list of values that can be used.
Name input Wrapper | Type object | Description Additional options for the wrapping element containing the search input component. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.
Name button | Type object | Description Optional object allowing customisation of the search button. See button macro options using button component macro .

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
Name before Input | Type object | Description Content to add before the input used by the search input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the search input component. See macro options for form Group after Input .

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
Name variant | Type string | Description Optional variant of search button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name classes | Type string | Description Classes to add to the search button.
Name aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when only an icon is used.
Name icon | Type object | Description Can be used to add an icon to the search button. See macro options for button icon .

Name | Type | Description
Name name | Type string | Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" .
Name html | Type string | Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored.
Name placement | Type string | Description Required. Placement of the icon within the button – "start" or "end" .

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
"search-input/macro.njk"
import
searchInput
%}
{{
searchInput
({
label
: {
text
:
"Search patients"
,
size
:
"m"
},
hint
: {
text
:
"Search by name, NHS number, postcode, or date of birth"
},
id
:
"example"
,
name
:
"example"
,
value
:
"LS1 4AP"
,
width
:
10
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

The search button can include a text label, for example "Find".

Depending on the hierarchy of the page, the search input can use a secondary button.

- HTML code for search input secondary button

- Nunjucks code for search input secondary button

```text
<
div
class
=
"nhsuk-form-group nhsuk-search-input"
>
<
label
class
=
"nhsuk-label nhsuk-label--m"
for
=
"example"
>
Find a patient by NHS number
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
"example-hint"
>
For example
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
</
div
>
<
div
class
=
"nhsuk-input-wrapper nhsuk-search-input__wrapper"
>
<
input
class
=
"nhsuk-input nhsuk-input--code nhsuk-input--width-10 nhsuk-search-input__input"
id
=
"example"
name
=
"example"
type
=
"search"
aria-describedby
=
"example-hint"
autocomplete
=
"off"
>
<
button
class
=
"nhsuk-button nhsuk-button--secondary nhsuk-button--icon nhsuk-button--small nhsuk-search-input__button"
data-module
=
"nhsuk-button"
type
=
"submit"
aria-label
=
"Search"
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--search"
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
"m20.7 18.9-4.1-4.1a7 7 0 1 0-1.4 1.4l4 4.1a1 1 0 0 0 1.5 0c.4-.4.4-1 0-1.4ZM6 10.6a5 5 0 1 1 10 0 5 5 0 0 1-10 0Z"
/>
</
svg
>
<
span
class
=
"nhsuk-button__content"
>
Find
</
span
>
</
button
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
Name type | Type string | Description Type of input control, for example, an email input control. Defaults to "search" .
Name inputmode | Type string | Description Optional value for the inputmode attribute .
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the search input component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to a search input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the search input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the search input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the search input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the search input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the search input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "bday-day" . See the Autofill section in the HTML standard for a full list of attributes that can be used. Default is "off" .
Name placeholder | Type string | Description Attribute to provide placeholder text for the search input.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the search input.
Name autocapitalize | Type string | Description Optional field to enable or disable autocapitalisation of user input. See the Autocapitalization section in the HTML standard for a full list of values that can be used.
Name input Wrapper | Type object | Description Additional options for the wrapping element containing the search input component. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.
Name button | Type object | Description Optional object allowing customisation of the search button. See button macro options using button component macro .

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
Name before Input | Type object | Description Content to add before the input used by the search input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the search input component. See macro options for form Group after Input .

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
Name variant | Type string | Description Optional variant of search button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name classes | Type string | Description Classes to add to the search button.
Name aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when only an icon is used.
Name icon | Type object | Description Can be used to add an icon to the search button. See macro options for button icon .

Name | Type | Description
Name name | Type string | Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" .
Name html | Type string | Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored.
Name placement | Type string | Description Required. Placement of the icon within the button – "start" or "end" .

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
"search-input/macro.njk"
import
searchInput
%}
{{
searchInput
({
label
: {
text
:
"Find a patient by NHS number"
,
size
:
"m"
},
hint
: {
html
:
'For example <span class="nhsuk-u-nowrap">999 123 4567</span>'
},
id
:
"example"
,
name
:
"example"
,
width
:
10
,
code
:
true
,
button
: {
text
:
"Find"
,
variant
:
"secondary"
}
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

The search input can be large, depending on the context of the page. For example, you can use a large input on a dedicated search page.

- HTML code for search input large

- Nunjucks code for search input large

```text
<
div
class
=
"nhsuk-form-group nhsuk-search-input nhsuk-search-input--large"
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
Search
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
"nhsuk-input-wrapper nhsuk-input-wrapper--large nhsuk-search-input__wrapper"
>
<
input
class
=
"nhsuk-input nhsuk-input--large nhsuk-input--width-20 nhsuk-search-input__input"
id
=
"example"
name
=
"example"
type
=
"search"
autocomplete
=
"off"
>
<
button
class
=
"nhsuk-button nhsuk-button--icon nhsuk-search-input__button"
data-module
=
"nhsuk-button"
type
=
"submit"
aria-label
=
"Search"
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--search"
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
"m20.7 18.9-4.1-4.1a7 7 0 1 0-1.4 1.4l4 4.1a1 1 0 0 0 1.5 0c.4-.4.4-1 0-1.4ZM6 10.6a5 5 0 1 1 10 0 5 5 0 0 1-10 0Z"
/>
</
svg
>
</
button
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
Name type | Type string | Description Type of input control, for example, an email input control. Defaults to "search" .
Name inputmode | Type string | Description Optional value for the inputmode attribute .
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the search input component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to a search input component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the search input component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the search input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the search input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the search input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the search input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose , for instance "bday-day" . See the Autofill section in the HTML standard for a full list of attributes that can be used. Default is "off" .
Name placeholder | Type string | Description Attribute to provide placeholder text for the search input.
Name spellcheck | Type boolean | Description Optional field to enable or disable the spellcheck attribute on the search input.
Name autocapitalize | Type string | Description Optional field to enable or disable autocapitalisation of user input. See the Autocapitalization section in the HTML standard for a full list of values that can be used.
Name input Wrapper | Type object | Description Additional options for the wrapping element containing the search input component. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.
Name button | Type object | Description Optional object allowing customisation of the search button. See button macro options using button component macro .

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
Name before Input | Type object | Description Content to add before the input used by the search input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the search input component. See macro options for form Group after Input .

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
Name variant | Type string | Description Optional variant of search button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name classes | Type string | Description Classes to add to the search button.
Name aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when only an icon is used.
Name icon | Type object | Description Can be used to add an icon to the search button. See macro options for button icon .

Name | Type | Description
Name name | Type string | Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" .
Name html | Type string | Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored.
Name placement | Type string | Description Required. Placement of the icon within the button – "start" or "end" .

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
"search-input/macro.njk"
import
searchInput
%}
{{
searchInput
({
label
: {
text
:
"Search"
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
"example"
,
id
:
"example"
,
large
:
true
,
width
:
20
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
