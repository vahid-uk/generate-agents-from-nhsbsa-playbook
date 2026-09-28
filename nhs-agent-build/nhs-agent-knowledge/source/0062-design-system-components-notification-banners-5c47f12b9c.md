# Notification banners – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/notification-banners/

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

# Content presentation – Notification banners

Use a notification banner to tell the user something they need to know that's not directly related to the page content.

- HTML code for notification banners

- Nunjucks code for notification banners

```text
<
div
class
=
"nhsuk-notification-banner"
data-module
=
"nhsuk-notification-banner"
role
=
"region"
aria-labelledby
=
"nhsuk-notification-banner-title"
>
<
div
class
=
"nhsuk-notification-banner__header"
>
<
h2
class
=
"nhsuk-notification-banner__title"
id
=
"nhsuk-notification-banner-title"
>
Important
</
h2
>
</
div
>
<
div
class
=
"nhsuk-notification-banner__content"
>
<
p
class
=
"nhsuk-notification-banner__heading"
>
<
p
class
=
"nhsuk-notification-banner__heading"
>
You have 7 days left to send your application.
<
a
class
=
"nhsuk-notification-banner__link"
href
=
"#"
>
View application
</
a
>
.
</
p
>
</
p
>
</
div
>
</
div
>
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the notification banner.
Name title | Type object | Description The title that displays in the notification banner: if you do not set variant , title.text defaults to "Important" if you set variant to "success" , title.text defaults to "Success" if you set title.text or title.html , the defaults are ignored See macro options for title .
Name title Id | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the title.id option.
Name title Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the title.text option.
Name title Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the title.html option.
Name title Heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the title.level option.
Name heading | Type object | Description Heading to be used within the notification banner. See macro options for heading .
Name text | Type string | Description Required. The text that displays in the notification banner. You can use any string with this option. If you set html , this option is not required and is ignored.
Name html | Type string | Description Required. The HTML to use within the notification banner. You can use any string with this option. If you set html , text is not required and is ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire notification banner component in a call block.
Name variant | Type string | Description Optional variant of notification banner. You can use only "success" or empty values with this option. If you set variant to "success" , the notification banner sets role to "alert" . JavaScript then moves the keyboard focus to the notification banner when the page loads. If you do not set variant , the notification banner sets role to "region" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option.
Name role | Type string | Description Overrides the value of the role attribute for the notification banner. Defaults to "region" . If you set variant to "success" , role defaults to "alert" .
Name disable Auto Focus | Type boolean | Description If you set variant to "success" , or role to "alert" , JavaScript moves the keyboard focus to the notification banner when the page loads. To disable this behaviour, set disableAutoFocus to true .
Name classes | Type string | Description The classes that you want to add to the notification banner.
Name attributes | Type object | Description The HTML attributes that you want to add to the notification banner, for example, data attributes.

- if you do not set variant , title.text defaults to "Important"

- if you set variant to "success" , title.text defaults to "Success"

- if you set title.text or title.html , the defaults are ignored

Name | Type | Description
Name id | Type string | Description The ID of the title.
Name text | Type string | Description Required. If html is set, this is not required. Text for the title. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the title. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the title.
Name heading Level | Type integer | Description Optional alias for the title heading level option.
Name level | Type integer | Description Optional heading level for the title. Defaults to 2 .
Name classes | Type string | Description Classes to add to the title.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the title.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the heading.
Name href | Type string | Description If set, the heading will become a link.
Name caption | Type object | Description Optional caption for the heading. See macro options for caption .
Name level | Type integer | Description Optional heading level for the heading. Defaults to 3 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.
Name element | Type string | Description HTML element for the heading – for example, "p" . Defaults to the level option prefixed with "h" .

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
"notification-banner/macro.njk"
import
notificationBanner
%}
{%
set
html
%}
<
p
class
=
"nhsuk-notification-banner__heading"
>
You have 7 days left to send your application.
<
a
class
=
"nhsuk-notification-banner__link"
href
=
"#"
>
View application
</
a
>
.
</
p
>
{%
endset
%}
{{
notificationBanner
({
heading
: {
html
: html,
element
:
"p"
}
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

## When to use this component

A notification banner lets you tell the user about something that's not directly relevant to the thing they're trying to do on that page of the service.

There are 2 versions of the notification banner:

- the information banner (blue)

- the success banner (green)

Use the information banner to tell the user about:

- something that affects the service as a whole (such as delays in processing applications or planned downtime)

- something that affects them in particular (for example, an approaching deadline they need to meet)

Use the success banner to tell the user that something they've just done on a previous page was successful (for example, confirming that an email has been sent).

## When not to use this component

Use notification banners sparingly. There's evidence that people often miss banners. Using them too often is likely to make this problem worse. See Banner blindness revisited by Nielsen Norman Group .

Avoid showing more than 1 notification banner on the same page. Instead, combine the messages in a single notification banner. If the messages are too different to combine, decide which is your highest priority message and show that one.

If the information is directly relevant to the thing the user is doing on that page, put the information in the main page content instead. If it needs to stand out, use:

- inset text component

- warning callout

Do not use a notification banner to tell the user about validation errors. Use an error message component and error summary component instead.

Do not show a notification banner and an error summary component on the same page. Just show the error summary.

## How it works

Put the notification banner at top of the main container. If your page includes breadcrumbs or a back link, place it below these but before the h1 .

The notification banner should be the same width as the page's other content, such as components, headings and body text. For example, if the other content takes up two-thirds of the screen on desktop devices, then the notification banner should also take up two-thirds. Read about page layout .

Use role="region" and aria-labelledby="nhsuk-notification-banners-title" (with id="nhsuk-notification-banners-title" on <nhsuk-notification-banners__title> ) so that screen reader users can navigate to the notification banner.

### Notification banner headings

The notification banner starts with a heading like "Important" or "Success". This is usually an <h2> .

If you need a heading in the banner content, place it in <div class="nhsuk-notification-banner__content"> . It will normally be an <h3> .

Do not use a heading for single line notifications. You can apply the nhsuk-notification-banners__heading class to a paragraph to make it stand out.

## Using the information banner

Use an information banner to tell users about something that affects the service as a whole.

For example:

- in a service that lets the user apply for something, they might need to know that it's taking longer than usual to process applications

- in an account-type service, the user might need to know that the service will be down for scheduled maintenance

- HTML code for notification banners whole service

- Nunjucks code for notification banners whole service

```text
<
div
class
=
"nhsuk-notification-banner"
data-module
=
"nhsuk-notification-banner"
role
=
"region"
aria-labelledby
=
"nhsuk-notification-banner-title"
>
<
div
class
=
"nhsuk-notification-banner__header"
>
<
h2
class
=
"nhsuk-notification-banner__title"
id
=
"nhsuk-notification-banner-title"
>
Important
</
h2
>
</
div
>
<
div
class
=
"nhsuk-notification-banner__content"
>
<
p
class
=
"nhsuk-notification-banner__heading"
>
The service will be unavailable from 8pm to 9pm on Thursday 1 January 2025.
</
p
>
</
div
>
</
div
>
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the notification banner.
Name title | Type object | Description The title that displays in the notification banner: if you do not set variant , title.text defaults to "Important" if you set variant to "success" , title.text defaults to "Success" if you set title.text or title.html , the defaults are ignored See macro options for title .
Name title Id | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the title.id option.
Name title Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the title.text option.
Name title Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the title.html option.
Name title Heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the title.level option.
Name heading | Type object | Description Heading to be used within the notification banner. See macro options for heading .
Name text | Type string | Description Required. The text that displays in the notification banner. You can use any string with this option. If you set html , this option is not required and is ignored.
Name html | Type string | Description Required. The HTML to use within the notification banner. You can use any string with this option. If you set html , text is not required and is ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire notification banner component in a call block.
Name variant | Type string | Description Optional variant of notification banner. You can use only "success" or empty values with this option. If you set variant to "success" , the notification banner sets role to "alert" . JavaScript then moves the keyboard focus to the notification banner when the page loads. If you do not set variant , the notification banner sets role to "region" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option.
Name role | Type string | Description Overrides the value of the role attribute for the notification banner. Defaults to "region" . If you set variant to "success" , role defaults to "alert" .
Name disable Auto Focus | Type boolean | Description If you set variant to "success" , or role to "alert" , JavaScript moves the keyboard focus to the notification banner when the page loads. To disable this behaviour, set disableAutoFocus to true .
Name classes | Type string | Description The classes that you want to add to the notification banner.
Name attributes | Type object | Description The HTML attributes that you want to add to the notification banner, for example, data attributes.

- if you do not set variant , title.text defaults to "Important"

- if you set variant to "success" , title.text defaults to "Success"

- if you set title.text or title.html , the defaults are ignored

Name | Type | Description
Name id | Type string | Description The ID of the title.
Name text | Type string | Description Required. If html is set, this is not required. Text for the title. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the title. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the title.
Name heading Level | Type integer | Description Optional alias for the title heading level option.
Name level | Type integer | Description Optional heading level for the title. Defaults to 2 .
Name classes | Type string | Description Classes to add to the title.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the title.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the heading.
Name href | Type string | Description If set, the heading will become a link.
Name caption | Type object | Description Optional caption for the heading. See macro options for caption .
Name level | Type integer | Description Optional heading level for the heading. Defaults to 3 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.
Name element | Type string | Description HTML element for the heading – for example, "p" . Defaults to the level option prefixed with "h" .

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
"notification-banner/macro.njk"
import
notificationBanner
%}
{{
notificationBanner
({
text
:
"The service will be unavailable from 8pm to 9pm on Thursday 1 January 2025."
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

If your service is getting more demand than usual, check that you've set up "There is a problem with the service" pages and "Service unavailable" pages, and the wording is up to date. Use the patterns in the GOV.UK design system .

You can also use the information banner to tell users information about something that's happening elsewhere in the service. For example:

- in a case working system, the user might need to know that there are new cases waiting for their attention

- in an account-type service, you might need to tell the user that there's a deadline approaching or that a payment is overdue

- HTML code for notification banners second

- Nunjucks code for notification banners second

```text
<
div
class
=
"nhsuk-notification-banner"
data-module
=
"nhsuk-notification-banner"
role
=
"region"
aria-labelledby
=
"nhsuk-notification-banner-title"
>
<
div
class
=
"nhsuk-notification-banner__header"
>
<
h2
class
=
"nhsuk-notification-banner__title"
id
=
"nhsuk-notification-banner-title"
>
Important
</
h2
>
</
div
>
<
div
class
=
"nhsuk-notification-banner__content"
>
<
p
class
=
"nhsuk-notification-banner__heading"
>
<
p
class
=
"nhsuk-notification-banner__heading"
>
You have 7 days left to send your application.
<
a
class
=
"nhsuk-notification-banner__link"
href
=
"#"
>
View application
</
a
>
.
</
p
>
</
p
>
</
div
>
</
div
>
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the notification banner.
Name title | Type object | Description The title that displays in the notification banner: if you do not set variant , title.text defaults to "Important" if you set variant to "success" , title.text defaults to "Success" if you set title.text or title.html , the defaults are ignored See macro options for title .
Name title Id | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the title.id option.
Name title Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the title.text option.
Name title Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the title.html option.
Name title Heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the title.level option.
Name heading | Type object | Description Heading to be used within the notification banner. See macro options for heading .
Name text | Type string | Description Required. The text that displays in the notification banner. You can use any string with this option. If you set html , this option is not required and is ignored.
Name html | Type string | Description Required. The HTML to use within the notification banner. You can use any string with this option. If you set html , text is not required and is ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire notification banner component in a call block.
Name variant | Type string | Description Optional variant of notification banner. You can use only "success" or empty values with this option. If you set variant to "success" , the notification banner sets role to "alert" . JavaScript then moves the keyboard focus to the notification banner when the page loads. If you do not set variant , the notification banner sets role to "region" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option.
Name role | Type string | Description Overrides the value of the role attribute for the notification banner. Defaults to "region" . If you set variant to "success" , role defaults to "alert" .
Name disable Auto Focus | Type boolean | Description If you set variant to "success" , or role to "alert" , JavaScript moves the keyboard focus to the notification banner when the page loads. To disable this behaviour, set disableAutoFocus to true .
Name classes | Type string | Description The classes that you want to add to the notification banner.
Name attributes | Type object | Description The HTML attributes that you want to add to the notification banner, for example, data attributes.

- if you do not set variant , title.text defaults to "Important"

- if you set variant to "success" , title.text defaults to "Success"

- if you set title.text or title.html , the defaults are ignored

Name | Type | Description
Name id | Type string | Description The ID of the title.
Name text | Type string | Description Required. If html is set, this is not required. Text for the title. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the title. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the title.
Name heading Level | Type integer | Description Optional alias for the title heading level option.
Name level | Type integer | Description Optional heading level for the title. Defaults to 2 .
Name classes | Type string | Description Classes to add to the title.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the title.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the heading.
Name href | Type string | Description If set, the heading will become a link.
Name caption | Type object | Description Optional caption for the heading. See macro options for caption .
Name level | Type integer | Description Optional heading level for the heading. Defaults to 3 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.
Name element | Type string | Description HTML element for the heading – for example, "p" . Defaults to the level option prefixed with "h" .

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
"notification-banner/macro.njk"
import
notificationBanner
%}
{%
set
html
%}
<
p
class
=
"nhsuk-notification-banner__heading"
>
You have 7 days left to send your application.
<
a
class
=
"nhsuk-notification-banner__link"
href
=
"#"
>
View application
</
a
>
.
</
p
>
{%
endset
%}
{{
notificationBanner
({
heading
: {
html
: html,
element
:
"p"
}
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

## Using the success banner

Use a success banner to confirm an action on a previous page was successful. For example, for steps in a long journey or small repeated tasks.

- HTML code for notification banners success

- Nunjucks code for notification banners success

```text
<
div
class
=
"nhsuk-notification-banner nhsuk-notification-banner--success"
data-module
=
"nhsuk-notification-banner"
role
=
"alert"
aria-labelledby
=
"nhsuk-notification-banner-title"
>
<
div
class
=
"nhsuk-notification-banner__header"
>
<
h2
class
=
"nhsuk-notification-banner__title"
id
=
"nhsuk-notification-banner-title"
>
Success
</
h2
>
</
div
>
<
div
class
=
"nhsuk-notification-banner__content"
>
<
h3
class
=
"nhsuk-notification-banner__heading"
>
Patient record updated
</
h3
>
<
p
>
Contact
<
a
class
=
"nhsuk-notification-banner__link"
href
=
"#"
>
example@department.nhs.uk
</
a
>
if you think there's a problem.
</
p
>
</
div
>
</
div
>
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the notification banner.
Name title | Type object | Description The title that displays in the notification banner: if you do not set variant , title.text defaults to "Important" if you set variant to "success" , title.text defaults to "Success" if you set title.text or title.html , the defaults are ignored See macro options for title .
Name title Id | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the title.id option.
Name title Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the title.text option.
Name title Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the title.html option.
Name title Heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the title.level option.
Name heading | Type object | Description Heading to be used within the notification banner. See macro options for heading .
Name text | Type string | Description Required. The text that displays in the notification banner. You can use any string with this option. If you set html , this option is not required and is ignored.
Name html | Type string | Description Required. The HTML to use within the notification banner. You can use any string with this option. If you set html , text is not required and is ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire notification banner component in a call block.
Name variant | Type string | Description Optional variant of notification banner. You can use only "success" or empty values with this option. If you set variant to "success" , the notification banner sets role to "alert" . JavaScript then moves the keyboard focus to the notification banner when the page loads. If you do not set variant , the notification banner sets role to "region" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option.
Name role | Type string | Description Overrides the value of the role attribute for the notification banner. Defaults to "region" . If you set variant to "success" , role defaults to "alert" .
Name disable Auto Focus | Type boolean | Description If you set variant to "success" , or role to "alert" , JavaScript moves the keyboard focus to the notification banner when the page loads. To disable this behaviour, set disableAutoFocus to true .
Name classes | Type string | Description The classes that you want to add to the notification banner.
Name attributes | Type object | Description The HTML attributes that you want to add to the notification banner, for example, data attributes.

- if you do not set variant , title.text defaults to "Important"

- if you set variant to "success" , title.text defaults to "Success"

- if you set title.text or title.html , the defaults are ignored

Name | Type | Description
Name id | Type string | Description The ID of the title.
Name text | Type string | Description Required. If html is set, this is not required. Text for the title. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the title. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the title.
Name heading Level | Type integer | Description Optional alias for the title heading level option.
Name level | Type integer | Description Optional heading level for the title. Defaults to 2 .
Name classes | Type string | Description Classes to add to the title.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the title.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the heading.
Name href | Type string | Description If set, the heading will become a link.
Name caption | Type object | Description Optional caption for the heading. See macro options for caption .
Name level | Type integer | Description Optional heading level for the heading. Defaults to 3 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.
Name element | Type string | Description HTML element for the heading – for example, "p" . Defaults to the level option prefixed with "h" .

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
"notification-banner/macro.njk"
import
notificationBanner
%}
{%
set
html
%}
<
p
>
Contact
<
a
class
=
"nhsuk-notification-banner__link"
href
=
"#"
>
example@department.nhs.uk
</
a
>
if you think there's a problem.
</
p
>
{%
endset
%}
{{
notificationBanner
({
heading
:
"Patient record updated"
,
html
: html,
variant
:
"success"
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

Remove the success banner when the user moves to a new page.

When the user finishes an entire journey, for example, a service that lets the user register for a thing, use a confirmation page , instead of a success banner.

For long, complex services, use the task list component . You are unlikely to need a success banner on a page with a task list.

## Accessibility

To make notification banners accessible:

- use a heading like "Success" so that you're not relying on colour alone to convey meaning (to meet WCAG 2.2 success criterion 1.4.1 Use of colour )

- use the same heading for banners across a service so that you're identifying components that work in the same way consistently (to meet WCAG 2.2 success criterion 3.2.4 Consistent identification )

- the success banner includes role="alert" so the focus state shifts to the notification banner on page load.

## Research on this component

We need more research to understand:

- how common it is for users to miss important information in notification banners (including users of assistive technology, who might skip straight to the h1 )

- when it's helpful to allow users to dismiss notifications, and how to do this

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
