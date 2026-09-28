# Skip link – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/skip-link/

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

# Navigation – Skip link

Use a skip link to help keyboard-only users skip to the main content on a page.

- HTML code for skip link

- Nunjucks code for skip link

```text
<
p
class
=
"nhsuk-body"
>
To view the skip link, tab to this example, or click inside this example and press tab.
</
p
>
<
a
class
=
"nhsuk-skip-link"
data-module
=
"nhsuk-skip-link"
href
=
"#maincontent"
>
Skip to main content
</
a
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the skip link.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the skip link. If html is provided, the text option will be ignored. Defaults to "Skip to main content" .
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the skip link. If html is provided, the text option will be ignored. Defaults to "Skip to main content" .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire skip link component in a call block.
Name href | Type string | Description The skip link href attribute. Defaults to "#maincontent" .
Name classes | Type string | Description Classes to add to the skip link.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the skip link.

```text
<
p
class
=
"nhsuk-body"
>
To view the skip link, tab to this example, or click inside this example and press tab.
</
p
>
{%
from
"skip-link/macro.njk"
import
skipLink
%}
{{
skipLink
({
href
:
"#maincontent"
,
text
:
"Skip to main content"
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## When to use a skip link

All nhs.uk pages must include a skip link in the header following guidance in the GOV.UK Design System .

## How skip links work

Some people use the tab key on their keyboard to navigate through the links and form elements on a web page. Including a skip link gives users the option to bypass the top-level navigation links and jump to the main content on the page.

The skip link component is visually hidden until a keyboard press activates it.

## Research

If you've used skip links, please share your user research findings.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
