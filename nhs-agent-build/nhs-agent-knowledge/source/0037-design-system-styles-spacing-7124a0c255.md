# Spacing – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/styles/spacing/

## Source content

## Styles navigation

- Colour

- Focus state

- Icons

- Layout

- Page template

- Spacing Responsive spacing Static spacing

- Responsive spacing

- Static spacing

- Typography

- Use the NHS Frutiger font

## Reference navigation

- Override classes

# Styles – Spacing

The design system uses 2 different spacing scales: responsive and static.

## Responsive spacing

The responsive spacing scale adapts based on screen size.

The spacing for "large screens" is used when the screen is wider than the desktop breakpoint (768px). Spacing for the smallest units (0 to 2) stays the same for all screen sizes. The responsive spacing scale Spacing unit Large screens Small screens 9 64px 56px 8 56px 48px 7 48px 40px 6 40px 32px 5 32px 24px 4 24px 16px 3 16px 8px 2 8px 8px 1 4px 4px 0 0 0 How to use responsive spacing classes The responsive spacing override classes start with: nhsuk-u- , followed by either margin- or padding- , and then a spacing unit number. To apply spacing in a single direction, include left- , right- , top- , or bottom- just before the spacing unit. For example, use: nhsuk-u-margin-9 to apply a 56px margin to all sides of the element on small screens, increasing to 64px on large screens nhsuk-u-padding-right-5 to apply 24px of padding to the right side of the element on small screens, increasing to 32px on large screens nhsuk-u-margin-0 to remove all margins at all screen sizes Examples Open this example in a new tab : spacing Copy code < div class = "spacing-example" > < div class = "nhsuk-u-padding-bottom-9" > </ div > < div class = "nhsuk-u-padding-bottom-8" > </ div > < div class = "nhsuk-u-padding-bottom-7" > </ div > < div class = "nhsuk-u-padding-bottom-6" > </ div > < div class = "nhsuk-u-padding-bottom-5" > </ div > < div class = "nhsuk-u-padding-bottom-4" > </ div > < div class = "nhsuk-u-padding-bottom-3" > </ div > < div class = "nhsuk-u-padding-bottom-2" > </ div > < div class = "nhsuk-u-padding-bottom-1" > </ div > </ div > Open this example in a new tab : spacing text Copy code < p class = "nhsuk-u-margin-bottom-9" > A paragraph with an overridden margin-bottom. </ p > < p class = "nhsuk-u-margin-bottom-8" > A paragraph with an overridden margin-bottom. </ p > < p class = "nhsuk-u-margin-bottom-7" > A paragraph with an overridden margin-bottom. </ p > < p class = "nhsuk-u-margin-bottom-6" > A paragraph with an overridden margin-bottom. </ p > < p class = "nhsuk-u-margin-bottom-5" > A paragraph with an overridden margin-bottom. </ p > < p class = "nhsuk-u-margin-bottom-4" > A paragraph with an overridden margin-bottom. </ p > < p class = "nhsuk-u-margin-bottom-3" > A paragraph with an overridden margin-bottom. </ p > < p class = "nhsuk-u-margin-bottom-2" > A paragraph with an overridden margin-bottom. </ p > < p class = "nhsuk-u-margin-bottom-1" > A paragraph with an overridden margin-bottom. </ p > < p class = "nhsuk-u-margin-bottom-0" > A paragraph with an overridden margin-bottom. </ p > How to use responsive spacing in your own components If you want to use the responsive spacing scale you can reference the mixin. For example: use @include nhsuk-responsive-margin(6, "bottom"); for 40px margin-bottom on large screens and 32px on small screens use @include nhsuk-responsive-padding(6); for 40px padding on all sides on large screens and 32px on small screens Static spacing The static spacing scale stays the same for all screen sizes, and uses the same spacing as "large screens" in the responsive spacing scale. The static spacing scale Spacing unit All screens 9 56px 8 48px 7 40px 6 32px 5 24px 4 16px 3 8px 2 8px 1 4px 0 0 How to use static spacing classes The static spacing override classes start with nhsuk-u-static . Use them the same way as the responsive spacing override classes. For example, use: nhsuk-u-static-margin-9 to apply a 64px margin to all sides of the element at all screen sizes nhsuk-u-static-padding-right-5 to apply 32px of padding to the right side of the element at all screen sizes nhsuk-u-static-margin-0 to remove all margins at all screen sizes, same as nhsuk-u-margin-0 How to use static spacing in your own components If you're building your own components and want to reference the spacing scale directly in your SCSS file, you can use the spacing scale through a function like this: padding-top: nhsuk-spacing(6) Help us improve this guidance Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public. Feed back or share insights on GitHub Read more about how to feed back or share insights . If you have any questions, get in touch with the service manual team. Updates to this page Updated: May 2025

Spacing unit | Large screens | Small screens
9 | 64px | 56px
8 | 56px | 48px
7 | 48px | 40px
6 | 40px | 32px
5 | 32px | 24px
4 | 24px | 16px
3 | 16px | 8px
2 | 8px | 8px
1 | 4px | 4px
0 | 0 | 0

### How to use responsive spacing classes

The responsive spacing override classes start with: nhsuk-u- , followed by either margin- or padding- , and then a spacing unit number.

To apply spacing in a single direction, include left- , right- , top- , or bottom- just before the spacing unit.

For example, use:

- nhsuk-u-margin-9 to apply a 56px margin to all sides of the element on small screens, increasing to 64px on large screens

nhsuk-u-margin-9 to apply a 56px margin to all sides of the element on small screens, increasing to 64px on large screens

- nhsuk-u-padding-right-5 to apply 24px of padding to the right side of the element on small screens, increasing to 32px on large screens

nhsuk-u-padding-right-5 to apply 24px of padding to the right side of the element on small screens, increasing to 32px on large screens

- nhsuk-u-margin-0 to remove all margins at all screen sizes

nhsuk-u-margin-0 to remove all margins at all screen sizes

#### Examples

```text
<
div
class
=
"spacing-example"
>
<
div
class
=
"nhsuk-u-padding-bottom-9"
>
</
div
>
<
div
class
=
"nhsuk-u-padding-bottom-8"
>
</
div
>
<
div
class
=
"nhsuk-u-padding-bottom-7"
>
</
div
>
<
div
class
=
"nhsuk-u-padding-bottom-6"
>
</
div
>
<
div
class
=
"nhsuk-u-padding-bottom-5"
>
</
div
>
<
div
class
=
"nhsuk-u-padding-bottom-4"
>
</
div
>
<
div
class
=
"nhsuk-u-padding-bottom-3"
>
</
div
>
<
div
class
=
"nhsuk-u-padding-bottom-2"
>
</
div
>
<
div
class
=
"nhsuk-u-padding-bottom-1"
>
</
div
>
</
div
>
```

```text
<
p
class
=
"nhsuk-u-margin-bottom-9"
>
A paragraph with an overridden margin-bottom.
</
p
>
<
p
class
=
"nhsuk-u-margin-bottom-8"
>
A paragraph with an overridden margin-bottom.
</
p
>
<
p
class
=
"nhsuk-u-margin-bottom-7"
>
A paragraph with an overridden margin-bottom.
</
p
>
<
p
class
=
"nhsuk-u-margin-bottom-6"
>
A paragraph with an overridden margin-bottom.
</
p
>
<
p
class
=
"nhsuk-u-margin-bottom-5"
>
A paragraph with an overridden margin-bottom.
</
p
>
<
p
class
=
"nhsuk-u-margin-bottom-4"
>
A paragraph with an overridden margin-bottom.
</
p
>
<
p
class
=
"nhsuk-u-margin-bottom-3"
>
A paragraph with an overridden margin-bottom.
</
p
>
<
p
class
=
"nhsuk-u-margin-bottom-2"
>
A paragraph with an overridden margin-bottom.
</
p
>
<
p
class
=
"nhsuk-u-margin-bottom-1"
>
A paragraph with an overridden margin-bottom.
</
p
>
<
p
class
=
"nhsuk-u-margin-bottom-0"
>
A paragraph with an overridden margin-bottom.
</
p
>
```

### How to use responsive spacing in your own components

If you want to use the responsive spacing scale you can reference the mixin.

For example:

- use @include nhsuk-responsive-margin(6, "bottom"); for 40px margin-bottom on large screens and 32px on small screens

use @include nhsuk-responsive-margin(6, "bottom"); for 40px margin-bottom on large screens and 32px on small screens

- use @include nhsuk-responsive-padding(6); for 40px padding on all sides on large screens and 32px on small screens

use @include nhsuk-responsive-padding(6); for 40px padding on all sides on large screens and 32px on small screens

## Static spacing

The static spacing scale stays the same for all screen sizes, and uses the same spacing as "large screens" in the responsive spacing scale.

Spacing unit | All screens
9 | 56px
8 | 48px
7 | 40px
6 | 32px
5 | 24px
4 | 16px
3 | 8px
2 | 8px
1 | 4px
0 | 0

### How to use static spacing classes

The static spacing override classes start with nhsuk-u-static . Use them the same way as the responsive spacing override classes.

For example, use:

- nhsuk-u-static-margin-9 to apply a 64px margin to all sides of the element at all screen sizes

nhsuk-u-static-margin-9 to apply a 64px margin to all sides of the element at all screen sizes

- nhsuk-u-static-padding-right-5 to apply 32px of padding to the right side of the element at all screen sizes

nhsuk-u-static-padding-right-5 to apply 32px of padding to the right side of the element at all screen sizes

- nhsuk-u-static-margin-0 to remove all margins at all screen sizes, same as nhsuk-u-margin-0

nhsuk-u-static-margin-0 to remove all margins at all screen sizes, same as nhsuk-u-margin-0

### How to use static spacing in your own components

If you're building your own components and want to reference the spacing scale directly in your SCSS file, you can use the spacing scale through a function like this:

padding-top: nhsuk-spacing(6)

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: May 2025
