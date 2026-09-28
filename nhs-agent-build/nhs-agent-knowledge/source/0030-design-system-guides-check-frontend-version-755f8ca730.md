# Check your frontend version – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/guides/check-frontend-version/

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

# Update guides – Check your frontend version

How to check which version of the NHS.UK frontend you are using and how to update.

## The frontend and the design system

The NHS.UK frontend codebase (in GitHub) contains the code used to create the design system components and styles.

When the design system is updated, for example with a new component, the frontend is updated too. If you're using an older version, for example with the NHS prototype kit , you cannot use the new component until you update your frontend version.

The current version of NHS.UK frontend is 10.6.1 .

Note: this guidance applies to the NHS prototype kit and production services. Community resources , such as the NHS Figma design library, are not based on the frontend code and are updated separately.

## How to check your NHS.UK frontend version

To check the version you are currently using, run npm list nhsuk-frontend on your project directory.

On Windows, you can run this with Command Prompt.

On a Mac, you can use the Terminal application.

You can also use the terminal in your code editor.

```text
$ npm list nhsuk-frontend
project@1.0.0 /path/to/your/project
└── nhsuk-frontend@10.0.0
```

If you are using a lower version than the latest version 10.6.1 , you will need to update to use the latest features.

## How to update your frontend

### Updating a prototype

If you are using the prototype kit, visit the updating the kit guide on the prototype kit website . When the frontend is released, we also update the NHS prototype kit to the latest version.

### Updating a production service

To update a production service or other code that uses the NHS.UK frontend, follow our guide to staying up to date on nhsuk-frontend (in GitHub) .

## Updates to this page

Updated: August 2026
