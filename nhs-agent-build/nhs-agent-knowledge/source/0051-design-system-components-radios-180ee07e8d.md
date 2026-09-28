# Radios – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/radios/

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

# Form elements – Radios

Use radios when you want users to select only 1 option from a list.

- HTML code for radios

- Nunjucks code for radios

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
"example-hints-hint"
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
"example-hints-hint"
>
Select 1 option
</
div
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
"example-hints"
name
=
"exampleHints"
type
=
"radio"
value
=
"email"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"example-hints"
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
"nhsuk-radios__item"
>
<
input
class
=
"nhsuk-radios__input"
id
=
"example-hints-2"
name
=
"exampleHints"
type
=
"radio"
value
=
"phone"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"example-hints-2"
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
"nhsuk-radios__item"
>
<
input
class
=
"nhsuk-radios__input"
id
=
"example-hints-3"
name
=
"exampleHints"
type
=
"radio"
value
=
"text"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"example-hints-3"
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
Name id | Type string | Description The ID of the radios component.
Name fieldset | Type object | Description The fieldset used by the radios component. The fieldset.html option is not supported. See macro options for fieldset .
Name hint | Type object | Description Can be used to add a hint to the radios component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the radios component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the radios component. See macro options for form Group .
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each radio input, hint and error message, separated by - . Defaults to the name option value.
Name name | Type string | Description Required. The name attribute for the radio items.
Name items | Type array | Description Required. The radio items within the radios component. See macro options for items .
Name value | Type string | Description The value for the radio which should be checked when the page loads. Use this as an alternative to setting the checked option on each individual item.
Name disabled | Type boolean | Description If true , radio inputs used by the radios component will be disabled.
Name small | Type boolean | Description If set to true , small radios will be used.
Name inline | Type boolean | Description If set to true , inline radios will be used.
Name classes | Type string | Description Classes to add to the radios container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the radios container.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before all radio items within the radios component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after all radio items within the radios component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before all radio items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before all radio items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after all radio items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after all radio items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each radio item label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each radio item label. If html is provided, the text option will be ignored.
Name id | Type string | Description Specific id attribute for the radio item. If omitted, then idPrefix string will be applied.
Name value | Type string | Description Required. The value attribute for the radio input.
Name label | Type object | Description The label used by each radio item within the radios component. The label.size and label.heading options are not supported. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to each radio item within the radios component. See macro options for hint .
Name divider | Type string | Description Divider text to separate radio items, for example the text "or" .
Name checked | Type boolean | Description Whether the radio should be checked when the page loads. Takes precedence over the top-level value option.
Name conditional | Type object | Description Provide additional content to reveal when the radio is checked. See macro options for items conditional .
Name disabled | Type boolean | Description If true , radio will be disabled.
Name classes | Type string | Description Classes to add to the radio input tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the radio input tag.

Name | Type | Description
Name html | Type string | Description Required. The HTML to reveal when the radio is checked.

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
"radios/macro.njk"
import
radios
%}
{%
from
"fieldset/macro.njk"
import
fieldset
%}
{%
from
"hint/macro.njk"
import
hint
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
"Select 1 option"
},
idPrefix
:
"example-hints"
,
name
:
"exampleHints"
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
"text"
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

## When to use radios

Use radios if users can only choose 1 option from a list.

## When not to use radios

Do not use radios if users might need to select more than 1 option. Use checkboxes instead.

## How to use radios

Position radios to the left of their labels. This makes them easier to find, especially for users of screen magnifiers.

Unlike with checkboxes, users can only select 1 option from a list of radios. Do not assume that users will know how many options they can select based on the visual difference between radios and checkboxes alone. If needed, add a hint explaining this, for example, "Select 1 option".

Do not pre-select radio options as this makes it more likely that users will:

- not realise they've missed a question

- submit the wrong answer

Users cannot go back to having no option selected once they have selected an option, without refreshing their browser window. So you should include "None of these" or "I do not know" if they are valid options. In any case, it's best to beware binary choices .

Order radio options alphabetically by default. In some cases, it's helpful to order them from most-to-least common options, for example, by population size. But be careful, as this can reinforce bias. If in doubt, order alphabetically.

Group radios together in a <fieldset> with a <legend> that describes them. You can see an example at the top of this page. This is usually a question, like "Are you 18 or over?". Read more about using fieldset .

### Inline radios

In some cases, you can choose to display radios "inline" beside one another (horizontally).

Only use inline radios when:

- the question only has 2 options

- both options are short

On small screens such as mobile devices, the radios will still be "stacked" on top of one another (vertically).

- HTML code for radios inline

- Nunjucks code for radios inline

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
Are you 18 or over?
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
"nhsuk-radios nhsuk-radios--inline"
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
"example-inline"
name
=
"exampleInline"
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
"example-inline"
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
"example-inline-2"
name
=
"exampleInline"
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
"example-inline-2"
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the radios component.
Name fieldset | Type object | Description The fieldset used by the radios component. The fieldset.html option is not supported. See macro options for fieldset .
Name hint | Type object | Description Can be used to add a hint to the radios component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the radios component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the radios component. See macro options for form Group .
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each radio input, hint and error message, separated by - . Defaults to the name option value.
Name name | Type string | Description Required. The name attribute for the radio items.
Name items | Type array | Description Required. The radio items within the radios component. See macro options for items .
Name value | Type string | Description The value for the radio which should be checked when the page loads. Use this as an alternative to setting the checked option on each individual item.
Name disabled | Type boolean | Description If true , radio inputs used by the radios component will be disabled.
Name small | Type boolean | Description If set to true , small radios will be used.
Name inline | Type boolean | Description If set to true , inline radios will be used.
Name classes | Type string | Description Classes to add to the radios container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the radios container.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before all radio items within the radios component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after all radio items within the radios component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before all radio items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before all radio items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after all radio items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after all radio items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each radio item label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each radio item label. If html is provided, the text option will be ignored.
Name id | Type string | Description Specific id attribute for the radio item. If omitted, then idPrefix string will be applied.
Name value | Type string | Description Required. The value attribute for the radio input.
Name label | Type object | Description The label used by each radio item within the radios component. The label.size and label.heading options are not supported. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to each radio item within the radios component. See macro options for hint .
Name divider | Type string | Description Divider text to separate radio items, for example the text "or" .
Name checked | Type boolean | Description Whether the radio should be checked when the page loads. Takes precedence over the top-level value option.
Name conditional | Type object | Description Provide additional content to reveal when the radio is checked. See macro options for items conditional .
Name disabled | Type boolean | Description If true , radio will be disabled.
Name classes | Type string | Description Classes to add to the radio input tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the radio input tag.

Name | Type | Description
Name html | Type string | Description Required. The HTML to reveal when the radio is checked.

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
"Are you 18 or over?"
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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### Radios with hints

Use hint text to give users help in context . Read more about hint text .

Do not assume that users will know that they can only select 1 option based on the visual difference between radios and checkboxes. If needed, add a hint explaining this, for example, "Select 1 option".

- HTML code for radios with hints

- Nunjucks code for radios with hints

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
"example-hints-hint"
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
"example-hints-hint"
>
Select 1 option
</
div
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
"example-hints"
name
=
"exampleHints"
type
=
"radio"
value
=
"email"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"example-hints"
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
"nhsuk-radios__item"
>
<
input
class
=
"nhsuk-radios__input"
id
=
"example-hints-2"
name
=
"exampleHints"
type
=
"radio"
value
=
"phone"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"example-hints-2"
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
"nhsuk-radios__item"
>
<
input
class
=
"nhsuk-radios__input"
id
=
"example-hints-3"
name
=
"exampleHints"
type
=
"radio"
value
=
"text"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"example-hints-3"
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
Name id | Type string | Description The ID of the radios component.
Name fieldset | Type object | Description The fieldset used by the radios component. The fieldset.html option is not supported. See macro options for fieldset .
Name hint | Type object | Description Can be used to add a hint to the radios component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the radios component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the radios component. See macro options for form Group .
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each radio input, hint and error message, separated by - . Defaults to the name option value.
Name name | Type string | Description Required. The name attribute for the radio items.
Name items | Type array | Description Required. The radio items within the radios component. See macro options for items .
Name value | Type string | Description The value for the radio which should be checked when the page loads. Use this as an alternative to setting the checked option on each individual item.
Name disabled | Type boolean | Description If true , radio inputs used by the radios component will be disabled.
Name small | Type boolean | Description If set to true , small radios will be used.
Name inline | Type boolean | Description If set to true , inline radios will be used.
Name classes | Type string | Description Classes to add to the radios container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the radios container.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before all radio items within the radios component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after all radio items within the radios component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before all radio items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before all radio items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after all radio items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after all radio items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each radio item label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each radio item label. If html is provided, the text option will be ignored.
Name id | Type string | Description Specific id attribute for the radio item. If omitted, then idPrefix string will be applied.
Name value | Type string | Description Required. The value attribute for the radio input.
Name label | Type object | Description The label used by each radio item within the radios component. The label.size and label.heading options are not supported. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to each radio item within the radios component. See macro options for hint .
Name divider | Type string | Description Divider text to separate radio items, for example the text "or" .
Name checked | Type boolean | Description Whether the radio should be checked when the page loads. Takes precedence over the top-level value option.
Name conditional | Type object | Description Provide additional content to reveal when the radio is checked. See macro options for items conditional .
Name disabled | Type boolean | Description If true , radio will be disabled.
Name classes | Type string | Description Classes to add to the radio input tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the radio input tag.

Name | Type | Description
Name html | Type string | Description Required. The HTML to reveal when the radio is checked.

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
"radios/macro.njk"
import
radios
%}
{%
from
"fieldset/macro.njk"
import
fieldset
%}
{%
from
"hint/macro.njk"
import
hint
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
"Select 1 option"
},
idPrefix
:
"example-hints"
,
name
:
"exampleHints"
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
"text"
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

### Radio items with hints

You can add hints to radios to give more information about the options.

- HTML code for radios with hints options

- Nunjucks code for radios with hints options

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
Do you have a mobile phone with signal?
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
"example-hints"
name
=
"exampleHints"
type
=
"radio"
value
=
"mobile"
aria-describedby
=
"example-hints-item-hint"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"example-hints"
>
Yes, I have a mobile phone with signal
</
label
>
<
div
class
=
"nhsuk-hint nhsuk-radios__hint"
id
=
"example-hints-item-hint"
>
We will text you a 6 digit security code
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
"nhsuk-radios__item"
>
<
input
class
=
"nhsuk-radios__input"
id
=
"example-hints-2"
name
=
"exampleHints"
type
=
"radio"
value
=
"landline"
aria-describedby
=
"example-hints-2-item-hint"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"example-hints-2"
>
No, I want to use my landline
</
label
>
<
div
class
=
"nhsuk-hint nhsuk-radios__hint"
id
=
"example-hints-2-item-hint"
>
We will call you to give you a 6 digit security code
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
Name id | Type string | Description The ID of the radios component.
Name fieldset | Type object | Description The fieldset used by the radios component. The fieldset.html option is not supported. See macro options for fieldset .
Name hint | Type object | Description Can be used to add a hint to the radios component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the radios component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the radios component. See macro options for form Group .
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each radio input, hint and error message, separated by - . Defaults to the name option value.
Name name | Type string | Description Required. The name attribute for the radio items.
Name items | Type array | Description Required. The radio items within the radios component. See macro options for items .
Name value | Type string | Description The value for the radio which should be checked when the page loads. Use this as an alternative to setting the checked option on each individual item.
Name disabled | Type boolean | Description If true , radio inputs used by the radios component will be disabled.
Name small | Type boolean | Description If set to true , small radios will be used.
Name inline | Type boolean | Description If set to true , inline radios will be used.
Name classes | Type string | Description Classes to add to the radios container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the radios container.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before all radio items within the radios component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after all radio items within the radios component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before all radio items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before all radio items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after all radio items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after all radio items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each radio item label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each radio item label. If html is provided, the text option will be ignored.
Name id | Type string | Description Specific id attribute for the radio item. If omitted, then idPrefix string will be applied.
Name value | Type string | Description Required. The value attribute for the radio input.
Name label | Type object | Description The label used by each radio item within the radios component. The label.size and label.heading options are not supported. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to each radio item within the radios component. See macro options for hint .
Name divider | Type string | Description Divider text to separate radio items, for example the text "or" .
Name checked | Type boolean | Description Whether the radio should be checked when the page loads. Takes precedence over the top-level value option.
Name conditional | Type object | Description Provide additional content to reveal when the radio is checked. See macro options for items conditional .
Name disabled | Type boolean | Description If true , radio will be disabled.
Name classes | Type string | Description Classes to add to the radio input tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the radio input tag.

Name | Type | Description
Name html | Type string | Description Required. The HTML to reveal when the radio is checked.

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
"Do you have a mobile phone with signal?"
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
"example-hints"
,
name
:
"exampleHints"
,
items
: [
    {
value
:
"mobile"
,
text
:
"Yes, I have a mobile phone with signal"
,
hint
: {
text
:
"We will text you a 6 digit security code"
}
    },
    {
value
:
"landline"
,
text
:
"No, I want to use my landline"
,
hint
: {
text
:
"We will call you to give you a 6 digit security code"
}
    }
  ]
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### Radio items with a text divider

If 1 or more of your radio options is different from the others, it can help users if you separate them using a text divider. The text is usually the word "or".

- HTML code for radios items with a text divider

- Nunjucks code for radios items with a text divider

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
"example-divider-hint"
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
Have you had all the vaccinations you
&#39;
re eligible for in the UK?
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
"example-divider-hint"
>
You would have got these vaccinations at school, from your GP surgery or another healthcare provider
</
div
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
"example-divider"
name
=
"exampleDivider"
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
"example-divider"
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
"example-divider-2"
name
=
"exampleDivider"
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
"example-divider-2"
>
No
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
"nhsuk-radios__divider"
>
or
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
"example-divider-4"
name
=
"exampleDivider"
type
=
"radio"
value
=
"unknown"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"example-divider-4"
>
I do not know
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
Name id | Type string | Description The ID of the radios component.
Name fieldset | Type object | Description The fieldset used by the radios component. The fieldset.html option is not supported. See macro options for fieldset .
Name hint | Type object | Description Can be used to add a hint to the radios component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the radios component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the radios component. See macro options for form Group .
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each radio input, hint and error message, separated by - . Defaults to the name option value.
Name name | Type string | Description Required. The name attribute for the radio items.
Name items | Type array | Description Required. The radio items within the radios component. See macro options for items .
Name value | Type string | Description The value for the radio which should be checked when the page loads. Use this as an alternative to setting the checked option on each individual item.
Name disabled | Type boolean | Description If true , radio inputs used by the radios component will be disabled.
Name small | Type boolean | Description If set to true , small radios will be used.
Name inline | Type boolean | Description If set to true , inline radios will be used.
Name classes | Type string | Description Classes to add to the radios container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the radios container.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before all radio items within the radios component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after all radio items within the radios component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before all radio items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before all radio items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after all radio items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after all radio items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each radio item label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each radio item label. If html is provided, the text option will be ignored.
Name id | Type string | Description Specific id attribute for the radio item. If omitted, then idPrefix string will be applied.
Name value | Type string | Description Required. The value attribute for the radio input.
Name label | Type object | Description The label used by each radio item within the radios component. The label.size and label.heading options are not supported. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to each radio item within the radios component. See macro options for hint .
Name divider | Type string | Description Divider text to separate radio items, for example the text "or" .
Name checked | Type boolean | Description Whether the radio should be checked when the page loads. Takes precedence over the top-level value option.
Name conditional | Type object | Description Provide additional content to reveal when the radio is checked. See macro options for items conditional .
Name disabled | Type boolean | Description If true , radio will be disabled.
Name classes | Type string | Description Classes to add to the radio input tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the radio input tag.

Name | Type | Description
Name html | Type string | Description Required. The HTML to reveal when the radio is checked.

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
"Have you had all the vaccinations you're eligible for in the UK?"
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
"You would have got these vaccinations at school, from your GP surgery or another healthcare provider"
},
idPrefix
:
"example-divider"
,
name
:
"exampleDivider"
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
},
    {
divider
:
"or"
},
    {
value
:
"unknown"
,
text
:
"I do not know"
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

### Conditionally revealing a related question

You can add a conditionally revealing question to radios, so users only see the question when it's relevant to them.

For example, you could reveal an email address input only when a user chooses to be contacted by email.

- HTML code for radios conditional

- Nunjucks code for radios conditional

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
Select 1 option
</
div
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
"contact"
name
=
"contact"
type
=
"radio"
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
"nhsuk-label nhsuk-radios__label"
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
"nhsuk-radios__conditional nhsuk-radios__conditional--hidden"
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
"nhsuk-radios__item"
>
<
input
class
=
"nhsuk-radios__input"
id
=
"contact-2"
name
=
"contact"
type
=
"radio"
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
"nhsuk-label nhsuk-radios__label"
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
"nhsuk-radios__conditional nhsuk-radios__conditional--hidden"
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
"nhsuk-radios__item"
>
<
input
class
=
"nhsuk-radios__input"
id
=
"contact-3"
name
=
"contact"
type
=
"radio"
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
"nhsuk-label nhsuk-radios__label"
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
"nhsuk-radios__conditional nhsuk-radios__conditional--hidden"
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
Name id | Type string | Description The ID of the radios component.
Name fieldset | Type object | Description The fieldset used by the radios component. The fieldset.html option is not supported. See macro options for fieldset .
Name hint | Type object | Description Can be used to add a hint to the radios component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the radios component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the radios component. See macro options for form Group .
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each radio input, hint and error message, separated by - . Defaults to the name option value.
Name name | Type string | Description Required. The name attribute for the radio items.
Name items | Type array | Description Required. The radio items within the radios component. See macro options for items .
Name value | Type string | Description The value for the radio which should be checked when the page loads. Use this as an alternative to setting the checked option on each individual item.
Name disabled | Type boolean | Description If true , radio inputs used by the radios component will be disabled.
Name small | Type boolean | Description If set to true , small radios will be used.
Name inline | Type boolean | Description If set to true , inline radios will be used.
Name classes | Type string | Description Classes to add to the radios container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the radios container.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before all radio items within the radios component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after all radio items within the radios component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before all radio items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before all radio items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after all radio items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after all radio items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each radio item label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each radio item label. If html is provided, the text option will be ignored.
Name id | Type string | Description Specific id attribute for the radio item. If omitted, then idPrefix string will be applied.
Name value | Type string | Description Required. The value attribute for the radio input.
Name label | Type object | Description The label used by each radio item within the radios component. The label.size and label.heading options are not supported. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to each radio item within the radios component. See macro options for hint .
Name divider | Type string | Description Divider text to separate radio items, for example the text "or" .
Name checked | Type boolean | Description Whether the radio should be checked when the page loads. Takes precedence over the top-level value option.
Name conditional | Type object | Description Provide additional content to reveal when the radio is checked. See macro options for items conditional .
Name disabled | Type boolean | Description If true , radio will be disabled.
Name classes | Type string | Description Classes to add to the radio input tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the radio input tag.

Name | Type | Description
Name html | Type string | Description Required. The HTML to reveal when the radio is checked.

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
"radios/macro.njk"
import
radios
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
radios
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
"Select 1 option"
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

Do not use this component to add conditionally revealing questions to inline radios.

Only conditionally reveal questions. Do not show or hide anything that is not a question.

#### Known issues

Users are not always notified when a conditionally revealed question is shown or hidden. This fails WCAG 2.2 success criterion 4.1.2 name, role, value (W3C)

However, GOV.UK found that screen reader users did not have difficulty answering a conditionally revealed question as long as it's simple. It confused users when they conditionally revealed complicated questions, particularly questions with more than 1 part.

### Smaller radios

- HTML code for radios smaller

- Nunjucks code for radios smaller

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
Filter
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
"nhsuk-radios nhsuk-radios--small"
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
"filter"
name
=
"filter"
type
=
"radio"
value
=
"monthly"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"filter"
>
Monthly
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
"filter-2"
name
=
"filter"
type
=
"radio"
value
=
"yearly"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"filter-2"
>
Yearly
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
Name id | Type string | Description The ID of the radios component.
Name fieldset | Type object | Description The fieldset used by the radios component. The fieldset.html option is not supported. See macro options for fieldset .
Name hint | Type object | Description Can be used to add a hint to the radios component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the radios component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the radios component. See macro options for form Group .
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each radio input, hint and error message, separated by - . Defaults to the name option value.
Name name | Type string | Description Required. The name attribute for the radio items.
Name items | Type array | Description Required. The radio items within the radios component. See macro options for items .
Name value | Type string | Description The value for the radio which should be checked when the page loads. Use this as an alternative to setting the checked option on each individual item.
Name disabled | Type boolean | Description If true , radio inputs used by the radios component will be disabled.
Name small | Type boolean | Description If set to true , small radios will be used.
Name inline | Type boolean | Description If set to true , inline radios will be used.
Name classes | Type string | Description Classes to add to the radios container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the radios container.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before all radio items within the radios component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after all radio items within the radios component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before all radio items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before all radio items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after all radio items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after all radio items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each radio item label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each radio item label. If html is provided, the text option will be ignored.
Name id | Type string | Description Specific id attribute for the radio item. If omitted, then idPrefix string will be applied.
Name value | Type string | Description Required. The value attribute for the radio input.
Name label | Type object | Description The label used by each radio item within the radios component. The label.size and label.heading options are not supported. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to each radio item within the radios component. See macro options for hint .
Name divider | Type string | Description Divider text to separate radio items, for example the text "or" .
Name checked | Type boolean | Description Whether the radio should be checked when the page loads. Takes precedence over the top-level value option.
Name conditional | Type object | Description Provide additional content to reveal when the radio is checked. See macro options for items conditional .
Name disabled | Type boolean | Description If true , radio will be disabled.
Name classes | Type string | Description Classes to add to the radio input tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the radio input tag.

Name | Type | Description
Name html | Type string | Description Required. The HTML to reveal when the radio is checked.

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
"Filter"
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
"filter"
,
name
:
"filter"
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
"monthly"
,
text
:
"Monthly"
},
    {
value
:
"yearly"
,
text
:
"Yearly"
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use standard-sized radios in most cases.

You can use small radios where you need something less visually prominent. For example, on:

- a page of search results where users need to see and change search filters without distracting them from the results

- on information-dense screens in services designed for repeat use, like staff-facing systems

### Error messages

Display an error message if the user has not:

- selected any radios

- answered a conditionally revealed question

Style error messages like this.

- HTML code for radios error message

- Nunjucks code for radios error message

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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the radios component.
Name fieldset | Type object | Description The fieldset used by the radios component. The fieldset.html option is not supported. See macro options for fieldset .
Name hint | Type object | Description Can be used to add a hint to the radios component. See macro options for hint .
Name error Message | Type object | Description Can be used to add an error message to the radios component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name form Group | Type object | Description Additional options for the form group containing the radios component. See macro options for form Group .
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for each radio input, hint and error message, separated by - . Defaults to the name option value.
Name name | Type string | Description Required. The name attribute for the radio items.
Name items | Type array | Description Required. The radio items within the radios component. See macro options for items .
Name value | Type string | Description The value for the radio which should be checked when the page loads. Use this as an alternative to setting the checked option on each individual item.
Name disabled | Type boolean | Description If true , radio inputs used by the radios component will be disabled.
Name small | Type boolean | Description If set to true , small radios will be used.
Name inline | Type boolean | Description If set to true , inline radios will be used.
Name classes | Type string | Description Classes to add to the radios container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the radios container.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Inputs | Type object | Description Content to add before all radio items within the radios component. See macro options for form Group before Inputs .
Name after Inputs | Type object | Description Content to add after all radio items within the radios component. See macro options for form Group after Inputs .

Name | Type | Description
Name text | Type string | Description Required. Text to add before all radio items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before all radio items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after all radio items. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after all radio items. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each radio item label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each radio item label. If html is provided, the text option will be ignored.
Name id | Type string | Description Specific id attribute for the radio item. If omitted, then idPrefix string will be applied.
Name value | Type string | Description Required. The value attribute for the radio input.
Name label | Type object | Description The label used by each radio item within the radios component. The label.size and label.heading options are not supported. See macro options for label .
Name hint | Type object | Description Can be used to add a hint to each radio item within the radios component. See macro options for hint .
Name divider | Type string | Description Divider text to separate radio items, for example the text "or" .
Name checked | Type boolean | Description Whether the radio should be checked when the page loads. Takes precedence over the top-level value option.
Name conditional | Type object | Description Provide additional content to reveal when the radio is checked. See macro options for items conditional .
Name disabled | Type boolean | Description If true , radio will be disabled.
Name classes | Type string | Description Classes to add to the radio input tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the radio input tag.

Name | Type | Description
Name html | Type string | Description Required. The HTML to reveal when the radio is checked.

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

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Follow:

- our guidance on error messages

- GOV.UK design system guidance on error messages for radios

## Progressive enhancement

The radios component uses progressive enhancement and requires JavaScript for enhanced functionality.

When JavaScript is not available, conditionally revealed content will be revealed by default.

## Research

Our radios are based on the GOV.UK design system. Read a GOV.UK blog post about their updates to radios and checkboxes .

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
