# Select – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/select/

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

# Form elements – Select

Use select to let users choose an option from a long list but only use it as a last resort.

- HTML code for select

- Nunjucks code for select

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
"sort-by"
>
Sort by
</
label
>
<
select
class
=
"nhsuk-select"
id
=
"sort-by"
name
=
"sortBy"
>
<
option
value
=
"recently-published"
selected
>
Recently published
</
option
>
<
option
value
=
"recently-updated"
>
Recently updated
</
option
>
<
option
value
=
"most-views"
>
Most views
</
option
>
<
option
value
=
"most-comments"
>
Most comments
</
option
>
</
select
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
Name id | Type string | Description ID for the select. Defaults to the value of name .
Name name | Type string | Description Required. The name attribute for the select.
Name items | Type array | Description Required. The items within the select component. See macro options for items .
Name value | Type string | Description The value for the option which should be selected. Use this as an alternative to setting the selected option on each individual item.
Name disabled | Type boolean | Description If true , select will be disabled. Use the disabled option on each individual item to only disable certain options.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the select component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to the select component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the select component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the select component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the select.
Name input Wrapper | Type object | Description If any of formGroup.beforeInput or formGroup.afterInput have a value, a wrapping element is added around the select and inserted content. This object allows you to customise that wrapping element. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the select.

Name | Type | Description
Name value | Type string | Description The value attribute for the option. If this is omitted, the value is taken from the text content of the option element.
Name text | Type string | Description Required. Text for the option item.
Name divider | Type boolean | Description Divider line used to separate option items.
Name selected | Type boolean | Description Whether the option should be selected when the page loads. Takes precedence over the top-level value option.
Name disabled | Type boolean | Description Sets the option item as disabled.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the option.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the select used by the select component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the select used by the select component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the select. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the select. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the select. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the select. If html is provided, the text option will be ignored.

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
"select/macro.njk"
import
select
%}
{{
select
({
label
: {
text
:
"Sort by"
},
id
:
"sort-by"
,
name
:
"sortBy"
,
value
:
"recently-published"
,
items
: [
    {
value
:
"recently-published"
,
text
:
"Recently published"
},
    {
value
:
"recently-updated"
,
text
:
"Recently updated"
},
    {
value
:
"most-views"
,
text
:
"Most views"
},
    {
value
:
"most-comments"
,
text
:
"Most comments"
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

## When to use select

The select component should only be used as a last resort in public-facing services because research shows that some users find selects very difficult to use.

## When not to use select

The select component allows users to choose an option from a long list. Before using the select component, try asking users other questions which will allow you to present them with fewer options.

Consider using a different solution, such as radios .

## How to use select

If you use the component for settings, you can make an option pre-selected by default when users first see it.

If you use the component for questions, do not pre-select any of the options in case it influences users' answers.

### Select with hint

You can add hint text to help the user understand the options and choose 1 of them.

- HTML code for select with hint

- Nunjucks code for select with hint

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
"nhsuk-label nhsuk-label--s"
for
=
"region"
>
Choose region
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
"region-hint"
>
This can be different to what you selected before
</
div
>
<
select
class
=
"nhsuk-select"
id
=
"region"
name
=
"region"
aria-describedby
=
"region-hint"
>
<
option
value
=
"choose"
selected
>
Choose region
</
option
>
<
option
value
=
"east"
>
East of England
</
option
>
<
option
value
=
"london"
>
London
</
option
>
<
option
value
=
"midlands"
>
Midlands
</
option
>
<
option
value
=
"yorkshire"
>
North East and Yorkshire
</
option
>
<
option
value
=
"northwest"
>
North West
</
option
>
<
option
value
=
"southeast"
>
South East
</
option
>
<
option
value
=
"southeast"
>
South West
</
option
>
</
select
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
Name id | Type string | Description ID for the select. Defaults to the value of name .
Name name | Type string | Description Required. The name attribute for the select.
Name items | Type array | Description Required. The items within the select component. See macro options for items .
Name value | Type string | Description The value for the option which should be selected. Use this as an alternative to setting the selected option on each individual item.
Name disabled | Type boolean | Description If true , select will be disabled. Use the disabled option on each individual item to only disable certain options.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the select component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to the select component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the select component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the select component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the select.
Name input Wrapper | Type object | Description If any of formGroup.beforeInput or formGroup.afterInput have a value, a wrapping element is added around the select and inserted content. This object allows you to customise that wrapping element. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the select.

Name | Type | Description
Name value | Type string | Description The value attribute for the option. If this is omitted, the value is taken from the text content of the option element.
Name text | Type string | Description Required. Text for the option item.
Name divider | Type boolean | Description Divider line used to separate option items.
Name selected | Type boolean | Description Whether the option should be selected when the page loads. Takes precedence over the top-level value option.
Name disabled | Type boolean | Description Sets the option item as disabled.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the option.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the select used by the select component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the select used by the select component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the select. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the select. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the select. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the select. If html is provided, the text option will be ignored.

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
"select/macro.njk"
import
select
%}
{{
select
({
label
: {
text
:
"Choose region"
,
size
:
"s"
},
hint
: {
text
:
"This can be different to what you selected before"
},
id
:
"region"
,
name
:
"region"
,
value
:
"choose"
,
items
: [
    {
value
:
"choose"
,
text
:
"Choose region"
},
    {
value
:
"east"
,
text
:
"East of England"
},
    {
value
:
"london"
,
text
:
"London"
},
    {
value
:
"midlands"
,
text
:
"Midlands"
},
    {
value
:
"yorkshire"
,
text
:
"North East and Yorkshire"
},
    {
value
:
"northwest"
,
text
:
"North West"
},
    {
value
:
"southeast"
,
text
:
"South East"
},
    {
value
:
"southeast"
,
text
:
"South West"
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### Error messages

Display an error message if the user has not selected an option.

Style error messages as shown in the example:

- HTML code for select error

- Nunjucks code for select error

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
"nhsuk-label nhsuk-label--s"
for
=
"region"
>
Choose region
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
"region-hint"
>
This can be different to what you selected before
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
"region-error"
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
Choose a region
</
span
>
<
select
class
=
"nhsuk-select nhsuk-select--error"
id
=
"region"
name
=
"region"
aria-describedby
=
"region-hint region-error"
>
<
option
value
=
"choose"
selected
>
Choose region
</
option
>
<
option
value
=
"east"
>
East of England
</
option
>
<
option
value
=
"london"
>
London
</
option
>
<
option
value
=
"midlands"
>
Midlands
</
option
>
<
option
value
=
"yorkshire"
>
North East and Yorkshire
</
option
>
<
option
value
=
"northwest"
>
North West
</
option
>
<
option
value
=
"southeast"
>
South East
</
option
>
<
option
value
=
"southeast"
>
South West
</
option
>
</
select
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
Name id | Type string | Description ID for the select. Defaults to the value of name .
Name name | Type string | Description Required. The name attribute for the select.
Name items | Type array | Description Required. The items within the select component. See macro options for items .
Name value | Type string | Description The value for the option which should be selected. Use this as an alternative to setting the selected option on each individual item.
Name disabled | Type boolean | Description If true , select will be disabled. Use the disabled option on each individual item to only disable certain options.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. The label used by the select component. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to the select component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the select component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the select component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the select.
Name input Wrapper | Type object | Description If any of formGroup.beforeInput or formGroup.afterInput have a value, a wrapping element is added around the select and inserted content. This object allows you to customise that wrapping element. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the select.

Name | Type | Description
Name value | Type string | Description The value attribute for the option. If this is omitted, the value is taken from the text content of the option element.
Name text | Type string | Description Required. Text for the option item.
Name divider | Type boolean | Description Divider line used to separate option items.
Name selected | Type boolean | Description Whether the option should be selected when the page loads. Takes precedence over the top-level value option.
Name disabled | Type boolean | Description Sets the option item as disabled.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the option.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the select used by the select component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the select used by the select component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the select. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the select. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the select. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the select. If html is provided, the text option will be ignored.

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
"select/macro.njk"
import
select
%}
{{
select
({
label
: {
text
:
"Choose region"
,
size
:
"s"
},
hint
: {
text
:
"This can be different to what you selected before"
},
errorMessage
: {
text
:
"Choose a region"
},
id
:
"region"
,
name
:
"region"
,
value
:
"choose"
,
items
: [
    {
value
:
"choose"
,
text
:
"Choose region"
},
    {
value
:
"east"
,
text
:
"East of England"
},
    {
value
:
"london"
,
text
:
"London"
},
    {
value
:
"midlands"
,
text
:
"Midlands"
},
    {
value
:
"yorkshire"
,
text
:
"North East and Yorkshire"
},
    {
value
:
"northwest"
,
text
:
"North West"
},
    {
value
:
"southeast"
,
text
:
"South East"
},
    {
value
:
"southeast"
,
text
:
"South West"
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### Avoid adding functionality to allow selecting multiple options

The select component does not support selecting multiple options, as there's a history of poor usability and assistive technology support for <select multiple> . If you need to ask the user to pick more than 1 item from a list, it's almost always better to use another method, such as a list of checkboxes .

Read Select your poison (24 Accessibility) .

If you still decide to allow selecting multiple options, you must offer a way to do so without relying on click and drag movements or keyboard and mouse combination actions.

## Research

User research shows that some users struggle with the select component, especially people who use a keyboard to navigate and people with motor difficulties. The dropdown feature makes users work hard to see and understand their options and click the option they want.

### Known issues and gaps

Research shows that users can struggle with selects, particularly when users have:

- been unable to close the select

- tried to type into the select

- confused focused items with selected items

- tried to pinch zoom select options on smaller devices

- not understood that they can scroll down to see more items, or how to

Find out more in:

- a video of Alice Barlett talking about binning select tags , with examples of users struggling with selects

- a blog post on Asking for a date of birth (GOV.UK) , which shows an example where a text input is used over a select

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
