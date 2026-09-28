# Typography – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/styles/typography/

## Source content

## Styles navigation

- Colour

- Focus state

- Icons

- Layout

- Page template

- Spacing

- Typography Font Headings Labels and legends Paragraphs Font override classes Links Lists Section break Text alignment

- Font

- Headings

- Labels and legends

- Paragraphs

- Font override classes

- Links

- Lists

- Section break

- Text alignment

- Use the NHS Frutiger font

## Reference navigation

- Override classes

# Styles – Typography

Our fonts and typographic styles, and how to apply them.

## Font

### Frutiger

Frutiger is the brand font for the NHS. NHS England has a licence for 3 weights of the font which NHS organisations in England can sign up to use.

Find out more about registering for a free licence .

The web font is referenced in the NHS.UK frontend.

### Fallback font

Default to Arial when Frutiger isn't available.

font-family: "Frutiger W01", Arial, sans-serif;

## Headings

Use heading tags such as <h1> , <h2> and so on, to tag the headings on a page. Apply a heading class, such as nhsuk-heading-l , to style them visually. Style headings consistently to create a clear content structure throughout your service.

Find out more about writing and structuring headings in the content guide .

### Headings in transactional journeys

For question pages and short content pages across a transactional journey, use nhsuk-heading-l for the main page heading <h1> , followed by nhsuk-heading-m for <h2> and so on.

If you're designing a form, read about making labels and legends headings (GOV.UK) .

```text
<
h1
class
=
"nhsuk-heading-l"
>
nhsuk-heading-l
</
h1
>
<
h2
class
=
"nhsuk-heading-m"
>
nhsuk-heading-m
</
h2
>
<
h3
class
=
"nhsuk-heading-s"
>
nhsuk-heading-s
</
h3
>
<
h4
class
=
"nhsuk-heading-xs"
>
nhsuk-heading-xs
</
h4
>
```

### Headings in long content and other types of pages

Some pages benefit from a larger <h1> to allow for better visual balance and more heading levels. Examples include:

- longer content pages

- start pages

- dashboards

For these pages, start with nhsuk-heading-xl for the <h1> , nhsuk-heading-l for <h2> , and so on.

```text
<
h1
class
=
"nhsuk-heading-xl"
>
nhsuk-heading-xl
</
h1
>
<
h2
class
=
"nhsuk-heading-l"
>
nhsuk-heading-l
</
h2
>
<
h3
class
=
"nhsuk-heading-m"
>
nhsuk-heading-m
</
h3
>
<
h4
class
=
"nhsuk-heading-s"
>
nhsuk-heading-s
</
h4
>
<
h5
class
=
"nhsuk-heading-xs"
>
nhsuk-heading-xs
</
h5
>
```

### Headings with captions

Sometimes you may need to make it clear that a page is part of a larger section or group. To do this, you can use a heading with a caption above or below it.

(Do not confuse headings with captions with table captions .)

```text
<
span
class
=
"nhsuk-caption-xl"
>
nhsuk-caption-xl
</
span
>
<
h1
class
=
"nhsuk-heading-xl"
>
nhsuk-heading-xl
</
h1
>
<
span
class
=
"nhsuk-caption-l"
>
nhsuk-caption-l
</
span
>
<
h1
class
=
"nhsuk-heading-l"
>
nhsuk-heading-l
</
h1
>
<
span
class
=
"nhsuk-caption-m"
>
nhsuk-caption-m
</
span
>
<
h1
class
=
"nhsuk-heading-m"
>
nhsuk-heading-m
</
h1
>
```

If the caption should be considered part of the page heading, you can also nest the caption within the <h1> , using the appropriate heading and caption classes.

```text
<
h1
class
=
"nhsuk-heading-l"
>
<
span
class
=
"nhsuk-caption-l"
>
nhsuk-caption-l
</
span
>
nhsuk-heading-l
</
h1
>
```

## Labels and legends

Style form field labels and fieldset legends to match heading sizes for visual hierarchy.

When using Nunjucks, you can set the size of labels and legends using the size option, for example: size: "l" . You can use sizes s , m , l , xl .

### Styling labels

- HTML code for typography styling labels

- Nunjucks code for typography styling labels

```text
<
h1
class
=
"nhsuk-label-wrapper"
>
<
label
class
=
"nhsuk-label nhsuk-label--l"
>
Label size large
</
label
>
</
h1
>
<
label
class
=
"nhsuk-label nhsuk-label--m"
>
Label size medium
</
label
>
<
label
class
=
"nhsuk-label nhsuk-label--s"
>
Label size small
</
label
>
<
label
class
=
"nhsuk-label"
>
Label default
</
label
>
```

```text
{%
from
"label/macro.njk"
import
label
%}
{{
label
({
text
:
"Label size large"
,
size
:
"l"
,
isPageHeading
:
true
})
}}
{{
label
({
text
:
"Label size medium"
,
size
:
"m"
})
}}
{{
label
({
text
:
"Label size small"
,
size
:
"s"
})
}}
{{
label
({
text
:
"Label default"
})
}}
```

### Styling legends

- HTML code for typography styling legends

- Nunjucks code for typography styling legends

```text
<
fieldset
class
=
"nhsuk-fieldset"
>
<
legend
class
=
"nhsuk-fieldset__legend nhsuk-fieldset__legend--l"
>
<
h1
class
=
"nhsuk-fieldset__heading"
>
Legend size large
</
h1
>
</
legend
>
</
fieldset
>
<
fieldset
class
=
"nhsuk-fieldset"
>
<
legend
class
=
"nhsuk-fieldset__legend nhsuk-fieldset__legend--m"
>
Legend size medium
</
legend
>
</
fieldset
>
<
fieldset
class
=
"nhsuk-fieldset"
>
<
legend
class
=
"nhsuk-fieldset__legend nhsuk-fieldset__legend--s"
>
Legend size small
</
legend
>
</
fieldset
>
<
fieldset
class
=
"nhsuk-fieldset"
>
<
legend
class
=
"nhsuk-fieldset__legend"
>
Legend default
</
legend
>
</
fieldset
>
```

```text
{%
from
"fieldset/macro.njk"
import
fieldset
%}
{{
fieldset
({
legend
: {
text
:
"Legend size large"
,
size
:
"l"
,
isPageHeading
:
true
}
})
}}
{{
fieldset
({
legend
: {
text
:
"Legend size medium"
,
size
:
"m"
}
})
}}
{{
fieldset
({
legend
: {
text
:
"Legend size small"
,
size
:
"s"
}
})
}}
{{
fieldset
({
legend
: {
text
:
"Legend default"
}
})
}}
```

See how to use labels and legends on question pages .

## Paragraphs

### Body

The default paragraph font size is 19px on large screens and 16px on small screens.

```text
<
p
class
=
"nhsuk-body"
>
nhsuk-body
</
p
>
```

You can also add classes to create a lead paragraph or smaller body copy to convey hierarchy in your page.

### Lead paragraph

A lead paragraph is an introductory paragraph that you can use at the top of a page to summarise the content. Lead paragraphs use 26px type on desktop and should only be used once per page if needed.

```text
<
p
class
=
"nhsuk-body-l"
>
nhsuk-body-l
</
p
>
```

### Body small

You can use the nhsuk-body-s class sparingly to make your paragraph font size smaller: 16px on larger screens and 14px on smaller screens.

The majority of your body copy should use the standard 19px paragraph size.

```text
<
p
class
=
"nhsuk-body-s"
>
nhsuk-body-s
</
p
>
```

### Bold, italics and underlining

Do not use italics or underlining (except for links , which are underlined by default). Use bold sparingly.

Find out more about bold, italics and underlining on the Formatting page in the content guide .

## Font override classes

You might need to set the font size or font weight of an element outside of the predefined heading and paragraph classes. For this you can use the font override classes in your HTML or reference the typography mixins in your own components.

### Font size

The full NHS.UK typography scale goes from 14px up to 64px on large screens. You can add these font size override classes to any other typographic class or element and they will change the font size.

```text
<
p
class
=
"nhsuk-u-font-size-64"
>
nhsuk-u-font-size-64
</
p
>
<
p
class
=
"nhsuk-u-font-size-48"
>
nhsuk-u-font-size-48
</
p
>
<
p
class
=
"nhsuk-u-font-size-36"
>
nhsuk-u-font-size-36
</
p
>
<
p
class
=
"nhsuk-u-font-size-26"
>
nhsuk-u-font-size-26
</
p
>
<
p
class
=
"nhsuk-u-font-size-22"
>
nhsuk-u-font-size-22
</
p
>
<
p
class
=
"nhsuk-u-font-size-19"
>
nhsuk-u-font-size-19
</
p
>
<
p
class
=
"nhsuk-u-font-size-16"
>
nhsuk-u-font-size-16
</
p
>
<
p
class
=
"nhsuk-u-font-size-14"
>
nhsuk-u-font-size-14
</
p
>
```

### Font weight

As with the font size, you can add a font weight override class to any other typographic class or element to change the font weight to regular or bold weight.

```text
<
p
class
=
"nhsuk-u-font-weight-normal"
>
nhsuk-u-font-weight-normal
</
p
>
<
p
class
=
"nhsuk-u-font-weight-bold"
>
nhsuk-u-font-weight-bold
</
p
>
```

### Breaking up long words

Long words, including email addresses, can create problems in limited spaces such as mobile device screens and data tables. They can overflow the layout, making users scroll horizontally to view some of your content.

You can help to reduce these issues by surrounding content likely to overflow with nhsuk-u-text-break-word .

When words are longer than the width of the container, this class splits them onto multiple lines. It makes the split exactly where the word would otherwise overflow, but this can make it difficult to read. You can control where a word can be split. There are 2 ways to do this.

#### Break with hyphen

Insert the &shy;­ HTML tag into the word at all the points where it's OK to break it up. It will add a hyphen where it breaks and will move the rest of the word to the next line.

Only use &shy;­ for long words. Do not use it for email addresses, for example, as it will insert a hyphen which users may mistake for part of the email address.

```text
<
div
class
=
"nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-one-half"
>
<
p
>
<
code
>
nhsuk-u-text-break-word
</
code
>
</
p
>
<
div
class
=
"nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-one-third nhsuk-u-one-third"
>
<
div
class
=
"nhsuk-card"
>
<
p
class
=
"nhsuk-u-text-break-word"
>
hyperparathyroidism
</
p
>
</
div
>
</
div
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
"nhsuk-grid-column-one-half"
>
<
p
>
<
code
>
&amp;
shy;
</
code
>
</
p
>
<
div
class
=
"nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-one-third nhsuk-u-one-third"
>
<
div
class
=
"nhsuk-card"
>
<
p
class
=
"nhsuk-u-text-break-word"
>
hyper
&shy;
para
&shy;
thyroidism
</
p
>
</
div
>
</
div
>
</
div
>
</
div
>
</
div
>
```

#### Break without hyphen

Insert the <wbr> HTML tag into your word at all the points where it's OK to break it up and add a line break. This is useful for long email addresses.

```text
<
div
class
=
"nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-one-half"
>
<
p
>
<
code
>
nhsuk-u-text-break-word
</
code
>
</
p
>
<
div
class
=
"nhsuk-card"
>
<
p
>
We'll send an email to:
<
span
class
=
"nhsuk-u-text-break-word"
>
communications@nettlegrovehealthpartnershipfamilypractice.nhs.net
</
span
>
.
</
p
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
"nhsuk-grid-column-one-half"
>
<
p
>
<
code
>
&lt;
wbr
&gt;
</
code
>
</
p
>
<
div
class
=
"nhsuk-card"
>
<
p
>
We'll send an email to:
<
span
class
=
"nhsuk-u-text-break-word"
>
communications@
<
wbr
>
nettlegrove
<
wbr
>
health
<
wbr
>
partnership
<
wbr
>
family
<
wbr
>
practice.nhs.net
</
span
>
.
</
p
>
</
div
>
</
div
>
</
div
>
```

There is also an example of breaking long email addresses in the table component .

## Links

Links are blue and underlined by default with a styled focus state for people who use keyboards or other devices to navigate through a page.

If your link is at the end of a sentence or paragraph, make sure that the linked text does not include the full stop.

```text
<
a
href
=
"#"
class
=
"nhsuk-link"
>
Link
</
a
>
```

If it's not helpful to distinguish between visited and unvisited states, for example when linking to pages with frequently-changing content, such as the dashboard for an admin interface, use the nhsuk-link--no-visited-state modifier class.

```text
<
a
href
=
"#"
class
=
"nhsuk-link nhsuk-link--no-visited-state"
>
Link nhsuk-link--no-visited-state
</
a
>
```

If the link is on a dark background, for example in custom components, use the nhsuk-link--reverse modifier class to make the text white.

The white links and background colour must have a contrast ratio of at least 4.5:1 to meet WCAG 2.2 success criterion 1.4.3 Contrast (minimum), level AA (W3C) .

```text
<
a
href
=
"#"
class
=
"nhsuk-link nhsuk-link--reverse"
>
Example link
</
a
>
```

## Lists

Use lists to make blocks of text easier to read, and to break information into manageable chunks.

```text
<
ul
class
=
"nhsuk-list"
>
<
li
>
<
a
href
=
"#"
>
Money, work and benefits
</
a
>
</
li
>
<
li
>
<
a
href
=
"#"
>
Care after a hospital stay
</
a
>
</
li
>
<
li
>
<
a
href
=
"#"
>
Support and benefits for carers
</
a
>
</
li
>
</
ul
>
```

### Bulleted lists

Introduce bulleted lists with a lead-in line ending in a colon. Start each item with a lowercase letter, and do not use a full stop at the end.

```text
<
p
>
Symptoms can include:
</
p
>
<
ul
class
=
"nhsuk-list nhsuk-list--bullet"
>
<
li
>
tiredness and lack of energy
</
li
>
<
li
>
shortness of breath
</
li
>
<
li
>
noticeable heartbeats (heart palpitations)
</
li
>
<
li
>
pale skin
</
li
>
</
ul
>
```

### Numbered lists

Use numbered lists instead of bulleted lists when the order of the items is relevant.

You do not need to use a lead-in line for numbered lists. Items in a numbered list should end in a full stop because each should be a complete sentence.

```text
<
h3
>
How to gargle with salt water
</
h3
>
<
ol
class
=
"nhsuk-list nhsuk-list--number"
>
<
li
>
Dissolve half a teaspoon of salt in a glass of warm water.
</
li
>
<
li
>
Gargle with the solution then spit it out – don't swallow it.
</
li
>
<
li
>
Repeat as often as you like.
</
li
>
</
ol
>
```

## Section break

You can use the nhsuk-section-break classes on an <hr> element to create a thematic break between sections of content. nhsuk-section-break has class-based modifiers for different size margins.

By default nhsuk-section-break is only visible by its margin. You can add the nhsuk-section-break--visible class to make it visible with a separator line.

```text
<
hr
class
=
"nhsuk-section-break nhsuk-section-break--xl nhsuk-section-break--visible"
>
<
hr
class
=
"nhsuk-section-break nhsuk-section-break--l nhsuk-section-break--visible"
>
<
hr
class
=
"nhsuk-section-break nhsuk-section-break--m nhsuk-section-break--visible"
>
<
hr
class
=
"nhsuk-section-break nhsuk-section-break--visible"
>
```

## Text alignment

Left align text in English. Text is left-aligned by default.

The straight edge of left-aligned text helps people who use screen magnifiers. It saves them having to search around the screen for the next line or item. People who use magnifiers may miss things that are not left-aligned.

Some people with cognitive differences have difficulty with blocks of text that are justified (aligned to left and right margins). Only centre align or fully justify text if you can show a clear clinical or user need.

For translations into languages that run right to left (like Arabic), right align instead.

### Text alignment override classes

You need to use the text alignment override class in your HTML to right align text.

Here is an example of Arabic.

```text
<
p
class
=
"nhsuk-u-text-align-right"
>
تعديل اتجاه الكتابة باللغة العربية ليكون من اليمين الى اليسار
</
p
>
```

## Research

We've tested our typography with lots of users including, for example, people with dyslexia and colour blindness.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
