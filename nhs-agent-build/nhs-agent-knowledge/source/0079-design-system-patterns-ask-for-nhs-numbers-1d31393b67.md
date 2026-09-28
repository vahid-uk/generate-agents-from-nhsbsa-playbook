# NHS numbers – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/patterns/ask-for-nhs-numbers/

## Source content

## Ask users for

- NHS numbers

## Help users to

- Check answers

- Complete multiple tasks

- Decide when and where to get care (care cards)

- Find British Sign Language content

- Know that a page is up to date

## Pages

- A to Z page

- Confirmation page

- Hub page

- Interruption page

- Mini-hub

- Question pages

- Start page

# Ask users for – NHS numbers

Use this pattern to ask people for their NHS number and help them find it.

## When to use the NHS number pattern

Follow this pattern when you need to ask for an NHS number.

Weigh up user and business needs and clinical risk in deciding whether to ask users for their NHS number. Asking users for their NHS number is the best way to identify a patient and minimise the risks of matching the wrong person but:

- users do not need to know their NHS number to get care

- some users do not know their number and cannot find it easily

Use this pattern if users are more likely to succeed in their journey by giving you their NHS number. Provide another route for users who cannot.

To minimise the risks of a wrong match, do not rely on an NHS number on its own.

## When not to use the NHS number pattern

Weigh up user and business needs and clinical risk. If users are more likely to succeed by providing other details instead of their NHS number, it may be better not to use this pattern.

Do not use this pattern if you need to digitally authenticate members of the public logging into a product or service. Use NHS login instead.

## How to use the NHS number pattern

There are 3 ways of asking users for their NHS number:

- single text input

- filter question before input

- filter question before input with a 3rd option

### Single text input

Use a single text input if the only way users can get the service is by entering their NHS number.

However, avoid building a service that relies on users entering their NHS number. If possible, give users another way to continue with their journey, and use a filter question instead.

- HTML code for ask for nhs numbers

- Nunjucks code for ask for nhs numbers

```text
<
div
class
=
"nhsuk-width-container"
>
<
main
class
=
"nhsuk-main-wrapper"
id
=
"maincontent"
>
<
div
class
=
"nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-two-thirds"
>
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
"nhsNumber"
type
=
"text"
spellcheck
=
"false"
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
<
button
class
=
"nhsuk-button"
data-module
=
"nhsuk-button"
type
=
"submit"
>
Continue
</
button
>
</
div
>
</
div
>
</
main
>
</
div
>
```

```text
{%
from
"input/macro.njk"
import
input
%}
{%
from
"button/macro.njk"
import
button
%}
{%
set
dummyNhsNumber
=
"999 123 4567"
%}
{%
block
content
%}
<
div
class
=
"nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-two-thirds"
>
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
"nhsNumber"
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
{{
button
({
text
:
"Continue"
})
}}
</
div
>
</
div
>
{%
endblock
%}
```

If you have no other option and must use a single text input:

- label it "What is your NHS number?" or "Enter your NHS number"

- help users recognise their NHS number and know the correct details to enter, for example with hint text

- tell users where they can find their NHS number before they start the service, as well as during the journey

### Filter question before single text input

Use a filter question before a single text input if there is another way for users to continue without an NHS number.

Use a 2-option radio button that asks the user if they know their NHS number.

- HTML code for ask for nhs numbers filter

- Nunjucks code for ask for nhs numbers filter

```text
<
div
class
=
"nhsuk-width-container"
>
<
main
class
=
"nhsuk-main-wrapper"
id
=
"maincontent"
>
<
div
class
=
"nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-two-thirds"
>
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
Do you know your NHS number?
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
Yes, I know my NHS number
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
No, continue without
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
<
button
class
=
"nhsuk-button"
data-module
=
"nhsuk-button"
type
=
"submit"
>
Continue
</
button
>
</
div
>
</
div
>
</
main
>
</
div
>
```

```text
{%
from
"button/macro.njk"
import
button
%}
{%
from
"hint/macro.njk"
import
hint
%}
{%
from
"fieldset/macro.njk"
import
fieldset
%}
{%
from
"radios/macro.njk"
import
radios
%}
{%
set
dummyNhsNumber
=
"999 123 4567"
%}
{%
block
content
%}
<
div
class
=
"nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-two-thirds"
>
{{
radios
({
fieldset
: {
legend
: {
text
:
"Do you know your NHS number?"
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
html
:
'This is a 10 digit number (like <span class="nhsuk-u-nowrap">'
~ dummyNhsNumber ~
'</span>) that you can find on an NHS letter, prescription or in the NHS App'
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
"Yes, I know my NHS number"
},
        {
value
:
"no"
,
text
:
"No, continue without"
}
      ]
      })
}}
{{
button
({
text
:
"Continue"
})
}}
</
div
>
</
div
>
{%
endblock
%}
```

If users know their NHS number, direct them to a page that asks for it.

- HTML code for ask for nhs numbers filter single

- Nunjucks code for ask for nhs numbers filter single

```text
<
div
class
=
"nhsuk-width-container"
>
<
main
class
=
"nhsuk-main-wrapper"
id
=
"maincontent"
>
<
div
class
=
"nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-two-thirds"
>
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
Your NHS number is a 10 digit number, for example
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
input
class
=
"nhsuk-input nhsuk-input--code nhsuk-input--width-10"
id
=
"nhs-number"
name
=
"nhsNumber"
type
=
"text"
spellcheck
=
"false"
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
<
button
class
=
"nhsuk-button"
data-module
=
"nhsuk-button"
type
=
"submit"
>
Continue
</
button
>
</
div
>
</
div
>
</
main
>
</
div
>
```

```text
{%
from
"input/macro.njk"
import
input
%}
{%
from
"button/macro.njk"
import
button
%}
{%
set
dummyNhsNumber
=
"999 123 4567"
%}
{%
block
content
%}
<
div
class
=
"nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-two-thirds"
>
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
'Your NHS number is a 10 digit number, for example <span class="nhsuk-u-nowrap">'
~ dummyNhsNumber ~
"</span>"
},
id
:
"nhs-number"
,
name
:
"nhsNumber"
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
{{
button
({
text
:
"Continue"
})
}}
</
div
>
</
div
>
{%
endblock
%}
```

If users do not know their NHS number, direct them to a page that asks for the alternative details your service needs, for example postcode and date of birth. It may help to set expectations on the filter question page by telling users what details you will ask them for so they can complete their journey.

### Filter question before input with 3rd option

Some users may benefit from a 3rd option: "I'm not sure".

Only use this if:

- you can demonstrate a clear user need and business value

- your service can offer an alternative journey for "not sure" users

Do not use a 3rd option to signpost to general information about NHS numbers.

- HTML code for ask for nhs numbers filter third

- Nunjucks code for ask for nhs numbers filter third

```text
<
div
class
=
"nhsuk-width-container"
>
<
main
class
=
"nhsuk-main-wrapper"
id
=
"maincontent"
>
<
div
class
=
"nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-two-thirds"
>
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
Do you know your NHS number?
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
"example-hints"
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
Yes, I know my NHS number
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
"example-hints"
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
No, I do not know my NHS number
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
"example-hints"
type
=
"radio"
value
=
"not sure"
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
I
&#39;
m not sure
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
</
div
>
</
div
>
</
main
>
</
div
>
```

```text
{%
from
"button/macro.njk"
import
button
%}
{%
from
"hint/macro.njk"
import
hint
%}
{%
from
"fieldset/macro.njk"
import
fieldset
%}
{%
from
"radios/macro.njk"
import
radios
%}
{%
set
dummyNhsNumber
=
"999 123 4567"
%}
{%
block
content
%}
<
div
class
=
"nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-two-thirds"
>
{{
radios
({
fieldset
: {
legend
: {
text
:
"Do you know your NHS number?"
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
html
:
'This is a 10 digit number (like <span class="nhsuk-u-nowrap">'
~ dummyNhsNumber ~
'</span>) that you can find on an NHS letter, prescription or in the NHS App'
},
idPrefix
:
"example-hints"
,
name
:
"example-hints"
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
"Yes, I know my NHS number"
},
          {
value
:
"no"
,
text
:
"No, I do not know my NHS number"
},
          {
value
:
"not sure"
,
text
:
"I'm not sure"
}
        ]
      })
}}
</
div
>
</
div
>
{%
endblock
%}
```

### How to build the NHS number pattern

When asking for an NHS number:

- use a text input that allows for spaces and other characters between numbers, as users will enter it in different ways (for example with dashes)

- allow at least 12 characters in your NHS number input

- check that the NHS number is valid by using a modulus 11 algorithm (explained on the NHS number page in the NHS Data Model and Dictionary)

- keep the NHS number on 1 line – if you use the NHS frontend library or prototype kit, use this HTML code to stop the number from breaking up over 2 lines: <span class="nhsuk-u-nowrap">999 123 4567</span>

- add the inputmode="numeric" attribute to your input so people can use a numeric keyboard on mobile browsers

- add <meta name="format-detection" content="telephone=no"> to your page to turn off automatic detection of possible phone numbers (including the NHS number) in Safari

### Help users find and recognise their NHS number

Explain where users can find their NHS number and what it looks like. Use hint text on the filter question page and the single text input page.

Users are more successful the earlier you mention that you will ask for their NHS number and where to find it. For example, explain on your service start page that having their NHS number is useful, but they do not need it.

You do not need your NHS number but entering it will give us the best chance of matching you to your NHS record. You can find your NHS number on an NHS letter, prescription or in the NHS App.

### Use the correct NHS number format

Write the NHS number as 3 groups of numbers, with a single space between them, like this: 999 123 4567.

We include an example NHS number in this pattern. 999 123 4567 is the preferred example number. If you include an example number, you must use a number that starts with 9 as these numbers are used for testing, not for real patients. Use the same number for all examples.

If you are displaying an NHS number a user has entered, show it in this format, not the way the user entered it.

Read more about how to format the NHS number in the A to Z of NHS health writing.

### Write clear error messages

Make sure you use clear error messages and error summaries when you ask users for their NHS number.

- HTML code for ask for nhs numbers error

- Nunjucks code for ask for nhs numbers error

```text
<
div
class
=
"nhsuk-width-container"
>
<
main
class
=
"nhsuk-main-wrapper"
id
=
"maincontent"
>
<
div
class
=
"nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-two-thirds"
>
<
div
class
=
"nhsuk-error-summary"
data-module
=
"nhsuk-error-summary"
>
<
div
role
=
"alert"
>
<
h2
class
=
"nhsuk-error-summary__heading"
>
There is a problem
</
h2
>
<
div
class
=
"nhsuk-error-summary__body"
>
<
ul
class
=
"nhsuk-list nhsuk-error-summary__list"
>
<
li
>
<
a
href
=
"#nhs-number"
>
Your NHS number is too long
</
a
>
</
li
>
</
ul
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
<
div
class
=
"nhsuk-form-group nhsuk-form-group--error"
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
span
class
=
"nhsuk-error-message"
id
=
"nhs-number-error"
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
Your NHS number is too long
</
span
>
<
input
class
=
"nhsuk-input nhsuk-input--code nhsuk-input--error nhsuk-input--width-10"
id
=
"nhs-number"
name
=
"nhsNumber"
type
=
"text"
spellcheck
=
"false"
aria-describedby
=
"nhs-number-hint nhs-number-error"
inputmode
=
"numeric"
>
</
div
>
<
button
class
=
"nhsuk-button"
data-module
=
"nhsuk-button"
type
=
"submit"
>
Continue
</
button
>
</
div
>
</
div
>
</
main
>
</
div
>
```

```text
{%
from
"input/macro.njk"
import
input
%}
{%
from
"button/macro.njk"
import
button
%}
{%
from
"error-summary/macro.njk"
import
errorSummary
%}
{%
set
dummyNhsNumber
=
"999 123 4567"
%}
{%
block
content
%}
<
div
class
=
"nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-two-thirds"
>
{{
errorSummary
({
titleText
:
"There is a problem"
,
errorList
: [
          {
text
:
"Your NHS number is too long"
,
href
:
"#nhs-number"
}
        ]
      })
}}
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
errorMessage
: {
text
:
"Your NHS number is too long"
},
id
:
"nhs-number"
,
name
:
"nhsNumber"
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
{{
button
({
text
:
"Continue"
})
}}
</
div
>
</
div
>
{%
endblock
%}
```

You should tell users if:

- they have included letters

- they have entered a number that is too short or too long (not including spaces)

You should check:

- if the user has entered a National Insurance number and tell them if they have

- if their NHS number is valid against a modulus 11 algorithm

## Matching patient data

If you're building products and services that need to access or manage patient demographic data, you must use the Personal Demographic Service (PDS). Read more about PDS .

## Research

Our research showed that many people know their NHS number, can find it quickly and would rather enter it than other details. But some users:

- do not know what their NHS number looks like

- cannot easily find it

- try to enter their National Insurance number or a Scottish CHI (Community Health Index) number

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: November 2025
