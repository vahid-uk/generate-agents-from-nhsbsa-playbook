# Task list – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/task-list/

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

# Content presentation – Task list

Use the task list to give users more control over how they complete long, complex services.

The task list component displays all the tasks a user needs to do, and allows users to easily identify which ones are done and which they still need to do.

- HTML code for task list

- Nunjucks code for task list

```text
<
ul
class
=
"nhsuk-task-list"
>
<
li
class
=
"nhsuk-task-list__item nhsuk-task-list__item--with-link"
>
<
div
class
=
"nhsuk-task-list__name-and-hint"
>
<
a
class
=
"nhsuk-task-list__link nhsuk-link"
href
=
"#"
aria-describedby
=
"your-health-1-status"
>
Exercise
</
a
>
</
div
>
<
div
class
=
"nhsuk-task-list__status nhsuk-task-list__status--completed"
id
=
"your-health-1-status"
>
Completed
</
div
>
</
li
>
<
li
class
=
"nhsuk-task-list__item nhsuk-task-list__item--with-link"
>
<
div
class
=
"nhsuk-task-list__name-and-hint"
>
<
a
class
=
"nhsuk-task-list__link nhsuk-link"
href
=
"#"
aria-describedby
=
"your-health-2-status"
>
Personal health
</
a
>
</
div
>
<
div
class
=
"nhsuk-task-list__status nhsuk-task-list__status--completed"
id
=
"your-health-2-status"
>
Completed
</
div
>
</
li
>
<
li
class
=
"nhsuk-task-list__item nhsuk-task-list__item--with-link"
>
<
div
class
=
"nhsuk-task-list__name-and-hint"
>
<
a
class
=
"nhsuk-task-list__link nhsuk-link"
href
=
"#"
aria-describedby
=
"your-health-3-hint your-health-3-status"
>
Family health history
</
a
>
<
div
class
=
"nhsuk-task-list__hint"
id
=
"your-health-3-hint"
>
Details of your parents, brothers and sisters
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
"nhsuk-task-list__status"
id
=
"your-health-3-status"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--blue"
>
Incomplete
</
strong
>
</
div
>
</
li
>
<
li
class
=
"nhsuk-task-list__item nhsuk-task-list__item--with-link"
>
<
div
class
=
"nhsuk-task-list__name-and-hint"
>
<
a
class
=
"nhsuk-task-list__link nhsuk-link"
href
=
"#"
aria-describedby
=
"your-health-4-status"
>
Smoking history
</
a
>
</
div
>
<
div
class
=
"nhsuk-task-list__status"
id
=
"your-health-4-status"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--blue"
>
Incomplete
</
strong
>
</
div
>
</
li
>
<
li
class
=
"nhsuk-task-list__item"
>
<
div
class
=
"nhsuk-task-list__name-and-hint"
>
<
div
>
Blood test
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
"nhsuk-task-list__status nhsuk-task-list__status--cannot-start-yet"
id
=
"your-health-5-status"
>
Cannot start yet
</
div
>
</
li
>
</
ul
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the task list.
Name classes | Type string | Description Classes to add to the ul container for the task list.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the ul container for the task list.
Name id Prefix | Type string | Description Optional prefix. This is used to prefix the id attribute for the task list item tag and hint, separated by "-" . Defaults to "task-list" .
Name items | Type array | Description Required. The items for each task within the task list component. See macro options for items .

Name | Type | Description
Name title | Type object | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the item.heading option.
Name heading | Type object | Description Required. The main heading for the task within the task list component. See macro options for items heading .
Name hint | Type object | Description Can be used to add a hint to each task within the task list component. See macro options for items hint .
Name status | Type object | Description Required. The status for each task within the task list component. See macro options for items status .
Name href | Type string | Description The value of the link's href attribute for the task list item.
Name classes | Type string | Description Classes to add to the item div .

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the heading.
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name text | Type string | Description Required. Text to use within the hint. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to use within the hint. If html is provided, the text option will be ignored.

Name | Type | Description
Name tag | Type object | Description Can be used to add a tag to the status of the task within the task list component. See macro options for tag .
Name text | Type string | Description Text to use for the status, as an alternative to using a tag. If html or tag is provided, the text option will be ignored.
Name html | Type string | Description HTML to use for the status, as an alternative to using a tag. If html or tag is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the status container.

```text
{%
from
"task-list/macro.njk"
import
taskList
%}
{{
taskList
({
idPrefix
:
"your-health"
,
items
: [
    {
heading
: {
text
:
"Exercise"
},
href
:
"#"
,
status
: {
text
:
"Completed"
,
classes
:
"nhsuk-task-list__status--completed"
}
    },
    {
heading
: {
text
:
"Personal health"
},
href
:
"#"
,
status
: {
text
:
"Completed"
,
classes
:
"nhsuk-task-list__status--completed"
}
    },
    {
heading
: {
text
:
"Family health history"
},
hint
: {
text
:
"Details of your parents, brothers and sisters"
},
href
:
"#"
,
status
: {
tag
: {
text
:
"Incomplete"
,
colour
:
"blue"
}
      }
    },
    {
heading
: {
text
:
"Smoking history"
},
href
:
"#"
,
status
: {
tag
: {
text
:
"Incomplete"
,
colour
:
"blue"
}
      }
    },
    {
heading
: {
text
:
"Blood test"
},
status
: {
text
:
"Cannot start yet"
,
classes
:
"nhsuk-task-list__status--cannot-start-yet"
}
    }
  ]
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## When to use the task list

If your users have to get through a long or complex service, use the task list to give them more control. For example, if some users cannot complete the tasks in one sitting.

You can also use a task list to allow users to complete tasks in the order they choose. This will help them plan their time and complete sections as and when they can.

## When not to use the task list

Try to simplify the service before you use a task list. If you're able to reduce the number of tasks or steps involved, you might not need one.

Do not use the task list as a way of showing users their answers. For this, use a summary list instead.

## How the task list works

Where possible, let users complete tasks in whatever order they like.

The status alongside the task indicates whether they can start it. Users can select a task to start completing it. Once they have completed it and returned to the task list, the status for that task will have changed to "Completed".

Users can only move on from the task list when all tasks are shown as "Completed".

Find more information about how to use the task list in a service in the complete multiple tasks pattern guidance .

### Tasks

Tasks are usually actions that the user needs to take to complete a service.

Each task in a task list includes a task name and a status. It can also include hint text if you decide this is needed.

The whole row turns grey on hover to show that it is linked, allowing users to select anywhere in it to start the task.

#### Write clear task descriptions

The task name gives users a reasonable expectation of what that task is about. For example, "Your contact details" or "Upload evidence". Use sentence case and keep it short. Users of screen readers might find it difficult to navigate the task list if the task names are too long.

If you're finding it difficult to come up with a clear and concise task name, it might be because the task itself is too complex and may need to be separated into smaller tasks. Group questions and actions into tasks in a way that makes sense to users, based on their needs.

#### Adding hint text

Only use hint text if there is evidence that the user needs more information about what the task will include.

Keep hint text to a single, short sentence. Screen readers read out the entire text when users interact with the task link. This could frustrate users if the text is long.

Do not include links in the hint text. The whole task row links users to the task itself, so any links in the hint text will not work.

#### Grouping tasks

If there are a lot of tasks to complete, you might find that grouping them makes it easier for users to understand and plan what they need to do. Tasks can be grouped into separate task lists on a page. Give each task list a short heading that clearly explains the grouping.

Find more information on grouping tasks in the complete multiple tasks pattern guidance .

### Statuses

Statuses use colour and a short descriptor to give users a quick overview of how much of the task list they have completed, and how much is left to do.

Find more information on how to show statuses in the complete multiple tasks pattern guidance .

## Research on the task list

The GOV.UK design system developed and tested this component. Find out more about their research on the GOV.UK task list page .

If you are using this component in a service, we would like to hear about any user research so that we can identify any potential issues.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: November 2024
