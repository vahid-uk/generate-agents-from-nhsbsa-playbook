# Panel – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/panel/

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

# Content presentation – Panel

Use a panel to highlight that users have done something successfully or to interrupt a journey.

- HTML code for panel

- Nunjucks code for panel

```text
<
div
class
=
"nhsuk-panel"
>
<
h1
class
=
"nhsuk-panel__heading"
>
Application complete
</
h1
>
<
div
class
=
"nhsuk-panel__body"
>
We have sent you a confirmation email
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
Name id | Type string | Description The ID of the panel.
Name heading | Type object | Description Required. Heading of the panel component. See macro options for heading .
Name title Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.text option.
Name title Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.html option.
Name title Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option.
Name title Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option.
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the panel content. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the panel content. If text is provided, the html option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire panel component in a call block.
Name classes | Type string | Description Classes to add to the panel.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the panel.
Name variant | Type string | Description Optional variant of panel. You can use only "interruption" or empty values with this option.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the heading.
Name href | Type string | Description If set, the heading will become a link.
Name caption | Type object | Description Optional caption for the heading. See macro options for caption .
Name size | Type string | Description Size of the heading – "m" , "l" or "xl" .
Name level | Type integer | Description Optional heading level. Defaults to 1 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name id | Type string | Description The ID of the caption.
Name element | Type string | Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" .
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block.
Name placement | Type string | Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" .
Name size | Type string | Description Size of the caption – "m" , "l" , "xl" or "xxl" .
Name classes | Type string | Description Classes to add to the caption.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the caption.

```text
{%
from
"panel/macro.njk"
import
panel
%}
{{
panel
({
titleText
:
"Application complete"
,
text
:
"We have sent you a confirmation email"
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## When to use a panel

Use the panel component to display important information.

There are 2 versions of this component:

- the green panel , used on confirmation pages to tell the user they have successfully completed the transaction

- the blue interruption panel , used on interruption pages to pause a user's journey with important information

## When not to use a panel

Never use the panel component to highlight important information in body content. Instead consider using:

- inset text

- a warning callout

- the pattern to help users decide when and where to get care (care cards)

## Green panel

### How to use the green panel

The panel is made up of:

- a heading that confirms what has happened

- description text, which is optional

Read how to use it in the confirmation page pattern . How to write panel text Keep your panel heading text brief. It only needs to summarise what has happened. For example, "Application complete". Use short words and phrases to make sure highlighted information is easy to read at different screen sizes. Shorter text is less likely to wrap around the panel, which can happen when using the zoom function on mobiles. If the panel heading needs to be longer, you can reduce the text size by adding the nhsuk-panel__heading--l class or setting the size: "l" Nunjucks macro option. You can add more context or details by using additional text under the heading. Blue interruption panel If you need to pause a user's journey with important information, use an interruption panel. Read how to use it in the interruption page pattern . Open this example in a new tab : panel interruption HTML code for panel interruption Nunjucks code for panel interruption HTML code for panel interruption Copy code < div class = "nhsuk-panel nhsuk-panel--interruption" > < h1 class = "nhsuk-panel__heading nhsuk-panel__heading--l" > Jodie Brown had a COVID-19 vaccine less than 3 months ago </ h1 > < div class = "nhsuk-panel__body" > < p > They had a COVID-19 vaccine on 25 December 2025. </ p > < p > For most people, the minimum recommended gap between COVID-19 vaccine doses is 3 months. </ p > < div class = "nhsuk-button-group" > < a class = "nhsuk-button nhsuk-button--reverse" data-module = "nhsuk-button" href = "#" role = "button" draggable = "false" > Continue anyway </ a > < a href = "#" > Cancel </ a > </ div > </ div > </ div > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : panel interruption Nunjucks code for panel interruption Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the panel. Name heading Type object Description Required. Heading of the panel component. See macro options for heading . Name title Text Type string Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.text option. Name title Html Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.html option. Name title Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option. Name title Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option. Name heading Level Type integer Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option. Name text Type string Description Required. If html is set, this is not required. Text to use within the panel content. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the panel content. If text is provided, the html option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire panel component in a call block. Name classes Type string Description Classes to add to the panel. Name attributes Type object Description HTML attributes (for example data attributes) to add to the panel. Name variant Type string Description Optional variant of panel. You can use only "interruption" or empty values with this option. Options for heading component Name Type Description Name id Type string Description The ID of the heading. Name text Type string Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description A visually hidden suffix added to the heading. Name href Type string Description If set, the heading will become a link. Name caption Type object Description Optional caption for the heading. See macro options for caption . Name size Type string Description Size of the heading – "m" , "l" or "xl" . Name level Type integer Description Optional heading level. Defaults to 1 . Name classes Type string Description Classes to add to the heading. Name attributes Type object Description HTML attributes (for example data attributes) to add to the heading. Options for caption component Name Type Description Name id Type string Description The ID of the caption. Name element Type string Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" . Name text Type string Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block. Name placement Type string Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" . Name size Type string Description Size of the caption – "m" , "l" , "xl" or "xxl" . Name classes Type string Description Classes to add to the caption. Name attributes Type object Description HTML attributes (for example data attributes) to add to the caption. Copy code {% from "button/macro.njk" import button %} {% from "panel/macro.njk" import panel %} {% set panelHtml %} < p > They had a COVID-19 vaccine on 25 December 2025. </ p > < p > For most people, the minimum recommended gap between COVID-19 vaccine doses is 3 months. </ p > < div class = "nhsuk-button-group" > {{ button ({ text : "Continue anyway" , href : "#" , variant : "reverse" }) }} < a href = "#" > Cancel </ a > </ div > {% endset %} {{ panel ({ heading : { text : "Jodie Brown had a COVID-19 vaccine less than 3 months ago" , size : "l" }, html : panelHtml, variant : "interruption" }) }} Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : panel interruption Help us improve this guidance Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public. Feed back or share insights on GitHub Read more about how to feed back or share insights . If you have any questions, get in touch with the service manual team. Updates to this page Updated: May 2026

#### How to write panel text

Keep your panel heading text brief. It only needs to summarise what has happened. For example, "Application complete".

Use short words and phrases to make sure highlighted information is easy to read at different screen sizes. Shorter text is less likely to wrap around the panel, which can happen when using the zoom function on mobiles.

If the panel heading needs to be longer, you can reduce the text size by adding the nhsuk-panel__heading--l class or setting the size: "l" Nunjucks macro option.

You can add more context or details by using additional text under the heading.

## Blue interruption panel

If you need to pause a user's journey with important information, use an interruption panel.

Read how to use it in the interruption page pattern .

- HTML code for panel interruption

- Nunjucks code for panel interruption

```text
<
div
class
=
"nhsuk-panel nhsuk-panel--interruption"
>
<
h1
class
=
"nhsuk-panel__heading nhsuk-panel__heading--l"
>
Jodie Brown had a COVID-19 vaccine less than 3 months ago
</
h1
>
<
div
class
=
"nhsuk-panel__body"
>
<
p
>
They had a COVID-19 vaccine on 25 December 2025.
</
p
>
<
p
>
For most people, the minimum recommended gap between COVID-19 vaccine doses is 3 months.
</
p
>
<
div
class
=
"nhsuk-button-group"
>
<
a
class
=
"nhsuk-button nhsuk-button--reverse"
data-module
=
"nhsuk-button"
href
=
"#"
role
=
"button"
draggable
=
"false"
>
Continue anyway
</
a
>
<
a
href
=
"#"
>
Cancel
</
a
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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the panel.
Name heading | Type object | Description Required. Heading of the panel component. See macro options for heading .
Name title Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.text option.
Name title Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.html option.
Name title Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option.
Name title Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option.
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the panel content. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the panel content. If text is provided, the html option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire panel component in a call block.
Name classes | Type string | Description Classes to add to the panel.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the panel.
Name variant | Type string | Description Optional variant of panel. You can use only "interruption" or empty values with this option.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the heading.
Name href | Type string | Description If set, the heading will become a link.
Name caption | Type object | Description Optional caption for the heading. See macro options for caption .
Name size | Type string | Description Size of the heading – "m" , "l" or "xl" .
Name level | Type integer | Description Optional heading level. Defaults to 1 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name id | Type string | Description The ID of the caption.
Name element | Type string | Description HTML element for the caption – for example, "span" , "p" , "h2" or "h3" . Defaults to "span" .
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the caption. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire caption component in a call block.
Name placement | Type string | Description Required. Placement of the caption relative to the heading – "before" , "after" , "start" or "end" .
Name size | Type string | Description Size of the caption – "m" , "l" , "xl" or "xxl" .
Name classes | Type string | Description Classes to add to the caption.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the caption.

```text
{%
from
"button/macro.njk"
import
button
%}
{%
from
"panel/macro.njk"
import
panel
%}
{%
set
panelHtml
%}
<
p
>
They had a COVID-19 vaccine on 25 December 2025.
</
p
>
<
p
>
For most people, the minimum recommended gap between COVID-19 vaccine doses is 3 months.
</
p
>
<
div
class
=
"nhsuk-button-group"
>
{{
button
({
text
:
"Continue anyway"
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
<
a
href
=
"#"
>
Cancel
</
a
>
</
div
>
{%
endset
%}
{{
panel
({
heading
: {
text
:
"Jodie Brown had a COVID-19 vaccine less than 3 months ago"
,
size
:
"l"
},
html
: panelHtml,
variant
:
"interruption"
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: May 2026
