# Prototyping – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/prototyping/

## Source content

## Principles

- Design principles

## Setup

- Prototyping

- Production code

## Design

- Styles

- Components

- Patterns

## Update guides

- Check your frontend version

- Updating to version 10

# Setup – Prototyping

Build prototypes quickly to show people and test with users.

## Before you start

To make prototypes you will need to install the NHS.UK prototype kit which has been built to work with the service manual.

## How to guides

The how to guides will show you how to use the prototype kit, from creating pages to building complex user journeys. Including guidance on passing data page to page, branching, setting up Git and publishing a prototype to the web.

## Styling page elements

The service manual provides lots of new CSS classes for styling page elements, so you should not need to write as much of your own Sass or CSS.

Explore the Styles section of the service manual to see what classes are available and how to apply them.

## Using components

Components are reusable parts of the user interface, like buttons, text inputs and checkboxes. The components in the service manual are designed to be accessible and responsive.

There are 2 ways to use components in the service manual. You can either use HTML or a Nunjucks macro.

You can copy the code from the HTML or Nunjucks tabs below the examples on our component pages, like this example of a button.

- HTML code for buttons

- Nunjucks code for buttons

```text
<
button
class
=
"nhsuk-button"
data-module
=
"nhsuk-button"
type
=
"submit"
>
Continue
</
button
>
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the button.
Name element | Type string | Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided.
Name text | Type string | Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block.
Name name | Type string | Description Name for the button. If href is provided, this has no effect.
Name type | Type string | Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The button value attribute. If href is provided, this has no effect.
Name disabled | Type boolean | Description Whether the button should be disabled. If href is provided, this has no effect.
Name href | Type string | Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided.
Name variant | Type string | Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name small | Type boolean | Description If set to true , smaller button size will be used.
Name classes | Type string | Description Classes to add to the button.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the button.
Name aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when only an icon is used.
Name prevent Double Click | Type boolean | Description Prevent accidental double clicks on submit buttons from submitting forms multiple times.
Name icon | Type object | Description Can be used to add an icon to the button. See macro options for icon .

Name | Type | Description
Name name | Type string | Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" .
Name html | Type string | Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored.
Name placement | Type string | Description Required. Placement of the icon within the button – "start" or "end" .

```text
{%
from
"button/macro.njk"
import
button
%}
{{
button
({
text
:
"Continue"
})
}}
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

## Using Nunjucks macros

A Nunjucks macro is a simple template that generates more complex HTML. However, macros are more sensitive to mistakes than HTML, so it's worth saving and previewing.

When using Nunjucks macros in the prototype kit leave out the first line that starts with {% from ... .

## Updates to this page

Updated: August 2020
