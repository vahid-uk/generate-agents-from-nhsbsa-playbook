# Summary list – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/summary-list/

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

# Content presentation – Summary list

Use the summary list to summarise information, for example, a user's responses at the end of a form.

- HTML code for summary list

- Nunjucks code for summary list

```text
<
dl
class
=
"nhsuk-summary-list"
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Name
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
Karen Francis
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
name
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Date of birth
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
15 March 1984
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
date of birth
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Contact information
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
73 Roman Rd
<
br
>
Leeds
<
br
>
LS2 5ZN
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
contact information
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Contact details
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
<
p
>
07700 900362
</
p
>
<
p
>
karen.francis@example.com
</
p
>
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
contact details
</
span
>
</
a
>
</
dd
>
</
div
>
</
dl
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the summary list.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. The rows within the summary list component. See macro options for rows .
Name html | Type string | Description HTML to use within the summary list.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire summary list component in a call block.
Name card | Type object | Description Can be used to wrap a card around the summary list component. If any of these options are present, a card will wrap around the summary list. See macro options for card .
Name classes | Type string | Description Classes to add to the container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the container.

Name | Type | Description
Name id | Type string | Description The ID of the row.
Name classes | Type string | Description Classes to add to the row.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the row.
Name border | Type boolean | Description If set to false , remove separating border from the row.
Name key | Type object | Description Required. The reference content (key) for each row item in the summary list component. See macro options for rows key .
Name value | Type object | Description Required. The value for each row item in the summary list component. See macro options for rows value .
Name actions | Type object | Description The action link content for each row item in the summary list component. See macro options for rows actions .

Name | Type | Description
Name id | Type string | Description The ID of the key item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each key. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each key. If html is provided, the text option will be ignored.
Name width | Type string | Description Specify the key wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the key wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the key wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the value item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each value. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each value. If html is provided, the text option will be ignored.
Name width | Type string | Description Specify the value wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the value wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the value wrapper.

Name | Type | Description
Name items | Type array | Description The action link items within the row item of the summary list component. See macro options for rows actions items .
Name width | Type string | Description Specify the actions wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the actions wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If type is set, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If type is set, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"summary-list/macro.njk"
import
summaryList
%}
{{
summaryList
({
rows
: [
    {
key
: {
text
:
"Name"
},
value
: {
text
:
"Karen Francis"
},
actions
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
"Change"
,
visuallyHiddenText
:
"name"
}
        ]
      }
    },
    {
key
: {
text
:
"Date of birth"
},
value
: {
text
:
"15 March 1984"
},
actions
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
"Change"
,
visuallyHiddenText
:
"date of birth"
}
        ]
      }
    },
    {
key
: {
text
:
"Contact information"
},
value
: {
html
:
"73 Roman Rd<br>Leeds<br> LS2 5ZN"
},
actions
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
"Change"
,
visuallyHiddenText
:
"contact information"
}
        ]
      }
    },
    {
key
: {
text
:
"Contact details"
},
value
: {
html
:
"<p>07700 900362</p><p>karen.francis@example.com</p>"
},
actions
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
"Change"
,
visuallyHiddenText
:
"contact details"
}
        ]
      }
    }
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## When to use summary lists

Use the summary list component to present pairs of related information, known as key-value pairs, in a list, where:

- the key is a label, like "Name"

- the value is the piece of information itself, like "John Smith"

Think about how you can use the summary list along with other components or patterns to give users a sense of control. You can use it to summarise a user's responses at the end of a form, for example as part of the check answers pattern .

## When not to use summary lists

The summary list uses the description list <dl> HTML element, so only use it to present information that has a key and at least 1 value.

Do not use it for tabular data or a simple list of information or tasks, like a task list page. (See the complete multiple tasks pattern .) For those, use a <table> , <ul> or <ol> .

## How to use summary lists

### Summary list with actions

You can add actions to a summary list, like a "Change" link to let users go back and edit their answer. If you do this, make sure information they have already entered is pre-populated.

People who use assistive technology, like a screen reader, may hear the links out of context and not know what they do. To give more context, add visually hidden text to the links. This means a screen reader user will hear a meaningful action, like "Change name" or "Change date of birth".

- HTML code for summary list second

- Nunjucks code for summary list second

```text
<
dl
class
=
"nhsuk-summary-list"
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Name
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
Karen Francis
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
name
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Date of birth
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
15 March 1984
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
date of birth
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Contact information
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
73 Roman Rd
<
br
>
Leeds
<
br
>
LS2 5ZN
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
contact information
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Contact details
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
<
p
>
07700 900362
</
p
>
<
p
>
karen.francis@example.com
</
p
>
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
contact details
</
span
>
</
a
>
</
dd
>
</
div
>
</
dl
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the summary list.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. The rows within the summary list component. See macro options for rows .
Name html | Type string | Description HTML to use within the summary list.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire summary list component in a call block.
Name card | Type object | Description Can be used to wrap a card around the summary list component. If any of these options are present, a card will wrap around the summary list. See macro options for card .
Name classes | Type string | Description Classes to add to the container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the container.

Name | Type | Description
Name id | Type string | Description The ID of the row.
Name classes | Type string | Description Classes to add to the row.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the row.
Name border | Type boolean | Description If set to false , remove separating border from the row.
Name key | Type object | Description Required. The reference content (key) for each row item in the summary list component. See macro options for rows key .
Name value | Type object | Description Required. The value for each row item in the summary list component. See macro options for rows value .
Name actions | Type object | Description The action link content for each row item in the summary list component. See macro options for rows actions .

Name | Type | Description
Name id | Type string | Description The ID of the key item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each key. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each key. If html is provided, the text option will be ignored.
Name width | Type string | Description Specify the key wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the key wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the key wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the value item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each value. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each value. If html is provided, the text option will be ignored.
Name width | Type string | Description Specify the value wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the value wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the value wrapper.

Name | Type | Description
Name items | Type array | Description The action link items within the row item of the summary list component. See macro options for rows actions items .
Name width | Type string | Description Specify the actions wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the actions wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If type is set, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If type is set, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"summary-list/macro.njk"
import
summaryList
%}
{{
summaryList
({
rows
: [
    {
key
: {
text
:
"Name"
},
value
: {
text
:
"Karen Francis"
},
actions
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
"Change"
,
visuallyHiddenText
:
"name"
}
        ]
      }
    },
    {
key
: {
text
:
"Date of birth"
},
value
: {
text
:
"15 March 1984"
},
actions
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
"Change"
,
visuallyHiddenText
:
"date of birth"
}
        ]
      }
    },
    {
key
: {
text
:
"Contact information"
},
value
: {
html
:
"73 Roman Rd<br>Leeds<br> LS2 5ZN"
},
actions
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
"Change"
,
visuallyHiddenText
:
"contact information"
}
        ]
      }
    },
    {
key
: {
text
:
"Contact details"
},
value
: {
html
:
"<p>07700 900362</p><p>karen.francis@example.com</p>"
},
actions
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
"Change"
,
visuallyHiddenText
:
"contact details"
}
        ]
      }
    }
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Summary list without actions

- HTML code for summary list without action

- Nunjucks code for summary list without action

```text
<
dl
class
=
"nhsuk-summary-list"
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Name
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
Karen Francis
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Date of birth
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
15 March 1984
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Contact information
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
73 Roman Rd
<
br
>
Leeds
<
br
>
LS2 5ZN
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Contact details
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
<
p
>
07700 900362
</
p
>
<
p
>
karen.francis@example.com
</
p
>
</
dd
>
</
div
>
</
dl
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the summary list.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. The rows within the summary list component. See macro options for rows .
Name html | Type string | Description HTML to use within the summary list.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire summary list component in a call block.
Name card | Type object | Description Can be used to wrap a card around the summary list component. If any of these options are present, a card will wrap around the summary list. See macro options for card .
Name classes | Type string | Description Classes to add to the container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the container.

Name | Type | Description
Name id | Type string | Description The ID of the row.
Name classes | Type string | Description Classes to add to the row.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the row.
Name border | Type boolean | Description If set to false , remove separating border from the row.
Name key | Type object | Description Required. The reference content (key) for each row item in the summary list component. See macro options for rows key .
Name value | Type object | Description Required. The value for each row item in the summary list component. See macro options for rows value .
Name actions | Type object | Description The action link content for each row item in the summary list component. See macro options for rows actions .

Name | Type | Description
Name id | Type string | Description The ID of the key item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each key. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each key. If html is provided, the text option will be ignored.
Name width | Type string | Description Specify the key wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the key wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the key wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the value item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each value. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each value. If html is provided, the text option will be ignored.
Name width | Type string | Description Specify the value wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the value wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the value wrapper.

Name | Type | Description
Name items | Type array | Description The action link items within the row item of the summary list component. See macro options for rows actions items .
Name width | Type string | Description Specify the actions wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the actions wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If type is set, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If type is set, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"summary-list/macro.njk"
import
summaryList
%}
{{
summaryList
({
rows
: [
    {
key
: {
text
:
"Name"
},
value
: {
text
:
"Karen Francis"
}
    },
    {
key
: {
text
:
"Date of birth"
},
value
: {
text
:
"15 March 1984"
}
    },
    {
key
: {
text
:
"Contact information"
},
value
: {
html
:
"73 Roman Rd<br>Leeds<br> LS2 5ZN"
}
    },
    {
key
: {
text
:
"Contact details"
},
value
: {
html
:
"<p>07700 900362</p><p>karen.francis@example.com</p>"
}
    }
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Summary list without actions or borders

If you do not include actions in your summary list and it would be better for your design to remove the separating borders, use the nhsuk-summary-list--no-border class.

- HTML code for summary list without border

- Nunjucks code for summary list without border

```text
<
dl
class
=
"nhsuk-summary-list nhsuk-summary-list--no-border"
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Name
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
Karen Francis
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Date of birth
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
15 March 1984
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Contact information
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
73 Roman Rd
<
br
>
Leeds
<
br
>
LS2 5ZN
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Contact details
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
<
p
>
07700 900362
</
p
>
<
p
>
karen.francis@example.com
</
p
>
</
dd
>
</
div
>
</
dl
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the summary list.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. The rows within the summary list component. See macro options for rows .
Name html | Type string | Description HTML to use within the summary list.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire summary list component in a call block.
Name card | Type object | Description Can be used to wrap a card around the summary list component. If any of these options are present, a card will wrap around the summary list. See macro options for card .
Name classes | Type string | Description Classes to add to the container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the container.

Name | Type | Description
Name id | Type string | Description The ID of the row.
Name classes | Type string | Description Classes to add to the row.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the row.
Name border | Type boolean | Description If set to false , remove separating border from the row.
Name key | Type object | Description Required. The reference content (key) for each row item in the summary list component. See macro options for rows key .
Name value | Type object | Description Required. The value for each row item in the summary list component. See macro options for rows value .
Name actions | Type object | Description The action link content for each row item in the summary list component. See macro options for rows actions .

Name | Type | Description
Name id | Type string | Description The ID of the key item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each key. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each key. If html is provided, the text option will be ignored.
Name width | Type string | Description Specify the key wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the key wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the key wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the value item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each value. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each value. If html is provided, the text option will be ignored.
Name width | Type string | Description Specify the value wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the value wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the value wrapper.

Name | Type | Description
Name items | Type array | Description The action link items within the row item of the summary list component. See macro options for rows actions items .
Name width | Type string | Description Specify the actions wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the actions wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If type is set, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If type is set, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"summary-list/macro.njk"
import
summaryList
%}
{{
summaryList
({
border
:
false
,
rows
: [
    {
key
: {
text
:
"Name"
},
value
: {
text
:
"Karen Francis"
}
    },
    {
key
: {
text
:
"Date of birth"
},
value
: {
text
:
"15 March 1984"
}
    },
    {
key
: {
text
:
"Contact information"
},
value
: {
html
:
"73 Roman Rd<br>Leeds<br> LS2 5ZN"
}
    },
    {
key
: {
text
:
"Contact details"
},
value
: {
html
:
"<p>07700 900362</p><p>karen.francis@example.com</p>"
}
    }
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

To remove borders on a single row, use the nhsuk-summary-list__row--no-border class.

## Summary cards

If you're showing multiple summary lists on a page, you can show each list within a summary card. This lets you visually separate each summary list and give each a title and some actions.

Use summary cards when you need to show:

- multiple summary lists that all describe the same type of thing, such as people

- actions that will apply to all the items in a list

Summary cards are often used in case working systems to help users quickly view a set of information and related actions.

Do not use summary cards if you only need to show a small amount of related information. Use summary lists instead, and structure them with headings if needed.

If you're showing summary cards at the end of a longer journey, you might want to familiarise the user with them earlier on, such as when the user reviews individual sections.

### Card titles

Use the summary card's header area to give each summary list a title.

Each title must be unique and help identify what the summary list describes. For example, this could be the name of a specific person, organisation or professional qualification.

Try to keep titles short and relevant. You can use 1 or 2 important values in the summary list, such as the first and last name of a person.

- HTML code for summary list summary card

- Nunjucks code for summary list summary card

```text
<
div
class
=
"nhsuk-card"
>
<
div
class
=
"nhsuk-card__content"
>
<
h2
class
=
"nhsuk-card__heading nhsuk-heading-m"
>
Karen Francis
</
h2
>
<
dl
class
=
"nhsuk-summary-list nhsuk-summary-list--no-last-row-border"
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Name
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
Karen Francis
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
name (Karen Francis)
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Appointment date
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
15 March 2027
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
date of birth (Karen Francis)
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Contact details
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
<
p
>
07700 900362
</
p
>
<
p
>
karen.francis@example.com
</
p
>
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
contact details (Karen Francis)
</
span
>
</
a
>
</
dd
>
</
div
>
</
dl
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
"nhsuk-card"
>
<
div
class
=
"nhsuk-card__content"
>
<
h2
class
=
"nhsuk-card__heading nhsuk-heading-m"
>
Dwayne Harvey
</
h2
>
<
dl
class
=
"nhsuk-summary-list nhsuk-summary-list--no-last-row-border"
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Name
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
Dwayne Harvey
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
name (Dwayne Harvey)
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Appointment date
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
15 March 2027
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
date of birth (Dwayne Harvey)
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Contact details
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
<
p
>
07964 850567
</
p
>
<
p
>
dwayne.harvey@example.com
</
p
>
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
contact details (Dwayne Harvey)
</
span
>
</
a
>
</
dd
>
</
div
>
</
dl
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
Name id | Type string | Description The ID of the summary list.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. The rows within the summary list component. See macro options for rows .
Name html | Type string | Description HTML to use within the summary list.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire summary list component in a call block.
Name card | Type object | Description Can be used to wrap a card around the summary list component. If any of these options are present, a card will wrap around the summary list. See macro options for card .
Name classes | Type string | Description Classes to add to the container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the container.

Name | Type | Description
Name id | Type string | Description The ID of the row.
Name classes | Type string | Description Classes to add to the row.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the row.
Name border | Type boolean | Description If set to false , remove separating border from the row.
Name key | Type object | Description Required. The reference content (key) for each row item in the summary list component. See macro options for rows key .
Name value | Type object | Description Required. The value for each row item in the summary list component. See macro options for rows value .
Name actions | Type object | Description The action link content for each row item in the summary list component. See macro options for rows actions .

Name | Type | Description
Name id | Type string | Description The ID of the key item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each key. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each key. If html is provided, the text option will be ignored.
Name width | Type string | Description Specify the key wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the key wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the key wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the value item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each value. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each value. If html is provided, the text option will be ignored.
Name width | Type string | Description Specify the value wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the value wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the value wrapper.

Name | Type | Description
Name items | Type array | Description The action link items within the row item of the summary list component. See macro options for rows actions items .
Name width | Type string | Description Specify the actions wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the actions wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If type is set, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If type is set, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"summary-list/macro.njk"
import
summaryList
%}
{{
summaryList
({
lastRowBorder
:
false
,
card
: {
heading
: {
text
:
"Karen Francis"
,
size
:
"m"
}
  },
rows
: [
    {
key
: {
text
:
"Name"
},
value
: {
text
:
"Karen Francis"
},
actions
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
"Change"
,
visuallyHiddenText
:
"name"
}
        ]
      }
    },
    {
key
: {
text
:
"Appointment date"
},
value
: {
text
:
"15 March 2027"
},
actions
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
"Change"
,
visuallyHiddenText
:
"date of birth"
}
        ]
      }
    },
    {
key
: {
text
:
"Contact details"
},
value
: {
html
:
"<p>07700 900362</p><p>karen.francis@example.com</p>"
},
actions
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
"Change"
,
visuallyHiddenText
:
"contact details"
}
        ]
      }
    }
  ]
})
}}
{{
summaryList
({
lastRowBorder
:
false
,
card
: {
heading
: {
text
:
"Dwayne Harvey"
,
size
:
"m"
}
  },
rows
: [
    {
key
: {
text
:
"Name"
},
value
: {
text
:
"Dwayne Harvey"
},
actions
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
"Change"
,
visuallyHiddenText
:
"name"
}
        ]
      }
    },
    {
key
: {
text
:
"Appointment date"
},
value
: {
text
:
"15 March 2027"
},
actions
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
"Change"
,
visuallyHiddenText
:
"date of birth"
}
        ]
      }
    },
    {
key
: {
text
:
"Contact details"
},
value
: {
html
:
"<p>07964 850567</p><p>dwayne.harvey@example.com</p>"
},
actions
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
"Change"
,
visuallyHiddenText
:
"contact details"
}
        ]
      }
    }
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

The example uses the nhsuk-summary-list__row--no-border class to remove the bottom border of the last row.

### Card actions

You can add card actions in the header, which will be shown after the summary card's title.

For example, if you have multiple rows with "change" actions that all take the user to the same place, you can show a single "change" card action instead. This helps avoid repeating the same row action on every row.

Card actions are shown in bold text to make them visually distinct from row actions. They help alert the user that the card action will affect the entire summary card.

Write link text for card actions to tell the user what the card action will do and that it will apply to the entire summary card. It should also be as short as possible, usually 2 words.

Example card actions include:

- remove appointment

- edit appointment

- update issue

- approve application

- cancel order

Keep it short and do not add more than 2 to 3 actions in a header.

If a card action cannot easily be undone or might have serious consequences, consider adding a warning or asking the user for confirmation.

- HTML code for summary list summary card with actions

- Nunjucks code for summary list summary card with actions

```text
<
div
class
=
"nhsuk-card"
>
<
div
class
=
"nhsuk-card__heading-container"
>
<
h2
class
=
"nhsuk-card__heading nhsuk-heading-m"
>
Karen Francis
</
h2
>
<
ul
class
=
"nhsuk-card__actions"
>
<
li
class
=
"nhsuk-card__action"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Cancel
<
span
class
=
"nhsuk-u-visually-hidden"
>
(Karen Francis)
</
span
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
"nhsuk-card__action"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Reschedule
<
span
class
=
"nhsuk-u-visually-hidden"
>
(Karen Francis)
</
span
>
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
<
div
class
=
"nhsuk-card__content"
>
<
dl
class
=
"nhsuk-summary-list nhsuk-summary-list--no-last-row-border"
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Name
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
Karen Francis
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
name (Karen Francis)
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Appointment date
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
15 March 2027
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
date of birth (Karen Francis)
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Contact details
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
<
p
>
07700 900362
</
p
>
<
p
>
karen.francis@example.com
</
p
>
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
contact details (Karen Francis)
</
span
>
</
a
>
</
dd
>
</
div
>
</
dl
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
"nhsuk-card"
>
<
div
class
=
"nhsuk-card__heading-container"
>
<
h2
class
=
"nhsuk-card__heading nhsuk-heading-m"
>
Dwayne Harvey
</
h2
>
<
ul
class
=
"nhsuk-card__actions"
>
<
li
class
=
"nhsuk-card__action"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Cancel
<
span
class
=
"nhsuk-u-visually-hidden"
>
(Dwayne Harvey)
</
span
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
"nhsuk-card__action"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Reschedule
<
span
class
=
"nhsuk-u-visually-hidden"
>
(Dwayne Harvey)
</
span
>
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
<
div
class
=
"nhsuk-card__content"
>
<
dl
class
=
"nhsuk-summary-list nhsuk-summary-list--no-last-row-border"
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Name
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
Dwayne Harvey
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
name (Dwayne Harvey)
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Appointment date
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
15 March 2027
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
date of birth (Dwayne Harvey)
</
span
>
</
a
>
</
dd
>
</
div
>
<
div
class
=
"nhsuk-summary-list__row"
>
<
dt
class
=
"nhsuk-summary-list__key"
>
Contact details
</
dt
>
<
dd
class
=
"nhsuk-summary-list__value"
>
<
p
>
07964 850567
</
p
>
<
p
>
dwayne.harvey@example.com
</
p
>
</
dd
>
<
dd
class
=
"nhsuk-summary-list__actions"
>
<
a
class
=
"nhsuk-link"
href
=
"#"
>
Change
<
span
class
=
"nhsuk-u-visually-hidden"
>
contact details (Dwayne Harvey)
</
span
>
</
a
>
</
dd
>
</
div
>
</
dl
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
Name id | Type string | Description The ID of the summary list.
Name border | Type boolean | Description If set to false , remove separating borders from all rows.
Name last Row Border | Type boolean | Description If set to false , remove separating border from the last row.
Name rows | Type array | Description Required. The rows within the summary list component. See macro options for rows .
Name html | Type string | Description HTML to use within the summary list.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire summary list component in a call block.
Name card | Type object | Description Can be used to wrap a card around the summary list component. If any of these options are present, a card will wrap around the summary list. See macro options for card .
Name classes | Type string | Description Classes to add to the container.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the container.

Name | Type | Description
Name id | Type string | Description The ID of the row.
Name classes | Type string | Description Classes to add to the row.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the row.
Name border | Type boolean | Description If set to false , remove separating border from the row.
Name key | Type object | Description Required. The reference content (key) for each row item in the summary list component. See macro options for rows key .
Name value | Type object | Description Required. The value for each row item in the summary list component. See macro options for rows value .
Name actions | Type object | Description The action link content for each row item in the summary list component. See macro options for rows actions .

Name | Type | Description
Name id | Type string | Description The ID of the key item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each key. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each key. If html is provided, the text option will be ignored.
Name width | Type string | Description Specify the key wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the key wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the key wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the value item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each value. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each value. If html is provided, the text option will be ignored.
Name width | Type string | Description Specify the value wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the value wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the value wrapper.

Name | Type | Description
Name items | Type array | Description The action link items within the row item of the summary list component. See macro options for rows actions items .
Name width | Type string | Description Specify the actions wrapper width. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" .
Name classes | Type string | Description Classes to add to the actions wrapper.
Name attributes | Type string | Description HTML attributes (for example data attributes) to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If type is set, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If type is set, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"summary-list/macro.njk"
import
summaryList
%}
{{
summaryList
({
lastRowBorder
:
false
,
card
: {
heading
: {
text
:
"Karen Francis"
,
size
:
"m"
},
actions
: {
items
: [
        {
text
:
"Cancel"
,
href
:
"#"
},
        {
text
:
"Reschedule"
,
href
:
"#"
}
      ]
    }
  },
rows
: [
    {
key
: {
text
:
"Name"
},
value
: {
text
:
"Karen Francis"
},
actions
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
"Change"
,
visuallyHiddenText
:
"name"
}
        ]
      }
    },
    {
key
: {
text
:
"Appointment date"
},
value
: {
text
:
"15 March 2027"
},
actions
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
"Change"
,
visuallyHiddenText
:
"date of birth"
}
        ]
      }
    },
    {
key
: {
text
:
"Contact details"
},
value
: {
html
:
"<p>07700 900362</p><p>karen.francis@example.com</p>"
},
actions
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
"Change"
,
visuallyHiddenText
:
"contact details"
}
        ]
      }
    }
  ]
})
}}
{{
summaryList
({
lastRowBorder
:
false
,
card
: {
heading
: {
text
:
"Dwayne Harvey"
,
size
:
"m"
},
actions
: {
items
: [
        {
text
:
"Cancel"
,
href
:
"#"
},
        {
text
:
"Reschedule"
,
href
:
"#"
}
      ]
    }
  },
rows
: [
    {
key
: {
text
:
"Name"
},
value
: {
text
:
"Dwayne Harvey"
},
actions
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
"Change"
,
visuallyHiddenText
:
"name"
}
        ]
      }
    },
    {
key
: {
text
:
"Appointment date"
},
value
: {
text
:
"15 March 2027"
},
actions
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
"Change"
,
visuallyHiddenText
:
"date of birth"
}
        ]
      }
    },
    {
key
: {
text
:
"Contact details"
},
value
: {
html
:
"<p>07964 850567</p><p>dwayne.harvey@example.com</p>"
},
actions
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
"Change"
,
visuallyHiddenText
:
"contact details"
}
        ]
      }
    }
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
