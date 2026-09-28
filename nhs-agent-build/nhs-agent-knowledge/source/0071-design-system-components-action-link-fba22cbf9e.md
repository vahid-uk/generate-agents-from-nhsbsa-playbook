# Action link – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/action-link/

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

# Navigation – Action link

Use action links to help users get to the next stage of a journey quickly by signposting the start of a digital service.

- HTML code for action link

- Nunjucks code for action link

```text
<
a
class
=
"nhsuk-action-link"
href
=
"#"
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--arrow-right-circle"
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
"M12 2a10 10 0 0 0-10 9h11.7l-4-4a1 1 0 0 1 1.5-1.4l5.6 5.7a1 1 0 0 1 0 1.4l-5.6 5.7a1 1 0 0 1-1.5 0 1 1 0 0 1 0-1.4l4-4H2A10 10 0 1 0 12 2z"
/>
</
svg
>
<
span
class
=
"nhsuk-action-link__text"
>
Find your nearest A
&amp;
E
</
span
>
</
a
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the action link.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the action link. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the action link. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire action link component in a call block.
Name type | Type string | Description Type of action link as a button – "button" or "submit" . Defaults to "submit" unless href is provided.
Name href | Type string | Description Required. The action link href attribute. If set, the action link will use an <a> tag automatically unless type is provided.
Name open In New Window | Type boolean | Description If set to true , then the action link will open in a new window. If type is set, this has no effect.
Name variant | Type string | Description Optional variant of action link. You can use only "reverse" or empty values with this option.
Name classes | Type string | Description Classes to add to the action link component.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action link component.
Name element | Type string | Description Deprecated in 10.6.0 (see GitHub) . Configured automatically if href is provided.

```text
{%
from
"action-link/macro.njk"
import
actionLink
%}
{{
actionLink
({
text
:
"Find your nearest A&E"
,
href
:
"#"
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## When to use action links

Use action links to signpost the start of a digital service.

## When not to use action links

Do not use action links in forms. Use a button instead.

We don't use action links just to link to another page or site. If you need a link to stand out, you can use inset text .

## How to use action links

Keep the words on the action link short. Start with a verb, for example: "Book an appointment" or "Apply for an EHIC card".

Action links usually sit in a block of text. You can also put one in a care card. (Find out more about helping users decide when and where to get care, with care cards .)

You can have more than one action link on a page but avoid putting them near each other.

The link colour and background colour contrast ratio is 5.76:1, which passes AAA guidelines at that font size.

### Action link on dark backgrounds

To show white links and arrows on dark backgrounds, add the variant: "reverse" option using Nunjucks. For HTML add the nhsuk-action-link--reverse class to the action link.

Make sure all users can see the action link. The background colour must have a contrast ratio of at least 4.5:1 with white to meet WCAG 2.2 success criterion 1.4.3 Contrast (minimum), level AA (W3C) .

- HTML code for action link reverse

- Nunjucks code for action link reverse

```text
<
a
class
=
"nhsuk-action-link nhsuk-action-link--reverse"
href
=
"#"
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--arrow-right-circle"
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
"M12 2a10 10 0 0 0-10 9h11.7l-4-4a1 1 0 0 1 1.5-1.4l5.6 5.7a1 1 0 0 1 0 1.4l-5.6 5.7a1 1 0 0 1-1.5 0 1 1 0 0 1 0-1.4l4-4H2A10 10 0 1 0 12 2z"
/>
</
svg
>
<
span
class
=
"nhsuk-action-link__text"
>
Find your nearest A
&amp;
E
</
span
>
</
a
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the action link.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the action link. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the action link. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire action link component in a call block.
Name type | Type string | Description Type of action link as a button – "button" or "submit" . Defaults to "submit" unless href is provided.
Name href | Type string | Description Required. The action link href attribute. If set, the action link will use an <a> tag automatically unless type is provided.
Name open In New Window | Type boolean | Description If set to true , then the action link will open in a new window. If type is set, this has no effect.
Name variant | Type string | Description Optional variant of action link. You can use only "reverse" or empty values with this option.
Name classes | Type string | Description Classes to add to the action link component.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action link component.
Name element | Type string | Description Deprecated in 10.6.0 (see GitHub) . Configured automatically if href is provided.

```text
{%
from
"action-link/macro.njk"
import
actionLink
%}
{{
actionLink
({
text
:
"Find your nearest A&E"
,
href
:
"#"
,
variant
:
"reverse"
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## Research

We tested the action links on health information pages with lots of content, callout boxes and multi-page navigation.

Users didn't notice early versions, so we made the size of the text larger than body text size.

We used NHS blue first but users didn't notice it. So we changed the arrow colour to green (our "action" colour). Users seemed to see the green better.

In follow-up tests on busy content pages, users pointed out the action links and said they found them useful.

Get in touch to share your research findings about this pattern.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
