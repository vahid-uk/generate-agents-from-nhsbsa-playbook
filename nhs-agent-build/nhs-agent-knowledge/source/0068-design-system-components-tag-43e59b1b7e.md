# Tag – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/tag/

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

# Content presentation – Tag

## When to use a tag

Use the tag component when it's possible for something to have more than 1 status and it's useful for the user to know about that status. For example, you can use a tag to show whether an item in a task list has been "completed".

## How it works

Tags are just used to indicate a status. Do not add links. Use adjectives rather than verbs for the names of your tags. Using a verb might make a user think that clicking on them will do something.

### Showing 1 or 2 statuses

Sometimes a single status is enough. For example, if you need to tell users which parts of an application they've finished and which they have not, you may only need a "Completed" tag. Because the user understands that if something does not have a tag, that means it's incomplete.

Or it can make sense to have 2 statuses. For example, you may find that you need 1 tag for "Active" users and 1 for "Inactive" users.

- HTML code for tag

- Nunjucks code for tag

```text
<
table
class
=
"nhsuk-table"
>
<
thead
class
=
"nhsuk-table__head"
>
<
tr
class
=
"nhsuk-table__row"
>
<
th
class
=
"nhsuk-table__header"
scope
=
"col"
>
Name of user
</
th
>
<
th
class
=
"nhsuk-table__header"
scope
=
"col"
>
Status
</
th
>
</
tr
>
</
thead
>
<
tbody
class
=
"nhsuk-table__body"
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Les Hunter
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--grey"
>
Inactive
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Naomi Edwards
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--grey"
>
Inactive
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Lyra Louth
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag"
>
Active
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Michelle Flynn
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag"
>
Active
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Brian Okello
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--grey"
>
Inactive
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Lisa Lenehan
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag"
>
Active
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Emily Snailham
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--grey"
>
Inactive
</
strong
>
</
td
>
</
tr
>
</
tbody
>
</
table
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the tag.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the tag component. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the tag component. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire tag component in a call block.
Name classes | Type string | Description Classes to add to the tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the tag.
Name colour | Type string | Description Optional colour modifier for the tag – "white" , "grey" , "green" , "aqua-green" , "blue" , "purple" , "pink" , "red" , "orange" or "yellow" . If set to false , remove colour from the tag.
Name border | Type boolean | Description If set to false , remove border from the tag.

```text
{%
from
"tag/macro.njk"
import
tag
%}
{%
from
"tables/macro.njk"
import
table
%}
{{
table
({
head
: [
    {
text
:
"Name of user"
},
    {
text
:
"Status"
}
  ],
rows
: [
    [
      {
text
:
"Les Hunter"
},
      {
html
:
tag
({
text
:
"Inactive"
,
colour
:
"grey"
})
}
    ],
    [
      {
text
:
"Naomi Edwards"
},
      {
html
:
tag
({
text
:
"Inactive"
,
colour
:
"grey"
})
}
    ],
    [
      {
text
:
"Lyra Louth"
},
      {
html
:
tag
({
text
:
"Active"
})
}
    ],
    [
      {
text
:
"Michelle Flynn"
},
      {
html
:
tag
({
text
:
"Active"
})
}
    ],
    [
      {
text
:
"Brian Okello"
},
      {
html
:
tag
({
text
:
"Inactive"
,
colour
:
"grey"
})
}
    ],
    [
      {
text
:
"Lisa Lenehan"
},
      {
html
:
tag
({
text
:
"Active"
})
}
    ],
    [
      {
text
:
"Emily Snailham"
},
      {
html
:
tag
({
text
:
"Inactive"
,
colour
:
"grey"
})
}
    ]
  ]
}) }}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Showing multiple statuses

Tags should be helpful to users. The more you add, the harder it is for users to remember them. So start with the smallest number of statuses you think might work, then add more if your user research shows there's a need for them.

- HTML code for tag multiple

- Nunjucks code for tag multiple

```text
<
table
class
=
"nhsuk-table"
>
<
thead
class
=
"nhsuk-table__head"
>
<
tr
class
=
"nhsuk-table__row"
>
<
th
class
=
"nhsuk-table__header"
scope
=
"col"
>
Application
</
th
>
<
th
class
=
"nhsuk-table__header"
scope
=
"col"
>
Status
</
th
>
</
tr
>
</
thead
>
<
tbody
class
=
"nhsuk-table__body"
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Leo Cashin
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--red"
>
Urgent
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Amy Louth
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--blue"
>
New
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Barbara Angel
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--blue"
>
New
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Annette Armstrong
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--blue"
>
New
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Vishal Gurudutt
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--blue"
>
New
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Rachel Preece
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--green"
>
Finished
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
Tom Hunter
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--yellow"
>
Waiting on
</
strong
>
</
td
>
</
tr
>
</
tbody
>
</
table
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the tag.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the tag component. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the tag component. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire tag component in a call block.
Name classes | Type string | Description Classes to add to the tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the tag.
Name colour | Type string | Description Optional colour modifier for the tag – "white" , "grey" , "green" , "aqua-green" , "blue" , "purple" , "pink" , "red" , "orange" or "yellow" . If set to false , remove colour from the tag.
Name border | Type boolean | Description If set to false , remove border from the tag.

```text
{%
from
"tag/macro.njk"
import
tag
%}
{%
from
"tables/macro.njk"
import
table
%}
{{
table
({
head
: [
    {
text
:
"Application"
},
    {
text
:
"Status"
}
  ],
rows
: [
    [
      {
text
:
"Leo Cashin"
},
      {
html
:
tag
({
text
:
"Urgent"
,
colour
:
"red"
})
}
    ],
    [
      {
text
:
"Amy Louth"
},
      {
html
:
tag
({
text
:
"New"
,
colour
:
"blue"
})
}
    ],
    [
      {
text
:
"Barbara Angel"
},
      {
html
:
tag
({
text
:
"New"
,
colour
:
"blue"
})
}
    ],
    [
      {
text
:
"Annette Armstrong"
},
      {
html
:
tag
({
text
:
"New"
,
colour
:
"blue"
})
}
    ],
    [
      {
text
:
"Vishal Gurudutt"
},
      {
html
:
tag
({
text
:
"New"
,
colour
:
"blue"
})
}
    ],
    [
      {
text
:
"Rachel Preece"
},
      {
html
:
tag
({
text
:
"Finished"
,
colour
:
"green"
})
}
    ],
    [
      {
text
:
"Tom Hunter"
},
      {
html
:
tag
({
text
:
"Waiting on"
,
colour
:
"yellow"
})
}
    ]
  ]
}) }}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Using colour with tags

You can use colour to help distinguish between different tags – or to help draw the user's attention to a tag if it's especially important. For example, it makes sense to use nhsuk-tag--red for a tag that reads "Urgent".

Do not rely on colour alone to convey information because it's not accessible. If you use the same tag in more than 1 place, make sure you keep the colour consistent.

Because tags with solid colours tend to stand out more, it's usually best to avoid mixing solid colours and tints: use one or the other. This matters less if you're only using 2 colours. For example, it's okay to use the tint nhsuk-tag--grey and solid blue tags together if you only need 2 statuses.

We use a border of the same colour as the tag text to stand out against the NHS page background colour.

### Additional colours

If you need more tag colours, you can use the following tints.

- HTML code for tag colours

- Nunjucks code for tag colours

```text
<
table
class
=
"nhsuk-table"
>
<
thead
class
=
"nhsuk-table__head"
>
<
tr
class
=
"nhsuk-table__row"
>
<
th
class
=
"nhsuk-table__header"
scope
=
"col"
>
Class name
</
th
>
<
th
class
=
"nhsuk-table__header"
scope
=
"col"
>
Tag
</
th
>
</
tr
>
</
thead
>
<
tbody
class
=
"nhsuk-table__body"
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
<
code
>
nhsuk-tag--white
</
code
>
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--white"
>
In progress
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
<
code
>
nhsuk-tag--grey
</
code
>
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--grey"
>
Inactive
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
<
code
>
nhsuk-tag--green
</
code
>
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--green"
>
New
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
<
code
>
nhsuk-tag--blue
</
code
>
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--blue"
>
Active
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
<
code
>
nhsuk-tag--aqua-green
</
code
>
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--aqua-green"
>
Pending
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
<
code
>
nhsuk-tag--purple
</
code
>
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--purple"
>
Received
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
<
code
>
nhsuk-tag--pink
</
code
>
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--pink"
>
Sent
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
<
code
>
nhsuk-tag--red
</
code
>
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--red"
>
Rejected
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
<
code
>
nhsuk-tag--orange
</
code
>
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--orange"
>
Declined
</
strong
>
</
td
>
</
tr
>
<
tr
class
=
"nhsuk-table__row"
>
<
td
class
=
"nhsuk-table__cell"
>
<
code
>
nhsuk-tag--yellow
</
code
>
</
td
>
<
td
class
=
"nhsuk-table__cell"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--yellow"
>
Delayed
</
strong
>
</
td
>
</
tr
>
</
tbody
>
</
table
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the tag.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the tag component. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the tag component. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire tag component in a call block.
Name classes | Type string | Description Classes to add to the tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the tag.
Name colour | Type string | Description Optional colour modifier for the tag – "white" , "grey" , "green" , "aqua-green" , "blue" , "purple" , "pink" , "red" , "orange" or "yellow" . If set to false , remove colour from the tag.
Name border | Type boolean | Description If set to false , remove border from the tag.

```text
{%
from
"tag/macro.njk"
import
tag
%}
{%
from
"tables/macro.njk"
import
table
%}
{{
table
({
head
: [
    {
text
:
"Class name"
},
    {
text
:
"Tag"
}
  ],
rows
: [
    [
      {
html
:
"<code>nhsuk-tag--white</code>"
},
      {
html
:
tag
({
text
:
"In progress"
,
colour
:
"white"
})
}
    ],
    [
      {
html
:
"<code>nhsuk-tag--grey</code>"
},
      {
html
:
tag
({
text
:
"Inactive"
,
colour
:
"grey"
})
}
    ],
    [
      {
html
:
"<code>nhsuk-tag--green</code>"
},
      {
html
:
tag
({
text
:
"New"
,
colour
:
"green"
})
}
    ],
    [
      {
html
:
"<code>nhsuk-tag--blue</code>"
},
      {
html
:
tag
({
text
:
"Active"
,
colour
:
"blue"
})
}
    ],
    [
      {
html
:
"<code>nhsuk-tag--aqua-green</code>"
},
      {
html
:
tag
({
text
:
"Pending"
,
colour
:
"aqua-green"
})
}
    ],
    [
      {
html
:
"<code>nhsuk-tag--purple</code>"
},
      {
html
:
tag
({
text
:
"Received"
,
colour
:
"purple"
})
}
    ],
    [
      {
html
:
"<code>nhsuk-tag--pink</code>"
},
      {
html
:
tag
({
text
:
"Sent"
,
colour
:
"pink"
})
}
    ],
    [
      {
html
:
"<code>nhsuk-tag--red</code>"
},
      {
html
:
tag
({
text
:
"Rejected"
,
colour
:
"red"
})
}
    ],
    [
      {
html
:
"<code>nhsuk-tag--orange</code>"
},
      {
html
:
tag
({
text
:
"Declined"
,
colour
:
"orange"
})
}
    ],
    [
      {
html
:
"<code>nhsuk-tag--yellow</code>"
},
      {
html
:
tag
({
text
:
"Delayed"
,
colour
:
"yellow"
})
}
    ]
  ]
}) }}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## Accessibility

All contrasts between text and background meet level AAA of WCAG 2.0. Read more about accessibility and colour .

## Research

We have tested tags in the NHS e-referral service, the "Submit your electronic declaration" service and the NHS App prescriptions service. We found that they helped users:

- make a decision about whether or not to proceed with their journey

- understand their progress or the status of an order

- save time as they could see the information they needed quickly

We also found that it helped to use sentence case rather than block capitals for readability.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
