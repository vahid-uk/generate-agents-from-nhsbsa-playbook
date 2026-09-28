# Icons – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/styles/icons/

## Source content

## Styles navigation

- Colour

- Focus state

- Icons

- Layout

- Page template

- Spacing

- Typography

- Use the NHS Frutiger font

## Reference navigation

- Override classes

# Styles – Icons

Use this small set of icons that we know our users need and understand to help them identify and navigate content more quickly.

## Icons you can use

Use these icons to mark important parts of the page and highlight things you want users to do.

Check the relevant component and pattern pages in the design system for guidance on how to use the icons, including use of colour.

### Left and right arrows

The left and right arrow icons are used in the pagination component. These icons should be used alongside text labels, for example "Previous page" and "Next page".

- HTML code for icons arrows

- Nunjucks code for icons arrows

```text
<
svg
class
=
"nhsuk-icon nhsuk-icon--arrow-left"
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
"M10.7 6.3c.4.4.4 1 0 1.4L7.4 11H19a1 1 0 0 1 0 2H7.4l3.3 3.3c.4.4.4 1 0 1.4a1 1 0 0 1-1.4 0l-5-5A1 1 0 0 1 4 12c0-.3.1-.5.3-.7l5-5a1 1 0 0 1 1.4 0Z"
/>
</
svg
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--arrow-right"
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
"m14.7 6.3 5 5c.2.2.3.4.3.7 0 .3-.1.5-.3.7l-5 5a1 1 0 0 1-1.4-1.4l3.3-3.3H5a1 1 0 0 1 0-2h11.6l-3.3-3.3a1 1 0 1 1 1.4-1.4Z"
/>
</
svg
>
```

```text
{%
from
"nhsuk/macros/icon.njk"
import
nhsukIcon
%}
{{
nhsukIcon
(
"arrow-left"
) }}
{{
nhsukIcon
(
"arrow-right"
) }}
```

### Right arrow (inside a circle)

The right arrow inside a circle icon is used in the action link component. This icon should be used to signpost links that start a digital service.

- HTML code for icons arrow right circle

- Nunjucks code for icons arrow right circle

```text
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
```

```text
{%
from
"nhsuk/macros/icon.njk"
import
nhsukIcon
%}
{{
nhsukIcon
(
"arrow-right-circle"
) }}
```

### Right chevron (inside a circle)

The right chevron inside a circle icon is used in the primary card component. This icon should be used on hub page cards to signpost important groups of information.

- HTML code for icons chevron right circle

- Nunjucks code for icons chevron right circle

```text
<
svg
class
=
"nhsuk-icon nhsuk-icon--chevron-right-circle"
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
"M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-.3 5.8a1 1 0 1 0-1.5 1.4l2.9 2.8-2.9 2.8a1 1 0 0 0 1.5 1.4l3.5-3.5c.4-.4.4-1 0-1.4Z"
/>
</
svg
>
```

```text
{%
from
"nhsuk/macros/icon.njk"
import
nhsukIcon
%}
{{
nhsukIcon
(
"chevron-right-circle"
) }}
```

### Tick and cross

The tick (do) and cross (don't) icons are used for do and don't lists . These icons should be shown below "Do" and "Don't" headings.

- HTML code for icons tick and cross

- Nunjucks code for icons tick and cross

```text
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
```

```text
{%
from
"nhsuk/macros/icon.njk"
import
nhsukIcon
%}
{{
nhsukIcon
(
"tick"
) }}
{{
nhsukIcon
(
"cross"
) }}
```

### Search

The search icon is used in the header component. When used without a visible text label, make sure the icon has an accessible name, for example "Search".

- HTML code for icons search

- Nunjucks code for icons search

```text
<
svg
class
=
"nhsuk-icon nhsuk-icon--search"
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
role
=
"img"
aria-label
=
"Search"
>
<
title
>
Search
</
title
>
<
path
d
=
"m20.7 18.9-4.1-4.1a7 7 0 1 0-1.4 1.4l4 4.1a1 1 0 0 0 1.5 0c.4-.4.4-1 0-1.4ZM6 10.6a5 5 0 1 1 10 0 5 5 0 0 1-10 0Z"
/>
</
svg
>
```

```text
{%
from
"nhsuk/macros/icon.njk"
import
nhsukIcon
%}
{{
nhsukIcon
(
"search"
, {
title
:
"Search"
}) }}
```

### User profile

The user profile icon is used in the header component. This icon should be shown alongside information about the currently logged-in user.

- HTML code for icons user

- Nunjucks code for icons user

```text
<
svg
class
=
"nhsuk-icon nhsuk-icon--user"
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
"M12 1a11 11 0 1 1 0 22 11 11 0 0 1 0-22Zm0 2a9 9 0 0 0-5 16.5V18a4 4 0 0 1 4-4h2a4 4 0 0 1 4 4v1.5A9 9 0 0 0 12 3Zm0 3a3.5 3.5 0 1 1-3.5 3.5A3.4 3.4 0 0 1 12 6Z"
/>
</
svg
>
```

```text
{%
from
"nhsuk/macros/icon.njk"
import
nhsukIcon
%}
{{
nhsukIcon
(
"user"
) }}
```

### Plus and minus

We use plus (+) and minus (-) in the expander component. However, these are provided by the CSS. We do not have SVG icons for them.

### British Sign Language (BSL)

We also have BSL icons you can download to help users recognise that information is available in BSL. See the Find BSL content pattern .

## How to use these icons

Use icons sparingly, and not for decoration.

### Using SVG classes for icons

We use scalable vector graphics (SVG) for icons, rather than images such as PNG. SVG are code snippets that you can drop directly into the HTML.

SVG icons are sharp, flexible, and load quickly. You can control how they appear, for example their colour, with style sheets (CSS).

If you're using Nunjucks templating language, you can use the nhsukIcon macro.

SVG icons use the nhsuk-icon class which sets a default size for the icon. Each icon also has a specific class, such as nhsuk-icon--search . The specific class allows you to modify the icon with styles, such as colour via fill .

### Using colour with icons

Icons often need to change colour based on their context and state, such as hover, focus and active. When choosing colours, make sure they have sufficient colour contrast to pass WCAG 2.2 success criterion 1.4.11 Non-text Contrast (W3C) .

### Changing the size of an icon

If you want to make an icon bigger, you can use the size override classes to make an icon 25%, 50%, 75% or 100% larger.

Make sure any icons used as buttons are at least 24px by 24px in target size, or that there is another way to perform the action.

- HTML code for icons sizes

- Nunjucks code for icons sizes

```text
<
svg
class
=
"nhsuk-icon nhsuk-icon--user nhsuk-icon--size-25"
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
"M12 1a11 11 0 1 1 0 22 11 11 0 0 1 0-22Zm0 2a9 9 0 0 0-5 16.5V18a4 4 0 0 1 4-4h2a4 4 0 0 1 4 4v1.5A9 9 0 0 0 12 3Zm0 3a3.5 3.5 0 1 1-3.5 3.5A3.4 3.4 0 0 1 12 6Z"
/>
</
svg
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--user nhsuk-icon--size-50"
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
"M12 1a11 11 0 1 1 0 22 11 11 0 0 1 0-22Zm0 2a9 9 0 0 0-5 16.5V18a4 4 0 0 1 4-4h2a4 4 0 0 1 4 4v1.5A9 9 0 0 0 12 3Zm0 3a3.5 3.5 0 1 1-3.5 3.5A3.4 3.4 0 0 1 12 6Z"
/>
</
svg
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--user nhsuk-icon--size-75"
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
"M12 1a11 11 0 1 1 0 22 11 11 0 0 1 0-22Zm0 2a9 9 0 0 0-5 16.5V18a4 4 0 0 1 4-4h2a4 4 0 0 1 4 4v1.5A9 9 0 0 0 12 3Zm0 3a3.5 3.5 0 1 1-3.5 3.5A3.4 3.4 0 0 1 12 6Z"
/>
</
svg
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--user nhsuk-icon--size-100"
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
"M12 1a11 11 0 1 1 0 22 11 11 0 0 1 0-22Zm0 2a9 9 0 0 0-5 16.5V18a4 4 0 0 1 4-4h2a4 4 0 0 1 4 4v1.5A9 9 0 0 0 12 3Zm0 3a3.5 3.5 0 1 1-3.5 3.5A3.4 3.4 0 0 1 12 6Z"
/>
</
svg
>
```

```text
{%
from
"nhsuk/macros/icon.njk"
import
nhsukIcon
%}
{{
nhsukIcon
(
"user"
, {
size
:
"25"
}) }}
{{
nhsukIcon
(
"user"
, {
size
:
"50"
}) }}
{{
nhsukIcon
(
"user"
, {
size
:
"75"
}) }}
{{
nhsukIcon
(
"user"
, {
size
:
"100"
}) }}
```

### Accessibility

SVG icons must be accessible. For example, they need to meet accessible colour contrast standards. Our recommended tool to test colour combinations is the WebAIM contrast checker . Read more about accessible SVGs on CSS Tricks website .

## Research

These icons seem to be universally recognisable. When we tested them, we found that people understood them. We tested them in context – not on their own, but in components on a full page.

Read Icons: avoid temptation and start with user needs (NHS England) .

Find out more about the benefits of SVG icons:

- CSS Tricks – a pretty good SVG icon system

- CSS Tricks – a complete guide to SVG fallbacks

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
