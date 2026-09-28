# Know that a page is up to date – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/patterns/know-that-a-page-is-up-to-date/

## Source content

## Ask users for

- NHS numbers

## Help users to

- Check answers

- Complete multiple tasks

- Decide when and where to get care (care cards)

- Find British Sign Language content

- Know that a page is up to date

## Pages

- A to Z page

- Confirmation page

- Hub page

- Interruption page

- Mini-hub

- Question pages

- Start page

# Help users to – Know that a page is up to date

Use review dates to let users know when a page was last checked and will be checked again.

- HTML code for know that a page is up to date

- Nunjucks code for know that a page is up to date

```text
<
p
class
=
"nhsuk-body-s nhsuk-u-secondary-text-colour nhsuk-u-margin-top-7 nhsuk-u-margin-bottom-0"
>
Page last reviewed: 15 March 2025
<
br
>
Next review due: 15 March 2028
</
p
>
```

```text
<
p
class
=
"nhsuk-body-s nhsuk-u-secondary-text-colour nhsuk-u-margin-top-7 nhsuk-u-margin-bottom-0"
>
Page last reviewed: 15 March 2025
<
br
>
Next review due: 15 March 2028
</
p
>
```

## When to use this pattern

Use this pattern when your research shows users need to know when the whole page was last checked and when it will be checked again.

## When not to use this pattern

Do not use this pattern in transactional services. We have not tested review dates in forms.

Do not use it when you change something on a page but have not reviewed the whole page.

## How the pattern works

The pattern consists of 2 dates:

- when you last reviewed the page

- when you will review it again

Put whole page review dates at the bottom of the page. They are not a high priority for users looking for information.

- HTML code for know that a page is up to date page

- Nunjucks code for know that a page is up to date page

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
meta
name
=
"description"
content
=
"Design and build digital services for the NHS. Things you need to make consistent, usable services that put people first."
>
<
meta
name
=
"format-detection"
content
=
"telephone=no"
>
<!-- Verify domain with Google -->
<
meta
name
=
"google-site-verification"
content
=
"Prj4LS7KX0amTkqVrOlnEyldVIjzJqbnXgPL1zbHocM"
>
<
meta
property
=
"og:url"
content
=
""
>
<
meta
property
=
"og:site_name"
content
=
"nhs.uk"
>
<
meta
property
=
"og:title"
content
=
"NHS digital service manual"
>
<
meta
property
=
"og:description"
content
=
"Design and build digital services for the NHS. Things you need to make consistent, usable services that put people first."
>
<
meta
property
=
"og:type"
content
=
"website"
>
<
meta
property
=
"og:locale"
content
=
"en_GB"
>
<
meta
property
=
"og:image"
content
=
"undefined/assets/open-graph.png"
>
<
meta
name
=
"twitter:card"
content
=
"summary_large_image"
>
<
meta
name
=
"twitter:site"
content
=
"@nhsuk"
>
<
meta
name
=
"twitter:creator"
content
=
"@nhsuk"
>
<
meta
name
=
"twitter:image:alt"
content
=
"nhs.uk"
>
<
link
href
=
"https://www.nhs.uk/"
rel
=
"preconnect"
>
<
link
href
=
"https://assets.nhs.uk/"
rel
=
"preconnect"
crossorigin
>
<
link
href
=
""
rel
=
"canonical"
>
<
link
rel
=
"stylesheet"
href
=
"/stylesheets/main.dee0a48.min.css"
>
<
meta
property
=
"og:image"
content
=
"undefined/assets/open-graph.png"
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
Health A to Z
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
Health A to Z
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
"nhsuk-main-wrapper nhsuk-main-wrapper--s app-main-wrapper"
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
>
Page heading
</
h1
>
<
p
>
Health information goes here.
</
p
>
<
p
class
=
"nhsuk-body-s nhsuk-u-secondary-text-colour nhsuk-u-margin-top-7 nhsuk-u-margin-bottom-0"
>
Page last reviewed: 15 March 2025
<
br
>
Next review due: 15 March 2028
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
"/javascripts/main.cc2a84f.min.js"
type
=
"module"
>
</
script
>
<
script
src
=
"/javascripts/vendor/cookie-consent.min.js"
data-policy-url
=
"/cookie-policy"
type
=
"module"
>
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
block
pageTitle
-%}
Content page template
{%-
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
"Home"
},
      {
href
:
"#"
,
text
:
"Health A to Z"
}
    ]
  })
}}
{%
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
>
Page heading
</
h1
>
<
p
>
Health information goes here.
</
p
>
<
p
class
=
"nhsuk-body-s nhsuk-u-secondary-text-colour nhsuk-u-margin-top-7 nhsuk-u-margin-bottom-0"
>
Page last reviewed: 15 March 2025
<
br
>
Next review due: 15 March 2028
</
p
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
```

### Embedded content, such as videos

Review dates for embedded content should sit close to the content they relate to. Include the last reviewed date (usually the production date) and next review date in the component that holds the embedded content. This is in addition to the page review date.

For example:

### The review process

A page review involves reviewing the whole page to check that it is still accurate and up to date. Whole page reviews should be part of a planned content lifecycle where you create, then update or delete outdated content.

Depending on the content, this may involve checking it with a clinician or other subject matter expert. It also involves, for example, considering any user feedback and checking for broken links or accessibility issues.

For health content, it means reviewing the clinical evidence to make sure that the page is up to date. If there are changes to clinical content, a clinician must sign them off. Read more about making your service clinically safe .

The NHS website (nhs.uk) uses review dates on every page of health content as part of the work to meet the standard for creating health content , but not on campaign content.

## Research We tested review dates on a health information page in summer 2018. At first we tested them away from the main content, closer to the footer of the page, separated by a rule, but users didn't notice them there. So we removed the rule and brought the dates closer to the content. Users then read them and said that they were helpful. We have not tested review dates in transactional services and do not recommend using them. If you use a review date in a transactional service, please test it with users and let us know what you find. Letting users know about content updates Some teams find their users want to know if information has changed since the page was last reviewed or when there is an important update. People who use the service manual and design system, for example, find it helpful to know when information on a page was last updated. We're using an experimental "Updated" pattern on service manual pages to let users know when we've updated something on a page. Please share any findings you have about telling users about content updates on GitHub . We'll share our research findings there. Help us improve this guidance Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public. Feed back or share insights on GitHub Read more about how to feed back or share insights . If you have any questions, get in touch with the service manual team. Updates to this page Updated: November 2025

We tested review dates on a health information page in summer 2018.

At first we tested them away from the main content, closer to the footer of the page, separated by a rule, but users didn't notice them there. So we removed the rule and brought the dates closer to the content. Users then read them and said that they were helpful.

We have not tested review dates in transactional services and do not recommend using them. If you use a review date in a transactional service, please test it with users and let us know what you find.

### Letting users know about content updates

Some teams find their users want to know if information has changed since the page was last reviewed or when there is an important update.

People who use the service manual and design system, for example, find it helpful to know when information on a page was last updated. We're using an experimental "Updated" pattern on service manual pages to let users know when we've updated something on a page.

Please share any findings you have about telling users about content updates on GitHub . We'll share our research findings there.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: November 2025
