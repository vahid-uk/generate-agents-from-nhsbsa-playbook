# Breadcrumbs – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/breadcrumbs/

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

# Navigation – Breadcrumbs

Use breadcrumbs to help users understand where they are in the website.

- HTML code for breadcrumbs

- Nunjucks code for breadcrumbs

```text
<
nav
class
=
"nhsuk-breadcrumb"
aria-label
=
"Breadcrumb"
>
<
ol
class
=
"nhsuk-breadcrumb__list"
>
<
li
class
=
"nhsuk-breadcrumb__list-item"
>
<
a
class
=
"nhsuk-breadcrumb__link"
href
=
"#"
>
Home
</
a
>
</
li
>
<
li
class
=
"nhsuk-breadcrumb__list-item"
>
<
a
class
=
"nhsuk-breadcrumb__link"
href
=
"#"
>
NHS services
</
a
>
</
li
>
<
li
class
=
"nhsuk-breadcrumb__list-item"
>
<
a
class
=
"nhsuk-breadcrumb__link"
href
=
"#"
>
Hospitals
</
a
>
</
li
>
</
ol
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
<
span
class
=
"nhsuk-u-visually-hidden"
>
Back to
</
span
>
Hospitals
</
a
>
</
nav
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the breadcrumb.
Name items | Type array | Description Required. Array of breadcrumbs items. See macro options for items .
Name text | Type string | Description Deprecated in 7.1.0 (see GitHub) . Required. Replaced by item.text in the items option.
Name href | Type string | Description Deprecated in 7.1.0 (see GitHub) . Required. Replaced by item.href in the items option.
Name variant | Type string | Description Optional variant of breadcrumb. You can use only "reverse" or empty values with this option.
Name classes | Type string | Description Classes to add to the container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the container.
Name label Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the ariaLabel option.
Name aria Label | Type string | Description Accessible name identifying the landmark to screen readers. Defaults to "Breadcrumb".
Name back Link | Type object | Description The back link used by the breadcrumbs component on mobile. See macro options for back Link .

Name | Type | Description
Name text | Type string | Description Required. Text to use within the breadcrumbs item.
Name html | Type string | Description Required. HTML to use within the breadcrumbs item.
Name href | Type string | Description The breadcrumb item href attribute.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the individual crumb.

```text
{%
from
"breadcrumb/macro.njk"
import
breadcrumb
%}
{{
breadcrumb
({
items
: [
    {
href
:
"#"
,
text
:
"Home"
},
    {
href
:
"#"
,
text
:
"NHS services"
},
    {
href
:
"#"
,
text
:
"Hospitals"
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## When to use breadcrumbs

Use breadcrumbs to give users context and let them move back or up a level if they cannot find what they want on the page.

## When not to use breadcrumbs

Do not use breadcrumbs in transactional journeys as they can get in the way of the user completing the task.

## How to use breadcrumbs

If the full breadcrumb trail does not fit the screen size, it can wrap onto 2 lines. Do not break the breadcrumb if it fits on 1 line.

If you put the back link in a different position, do not put it close to other links or buttons where it might distract users from what they need to do. Also think about people who use a screen reader: is the page read out in a logical order?

You do not need to show the current page in the breadcrumb because this information is in the H1.

On mobile, we replace the full breadcrumb trail with a "Back to [parent]" link.

We use aria-label="breadcrumb" as a label in the nav element to let people who use screen readers know what it is.

## Breadcrumbs on dark backgrounds

To show white links and arrows on dark backgrounds, add the variant: "reverse" option using Nunjucks. For HTML add the nhsuk-breadcrumb--reverse class to the breadcrumb.

Make sure all users can see the breadcrumbs. The background colour must have a contrast ratio of at least 4.5:1 with white to meet WCAG 2.2 success criterion 1.4.3 Contrast (minimum), level AA (W3C) .

- HTML code for breadcrumbs reverse

- Nunjucks code for breadcrumbs reverse

```text
<
nav
class
=
"nhsuk-breadcrumb nhsuk-breadcrumb--reverse"
aria-label
=
"Breadcrumb"
>
<
ol
class
=
"nhsuk-breadcrumb__list"
>
<
li
class
=
"nhsuk-breadcrumb__list-item"
>
<
a
class
=
"nhsuk-breadcrumb__link"
href
=
"#"
>
Home
</
a
>
</
li
>
<
li
class
=
"nhsuk-breadcrumb__list-item"
>
<
a
class
=
"nhsuk-breadcrumb__link"
href
=
"#"
>
NHS services
</
a
>
</
li
>
<
li
class
=
"nhsuk-breadcrumb__list-item"
>
<
a
class
=
"nhsuk-breadcrumb__link"
href
=
"#"
>
Hospitals
</
a
>
</
li
>
</
ol
>
<
a
class
=
"nhsuk-back-link nhsuk-back-link--reverse"
href
=
"#"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Back to
</
span
>
Hospitals
</
a
>
</
nav
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the breadcrumb.
Name items | Type array | Description Required. Array of breadcrumbs items. See macro options for items .
Name text | Type string | Description Deprecated in 7.1.0 (see GitHub) . Required. Replaced by item.text in the items option.
Name href | Type string | Description Deprecated in 7.1.0 (see GitHub) . Required. Replaced by item.href in the items option.
Name variant | Type string | Description Optional variant of breadcrumb. You can use only "reverse" or empty values with this option.
Name classes | Type string | Description Classes to add to the container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the container.
Name label Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the ariaLabel option.
Name aria Label | Type string | Description Accessible name identifying the landmark to screen readers. Defaults to "Breadcrumb".
Name back Link | Type object | Description The back link used by the breadcrumbs component on mobile. See macro options for back Link .

Name | Type | Description
Name text | Type string | Description Required. Text to use within the breadcrumbs item.
Name html | Type string | Description Required. HTML to use within the breadcrumbs item.
Name href | Type string | Description The breadcrumb item href attribute.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the individual crumb.

```text
{%
from
"breadcrumb/macro.njk"
import
breadcrumb
%}
{{
breadcrumb
({
variant
:
"reverse"
,
items
: [
    {
href
:
"#"
,
text
:
"Home"
},
    {
href
:
"#"
,
text
:
"NHS services"
},
    {
href
:
"#"
,
text
:
"Hospitals"
}
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## Research

We tested breadcrumbs on pages with lots of content about conditions or medicines. They helped people understand their place on the website. People noticed them and appreciated the context they gave. People also used them to get back to where they came from or to get back home.

We took out the breadcrumb links when we tested our pages in transactional journeys (in more than 3 labs). We thought that having breadcrumb links would distract users from completing the journey. We found that they did not need the breadcrumbs because they were focused on the task.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
