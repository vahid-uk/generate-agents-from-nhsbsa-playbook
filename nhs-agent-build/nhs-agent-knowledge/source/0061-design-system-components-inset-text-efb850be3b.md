# Inset text – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/inset-text/

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

# Content presentation – Inset text

Use inset text to help users identify and understand important content on the page, even if they do not read the whole page.

- HTML code for inset text

- Nunjucks code for inset text

```text
<
div
class
=
"nhsuk-inset-text"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Information:
</
span
>
<
p
>
You can report any suspected side effect using the
<
a
href
=
"#"
>
Yellow Card safety scheme
</
a
>
.
</
p
>
</
div
>
```

Requires NHS.UK frontend 10.1.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the inset text component.
Name text | Type string | Description Required. Text content to be used within the inset text component. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML content to be used within the inset text component. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire inset text component in a call block.
Name classes | Type string | Description Classes to add to the inset text.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the inset text.
Name visually Hidden Text | Type string | Description A visually hidden prefix used before the inset text. Defaults to "Information" .

```text
{%
from
"inset-text/macro.njk"
import
insetText
%}
{%
set
insetTextHtml
%}
<
p
>
You can report any suspected side effect using the
<
a
href
=
"#"
>
Yellow Card safety scheme
</
a
>
.
</
p
>
{%
endset
%}
{{
insetText
({
html
: insetTextHtml
})
}}
```

Requires NHS.UK frontend 10.1.0 – check your version of NHS.UK frontend

## When to use inset text

Use inset text for content that needs to stand out from the rest of the page.

## When not to use inset text

Do not use inset text in transactional pages. We haven't tested it there yet.

Do not use inset text if you need to tell a user to contact their GP or get medical help. Use the pattern to help users decide when and where to get care (care cards) instead.

Some users don't notice inset text on complex pages or near to other prominent elements, so we avoid using it for very important information that users need to see. Use a warning callout instead if the information:

- is time critical

- could have a significant effect on someone's health

- addresses a common or significant misconception or mistake

## How to use inset text

Don't overdo inset text. Think about whether you need it and the best place to put it.

### Accessibility

People with visual disabilities may not be able to see the colour that marks out inset text. Instead they may rely on hidden labels to recognise it.

We use <span class="visually-hidden">Information: </span> to let users with screen readers know that this is different to the body text.

## Research

We've tested inset text in content pages and users understood its purpose. We haven't tested inset text in transactional pages.

Get in touch to share your research findings if you've used this pattern.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
