# Do and Don't lists – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/do-and-dont-lists/

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

# Content presentation – Do and Don't lists

Use Do and Don't lists to help users understand more easily what they should and shouldn't do.

- HTML code for do and dont lists

- Nunjucks code for do and dont lists

```text
<
div
class
=
"nhsuk-card nhsuk-card--feature"
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
Do
</
h3
>
<
ul
class
=
"nhsuk-list nhsuk-list--tick"
role
=
"list"
>
<
li
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--tick"
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
"M11.4 17.5a2 2 0 0 1-2.7.1h-.1L4 12.8a1.5 1.5 0 0 1 2.1-2L10 14.7l8.1-8.1a1.5 1.5 0 1 1 2.2 2l-8.9 9Z"
/>
</
svg
>
cover blisters with a soft plaster or padded dressing
</
li
>
<
li
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--tick"
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
"M11.4 17.5a2 2 0 0 1-2.7.1h-.1L4 12.8a1.5 1.5 0 0 1 2.1-2L10 14.7l8.1-8.1a1.5 1.5 0 1 1 2.2 2l-8.9 9Z"
/>
</
svg
>
wash your hands before touching a burst blister
</
li
>
<
li
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--tick"
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
"M11.4 17.5a2 2 0 0 1-2.7.1h-.1L4 12.8a1.5 1.5 0 0 1 2.1-2L10 14.7l8.1-8.1a1.5 1.5 0 1 1 2.2 2l-8.9 9Z"
/>
</
svg
>
allow the fluid in a burst blister to drain before covering it with a plaster or dressing
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
<
div
class
=
"nhsuk-card nhsuk-card--feature"
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
Don
&#39;
t
</
h3
>
<
ul
class
=
"nhsuk-list nhsuk-list--cross"
role
=
"list"
>
<
li
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--cross"
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
"M17 18.5c-.4 0-.8-.1-1.1-.4l-10-10c-.6-.6-.6-1.6 0-2.1.6-.6 1.5-.6 2.1 0l10 10c.6.6.6 1.5 0 2.1-.3.3-.6.4-1 .4z M7 18.5c-.4 0-.8-.1-1.1-.4-.6-.6-.6-1.5 0-2.1l10-10c.6-.6 1.5-.6 2.1 0 .6.6.6 1.5 0 2.1l-10 10c-.3.3-.6.4-1 .4z"
/>
</
svg
>
do not burst a blister yourself
</
li
>
<
li
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--cross"
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
"M17 18.5c-.4 0-.8-.1-1.1-.4l-10-10c-.6-.6-.6-1.6 0-2.1.6-.6 1.5-.6 2.1 0l10 10c.6.6.6 1.5 0 2.1-.3.3-.6.4-1 .4z M7 18.5c-.4 0-.8-.1-1.1-.4-.6-.6-.6-1.5 0-2.1l10-10c.6-.6 1.5-.6 2.1 0 .6.6.6 1.5 0 2.1l-10 10c-.3.3-.6.4-1 .4z"
/>
</
svg
>
do not peel the skin off a burst blister
</
li
>
<
li
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--cross"
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
"M17 18.5c-.4 0-.8-.1-1.1-.4l-10-10c-.6-.6-.6-1.6 0-2.1.6-.6 1.5-.6 2.1 0l10 10c.6.6.6 1.5 0 2.1-.3.3-.6.4-1 .4z M7 18.5c-.4 0-.8-.1-1.1-.4-.6-.6-.6-1.5 0-2.1l10-10c.6-.6 1.5-.6 2.1 0 .6.6.6 1.5 0 2.1l-10 10c-.3.3-.6.4-1 .4z"
/>
</
svg
>
do not pick at the edges of the remaining skin
</
li
>
<
li
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--cross"
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
"M17 18.5c-.4 0-.8-.1-1.1-.4l-10-10c-.6-.6-.6-1.6 0-2.1.6-.6 1.5-.6 2.1 0l10 10c.6.6.6 1.5 0 2.1-.3.3-.6.4-1 .4z M7 18.5c-.4 0-.8-.1-1.1-.4-.6-.6-.6-1.5 0-2.1l10-10c.6-.6 1.5-.6 2.1 0 .6.6.6 1.5 0 2.1l-10 10c-.3.3-.6.4-1 .4z"
/>
</
svg
>
do not wear the shoes or use the equipment that caused your blister until it heals
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the do and don't list component.
Name title | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.text option.
Name heading | Type object | Description Required. Heading to be displayed on the do and don't list component. See macro options for heading .
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name icon | Type string | Description Optional icon modifier for the do and don't list items – "cross" or "tick" . Defaults to "tick" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Required. Replaced by the icon option.
Name items | Type array | Description Required. Array of do and don't items objects. See macro options for items .
Name prefix Text | Type string | Description Optional prefix text used before each do and don't item. Defaults to "do not" when type is "cross" .
Name hide Prefix | Type boolean | Description If set to true , the optional prefixText will be removed from each do and don't item.
Name classes | Type string | Description Classes to add to the do and don't list container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the do and don't list container.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the heading.
Name level | Type integer | Description Optional heading level. Defaults to 3 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name item | Type string | Description Deprecated in 10.1.0 (see GitHub) . Required. Replaced by the item.text and item.html options.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each do and don't item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each do and don't item. If html is provided, the text option will be ignored.

```text
{%
from
"do-dont-list/macro.njk"
import
list
%}
{{
list
({
heading
:
"Do"
,
icon
:
"tick"
,
items
: [
    {
text
:
"cover blisters with a soft plaster or padded dressing"
},
    {
text
:
"wash your hands before touching a burst blister"
},
    {
text
:
"allow the fluid in a burst blister to drain before covering it with a plaster or dressing"
}
  ]
})
}}
{{
list
({
heading
:
"Don't"
,
icon
:
"cross"
,
items
: [
    {
text
:
"burst a blister yourself"
},
    {
text
:
"peel the skin off a burst blister"
},
    {
text
:
"pick at the edges of the remaining skin"
},
    {
text
:
"wear the shoes or use the equipment that caused your blister until it heals"
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## When to use Do and Don't lists

Use a Do and Don't list to give users clear and simple advice, for example about treating a problem themselves.

## When not to use Do and Don't lists

If you only have 1 Do or 1 Don't, consider using inset text or a warning callout instead.

## How to use Do and Don't lists

Keep your points as brief as possible.

Dos normally come before Don'ts.

It is alright to just have Don'ts if there aren't any Dos and just Dos if there aren't any Don'ts.

Treat the heading as a lead-in and the items under the heading as part of 1 long sentence. Start each bullet point lower case. With Dos, just write the action. With Don'ts, include "do not" at the beginning of each bullet point.

Make sure any text below a Do or Don't list has its own heading so that screen reader users know it's not part of the Do or Don't section.

## Research

Users recognised and understood the meaning of the ticks and crosses. They saw the green ticks as a positive "do" action and the red as a warning.

We've tested the Do and Don't lists in pages with lots of content. We aren't using them in forms or transactional content and haven't tested them there.

The Do and Don't lists stack on desktop and mobile, rather than sitting side by side on the page. We found that users read down the page, not across it. Also, when we tried the lists side by side, the number of characters in each line was too short which made reading difficult.

### Accessibility

People with a visual disability may not be able to see the ticks and crosses. We use aria labels to hide them from screen reader users, so we don't confuse them.

People with a visual disability may rely on the words. With the Don't lists, we found that screen reader users need "do not" repeated at the beginning of every line. If we leave out "do not", there is a risk they will hear the command as a positive one, which could be dangerous. This could also apply to other user groups, like people with a learning disability or people who are very stressed. Users could also scroll down and miss the "Don't" heading. So we include "do not" at the start of every bullet point.

We don't say "do" at the start of every line in a Do list. People found this unnecessary and annoying.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
