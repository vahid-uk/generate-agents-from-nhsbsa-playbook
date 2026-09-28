# Question pages – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/patterns/question-pages/

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

# Pages – Question pages

This pattern explains when to use question pages and the elements they can include.

- HTML code for question pages

- Nunjucks code for question pages

```text
<
div
class
=
"nhsuk-width-container"
>
<
a
class
=
"nhsuk-back-link"
href
=
"#"
>
Back
</
a
>
<
main
class
=
"nhsuk-main-wrapper nhsuk-main-wrapper--s"
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
form
action
=
"/form-handler"
method
=
"post"
novalidate
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
Where do you live?
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
"whereDoYouLive"
name
=
"whereDoYouLive"
type
=
"radio"
value
=
"england"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"whereDoYouLive"
>
England
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
"whereDoYouLive-2"
name
=
"whereDoYouLive"
type
=
"radio"
value
=
"scotland"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"whereDoYouLive-2"
>
Scotland
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
"whereDoYouLive-3"
name
=
"whereDoYouLive"
type
=
"radio"
value
=
"wales"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"whereDoYouLive-3"
>
Wales
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
"whereDoYouLive-4"
name
=
"whereDoYouLive"
type
=
"radio"
value
=
"northern-ireland"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"whereDoYouLive-4"
>
Northern Ireland
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
form
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
"back-link/macro.njk"
import
backLink
%}
{%
from
"button/macro.njk"
import
button
%}
{%
from
"radios/macro.njk"
import
radios
%}
{%
set
mainClasses
=
"nhsuk-main-wrapper--s"
%}
{%
block
beforeContent
%}
{{
backLink
({
href
:
"#"
,
text
:
"Back"
})
}}
{%
endblock
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
<
form
action
=
"/form-handler"
method
=
"post"
novalidate
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
"Where do you live?"
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
name
:
"whereDoYouLive"
,
items
: [
            {
value
:
"england"
,
text
:
"England"
},
            {
value
:
"scotland"
,
text
:
"Scotland"
},
            {
value
:
"wales"
,
text
:
"Wales"
},
            {
value
:
"northern-ireland"
,
text
:
"Northern Ireland"
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
form
>
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

## When to use a question page

Follow this pattern whenever you need to ask users questions in your service.

Make sure you know why you're asking every question and only ask users for information you really need.

On every question page you should:

- make sure it's clear to users why you're asking each question

- allow users to answer "I do not know" or "I'm not sure" if they are valid responses

Read more about:

- making sure you need each question (in our guidance on How to write good questions for forms) , which also covers essential and optional questions

- designing good questions (GOV.UK service manual)

- the question protocol (by Caroline Jarrett on Effortmark website)

## How to use a question page

### Start by asking 1 question per page

Asking just 1 question per page helps users:

- understand what you're asking them to do

- focus on the specific question and its answer

Sometimes it makes sense to group related questions on the same page. User research will tell you when to do this. See the section on asking multiple questions on a page .

### Elements you must include

Question pages must include a:

- back link

- page heading

- way for users to input information

- continue button

#### Back link

Some users do not trust browser back buttons when they're entering data.

Always include a back link component at the top of question pages to reassure users it's possible to go back and change previous answers.

However, do not break the browser back button. Make sure it takes users to the previous page they were on, in the state they last saw it.

An exception to this is when the user has performed an action they should only do once, like make a payment or complete an application. The browser back button should still work, but show the user a sensible message rather than letting them perform the action again.

#### Page heading

Usually the page heading should be the question. Do this by placing the heading ( <h1> ) into the label or legend. Find out about using legends, labels and captions .

Sometimes the page heading will be a statement. Find out more about when to use statements in the sections on:

- asking complex questions without using hint text

- asking multiple questions on a page

#### Input

For example, a text input box, radios or checkboxes .

Make sure to only ask for a piece of information once within a single journey.

If the same type of information is needed more than once, make it easier to reuse previously entered answers by:

- pre-populating the relevant fields

- showing carried-forward responses as an option for the user to select

#### Continue button

Make sure your Continue button is:

- labelled "Continue", not "Next"

- aligned to the left so users do not miss it

### Using legends, labels and captions

For single question pages, using a <legend> or <label> as the page heading is good practice as it means that screen reader users will only hear the contents once. (Use a legend for a group or set of elements as a whole and a label for a specific element, like a text input.)

Read more about why and how to make labels and legends headings (on GOV.UK) or see the examples below.

Learn how to set label and legend sizes on the typography page .

Here's an example of a question page with a legend as the page heading.

- HTML code for question pages legend page heading

- Nunjucks code for question pages legend page heading

```text
<
div
class
=
"nhsuk-width-container"
>
<
a
class
=
"nhsuk-back-link"
href
=
"#"
>
Back
</
a
>
<
main
class
=
"nhsuk-main-wrapper nhsuk-main-wrapper--s"
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
form
action
=
"/form-handler"
method
=
"post"
novalidate
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
role
=
"group"
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
What is your date of birth?
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
For example, 15 3 1984
</
div
>
<
div
class
=
"nhsuk-date-input"
id
=
"example"
>
<
div
class
=
"nhsuk-date-input__item"
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
"nhsuk-label nhsuk-date-input__label"
for
=
"example-day"
>
Day
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--width-2 nhsuk-date-input__input"
id
=
"example-day"
name
=
"example[day]"
type
=
"text"
inputmode
=
"numeric"
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
"nhsuk-date-input__item"
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
"nhsuk-label nhsuk-date-input__label"
for
=
"example-month"
>
Month
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--width-2 nhsuk-date-input__input"
id
=
"example-month"
name
=
"example[month]"
type
=
"text"
inputmode
=
"numeric"
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
"nhsuk-date-input__item"
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
"nhsuk-label nhsuk-date-input__label"
for
=
"example-year"
>
Year
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--width-4 nhsuk-date-input__input"
id
=
"example-year"
name
=
"example[year]"
type
=
"text"
inputmode
=
"numeric"
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
form
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
"back-link/macro.njk"
import
backLink
%}
{%
from
"button/macro.njk"
import
button
%}
{%
from
"date-input/macro.njk"
import
dateInput
%}
{%
set
mainClasses
=
"nhsuk-main-wrapper--s"
%}
{%
block
beforeContent
%}
{{
backLink
({
href
:
"#"
,
text
:
"Back"
})
}}
{%
endblock
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
<
form
action
=
"/form-handler"
method
=
"post"
novalidate
>
{{
dateInput
({
fieldset
: {
legend
: {
text
:
"What is your date of birth?"
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
"For example, 15 3 1984"
},
id
:
"example"
,
namePrefix
:
"example"
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
form
>
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

This is an example of a question page with a label as the page heading.

- HTML code for question pages label page heading

- Nunjucks code for question pages label page heading

```text
<
div
class
=
"nhsuk-width-container"
>
<
a
class
=
"nhsuk-back-link"
href
=
"#"
>
Back
</
a
>
<
main
class
=
"nhsuk-main-wrapper nhsuk-main-wrapper--s"
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
form
action
=
"/form-handler"
method
=
"post"
novalidate
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
"postcode"
>
What is your home postcode?
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
"nhsuk-input nhsuk-input--width-10"
id
=
"postcode"
name
=
"postcode"
type
=
"text"
autocomplete
=
"postal-code"
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
form
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
"back-link/macro.njk"
import
backLink
%}
{%
from
"button/macro.njk"
import
button
%}
{%
from
"input/macro.njk"
import
input
%}
{%
set
mainClasses
=
"nhsuk-main-wrapper--s"
%}
{%
block
beforeContent
%}
{{
backLink
({
href
:
"#"
,
text
:
"Back"
})
}}
{%
endblock
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
<
form
action
=
"/form-handler"
method
=
"post"
novalidate
>
{{
input
({
label
: {
text
:
"What is your home postcode?"
,
size
:
"l"
,
isPageHeading
:
true
},
id
:
"postcode"
,
name
:
"postcode"
,
width
:
10
,
autocomplete
:
"postal-code"
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
form
>
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

Do not use the same page heading across multiple pages. The page heading should relate specifically to the information being asked for on the current page, not any higher-level section the page is part of.

If you need to show the high-level section, you can use an nhsuk-caption style. See headings with captions (on the Typography page) .

In this example, the heading has the caption "About you" above it.

```text
<
span
class
=
"nhsuk-caption-l"
>
About you
</
span
>
<
h1
class
=
"nhsuk-heading-l"
>
What is your home address?
</
h1
>
```

### Helping users answer questions

#### Using hint text

Use hint text to show information that helps the majority of users answer the question, like how their information will be used or where to find it.

#### Asking complex questions without using hint text

If you're asking a question that needs a detailed explanation, use:

- an <h1> heading that's a statement (for example, "If we need to contact you") rather than a question

- whatever mix of text, paragraphs, lists and examples best explains your question to users

- a label, above the form input, that asks users a specific question, for example, "Do you have any communication needs?"

- HTML code for question pages complex question

- Nunjucks code for question pages complex question

```text
<
div
class
=
"nhsuk-width-container"
>
<
a
class
=
"nhsuk-back-link"
href
=
"#"
>
Back
</
a
>
<
main
class
=
"nhsuk-main-wrapper nhsuk-main-wrapper--s"
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
h1
class
=
"nhsuk-heading-l"
>
If we need to contact you
</
h1
>
<
p
>
Let us know if you have any communication needs you'd like us to be aware of. For example, a hearing or visual impairment.
</
p
>
<
form
action
=
"/form-handler"
method
=
"post"
novalidate
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
>
<
legend
class
=
"nhsuk-fieldset__legend nhsuk-fieldset__legend--m"
>
Do you have any communication needs?
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
"contactNeeds"
name
=
"contactNeeds"
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
"contactNeeds"
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
"contactNeeds-2"
name
=
"contactNeeds"
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
"contactNeeds-2"
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
form
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
"back-link/macro.njk"
import
backLink
%}
{%
from
"button/macro.njk"
import
button
%}
{%
from
"radios/macro.njk"
import
radios
%}
{%
set
mainClasses
=
"nhsuk-main-wrapper--s"
%}
{%
block
beforeContent
%}
{{
backLink
({
href
:
"#"
,
text
:
"Back"
})
}}
{%
endblock
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
<
h1
class
=
"nhsuk-heading-l"
>
If we need to contact you
</
h1
>
<
p
>
Let us know if you have any communication needs you'd like us to be aware of. For example, a hearing or visual impairment.
</
p
>
<
form
action
=
"/form-handler"
method
=
"post"
novalidate
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
"Do you have any communication needs?"
,
size
:
"m"
}
          },
name
:
"contactNeeds"
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
{{
button
({
text
:
"Continue"
})
}}
</
form
>
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

### Asking multiple questions on a page

Sometimes it makes sense to group related questions on the same page. For example, if you're designing an internal service for staff who need to repeat and switch between tasks quickly.

If you need to ask for multiple related things on a page, use a statement as the heading.

You can style each <legend> or <label> to make the questions easier to scan. Read more about why and how to style labels and legends headings (on GOV.UK) .

- HTML code for question pages multiple questions

- Nunjucks code for question pages multiple questions

```text
<
div
class
=
"nhsuk-width-container"
>
<
a
class
=
"nhsuk-back-link"
href
=
"#"
>
Back
</
a
>
<
main
class
=
"nhsuk-main-wrapper nhsuk-main-wrapper--s"
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
h1
class
=
"nhsuk-heading-l"
>
Your details
</
h1
>
<
p
>
You've told us you are the carer. We need your details.
</
p
>
<
form
action
=
"/form-handler"
method
=
"post"
novalidate
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
"nhsuk-label nhsuk-label--s"
for
=
"example"
>
First name
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
"example"
name
=
"example"
type
=
"text"
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
"nhsuk-label nhsuk-label--s"
for
=
"example1"
>
Last name
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
"example1"
name
=
"example1"
type
=
"text"
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
"nhsuk-label nhsuk-label--s"
for
=
"example2"
>
Relationship to the person being registered
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
"example2-hint"
>
For example, a family member or friend
</
div
>
<
input
class
=
"nhsuk-input"
id
=
"example2"
name
=
"example2"
type
=
"text"
aria-describedby
=
"example2-hint"
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
"nhsuk-label nhsuk-label--s"
for
=
"example3"
>
Contact phone number
</
label
>
<
input
class
=
"nhsuk-input nhsuk-input--width-20"
id
=
"example3"
name
=
"example3"
type
=
"tel"
autocomplete
=
"tel"
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
form
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
"back-link/macro.njk"
import
backLink
%}
{%
from
"button/macro.njk"
import
button
%}
{%
from
"input/macro.njk"
import
input
%}
{%
set
mainClasses
=
"nhsuk-main-wrapper--s"
%}
{%
block
beforeContent
%}
{{
backLink
({
href
:
"#"
,
text
:
"Back"
})
}}
{%
endblock
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
<
h1
class
=
"nhsuk-heading-l"
>
Your details
</
h1
>
<
p
>
You've told us you are the carer. We need your details.
</
p
>
<
form
action
=
"/form-handler"
method
=
"post"
novalidate
>
{{
input
({
label
: {
text
:
"First name"
,
size
:
"s"
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
{{
input
({
label
: {
text
:
"Last name"
,
size
:
"s"
},
id
:
"example1"
,
name
:
"example1"
})
}}
{{
input
({
label
: {
text
:
"Relationship to the person being registered"
,
size
:
"s"
},
hint
: {
text
:
"For example, a family member or friend"
},
id
:
"example2"
,
name
:
"example2"
})
}}
{{
input
({
label
: {
text
:
"Contact phone number"
,
size
:
"s"
},
id
:
"example3"
,
name
:
"example3"
,
width
:
20
,
type
:
"tel"
,
autocomplete
:
"tel"
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
form
>
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

### Using progress indicators

Start by testing your form without a progress indicator to see if it's simple enough that users do not need one.

Try improving the order, type or number of questions before adding a progress indicator. If people still have difficulty, try adding a simple step or question indicator like this one.

```text
<
span
class
=
"nhsuk-caption-l"
>
Question 3 of 9
</
span
>
<
h1
class
=
"nhsuk-heading-l"
>
Your details
</
h1
>
```

Only include the total number of questions if you can do so reliably. As the user moves through the form, make sure the indicator updates to tell them which question they are on and the total number remaining.

Do not use progress indicators, like this one, that show all the questions at once.

These can be problematic because they:

- are often not noticed

- take up lots of space

- do not scale well on small screens

- can distract and confuse some users

- make it hard to write good labels for the steps

- make it hard to handle conditional sections

### Using range sliders

Avoid using range slider questions, where the user needs to click and drag a selector across a range of answers or values. These types of controls are difficult for some users to interact with.

If you do use a range slider, you must provide a method for selecting an answer that does not rely on click and drag movements. This relates to WCAG 2.2 success criterion 2.5.7 Dragging movements (W3C) .

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
