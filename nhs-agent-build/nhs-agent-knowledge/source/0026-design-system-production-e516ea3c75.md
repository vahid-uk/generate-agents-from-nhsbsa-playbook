# Production code – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/production/

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

# Setup – Production code

The code you need to start building user interfaces for NHS websites and services.

## Include the NHS.UK frontend library in your project

To start using the NHS website styles, components and patterns contained here, you'll need to include the NHS.UK frontend library in your project.

There are 2 ways to do this. You can either install it using node package manager (npm) or include the compiled files in your application.

### Option 1: install using npm

We recommend installing the NHS.UK frontend library using npm .

Using this option, you will be able to:

- selectively include the CSS or JavaScript for individual components

- build your own styles or components based on the palette or typography and spacing mixins

- customise the build (for example, overriding colours or enabling global styles)

- use the component Nunjucks templates

### Option 2: include compiled files

If your project does not use npm, or if you want to try out the NHS.UK frontend library in your project without installing it through npm, you can download and include compiled stylesheets, JavaScript and the asset files .

Using this option, you will be able to include all the CSS and JavaScript of the NHS.UK frontend library in your project.

You will not be able to:

- selectively include the CSS or JavaScript for individual components

- build your own styles or components based on the palette or typography and spacing mixins

- customise the build, for example, overriding colours or enabling global styles

- use the component Nunjucks templates

## Styling page elements

The service manual provides CSS classes for styling content, instead of global styles.

The class names follow the Block Element Modifier (BEM) naming convention. This can look a bit daunting at first, but it makes robust code that's easy to maintain.

Explore the Styles section of the service manual to see what classes are available.

## Using components

The components in the service manual are designed to be accessible and responsive. There are 2 ways to implement them in your application.

You can either use HTML or, if you're using Nunjucks with node.js and you installed the NHS.UK frontend library using npm, you can use a Nunjucks Macro.

You can get the code from the HTML or Nunjucks tabs below the examples on our component pages, like this example of a button.

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

### Using Nunjucks macros

A Nunjucks macro is a simple template that generates more complex HTML.

Nunjucks macros save you time by managing repetitive or error-prone tasks, like linking form labels to their controls.

Nunjucks macros also make it easier to keep your application up to date. You can run a command to update component code instead of having to manually update your HTML.

For example, to use the button macro, use the import statement:

```text
{%
from
"nhsuk/components/button/macro.njk"
import
button
%}
```

To use Nunjucks macros in your application, you'll need to setup Nunjucks views to point to the location of NHS.UK frontend. NHS.UK frontend v10.x (latest) Configure Nunjucks search paths for v10.x versions and higher: nunjucks. configure ([ 'node_modules/nhsuk-frontend/dist/nhsuk/components' , 'node_modules/nhsuk-frontend/dist/nhsuk/macros' , 'node_modules/nhsuk-frontend/dist/nhsuk' , 'node_modules/nhsuk-frontend/dist' ]) NHS.UK frontend v9.x Configure Nunjucks search paths for v9.x versions only: nunjucks. configure ([ 'node_modules/nhsuk-frontend/packages/components' , 'node_modules/nhsuk-frontend/packages/macros' ]) Information: If you're using Nunjucks macros in production, be aware that using html arguments or ones ending with html can be a security risk. The Nunjucks templating documentation has guidance on how to mitigate the risks. Keeping your code up to date We update the NHS.UK frontend library from time to time. Check for recent releases in the NHS.UK frontend changelog . Updates to this page Updated: January 2020

#### NHS.UK frontend v10.x (latest)

Configure Nunjucks search paths for v10.x versions and higher:

```text
nunjucks.
configure
([
'node_modules/nhsuk-frontend/dist/nhsuk/components'
,
'node_modules/nhsuk-frontend/dist/nhsuk/macros'
,
'node_modules/nhsuk-frontend/dist/nhsuk'
,
'node_modules/nhsuk-frontend/dist'
])
```

#### NHS.UK frontend v9.x

Configure Nunjucks search paths for v9.x versions only:

```text
nunjucks.
configure
([
'node_modules/nhsuk-frontend/packages/components'
,
'node_modules/nhsuk-frontend/packages/macros'
])
```

If you're using Nunjucks macros in production, be aware that using html arguments or ones ending with html can be a security risk. The Nunjucks templating documentation has guidance on how to mitigate the risks.

## Keeping your code up to date

We update the NHS.UK frontend library from time to time. Check for recent releases in the NHS.UK frontend changelog .

## Updates to this page

Updated: January 2020
