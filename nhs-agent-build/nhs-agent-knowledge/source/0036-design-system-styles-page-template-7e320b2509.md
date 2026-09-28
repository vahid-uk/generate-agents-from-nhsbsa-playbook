# Page template – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/styles/page-template/

## Source content

## Styles navigation

- Colour

- Focus state

- Icons

- Layout

- Page template Page title Default page template Customised page template Changing template content

- Page title

- Default page template

- Customised page template

- Changing template content

- Spacing

- Typography

- Use the NHS Frutiger font

## Reference navigation

- Override classes

# Styles – Page template

Use this template to keep your pages consistent with other NHS services.

This page template combines boilerplate markup and components needed for a content page and a transactional page. This includes:

- JavaScript that adds a nhsuk-frontend-supported class, which components with JavaScript behaviour need

- the skip link , header and footer components

- favicons, and other page metadata

The examples we give show both HTML and Nunjucks.

You can use the HTML examples if you are not able to use Nunjucks. If you use HTML you'll need to update it manually when new versions are released.

## Page title

The page title ( <title> ) is in the HTML metadata, in the <head> section. It is displayed in the browser tab.

A basic page title is made up of the main page heading (the <h1> ) and the website name, separated by an en dash. For example: <title>Flu – NHS</title> , which is the title for the flu page on the NHS website . Use a unique and informative title on every page.

A page title can have up to 4 elements separated by dashes. They are the:

- <h1>

- section name, if the service has more than 1 section

- service name

- website

Examples from the NHS website include:

- Money, work, benefits and social care – Social care and support guide – NHS

- How old are you? – Calculate your heart age – NHS

This is an example from HMRC: Do you live in the UK? – Your details – Manage your tax credits – GOV.UK

If the user makes an error, add "Error: " to the beginning of the title so screen readers read it out as soon as possible.

If there is personally identifiable information in the <h1> , for example, in a transactional journey, you must make sure it is not recorded in your analytics package.

For example, if the <h1> is "What is Gordon's date of birth?", record "What is their date of birth?".

To do this you could change the page title to use "their" but keep "Gordon" in the <h1> . Or you could keep "Gordon" in the page title and send a different page title to your analytics package.

Find out more about writing good headings in the content guide .

See examples of page headings with legends, labels and captions in the question pages pattern .

## Default page template

This example shows the minimum required for an NHS service.

- HTML code for page template

- Nunjucks code for page template

```text
<!DOCTYPE
html
>
<
html
lang
=
"en"
>
<
head
>
<
meta
charset
=
"utf-8"
>
<
title
>
Default page template
</
title
>
<
meta
name
=
"viewport"
content
=
"width=device-width, initial-scale=1, viewport-fit=cover"
>
<
meta
name
=
"theme-color"
content
=
"#005eb8"
>
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
<
link
rel
=
"stylesheet"
href
=
"/stylesheets/nhsuk-frontend.bd25200.min.css"
>
<
link
rel
=
"stylesheet"
href
=
"/stylesheets/preview.e659bda.min.css"
>
</
head
>
<
body
>
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
<
a
class
=
"nhsuk-skip-link"
data-module
=
"nhsuk-skip-link"
href
=
"#maincontent"
>
Skip to main content
</
a
>
<
header
class
=
"nhsuk-header"
data-module
=
"nhsuk-header"
role
=
"banner"
>
<
div
class
=
"nhsuk-header__container nhsuk-width-container"
>
<
div
class
=
"nhsuk-header__service"
>
<
svg
class
=
"nhsuk-header__logo"
xmlns
=
"http://www.w3.org/2000/svg"
viewBox
=
"0 0 200 80"
height
=
"40"
width
=
"100"
focusable
=
"false"
role
=
"img"
aria-label
=
"NHS"
>
<
title
>
NHS
</
title
>
<
path
fill
=
"currentcolor"
d
=
"M200 0v80H0V0h200Zm-27.5 5.5c-14.5 0-29 5-29 22 0 10.2 7.7 13.5 14.7 16.3l.7.3c5.4 2 10.1 3.9 10.1 8.4 0 6.5-8.5 7.5-14 7.5s-12.5-1.5-16-3.5L135 70c5.5 2 13.5 3.5 20 3.5 15.5 0 32-4.5 32-22.5 0-19.5-25.5-16.5-25.5-25.5 0-5.5 5.5-6.5 12.5-6.5a35 35 0 0 1 14.5 3l4-13.5c-4.5-2-12-3-20-3Zm-131 2h-22l-14 65H22l9-45h.5l13.5 45h21.5l14-65H64l-9 45h-.5l-13-45Zm63 0h-18l-13 65h17l6-28H117l-5.5 28H129l13.5-65H125L119.5 32h-20l5-24.5Z"
/>
</
svg
>
</
div
>
</
div
>
</
header
>
<
div
class
=
"nhsuk-width-container"
>
<
main
class
=
"nhsuk-main-wrapper"
id
=
"maincontent"
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
"nhsuk-grid-column-two-thirds"
>
<
h1
class
=
"nhsuk-heading-l"
>
Default page template
</
h1
>
</
div
>
</
div
>
</
main
>
</
div
>
<
footer
class
=
"nhsuk-footer"
role
=
"contentinfo"
>
<
div
class
=
"nhsuk-width-container"
>
<
div
class
=
"nhsuk-footer__meta"
>
<
p
class
=
"nhsuk-body-s"
>
© NHS England
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
footer
>
<
script
src
=
"/javascripts/nhsuk-frontend.058ae3b.min.js"
type
=
"module"
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
{
      initAll
    }
from
'/javascripts/nhsuk-frontend.058ae3b.min.js'
initAll
()
</
script
>
</
body
>
</
html
>
```

```text
{%
block
head
%}
<
link
rel
=
"stylesheet"
href
=
"
{{
getAssetPath
(
"stylesheets/nhsuk-frontend.min.css"
) }}
"
>
<
link
rel
=
"stylesheet"
href
=
"
{{
getAssetPath
(
"stylesheets/preview.scss"
) }}
"
>
{%
endblock
%}
{%
block
pageTitle
-%}
Default page template
{%-
endblock
%}
{%
block
content
%}
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
"nhsuk-grid-column-two-thirds"
>
<
h1
class
=
"nhsuk-heading-l"
>
Default page template
</
h1
>
</
div
>
</
div
>
{%
endblock
%}
{%
block
bodyEnd
%}
<
script
src
=
"
{{
getAssetPath
(
"javascripts/nhsuk-frontend.min.js"
) }}
"
type
=
"module"
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
'
{{
getAssetPath
(
"javascripts/nhsuk-frontend.min.js"
) }}
'
    initAll()
</
script
>
{%
endblock
%}
```

## Customised page template

You can customise the page template, for example, by structuring your page layout , using the organisational header or adding a block before the main container to include a breadcrumbs component.

### Transactional page template

The transactional page template example uses the transactional service header and a back link component.

- HTML code for page template transactional

- Nunjucks code for page template transactional

```text
<!DOCTYPE
html
>
<
html
lang
=
"en"
>
<
head
>
<
meta
charset
=
"utf-8"
>
<
title
>
Transactional page template
</
title
>
<
meta
name
=
"viewport"
content
=
"width=device-width, initial-scale=1, viewport-fit=cover"
>
<
meta
name
=
"theme-color"
content
=
"#005eb8"
>
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
<
link
rel
=
"stylesheet"
href
=
"/stylesheets/nhsuk-frontend.bd25200.min.css"
>
<
link
rel
=
"stylesheet"
href
=
"/stylesheets/preview.e659bda.min.css"
>
</
head
>
<
body
>
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
<
a
class
=
"nhsuk-skip-link"
data-module
=
"nhsuk-skip-link"
href
=
"#maincontent"
>
Skip to main content
</
a
>
<
header
class
=
"nhsuk-header"
data-module
=
"nhsuk-header"
role
=
"banner"
>
<
div
class
=
"nhsuk-header__container nhsuk-width-container"
>
<
div
class
=
"nhsuk-header__service"
>
<
a
class
=
"nhsuk-header__service-logo"
href
=
"#"
aria-label
=
"NHS Service name here homepage"
>
<
svg
class
=
"nhsuk-header__logo"
xmlns
=
"http://www.w3.org/2000/svg"
viewBox
=
"0 0 200 80"
height
=
"40"
width
=
"100"
focusable
=
"false"
role
=
"img"
aria-label
=
"NHS"
>
<
title
>
NHS
</
title
>
<
path
fill
=
"currentcolor"
d
=
"M200 0v80H0V0h200Zm-27.5 5.5c-14.5 0-29 5-29 22 0 10.2 7.7 13.5 14.7 16.3l.7.3c5.4 2 10.1 3.9 10.1 8.4 0 6.5-8.5 7.5-14 7.5s-12.5-1.5-16-3.5L135 70c5.5 2 13.5 3.5 20 3.5 15.5 0 32-4.5 32-22.5 0-19.5-25.5-16.5-25.5-25.5 0-5.5 5.5-6.5 12.5-6.5a35 35 0 0 1 14.5 3l4-13.5c-4.5-2-12-3-20-3Zm-131 2h-22l-14 65H22l9-45h.5l13.5 45h21.5l14-65H64l-9 45h-.5l-13-45Zm63 0h-18l-13 65h17l6-28H117l-5.5 28H129l13.5-65H125L119.5 32h-20l5-24.5Z"
/>
</
svg
>
<
span
class
=
"nhsuk-header__service-name"
>
Service name here
</
span
>
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
header
>
<
div
class
=
"nhsuk-width-container"
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
Back
</
a
>
<
main
class
=
"nhsuk-main-wrapper nhsuk-main-wrapper--s"
id
=
"maincontent"
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
"nhsuk-grid-column-two-thirds"
>
<
h1
class
=
"nhsuk-heading-l"
>
Transactional page template
</
h1
>
</
div
>
</
div
>
</
main
>
</
div
>
<
footer
class
=
"nhsuk-footer"
role
=
"contentinfo"
>
<
div
class
=
"nhsuk-width-container"
>
<
div
class
=
"nhsuk-footer__navigation nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-one-quarter"
>
<
ul
class
=
"nhsuk-footer__list"
>
<
li
class
=
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Accessibility statement
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Contact us
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Cookies
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Privacy policy
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Terms and conditions
</
a
>
</
li
>
</
ul
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
"nhsuk-footer__meta"
>
<
p
class
=
"nhsuk-body-s"
>
© NHS England
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
footer
>
<
script
src
=
"/javascripts/nhsuk-frontend.058ae3b.min.js"
type
=
"module"
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
{
      initAll
    }
from
'/javascripts/nhsuk-frontend.058ae3b.min.js'
initAll
()
</
script
>
</
body
>
</
html
>
```

```text
{%
from
"back-link/macro.njk"
import
backLink
%}
{%
from
"header/macro.njk"
import
header
%}
{%
from
"footer/macro.njk"
import
footer
%}
{%
set
mainClasses
=
"nhsuk-main-wrapper--s"
%}
{%
block
head
%}
<
link
rel
=
"stylesheet"
href
=
"
{{
getAssetPath
(
"stylesheets/nhsuk-frontend.min.css"
) }}
"
>
<
link
rel
=
"stylesheet"
href
=
"
{{
getAssetPath
(
"stylesheets/preview.scss"
) }}
"
>
{%
endblock
%}
{%
block
pageTitle
-%}
Transactional page template
{%-
endblock
%}
{%
block
header
%}
{{
header
({
service
: {
text
:
"Service name here"
,
href
:
"#"
}
  })
}}
{%
endblock
%}
{%
block
beforeContent
%}
{{
backLink
({
href
:
"#"
,
text
:
"Back"
})
}}
{%
endblock
%}
{%
block
content
%}
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
"nhsuk-grid-column-two-thirds"
>
<
h1
class
=
"nhsuk-heading-l"
>
Transactional page template
</
h1
>
</
div
>
</
div
>
{%
endblock
%}
{%
block
footer
%}
{{
footer
({
navigation
: {
items
: [
        {
href
:
"#"
,
text
:
"Accessibility statement"
},
        {
href
:
"#"
,
text
:
"Contact us"
},
        {
href
:
"#"
,
text
:
"Cookies"
},
        {
href
:
"#"
,
text
:
"Privacy policy"
},
        {
href
:
"#"
,
text
:
"Terms and conditions"
}
      ]
    }
  })
}}
{%
endblock
%}
{%
block
bodyEnd
%}
<
script
src
=
"
{{
getAssetPath
(
"javascripts/nhsuk-frontend.min.js"
) }}
"
type
=
"module"
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
'
{{
getAssetPath
(
"javascripts/nhsuk-frontend.min.js"
) }}
'
    initAll()
</
script
>
{%
endblock
%}
```

Vertical padding is reduced on transactional services using the nhsuk-main-wrapper--s modifier class. We also recommend you use a smaller <h1> heading size using the nhsuk-heading-l modifier class. Content page template The content page template example includes navigation and search in the header and a breadcrumbs component. We recommend you use a larger <h1> heading size using the nhsuk-heading-xl modifier class. Content pages may need more heading levels and the larger size makes the heading hierarchy clearer. Open this example in a new tab : page template content HTML code for page template content Nunjucks code for page template content HTML code for page template content Copy code <!DOCTYPE html > < html lang = "en" > < head > < meta charset = "utf-8" > < title > Content page template </ title > < meta name = "viewport" content = "width=device-width, initial-scale=1, viewport-fit=cover" > < meta name = "theme-color" content = "#005eb8" > < link rel = "icon" href = "/assets/images/favicon.ico" sizes = "48x48" > < link rel = "icon" href = "/assets/images/favicon.svg" sizes = "any" type = "image/svg+xml" > < link rel = "mask-icon" href = "/assets/images/nhsuk-icon-mask.svg" color = "#005eb8" > < link rel = "apple-touch-icon" href = "/assets/images/nhsuk-icon-180.png" > < link rel = "manifest" href = "/assets/manifest.json" > < link rel = "stylesheet" href = "/stylesheets/nhsuk-frontend.bd25200.min.css" > < link rel = "stylesheet" href = "/stylesheets/preview.e659bda.min.css" > </ head > < body > < script > document . body . className += ' js-enabled' + ( 'noModule' in HTMLScriptElement . prototype ? ' nhsuk-frontend-supported' : '' ); </ script > < a class = "nhsuk-skip-link" data-module = "nhsuk-skip-link" href = "#maincontent" > Skip to main content </ a > < header class = "nhsuk-header" data-module = "nhsuk-header" role = "banner" > < div class = "nhsuk-header__container nhsuk-width-container" > < div class = "nhsuk-header__service" > < svg class = "nhsuk-header__logo" xmlns = "http://www.w3.org/2000/svg" viewBox = "0 0 200 80" height = "40" width = "100" focusable = "false" role = "img" aria-label = "NHS" > < title > NHS </ title > < path fill = "currentcolor" d = "M200 0v80H0V0h200Zm-27.5 5.5c-14.5 0-29 5-29 22 0 10.2 7.7 13.5 14.7 16.3l.7.3c5.4 2 10.1 3.9 10.1 8.4 0 6.5-8.5 7.5-14 7.5s-12.5-1.5-16-3.5L135 70c5.5 2 13.5 3.5 20 3.5 15.5 0 32-4.5 32-22.5 0-19.5-25.5-16.5-25.5-25.5 0-5.5 5.5-6.5 12.5-6.5a35 35 0 0 1 14.5 3l4-13.5c-4.5-2-12-3-20-3Zm-131 2h-22l-14 65H22l9-45h.5l13.5 45h21.5l14-65H64l-9 45h-.5l-13-45Zm63 0h-18l-13 65h17l6-28H117l-5.5 28H129l13.5-65H125L119.5 32h-20l5-24.5Z" /> </ svg > </ div > </ div > < nav class = "nhsuk-header__navigation" aria-label = "Menu" > < div class = "nhsuk-header__navigation-container nhsuk-width-container" > < ul class = "nhsuk-header__navigation-list" > < li class = "nhsuk-header__navigation-item" > < a class = "nhsuk-header__navigation-link" href = "#" > Health A to Z </ a > </ li > < li class = "nhsuk-header__navigation-item" > < a class = "nhsuk-header__navigation-link" href = "#" > Live Well </ a > </ li > < li class = "nhsuk-header__navigation-item" > < a class = "nhsuk-header__navigation-link" href = "#" > Care and support </ a > </ li > < li class = "nhsuk-header__navigation-item" > < a class = "nhsuk-header__navigation-link" href = "#" > Pregnancy </ a > </ li > < li class = "nhsuk-header__navigation-item" > < a class = "nhsuk-header__navigation-link" href = "#" > NHS services </ a > </ li > < li class = "nhsuk-header__menu" hidden > < button class = "nhsuk-header__menu-toggle nhsuk-header__navigation-link" id = "toggle-menu" aria-expanded = "false" > < span class = "nhsuk-u-visually-hidden" > Browse </ span > More </ button > </ li > </ ul > </ div > </ nav > </ header > < div class = "nhsuk-width-container" > < nav class = "nhsuk-breadcrumb" aria-label = "Breadcrumb" > < ol class = "nhsuk-breadcrumb__list" > < li class = "nhsuk-breadcrumb__list-item" > < a class = "nhsuk-breadcrumb__link" href = "#" > Level one </ a > </ li > < li class = "nhsuk-breadcrumb__list-item" > < a class = "nhsuk-breadcrumb__link" href = "#" > Level two </ a > </ li > < li class = "nhsuk-breadcrumb__list-item" > < a class = "nhsuk-breadcrumb__link" href = "#" > Level three </ a > </ li > </ ol > < a class = "nhsuk-back-link" href = "#" > < span class = "nhsuk-u-visually-hidden" > Back to </ span > Level three </ a > </ nav > < main class = "nhsuk-main-wrapper" id = "maincontent" > < div class = "nhsuk-grid-row" > < div class = "nhsuk-grid-column-two-thirds" > < h1 class = "nhsuk-heading-xl" > Content page template </ h1 > </ div > </ div > </ main > </ div > < footer class = "nhsuk-footer" role = "contentinfo" > < div class = "nhsuk-width-container" > < div class = "nhsuk-footer__navigation nhsuk-grid-row" > < div class = "nhsuk-grid-column-one-quarter" > < ul class = "nhsuk-footer__list" > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > NHS sites </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > About us </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Contact us </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Profile editor login </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Site map </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Accessibility statement </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Our policies </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Cookies </ a > </ li > </ ul > </ div > </ div > < div class = "nhsuk-footer__meta" > < p class = "nhsuk-body-s" > © NHS England </ p > </ div > </ div > </ footer > < script src = "/javascripts/nhsuk-frontend.058ae3b.min.js" type = "module" > </ script > < script type = "module" > import { initAll } from '/javascripts/nhsuk-frontend.058ae3b.min.js' initAll () </ script > </ body > </ html > Close : page template content Nunjucks code for page template content Copy code {% from "breadcrumb/macro.njk" import breadcrumb %} {% from "header/macro.njk" import header %} {% from "footer/macro.njk" import footer %} {% block head %} < link rel = "stylesheet" href = " {{ getAssetPath ( "stylesheets/nhsuk-frontend.min.css" ) }} " > < link rel = "stylesheet" href = " {{ getAssetPath ( "stylesheets/preview.scss" ) }} " > {% endblock %} {% block pageTitle -%} Content page template {%- endblock %} {% block header %} {{ header ({ navigation : { items : [ { text : "Health A to Z" , href : "#" }, { text : "Live Well" , href : "#" }, { text : "Care and support" , href : "#" }, { text : "Pregnancy" , href : "#" }, { text : "NHS services" , href : "#" } ] } }) }} {% endblock %} {% block beforeContent %} {{ breadcrumb ({ items : [ { href : "#" , text : "Level one" }, { href : "#" , text : "Level two" }, { href : "#" , text : "Level three" } ] }) }} {% endblock %} {% block content %} < div class = "nhsuk-grid-row" > < div class = "nhsuk-grid-column-two-thirds" > < h1 class = "nhsuk-heading-xl" > Content page template </ h1 > </ div > </ div > {% endblock %} {% block footer %} {{ footer ({ navigation : { items : [ { href : "#" , text : "NHS sites" }, { href : "#" , text : "About us" }, { href : "#" , text : "Contact us" }, { href : "#" , text : "Profile editor login" }, { href : "#" , text : "Site map" }, { href : "#" , text : "Accessibility statement" }, { href : "#" , text : "Our policies" }, { href : "#" , text : "Cookies" } ] } }) }} {% endblock %} {% block bodyEnd %} < script src = " {{ getAssetPath ( "javascripts/nhsuk-frontend.min.js" ) }} " type = "module" > </ script > < script type = "module" > import { initAll } from ' {{ getAssetPath ( "javascripts/nhsuk-frontend.min.js" ) }} ' initAll() </ script > {% endblock %} Close : page template content Changing template content If you're using Nunjucks, you can change the template's content using options. How you set an option depends on whether it's a 'variable' option or a 'block' option. To set a 'variable' option, use set to pass in a single value or string. For example, to add a class to the <main> element using the mainClasses option: Copy code {% set mainClasses = "nhsuk-main-wrapper--s" %} To set a 'block' option, use block to pass in a multiline value or HTML markup. For example, to add a block of HTML before the closing element in the page template using the bodyEnd option: Copy code {% block bodyEnd %} < div > < p > Example text </ p > </ div > {% endblock %} To change the components that are included in the page template by default, set their equivalent blocks. For example: Copy code {% from "header/macro.njk" import header %} {% block header %} {{ header () }} {% endblock %} Options Page template options and descriptions Option name Option type Description Option name assetPath Option type Variable Description Path to the NHS frontend assets (icons and images). Defaults to /assets . Option name bodyAttributes Option type Variable Description Add attributes to the <body> element. Add each attribute and its value in the bodyAttributes object. Option name bodyClasses Option type Variable Description Add a class to the <body> element. Option name beforeContent Option type Block Description Add content that needs to appear within the <div class="nhsuk-width-container"> container but outside the <main> element. For example: the breadcrumbs component and the back link . Option name bodyEnd Option type Block Description Add content just before the closing </body> element. Option name bodyStart Option type Block Description Add content after the opening <body> element. Option name containerClasses Option type Variable Description Add a class to the container. This is useful if you want to make the page wrapper a fixed width. Option name content Option type Block Description Add content that needs to appear centered in the <main> element. Option name footer Option type Block Description Override the default footer component. Option name head Option type Block Description Add additional items inside the <head> element. For example: <meta name="description" content="My page description"> Option name header Option type Block Description Override the default header component. Option name headIcons Option type Block Description Override the default icons used for NHS.UK branded pages. For example: <link rel="shortcut icon" href="favicon.ico" type="image/x-icon" /> Option name htmlAttributes Option type Variable Description Add attributes to the <html> element. Add each attribute and its value in the htmlAttributes object. Option name htmlLang Option type Variable Description Override the default language of your page. Defaults is en for English. Option name main Option type Block Description Override the main section of the page, which by default wraps the beforeContent block, the <main> element, and content block. Option name mainClasses Option type Variable Description Add a class to the <main> element. Option name pageTitle Option type Block Description Override the default page title ( <title> element). Option name skipLink Option type Block Description Override the default skip link component. Exploded view of the page template block areas Open this example in a new tab : page template annotated Help us improve this guidance Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public. Feed back or share insights on GitHub Read more about how to feed back or share insights . If you have any questions, get in touch with the service manual team. Updates to this page Updated: June 2026

### Content page template

The content page template example includes navigation and search in the header and a breadcrumbs component.

We recommend you use a larger <h1> heading size using the nhsuk-heading-xl modifier class. Content pages may need more heading levels and the larger size makes the heading hierarchy clearer. Open this example in a new tab : page template content HTML code for page template content Nunjucks code for page template content HTML code for page template content Copy code <!DOCTYPE html > < html lang = "en" > < head > < meta charset = "utf-8" > < title > Content page template </ title > < meta name = "viewport" content = "width=device-width, initial-scale=1, viewport-fit=cover" > < meta name = "theme-color" content = "#005eb8" > < link rel = "icon" href = "/assets/images/favicon.ico" sizes = "48x48" > < link rel = "icon" href = "/assets/images/favicon.svg" sizes = "any" type = "image/svg+xml" > < link rel = "mask-icon" href = "/assets/images/nhsuk-icon-mask.svg" color = "#005eb8" > < link rel = "apple-touch-icon" href = "/assets/images/nhsuk-icon-180.png" > < link rel = "manifest" href = "/assets/manifest.json" > < link rel = "stylesheet" href = "/stylesheets/nhsuk-frontend.bd25200.min.css" > < link rel = "stylesheet" href = "/stylesheets/preview.e659bda.min.css" > </ head > < body > < script > document . body . className += ' js-enabled' + ( 'noModule' in HTMLScriptElement . prototype ? ' nhsuk-frontend-supported' : '' ); </ script > < a class = "nhsuk-skip-link" data-module = "nhsuk-skip-link" href = "#maincontent" > Skip to main content </ a > < header class = "nhsuk-header" data-module = "nhsuk-header" role = "banner" > < div class = "nhsuk-header__container nhsuk-width-container" > < div class = "nhsuk-header__service" > < svg class = "nhsuk-header__logo" xmlns = "http://www.w3.org/2000/svg" viewBox = "0 0 200 80" height = "40" width = "100" focusable = "false" role = "img" aria-label = "NHS" > < title > NHS </ title > < path fill = "currentcolor" d = "M200 0v80H0V0h200Zm-27.5 5.5c-14.5 0-29 5-29 22 0 10.2 7.7 13.5 14.7 16.3l.7.3c5.4 2 10.1 3.9 10.1 8.4 0 6.5-8.5 7.5-14 7.5s-12.5-1.5-16-3.5L135 70c5.5 2 13.5 3.5 20 3.5 15.5 0 32-4.5 32-22.5 0-19.5-25.5-16.5-25.5-25.5 0-5.5 5.5-6.5 12.5-6.5a35 35 0 0 1 14.5 3l4-13.5c-4.5-2-12-3-20-3Zm-131 2h-22l-14 65H22l9-45h.5l13.5 45h21.5l14-65H64l-9 45h-.5l-13-45Zm63 0h-18l-13 65h17l6-28H117l-5.5 28H129l13.5-65H125L119.5 32h-20l5-24.5Z" /> </ svg > </ div > </ div > < nav class = "nhsuk-header__navigation" aria-label = "Menu" > < div class = "nhsuk-header__navigation-container nhsuk-width-container" > < ul class = "nhsuk-header__navigation-list" > < li class = "nhsuk-header__navigation-item" > < a class = "nhsuk-header__navigation-link" href = "#" > Health A to Z </ a > </ li > < li class = "nhsuk-header__navigation-item" > < a class = "nhsuk-header__navigation-link" href = "#" > Live Well </ a > </ li > < li class = "nhsuk-header__navigation-item" > < a class = "nhsuk-header__navigation-link" href = "#" > Care and support </ a > </ li > < li class = "nhsuk-header__navigation-item" > < a class = "nhsuk-header__navigation-link" href = "#" > Pregnancy </ a > </ li > < li class = "nhsuk-header__navigation-item" > < a class = "nhsuk-header__navigation-link" href = "#" > NHS services </ a > </ li > < li class = "nhsuk-header__menu" hidden > < button class = "nhsuk-header__menu-toggle nhsuk-header__navigation-link" id = "toggle-menu" aria-expanded = "false" > < span class = "nhsuk-u-visually-hidden" > Browse </ span > More </ button > </ li > </ ul > </ div > </ nav > </ header > < div class = "nhsuk-width-container" > < nav class = "nhsuk-breadcrumb" aria-label = "Breadcrumb" > < ol class = "nhsuk-breadcrumb__list" > < li class = "nhsuk-breadcrumb__list-item" > < a class = "nhsuk-breadcrumb__link" href = "#" > Level one </ a > </ li > < li class = "nhsuk-breadcrumb__list-item" > < a class = "nhsuk-breadcrumb__link" href = "#" > Level two </ a > </ li > < li class = "nhsuk-breadcrumb__list-item" > < a class = "nhsuk-breadcrumb__link" href = "#" > Level three </ a > </ li > </ ol > < a class = "nhsuk-back-link" href = "#" > < span class = "nhsuk-u-visually-hidden" > Back to </ span > Level three </ a > </ nav > < main class = "nhsuk-main-wrapper" id = "maincontent" > < div class = "nhsuk-grid-row" > < div class = "nhsuk-grid-column-two-thirds" > < h1 class = "nhsuk-heading-xl" > Content page template </ h1 > </ div > </ div > </ main > </ div > < footer class = "nhsuk-footer" role = "contentinfo" > < div class = "nhsuk-width-container" > < div class = "nhsuk-footer__navigation nhsuk-grid-row" > < div class = "nhsuk-grid-column-one-quarter" > < ul class = "nhsuk-footer__list" > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > NHS sites </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > About us </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Contact us </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Profile editor login </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Site map </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Accessibility statement </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Our policies </ a > </ li > < li class = "nhsuk-footer__list-item" > < a class = "nhsuk-footer__list-item-link" href = "#" > Cookies </ a > </ li > </ ul > </ div > </ div > < div class = "nhsuk-footer__meta" > < p class = "nhsuk-body-s" > © NHS England </ p > </ div > </ div > </ footer > < script src = "/javascripts/nhsuk-frontend.058ae3b.min.js" type = "module" > </ script > < script type = "module" > import { initAll } from '/javascripts/nhsuk-frontend.058ae3b.min.js' initAll () </ script > </ body > </ html > Close : page template content Nunjucks code for page template content Copy code {% from "breadcrumb/macro.njk" import breadcrumb %} {% from "header/macro.njk" import header %} {% from "footer/macro.njk" import footer %} {% block head %} < link rel = "stylesheet" href = " {{ getAssetPath ( "stylesheets/nhsuk-frontend.min.css" ) }} " > < link rel = "stylesheet" href = " {{ getAssetPath ( "stylesheets/preview.scss" ) }} " > {% endblock %} {% block pageTitle -%} Content page template {%- endblock %} {% block header %} {{ header ({ navigation : { items : [ { text : "Health A to Z" , href : "#" }, { text : "Live Well" , href : "#" }, { text : "Care and support" , href : "#" }, { text : "Pregnancy" , href : "#" }, { text : "NHS services" , href : "#" } ] } }) }} {% endblock %} {% block beforeContent %} {{ breadcrumb ({ items : [ { href : "#" , text : "Level one" }, { href : "#" , text : "Level two" }, { href : "#" , text : "Level three" } ] }) }} {% endblock %} {% block content %} < div class = "nhsuk-grid-row" > < div class = "nhsuk-grid-column-two-thirds" > < h1 class = "nhsuk-heading-xl" > Content page template </ h1 > </ div > </ div > {% endblock %} {% block footer %} {{ footer ({ navigation : { items : [ { href : "#" , text : "NHS sites" }, { href : "#" , text : "About us" }, { href : "#" , text : "Contact us" }, { href : "#" , text : "Profile editor login" }, { href : "#" , text : "Site map" }, { href : "#" , text : "Accessibility statement" }, { href : "#" , text : "Our policies" }, { href : "#" , text : "Cookies" } ] } }) }} {% endblock %} {% block bodyEnd %} < script src = " {{ getAssetPath ( "javascripts/nhsuk-frontend.min.js" ) }} " type = "module" > </ script > < script type = "module" > import { initAll } from ' {{ getAssetPath ( "javascripts/nhsuk-frontend.min.js" ) }} ' initAll() </ script > {% endblock %} Close : page template content Changing template content If you're using Nunjucks, you can change the template's content using options. How you set an option depends on whether it's a 'variable' option or a 'block' option. To set a 'variable' option, use set to pass in a single value or string. For example, to add a class to the <main> element using the mainClasses option: Copy code {% set mainClasses = "nhsuk-main-wrapper--s" %} To set a 'block' option, use block to pass in a multiline value or HTML markup. For example, to add a block of HTML before the closing element in the page template using the bodyEnd option: Copy code {% block bodyEnd %} < div > < p > Example text </ p > </ div > {% endblock %} To change the components that are included in the page template by default, set their equivalent blocks. For example: Copy code {% from "header/macro.njk" import header %} {% block header %} {{ header () }} {% endblock %} Options Page template options and descriptions Option name Option type Description Option name assetPath Option type Variable Description Path to the NHS frontend assets (icons and images). Defaults to /assets . Option name bodyAttributes Option type Variable Description Add attributes to the <body> element. Add each attribute and its value in the bodyAttributes object. Option name bodyClasses Option type Variable Description Add a class to the <body> element. Option name beforeContent Option type Block Description Add content that needs to appear within the <div class="nhsuk-width-container"> container but outside the <main> element. For example: the breadcrumbs component and the back link . Option name bodyEnd Option type Block Description Add content just before the closing </body> element. Option name bodyStart Option type Block Description Add content after the opening <body> element. Option name containerClasses Option type Variable Description Add a class to the container. This is useful if you want to make the page wrapper a fixed width. Option name content Option type Block Description Add content that needs to appear centered in the <main> element. Option name footer Option type Block Description Override the default footer component. Option name head Option type Block Description Add additional items inside the <head> element. For example: <meta name="description" content="My page description"> Option name header Option type Block Description Override the default header component. Option name headIcons Option type Block Description Override the default icons used for NHS.UK branded pages. For example: <link rel="shortcut icon" href="favicon.ico" type="image/x-icon" /> Option name htmlAttributes Option type Variable Description Add attributes to the <html> element. Add each attribute and its value in the htmlAttributes object. Option name htmlLang Option type Variable Description Override the default language of your page. Defaults is en for English. Option name main Option type Block Description Override the main section of the page, which by default wraps the beforeContent block, the <main> element, and content block. Option name mainClasses Option type Variable Description Add a class to the <main> element. Option name pageTitle Option type Block Description Override the default page title ( <title> element). Option name skipLink Option type Block Description Override the default skip link component. Exploded view of the page template block areas Open this example in a new tab : page template annotated Help us improve this guidance Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public. Feed back or share insights on GitHub Read more about how to feed back or share insights . If you have any questions, get in touch with the service manual team. Updates to this page Updated: June 2026

- HTML code for page template content

- Nunjucks code for page template content

```text
<!DOCTYPE
html
>
<
html
lang
=
"en"
>
<
head
>
<
meta
charset
=
"utf-8"
>
<
title
>
Content page template
</
title
>
<
meta
name
=
"viewport"
content
=
"width=device-width, initial-scale=1, viewport-fit=cover"
>
<
meta
name
=
"theme-color"
content
=
"#005eb8"
>
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
<
link
rel
=
"stylesheet"
href
=
"/stylesheets/nhsuk-frontend.bd25200.min.css"
>
<
link
rel
=
"stylesheet"
href
=
"/stylesheets/preview.e659bda.min.css"
>
</
head
>
<
body
>
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
<
a
class
=
"nhsuk-skip-link"
data-module
=
"nhsuk-skip-link"
href
=
"#maincontent"
>
Skip to main content
</
a
>
<
header
class
=
"nhsuk-header"
data-module
=
"nhsuk-header"
role
=
"banner"
>
<
div
class
=
"nhsuk-header__container nhsuk-width-container"
>
<
div
class
=
"nhsuk-header__service"
>
<
svg
class
=
"nhsuk-header__logo"
xmlns
=
"http://www.w3.org/2000/svg"
viewBox
=
"0 0 200 80"
height
=
"40"
width
=
"100"
focusable
=
"false"
role
=
"img"
aria-label
=
"NHS"
>
<
title
>
NHS
</
title
>
<
path
fill
=
"currentcolor"
d
=
"M200 0v80H0V0h200Zm-27.5 5.5c-14.5 0-29 5-29 22 0 10.2 7.7 13.5 14.7 16.3l.7.3c5.4 2 10.1 3.9 10.1 8.4 0 6.5-8.5 7.5-14 7.5s-12.5-1.5-16-3.5L135 70c5.5 2 13.5 3.5 20 3.5 15.5 0 32-4.5 32-22.5 0-19.5-25.5-16.5-25.5-25.5 0-5.5 5.5-6.5 12.5-6.5a35 35 0 0 1 14.5 3l4-13.5c-4.5-2-12-3-20-3Zm-131 2h-22l-14 65H22l9-45h.5l13.5 45h21.5l14-65H64l-9 45h-.5l-13-45Zm63 0h-18l-13 65h17l6-28H117l-5.5 28H129l13.5-65H125L119.5 32h-20l5-24.5Z"
/>
</
svg
>
</
div
>
</
div
>
<
nav
class
=
"nhsuk-header__navigation"
aria-label
=
"Menu"
>
<
div
class
=
"nhsuk-header__navigation-container nhsuk-width-container"
>
<
ul
class
=
"nhsuk-header__navigation-list"
>
<
li
class
=
"nhsuk-header__navigation-item"
>
<
a
class
=
"nhsuk-header__navigation-link"
href
=
"#"
>
Health A to Z
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
"nhsuk-header__navigation-item"
>
<
a
class
=
"nhsuk-header__navigation-link"
href
=
"#"
>
Live Well
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
"nhsuk-header__navigation-item"
>
<
a
class
=
"nhsuk-header__navigation-link"
href
=
"#"
>
Care and support
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
"nhsuk-header__navigation-item"
>
<
a
class
=
"nhsuk-header__navigation-link"
href
=
"#"
>
Pregnancy
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
"nhsuk-header__navigation-item"
>
<
a
class
=
"nhsuk-header__navigation-link"
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
"nhsuk-header__menu"
hidden
>
<
button
class
=
"nhsuk-header__menu-toggle nhsuk-header__navigation-link"
id
=
"toggle-menu"
aria-expanded
=
"false"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Browse
</
span
>
More
</
button
>
</
li
>
</
ul
>
</
div
>
</
nav
>
</
header
>
<
div
class
=
"nhsuk-width-container"
>
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
Level one
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
Level two
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
Level three
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
Level three
</
a
>
</
nav
>
<
main
class
=
"nhsuk-main-wrapper"
id
=
"maincontent"
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
"nhsuk-grid-column-two-thirds"
>
<
h1
class
=
"nhsuk-heading-xl"
>
Content page template
</
h1
>
</
div
>
</
div
>
</
main
>
</
div
>
<
footer
class
=
"nhsuk-footer"
role
=
"contentinfo"
>
<
div
class
=
"nhsuk-width-container"
>
<
div
class
=
"nhsuk-footer__navigation nhsuk-grid-row"
>
<
div
class
=
"nhsuk-grid-column-one-quarter"
>
<
ul
class
=
"nhsuk-footer__list"
>
<
li
class
=
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
NHS sites
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
About us
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Contact us
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Profile editor login
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Site map
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Accessibility statement
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Our policies
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
"nhsuk-footer__list-item"
>
<
a
class
=
"nhsuk-footer__list-item-link"
href
=
"#"
>
Cookies
</
a
>
</
li
>
</
ul
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
"nhsuk-footer__meta"
>
<
p
class
=
"nhsuk-body-s"
>
© NHS England
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
footer
>
<
script
src
=
"/javascripts/nhsuk-frontend.058ae3b.min.js"
type
=
"module"
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
{
      initAll
    }
from
'/javascripts/nhsuk-frontend.058ae3b.min.js'
initAll
()
</
script
>
</
body
>
</
html
>
```

```text
{%
from
"breadcrumb/macro.njk"
import
breadcrumb
%}
{%
from
"header/macro.njk"
import
header
%}
{%
from
"footer/macro.njk"
import
footer
%}
{%
block
head
%}
<
link
rel
=
"stylesheet"
href
=
"
{{
getAssetPath
(
"stylesheets/nhsuk-frontend.min.css"
) }}
"
>
<
link
rel
=
"stylesheet"
href
=
"
{{
getAssetPath
(
"stylesheets/preview.scss"
) }}
"
>
{%
endblock
%}
{%
block
pageTitle
-%}
Content page template
{%-
endblock
%}
{%
block
header
%}
{{
header
({
navigation
: {
items
: [
        {
text
:
"Health A to Z"
,
href
:
"#"
},
        {
text
:
"Live Well"
,
href
:
"#"
},
        {
text
:
"Care and support"
,
href
:
"#"
},
        {
text
:
"Pregnancy"
,
href
:
"#"
},
        {
text
:
"NHS services"
,
href
:
"#"
}
      ]
    }
  })
}}
{%
endblock
%}
{%
block
beforeContent
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
"Level one"
},
      {
href
:
"#"
,
text
:
"Level two"
},
      {
href
:
"#"
,
text
:
"Level three"
}
    ]
  })
}}
{%
endblock
%}
{%
block
content
%}
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
"nhsuk-grid-column-two-thirds"
>
<
h1
class
=
"nhsuk-heading-xl"
>
Content page template
</
h1
>
</
div
>
</
div
>
{%
endblock
%}
{%
block
footer
%}
{{
footer
({
navigation
: {
items
: [
        {
href
:
"#"
,
text
:
"NHS sites"
},
        {
href
:
"#"
,
text
:
"About us"
},
        {
href
:
"#"
,
text
:
"Contact us"
},
        {
href
:
"#"
,
text
:
"Profile editor login"
},
        {
href
:
"#"
,
text
:
"Site map"
},
        {
href
:
"#"
,
text
:
"Accessibility statement"
},
        {
href
:
"#"
,
text
:
"Our policies"
},
        {
href
:
"#"
,
text
:
"Cookies"
}
      ]
    }
  })
}}
{%
endblock
%}
{%
block
bodyEnd
%}
<
script
src
=
"
{{
getAssetPath
(
"javascripts/nhsuk-frontend.min.js"
) }}
"
type
=
"module"
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
'
{{
getAssetPath
(
"javascripts/nhsuk-frontend.min.js"
) }}
'
    initAll()
</
script
>
{%
endblock
%}
```

## Changing template content

If you're using Nunjucks, you can change the template's content using options.

How you set an option depends on whether it's a 'variable' option or a 'block' option.

To set a 'variable' option, use set to pass in a single value or string. For example, to add a class to the <main> element using the mainClasses option:

```text
{%
set
mainClasses
=
"nhsuk-main-wrapper--s"
%}
```

To set a 'block' option, use block to pass in a multiline value or HTML markup. For example, to add a block of HTML before the closing element in the page template using the bodyEnd option:

```text
{%
block
bodyEnd
%}
<
div
>
<
p
>
Example text
</
p
>
</
div
>
{%
endblock
%}
```

To change the components that are included in the page template by default, set their equivalent blocks. For example:

```text
{%
from
"header/macro.njk"
import
header
%}
{%
block
header
%}
{{
header
() }}
{%
endblock
%}
```

### Options

Option name | Option type | Description
Option name assetPath | Option type Variable | Description Path to the NHS frontend assets (icons and images). Defaults to /assets .
Option name bodyAttributes | Option type Variable | Description Add attributes to the <body> element. Add each attribute and its value in the bodyAttributes object.
Option name bodyClasses | Option type Variable | Description Add a class to the <body> element.
Option name beforeContent | Option type Block | Description Add content that needs to appear within the <div class="nhsuk-width-container"> container but outside the <main> element. For example: the breadcrumbs component and the back link .
Option name bodyEnd | Option type Block | Description Add content just before the closing </body> element.
Option name bodyStart | Option type Block | Description Add content after the opening <body> element.
Option name containerClasses | Option type Variable | Description Add a class to the container. This is useful if you want to make the page wrapper a fixed width.
Option name content | Option type Block | Description Add content that needs to appear centered in the <main> element.
Option name footer | Option type Block | Description Override the default footer component.
Option name head | Option type Block | Description Add additional items inside the <head> element. For example: <meta name="description" content="My page description">
Option name header | Option type Block | Description Override the default header component.
Option name headIcons | Option type Block | Description Override the default icons used for NHS.UK branded pages. For example: <link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />
Option name htmlAttributes | Option type Variable | Description Add attributes to the <html> element. Add each attribute and its value in the htmlAttributes object.
Option name htmlLang | Option type Variable | Description Override the default language of your page. Defaults is en for English.
Option name main | Option type Block | Description Override the main section of the page, which by default wraps the beforeContent block, the <main> element, and content block.
Option name mainClasses | Option type Variable | Description Add a class to the <main> element.
Option name pageTitle | Option type Block | Description Override the default page title ( <title> element).
Option name skipLink | Option type Block | Description Override the default skip link component.

#### Exploded view of the page template block areas

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
