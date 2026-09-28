# Checkboxes – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/checkboxes/

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

# Form elements – Checkboxes

Use checkboxes to let users select 1 or more options on a form.

- HTML code for checkboxes

- Nunjucks code for checkboxes

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
aria-describedby
=
"example-hint"
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
"example-hint"
>
Select all options that are relevant to you
</
div
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
"example"
name
=
"example"
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
"example"
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
"example-2"
name
=
"example"
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
"example-2"
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
"example-3"
name
=
"example"
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
"example-3"
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the checkboxes component.
Name described By | Type string | Description One or more element IDs to add to the input aria-describedby attribute without a fieldset, used to provide additional descriptive information for screenreader users.
Name fieldset | Type object | Description Can be used to add a fieldset to the checkboxes component. The fieldset.html option is not supported. See macro options for fieldset .
Name hint | Type object | Description Can be used to add a hint to the checkboxes component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the checkboxes component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the checkboxes component. See macro options for form Group .
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each checkbox item input, hint and error message, separated by - . Defaults to the name option value.
Name name | Type string | Description Required. The name attribute for all checkbox items.
Name items | Type array | Description Required. The checkbox items within the checkboxes component. See macro options for items .
Name values | Type array | Description Array of values for checkboxes which should be checked when the page loads. Use this as an alternative to setting the checked option on each individual item.
Name disabled | Type boolean | Description If true , checkbox inputs used by the checkboxes component will be disabled.
Name small | Type boolean | Description If set to true , small checkboxes will be used.
Name inline | Type boolean | Description If set to true , inline checkboxes will be used.
Name classes | Type string | Description Classes to add to the checkboxes container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkboxes container.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before all checkbox items within the checkboxes component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after all checkbox items within the checkboxes component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each checkbox item label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each checkbox item label. If html is provided, the text option will be ignored.
Name id | Type string | Description Specific id attribute for the checkbox item. If omitted, then component global idPrefix option will be applied.
Name name | Type string | Description Specific name attribute for the checkbox item. If omitted, then component global name string will be applied.
Name value | Type string | Description Required. The value attribute for the checkbox input.
Name label | Type object | Description The label used by each checkbox item within the checkboxes component. The label.size and label.heading options are not supported. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to each checkbox item within the checkboxes component. See macro options for hint .
Name divider | Type string | Description Divider text to separate checkbox items, for example the text "or" .
Name checked | Type boolean | Description Whether the checkbox should be checked when the page loads. Takes precedence over the top-level values option.
Name conditional | Type object | Description Provide additional content to reveal when the checkbox is checked. See macro options for items conditional .
Name disabled | Type boolean | Description If true , checkbox will be disabled.
Name classes | Type string | Description Classes to add to the checkbox input tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkbox input tag.
Name behaviour | Type string | Description Behaviour of the checkbox when JavaScript is enabled – "exclusive" or "inclusive" . Use "exclusive" for a "none" option or "inclusive" for an "all" option.
Name behaviour Group | Type string | Description Used in conjunction with behaviour - this should be set to a string which groups checkboxes together into a set for use with a "none" or "all" option.
Name exclusive | Type boolean | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviour in the items option.
Name exclusive Group | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviourGroup in the items option.

Name | Type | Description
Name html | Type string | Description Required. The HTML to reveal when the checkbox is checked.

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
"checkboxes/macro.njk"
import
checkboxes
%}
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
idPrefix
:
"example"
,
name
:
"example"
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

## When to use checkboxes

Use checkboxes when you need to help users:

- select more than 1 option from a list

- toggle a single option on or off

## When not to use checkboxes

Do not use the checkboxes component if users can only choose 1 option from a selection. In this case, use a radio .

## How to use checkboxes

Position checkboxes to the left of their labels. This makes them easier to find, especially for users of screen magnifiers.

Do not pre-select checkbox options as this makes it more likely that users will:

- not realise they've missed a question

- submit the wrong answer

Order checkbox options alphabetically by default. In some cases, it's helpful to order them from most-to-least common options, for example, by population size. But be careful, as this can reinforce bias. If in doubt, order alphabetically.

Group checkboxes together in a <fieldset> with a <legend> that describes them. You can see an example at the top of this page. The legend is usually a question, like "How do you want to be contacted about this?".

Read more about using fieldset .

### Inline checkboxes

In some cases, you can choose to display checkboxes "inline" beside one another (horizontally).

Only use inline checkboxes when:

- the question only has 2 options

- both options are short

On small screens such as mobile devices, the checkboxes will still be "stacked" on top of one another (vertically).

- HTML code for checkboxes inline

- Nunjucks code for checkboxes inline

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
Which nipple has changed?
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
"nhsuk-checkboxes nhsuk-checkboxes--inline"
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
"example-inline"
name
=
"exampleInline"
type
=
"checkbox"
value
=
"right"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"example-inline"
>
Right nipple
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
"example-inline-2"
name
=
"exampleInline"
type
=
"checkbox"
value
=
"left"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"example-inline-2"
>
Left nipple
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the checkboxes component.
Name described By | Type string | Description One or more element IDs to add to the input aria-describedby attribute without a fieldset, used to provide additional descriptive information for screenreader users.
Name fieldset | Type object | Description Can be used to add a fieldset to the checkboxes component. The fieldset.html option is not supported. See macro options for fieldset .
Name hint | Type object | Description Can be used to add a hint to the checkboxes component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the checkboxes component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the checkboxes component. See macro options for form Group .
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each checkbox item input, hint and error message, separated by - . Defaults to the name option value.
Name name | Type string | Description Required. The name attribute for all checkbox items.
Name items | Type array | Description Required. The checkbox items within the checkboxes component. See macro options for items .
Name values | Type array | Description Array of values for checkboxes which should be checked when the page loads. Use this as an alternative to setting the checked option on each individual item.
Name disabled | Type boolean | Description If true , checkbox inputs used by the checkboxes component will be disabled.
Name small | Type boolean | Description If set to true , small checkboxes will be used.
Name inline | Type boolean | Description If set to true , inline checkboxes will be used.
Name classes | Type string | Description Classes to add to the checkboxes container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkboxes container.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before all checkbox items within the checkboxes component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after all checkbox items within the checkboxes component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each checkbox item label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each checkbox item label. If html is provided, the text option will be ignored.
Name id | Type string | Description Specific id attribute for the checkbox item. If omitted, then component global idPrefix option will be applied.
Name name | Type string | Description Specific name attribute for the checkbox item. If omitted, then component global name string will be applied.
Name value | Type string | Description Required. The value attribute for the checkbox input.
Name label | Type object | Description The label used by each checkbox item within the checkboxes component. The label.size and label.heading options are not supported. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to each checkbox item within the checkboxes component. See macro options for hint .
Name divider | Type string | Description Divider text to separate checkbox items, for example the text "or" .
Name checked | Type boolean | Description Whether the checkbox should be checked when the page loads. Takes precedence over the top-level values option.
Name conditional | Type object | Description Provide additional content to reveal when the checkbox is checked. See macro options for items conditional .
Name disabled | Type boolean | Description If true , checkbox will be disabled.
Name classes | Type string | Description Classes to add to the checkbox input tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkbox input tag.
Name behaviour | Type string | Description Behaviour of the checkbox when JavaScript is enabled – "exclusive" or "inclusive" . Use "exclusive" for a "none" option or "inclusive" for an "all" option.
Name behaviour Group | Type string | Description Used in conjunction with behaviour - this should be set to a string which groups checkboxes together into a set for use with a "none" or "all" option.
Name exclusive | Type boolean | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviour in the items option.
Name exclusive Group | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviourGroup in the items option.

Name | Type | Description
Name html | Type string | Description Required. The HTML to reveal when the checkbox is checked.

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
"checkboxes/macro.njk"
import
checkboxes
%}
{{
checkboxes
({
fieldset
: {
legend
: {
text
:
"Which nipple has changed?"
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
idPrefix
:
"example-inline"
,
name
:
"exampleInline"
,
inline
:
true
,
items
: [
    {
value
:
"right"
,
text
:
"Right nipple"
},
    {
value
:
"left"
,
text
:
"Left nipple"
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### Checkboxes with hint text

Unlike with radios , users can select more than 1 option from a list of checkboxes. Do not assume that users will know how many options they can select.

Use hint text to give users help in context . For example, say "Select all the options that are relevant to you". Read more about hint text .

- HTML code for checkboxes hint text

- Nunjucks code for checkboxes hint text

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
aria-describedby
=
"contact-hint"
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the checkboxes component.
Name described By | Type string | Description One or more element IDs to add to the input aria-describedby attribute without a fieldset, used to provide additional descriptive information for screenreader users.
Name fieldset | Type object | Description Can be used to add a fieldset to the checkboxes component. The fieldset.html option is not supported. See macro options for fieldset .
Name hint | Type object | Description Can be used to add a hint to the checkboxes component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the checkboxes component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the checkboxes component. See macro options for form Group .
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each checkbox item input, hint and error message, separated by - . Defaults to the name option value.
Name name | Type string | Description Required. The name attribute for all checkbox items.
Name items | Type array | Description Required. The checkbox items within the checkboxes component. See macro options for items .
Name values | Type array | Description Array of values for checkboxes which should be checked when the page loads. Use this as an alternative to setting the checked option on each individual item.
Name disabled | Type boolean | Description If true , checkbox inputs used by the checkboxes component will be disabled.
Name small | Type boolean | Description If set to true , small checkboxes will be used.
Name inline | Type boolean | Description If set to true , inline checkboxes will be used.
Name classes | Type string | Description Classes to add to the checkboxes container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkboxes container.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before all checkbox items within the checkboxes component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after all checkbox items within the checkboxes component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each checkbox item label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each checkbox item label. If html is provided, the text option will be ignored.
Name id | Type string | Description Specific id attribute for the checkbox item. If omitted, then component global idPrefix option will be applied.
Name name | Type string | Description Specific name attribute for the checkbox item. If omitted, then component global name string will be applied.
Name value | Type string | Description Required. The value attribute for the checkbox input.
Name label | Type object | Description The label used by each checkbox item within the checkboxes component. The label.size and label.heading options are not supported. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to each checkbox item within the checkboxes component. See macro options for hint .
Name divider | Type string | Description Divider text to separate checkbox items, for example the text "or" .
Name checked | Type boolean | Description Whether the checkbox should be checked when the page loads. Takes precedence over the top-level values option.
Name conditional | Type object | Description Provide additional content to reveal when the checkbox is checked. See macro options for items conditional .
Name disabled | Type boolean | Description If true , checkbox will be disabled.
Name classes | Type string | Description Classes to add to the checkbox input tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkbox input tag.
Name behaviour | Type string | Description Behaviour of the checkbox when JavaScript is enabled – "exclusive" or "inclusive" . Use "exclusive" for a "none" option or "inclusive" for an "all" option.
Name behaviour Group | Type string | Description Used in conjunction with behaviour - this should be set to a string which groups checkboxes together into a set for use with a "none" or "all" option.
Name exclusive | Type boolean | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviour in the items option.
Name exclusive Group | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviourGroup in the items option.

Name | Type | Description
Name html | Type string | Description Required. The HTML to reveal when the checkbox is checked.

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
"checkboxes/macro.njk"
import
checkboxes
%}
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### Checkbox items with hints

You can add hints to checkbox items to provide additional information about the options.

- HTML code for checkboxes items with hints

- Nunjucks code for checkboxes items with hints

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
aria-describedby
=
"nationality-hint"
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
What medical conditions do you have?
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
"nationality-hint"
>
Select 1 or more
</
div
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
"nationality"
name
=
"nationality"
type
=
"checkbox"
value
=
"alzheimers"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"nationality"
>
Alzheimer
&#39;
s disease or dementia
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
"nationality-2"
name
=
"nationality"
type
=
"checkbox"
value
=
"asthma"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"nationality-2"
>
Asthma
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
"nationality-3"
name
=
"nationality"
type
=
"checkbox"
value
=
"cancer"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"nationality-3"
>
Cancer
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
"nationality-4"
name
=
"nationality"
type
=
"checkbox"
value
=
"diabetes"
aria-describedby
=
"nationality-4-item-hint"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"nationality-4"
>
Diabetes
</
label
>
<
div
class
=
"nhsuk-hint nhsuk-checkboxes__hint"
id
=
"nationality-4-item-hint"
>
including type 1, type 2, and gestational diabetes
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
Name id | Type string | Description The ID of the checkboxes component.
Name described By | Type string | Description One or more element IDs to add to the input aria-describedby attribute without a fieldset, used to provide additional descriptive information for screenreader users.
Name fieldset | Type object | Description Can be used to add a fieldset to the checkboxes component. The fieldset.html option is not supported. See macro options for fieldset .
Name hint | Type object | Description Can be used to add a hint to the checkboxes component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the checkboxes component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the checkboxes component. See macro options for form Group .
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each checkbox item input, hint and error message, separated by - . Defaults to the name option value.
Name name | Type string | Description Required. The name attribute for all checkbox items.
Name items | Type array | Description Required. The checkbox items within the checkboxes component. See macro options for items .
Name values | Type array | Description Array of values for checkboxes which should be checked when the page loads. Use this as an alternative to setting the checked option on each individual item.
Name disabled | Type boolean | Description If true , checkbox inputs used by the checkboxes component will be disabled.
Name small | Type boolean | Description If set to true , small checkboxes will be used.
Name inline | Type boolean | Description If set to true , inline checkboxes will be used.
Name classes | Type string | Description Classes to add to the checkboxes container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkboxes container.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before all checkbox items within the checkboxes component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after all checkbox items within the checkboxes component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each checkbox item label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each checkbox item label. If html is provided, the text option will be ignored.
Name id | Type string | Description Specific id attribute for the checkbox item. If omitted, then component global idPrefix option will be applied.
Name name | Type string | Description Specific name attribute for the checkbox item. If omitted, then component global name string will be applied.
Name value | Type string | Description Required. The value attribute for the checkbox input.
Name label | Type object | Description The label used by each checkbox item within the checkboxes component. The label.size and label.heading options are not supported. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to each checkbox item within the checkboxes component. See macro options for hint .
Name divider | Type string | Description Divider text to separate checkbox items, for example the text "or" .
Name checked | Type boolean | Description Whether the checkbox should be checked when the page loads. Takes precedence over the top-level values option.
Name conditional | Type object | Description Provide additional content to reveal when the checkbox is checked. See macro options for items conditional .
Name disabled | Type boolean | Description If true , checkbox will be disabled.
Name classes | Type string | Description Classes to add to the checkbox input tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkbox input tag.
Name behaviour | Type string | Description Behaviour of the checkbox when JavaScript is enabled – "exclusive" or "inclusive" . Use "exclusive" for a "none" option or "inclusive" for an "all" option.
Name behaviour Group | Type string | Description Used in conjunction with behaviour - this should be set to a string which groups checkboxes together into a set for use with a "none" or "all" option.
Name exclusive | Type boolean | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviour in the items option.
Name exclusive Group | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviourGroup in the items option.

Name | Type | Description
Name html | Type string | Description Required. The HTML to reveal when the checkbox is checked.

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
"checkboxes/macro.njk"
import
checkboxes
%}
{{
checkboxes
({
fieldset
: {
legend
: {
text
:
"What medical conditions do you have?"
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
"Select 1 or more"
},
idPrefix
:
"nationality"
,
name
:
"nationality"
,
items
: [
    {
value
:
"alzheimers"
,
text
:
"Alzheimer's disease or dementia"
},
    {
value
:
"asthma"
,
text
:
"Asthma"
},
    {
value
:
"cancer"
,
text
:
"Cancer"
},
    {
value
:
"diabetes"
,
text
:
"Diabetes"
,
hint
: {
text
:
"including type 1, type 2, and gestational diabetes"
}
    }
  ]
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### Add an option for "none"

You can give users the option to say none of the other options apply to them.

This option means users need to actively select "none" rather than leave all the boxes unchecked, which makes sure they do not skip the question by accident.

Remember to start by asking 1 question per page. You might be able to remove the need for a "none" option by asking the user a better question or by using filter questions to filter users out beforehand.

Show the "none" option last. Separate it from the other options using a divider, normally the word "or".

Write a label that repeats the key part of the question. For example, for the question "Do you have any of these symptoms?", say "No, I do not have any of these symptoms". Avoid phrases like "none of the above" because this is a visual reference and might be hard for people who use screen readers to understand.

To enable some JavaScript that unchecks all other checkboxes when the user clicks "none", add the data-behaviour="exclusive" behaviour to the "none" checkbox. If you are using the Nunjucks macro, use the behaviour: "exclusive" option instead.

- HTML code for checkboxes none option

- Nunjucks code for checkboxes none option

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
aria-describedby
=
"symptoms-hint"
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
Do you have any of these symptoms?
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
"symptoms-hint"
>
Select all the symptoms you have
</
div
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
"symptoms"
name
=
"symptoms"
type
=
"checkbox"
value
=
"sorethroat"
data-behaviour-group
=
"symptoms-list"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"symptoms"
>
Sore throat
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
"symptoms-2"
name
=
"symptoms"
type
=
"checkbox"
value
=
"runnynose"
data-behaviour-group
=
"symptoms-list"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"symptoms-2"
>
Runny nose
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
"symptoms-3"
name
=
"symptoms"
type
=
"checkbox"
value
=
"muscleorjointpain"
data-behaviour-group
=
"symptoms-list"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"symptoms-3"
>
Muscle or joint pain
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
"nhsuk-checkboxes__divider"
>
or
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
"symptoms-5"
name
=
"symptoms"
type
=
"checkbox"
value
=
"none"
data-behaviour
=
"exclusive"
data-behaviour-group
=
"symptoms-list"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"symptoms-5"
>
No, I do not have any of these symptoms
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the checkboxes component.
Name described By | Type string | Description One or more element IDs to add to the input aria-describedby attribute without a fieldset, used to provide additional descriptive information for screenreader users.
Name fieldset | Type object | Description Can be used to add a fieldset to the checkboxes component. The fieldset.html option is not supported. See macro options for fieldset .
Name hint | Type object | Description Can be used to add a hint to the checkboxes component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the checkboxes component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the checkboxes component. See macro options for form Group .
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each checkbox item input, hint and error message, separated by - . Defaults to the name option value.
Name name | Type string | Description Required. The name attribute for all checkbox items.
Name items | Type array | Description Required. The checkbox items within the checkboxes component. See macro options for items .
Name values | Type array | Description Array of values for checkboxes which should be checked when the page loads. Use this as an alternative to setting the checked option on each individual item.
Name disabled | Type boolean | Description If true , checkbox inputs used by the checkboxes component will be disabled.
Name small | Type boolean | Description If set to true , small checkboxes will be used.
Name inline | Type boolean | Description If set to true , inline checkboxes will be used.
Name classes | Type string | Description Classes to add to the checkboxes container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkboxes container.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before all checkbox items within the checkboxes component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after all checkbox items within the checkboxes component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each checkbox item label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each checkbox item label. If html is provided, the text option will be ignored.
Name id | Type string | Description Specific id attribute for the checkbox item. If omitted, then component global idPrefix option will be applied.
Name name | Type string | Description Specific name attribute for the checkbox item. If omitted, then component global name string will be applied.
Name value | Type string | Description Required. The value attribute for the checkbox input.
Name label | Type object | Description The label used by each checkbox item within the checkboxes component. The label.size and label.heading options are not supported. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to each checkbox item within the checkboxes component. See macro options for hint .
Name divider | Type string | Description Divider text to separate checkbox items, for example the text "or" .
Name checked | Type boolean | Description Whether the checkbox should be checked when the page loads. Takes precedence over the top-level values option.
Name conditional | Type object | Description Provide additional content to reveal when the checkbox is checked. See macro options for items conditional .
Name disabled | Type boolean | Description If true , checkbox will be disabled.
Name classes | Type string | Description Classes to add to the checkbox input tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkbox input tag.
Name behaviour | Type string | Description Behaviour of the checkbox when JavaScript is enabled – "exclusive" or "inclusive" . Use "exclusive" for a "none" option or "inclusive" for an "all" option.
Name behaviour Group | Type string | Description Used in conjunction with behaviour - this should be set to a string which groups checkboxes together into a set for use with a "none" or "all" option.
Name exclusive | Type boolean | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviour in the items option.
Name exclusive Group | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviourGroup in the items option.

Name | Type | Description
Name html | Type string | Description Required. The HTML to reveal when the checkbox is checked.

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
"checkboxes/macro.njk"
import
checkboxes
%}
{{
checkboxes
({
fieldset
: {
legend
: {
text
:
"Do you have any of these symptoms?"
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
"Select all the symptoms you have"
},
idPrefix
:
"symptoms"
,
name
:
"symptoms"
,
items
: [
    {
value
:
"sorethroat"
,
text
:
"Sore throat"
,
behaviourGroup
:
"symptoms-list"
},
    {
value
:
"runnynose"
,
text
:
"Runny nose"
,
behaviourGroup
:
"symptoms-list"
},
    {
value
:
"muscleorjointpain"
,
text
:
"Muscle or joint pain"
,
behaviourGroup
:
"symptoms-list"
},
    {
divider
:
"or"
},
    {
value
:
"none"
,
text
:
"No, I do not have any of these symptoms"
,
behaviour
:
"exclusive"
,
behaviourGroup
:
"symptoms-list"
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

If JavaScript is unavailable, and a user selects both the "none" checkbox and another checkbox, display an error message.

### Add an option for "all"

You can give users an option to be able to quickly select or unselect all the checkboxes. This checkbox only displays when JavaScript is available.

Show this option first so that users see it before starting to select each checkbox individually.

To use it, add the data-behaviour="inclusive" attribute to the checkbox, and add the HTML class nhsuk-frontend-supported-only to its container and any divider that appears after it. If you are using the Nunjucks macro, use the behaviour: "inclusive" option instead.

- HTML code for checkboxes all option

- Nunjucks code for checkboxes all option

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
Which vaccines would you like to include?
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
"nhsuk-checkboxes"
data-module
=
"nhsuk-checkboxes"
>
<
div
class
=
"nhsuk-checkboxes__item nhsuk-u-frontend-not-supported-hidden"
>
<
input
class
=
"nhsuk-checkboxes__input"
id
=
"vaccines"
name
=
"vaccines"
type
=
"checkbox"
value
=
"all"
data-behaviour
=
"inclusive"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"vaccines"
>
All 9 vaccines
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
"nhsuk-checkboxes__divider nhsuk-u-frontend-not-supported-hidden"
>
or
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
"vaccines-3"
name
=
"vaccines"
type
=
"checkbox"
value
=
"4in1"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"vaccines-3"
>
4-in-1 pre-school booster
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
"vaccines-4"
name
=
"vaccines"
type
=
"checkbox"
value
=
"6in1"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"vaccines-4"
>
6-in-1
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
"vaccines-5"
name
=
"vaccines"
type
=
"checkbox"
value
=
"hpv"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"vaccines-5"
>
HPV
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
"vaccines-6"
name
=
"vaccines"
type
=
"checkbox"
value
=
"menb"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"vaccines-6"
>
MenB
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
"vaccines-7"
name
=
"vaccines"
type
=
"checkbox"
value
=
"menacwy"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"vaccines-7"
>
MenACWY
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
"vaccines-8"
name
=
"vaccines"
type
=
"checkbox"
value
=
"mmrv"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"vaccines-8"
>
MMRV
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
"vaccines-9"
name
=
"vaccines"
type
=
"checkbox"
value
=
"rotavirus"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"vaccines-9"
>
Rotavirus
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
"vaccines-10"
name
=
"vaccines"
type
=
"checkbox"
value
=
"pneumococcal"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"vaccines-10"
>
Pneumococcal
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
"vaccines-11"
name
=
"vaccines"
type
=
"checkbox"
value
=
"tdipv"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"vaccines-11"
>
Td/IPV
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the checkboxes component.
Name described By | Type string | Description One or more element IDs to add to the input aria-describedby attribute without a fieldset, used to provide additional descriptive information for screenreader users.
Name fieldset | Type object | Description Can be used to add a fieldset to the checkboxes component. The fieldset.html option is not supported. See macro options for fieldset .
Name hint | Type object | Description Can be used to add a hint to the checkboxes component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the checkboxes component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the checkboxes component. See macro options for form Group .
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each checkbox item input, hint and error message, separated by - . Defaults to the name option value.
Name name | Type string | Description Required. The name attribute for all checkbox items.
Name items | Type array | Description Required. The checkbox items within the checkboxes component. See macro options for items .
Name values | Type array | Description Array of values for checkboxes which should be checked when the page loads. Use this as an alternative to setting the checked option on each individual item.
Name disabled | Type boolean | Description If true , checkbox inputs used by the checkboxes component will be disabled.
Name small | Type boolean | Description If set to true , small checkboxes will be used.
Name inline | Type boolean | Description If set to true , inline checkboxes will be used.
Name classes | Type string | Description Classes to add to the checkboxes container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkboxes container.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before all checkbox items within the checkboxes component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after all checkbox items within the checkboxes component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each checkbox item label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each checkbox item label. If html is provided, the text option will be ignored.
Name id | Type string | Description Specific id attribute for the checkbox item. If omitted, then component global idPrefix option will be applied.
Name name | Type string | Description Specific name attribute for the checkbox item. If omitted, then component global name string will be applied.
Name value | Type string | Description Required. The value attribute for the checkbox input.
Name label | Type object | Description The label used by each checkbox item within the checkboxes component. The label.size and label.heading options are not supported. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to each checkbox item within the checkboxes component. See macro options for hint .
Name divider | Type string | Description Divider text to separate checkbox items, for example the text "or" .
Name checked | Type boolean | Description Whether the checkbox should be checked when the page loads. Takes precedence over the top-level values option.
Name conditional | Type object | Description Provide additional content to reveal when the checkbox is checked. See macro options for items conditional .
Name disabled | Type boolean | Description If true , checkbox will be disabled.
Name classes | Type string | Description Classes to add to the checkbox input tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkbox input tag.
Name behaviour | Type string | Description Behaviour of the checkbox when JavaScript is enabled – "exclusive" or "inclusive" . Use "exclusive" for a "none" option or "inclusive" for an "all" option.
Name behaviour Group | Type string | Description Used in conjunction with behaviour - this should be set to a string which groups checkboxes together into a set for use with a "none" or "all" option.
Name exclusive | Type boolean | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviour in the items option.
Name exclusive Group | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviourGroup in the items option.

Name | Type | Description
Name html | Type string | Description Required. The HTML to reveal when the checkbox is checked.

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
"checkboxes/macro.njk"
import
checkboxes
%}
{{
checkboxes
({
fieldset
: {
legend
: {
text
:
"Which vaccines would you like to include?"
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
idPrefix
:
"vaccines"
,
name
:
"vaccines"
,
items
: [
    {
value
:
"all"
,
text
:
"All 9 vaccines"
,
behaviour
:
"inclusive"
},
    {
divider
:
"or"
,
behaviour
:
"inclusive"
},
    {
value
:
"4in1"
,
text
:
"4-in-1 pre-school booster"
},
    {
value
:
"6in1"
,
text
:
"6-in-1"
},
    {
value
:
"hpv"
,
text
:
"HPV"
},
    {
value
:
"menb"
,
text
:
"MenB"
},
    {
value
:
"menacwy"
,
text
:
"MenACWY"
},
    {
value
:
"mmrv"
,
text
:
"MMRV"
},
    {
value
:
"rotavirus"
,
text
:
"Rotavirus"
},
    {
value
:
"pneumococcal"
,
text
:
"Pneumococcal"
},
    {
value
:
"tdipv"
,
text
:
"Td/IPV"
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### Conditionally revealing a related question

You can add a conditionally revealing related question to checkboxes, so users only see the question when it's relevant to them.

For example, you could reveal a phone number input only when a user chooses to be contacted by phone.

- HTML code for checkboxes conditional

- Nunjucks code for checkboxes conditional

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
aria-describedby
=
"contact-hint"
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
data-aria-controls
=
"conditional-contact"
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
"nhsuk-checkboxes__conditional nhsuk-checkboxes__conditional--hidden"
id
=
"conditional-contact"
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
"email"
>
Email address
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
"email"
name
=
"email"
type
=
"text"
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
data-aria-controls
=
"conditional-contact-2"
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
"nhsuk-checkboxes__conditional nhsuk-checkboxes__conditional--hidden"
id
=
"conditional-contact-2"
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
"phone"
>
Phone number
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
"phone"
name
=
"phone"
type
=
"text"
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
"text"
data-aria-controls
=
"conditional-contact-3"
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
<
div
class
=
"nhsuk-checkboxes__conditional nhsuk-checkboxes__conditional--hidden"
id
=
"conditional-contact-3"
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
"mobile"
>
Mobile phone number
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
"mobile"
name
=
"mobile"
type
=
"text"
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
Name id | Type string | Description The ID of the checkboxes component.
Name described By | Type string | Description One or more element IDs to add to the input aria-describedby attribute without a fieldset, used to provide additional descriptive information for screenreader users.
Name fieldset | Type object | Description Can be used to add a fieldset to the checkboxes component. The fieldset.html option is not supported. See macro options for fieldset .
Name hint | Type object | Description Can be used to add a hint to the checkboxes component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the checkboxes component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the checkboxes component. See macro options for form Group .
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each checkbox item input, hint and error message, separated by - . Defaults to the name option value.
Name name | Type string | Description Required. The name attribute for all checkbox items.
Name items | Type array | Description Required. The checkbox items within the checkboxes component. See macro options for items .
Name values | Type array | Description Array of values for checkboxes which should be checked when the page loads. Use this as an alternative to setting the checked option on each individual item.
Name disabled | Type boolean | Description If true , checkbox inputs used by the checkboxes component will be disabled.
Name small | Type boolean | Description If set to true , small checkboxes will be used.
Name inline | Type boolean | Description If set to true , inline checkboxes will be used.
Name classes | Type string | Description Classes to add to the checkboxes container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkboxes container.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before all checkbox items within the checkboxes component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after all checkbox items within the checkboxes component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each checkbox item label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each checkbox item label. If html is provided, the text option will be ignored.
Name id | Type string | Description Specific id attribute for the checkbox item. If omitted, then component global idPrefix option will be applied.
Name name | Type string | Description Specific name attribute for the checkbox item. If omitted, then component global name string will be applied.
Name value | Type string | Description Required. The value attribute for the checkbox input.
Name label | Type object | Description The label used by each checkbox item within the checkboxes component. The label.size and label.heading options are not supported. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to each checkbox item within the checkboxes component. See macro options for hint .
Name divider | Type string | Description Divider text to separate checkbox items, for example the text "or" .
Name checked | Type boolean | Description Whether the checkbox should be checked when the page loads. Takes precedence over the top-level values option.
Name conditional | Type object | Description Provide additional content to reveal when the checkbox is checked. See macro options for items conditional .
Name disabled | Type boolean | Description If true , checkbox will be disabled.
Name classes | Type string | Description Classes to add to the checkbox input tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkbox input tag.
Name behaviour | Type string | Description Behaviour of the checkbox when JavaScript is enabled – "exclusive" or "inclusive" . Use "exclusive" for a "none" option or "inclusive" for an "all" option.
Name behaviour Group | Type string | Description Used in conjunction with behaviour - this should be set to a string which groups checkboxes together into a set for use with a "none" or "all" option.
Name exclusive | Type boolean | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviour in the items option.
Name exclusive Group | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviourGroup in the items option.

Name | Type | Description
Name html | Type string | Description Required. The HTML to reveal when the checkbox is checked.

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
"checkboxes/macro.njk"
import
checkboxes
%}
{%
from
"input/macro.njk"
import
input
%}
{%
set
emailHtml
%}
{{
input
({
label
: {
text
:
"Email address"
},
id
:
"email"
,
name
:
"email"
,
classes
:
"nhsuk-u-width-two-thirds"
})
}}
{%
endset
-%}
{%
set
phoneHtml
%}
{{
input
({
label
: {
text
:
"Phone number"
},
id
:
"phone"
,
name
:
"phone"
,
classes
:
"nhsuk-u-width-two-thirds"
})
}}
{%
endset
-%}
{%
set
mobileHtml
%}
{{
input
({
label
: {
text
:
"Mobile phone number"
},
id
:
"mobile"
,
name
:
"mobile"
,
classes
:
"nhsuk-u-width-two-thirds"
})
}}
{%
endset
-%}
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
conditional
: {
html
: emailHtml
      }
    },
    {
value
:
"phone"
,
text
:
"Phone"
,
conditional
: {
html
: phoneHtml
      }
    },
    {
value
:
"text"
,
text
:
"Text message"
,
conditional
: {
html
: mobileHtml
      }
    }
  ]
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Keep it simple. If you need to add a lot of content, consider showing it on the next page in the process instead.

Only conditionally reveal questions. Do not show or hide anything that is not a question.

#### Known issues

Users are not always notified when a conditionally revealed question is shown or hidden. This fails WCAG 2.2 success criterion 4.1.2 name, role, value (W3C) .

However, GOV.UK found that screen reader users did not have difficulty answering a conditionally revealed question as long as it's simple. It confused users when they conditionally revealed complicated questions.

### Smaller checkboxes

- HTML code for checkboxes smaller

- Nunjucks code for checkboxes smaller

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
>
<
legend
class
=
"nhsuk-fieldset__legend nhsuk-fieldset__legend--m"
>
<
h1
class
=
"nhsuk-fieldset__heading"
>
Care setting
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
"nhsuk-checkboxes nhsuk-checkboxes--small"
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
"example"
name
=
"example"
type
=
"checkbox"
value
=
"ambulance or urgent and emergency care"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"example"
>
Ambulance or urgent and emergency care
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
"example-2"
name
=
"example"
type
=
"checkbox"
value
=
"care home"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"example-2"
>
Care home
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
"example-3"
name
=
"example"
type
=
"checkbox"
value
=
"community health"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"example-3"
>
Community health
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
"example-4"
name
=
"example"
type
=
"checkbox"
value
=
"dentistry"
>
<
label
class
=
"nhsuk-label nhsuk-checkboxes__label"
for
=
"example-4"
>
Dentistry
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the checkboxes component.
Name described By | Type string | Description One or more element IDs to add to the input aria-describedby attribute without a fieldset, used to provide additional descriptive information for screenreader users.
Name fieldset | Type object | Description Can be used to add a fieldset to the checkboxes component. The fieldset.html option is not supported. See macro options for fieldset .
Name hint | Type object | Description Can be used to add a hint to the checkboxes component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the checkboxes component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the checkboxes component. See macro options for form Group .
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each checkbox item input, hint and error message, separated by - . Defaults to the name option value.
Name name | Type string | Description Required. The name attribute for all checkbox items.
Name items | Type array | Description Required. The checkbox items within the checkboxes component. See macro options for items .
Name values | Type array | Description Array of values for checkboxes which should be checked when the page loads. Use this as an alternative to setting the checked option on each individual item.
Name disabled | Type boolean | Description If true , checkbox inputs used by the checkboxes component will be disabled.
Name small | Type boolean | Description If set to true , small checkboxes will be used.
Name inline | Type boolean | Description If set to true , inline checkboxes will be used.
Name classes | Type string | Description Classes to add to the checkboxes container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkboxes container.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before all checkbox items within the checkboxes component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after all checkbox items within the checkboxes component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each checkbox item label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each checkbox item label. If html is provided, the text option will be ignored.
Name id | Type string | Description Specific id attribute for the checkbox item. If omitted, then component global idPrefix option will be applied.
Name name | Type string | Description Specific name attribute for the checkbox item. If omitted, then component global name string will be applied.
Name value | Type string | Description Required. The value attribute for the checkbox input.
Name label | Type object | Description The label used by each checkbox item within the checkboxes component. The label.size and label.heading options are not supported. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to each checkbox item within the checkboxes component. See macro options for hint .
Name divider | Type string | Description Divider text to separate checkbox items, for example the text "or" .
Name checked | Type boolean | Description Whether the checkbox should be checked when the page loads. Takes precedence over the top-level values option.
Name conditional | Type object | Description Provide additional content to reveal when the checkbox is checked. See macro options for items conditional .
Name disabled | Type boolean | Description If true , checkbox will be disabled.
Name classes | Type string | Description Classes to add to the checkbox input tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkbox input tag.
Name behaviour | Type string | Description Behaviour of the checkbox when JavaScript is enabled – "exclusive" or "inclusive" . Use "exclusive" for a "none" option or "inclusive" for an "all" option.
Name behaviour Group | Type string | Description Used in conjunction with behaviour - this should be set to a string which groups checkboxes together into a set for use with a "none" or "all" option.
Name exclusive | Type boolean | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviour in the items option.
Name exclusive Group | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviourGroup in the items option.

Name | Type | Description
Name html | Type string | Description Required. The HTML to reveal when the checkbox is checked.

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
"checkboxes/macro.njk"
import
checkboxes
%}
{{
checkboxes
({
fieldset
: {
legend
: {
text
:
"Care setting"
,
size
:
"m"
,
isPageHeading
:
true
}
  },
idPrefix
:
"example"
,
name
:
"example"
,
small
:
true
,
items
: [
    {
value
:
"ambulance or urgent and emergency care"
,
text
:
"Ambulance or urgent and emergency care"
},
    {
value
:
"care home"
,
text
:
"Care home"
},
    {
value
:
"community health"
,
text
:
"Community health"
},
    {
value
:
"dentistry"
,
text
:
"Dentistry"
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use standard-sized checkboxes in most cases.

You can use small checkboxes where you need something less visually prominent. For example, on:

- a page of search results where users need to see and change search filters without distracting them from the results

- on information-dense screens in services designed for repeat use, like staff-facing systems

### Error messages

Style error messages like this.

- HTML code for checkboxes error messages

- Nunjucks code for checkboxes error messages

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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the checkboxes component.
Name described By | Type string | Description One or more element IDs to add to the input aria-describedby attribute without a fieldset, used to provide additional descriptive information for screenreader users.
Name fieldset | Type object | Description Can be used to add a fieldset to the checkboxes component. The fieldset.html option is not supported. See macro options for fieldset .
Name hint | Type object | Description Can be used to add a hint to the checkboxes component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the checkboxes component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the checkboxes component. See macro options for form Group .
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each checkbox item input, hint and error message, separated by - . Defaults to the name option value.
Name name | Type string | Description Required. The name attribute for all checkbox items.
Name items | Type array | Description Required. The checkbox items within the checkboxes component. See macro options for items .
Name values | Type array | Description Array of values for checkboxes which should be checked when the page loads. Use this as an alternative to setting the checked option on each individual item.
Name disabled | Type boolean | Description If true , checkbox inputs used by the checkboxes component will be disabled.
Name small | Type boolean | Description If set to true , small checkboxes will be used.
Name inline | Type boolean | Description If set to true , inline checkboxes will be used.
Name classes | Type string | Description Classes to add to the checkboxes container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkboxes container.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before all checkbox items within the checkboxes component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after all checkbox items within the checkboxes component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after all checkbox items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after all checkbox items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each checkbox item label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each checkbox item label. If html is provided, the text option will be ignored.
Name id | Type string | Description Specific id attribute for the checkbox item. If omitted, then component global idPrefix option will be applied.
Name name | Type string | Description Specific name attribute for the checkbox item. If omitted, then component global name string will be applied.
Name value | Type string | Description Required. The value attribute for the checkbox input.
Name label | Type object | Description The label used by each checkbox item within the checkboxes component. The label.size and label.heading options are not supported. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to each checkbox item within the checkboxes component. See macro options for hint .
Name divider | Type string | Description Divider text to separate checkbox items, for example the text "or" .
Name checked | Type boolean | Description Whether the checkbox should be checked when the page loads. Takes precedence over the top-level values option.
Name conditional | Type object | Description Provide additional content to reveal when the checkbox is checked. See macro options for items conditional .
Name disabled | Type boolean | Description If true , checkbox will be disabled.
Name classes | Type string | Description Classes to add to the checkbox input tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the checkbox input tag.
Name behaviour | Type string | Description Behaviour of the checkbox when JavaScript is enabled – "exclusive" or "inclusive" . Use "exclusive" for a "none" option or "inclusive" for an "all" option.
Name behaviour Group | Type string | Description Used in conjunction with behaviour - this should be set to a string which groups checkboxes together into a set for use with a "none" or "all" option.
Name exclusive | Type boolean | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviour in the items option.
Name exclusive Group | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by item.behaviourGroup in the items option.

Name | Type | Description
Name html | Type string | Description Required. The HTML to reveal when the checkbox is checked.

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
"checkboxes/macro.njk"
import
checkboxes
%}
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Follow:

- our guidance on error messages

- GOV.UK design system guidance on error messages for checkboxes

## Progressive enhancement

The checkboxes component uses progressive enhancement and requires JavaScript for enhanced functionality.

When JavaScript is not available, conditionally revealed content will be revealed by default and "none" checkboxes will not uncheck all other checkboxes when clicked.

## Research

Our checkboxes are based on the GOV.UK design system. Read a GOV.UK blog post about their updates to radios and checkboxes .

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: August 2026
