# Colour – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/styles/colour/

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

# Styles – Colour

Our colours, and how to apply them.

## Using colour

Our brand colours help people recognise and trust that our services come from the NHS.

We also use colour to help users prioritise and differentiate information – for example we use:

- yellow for our focus state styles and for warning callouts

- red for urgent care cards in the pattern to help users decide when and where to get care

Our text and background colours are designed to meet accessibility needs. Read more about accessibility and colour on this page .

## Main colours

If you are using the NHS.UK frontend or the NHS.UK prototype kit , use the Sass variables provided rather than copying the hexadecimal (hex) colour values. For example, use $nhsuk-text-colour rather than #212b32 . This means that your service will always use the most recent colour palette whenever you update.

Only use the variables in the context they're designed for. In all other cases, you should reference the colour palette directly. For example, if you wanted to use red to represent some data in a graph you should use nhsuk-colour("red") rather than $nhsuk-error-colour .

Text
$nhsuk-text-colour | #212b32
$nhsuk-secondary-text-colour Modifier class: nhsuk-u-secondary-text-colour | #4c6272
Links
$nhsuk-link-colour | #005eb8
$nhsuk-link-hover-colour | #7C2855
$nhsuk-link-visited-colour | #330072
$nhsuk-link-active-colour | #002f5c
Focus state
$nhsuk-focus-colour | #ffeb3b
$nhsuk-focus-text-colour | #212b32
Border
$nhsuk-border-colour | #d8dde0
$nhsuk-input-border-colour | #4c6272
Error state
$nhsuk-error-colour | #d5281b
Success state
$nhsuk-success-colour | #007f3b
Button
$nhsuk-button-colour | #007f3b
$nhsuk-secondary-button-border-colour | #005eb8

### Text

Modifier class: nhsuk-u-secondary-text-colour

### Links

### Focus state

### Border

### Error state

### Success state

### Button

### Page background colour

We use $nhsuk-body-background-colour or nhsuk-colour("grey-5") as a background tint. This is because:

- it reduces overall page glare

- the British Dyslexia Association's style guide recommends dark text on a light, but not white, background

- components with important information, like callouts, stand out

$nhsuk-reverse-text-colour or nhsuk-colour("white") is used to make important information stand out and for alternating backgrounds, for example on the NHS website home page .

### Secondary text colour

You can use the nhsuk-u-secondary-text-colour class for text that should appear in the secondary text colour of dark grey.

For example, this could be used for text to describe missing data in a table or summary list.

## Colour palette

Avoid using the palette colours if there is a Sass variable that is designed for your context. For example, if you are styling the error state of a component you should use the $nhsuk-error-colour Sass variable rather than nhsuk-colour("red") .

nhsuk-colour("red") | #d5281b
nhsuk-colour("yellow") | #ffeb3b
nhsuk-colour("green") | #007f3b
nhsuk-colour("aqua-green") | #00a499
nhsuk-colour("blue") | #005eb8
nhsuk-colour("dark-blue") | #003087
nhsuk-colour("purple") | #330072
nhsuk-colour("dark-pink") | #7c2855
nhsuk-colour("pink") | #ae2573
nhsuk-colour("orange") | #ed8b00
nhsuk-colour("warm-yellow") | #ffb81c
nhsuk-colour("pale-yellow") | #fff9c4
nhsuk-colour("black") | #212b32
nhsuk-colour("grey-1") | #4c6272
nhsuk-colour("grey-2") | #768692
nhsuk-colour("grey-3") | #aeb7bd
nhsuk-colour("grey-4") | #d8dde0
nhsuk-colour("grey-5") | #f0f4f5
nhsuk-colour("white") | #ffffff

## Extended colours

The NHS Identity Guidelines have an extended colour palette . We haven't tested these colours yet for digital use.

## Accessibility

Make sure that what the colour is "saying" is available in other ways. Read " Do not rely on colour or position alone " in our accessibility guidance.

### Colour contrast

Text, interface components (like buttons) and graphic elements must have contrast ratios that meet the contrast minimum for AA of the Web Content Accessibility Guidelines (WCAG 2.2) . We aim for AAA as far as possible.

This helps people with low vision and colour vision deficiency (colour blindness) who find it difficult to distinguish between certain colours, often shades of red, yellow and green.

Not all combinations from our colour palette meet the minimum contrast. For example, $nhsuk-border-colour has low contrast on our page background.

Use a tool to calculate the ratio between the element and the adjacent colour. For example, the white arrow (foreground) and the green circle (background) in an action link .

If you rely on users understanding a graphic (like an icon) without text, it must meet the minimum contrast ratio. If it also has text, it does not have to meet the requirement but we recommend you try to meet it anyway.

Components that are visible but not currently active (like a submit button that is not active until the user has filled in the form) do not have to meet the requirement. But if you can meet the minimum contrast without it being confusing, it will help people with low vision.

#### WCAG 2.2 AA

The contrast ratio should be at least:

- 4.5:1 for small text (smaller than 24px, or smaller than 19px if bold)

- 3:1 for large text (24px or over, or 19px or over if bold) and components (like a text input field or button) and graphic elements (like an icon)

#### WCAG 2.2 AAA

The contrast ratio should be at least:

- 7:1 for small text (smaller than 24px, or smaller than 19px if bold)

- 4.5:1 for large text (24px or over, or 19px or over if bold) and components (like a text input field or button) and graphic elements (like an icon)

#### Testing tools

Use tools like these to check contrast:

- WebAIM's colour contrast checker

- Color Oracle (free colour blindness simulator)

Also test colour contrast with people of all abilities.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
