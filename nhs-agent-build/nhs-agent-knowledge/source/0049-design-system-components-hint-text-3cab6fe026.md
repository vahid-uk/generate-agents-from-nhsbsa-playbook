# Hint text – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/hint-text/

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

# Form elements – Hint text

Use hint text to help users understand a question.

- HTML code for hint text

- Nunjucks code for hint text

```text
<
div
class
=
"nhsuk-hint"
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the hint. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the hint. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire hint component in a call block.
Name id | Type string | Description The id attribute to add to the hint.
Name classes | Type string | Description Classes to add to the hint.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the hint.

```text
{%
from
"hint/macro.njk"
import
hint
%}
{%
set
dummyNhsNumber
=
"999 123 4567"
%}
{{
hint
({
html
:
'This is a 10 digit number (like <span class="nhsuk-u-nowrap">'
~ dummyNhsNumber ~
'</span>) that you can find on an NHS letter, prescription or in the NHS App'
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## How to use hint text

Use hint text to show information that helps the majority of users answer the question. Use it to give users help in context .

Keep each hint to a single short phrase or sentence, without full stops.

If you need to give a long, detailed explanation, do not use hint text. Screen readers will read out the entire text when users interact with the form element. This could frustrate users if the text is long.

Do not use links in hint text. While screen readers will read out the link text, they usually do not tell users the text is a link.

Do not use other interactive elements such as the details component in hint text. When screen reader users are in "form mode", they are unable to interact with the link in the component.

### Text input with hint text

- HTML code for hint text input

- Nunjucks code for hint text input

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
"example-with-hint-text"
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
"example-with-hint-text-hint"
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
inputmode
=
"numeric"
>
</
div
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the hint. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the hint. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire hint component in a call block.
Name id | Type string | Description The id attribute to add to the hint.
Name classes | Type string | Description Classes to add to the hint.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the hint.

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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Radios with hint text

- HTML code for hint text radios

- Nunjucks code for hint text radios

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
"example-hints-hint"
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
"example-hints"
name
=
"exampleHints"
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
"example-hints"
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
"example-hints-2"
name
=
"exampleHints"
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
"example-hints-2"
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
"example-hints-4"
name
=
"exampleHints"
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
"example-hints-4"
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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the hint. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the hint. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire hint component in a call block.
Name id | Type string | Description The id attribute to add to the hint.
Name classes | Type string | Description Classes to add to the hint.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the hint.

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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Radio items with hints

You can add hints to radios to give more information about the options.

- HTML code for hint text radio item with hints

- Nunjucks code for hint text radio item with hints

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
How do you want to sign in?
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
"gateway"
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
Sign in with NHS login
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
You
&#39;
ll have a user ID if you
&#39;
ve registered for the NHS App
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
"verify"
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
Sign in with GOV.UK Verify
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
You
&#39;
ll have an account if you
&#39;
ve already proved your identity with either Barclays, CitizenSafe, Digidentity, Experian, Post Office, Royal Mail or SecureIdentity
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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the hint. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the hint. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire hint component in a call block.
Name id | Type string | Description The id attribute to add to the hint.
Name classes | Type string | Description Classes to add to the hint.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the hint.

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
"How do you want to sign in?"
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
"gateway"
,
text
:
"Sign in with NHS login"
,
hint
: {
text
:
"You'll have a user ID if you've registered for the NHS App"
}
    },
    {
value
:
"verify"
,
text
:
"Sign in with GOV.UK Verify"
,
hint
: {
text
:
"You'll have an account if you've already proved your identity with either Barclays, CitizenSafe, Digidentity, Experian, Post Office, Royal Mail or SecureIdentity"
}
    }
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Checkboxes with hint text

Unlike with radios , users can select more than 1 option from a list of checkboxes . Do not assume that users will know how many options they can select.

- HTML code for hint text checkboxes

- Nunjucks code for hint text checkboxes

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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the hint. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the hint. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire hint component in a call block.
Name id | Type string | Description The id attribute to add to the hint.
Name classes | Type string | Description Classes to add to the hint.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the hint.

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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Textarea with hint text

- HTML code for hint text textarea

- Nunjucks code for hint text textarea

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
Can you provide more detail about how you move around (your mobility)?
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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the hint. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the hint. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire hint component in a call block.
Name id | Type string | Description The id attribute to add to the hint.
Name classes | Type string | Description Classes to add to the hint.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the hint.

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
"Can you provide more detail about how you move around (your mobility)?"
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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: November 2025
