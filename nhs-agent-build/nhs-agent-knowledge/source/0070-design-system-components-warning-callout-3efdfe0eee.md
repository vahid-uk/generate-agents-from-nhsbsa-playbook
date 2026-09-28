# Warning callout – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/warning-callout/

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

# Content presentation – Warning callout

Use a warning callout to help users identify and understand warning content on the page, even if they do not read the whole page.

- HTML code for warning callout custom heading

- Nunjucks code for warning callout custom heading

```text
<
div
class
=
"nhsuk-card nhsuk-card--warning"
>
<
div
class
=
"nhsuk-card__content"
>
<
h3
class
=
"nhsuk-card__heading"
>
<
span
role
=
"text"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Important:
</
span
>
School, nursery or work
</
span
>
</
h3
>
<
p
class
=
"nhsuk-card__description"
>
Stay away from school, nursery or work until all the spots have crusted over. This is usually 5 days after the spots first appeared.
</
p
>
</
div
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
Name id | Type string | Description The ID of the warning callout.
Name heading | Type object | Description Required. Heading to be used on the warning callout. See macro options for heading .
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name heading Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option.
Name text | Type string | Description Required. Text content to be used within the warning callout.
Name html | Type string | Description Required. HTML content to be used within the warning callout.
Name actions | Type object | Description Can be used to add actions to the warning callout. See macro options for actions .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire warning callout component in a call block.
Name classes | Type string | Description Classes to add to the warning callout.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the warning callout.
Name visually Hidden Text | Type string | Description A visually hidden prefix used before the heading. Defaults to "Important" .

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the heading.
Name level | Type integer | Description Optional heading level for the heading. Defaults to 3 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name items | Type array | Description Array of actions as links for use in the warning callout. See macro options for actions items .
Name classes | Type string | Description Classes to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If type is set, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If type is set, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"warning-callout/macro.njk"
import
warningCallout
%}
{{
warningCallout
({
heading
:
"School, nursery or work"
,
text
:
"Stay away from school, nursery or work until all the spots have crusted over. This is usually 5 days after the spots first appeared."
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## When to use a warning callout

Use this callout for information that:

- is time critical

- could have a significant effect on someone's health

- addresses a common or significant misconception or mistake

## When not to use a warning callout

Do not use a warning callout

- in transactional journeys as we have not tested them there, but you can use a panel if you need an interruption page

- if you need to tell a user to contact their GP or get medical help – use the pattern to help users decide when and where to get care (care cards) instead

- if the information is not important enough for a warning callout – use inset text instead

## How to use a warning callout

Try to give the callout a short, clearly worded heading. Headings help people scan the page for warnings and understand what's relevant to them.

Make the callout concise, specific and self-contained. For example, do not introduce a callout with the words "If this happens...". Explain the circumstances.

Avoid having more than 2 callouts on a page. We want to reassure people, not to scare them.

### Placing warning callouts

Do not break the flow with a callout. Think about whether you need it and the best place to put it.

Make sure any text below a warning callout has its own heading so that screen reader users know it's not part of the callout.

If possible, put at least 1 short paragraph of text between 2 callouts or between an action link and a callout.

### Accessibility

The heading and background contrast ratio is 11.92:1 and the content and background contrast ratio is 13.69:1. These go beyond AAA guidelines.

#### Headings

The callout should have a specific heading, for example "School, nursery or work", prefixed with the visually hidden text Important: . This will help users with screen readers understand that the information is important.

If the heading is simply the word "Important" or it includes the word "important", you do not need to use visually hidden text.

- HTML code for warning callout

- Nunjucks code for warning callout

```text
<
div
class
=
"nhsuk-card nhsuk-card--warning"
>
<
div
class
=
"nhsuk-card__content"
>
<
h3
class
=
"nhsuk-card__heading"
>
Important
</
h3
>
<
p
class
=
"nhsuk-card__description"
>
For safety, tell your doctor or pharmacist if you
&#39;
re taking any other medicines, including herbal medicines, vitamins or supplements.
</
p
>
</
div
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
Name id | Type string | Description The ID of the warning callout.
Name heading | Type object | Description Required. Heading to be used on the warning callout. See macro options for heading .
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name heading Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option.
Name text | Type string | Description Required. Text content to be used within the warning callout.
Name html | Type string | Description Required. HTML content to be used within the warning callout.
Name actions | Type object | Description Can be used to add actions to the warning callout. See macro options for actions .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire warning callout component in a call block.
Name classes | Type string | Description Classes to add to the warning callout.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the warning callout.
Name visually Hidden Text | Type string | Description A visually hidden prefix used before the heading. Defaults to "Important" .

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the heading.
Name level | Type integer | Description Optional heading level for the heading. Defaults to 3 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name items | Type array | Description Array of actions as links for use in the warning callout. See macro options for actions items .
Name classes | Type string | Description Classes to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If type is set, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If type is set, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"warning-callout/macro.njk"
import
warningCallout
%}
{{
warningCallout
({
heading
:
"Important"
,
text
:
"For safety, tell your doctor or pharmacist if you're taking any other medicines, including herbal medicines, vitamins or supplements."
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## Research

In testing, users noticed the yellow callouts and understood them as a warning.

Our research shows that clearly worded callout headings:

- help users spot relevant information quickly

- help users who cannot distinguish callouts by their colour

- are better than icons , like exclamation marks, which may not be accessible and can be interpreted in different ways

We've tested warning callouts in pages with lots of content. We haven't yet tested them in forms or transactional content.

We haven't tested links in warning callouts. If you want to include a link, please test it and let us know.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
