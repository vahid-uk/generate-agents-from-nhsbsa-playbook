# Back link – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/back-link/

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

# Navigation – Back link

Use back links to help users go back to the previous page in a multi-page transaction.

- HTML code for back link

- Nunjucks code for back link

```text
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the back link.
Name text | Type string | Description Text to use within the back link component. If html is provided, the text option will be ignored. Defaults to "Back" .
Name html | Type string | Description HTML to use within the back link component. If html is provided, the text option will be ignored. Defaults to "Back" .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire back link component in a call block.
Name type | Type string | Description Type of back link as a button – "button" or "submit" . Defaults to "submit" unless href is provided.
Name href | Type string | Description The back link href attribute. If set, the back link will use an <a> tag automatically unless type is provided.
Name variant | Type string | Description Optional variant of back link. You can use only "reverse" or empty values with this option.
Name classes | Type string | Description Classes to add to the back link component.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the back link component.
Name visually Hidden Text | Type string | Description An optional visually hidden prefix used before the back link text, for example "Back to" used by the breadcrumbs component.
Name element | Type string | Description Deprecated in 10.6.0 (see GitHub) . Configured automatically if href is provided.

```text
{%
from
"back-link/macro.njk"
import
backLink
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## When to use a back link

We only use back links on transactional services or multi-page forms.

The GOV.UK design system recommends including a back link on question pages. Read more about question pages on GOV.UK .

You can include a back link on other pages in a multi-page transaction, if it makes sense to do so.

## When not to use a back link

Do not use a back link on a content page, like a health information page.

Do not use a back link with breadcrumbs .

## How to use back links

Make sure the text used in the link describes the action, for example "Back". Carry out research with users to find the words that help them the most.

The link should take users back to the page they were on in the state they last saw it. Make sure information they have already entered is pre-populated. Do not pre-populate if the information is no longer valid, or when pre-populating would be a major safety or security concern.

Generally, the back link should go at the top left of the page. Within the HTML it should appear before the <main> tag. This is so that skip link skips past the back link to the main content.

If you put the back link in a different position, do not put it close to other links or buttons where it might distract users from what they need to do. Also think about people who use a screen reader: is the page read out in a logical order?

### Back link as a button

You can render the back link as a button element if necessary in order to post form data back to the previous page.

- HTML code for back link button

- Nunjucks code for back link button

```text
<
button
class
=
"nhsuk-back-link"
type
=
"submit"
>
Back
</
button
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the back link.
Name text | Type string | Description Text to use within the back link component. If html is provided, the text option will be ignored. Defaults to "Back" .
Name html | Type string | Description HTML to use within the back link component. If html is provided, the text option will be ignored. Defaults to "Back" .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire back link component in a call block.
Name type | Type string | Description Type of back link as a button – "button" or "submit" . Defaults to "submit" unless href is provided.
Name href | Type string | Description The back link href attribute. If set, the back link will use an <a> tag automatically unless type is provided.
Name variant | Type string | Description Optional variant of back link. You can use only "reverse" or empty values with this option.
Name classes | Type string | Description Classes to add to the back link component.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the back link component.
Name visually Hidden Text | Type string | Description An optional visually hidden prefix used before the back link text, for example "Back to" used by the breadcrumbs component.
Name element | Type string | Description Deprecated in 10.6.0 (see GitHub) . Configured automatically if href is provided.

```text
{%
from
"back-link/macro.njk"
import
backLink
%}
{{
backLink
({
text
:
"Back"
,
type
:
"submit"
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Back link on dark backgrounds

To show white links and chevrons on dark backgrounds, add the variant: "reverse" option using Nunjucks. For HTML add the nhsuk-back-link--reverse class to the back link.

Make sure all users can see the back link. The background colour must have a contrast ratio of at least 4.5:1 with white to meet WCAG 2.2 success criterion 1.4.3 Contrast (minimum), level AA (W3C) .

- HTML code for back link reverse

- Nunjucks code for back link reverse

```text
<
a
class
=
"nhsuk-back-link nhsuk-back-link--reverse"
href
=
"#"
>
Back
</
a
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the back link.
Name text | Type string | Description Text to use within the back link component. If html is provided, the text option will be ignored. Defaults to "Back" .
Name html | Type string | Description HTML to use within the back link component. If html is provided, the text option will be ignored. Defaults to "Back" .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire back link component in a call block.
Name type | Type string | Description Type of back link as a button – "button" or "submit" . Defaults to "submit" unless href is provided.
Name href | Type string | Description The back link href attribute. If set, the back link will use an <a> tag automatically unless type is provided.
Name variant | Type string | Description Optional variant of back link. You can use only "reverse" or empty values with this option.
Name classes | Type string | Description Classes to add to the back link component.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the back link component.
Name visually Hidden Text | Type string | Description An optional visually hidden prefix used before the back link text, for example "Back to" used by the breadcrumbs component.
Name element | Type string | Description Deprecated in 10.6.0 (see GitHub) . Configured automatically if href is provided.

```text
{%
from
"back-link/macro.njk"
import
backLink
%}
{{
backLink
({
text
:
"Back"
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

During testing, NHS 111 online found that some users wanted to change their answers, so they introduced a back link and labelled it to "Change my previous answer".

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
