# Fieldset – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/fieldset/

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

# Form elements – Fieldset

Use a fieldset to group related form inputs.

## When to use a fieldset

Use a fieldset when you need to show a relationship between multiple form inputs. For example, to group a set of text inputs into a single fieldset when asking for an address or a date .

- HTML code for fieldset

- Nunjucks code for fieldset

```text
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
What is your address?
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
"nhsuk-form-group"
>
<
label
class
=
"nhsuk-label"
for
=
"address-line-1"
>
Address line 1
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
"address-line-1"
name
=
"addressLine1"
type
=
"text"
autocomplete
=
"address-line1"
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
"address-line-2"
>
Address line 2 (optional)
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
"address-line-2"
name
=
"addressLine2"
type
=
"text"
autocomplete
=
"address-line2"
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
"address-town"
>
Town or city
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
"address-town"
name
=
"addressTown"
type
=
"text"
autocomplete
=
"address-level2"
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
"address-postcode"
>
Postcode
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
"address-postcode"
name
=
"addressPostcode"
type
=
"text"
spellcheck
=
"false"
autocomplete
=
"postal-code"
>
</
div
>
</
fieldset
>
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the fieldset.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name legend | Type object | Description The legend for the fieldset component. See macro options for legend .
Name classes | Type string | Description Classes to add to the fieldset container.
Name role | Type string | Description Optional ARIA role attribute.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the fieldset container.
Name html | Type string | Description HTML to use within the fieldset element.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire fieldset component in a call block.

Name | Type | Description
Name id | Type string | Description The ID of the legend.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the legend. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the legend. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire legend component in a call block.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the legend.
Name caption | Type object | Description Optional caption for the legend. See macro options for caption .
Name size | Type string | Description Size of the legend – "s" , "m" , "l" or "xl" .
Name heading | Type object | Description Whether the legend also acts as a heading. See macro options for heading .
Name is Page Heading | Type boolean | Description Deprecated in 10.6.1 (see GitHub) . Replaced by the heading option.
Name classes | Type string | Description Classes to add to the legend.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the legend.

```text
{%
from
"fieldset/macro.njk"
import
fieldset
%}
{%
from
"input/macro.njk"
import
input
%}
{%
call
fieldset
({
legend
: {
text
:
"What is your address?"
,
size
:
"l"
,
isPageHeading
:
true
}
}) %}
{{
input
({
label
: {
text
:
"Address line 1"
},
id
:
"address-line-1"
,
name
:
"addressLine1"
,
autocomplete
:
"address-line1"
})
}}
{{
input
({
label
: {
text
:
"Address line 2 (optional)"
},
id
:
"address-line-2"
,
name
:
"addressLine2"
,
autocomplete
:
"address-line2"
})
}}
{{
input
({
label
: {
text
:
"Town or city"
},
classes
:
"nhsuk-u-width-two-thirds"
,
id
:
"address-town"
,
name
:
"addressTown"
,
autocomplete
:
"address-level2"
})
}}
{{
input
({
label
: {
text
:
"Postcode"
},
id
:
"address-postcode"
,
name
:
"addressPostcode"
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
{%
endcall
%}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

## How to use a fieldset

The 1st element in a fieldset must be a <legend> which describes the group of inputs. This could be a question, such as "What is your address?" or a statement like "Personal details".

If you are asking just 1 question per page as we recommend, you can set the contents of the <legend> as the page heading. You can see an example below. This is good practice as it means that users of screen readers will only hear the contents once.

Read more about why and how to set legends as headings on the GOV.UK Design System.

- HTML code for fieldset as heading

- Nunjucks code for fieldset as heading

```text
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
What is your address?
</
h1
>
</
legend
>
</
fieldset
>
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the fieldset.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name legend | Type object | Description The legend for the fieldset component. See macro options for legend .
Name classes | Type string | Description Classes to add to the fieldset container.
Name role | Type string | Description Optional ARIA role attribute.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the fieldset container.
Name html | Type string | Description HTML to use within the fieldset element.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire fieldset component in a call block.

Name | Type | Description
Name id | Type string | Description The ID of the legend.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the legend. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the legend. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire legend component in a call block.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the legend.
Name caption | Type object | Description Optional caption for the legend. See macro options for caption .
Name size | Type string | Description Size of the legend – "s" , "m" , "l" or "xl" .
Name heading | Type object | Description Whether the legend also acts as a heading. See macro options for heading .
Name is Page Heading | Type boolean | Description Deprecated in 10.6.1 (see GitHub) . Replaced by the heading option.
Name classes | Type string | Description Classes to add to the legend.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the legend.

```text
{%
from
"fieldset/macro.njk"
import
fieldset
%}
{{
fieldset
({
legend
: {
text
:
"What is your address?"
,
size
:
"l"
,
isPageHeading
:
true
}
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

## Accessibility

On question pages containing a set of inputs, group them using a <fieldset> and include the question as the <legend> . This helps screen reader users understand that the inputs are all related to that question.

Include any important general help text in the legend if it would help the user fill in the form, and you cannot write it as hint text . Keep it as short as possible because screen readers may repeat the legend for each input in the fieldset.

## Research

If you have used this component, get in touch to share your user research findings .

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: November 2025
