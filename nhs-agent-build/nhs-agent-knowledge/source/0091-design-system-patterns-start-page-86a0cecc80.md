# Start page – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/patterns/start-page/

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

# Pages – Start page

Use this pattern to help users start a service.

- HTML code for start page example

- Nunjucks code for start page example

```text
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
Online services
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
Online services
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
"nhsuk-heading-xl"
>
Find your NHS number
</
h1
>
<
p
>
Use this service to get your NHS number.
</
p
>
<
p
>
Your NHS number is a 10 digit number, like
<
span
class
=
"nhsuk-u-nowrap"
>
999 123 4567
</
span
>
.
</
p
>
<
p
>
You do not need to know your NHS number to use NHS services, but it can be useful to have it.
</
p
>
<
div
class
=
"nhsuk-inset-text"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Information:
</
span
>
<
p
>
You can also get your NHS number in your
<
a
href
=
"#"
>
NHS account
</
a
>
.
</
p
>
</
div
>
<
h2
class
=
"nhsuk-heading-l"
>
Who can use this service
</
h2
>
<
p
>
You can use this service if you live in England.
</
p
>
<
p
>
You can also use this service for someone else.
</
p
>
<
h2
class
=
"nhsuk-heading-l"
>
Before you start
</
h2
>
<
p
>
You will need your:
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
full name
</
li
>
<
li
>
date of birth
</
li
>
<
li
>
postcode of the address you've registered at a GP surgery with
</
li
>
</
ul
>
<
p
>
You will have your NHS number sent to you by text, email or letter.
</
p
>
<
p
>
If you're using this service for someone else, enter their details. They will be sent their NHS number.
</
p
>
<
p
>
By using this service you agree to our
<
a
href
=
"#"
>
terms of use
</
a
>
and confirm that you have read the
<
a
href
=
"#"
>
privacy policy
</
a
>
.
</
p
>
<
a
class
=
"nhsuk-button"
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
Start now
</
a
>
<
h2
class
=
"nhsuk-heading-m"
>
Other ways to get your NHS number
</
h2
>
<
p
>
If you cannot get your NHS number online you can:
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
find it on any letter from the NHS like a prescription or appointment letter
</
li
>
<
li
>
call your GP surgery and ask them for your number
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
</
main
>
</
div
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
"button/macro.njk"
import
button
%}
{%
from
"inset-text/macro.njk"
import
insetText
%}
{%
set
mainClasses
=
"nhsuk-main-wrapper--s"
%}
{%
set
dummyNhsNumber
=
"999 123 4567"
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
"NHS services"
},
      {
href
:
"#"
,
text
:
"Online services"
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
Find your NHS number
</
h1
>
<
p
>
Use this service to get your NHS number.
</
p
>
<
p
>
Your NHS number is a 10 digit number, like
<
span
class
=
"nhsuk-u-nowrap"
>
{{
dummyNhsNumber
}}
</
span
>
.
</
p
>
<
p
>
You do not need to know your NHS number to use NHS services, but it can be useful to have it.
</
p
>
{%
set
insetTextHtml
%}
<
p
>
You can also get your NHS number in your
<
a
href
=
"#"
>
NHS account
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
insetText
({
html
: insetTextHtml | safe
      })
}}
<
h2
class
=
"nhsuk-heading-l"
>
Who can use this service
</
h2
>
<
p
>
You can use this service if you live in England.
</
p
>
<
p
>
You can also use this service for someone else.
</
p
>
<
h2
class
=
"nhsuk-heading-l"
>
Before you start
</
h2
>
<
p
>
You will need your:
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
full name
</
li
>
<
li
>
date of birth
</
li
>
<
li
>
postcode of the address you've registered at a GP surgery with
</
li
>
</
ul
>
<
p
>
You will have your NHS number sent to you by text, email or letter.
</
p
>
<
p
>
If you're using this service for someone else, enter their details. They will be sent their NHS number.
</
p
>
<
p
>
By using this service you agree to our
<
a
href
=
"#"
>
terms of use
</
a
>
and confirm that you have read the
<
a
href
=
"#"
>
privacy policy
</
a
>
.
</
p
>
{{
button
({
text
:
"Start now"
,
href
:
"#"
})
}}
<
h2
class
=
"nhsuk-heading-m"
>
Other ways to get your NHS number
</
h2
>
<
p
>
If you cannot get your NHS number online you can:
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
find it on any letter from the NHS like a prescription or appointment letter
</
li
>
<
li
>
call your GP surgery and ask them for your number
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
{%
endblock
%}
```

## When to use a start page

At the start of a service which involves the user inputting information in order to get something. For example, at the start of an application form.

To get a start page on the NHS website, contact the NHS website information architecture team on the #information-architecture channel on the service manual public Slack workspace .

## How to use a start page

Start pages include 4 main elements. These are:

- the service name: this helps people understand what your service does and whether they need to use it, like Find your NHS number – read more about naming your service on GOV.UK

- a list of things most users need to know: for example, what your service is, what will happen, what users will get or how much it'll cost

- the "Start now" call-to-action button

- a list of other ways to access the service: for example, phone or text relay

Keep your start page focused on helping users get started and successfully complete the service.

A good start page:

- lets users know they're in the right place

- sets expectations: users know what to expect before clicking anything, including whether they're eligible and what the outcome will be

- helps users succeed by telling them what information they must give or documents they need to have

- gives users options if the service is not for them, because it's connected to a wider topic

- is easy to find and ranks highly in search engines, because it uses the language of its users

Read more about designing how content and transactions work together, on GOV.UK .

### Put your start page in the right place

Consider where your transaction sits in a wider topic, service or website. Do not disconnect it from its wider context. Place it in a broader information architecture with elements such as the main navigation, internal search and breadcrumbs. This helps users:

- feel confident they're on the right start page

- know if the service is for them and that they're eligible

- avoid dead ends, if they're in the wrong place, and find what they need through surrounding navigation elements

The Book, change or cancel a COVID-19 vaccination appointment service on the NHS website is in the section about vaccination and booking services.

The start page links to other information people want to know about COVID-19 vaccines.

If possible:

- run an open card sort to see how users group and label pages around your start page, including the start page

- run tree tests to check users find the start page in your proposed structure

- follow up with usability testing

### Keep important information above the button

Many users do not look at information below the start button.

If information applies to everyone and they need it to complete the service, put it above the button.

Sometimes it's necessary to put information that only some users need below the button to stop the page getting too long for the majority of users.

### Set a helpful URL

Set up a URL that embeds your start page in the wider service, topic or website. Use a verb that reflects the name of the task or service.

Here is a good example: https://www.nhs.uk/nhs-services/hospitals/book-an-appointment . It's the URL for booking an appointment using the NHS e-Referral service. It shows the start page's relationship to the wider topic and the website it sits in: book an appointment, for hospitals that are part of NHS services.

If you need to, create a short vanity URL to promote the service in letters or other offline activities which direct people to the service start page. For example, this is the vanity URL for e-Referral service bookings: https://www.nhs.uk/referrals .

### Make it easy to update your start page

Some start pages need to be updated regularly, sometimes at short notice.

If possible, put your start page in a content management system (CMS) so it's easy for a number of people to amend. It can be difficult to manage if you have it in a separate application and rely on a developer to make changes.

### Check your start page includes the correct links

Many websites (including the NHS website) have policy and contact information links in the footer that relate to the website as a whole. These may not be the right links for your service.

If your start page sits in a wider website, but your service is on an external domain, make sure users can access service-specific policy and contact information, for example by placing links to them within the start page.

### What not to include on a start page

Avoid telling people all about the service on the start page. Too much information will distract them.

If you can, check eligibility as part of the service to avoid overloading the start page with criteria.

Do not use an action link on a start page instead of a button.

## Accessibility

It's particularly important to keep your start page brief for users with access needs. Consider:

- how a screen reader will read out the content

- how much time it takes for the user to get to the main call to action

- how much information they have to process

Lots of people miss information below the start button, especially:

- people who zoom in or magnify content on the page

- people with screen readers who navigate the page by headings and interactive elements (such as buttons)

## Research

This pattern is based on the start page in the GOV.UK Design System, which has been tested over a number of years in a wide range of contexts.

### Start now button

We follow the GOV.UK start page pattern and word the start button "Start now".

There are good reasons to use context-specific verbs, like "Book now", "Check now" or "Start booking", but we do not have enough research to recommend these yet. Please let us know if you have research to share.

### Average time to complete

Some services have found that telling users how long it takes helps set expectations and increases the number of successful journeys.

But the time it takes varies a lot, especially for users with access needs. Users who take longer than average may feel pressurised or stupid. If you're researching this, test with a wide range of users, and let us know what you find.

### Known issues and gaps

We do not yet have enough information about start pages in applications, such as services in the NHS App that appear after a user has signed in.

We also need to know more about services where the user needs to read content as part of the journey, as well as filling in a form.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: August 2026
