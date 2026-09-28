# Header – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/header/

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

# Navigation – Header

Use the appropriate header at the top of every page to show users they are on an NHS service and help them get started in finding what they need.

- HTML code for header

- Nunjucks code for header

```text
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
"NHS digital service manual homepage"
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
Digital service manual
</
span
>
</
a
>
</
div
>
<
search
class
=
"nhsuk-header__search"
>
<
form
class
=
"nhsuk-header__search-form"
id
=
"search"
action
=
"https://www.nhs.uk/search/"
method
=
"get"
novalidate
>
<
div
class
=
"nhsuk-form-group"
>
<
label
class
=
"nhsuk-label nhsuk-u-visually-hidden"
for
=
"search-field"
>
Search the NHS digital service manual
</
label
>
<
div
class
=
"nhsuk-input-wrapper"
>
<
input
class
=
"nhsuk-input"
id
=
"search-field"
name
=
"q"
type
=
"search"
autocomplete
=
"off"
placeholder
=
"Search"
>
<
button
class
=
"nhsuk-button nhsuk-button--icon nhsuk-button--small"
data-module
=
"nhsuk-button"
type
=
"submit"
aria-label
=
"Search"
>
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
aria-hidden
=
"true"
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
</
button
>
</
div
>
</
div
>
</
form
>
</
search
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
NHS service standard
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
Design system
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
Content guide
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
Accessibility
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
Community and contribution
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the header.
Name logo | Type object | Description Object containing options for the logo. See macro options for logo .
Name service | Type object | Description Object containing options for the service name. See macro options for service .
Name inline | Type boolean | Description If set to true , positions the search box (or account links) inline with the NHS logo.
Name organisation | Type object | Description Settings for header with organisational logo. See macro options for organisation .
Name navigation | Type object | Description Object containing settings for the primary navigation. See macro options for navigation .
Name search | Type object | Description Object containing settings for a search box. See macro options for search .
Name account | Type object | Description Object containing settings for the account section of the header. See macro options for account .
Name container Classes | Type string | Description Classes to add to the header container, useful if you want to make the header fixed width.
Name classes | Type string | Description Classes to add to the header container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the header container.
Name colour | Type string | Description Optional colour modifier for the header. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of the link for the logo. If not set, and a service.href is set, or both are set to same value, then the logo and service name will be combined into a single link.
Name src | Type string | Description The path of the logo image, if you are not using the default NHS logo.
Name alt | Type string | Description The alt text for the logo. Defaults to "NHS" .
Name aria Label | Type string | Description The aria-label for a linked logo. Defaults to "NHS homepage" .

Name | Type | Description
Name text | Type string | Description The text to use for the service name.
Name href | Type string | Description The href of the link for the service name.

Name | Type | Description
Name name | Type string | Description Organisation name.
Name split | Type string | Description Longer organisation names can be split onto multiple lines.
Name descriptor | Type string | Description Organisation descriptor.

Name | Type | Description
Name items | Type array | Description Array of navigation links for use in the header. See macro options for navigation items .
Name aria Label | Type string | Description The aria-label for the primary navigation. Defaults to "Menu" .
Name toggle Menu Text | Type string | Description Text for the toggle menu button. Defaults to "More" .
Name toggle Menu Visually Hidden Text | Type string | Description A visually hidden prefix used before the toggle menu button text. Defaults to "Browse" .
Name classes | Type string | Description Classes to add to the primary navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the primary navigation.
Name justified | Type boolean | Description If set to true , use justified alignment where navigation items appeared evenly spaced out.
Name colour | Type string | Description Optional colour modifier for the primary navigation. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of a navigation item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the navigation item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the navigation item. If html is provided, the text option will be ignored.
Name current | Type boolean | Description Set to true if this links to the current page being shown.
Name active | Type boolean | Description Set to true if the current page is within this section, but the link doesn't necessarily link to the current page
Name classes | Type string | Description Classes to add to the list item containing the link.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the list item containing the link.

Name | Type | Description
Name action | Type string | Description The search form action attribute. Defaults to "https://www.nhs.uk/search" .
Name method | Type string | Description The search form method attribute. Defaults to "get" .
Name name | Type string | Description The name attribute for the search input. Defaults to "q" .
Name placeholder | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.input.placeholder option.
Name visually Hidden Label | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.label.visuallyHiddenText option.
Name visually Hidden Button | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.button.ariaLabel option.
Name label | Type object | Description Optional object allowing customisation of the search input label. See macro options for search label .
Name input | Type object | Description Optional object allowing customisation of the search input. See search input macro options using input component macro .
Name button | Type object | Description Optional object allowing customisation of the search button. See search button macro options using button component macro .
Name classes | Type string | Description Classes to add to the search element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the search element.

Name | Type | Description
Name visually Hidden Text | Type string | Description The visually hidden label text for the search input. Defaults to "Search the NHS website" .

Name | Type | Description
Name placeholder | Type string | Description The placeholder text for the search input. Defaults to "Search" .

Name | Type | Description
Name aria Label | Type string | Description Search button text exposed to assistive technologies, like screen readers, when only an icon is used. Defaults to "Search" .

Name | Type | Description
Name items | Type array | Description Array of account items for use in the header. See macro options for account items .
Name aria Label | Type string | Description The aria-label for the account navigation. Defaults to "Account" .
Name classes | Type string | Description Classes to add to the account navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the account navigation.

Name | Type | Description
Name href | Type string | Description The href of an account item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the account item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the account item. If html is provided, the text option will be ignored.
Name icon | Type boolean | Description Whether to include the account icon for the account item. Defaults to false .
Name action | Type string | Description If set, the item will become a button wrapped in a form with the action given. Useful for log out buttons.
Name method | Type string | Description The value to use for the method of the form if action is set. Defaults to "post" .
Name classes | Type string | Description Classes to add to the list item containing the account item.

```text
{%
from
"header/macro.njk"
import
header
%}
{{
header
({
logo
: {
href
:
"#"
,
ariaLabel
:
"NHS digital service manual homepage"
},
service
: {
text
:
"Digital service manual"
,
href
:
"#"
},
search
: {
input
: {
placeholder
:
"Search"
},
label
: {
visuallyHiddenText
:
"Search the NHS digital service manual"
}
  },
navigation
: {
items
: [
      {
text
:
"NHS service standard"
,
href
:
"#"
},
      {
text
:
"Design system"
,
href
:
"#"
},
      {
text
:
"Content guide"
,
href
:
"#"
},
      {
text
:
"Accessibility"
,
href
:
"#"
},
      {
text
:
"Community and contribution"
,
href
:
"#"
}
    ]
  }
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

The standard NHS header is made up of 4 elements:

- the NHS logo and service name

- a search bar

- navigation

- logged-in account information and links

This page also covers:

- inline account or search

- organisational headers and information about organisational logos

## When to use the standard header

Use the standard NHS header if your service is a national NHS service in England.

## When not to use the standard header

Do not use the NHS logo alone if your service is a local NHS service. Use the organisational header instead.

For information about supplier and partnership branding, see the NHS identity guidelines .

## How to use the standard header

The standard header is made up of 4 elements:

- the NHS logo which may be accompanied by the service name

- a search bar

- navigation, with exposed links and a drop-down "More" button

- account information and links

The elements you include depend on the nature of your service and your users' needs.

For example, transactional services (like Find your NHS number, on the NHS website ) do not usually include navigation and search, just the logo and service name. This is less distracting for users in a transactional journey.

If you add a link to a "help" page in your service's header, you must position it consistently in the header and always link to the same place.

### NHS logo and service name

The NHS logo must always be used. Add a service name to distinguish your service from the main NHS website at www.nhs.uk .

- HTML code for header logo service name

- Nunjucks code for header logo service name

```text
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
"Manage patients homepage"
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
Manage patients
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the header.
Name logo | Type object | Description Object containing options for the logo. See macro options for logo .
Name service | Type object | Description Object containing options for the service name. See macro options for service .
Name inline | Type boolean | Description If set to true , positions the search box (or account links) inline with the NHS logo.
Name organisation | Type object | Description Settings for header with organisational logo. See macro options for organisation .
Name navigation | Type object | Description Object containing settings for the primary navigation. See macro options for navigation .
Name search | Type object | Description Object containing settings for a search box. See macro options for search .
Name account | Type object | Description Object containing settings for the account section of the header. See macro options for account .
Name container Classes | Type string | Description Classes to add to the header container, useful if you want to make the header fixed width.
Name classes | Type string | Description Classes to add to the header container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the header container.
Name colour | Type string | Description Optional colour modifier for the header. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of the link for the logo. If not set, and a service.href is set, or both are set to same value, then the logo and service name will be combined into a single link.
Name src | Type string | Description The path of the logo image, if you are not using the default NHS logo.
Name alt | Type string | Description The alt text for the logo. Defaults to "NHS" .
Name aria Label | Type string | Description The aria-label for a linked logo. Defaults to "NHS homepage" .

Name | Type | Description
Name text | Type string | Description The text to use for the service name.
Name href | Type string | Description The href of the link for the service name.

Name | Type | Description
Name name | Type string | Description Organisation name.
Name split | Type string | Description Longer organisation names can be split onto multiple lines.
Name descriptor | Type string | Description Organisation descriptor.

Name | Type | Description
Name items | Type array | Description Array of navigation links for use in the header. See macro options for navigation items .
Name aria Label | Type string | Description The aria-label for the primary navigation. Defaults to "Menu" .
Name toggle Menu Text | Type string | Description Text for the toggle menu button. Defaults to "More" .
Name toggle Menu Visually Hidden Text | Type string | Description A visually hidden prefix used before the toggle menu button text. Defaults to "Browse" .
Name classes | Type string | Description Classes to add to the primary navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the primary navigation.
Name justified | Type boolean | Description If set to true , use justified alignment where navigation items appeared evenly spaced out.
Name colour | Type string | Description Optional colour modifier for the primary navigation. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of a navigation item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the navigation item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the navigation item. If html is provided, the text option will be ignored.
Name current | Type boolean | Description Set to true if this links to the current page being shown.
Name active | Type boolean | Description Set to true if the current page is within this section, but the link doesn't necessarily link to the current page
Name classes | Type string | Description Classes to add to the list item containing the link.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the list item containing the link.

Name | Type | Description
Name action | Type string | Description The search form action attribute. Defaults to "https://www.nhs.uk/search" .
Name method | Type string | Description The search form method attribute. Defaults to "get" .
Name name | Type string | Description The name attribute for the search input. Defaults to "q" .
Name placeholder | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.input.placeholder option.
Name visually Hidden Label | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.label.visuallyHiddenText option.
Name visually Hidden Button | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.button.ariaLabel option.
Name label | Type object | Description Optional object allowing customisation of the search input label. See macro options for search label .
Name input | Type object | Description Optional object allowing customisation of the search input. See search input macro options using input component macro .
Name button | Type object | Description Optional object allowing customisation of the search button. See search button macro options using button component macro .
Name classes | Type string | Description Classes to add to the search element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the search element.

Name | Type | Description
Name visually Hidden Text | Type string | Description The visually hidden label text for the search input. Defaults to "Search the NHS website" .

Name | Type | Description
Name placeholder | Type string | Description The placeholder text for the search input. Defaults to "Search" .

Name | Type | Description
Name aria Label | Type string | Description Search button text exposed to assistive technologies, like screen readers, when only an icon is used. Defaults to "Search" .

Name | Type | Description
Name items | Type array | Description Array of account items for use in the header. See macro options for account items .
Name aria Label | Type string | Description The aria-label for the account navigation. Defaults to "Account" .
Name classes | Type string | Description Classes to add to the account navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the account navigation.

Name | Type | Description
Name href | Type string | Description The href of an account item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the account item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the account item. If html is provided, the text option will be ignored.
Name icon | Type boolean | Description Whether to include the account icon for the account item. Defaults to false .
Name action | Type string | Description If set, the item will become a button wrapped in a form with the action given. Useful for log out buttons.
Name method | Type string | Description The value to use for the method of the form if action is set. Defaults to "post" .
Name classes | Type string | Description Classes to add to the list item containing the account item.

```text
{%
from
"header/macro.njk"
import
header
%}
{{
header
({
logo
: {
href
:
"#"
,
ariaLabel
:
"Manage patients homepage"
},
service
: {
text
:
"Manage patients"
,
href
:
"#"
}
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Search bar

The header can include a search bar.

If your content or service is on the main NHS website and you need help with search, the service manual team can put you in touch with the team that manages their search functionality.

If your service is not part of the main NHS website, you will have to arrange your own search functionality, if you need it.

- HTML code for header search

- Nunjucks code for header search

```text
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
<
search
class
=
"nhsuk-header__search"
>
<
form
class
=
"nhsuk-header__search-form"
id
=
"search"
action
=
"https://www.nhs.uk/search/"
method
=
"get"
novalidate
>
<
div
class
=
"nhsuk-form-group"
>
<
label
class
=
"nhsuk-label nhsuk-u-visually-hidden"
for
=
"search-field"
>
Search the NHS website
</
label
>
<
div
class
=
"nhsuk-input-wrapper"
>
<
input
class
=
"nhsuk-input"
id
=
"search-field"
name
=
"q"
type
=
"search"
autocomplete
=
"off"
placeholder
=
"Search"
>
<
button
class
=
"nhsuk-button nhsuk-button--icon nhsuk-button--small"
data-module
=
"nhsuk-button"
type
=
"submit"
aria-label
=
"Search"
>
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
aria-hidden
=
"true"
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
</
button
>
</
div
>
</
div
>
</
form
>
</
search
>
</
div
>
</
header
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the header.
Name logo | Type object | Description Object containing options for the logo. See macro options for logo .
Name service | Type object | Description Object containing options for the service name. See macro options for service .
Name inline | Type boolean | Description If set to true , positions the search box (or account links) inline with the NHS logo.
Name organisation | Type object | Description Settings for header with organisational logo. See macro options for organisation .
Name navigation | Type object | Description Object containing settings for the primary navigation. See macro options for navigation .
Name search | Type object | Description Object containing settings for a search box. See macro options for search .
Name account | Type object | Description Object containing settings for the account section of the header. See macro options for account .
Name container Classes | Type string | Description Classes to add to the header container, useful if you want to make the header fixed width.
Name classes | Type string | Description Classes to add to the header container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the header container.
Name colour | Type string | Description Optional colour modifier for the header. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of the link for the logo. If not set, and a service.href is set, or both are set to same value, then the logo and service name will be combined into a single link.
Name src | Type string | Description The path of the logo image, if you are not using the default NHS logo.
Name alt | Type string | Description The alt text for the logo. Defaults to "NHS" .
Name aria Label | Type string | Description The aria-label for a linked logo. Defaults to "NHS homepage" .

Name | Type | Description
Name text | Type string | Description The text to use for the service name.
Name href | Type string | Description The href of the link for the service name.

Name | Type | Description
Name name | Type string | Description Organisation name.
Name split | Type string | Description Longer organisation names can be split onto multiple lines.
Name descriptor | Type string | Description Organisation descriptor.

Name | Type | Description
Name items | Type array | Description Array of navigation links for use in the header. See macro options for navigation items .
Name aria Label | Type string | Description The aria-label for the primary navigation. Defaults to "Menu" .
Name toggle Menu Text | Type string | Description Text for the toggle menu button. Defaults to "More" .
Name toggle Menu Visually Hidden Text | Type string | Description A visually hidden prefix used before the toggle menu button text. Defaults to "Browse" .
Name classes | Type string | Description Classes to add to the primary navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the primary navigation.
Name justified | Type boolean | Description If set to true , use justified alignment where navigation items appeared evenly spaced out.
Name colour | Type string | Description Optional colour modifier for the primary navigation. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of a navigation item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the navigation item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the navigation item. If html is provided, the text option will be ignored.
Name current | Type boolean | Description Set to true if this links to the current page being shown.
Name active | Type boolean | Description Set to true if the current page is within this section, but the link doesn't necessarily link to the current page
Name classes | Type string | Description Classes to add to the list item containing the link.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the list item containing the link.

Name | Type | Description
Name action | Type string | Description The search form action attribute. Defaults to "https://www.nhs.uk/search" .
Name method | Type string | Description The search form method attribute. Defaults to "get" .
Name name | Type string | Description The name attribute for the search input. Defaults to "q" .
Name placeholder | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.input.placeholder option.
Name visually Hidden Label | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.label.visuallyHiddenText option.
Name visually Hidden Button | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.button.ariaLabel option.
Name label | Type object | Description Optional object allowing customisation of the search input label. See macro options for search label .
Name input | Type object | Description Optional object allowing customisation of the search input. See search input macro options using input component macro .
Name button | Type object | Description Optional object allowing customisation of the search button. See search button macro options using button component macro .
Name classes | Type string | Description Classes to add to the search element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the search element.

Name | Type | Description
Name visually Hidden Text | Type string | Description The visually hidden label text for the search input. Defaults to "Search the NHS website" .

Name | Type | Description
Name placeholder | Type string | Description The placeholder text for the search input. Defaults to "Search" .

Name | Type | Description
Name aria Label | Type string | Description Search button text exposed to assistive technologies, like screen readers, when only an icon is used. Defaults to "Search" .

Name | Type | Description
Name items | Type array | Description Array of account items for use in the header. See macro options for account items .
Name aria Label | Type string | Description The aria-label for the account navigation. Defaults to "Account" .
Name classes | Type string | Description Classes to add to the account navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the account navigation.

Name | Type | Description
Name href | Type string | Description The href of an account item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the account item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the account item. If html is provided, the text option will be ignored.
Name icon | Type boolean | Description Whether to include the account icon for the account item. Defaults to false .
Name action | Type string | Description If set, the item will become a button wrapped in a form with the action given. Useful for log out buttons.
Name method | Type string | Description The value to use for the method of the form if action is set. Defaults to "post" .
Name classes | Type string | Description Classes to add to the list item containing the account item.

```text
{%
from
"header/macro.njk"
import
header
%}
{{
header
({
search
: {
input
: {
placeholder
:
"Search"
},
label
: {
visuallyHiddenText
:
"Search the NHS website"
}
  }
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Navigation

Help users find what they need quickly by providing consistent navigation.

If your service is a linear end-to-end journey, you probably do not need navigation links. You can use the Complete multiple tasks pattern .

Place links to your most important top-level sections first. When there is not enough space to show all links, they will be moved into the "More" drop-down list.

You can highlight the section the user is currently in.

- HTML code for header navigation

- Nunjucks code for header navigation

```text
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
NHS service standard
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
"nhsuk-header__navigation-item nhsuk-header__navigation-item--current"
>
<
a
class
=
"nhsuk-header__navigation-link"
href
=
"#"
aria-current
=
"true"
>
<
strong
class
=
"nhsuk-header__navigation-item-current-fallback"
>
Design system
</
strong
>
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
Content guide
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
Accessibility
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
Community and contribution
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the header.
Name logo | Type object | Description Object containing options for the logo. See macro options for logo .
Name service | Type object | Description Object containing options for the service name. See macro options for service .
Name inline | Type boolean | Description If set to true , positions the search box (or account links) inline with the NHS logo.
Name organisation | Type object | Description Settings for header with organisational logo. See macro options for organisation .
Name navigation | Type object | Description Object containing settings for the primary navigation. See macro options for navigation .
Name search | Type object | Description Object containing settings for a search box. See macro options for search .
Name account | Type object | Description Object containing settings for the account section of the header. See macro options for account .
Name container Classes | Type string | Description Classes to add to the header container, useful if you want to make the header fixed width.
Name classes | Type string | Description Classes to add to the header container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the header container.
Name colour | Type string | Description Optional colour modifier for the header. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of the link for the logo. If not set, and a service.href is set, or both are set to same value, then the logo and service name will be combined into a single link.
Name src | Type string | Description The path of the logo image, if you are not using the default NHS logo.
Name alt | Type string | Description The alt text for the logo. Defaults to "NHS" .
Name aria Label | Type string | Description The aria-label for a linked logo. Defaults to "NHS homepage" .

Name | Type | Description
Name text | Type string | Description The text to use for the service name.
Name href | Type string | Description The href of the link for the service name.

Name | Type | Description
Name name | Type string | Description Organisation name.
Name split | Type string | Description Longer organisation names can be split onto multiple lines.
Name descriptor | Type string | Description Organisation descriptor.

Name | Type | Description
Name items | Type array | Description Array of navigation links for use in the header. See macro options for navigation items .
Name aria Label | Type string | Description The aria-label for the primary navigation. Defaults to "Menu" .
Name toggle Menu Text | Type string | Description Text for the toggle menu button. Defaults to "More" .
Name toggle Menu Visually Hidden Text | Type string | Description A visually hidden prefix used before the toggle menu button text. Defaults to "Browse" .
Name classes | Type string | Description Classes to add to the primary navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the primary navigation.
Name justified | Type boolean | Description If set to true , use justified alignment where navigation items appeared evenly spaced out.
Name colour | Type string | Description Optional colour modifier for the primary navigation. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of a navigation item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the navigation item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the navigation item. If html is provided, the text option will be ignored.
Name current | Type boolean | Description Set to true if this links to the current page being shown.
Name active | Type boolean | Description Set to true if the current page is within this section, but the link doesn't necessarily link to the current page
Name classes | Type string | Description Classes to add to the list item containing the link.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the list item containing the link.

Name | Type | Description
Name action | Type string | Description The search form action attribute. Defaults to "https://www.nhs.uk/search" .
Name method | Type string | Description The search form method attribute. Defaults to "get" .
Name name | Type string | Description The name attribute for the search input. Defaults to "q" .
Name placeholder | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.input.placeholder option.
Name visually Hidden Label | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.label.visuallyHiddenText option.
Name visually Hidden Button | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.button.ariaLabel option.
Name label | Type object | Description Optional object allowing customisation of the search input label. See macro options for search label .
Name input | Type object | Description Optional object allowing customisation of the search input. See search input macro options using input component macro .
Name button | Type object | Description Optional object allowing customisation of the search button. See search button macro options using button component macro .
Name classes | Type string | Description Classes to add to the search element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the search element.

Name | Type | Description
Name visually Hidden Text | Type string | Description The visually hidden label text for the search input. Defaults to "Search the NHS website" .

Name | Type | Description
Name placeholder | Type string | Description The placeholder text for the search input. Defaults to "Search" .

Name | Type | Description
Name aria Label | Type string | Description Search button text exposed to assistive technologies, like screen readers, when only an icon is used. Defaults to "Search" .

Name | Type | Description
Name items | Type array | Description Array of account items for use in the header. See macro options for account items .
Name aria Label | Type string | Description The aria-label for the account navigation. Defaults to "Account" .
Name classes | Type string | Description Classes to add to the account navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the account navigation.

Name | Type | Description
Name href | Type string | Description The href of an account item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the account item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the account item. If html is provided, the text option will be ignored.
Name icon | Type boolean | Description Whether to include the account icon for the account item. Defaults to false .
Name action | Type string | Description If set, the item will become a button wrapped in a form with the action given. Useful for log out buttons.
Name method | Type string | Description The value to use for the method of the form if action is set. Defaults to "post" .
Name classes | Type string | Description Classes to add to the list item containing the account item.

```text
{%
from
"header/macro.njk"
import
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
"NHS service standard"
,
href
:
"#"
},
      {
text
:
"Design system"
,
href
:
"#"
,
active
:
true
},
      {
text
:
"Content guide"
,
href
:
"#"
},
      {
text
:
"Accessibility"
,
href
:
"#"
},
      {
text
:
"Community and contribution"
,
href
:
"#"
}
    ]
  }
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Logged-in account information and links

The header can include account information and links for logged-in users.

- HTML code for header account basic

- Nunjucks code for header account basic

```text
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
"Manage patients homepage"
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
Manage patients
</
span
>
</
a
>
</
div
>
<
nav
class
=
"nhsuk-header__account"
aria-label
=
"Account"
>
<
ul
class
=
"nhsuk-header__account-list"
>
<
li
class
=
"nhsuk-header__account-item"
>
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
Florence Nightingale
</
li
>
<
li
class
=
"nhsuk-header__account-item"
>
<
a
class
=
"nhsuk-header__account-link"
href
=
"#"
>
Log out
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
nav
>
</
div
>
</
header
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the header.
Name logo | Type object | Description Object containing options for the logo. See macro options for logo .
Name service | Type object | Description Object containing options for the service name. See macro options for service .
Name inline | Type boolean | Description If set to true , positions the search box (or account links) inline with the NHS logo.
Name organisation | Type object | Description Settings for header with organisational logo. See macro options for organisation .
Name navigation | Type object | Description Object containing settings for the primary navigation. See macro options for navigation .
Name search | Type object | Description Object containing settings for a search box. See macro options for search .
Name account | Type object | Description Object containing settings for the account section of the header. See macro options for account .
Name container Classes | Type string | Description Classes to add to the header container, useful if you want to make the header fixed width.
Name classes | Type string | Description Classes to add to the header container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the header container.
Name colour | Type string | Description Optional colour modifier for the header. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of the link for the logo. If not set, and a service.href is set, or both are set to same value, then the logo and service name will be combined into a single link.
Name src | Type string | Description The path of the logo image, if you are not using the default NHS logo.
Name alt | Type string | Description The alt text for the logo. Defaults to "NHS" .
Name aria Label | Type string | Description The aria-label for a linked logo. Defaults to "NHS homepage" .

Name | Type | Description
Name text | Type string | Description The text to use for the service name.
Name href | Type string | Description The href of the link for the service name.

Name | Type | Description
Name name | Type string | Description Organisation name.
Name split | Type string | Description Longer organisation names can be split onto multiple lines.
Name descriptor | Type string | Description Organisation descriptor.

Name | Type | Description
Name items | Type array | Description Array of navigation links for use in the header. See macro options for navigation items .
Name aria Label | Type string | Description The aria-label for the primary navigation. Defaults to "Menu" .
Name toggle Menu Text | Type string | Description Text for the toggle menu button. Defaults to "More" .
Name toggle Menu Visually Hidden Text | Type string | Description A visually hidden prefix used before the toggle menu button text. Defaults to "Browse" .
Name classes | Type string | Description Classes to add to the primary navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the primary navigation.
Name justified | Type boolean | Description If set to true , use justified alignment where navigation items appeared evenly spaced out.
Name colour | Type string | Description Optional colour modifier for the primary navigation. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of a navigation item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the navigation item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the navigation item. If html is provided, the text option will be ignored.
Name current | Type boolean | Description Set to true if this links to the current page being shown.
Name active | Type boolean | Description Set to true if the current page is within this section, but the link doesn't necessarily link to the current page
Name classes | Type string | Description Classes to add to the list item containing the link.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the list item containing the link.

Name | Type | Description
Name action | Type string | Description The search form action attribute. Defaults to "https://www.nhs.uk/search" .
Name method | Type string | Description The search form method attribute. Defaults to "get" .
Name name | Type string | Description The name attribute for the search input. Defaults to "q" .
Name placeholder | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.input.placeholder option.
Name visually Hidden Label | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.label.visuallyHiddenText option.
Name visually Hidden Button | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.button.ariaLabel option.
Name label | Type object | Description Optional object allowing customisation of the search input label. See macro options for search label .
Name input | Type object | Description Optional object allowing customisation of the search input. See search input macro options using input component macro .
Name button | Type object | Description Optional object allowing customisation of the search button. See search button macro options using button component macro .
Name classes | Type string | Description Classes to add to the search element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the search element.

Name | Type | Description
Name visually Hidden Text | Type string | Description The visually hidden label text for the search input. Defaults to "Search the NHS website" .

Name | Type | Description
Name placeholder | Type string | Description The placeholder text for the search input. Defaults to "Search" .

Name | Type | Description
Name aria Label | Type string | Description Search button text exposed to assistive technologies, like screen readers, when only an icon is used. Defaults to "Search" .

Name | Type | Description
Name items | Type array | Description Array of account items for use in the header. See macro options for account items .
Name aria Label | Type string | Description The aria-label for the account navigation. Defaults to "Account" .
Name classes | Type string | Description Classes to add to the account navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the account navigation.

Name | Type | Description
Name href | Type string | Description The href of an account item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the account item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the account item. If html is provided, the text option will be ignored.
Name icon | Type boolean | Description Whether to include the account icon for the account item. Defaults to false .
Name action | Type string | Description If set, the item will become a button wrapped in a form with the action given. Useful for log out buttons.
Name method | Type string | Description The value to use for the method of the form if action is set. Defaults to "post" .
Name classes | Type string | Description Classes to add to the list item containing the account item.

```text
{%
from
"header/macro.njk"
import
header
%}
{{
header
({
logo
: {
href
:
"#"
,
ariaLabel
:
"Manage patients homepage"
},
service
: {
text
:
"Manage patients"
,
href
:
"#"
},
account
: {
items
: [
      {
text
:
"Florence Nightingale"
,
icon
:
true
},
      {
text
:
"Log out"
,
href
:
"#"
}
    ]
  }
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

#### When to use it

Use the logged-in header for services where users have an account. The header can display a "log out" link and other account-related information and links.

#### How to use it

Account information and links can be used with the other header features, for example service name and search. However, keep the number of items in the header to a minimum.

When allowing users to log in to your service, make sure you have a visible service name, so that they know which system they are logging in to.

#### Using account information and links

You can add multiple items to the account information and links section, such as the logged-in user's name and role. Items can be links or just plain text information.

Keep the number of links to a minimum. If you have more than 3 account links, consider combining functions and putting them on a separate page. For example, an account settings page could include actions like change name, change role and reset password. Test with users so you know which combination of items best meets their needs.

If you use a "log out" link, put it last in the list, showing top right on desktop screens and last on small screens. If you put log out and other account actions on a separate page, show the "log out" link last.

#### User information

Consider whether you need to show the user information about the account they have logged in to. This may depend on whether they:

- share a computer

- have multiple accounts or roles

When showing the user their account, you can highlight this with the profile icon (on the icons page ). Only show the icon next to 1 item. Test with users how best to display the user's account information, for example whether to show their full name or their email address.

#### Header with complex account information and links

This example shows account information and multiple links, with a service name and navigation.

- HTML code for header account complex

- Nunjucks code for header account complex

```text
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
"Manage patients homepage"
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
Manage patients
</
span
>
</
a
>
</
div
>
<
nav
class
=
"nhsuk-header__account"
aria-label
=
"Account"
>
<
ul
class
=
"nhsuk-header__account-list"
>
<
li
class
=
"nhsuk-header__account-item"
>
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
Florence Nightingale (Regional Manager)
</
li
>
<
li
class
=
"nhsuk-header__account-item"
>
<
a
class
=
"nhsuk-header__account-link"
href
=
"#"
>
Change role
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
"nhsuk-header__account-item"
>
<
a
class
=
"nhsuk-header__account-link"
href
=
"#"
>
Log out
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
nav
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
Add new patient
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
Find a patient
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the header.
Name logo | Type object | Description Object containing options for the logo. See macro options for logo .
Name service | Type object | Description Object containing options for the service name. See macro options for service .
Name inline | Type boolean | Description If set to true , positions the search box (or account links) inline with the NHS logo.
Name organisation | Type object | Description Settings for header with organisational logo. See macro options for organisation .
Name navigation | Type object | Description Object containing settings for the primary navigation. See macro options for navigation .
Name search | Type object | Description Object containing settings for a search box. See macro options for search .
Name account | Type object | Description Object containing settings for the account section of the header. See macro options for account .
Name container Classes | Type string | Description Classes to add to the header container, useful if you want to make the header fixed width.
Name classes | Type string | Description Classes to add to the header container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the header container.
Name colour | Type string | Description Optional colour modifier for the header. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of the link for the logo. If not set, and a service.href is set, or both are set to same value, then the logo and service name will be combined into a single link.
Name src | Type string | Description The path of the logo image, if you are not using the default NHS logo.
Name alt | Type string | Description The alt text for the logo. Defaults to "NHS" .
Name aria Label | Type string | Description The aria-label for a linked logo. Defaults to "NHS homepage" .

Name | Type | Description
Name text | Type string | Description The text to use for the service name.
Name href | Type string | Description The href of the link for the service name.

Name | Type | Description
Name name | Type string | Description Organisation name.
Name split | Type string | Description Longer organisation names can be split onto multiple lines.
Name descriptor | Type string | Description Organisation descriptor.

Name | Type | Description
Name items | Type array | Description Array of navigation links for use in the header. See macro options for navigation items .
Name aria Label | Type string | Description The aria-label for the primary navigation. Defaults to "Menu" .
Name toggle Menu Text | Type string | Description Text for the toggle menu button. Defaults to "More" .
Name toggle Menu Visually Hidden Text | Type string | Description A visually hidden prefix used before the toggle menu button text. Defaults to "Browse" .
Name classes | Type string | Description Classes to add to the primary navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the primary navigation.
Name justified | Type boolean | Description If set to true , use justified alignment where navigation items appeared evenly spaced out.
Name colour | Type string | Description Optional colour modifier for the primary navigation. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of a navigation item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the navigation item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the navigation item. If html is provided, the text option will be ignored.
Name current | Type boolean | Description Set to true if this links to the current page being shown.
Name active | Type boolean | Description Set to true if the current page is within this section, but the link doesn't necessarily link to the current page
Name classes | Type string | Description Classes to add to the list item containing the link.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the list item containing the link.

Name | Type | Description
Name action | Type string | Description The search form action attribute. Defaults to "https://www.nhs.uk/search" .
Name method | Type string | Description The search form method attribute. Defaults to "get" .
Name name | Type string | Description The name attribute for the search input. Defaults to "q" .
Name placeholder | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.input.placeholder option.
Name visually Hidden Label | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.label.visuallyHiddenText option.
Name visually Hidden Button | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.button.ariaLabel option.
Name label | Type object | Description Optional object allowing customisation of the search input label. See macro options for search label .
Name input | Type object | Description Optional object allowing customisation of the search input. See search input macro options using input component macro .
Name button | Type object | Description Optional object allowing customisation of the search button. See search button macro options using button component macro .
Name classes | Type string | Description Classes to add to the search element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the search element.

Name | Type | Description
Name visually Hidden Text | Type string | Description The visually hidden label text for the search input. Defaults to "Search the NHS website" .

Name | Type | Description
Name placeholder | Type string | Description The placeholder text for the search input. Defaults to "Search" .

Name | Type | Description
Name aria Label | Type string | Description Search button text exposed to assistive technologies, like screen readers, when only an icon is used. Defaults to "Search" .

Name | Type | Description
Name items | Type array | Description Array of account items for use in the header. See macro options for account items .
Name aria Label | Type string | Description The aria-label for the account navigation. Defaults to "Account" .
Name classes | Type string | Description Classes to add to the account navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the account navigation.

Name | Type | Description
Name href | Type string | Description The href of an account item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the account item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the account item. If html is provided, the text option will be ignored.
Name icon | Type boolean | Description Whether to include the account icon for the account item. Defaults to false .
Name action | Type string | Description If set, the item will become a button wrapped in a form with the action given. Useful for log out buttons.
Name method | Type string | Description The value to use for the method of the form if action is set. Defaults to "post" .
Name classes | Type string | Description Classes to add to the list item containing the account item.

```text
{%
from
"header/macro.njk"
import
header
%}
{{
header
({
logo
: {
href
:
"#"
,
ariaLabel
:
"Manage patients homepage"
},
service
: {
text
:
"Manage patients"
,
href
:
"#"
},
account
: {
items
: [
      {
text
:
"Florence Nightingale (Regional Manager)"
,
icon
:
true
},
      {
text
:
"Change role"
,
href
:
"#"
},
      {
text
:
"Log out"
,
href
:
"#"
}
    ]
  },
navigation
: {
items
: [
      {
text
:
"Home"
,
href
:
"#"
},
      {
text
:
"Add new patient"
,
href
:
"#"
},
      {
text
:
"Find a patient"
,
href
:
"#"
}
    ]
  }
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Inline account or search

To keep account links or the search bar inline with the logo and service name on small screens, add the inline: true Nunjucks option. For HTML add the nhsuk-header--inline class to the table.

#### Inline account links

- HTML code for header account inline

- Nunjucks code for header account inline

```text
<
header
class
=
"nhsuk-header nhsuk-header--inline"
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
"Manage patients homepage"
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
Manage patients
</
span
>
</
a
>
</
div
>
<
nav
class
=
"nhsuk-header__account"
aria-label
=
"Account"
>
<
ul
class
=
"nhsuk-header__account-list"
>
<
li
class
=
"nhsuk-header__account-item"
>
<
a
class
=
"nhsuk-header__account-link"
href
=
"#"
>
Log out
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
nav
>
</
div
>
</
header
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the header.
Name logo | Type object | Description Object containing options for the logo. See macro options for logo .
Name service | Type object | Description Object containing options for the service name. See macro options for service .
Name inline | Type boolean | Description If set to true , positions the search box (or account links) inline with the NHS logo.
Name organisation | Type object | Description Settings for header with organisational logo. See macro options for organisation .
Name navigation | Type object | Description Object containing settings for the primary navigation. See macro options for navigation .
Name search | Type object | Description Object containing settings for a search box. See macro options for search .
Name account | Type object | Description Object containing settings for the account section of the header. See macro options for account .
Name container Classes | Type string | Description Classes to add to the header container, useful if you want to make the header fixed width.
Name classes | Type string | Description Classes to add to the header container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the header container.
Name colour | Type string | Description Optional colour modifier for the header. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of the link for the logo. If not set, and a service.href is set, or both are set to same value, then the logo and service name will be combined into a single link.
Name src | Type string | Description The path of the logo image, if you are not using the default NHS logo.
Name alt | Type string | Description The alt text for the logo. Defaults to "NHS" .
Name aria Label | Type string | Description The aria-label for a linked logo. Defaults to "NHS homepage" .

Name | Type | Description
Name text | Type string | Description The text to use for the service name.
Name href | Type string | Description The href of the link for the service name.

Name | Type | Description
Name name | Type string | Description Organisation name.
Name split | Type string | Description Longer organisation names can be split onto multiple lines.
Name descriptor | Type string | Description Organisation descriptor.

Name | Type | Description
Name items | Type array | Description Array of navigation links for use in the header. See macro options for navigation items .
Name aria Label | Type string | Description The aria-label for the primary navigation. Defaults to "Menu" .
Name toggle Menu Text | Type string | Description Text for the toggle menu button. Defaults to "More" .
Name toggle Menu Visually Hidden Text | Type string | Description A visually hidden prefix used before the toggle menu button text. Defaults to "Browse" .
Name classes | Type string | Description Classes to add to the primary navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the primary navigation.
Name justified | Type boolean | Description If set to true , use justified alignment where navigation items appeared evenly spaced out.
Name colour | Type string | Description Optional colour modifier for the primary navigation. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of a navigation item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the navigation item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the navigation item. If html is provided, the text option will be ignored.
Name current | Type boolean | Description Set to true if this links to the current page being shown.
Name active | Type boolean | Description Set to true if the current page is within this section, but the link doesn't necessarily link to the current page
Name classes | Type string | Description Classes to add to the list item containing the link.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the list item containing the link.

Name | Type | Description
Name action | Type string | Description The search form action attribute. Defaults to "https://www.nhs.uk/search" .
Name method | Type string | Description The search form method attribute. Defaults to "get" .
Name name | Type string | Description The name attribute for the search input. Defaults to "q" .
Name placeholder | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.input.placeholder option.
Name visually Hidden Label | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.label.visuallyHiddenText option.
Name visually Hidden Button | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.button.ariaLabel option.
Name label | Type object | Description Optional object allowing customisation of the search input label. See macro options for search label .
Name input | Type object | Description Optional object allowing customisation of the search input. See search input macro options using input component macro .
Name button | Type object | Description Optional object allowing customisation of the search button. See search button macro options using button component macro .
Name classes | Type string | Description Classes to add to the search element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the search element.

Name | Type | Description
Name visually Hidden Text | Type string | Description The visually hidden label text for the search input. Defaults to "Search the NHS website" .

Name | Type | Description
Name placeholder | Type string | Description The placeholder text for the search input. Defaults to "Search" .

Name | Type | Description
Name aria Label | Type string | Description Search button text exposed to assistive technologies, like screen readers, when only an icon is used. Defaults to "Search" .

Name | Type | Description
Name items | Type array | Description Array of account items for use in the header. See macro options for account items .
Name aria Label | Type string | Description The aria-label for the account navigation. Defaults to "Account" .
Name classes | Type string | Description Classes to add to the account navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the account navigation.

Name | Type | Description
Name href | Type string | Description The href of an account item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the account item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the account item. If html is provided, the text option will be ignored.
Name icon | Type boolean | Description Whether to include the account icon for the account item. Defaults to false .
Name action | Type string | Description If set, the item will become a button wrapped in a form with the action given. Useful for log out buttons.
Name method | Type string | Description The value to use for the method of the form if action is set. Defaults to "post" .
Name classes | Type string | Description Classes to add to the list item containing the account item.

```text
{%
from
"header/macro.njk"
import
header
%}
{{
header
({
inline
:
true
,
logo
: {
href
:
"#"
,
ariaLabel
:
"Manage patients homepage"
},
service
: {
text
:
"Manage patients"
,
href
:
"#"
},
account
: {
items
: [
      {
text
:
"Log out"
,
href
:
"#"
}
    ]
  }
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

#### Inline search

- HTML code for header search inline

- Nunjucks code for header search inline

```text
<
header
class
=
"nhsuk-header nhsuk-header--inline"
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
<
search
class
=
"nhsuk-header__search"
>
<
form
class
=
"nhsuk-header__search-form"
id
=
"search"
action
=
"https://www.nhs.uk/search/"
method
=
"get"
novalidate
>
<
div
class
=
"nhsuk-form-group"
>
<
label
class
=
"nhsuk-label nhsuk-u-visually-hidden"
for
=
"search-field"
>
Search the NHS website
</
label
>
<
div
class
=
"nhsuk-input-wrapper"
>
<
input
class
=
"nhsuk-input"
id
=
"search-field"
name
=
"q"
type
=
"search"
autocomplete
=
"off"
placeholder
=
"Search"
>
<
button
class
=
"nhsuk-button nhsuk-button--icon nhsuk-button--small"
data-module
=
"nhsuk-button"
type
=
"submit"
aria-label
=
"Search"
>
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
aria-hidden
=
"true"
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
</
button
>
</
div
>
</
div
>
</
form
>
</
search
>
</
div
>
</
header
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the header.
Name logo | Type object | Description Object containing options for the logo. See macro options for logo .
Name service | Type object | Description Object containing options for the service name. See macro options for service .
Name inline | Type boolean | Description If set to true , positions the search box (or account links) inline with the NHS logo.
Name organisation | Type object | Description Settings for header with organisational logo. See macro options for organisation .
Name navigation | Type object | Description Object containing settings for the primary navigation. See macro options for navigation .
Name search | Type object | Description Object containing settings for a search box. See macro options for search .
Name account | Type object | Description Object containing settings for the account section of the header. See macro options for account .
Name container Classes | Type string | Description Classes to add to the header container, useful if you want to make the header fixed width.
Name classes | Type string | Description Classes to add to the header container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the header container.
Name colour | Type string | Description Optional colour modifier for the header. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of the link for the logo. If not set, and a service.href is set, or both are set to same value, then the logo and service name will be combined into a single link.
Name src | Type string | Description The path of the logo image, if you are not using the default NHS logo.
Name alt | Type string | Description The alt text for the logo. Defaults to "NHS" .
Name aria Label | Type string | Description The aria-label for a linked logo. Defaults to "NHS homepage" .

Name | Type | Description
Name text | Type string | Description The text to use for the service name.
Name href | Type string | Description The href of the link for the service name.

Name | Type | Description
Name name | Type string | Description Organisation name.
Name split | Type string | Description Longer organisation names can be split onto multiple lines.
Name descriptor | Type string | Description Organisation descriptor.

Name | Type | Description
Name items | Type array | Description Array of navigation links for use in the header. See macro options for navigation items .
Name aria Label | Type string | Description The aria-label for the primary navigation. Defaults to "Menu" .
Name toggle Menu Text | Type string | Description Text for the toggle menu button. Defaults to "More" .
Name toggle Menu Visually Hidden Text | Type string | Description A visually hidden prefix used before the toggle menu button text. Defaults to "Browse" .
Name classes | Type string | Description Classes to add to the primary navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the primary navigation.
Name justified | Type boolean | Description If set to true , use justified alignment where navigation items appeared evenly spaced out.
Name colour | Type string | Description Optional colour modifier for the primary navigation. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of a navigation item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the navigation item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the navigation item. If html is provided, the text option will be ignored.
Name current | Type boolean | Description Set to true if this links to the current page being shown.
Name active | Type boolean | Description Set to true if the current page is within this section, but the link doesn't necessarily link to the current page
Name classes | Type string | Description Classes to add to the list item containing the link.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the list item containing the link.

Name | Type | Description
Name action | Type string | Description The search form action attribute. Defaults to "https://www.nhs.uk/search" .
Name method | Type string | Description The search form method attribute. Defaults to "get" .
Name name | Type string | Description The name attribute for the search input. Defaults to "q" .
Name placeholder | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.input.placeholder option.
Name visually Hidden Label | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.label.visuallyHiddenText option.
Name visually Hidden Button | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.button.ariaLabel option.
Name label | Type object | Description Optional object allowing customisation of the search input label. See macro options for search label .
Name input | Type object | Description Optional object allowing customisation of the search input. See search input macro options using input component macro .
Name button | Type object | Description Optional object allowing customisation of the search button. See search button macro options using button component macro .
Name classes | Type string | Description Classes to add to the search element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the search element.

Name | Type | Description
Name visually Hidden Text | Type string | Description The visually hidden label text for the search input. Defaults to "Search the NHS website" .

Name | Type | Description
Name placeholder | Type string | Description The placeholder text for the search input. Defaults to "Search" .

Name | Type | Description
Name aria Label | Type string | Description Search button text exposed to assistive technologies, like screen readers, when only an icon is used. Defaults to "Search" .

Name | Type | Description
Name items | Type array | Description Array of account items for use in the header. See macro options for account items .
Name aria Label | Type string | Description The aria-label for the account navigation. Defaults to "Account" .
Name classes | Type string | Description Classes to add to the account navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the account navigation.

Name | Type | Description
Name href | Type string | Description The href of an account item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the account item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the account item. If html is provided, the text option will be ignored.
Name icon | Type boolean | Description Whether to include the account icon for the account item. Defaults to false .
Name action | Type string | Description If set, the item will become a button wrapped in a form with the action given. Useful for log out buttons.
Name method | Type string | Description The value to use for the method of the form if action is set. Defaults to "post" .
Name classes | Type string | Description Classes to add to the list item containing the account item.

```text
{%
from
"header/macro.njk"
import
header
%}
{{
header
({
inline
:
true
,
search
: {
input
: {
placeholder
:
"Search"
},
label
: {
visuallyHiddenText
:
"Search the NHS website"
}
  }
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## Organisational header

Use the organisational header if your organisation or service is a regional or local NHS service, such as an NHS trust.

All NHS websites need to have an nhs.uk domain. See Network addressing (NHS England) .

There are 3 variants of the organisational header:

- blue header

- white header

- white header with blue navigation

### Blue header

- HTML code for header organisational

- Nunjucks code for header organisational

```text
<
header
class
=
"nhsuk-header nhsuk-header--organisation"
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
"NHS Anytown Anyplace Anywhere NHS Foundation Trust homepage"
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
"nhsuk-header__organisation-name"
>
Anytown Anyplace
<
span
class
=
"nhsuk-header__organisation-name-split"
>
Anywhere
</
span
>
</
span
>
<
span
class
=
"nhsuk-header__organisation-name-descriptor"
>
NHS Foundation Trust
</
span
>
</
a
>
</
div
>
<
search
class
=
"nhsuk-header__search"
>
<
form
class
=
"nhsuk-header__search-form"
id
=
"search"
action
=
"https://www.nhs.uk/search/"
method
=
"get"
novalidate
>
<
div
class
=
"nhsuk-form-group"
>
<
label
class
=
"nhsuk-label nhsuk-u-visually-hidden"
for
=
"search-field"
>
Search the Anytown Anyplace Anywhere website
</
label
>
<
div
class
=
"nhsuk-input-wrapper"
>
<
input
class
=
"nhsuk-input"
id
=
"search-field"
name
=
"q"
type
=
"search"
autocomplete
=
"off"
placeholder
=
"Search"
>
<
button
class
=
"nhsuk-button nhsuk-button--icon nhsuk-button--small"
data-module
=
"nhsuk-button"
type
=
"submit"
aria-label
=
"Search"
>
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
aria-hidden
=
"true"
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
</
button
>
</
div
>
</
div
>
</
form
>
</
search
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
Your hospital visit
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
"nhsuk-header__navigation-item nhsuk-header__navigation-item--current"
>
<
a
class
=
"nhsuk-header__navigation-link"
href
=
"#"
aria-current
=
"true"
>
<
strong
class
=
"nhsuk-header__navigation-item-current-fallback"
>
Wards and departments
</
strong
>
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
Conditions and treatments
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
Our people
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
Our research
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the header.
Name logo | Type object | Description Object containing options for the logo. See macro options for logo .
Name service | Type object | Description Object containing options for the service name. See macro options for service .
Name inline | Type boolean | Description If set to true , positions the search box (or account links) inline with the NHS logo.
Name organisation | Type object | Description Settings for header with organisational logo. See macro options for organisation .
Name navigation | Type object | Description Object containing settings for the primary navigation. See macro options for navigation .
Name search | Type object | Description Object containing settings for a search box. See macro options for search .
Name account | Type object | Description Object containing settings for the account section of the header. See macro options for account .
Name container Classes | Type string | Description Classes to add to the header container, useful if you want to make the header fixed width.
Name classes | Type string | Description Classes to add to the header container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the header container.
Name colour | Type string | Description Optional colour modifier for the header. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of the link for the logo. If not set, and a service.href is set, or both are set to same value, then the logo and service name will be combined into a single link.
Name src | Type string | Description The path of the logo image, if you are not using the default NHS logo.
Name alt | Type string | Description The alt text for the logo. Defaults to "NHS" .
Name aria Label | Type string | Description The aria-label for a linked logo. Defaults to "NHS homepage" .

Name | Type | Description
Name text | Type string | Description The text to use for the service name.
Name href | Type string | Description The href of the link for the service name.

Name | Type | Description
Name name | Type string | Description Organisation name.
Name split | Type string | Description Longer organisation names can be split onto multiple lines.
Name descriptor | Type string | Description Organisation descriptor.

Name | Type | Description
Name items | Type array | Description Array of navigation links for use in the header. See macro options for navigation items .
Name aria Label | Type string | Description The aria-label for the primary navigation. Defaults to "Menu" .
Name toggle Menu Text | Type string | Description Text for the toggle menu button. Defaults to "More" .
Name toggle Menu Visually Hidden Text | Type string | Description A visually hidden prefix used before the toggle menu button text. Defaults to "Browse" .
Name classes | Type string | Description Classes to add to the primary navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the primary navigation.
Name justified | Type boolean | Description If set to true , use justified alignment where navigation items appeared evenly spaced out.
Name colour | Type string | Description Optional colour modifier for the primary navigation. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of a navigation item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the navigation item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the navigation item. If html is provided, the text option will be ignored.
Name current | Type boolean | Description Set to true if this links to the current page being shown.
Name active | Type boolean | Description Set to true if the current page is within this section, but the link doesn't necessarily link to the current page
Name classes | Type string | Description Classes to add to the list item containing the link.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the list item containing the link.

Name | Type | Description
Name action | Type string | Description The search form action attribute. Defaults to "https://www.nhs.uk/search" .
Name method | Type string | Description The search form method attribute. Defaults to "get" .
Name name | Type string | Description The name attribute for the search input. Defaults to "q" .
Name placeholder | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.input.placeholder option.
Name visually Hidden Label | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.label.visuallyHiddenText option.
Name visually Hidden Button | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.button.ariaLabel option.
Name label | Type object | Description Optional object allowing customisation of the search input label. See macro options for search label .
Name input | Type object | Description Optional object allowing customisation of the search input. See search input macro options using input component macro .
Name button | Type object | Description Optional object allowing customisation of the search button. See search button macro options using button component macro .
Name classes | Type string | Description Classes to add to the search element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the search element.

Name | Type | Description
Name visually Hidden Text | Type string | Description The visually hidden label text for the search input. Defaults to "Search the NHS website" .

Name | Type | Description
Name placeholder | Type string | Description The placeholder text for the search input. Defaults to "Search" .

Name | Type | Description
Name aria Label | Type string | Description Search button text exposed to assistive technologies, like screen readers, when only an icon is used. Defaults to "Search" .

Name | Type | Description
Name items | Type array | Description Array of account items for use in the header. See macro options for account items .
Name aria Label | Type string | Description The aria-label for the account navigation. Defaults to "Account" .
Name classes | Type string | Description Classes to add to the account navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the account navigation.

Name | Type | Description
Name href | Type string | Description The href of an account item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the account item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the account item. If html is provided, the text option will be ignored.
Name icon | Type boolean | Description Whether to include the account icon for the account item. Defaults to false .
Name action | Type string | Description If set, the item will become a button wrapped in a form with the action given. Useful for log out buttons.
Name method | Type string | Description The value to use for the method of the form if action is set. Defaults to "post" .
Name classes | Type string | Description Classes to add to the list item containing the account item.

```text
{%
from
"header/macro.njk"
import
header
%}
{{
header
({
logo
: {
href
:
"#"
,
ariaLabel
:
"NHS Anytown Anyplace Anywhere NHS Foundation Trust homepage"
},
organisation
: {
name
:
"Anytown Anyplace"
,
split
:
"Anywhere"
,
descriptor
:
"NHS Foundation Trust"
},
search
: {
label
: {
visuallyHiddenText
:
"Search the Anytown Anyplace Anywhere website"
}
  },
navigation
: {
items
: [
      {
text
:
"Your hospital visit"
,
href
:
"#"
},
      {
text
:
"Wards and departments"
,
href
:
"#"
,
active
:
true
},
      {
text
:
"Conditions and treatments"
,
href
:
"#"
},
      {
text
:
"Our people"
,
href
:
"#"
},
      {
text
:
"Our research"
,
href
:
"#"
}
    ]
  }
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### White header

- HTML code for header organisational white

- Nunjucks code for header organisational white

```text
<
header
class
=
"nhsuk-header nhsuk-header--white nhsuk-header--organisation"
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
"NHS Anytown Anyplace Anywhere NHS Foundation Trust homepage"
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
"nhsuk-header__organisation-name"
>
Anytown Anyplace
<
span
class
=
"nhsuk-header__organisation-name-split"
>
Anywhere
</
span
>
</
span
>
<
span
class
=
"nhsuk-header__organisation-name-descriptor"
>
NHS Foundation Trust
</
span
>
</
a
>
</
div
>
<
search
class
=
"nhsuk-header__search"
>
<
form
class
=
"nhsuk-header__search-form"
id
=
"search"
action
=
"https://www.nhs.uk/search/"
method
=
"get"
novalidate
>
<
div
class
=
"nhsuk-form-group"
>
<
label
class
=
"nhsuk-label nhsuk-u-visually-hidden"
for
=
"search-field"
>
Search the Anytown Anyplace Anywhere website
</
label
>
<
div
class
=
"nhsuk-input-wrapper"
>
<
input
class
=
"nhsuk-input"
id
=
"search-field"
name
=
"q"
type
=
"search"
autocomplete
=
"off"
placeholder
=
"Search"
>
<
button
class
=
"nhsuk-button nhsuk-button--icon nhsuk-button--small"
data-module
=
"nhsuk-button"
type
=
"submit"
aria-label
=
"Search"
>
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
aria-hidden
=
"true"
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
</
button
>
</
div
>
</
div
>
</
form
>
</
search
>
</
div
>
<
nav
class
=
"nhsuk-header__navigation nhsuk-header__navigation--white"
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
Your hospital visit
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
"nhsuk-header__navigation-item nhsuk-header__navigation-item--current"
>
<
a
class
=
"nhsuk-header__navigation-link"
href
=
"#"
aria-current
=
"true"
>
<
strong
class
=
"nhsuk-header__navigation-item-current-fallback"
>
Wards and departments
</
strong
>
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
Conditions and treatments
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
Our people
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
Our research
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the header.
Name logo | Type object | Description Object containing options for the logo. See macro options for logo .
Name service | Type object | Description Object containing options for the service name. See macro options for service .
Name inline | Type boolean | Description If set to true , positions the search box (or account links) inline with the NHS logo.
Name organisation | Type object | Description Settings for header with organisational logo. See macro options for organisation .
Name navigation | Type object | Description Object containing settings for the primary navigation. See macro options for navigation .
Name search | Type object | Description Object containing settings for a search box. See macro options for search .
Name account | Type object | Description Object containing settings for the account section of the header. See macro options for account .
Name container Classes | Type string | Description Classes to add to the header container, useful if you want to make the header fixed width.
Name classes | Type string | Description Classes to add to the header container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the header container.
Name colour | Type string | Description Optional colour modifier for the header. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of the link for the logo. If not set, and a service.href is set, or both are set to same value, then the logo and service name will be combined into a single link.
Name src | Type string | Description The path of the logo image, if you are not using the default NHS logo.
Name alt | Type string | Description The alt text for the logo. Defaults to "NHS" .
Name aria Label | Type string | Description The aria-label for a linked logo. Defaults to "NHS homepage" .

Name | Type | Description
Name text | Type string | Description The text to use for the service name.
Name href | Type string | Description The href of the link for the service name.

Name | Type | Description
Name name | Type string | Description Organisation name.
Name split | Type string | Description Longer organisation names can be split onto multiple lines.
Name descriptor | Type string | Description Organisation descriptor.

Name | Type | Description
Name items | Type array | Description Array of navigation links for use in the header. See macro options for navigation items .
Name aria Label | Type string | Description The aria-label for the primary navigation. Defaults to "Menu" .
Name toggle Menu Text | Type string | Description Text for the toggle menu button. Defaults to "More" .
Name toggle Menu Visually Hidden Text | Type string | Description A visually hidden prefix used before the toggle menu button text. Defaults to "Browse" .
Name classes | Type string | Description Classes to add to the primary navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the primary navigation.
Name justified | Type boolean | Description If set to true , use justified alignment where navigation items appeared evenly spaced out.
Name colour | Type string | Description Optional colour modifier for the primary navigation. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of a navigation item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the navigation item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the navigation item. If html is provided, the text option will be ignored.
Name current | Type boolean | Description Set to true if this links to the current page being shown.
Name active | Type boolean | Description Set to true if the current page is within this section, but the link doesn't necessarily link to the current page
Name classes | Type string | Description Classes to add to the list item containing the link.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the list item containing the link.

Name | Type | Description
Name action | Type string | Description The search form action attribute. Defaults to "https://www.nhs.uk/search" .
Name method | Type string | Description The search form method attribute. Defaults to "get" .
Name name | Type string | Description The name attribute for the search input. Defaults to "q" .
Name placeholder | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.input.placeholder option.
Name visually Hidden Label | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.label.visuallyHiddenText option.
Name visually Hidden Button | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.button.ariaLabel option.
Name label | Type object | Description Optional object allowing customisation of the search input label. See macro options for search label .
Name input | Type object | Description Optional object allowing customisation of the search input. See search input macro options using input component macro .
Name button | Type object | Description Optional object allowing customisation of the search button. See search button macro options using button component macro .
Name classes | Type string | Description Classes to add to the search element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the search element.

Name | Type | Description
Name visually Hidden Text | Type string | Description The visually hidden label text for the search input. Defaults to "Search the NHS website" .

Name | Type | Description
Name placeholder | Type string | Description The placeholder text for the search input. Defaults to "Search" .

Name | Type | Description
Name aria Label | Type string | Description Search button text exposed to assistive technologies, like screen readers, when only an icon is used. Defaults to "Search" .

Name | Type | Description
Name items | Type array | Description Array of account items for use in the header. See macro options for account items .
Name aria Label | Type string | Description The aria-label for the account navigation. Defaults to "Account" .
Name classes | Type string | Description Classes to add to the account navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the account navigation.

Name | Type | Description
Name href | Type string | Description The href of an account item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the account item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the account item. If html is provided, the text option will be ignored.
Name icon | Type boolean | Description Whether to include the account icon for the account item. Defaults to false .
Name action | Type string | Description If set, the item will become a button wrapped in a form with the action given. Useful for log out buttons.
Name method | Type string | Description The value to use for the method of the form if action is set. Defaults to "post" .
Name classes | Type string | Description Classes to add to the list item containing the account item.

```text
{%
from
"header/macro.njk"
import
header
%}
{{
header
({
colour
:
"white"
,
logo
: {
href
:
"#"
,
ariaLabel
:
"NHS Anytown Anyplace Anywhere NHS Foundation Trust homepage"
},
organisation
: {
name
:
"Anytown Anyplace"
,
split
:
"Anywhere"
,
descriptor
:
"NHS Foundation Trust"
},
search
: {
label
: {
visuallyHiddenText
:
"Search the Anytown Anyplace Anywhere website"
}
  },
navigation
: {
colour
:
"white"
,
items
: [
      {
text
:
"Your hospital visit"
,
href
:
"#"
},
      {
text
:
"Wards and departments"
,
href
:
"#"
,
active
:
true
},
      {
text
:
"Conditions and treatments"
,
href
:
"#"
},
      {
text
:
"Our people"
,
href
:
"#"
},
      {
text
:
"Our research"
,
href
:
"#"
}
    ]
  }
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### White header with blue navigation

- HTML code for header organisational white with blue navigation

- Nunjucks code for header organisational white with blue navigation

```text
<
header
class
=
"nhsuk-header nhsuk-header--white nhsuk-header--organisation"
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
"NHS Anytown Anyplace Anywhere NHS Foundation Trust homepage"
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
"nhsuk-header__organisation-name"
>
Anytown Anyplace
<
span
class
=
"nhsuk-header__organisation-name-split"
>
Anywhere
</
span
>
</
span
>
<
span
class
=
"nhsuk-header__organisation-name-descriptor"
>
NHS Foundation Trust
</
span
>
</
a
>
</
div
>
<
search
class
=
"nhsuk-header__search"
>
<
form
class
=
"nhsuk-header__search-form"
id
=
"search"
action
=
"https://www.nhs.uk/search/"
method
=
"get"
novalidate
>
<
div
class
=
"nhsuk-form-group"
>
<
label
class
=
"nhsuk-label nhsuk-u-visually-hidden"
for
=
"search-field"
>
Search the Anytown Anyplace Anywhere website
</
label
>
<
div
class
=
"nhsuk-input-wrapper"
>
<
input
class
=
"nhsuk-input"
id
=
"search-field"
name
=
"q"
type
=
"search"
autocomplete
=
"off"
placeholder
=
"Search"
>
<
button
class
=
"nhsuk-button nhsuk-button--icon nhsuk-button--small"
data-module
=
"nhsuk-button"
type
=
"submit"
aria-label
=
"Search"
>
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
aria-hidden
=
"true"
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
</
button
>
</
div
>
</
div
>
</
form
>
</
search
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
Your hospital visit
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
"nhsuk-header__navigation-item nhsuk-header__navigation-item--current"
>
<
a
class
=
"nhsuk-header__navigation-link"
href
=
"#"
aria-current
=
"true"
>
<
strong
class
=
"nhsuk-header__navigation-item-current-fallback"
>
Wards and departments
</
strong
>
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
Conditions and treatments
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
Our people
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
Our research
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
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the header.
Name logo | Type object | Description Object containing options for the logo. See macro options for logo .
Name service | Type object | Description Object containing options for the service name. See macro options for service .
Name inline | Type boolean | Description If set to true , positions the search box (or account links) inline with the NHS logo.
Name organisation | Type object | Description Settings for header with organisational logo. See macro options for organisation .
Name navigation | Type object | Description Object containing settings for the primary navigation. See macro options for navigation .
Name search | Type object | Description Object containing settings for a search box. See macro options for search .
Name account | Type object | Description Object containing settings for the account section of the header. See macro options for account .
Name container Classes | Type string | Description Classes to add to the header container, useful if you want to make the header fixed width.
Name classes | Type string | Description Classes to add to the header container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the header container.
Name colour | Type string | Description Optional colour modifier for the header. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of the link for the logo. If not set, and a service.href is set, or both are set to same value, then the logo and service name will be combined into a single link.
Name src | Type string | Description The path of the logo image, if you are not using the default NHS logo.
Name alt | Type string | Description The alt text for the logo. Defaults to "NHS" .
Name aria Label | Type string | Description The aria-label for a linked logo. Defaults to "NHS homepage" .

Name | Type | Description
Name text | Type string | Description The text to use for the service name.
Name href | Type string | Description The href of the link for the service name.

Name | Type | Description
Name name | Type string | Description Organisation name.
Name split | Type string | Description Longer organisation names can be split onto multiple lines.
Name descriptor | Type string | Description Organisation descriptor.

Name | Type | Description
Name items | Type array | Description Array of navigation links for use in the header. See macro options for navigation items .
Name aria Label | Type string | Description The aria-label for the primary navigation. Defaults to "Menu" .
Name toggle Menu Text | Type string | Description Text for the toggle menu button. Defaults to "More" .
Name toggle Menu Visually Hidden Text | Type string | Description A visually hidden prefix used before the toggle menu button text. Defaults to "Browse" .
Name classes | Type string | Description Classes to add to the primary navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the primary navigation.
Name justified | Type boolean | Description If set to true , use justified alignment where navigation items appeared evenly spaced out.
Name colour | Type string | Description Optional colour modifier for the primary navigation. You can use only "white" or empty values with this option.

Name | Type | Description
Name href | Type string | Description The href of a navigation item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the navigation item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the navigation item. If html is provided, the text option will be ignored.
Name current | Type boolean | Description Set to true if this links to the current page being shown.
Name active | Type boolean | Description Set to true if the current page is within this section, but the link doesn't necessarily link to the current page
Name classes | Type string | Description Classes to add to the list item containing the link.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the list item containing the link.

Name | Type | Description
Name action | Type string | Description The search form action attribute. Defaults to "https://www.nhs.uk/search" .
Name method | Type string | Description The search form method attribute. Defaults to "get" .
Name name | Type string | Description The name attribute for the search input. Defaults to "q" .
Name placeholder | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.input.placeholder option.
Name visually Hidden Label | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.label.visuallyHiddenText option.
Name visually Hidden Button | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the search.button.ariaLabel option.
Name label | Type object | Description Optional object allowing customisation of the search input label. See macro options for search label .
Name input | Type object | Description Optional object allowing customisation of the search input. See search input macro options using input component macro .
Name button | Type object | Description Optional object allowing customisation of the search button. See search button macro options using button component macro .
Name classes | Type string | Description Classes to add to the search element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the search element.

Name | Type | Description
Name visually Hidden Text | Type string | Description The visually hidden label text for the search input. Defaults to "Search the NHS website" .

Name | Type | Description
Name placeholder | Type string | Description The placeholder text for the search input. Defaults to "Search" .

Name | Type | Description
Name aria Label | Type string | Description Search button text exposed to assistive technologies, like screen readers, when only an icon is used. Defaults to "Search" .

Name | Type | Description
Name items | Type array | Description Array of account items for use in the header. See macro options for account items .
Name aria Label | Type string | Description The aria-label for the account navigation. Defaults to "Account" .
Name classes | Type string | Description Classes to add to the account navigation.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the account navigation.

Name | Type | Description
Name href | Type string | Description The href of an account item in the header.
Name text | Type string | Description Required. If html is set, this is not required. Text for the account item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the account item. If html is provided, the text option will be ignored.
Name icon | Type boolean | Description Whether to include the account icon for the account item. Defaults to false .
Name action | Type string | Description If set, the item will become a button wrapped in a form with the action given. Useful for log out buttons.
Name method | Type string | Description The value to use for the method of the form if action is set. Defaults to "post" .
Name classes | Type string | Description Classes to add to the list item containing the account item.

```text
{%
from
"header/macro.njk"
import
header
%}
{{
header
({
colour
:
"white"
,
logo
: {
href
:
"#"
,
ariaLabel
:
"NHS Anytown Anyplace Anywhere NHS Foundation Trust homepage"
},
organisation
: {
name
:
"Anytown Anyplace"
,
split
:
"Anywhere"
,
descriptor
:
"NHS Foundation Trust"
},
search
: {
label
: {
visuallyHiddenText
:
"Search the Anytown Anyplace Anywhere website"
}
  },
navigation
: {
items
: [
      {
text
:
"Your hospital visit"
,
href
:
"#"
},
      {
text
:
"Wards and departments"
,
href
:
"#"
,
active
:
true
},
      {
text
:
"Conditions and treatments"
,
href
:
"#"
},
      {
text
:
"Our people"
,
href
:
"#"
},
      {
text
:
"Our research"
,
href
:
"#"
}
    ]
  }
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

You must have a Frutiger font licence to use an NHS organisational logo. Find out about using the Frutiger font , including registering for a free licence.

### Organisational logos

Read more about creating NHS organisational logos in the NHS England identity guidelines .

The organisational logo is an SVG (scalable vector graphic) and you can change the organisation name and descriptor in the code. Longer organisation names should be split onto 2 lines.

You can also use a static asset, such as a PNG file.

```text
<
a
class
=
"nhsuk-header__service-logo"
href
=
"/"
>
<
img
class
=
"nhsuk-header__organisation-logo"
src
=
"/assets/logo.png"
width
=
"280"
alt
=
"Anyplace Anytown Anywhere NHS Foundation Trust homepage"
>
</
a
>
```

## Progressive enhancement

The header component uses progressive enhancement and requires JavaScript for enhanced functionality.

When JavaScript is not available, users will not see the drop-down "More" button. Navigation links will be wrapped onto multiple lines.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
