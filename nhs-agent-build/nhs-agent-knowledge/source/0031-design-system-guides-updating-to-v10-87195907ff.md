# Updating to version 10 – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/guides/updating-to-v10/

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

# Update guides – Updating to version 10

In August 2025, we released version 10 of the design system and NHS.UK frontend library with new features, updates and bug fixes.

This release introduces a number of breaking changes.

Follow this guide carefully when applying updates to make sure your service does not break.

Learn more about the NHS.UK frontend library .

If you are using a build of the design system in another language or framework, for example React or a Wordpress theme, you may need the maintainer of that tool to follow these updates to support version 10 before you can upgrade.

## Contents

- Stylesheets

- JavaScript

- Static assets

- Nunjucks

- Page template

- Components

- Sass functions

## Stylesheets

The file structure for the stylesheets has changed. You will have to make different updates depending on whether you are compiling the Sass or using the precompiled CSS files.

### Sass

If you are compiling the Sass files, you must add node_modules to load paths, by either:

- calling the Sass compiler from the command line with the --load-path node_modules flag

- using the JavaScript API with loadPaths: ['node_modules'] in the options object

Replace packages with dist/nhsuk for any @forward , @use or @import paths in your Sass files, making sure to remove the unnecessary node_modules/ prefix:

```text
- @import "node_modules/nhsuk-frontend/packages/nhsuk";
+ @import "nhsuk-frontend/dist/nhsuk";
```

### Precompiled stylesheets

If you are using the precompiled file in the npm package at node_modules/nhsuk-frontend/dist/nhsuk.min.css , update this path to node_modules/nhsuk-frontend/dist/nhsuk/nhsuk-frontend.min.css .

We no longer provide a non-minified precompiled file, so you should update any usage of node_modules/nhsuk-frontend/dist/nhsuk.css too.

If you are using the precompiled file from the GitHub release zip file at css/nhsuk-<VERSION-NUMBER>.min.css , update this path to nhsuk-frontend-<VERSION-NUMBER>.min.css .

## JavaScript

The file structure for the JavaScript has changed. You will have to make different updates depending on whether you are using a bundler or the precompiled JavaScript.

### Using a JavaScript bundler

For JavaScript imported using a bundler, consolidate all import or require() calls to nhsuk-frontend/packages/components/* into a single statement:

```text
- import initButtons from 'nhsuk-frontend/packages/components/button/button.js'
- import initCheckboxes from 'nhsuk-frontend/packages/components/checkboxes/checkboxes.js'
+ import { initButtons, initCheckboxes } from 'nhsuk-frontend'
```

Make sure component initialisation functions match the named exports:

```text
import
{ initButtons, initCheckboxes }
from
'nhsuk-frontend'
// Initialise all button components
initButtons
();
// Initialise all checkboxes components
initCheckboxes
();
```

Or alternatively, you can initialise individual component classes:

```text
import
{
Button
,
Checkboxes
}
from
'nhsuk-frontend'
;
const
$button =
document
.
querySelector
(
'.app-button'
)
const
$checkboxes =
document
.
querySelector
(
'.app-checkboxes'
)
// Initialise single button component
new
Button
($button);
// Initialise single checkboxes component
new
Checkboxes
($checkboxes);
```

### Using precompiled JavaScript

For precompiled JavaScript, note the following path changes:

If you are using the precompiled file in the npm package at node_modules/nhsuk-frontend/dist/nhsuk.min.js , update this path to node_modules/nhsuk-frontend/dist/nhsuk/nhsuk-frontend.min.js

If you are using the precompiled file from the GitHub release zip file at css/nhsuk-<VERSION-NUMBER>.min.js , update this path to nhsuk-frontend-<VERSION-NUMBER>.min.js .

## Static assets

The location of the folder containing static assets such as logos, icons and other images has changed.

Replace packages/ with dist/nhsuk when copying or serving NHS.UK frontend logos, icons and other assets:

```text
- node_modules/nhsuk-frontend/packages/assets
+ node_modules/nhsuk-frontend/dist/nhsuk/assets
```

For example, if you're using Express.js , request routing could be set up as follows:

```text
router.
use
(
'/assets'
, [
  express.
static
(
'node_modules/nhsuk-frontend/dist/nhsuk/assets'
)
])
```

## Nunjucks

If you are using the Nunjucks macros, update the list of paths in nunjucks.configure() :

```text
nunjucks.configure([
-   'node_modules/nhsuk-frontend/packages/components',
-   'node_modules/nhsuk-frontend/packages/macros'
+   'node_modules/nhsuk-frontend/dist/nhsuk/components',
+   'node_modules/nhsuk-frontend/dist/nhsuk/macros',
+   'node_modules/nhsuk-frontend/dist/nhsuk',
+   'node_modules/nhsuk-frontend/dist'
])
```

## Page template

We have made several updates to the page template .

### Update the JavaScript supported script snippet

The <script> snippet at the top of the <body> tag to check whether JavaScript is supported has been updated.

Change this:

```text
<
script
>
document
.
body
.
className
= ((
document
.
body
.
className
) ?
document
.
body
.
className
+
' js-enabled'
:
'js-enabled'
);
</
script
>
```

to this:

```text
<
script
>
document
.
body
.
className
+=
' js-enabled'
+ (
'noModule'
in
HTMLScriptElement
.
prototype
?
' nhsuk-frontend-supported'
:
''
);
</
script
>
```

If you are using the Nunjucks page template included within NHS frontend, you do not need to make this change.

### Update the main script tag

The main <script> tag for the JavaScript has been updated and moved.

You need to:

- move it from within the <head> element to just before the closing </body> tag

- remove the defer boolean attribute

- add the type="module" attribute

- add a second <script> tag to import and initialise the components

Before:

```text
<
script
src
=
"/<JAVASCRIPTS-PATH>/nhsuk.min.js"
defer
>
</
script
>
</
head
>
```

After:

```text
<
script
type
=
"module"
src
=
"/<JAVASCRIPTS-PATH>/nhsuk-frontend.min.js"
>
</
script
>
<
script
type
=
"module"
>
import
{ initAll }
from
'/<JAVASCRIPTS-PATH>/nhsuk-frontend.min.js'
initAll
()
</
script
>
```

If you are using the Nunjucks page template included within NHS frontend, the code should moved from the head block to the bodyEnd block.

### Remove the X-UA-Compatible meta tag

Remove the <meta http-equiv="X-UA-Compatible" content="IE=edge"> tag.

Internet Explorer versions 8, 9 and 10 included a feature that would try to determine if the page was built for an older version of IE and silently enable compatibility mode, modifying the rendering engine's behaviour to match the older version of IE. Setting this meta tag prevented that behaviour.

IE11 deprecated this meta tag and defaulted to always using IE11's renderer when the page has a HTML5 doctype ( <!DOCTYPE html> ).

As NHS.UK frontend no longer supports Internet Explorer versions older than 11, this meta tag should now be removed.

If you are using the Nunjucks page template included within NHS frontend, you do not need to make this change.

### Update the viewport meta tag

Update the viewport meta tag by changing shrink-to-fit=no to viewport-fit=cover :

```text
- <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
+ <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

This is to better accommodate mobile devices with camera notches.

If you are using the Nunjucks page template included within NHS frontend, you do not need to make this change.

### Update the favicons, app icons and Open Graph image tags

We've changed the names, formats and sizes of icon assets we distribute in NHS.UK frontend.

Update the list of icons in the template's head with the following:

```text
<
link
rel
=
"icon"
href
=
"/assets/images/favicon.ico"
sizes
=
"48x48"
>
<
link
rel
=
"icon"
href
=
"/assets/images/favicon.svg"
sizes
=
"any"
type
=
"image/svg+xml"
>
<
link
rel
=
"mask-icon"
href
=
"/assets/images/nhsuk-icon-mask.svg"
color
=
"#005eb8"
>
<
link
rel
=
"apple-touch-icon"
href
=
"/assets/images/nhsuk-icon-180.png"
>
<
link
rel
=
"manifest"
href
=
"/assets/manifest.json"
>
```

You will need to update the /assets/images/ file path if you copy the assets to a different location.

If you are using the Nunjucks page template included within NHS frontend, you do not need to make this change.

## Components

The generated HTML and Nunjucks params for some of the components has changed.

### Header

The generated HTML and Nunjucks macro options for the Header component has been completely refactored and changed.

Update the HTML generated for your header using the examples on Header page.

If you are using the header Nunjucks macro, then make these changes instead:

- rename the transactionalService option to the new service option, and remove the boolean transactional option

- replace the primaryLinks option with the nested navigation.items option, using text and href instead of label and url

- replace the searchAction option with the nested search.action option

- replace the searchInputName option with the nested search.name option

- remove the boolean showNav and showSearch options – the respective parts of the header are now shown automatically when navigation.items or search options are provided

#### Header modifier classes

If you are using the nhsuk-header--white-nav class to have a white background on the navigation bar, update this to nhsuk-header__navigation--white .

If you are using the nhsuk-header__navigation-list--left-aligned class, remove this as navigation items are now aligned left by default.

To restore the previous justified alignment, where navigation items appeared evenly spaced out, add the new nhsuk-header__navigation--justified modifier class.

### Footer

The footer component's Nunjucks macros and HTML have been updated for better consistency and flexibility.

See the examples on the footer page for the updated HTML.

If you are using the Nunjucks macro, make these changes instead:

- replace the links option with the nested navigation.items option

- replace the metaLinks option with the nested meta.items option

- update all items to rename label to text and URL to href

If you are using additional columns with the linksColumn2 and linksColumn3 options, update this to wrap the navigation object in an array to support multiple columns.

### Action link

The HTML for the action link has been updated.

You need to:

- remove the wrapper element <div class="nhsuk-action-link"> </div>

- rename the action link <a class="nhsuk-action-link__link" class attribute to <a class="nhsuk-action-link"

- update the SVG of the embedded icon

Before:

```text
<
div
class
=
"nhsuk-action-link"
>
<
a
class
=
"nhsuk-action-link__link"
href
=
"#"
>
<
svg
class
=
"nhsuk-icon nhsuk-icon__arrow-right-circle"
xmlns
=
"http://www.w3.org/2000/svg"
viewBox
=
"0 0 24 24"
aria-hidden
=
"true"
width
=
"36"
height
=
"36"
>
<
path
d
=
"M0 0h24v24H0z"
fill
=
"none"
>
</
path
>
<
path
d
=
"M12 2a10 10 0 0 0-9.95 9h11.64L9.74 7.05a1 1 0 0 1 1.41-1.41l5.66 5.65a1 1 0 0 1 0 1.42l-5.66 5.65a1 1 0 0 1-1.41 0 1 1 0 0 1 0-1.41L13.69 13H2.05A10 10 0 1 0 12 2z"
>
</
path
>
</
svg
>
<
span
class
=
"nhsuk-action-link__text"
>
Find your nearest A&E
</
span
>
</
a
>
</
div
>
```

After:

```text
<
a
class
=
"nhsuk-action-link"
href
=
"#"
>
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
<
span
class
=
"nhsuk-action-link__text"
>
Find your nearest A&E
</
span
>
</
a
>
```

You do not need to do anything if you're using Nunjucks macros.

### Back link

For consistency with other links, we've added an underline to the back link component. We've also changed the default text from "Go back" to "Back" in all examples.

The HTML has been updated to no longer have a wrapper element or an embedded SVG icon.

You need to make these changes:

```text
- <div class="nhsuk-back-link"> <a class="nhsuk-back-link__link" href="#">
-   <svg class="nhsuk-icon nhsuk-icon__chevron-left" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" height="24" width="24">
-     <path d="M8.5 12c0-.3.1-.5.3-.7l5-5c.4-.4 1-.4 1.4 0s.4 1 0 1.4L10.9 12l4.3 4.3c.4.4.4 1 0 1.4s-1 .4-1.4 0l-5-5c-.2-.2-.3-.4-.3-.7z"></path>
-   </svg>
-   Back</a>
- </div>
+ <a class="nhsuk-back-link" href="#">Back</a>
```

You do not need to do anything if you're using Nunjucks macros.

### Breadcrumbs

The HTML for the breadcrumbs component has been updated.

You need to:

- update the nhsuk-breadcrumb__item class to nhsuk-breadcrumb__list-item

- update the back link within the breadcrumb by removing the <p class="nhsuk-breadcrumb__back"> and replacing it with the HTML used for the regular back link

See changes:

```text
<nav class="nhsuk-breadcrumb" aria-label="Breadcrumb">
    <ol class="nhsuk-breadcrumb__list">
-     <li class="nhsuk-breadcrumb__item">
+     <li class="nhsuk-breadcrumb__list-item">
<a class="nhsuk-breadcrumb__link" href="#">Level one</a>
      </li>
-     <li class="nhsuk-breadcrumb__item">
+     <li class="nhsuk-breadcrumb__list-item">
<a class="nhsuk-breadcrumb__link" href="#">Level two</a>
      </li>
-     <li class="nhsuk-breadcrumb__item">
+     <li class="nhsuk-breadcrumb__list-item">
<a class="nhsuk-breadcrumb__link" href="#">Level three</a>
      </li>
    </ol>
-   <p class="nhsuk-breadcrumb__back">
-     <a class="nhsuk-breadcrumb__backlink" href="#">
-       <span class="nhsuk-u-visually-hidden">Back to &nbsp;</span>
-       Level three
-     </a>
-   </p>
+   <a class="nhsuk-back-link" href="#">
+    <span class="nhsuk-u-visually-hidden">Back to&nbsp;</span>
+    Level three
+   </a>
</nav>
```

You do not need to do anything if you're using Nunjucks macros.

### Details

The details component no longer uses JavaScript, and is no longer polyfilled in older browsers. If you have extended browser support requirements, check that the details component works as expected in older browsers.

There are no changes to the HTML.

If you are using the Nunjucks macro, you need to rename the text param to summary .

You can also rename the html option to text if there is no HTML markup within your content.

Make sure you are using the lowercase html option, as the the uppercase HTML option has been removed.

### Do and don't lists

The SVG icons within the Do and don't lists have been updated.

Update the tick icon like this:

```text
- <svg class="nhsuk-icon nhsuk-icon__tick" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" aria-hidden="true" width="34" height="34">
-   <path stroke-width="4" stroke-linecap="round" d="M18.4 7.8l-8.5 8.4L5.6 12" stroke="#007f3b"></path>
- </svg>
+ <svg class="nhsuk-icon nhsuk-icon--tick" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16" focusable="false" aria-hidden="true">
+   <path d="M11.4 18.8a2 2 0 0 1-2.7.1h-.1L4 14.1a1.5 1.5 0 0 1 2.1-2L10 16l8.1-8.1a1.5 1.5 0 1 1 2.2 2l-8.9 9Z"/>
+ </svg>
```

Update the cross icon like this:

```text
- <svg class="nhsuk-icon nhsuk-icon__cross" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" width="34" height="34">
-   <path d="M17 18.5c-.4 0-.8-.1-1.1-.4l-10-10c-.6-.6-.6-1.6 0-2.1.6-.6 1.5-.6 2.1 0l10 10c.6.6.6 1.5 0 2.1-.3.3-.6.4-1 .4z" fill="#d5281b"></path>
-   <path d="M7 18.5c-.4 0-.8-.1-1.1-.4-.6-.6-.6-1.5 0-2.1l10-10c.6-.6 1.5-.6 2.1 0 .6.6.6 1.5 0 2.1l-10 10c-.3.3-.6.4-1 .4z" fill="#d5281b"></path>
- </svg>
+ <svg class="nhsuk-icon nhsuk-icon--cross" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16" focusable="false" aria-hidden="true">
+   <path d="M17 18.5c-.4 0-.8-.1-1.1-.4l-10-10c-.6-.6-.6-1.6 0-2.1.6-.6 1.5-.6 2.1 0l10 10c.6.6.6 1.5 0 2.1-.3.3-.6.4-1 .4z M7 18.5c-.4 0-.8-.1-1.1-.4-.6-.6-.6-1.5 0-2.1l10-10c.6-.6 1.5-.6 2.1 0 .6.6.6 1.5 0 2.1l-10 10c-.3.3-.6.4-1 .4z"/>
+ </svg>
```

You do not neet to make any changes if you are using the Nunjucks macro.

### Pagination

The SVG icons within the pagination component have been updated.

Update the left arrow icon like this:

```text
- <svg class="nhsuk-icon nhsuk-icon__arrow-left" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" width="34" height="34">
-   <path d="M4.1 12.3l2.7 3c.2.2.5.2.7 0 .1-.1.1-.2.1-.3v-2h11c.6 0 1-.4 1-1s-.4-1-1-1h-11V9c0-.2-.1-.4-.3-.5h-.2c-.1 0-.3.1-.4.2l-2.7 3c0 .2 0 .4.1.6z"></path>
- </svg>
+ <svg class="nhsuk-icon nhsuk-icon--arrow-left" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16" focusable="false" aria-hidden="true">
+   <path d="M10.7 6.3c.4.4.4 1 0 1.4L7.4 11H19a1 1 0 0 1 0 2H7.4l3.3 3.3c.4.4.4 1 0 1.4a1 1 0 0 1-1.4 0l-5-5A1 1 0 0 1 4 12c0-.3.1-.5.3-.7l5-5a1 1 0 0 1 1.4 0Z"/>
+ </svg>
```

Update the right arrow icon like this:

```text
- <svg class="nhsuk-icon nhsuk-icon__arrow-right" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" width="34" height="34">
-   <path d="M19.6 11.66l-2.73-3A.51.51 0 0 0 16 9v2H5a1 1 0 0 0 0 2h11v2a.5.5 0 0 0 .32.46.39.39 0 0 0 .18 0 .52.52 0 0 0 .37-.16l2.73-3a.5.5 0 0 0 0-.64z"></path>
- </svg>
+ <svg class="nhsuk-icon nhsuk-icon--arrow-right" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16" focusable="false" aria-hidden="true">
+   <path d="m14.7 6.3 5 5c.2.2.3.4.3.7 0 .3-.1.5-.3.7l-5 5a1 1 0 0 1-1.4-1.4l3.3-3.3H5a1 1 0 0 1 0-2h11.6l-3.3-3.3a1 1 0 1 1 1.4-1.4Z"/>
+ </svg>
```

You do not neet to make any changes if you are using the Nunjucks macro.

### Card

The SVG arrow icon in the card component has been updated.

Update the icon like this:

```text
- <svg class="nhsuk-icon" xmlns="http://www.w3.org/2000/svg" width="27" height="27" aria-hidden="true" focusable="false">
-   <circle cx="13.333" cy="13.333" r="13.333" fill="" />
-   <g fill="none" stroke="#fff" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2.667">
-     <path d="M15.438 13l-3.771 3.771" />
-     <path d="M11.667 9.229L15.438 13" />
-   </g>
- </svg>
+ <svg class="nhsuk-icon nhsuk-icon--chevron-right-circle" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16" focusable="false" aria-hidden="true">
+   <path d="M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-.3 5.8a1 1 0 1 0-1.5 1.4l2.9 2.8-2.9 2.8a1 1 0 0 0 1.5 1.4l3.5-3.5c.4-.4.4-1 0-1.4Z"></path>
+ </svg>
```

If you are using the Nunjucks macro, make sure you are using the lowercase html option, as the the uppercase HTML option has been removed.

### Buttons

All buttons are now displayed at full width on mobile. Check that it does not break any of your layouts.

We've removed support for the nhsuk-button--disabled class. If you are using this, remove it and use the disabled attribute to mark the button as disabled instead.

Buttons and links can now be grouped together so that they appear side-by-side on tablet and desktop by using a <div class="nhsuk-button-group"> </div> container. If you are currently doing this using custom CSS code, you can remove that code and use the class provided.

### Inset text

There are no changes to the HTML.

If you are using the Nunjucks macro for inset text , make sure you are using the lowercase html option, as the the uppercase HTML option has been removed.

### Warning callout

There are no changes to the HTML.

If you are using the Nunjucks macro for warning callout , make sure you are using the lowercase html option, as the the uppercase HTML option has been removed.

### Tabs

There are no changes to the HTML or Nunjucks for tabs .

The tabs component no longer triggers the tab.show and tab.hide custom JavaScript events. Get in touch if you need to continue using these events. Checkboxes The HTML has been updated to add a missing data-module attribute: - <div class="nhsuk-checkboxes"> + <div class="nhsuk-checkboxes" data-module="nhsuk-checkboxes"> If you are using the Nunjucks macro, the first checkbox input's id attribute no longer has the suffix -1 . You will need to update any links to the first checkbox input from error summary components to remove this suffix. Radios The HTML has been updated to add a missing data-module attribute: - <div class="nhsuk-radios"> + <div class="nhsuk-radios" data-module="nhsuk-radios"> If you are using the Nunjucks macro, the first radio input's id attribute no longer has the suffix -1 . You will need to update any links to the first radio input from error summary components to remove this suffix. Skip link The HTML has been updated to add a missing data-module attribute: - <div class="nhsuk-skip-link"> + <div class="nhsuk-skip-link" data-module="nhsuk-skip-link"> Notification banners A notification banner component has been added. If you have created your own custom notification banner component, you can replace this with the newly added one. Sass functions If you make use of the Sass functions, variables or mixins for your own custom CSS, you may need to make some changes. Tinted and shaded colours Sass colour tint and shade variables (e.g. $color_tint_nhsuk-black-10 ) have been removed but are available using the nhsuk-tint and nhsuk-shade functions: Before: Colour variable After: Suggested replacement $color_tint_nhsuk-black-10 nhsuk-tint(nhsuk-colour("black"), 10%) $color_shade_nhsuk-blue-20 nhsuk-shade(nhsuk-colour("blue"), 20%) $color_shade_nhsuk-blue-35 nhsuk-shade(nhsuk-colour("blue"), 35%) $color_shade_nhsuk-blue-50 nhsuk-shade(nhsuk-colour("blue"), 50%) $color_shade_nhsuk-green-35 nhsuk-shade(nhsuk-colour("green"), 35%) $color_shade_nhsuk-green-50 nhsuk-shade(nhsuk-colour("green"), 50%) NHS colour function added The Sass colour palette variables (e.g. $color_nhsuk-blue ) have been moved into a new single $nhsuk-colours map. If you need to reference a colour within your application you should use the new nhsuk-colour function: .nhsuk-example { - color: $color_nhsuk-blue; + color: nhsuk-colour("blue"); } The existing colour variables will continue to work but are deprecated and will be removed in a future release. Typography scale point 24 removed The point 24 (24px large screens, 20px small screens) on the typography scale has been removed, after previously being deprecated in version 9.5.0. Use either point 22 or point 26 instead. Main wrapper mixins removed We've removed the govuk-main-wrapper() , govuk-main-wrapper--l() and govuk-main-wrapper--s() Sass mixins, after previously being deprecated in version 9.5.0. Remove any use of these mixins and replace them with the nhsuk-main-wrapper , nhsuk-main-wrapper--l and nhsuk-main-wrapper--s classes in your HTML instead. Class param removed from grid column mixin If you're using the nhsuk-grid-column() Sass mixin to create custom grid classes, you must remove the $class parameter: .app-grid-column-one-quarter-at-desktop { - @include nhsuk-grid-column(one-quarter, $at: desktop, $class: false); + @include nhsuk-grid-column(one-quarter, $at: desktop); } Prefix added to mixins and functions Sass mixins have been updated to all have an nhsuk- prefix. If you are using any of these in your code, update the names of the functions as follows: govuk-exports updated to nhsuk-exports govuk-grid-column updated to nhsuk-grid-column govuk-shape-arrow updated to nhsuk-shape-arrow govuk-width-container updated to nhsuk-width-container grid-width updated to nhsuk-grid-width tint updated to nhsuk-tint shade updated to nhsuk-shade Color spelling updated to colour All Sass variables and mixins have been updated to use "colour" (not "color") spelling. For example: $nhsuk-link-color renamed to $nhsuk-link-colour $nhsuk-link-hover-color renamed to $nhsuk-link-hover-colour $nhsuk-link-active-color renamed to $nhsuk-link-active-colour $nhsuk-link-visited-color renamed to $nhsuk-link-visited-colour nhsuk-print-color() renamed to nhsuk-print-colour() nhsuk-text-color() renamed to nhsuk-text-colour() You can still use the previous names but they are deprecated and will be removed in a future breaking release. Grid row mixin removed The govuk-grid-row mixin has been removed. If you are using this, update your code to use the nhsuk-grid-row class in your HTML instead. Iff function removed The iff function has been removed. If you are using this, update your code to use the Sass if function instead. Updates to this page Updated: August 2025

### Checkboxes

The HTML has been updated to add a missing data-module attribute:

```text
- <div class="nhsuk-checkboxes">
+ <div class="nhsuk-checkboxes" data-module="nhsuk-checkboxes">
```

If you are using the Nunjucks macro, the first checkbox input's id attribute no longer has the suffix -1 . You will need to update any links to the first checkbox input from error summary components to remove this suffix.

### Radios

The HTML has been updated to add a missing data-module attribute:

```text
- <div class="nhsuk-radios">
+ <div class="nhsuk-radios" data-module="nhsuk-radios">
```

If you are using the Nunjucks macro, the first radio input's id attribute no longer has the suffix -1 . You will need to update any links to the first radio input from error summary components to remove this suffix.

### Skip link

The HTML has been updated to add a missing data-module attribute:

```text
- <div class="nhsuk-skip-link">
+ <div class="nhsuk-skip-link" data-module="nhsuk-skip-link">
```

### Notification banners

A notification banner component has been added.

If you have created your own custom notification banner component, you can replace this with the newly added one.

## Sass functions

If you make use of the Sass functions, variables or mixins for your own custom CSS, you may need to make some changes.

### Tinted and shaded colours

Sass colour tint and shade variables (e.g. $color_tint_nhsuk-black-10 ) have been removed but are available using the nhsuk-tint and nhsuk-shade functions:

Before: Colour variable | After: Suggested replacement
$color_tint_nhsuk-black-10 | nhsuk-tint(nhsuk-colour("black"), 10%)
$color_shade_nhsuk-blue-20 | nhsuk-shade(nhsuk-colour("blue"), 20%)
$color_shade_nhsuk-blue-35 | nhsuk-shade(nhsuk-colour("blue"), 35%)
$color_shade_nhsuk-blue-50 | nhsuk-shade(nhsuk-colour("blue"), 50%)
$color_shade_nhsuk-green-35 | nhsuk-shade(nhsuk-colour("green"), 35%)
$color_shade_nhsuk-green-50 | nhsuk-shade(nhsuk-colour("green"), 50%)

### NHS colour function added

The Sass colour palette variables (e.g. $color_nhsuk-blue ) have been moved into a new single $nhsuk-colours map.

If you need to reference a colour within your application you should use the new nhsuk-colour function:

```text
.nhsuk-example {
-   color: $color_nhsuk-blue;
+   color: nhsuk-colour("blue");
}
```

The existing colour variables will continue to work but are deprecated and will be removed in a future release.

### Typography scale point 24 removed

The point 24 (24px large screens, 20px small screens) on the typography scale has been removed, after previously being deprecated in version 9.5.0.

Use either point 22 or point 26 instead.

### Main wrapper mixins removed

We've removed the govuk-main-wrapper() , govuk-main-wrapper--l() and govuk-main-wrapper--s() Sass mixins, after previously being deprecated in version 9.5.0.

Remove any use of these mixins and replace them with the nhsuk-main-wrapper , nhsuk-main-wrapper--l and nhsuk-main-wrapper--s classes in your HTML instead.

### Class param removed from grid column mixin

If you're using the nhsuk-grid-column() Sass mixin to create custom grid classes, you must remove the $class parameter:

```text
.app-grid-column-one-quarter-at-desktop {
-   @include nhsuk-grid-column(one-quarter, $at: desktop, $class: false);
+   @include nhsuk-grid-column(one-quarter, $at: desktop);
}
```

### Prefix added to mixins and functions

Sass mixins have been updated to all have an nhsuk- prefix. If you are using any of these in your code, update the names of the functions as follows:

- govuk-exports updated to nhsuk-exports

- govuk-grid-column updated to nhsuk-grid-column govuk-shape-arrow updated to nhsuk-shape-arrow govuk-width-container updated to nhsuk-width-container grid-width updated to nhsuk-grid-width tint updated to nhsuk-tint shade updated to nhsuk-shade

- govuk-shape-arrow updated to nhsuk-shape-arrow govuk-width-container updated to nhsuk-width-container grid-width updated to nhsuk-grid-width tint updated to nhsuk-tint shade updated to nhsuk-shade

- govuk-width-container updated to nhsuk-width-container grid-width updated to nhsuk-grid-width tint updated to nhsuk-tint shade updated to nhsuk-shade

- grid-width updated to nhsuk-grid-width tint updated to nhsuk-tint shade updated to nhsuk-shade

- tint updated to nhsuk-tint shade updated to nhsuk-shade

- shade updated to nhsuk-shade

### Color spelling updated to colour

All Sass variables and mixins have been updated to use "colour" (not "color") spelling.

For example:

- $nhsuk-link-color renamed to $nhsuk-link-colour

- $nhsuk-link-hover-color renamed to $nhsuk-link-hover-colour

- $nhsuk-link-active-color renamed to $nhsuk-link-active-colour

- $nhsuk-link-visited-color renamed to $nhsuk-link-visited-colour

- nhsuk-print-color() renamed to nhsuk-print-colour()

- nhsuk-text-color() renamed to nhsuk-text-colour()

You can still use the previous names but they are deprecated and will be removed in a future breaking release.

### Grid row mixin removed

The govuk-grid-row mixin has been removed. If you are using this, update your code to use the nhsuk-grid-row class in your HTML instead.

### Iff function removed

The iff function has been removed. If you are using this, update your code to use the Sass if function instead.

## Updates to this page

Updated: August 2025
