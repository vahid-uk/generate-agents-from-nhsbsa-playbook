# Complete multiple tasks – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/patterns/complete-multiple-tasks/

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

# Help users to – Complete multiple tasks

Use this pattern to give users more control over how they complete long, complex services.

Help users understand:

- the tasks involved in completing a transaction

- whether they've completed tasks

- HTML code for complete multiple tasks example

- Nunjucks code for complete multiple tasks example

```text
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
Service name
</
h1
>
<
h2
class
=
"nhsuk-heading-m"
>
Your details
</
h2
>
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
"your-details-1-status"
>
Name
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
"your-details-1-status"
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
"your-details-2-status"
>
Contact details
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
"your-details-2-status"
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
</
ul
>
<
h2
class
=
"nhsuk-heading-m"
>
Your health
</
h2
>
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
Physical activity
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
"your-health-2-status"
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
"your-health-3-status"
>
Vaccination history
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
"your-health-3-status"
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
"your-health-4-status"
>
Alcohol use
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
"your-health-5-status"
>
Body measurements
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
"your-health-5-status"
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
</
ul
>
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
Send
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
main
>
</
div
>
```

```text
{%
from
"button/macro.njk"
import
button
%}
{%
from
"task-list/macro.njk"
import
taskList
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
Service name
</
h1
>
<
h2
class
=
"nhsuk-heading-m"
>
Your details
</
h2
>
{{
taskList
({
idPrefix
:
"your-details"
,
items
: [
          {
heading
: {
text
:
"Name"
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
"Contact details"
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
          }
        ]
      })
}}
<
h2
class
=
"nhsuk-heading-m"
>
Your health
</
h2
>
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
"Physical activity"
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
"Vaccination history"
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
"Alcohol use"
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
"Body measurements"
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
          }
        ]
      })
}}
{{
button
({
text
:
"Send"
})
}}
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

This pattern uses a task list component for each group of tasks on the page.

## When to use this pattern

If your users have to get through a long or complex service, use the complete multiple tasks page to give them more control. For example, if some users cannot complete the tasks in one sitting.

## When not to use this pattern

Try to simplify the service before you use a complete multiple tasks page. If you're able to reduce the number of tasks or steps involved, you might not need one.

Do not use the complete multiple tasks page as a way of showing users their answers. For this, use a summary list instead.

## How this pattern works

Show a complete multiple tasks page:

- at the start of the transaction

- at the start of each returning session

If you use a complete multiple tasks page in your service, you'll need to:

- group related actions into tasks

- show the status of the tasks

If there are lots of tasks to complete, you might also need to group tasks together.

### Show related actions as a task

Summarise a set of related activities and questions into a task, for example, "Give medical information". This will help users understand and plan what they need to do.

### Show the status of the tasks

Make it clear to users which tasks they have completed and which still need their attention, by labelling them using statuses.

- HTML code for complete multiple tasks task list statuses

- Nunjucks code for complete multiple tasks task list statuses

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
"your-health-2-hint your-health-2-status"
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
"your-health-2-hint"
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
"your-health-2-status"
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
"your-health-3-status"
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
</
ul
>
```

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
    }
  ]
})
}}
```

Start with the smallest number of different statuses you think might work, for example "Completed" and "Incomplete", then add more if your user research shows there's a need for them. The more you add, the harder it is for users to remember them.

Once the user has completed the task, show the status as "Completed" in black text with no background colour. This will draw more attention to tasks that require action.

#### Tasks that are in progress

You may find you need additional statuses if your user research shows that users want to be able to distinguish between the tasks they have not started at all, and those they've started but not completed.

In this instance, instead of "Incomplete", you may want to use "Not yet started" to show which tasks they are yet to start. Use "In progress" for tasks they have started but are yet to complete.

"Not yet started" uses a light blue background, and "In progress" uses a white background.

- HTML code for complete multiple tasks in progress

- Nunjucks code for complete multiple tasks in progress

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
Contact details
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
"your-health-2-hint your-health-2-status"
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
"your-health-2-hint"
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
"your-health-2-status"
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
"your-health-3-status"
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
"your-health-3-status"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--blue"
>
Not yet started
</
strong
>
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
"Contact details"
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
"In progress"
,
colour
:
"white"
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
"Not yet started"
,
colour
:
"blue"
}
      }
    }
  ]
})
}}
```

#### Tasks that cannot yet be started

If the user cannot start the task yet, for example because another task must be completed first, use the "Cannot start yet" status. Use grey text with no background colour, and do not link the "task row".

- HTML code for complete multiple tasks cannot start yet

- Nunjucks code for complete multiple tasks cannot start yet

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
"your-health-2-hint your-health-2-status"
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
"your-health-2-hint"
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
"your-health-2-status"
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
<
div
class
=
"nhsuk-task-list__hint"
id
=
"your-health-3-hint"
>
Complete family health history first
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
"your-health-3-status"
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
"Blood test"
},
hint
: {
text
:
"Complete family health history first"
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

#### Tasks containing an error

Avoid tasks having an error status by using the error summary and error messages displayed at the point that the error is made, so that the user can fix it straight away.

If it is unavoidable that a task may end up saved but containing an error, use the status text "There is a problem" and a red background.

Do not use the red background colour for any status text except errors.

- HTML code for complete multiple tasks error

- Nunjucks code for complete multiple tasks error

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
"your-health-2-hint your-health-2-status"
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
"your-health-2-hint"
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
"your-health-2-status"
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
"your-health-3-status"
>
Vaccination history
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
"your-health-3-status"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--red"
>
There is a problem
</
strong
>
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
"Vaccination history"
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
"There is a problem"
,
colour
:
"red"
}
      }
    }
  ]
})
}}
```

#### Status text

Although we recommend using consistent wording across task lists, you can change it if research shows that different text is more suitable to your service or users.

If you are creating your own statuses, use adjectives rather than verbs. Use sentence case and keep it short, so that it can be easily read and understood.

#### Additional statuses

If your user research shows that there is a need for additional status tags, you can use other colours to help distinguish between them.

- HTML code for complete multiple tasks all colours

- Nunjucks code for complete multiple tasks all colours

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
"all-colours-1-status"
>
Task A
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
"all-colours-1-status"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--white"
>
White
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
"all-colours-2-status"
>
Task B
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
"all-colours-2-status"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--grey"
>
Grey
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
"all-colours-3-status"
>
Task C
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
"all-colours-3-status"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--green"
>
Green
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
"all-colours-4-status"
>
Task D
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
"all-colours-4-status"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--aqua-green"
>
Aqua green
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
"all-colours-5-status"
>
Task E
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
"all-colours-5-status"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--blue"
>
Blue
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
"all-colours-6-status"
>
Task F
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
"all-colours-6-status"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--purple"
>
Purple
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
"all-colours-7-status"
>
Task G
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
"all-colours-7-status"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--pink"
>
Pink
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
"all-colours-8-status"
>
Task H
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
"all-colours-8-status"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--orange"
>
Orange
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
"all-colours-9-status"
>
Task I
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
"all-colours-9-status"
>
<
strong
class
=
"nhsuk-tag nhsuk-tag--yellow"
>
Yellow
</
strong
>
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
"all-colours"
,
items
: [
    {
heading
: {
text
:
"Task A"
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
"White"
,
colour
:
"white"
}
      }
    },
    {
heading
: {
text
:
"Task B"
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
"Grey"
,
colour
:
"grey"
}
      }
    },
    {
heading
: {
text
:
"Task C"
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
"Green"
,
colour
:
"green"
}
      }
    },
    {
heading
: {
text
:
"Task D"
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
"Aqua green"
,
colour
:
"aqua-green"
}
      }
    },
    {
heading
: {
text
:
"Task E"
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
"Blue"
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
"Task F"
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
"Purple"
,
colour
:
"purple"
}
      }
    },
    {
heading
: {
text
:
"Task G"
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
"Pink"
,
colour
:
"pink"
}
      }
    },
    {
heading
: {
text
:
"Task H"
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
"Orange"
,
colour
:
"orange"
}
      }
    },
    {
heading
: {
text
:
"Task I"
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
"Yellow"
,
colour
:
"yellow"
}
      }
    }
  ]
})
}}
```

### Group related tasks together

If your transaction involves lots of tasks, make it manageable by grouping them.

For example, you could group all tasks which ask for related information under a heading, such as "Your details".

Where possible, allow users to complete tasks in any order. This will help them plan their time and complete sections as and when they can.

### Marking tasks as completed

Sometimes, it's better to let the user decide when a task is completed.

This can be helpful when a task involves:

- some questions that are optional

- writing a long answer (such as in a textarea )

- looking up information, such as details about previous jobs

- answers that need to be checked carefully with someone else

Do this by asking a radio question at the end of the task. If the task is on:

- a single page, do it as the last question

- on multiple question pages, do it on a check answers page

Ask "Have you completed this section?" with the radio options "Yes, I've completed this section" or "No, I'll come back later".

If the user selects "No, I'll come back to it later", mark the task as "Incomplete" or "In progress".

If the user selects "Yes, I've completed this section", mark the task as "Completed".

- HTML code for complete multiple tasks have you completed this section

- Nunjucks code for complete multiple tasks have you completed this section

```text
<
div
class
=
"nhsuk-form-group"
>
<
fieldset
class
=
"nhsuk-fieldset"
>
<
legend
class
=
"nhsuk-fieldset__legend nhsuk-fieldset__legend--m"
>
Have you completed this section?
</
legend
>
<
div
class
=
"nhsuk-radios"
data-module
=
"nhsuk-radios"
>
<
div
class
=
"nhsuk-radios__item"
>
<
input
class
=
"nhsuk-radios__input"
id
=
"haveYouCompletedThisSection"
name
=
"haveYouCompletedThisSection"
type
=
"radio"
value
=
"yes"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"haveYouCompletedThisSection"
>
Yes, I
&#39;
ve completed this section
</
label
>
</
div
>
<
div
class
=
"nhsuk-radios__item"
>
<
input
class
=
"nhsuk-radios__input"
id
=
"haveYouCompletedThisSection-2"
name
=
"haveYouCompletedThisSection"
type
=
"radio"
value
=
"no"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"haveYouCompletedThisSection-2"
>
No, I
&#39;
ll come back to it later
</
label
>
</
div
>
</
div
>
</
fieldset
>
</
div
>
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

```text
{%
from
"button/macro.njk"
import
button
%}
{%
from
"radios/macro.njk"
import
radios
%}
{{
radios
({
fieldset
: {
legend
: {
text
:
"Have you completed this section?"
,
isPageHeading
:
false
,
size
:
"m"
}
  },
name
:
"haveYouCompletedThisSection"
,
items
: [
    {
value
:
"yes"
,
text
:
"Yes, I've completed this section"
},
    {
value
:
"no"
,
text
:
"No, I'll come back to it later"
}
  ]
})
}}
{{
button
({
text
:
"Continue"
})
}}
```

Always allow users to go back into a task to change their answer, make sure information they have already entered is pre-populated.

#### Error messages

If the user does not select an option, show an error message to say: "Select whether you've completed this section".

- HTML code for complete multiple tasks have you completed this section error

- Nunjucks code for complete multiple tasks have you completed this section error

```text
<
div
class
=
"nhsuk-form-group nhsuk-form-group--error"
>
<
fieldset
class
=
"nhsuk-fieldset"
aria-describedby
=
"haveYouCompletedThisSection-error"
>
<
legend
class
=
"nhsuk-fieldset__legend nhsuk-fieldset__legend--m"
>
Have you completed this section?
</
legend
>
<
span
class
=
"nhsuk-error-message"
id
=
"haveYouCompletedThisSection-error"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Error:
</
span
>
Select whether you
&#39;
ve completed this section
</
span
>
<
div
class
=
"nhsuk-radios"
data-module
=
"nhsuk-radios"
>
<
div
class
=
"nhsuk-radios__item"
>
<
input
class
=
"nhsuk-radios__input"
id
=
"haveYouCompletedThisSection"
name
=
"haveYouCompletedThisSection"
type
=
"radio"
value
=
"yes"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"haveYouCompletedThisSection"
>
Yes, I
&#39;
ve completed this section
</
label
>
</
div
>
<
div
class
=
"nhsuk-radios__item"
>
<
input
class
=
"nhsuk-radios__input"
id
=
"haveYouCompletedThisSection-2"
name
=
"haveYouCompletedThisSection"
type
=
"radio"
value
=
"no"
>
<
label
class
=
"nhsuk-label nhsuk-radios__label"
for
=
"haveYouCompletedThisSection-2"
>
No, I
&#39;
ll come back to it later
</
label
>
</
div
>
</
div
>
</
fieldset
>
</
div
>
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

```text
{%
from
"button/macro.njk"
import
button
%}
{%
from
"radios/macro.njk"
import
radios
%}
{{
radios
({
fieldset
: {
legend
: {
text
:
"Have you completed this section?"
,
size
:
"m"
,
isPageHeading
:
false
}
  },
errorMessage
: {
text
:
"Select whether you've completed this section"
},
name
:
"haveYouCompletedThisSection"
,
items
: [
    {
value
:
"yes"
,
text
:
"Yes, I've completed this section"
},
    {
value
:
"no"
,
text
:
"No, I'll come back to it later"
}
  ]
})
}}
{{
button
({
text
:
"Continue"
})
}}
```

## Research on this pattern

This pattern is based on the pattern in the GOV.UK design system.

Find out about the GOV.UK research on the task list component page , including known issues and gaps.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
