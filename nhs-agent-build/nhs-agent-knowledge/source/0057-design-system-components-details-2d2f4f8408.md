# Details – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/details/

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

# Content presentation – Details

Make a page easier to scan by letting users reveal more detailed information only if they need it.

- HTML code for details

- Nunjucks code for details

```text
<
details
class
=
"nhsuk-details"
>
<
summary
class
=
"nhsuk-details__summary"
>
<
span
class
=
"nhsuk-details__summary-text"
>
How to find your NHS number
</
span
>
</
summary
>
<
div
class
=
"nhsuk-details__text"
>
<
p
>
An NHS number is a 10 digit number, like
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
.
</
p
>
<
p
>
You can find your NHS number by logging in to the NHS App or on any document the NHS has sent you, such as your:
</
p
>
<
ul
>
<
li
>
prescriptions
</
li
>
<
li
>
test results
</
li
>
<
li
>
hospital referral letters
</
li
>
<
li
>
appointment letters
</
li
>
</
ul
>
<
p
>
Ask your GP surgery for help if you cannot find your NHS number.
</
p
>
</
div
>
</
details
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name summary | Type object | Description Summary element content (the visible part of the details element). See macro options for summary .
Name summary Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the summary.text option.
Name summary Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the summary.html option.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the disclosed part of the details element. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the disclosed part of the details element. If html is provided, the text option will be ignored.
Name id | Type string | Description The id to add to the details element.
Name open | Type boolean | Description If true , details element will be expanded.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire details component in a call block.
Name variant | Type string | Description Optional variant of details. You can use only "reverse" or empty values with this option.
Name classes | Type string | Description Classes to add to the details element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the details element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the summary element (the visible part of the details element). If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the summary element (the visible part of the details element). If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the summary element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the summary element.

```text
{%
from
"details/macro.njk"
import
details
%}
{%
set
dummyNhsNumber
=
"999 123 4567"
%}
{%
call
details
({
summary
:
"How to find your NHS number"
}) %}
<
p
>
An NHS number is a 10 digit number, like
<
span
class
=
"nhsuk-u-nowrap"
>
{{
dummyNhsNumber
}}
</
span
>
.
</
p
>
<
p
>
You can find your NHS number by logging in to the NHS App or on any document the NHS has sent you, such as your:
</
p
>
<
ul
>
<
li
>
prescriptions
</
li
>
<
li
>
test results
</
li
>
<
li
>
hospital referral letters
</
li
>
<
li
>
appointment letters
</
li
>
</
ul
>
<
p
>
Ask your GP surgery for help if you cannot find your NHS number.
</
p
>
{%
endcall
%}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## When to use details

There are 2 ways to let users reveal more information:

- details

- expander

Use the details component to make a page easier to scan when it contains information that only some users will need. For example, use it to give users help in context .

## When not to use details

Do not use details to hide information that most users will need.

## How to use details

The details component is a short link that expands to show more text when a user clicks on it.

Make the link text short and descriptive so users can quickly work out if they need to click on it.

## Details and expanders

Details and expanders both hide sections of content which a user can choose to reveal.

The details component is less visually prominent than an expander, so tends to work better for content which is not as important to users.

Users may be reluctant to click on the details component in forms. Read more in the research section below.

## Research

User research has shown us that users understand the purpose of the component and are able to use it.

Anecdotally we've heard users being reluctant to expand the details component in user testing sessions for transactional services (forms). When asked why they wouldn't click, they explained that they thought the link text (blue underlined text) would take them to a new page and they would lose their progress.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
