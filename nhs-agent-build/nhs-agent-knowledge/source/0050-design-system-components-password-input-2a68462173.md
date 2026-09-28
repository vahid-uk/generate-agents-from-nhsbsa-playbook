# Password input – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/password-input/

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

# Form elements – Password input

Help users to create and enter passwords.

- HTML code for password input

- Nunjucks code for password input

```text
<
div
class
=
"nhsuk-form-group nhsuk-password-input"
data-module
=
"nhsuk-password-input"
>
<
label
class
=
"nhsuk-label"
for
=
"example"
>
Password
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
"nhsuk-input nhsuk-password-input__input nhsuk-js-password-input-input"
id
=
"example"
name
=
"example"
type
=
"password"
spellcheck
=
"false"
autocomplete
=
"current-password"
autocapitalize
=
"none"
>
<
button
class
=
"nhsuk-button nhsuk-button--secondary nhsuk-button--small nhsuk-password-input__toggle nhsuk-js-password-input-toggle"
data-module
=
"nhsuk-button"
type
=
"button"
aria-label
=
"Show password"
aria-controls
=
"example"
hidden
>
Show
</
button
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
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. Options for the label component. See macro options for label .
Name hint | Type object | Description Options for the hint component. See macro options for hint .
Name error Message | Type object | Description Options for the error message component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the password input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the password input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the text input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the text input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose . See the Autofill section in the HTML standard for full list of attributes that can be used. Default is "current-password" .
Name input Wrapper | Type object | Description Additional options for the wrapping element containing the password input component. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.
Name show Password Text | Type string | Description Button text when the password is hidden. Defaults to "Show" .
Name hide Password Text | Type string | Description Button text when the password is visible. Defaults to "Hide" .
Name show Password Aria Label Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by showPasswordAriaLabel .
Name show Password Aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when the password is hidden. Defaults to "Show password" .
Name hide Password Aria Label Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by hidePasswordAriaLabel .
Name hide Password Aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when the password is visible. Defaults to "Hide password" .
Name password Shown Announcement Text | Type string | Description Announcement made to screen reader users when their password has become visible in plain text. Defaults to "Your password is visible" .
Name password Hidden Announcement Text | Type string | Description Announcement made to screen reader users when their password has been obscured and is not visible. Defaults to "Your password is hidden" .
Name button | Type object | Description Optional object allowing customisation of the toggle button. The button.attributes and button.html options are not supported. See button macro options using button component macro .

Name | Type | Description
Name text | Type string | Description Required. Required. If html is set, this is not required. Text to use within the prefix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. Required. If text is set, this is not required. HTML to use within the prefix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the prefix.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the prefix element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the suffix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the suffix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the suffix element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the suffix element.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the text input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the text input component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the wrapping element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the wrapping element.

Name | Type | Description
Name variant | Type string | Description Optional variant of password input button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name classes | Type string | Description Classes to add to the button.

Name | Type | Description
Name id | Type string | Description The ID of the label.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the label. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire label component in a call block.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the label.
Name caption | Type object | Description Optional caption for the label. See macro options for caption .
Name for | Type string | Description The label for attribute, the ID of the input the label is associated with.
Name heading | Type object | Description Whether the label also acts as a heading. See macro options for heading .
Name is Page Heading | Type boolean | Description Deprecated in 10.6.1 (see GitHub) . Replaced by the heading option.
Name size | Type string | Description Size of the label – "s" , "m" , "l" or "xl" .
Name classes | Type string | Description Classes to add to the label tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the label tag.

```text
{%
from
"password-input/macro.njk"
import
passwordInput
%}
{{
passwordInput
({
label
: {
text
:
"Password"
},
id
:
"example"
,
name
:
"example"
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

## When to use password input

Use this component whenever you need users to create or enter a password.

Before using this component, read:

- the National Cyber Security Centre (NCSC) guidance on password administration for system owners (including their password policy ) and NHS England's multi-factor authentication (MFA) policy

- about using NHS login and Care Identity Service (NHS England) for authentication

## When not to use password input

Do not use this component to ask for any information other than a password.

Use a text input component to ask for other security information, such as:

- multi-factor authentication codes

- answers to security questions

- other personally identifiable information

Also see GOV.UK's Confirm a phone number pattern .

## How to use password input

This component lets users enter a password, with an option to show what they've entered as plain text.

This allows users to visually check their password before they submit it, which helps them reduce errors and choose passwords that are more unique and secure.

Use this guidance with GOV.UK's Ask users for passwords pattern , which explains how to help users create and enter secure and memorable passwords.

### Error messages

- HTML code for password input error

- Nunjucks code for password input error

```text
<
div
class
=
"nhsuk-form-group nhsuk-form-group--error nhsuk-password-input"
data-module
=
"nhsuk-password-input"
>
<
label
class
=
"nhsuk-label"
for
=
"example"
>
Password
</
label
>
<
span
class
=
"nhsuk-error-message"
id
=
"example-error"
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
Enter a password
</
span
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
"nhsuk-input nhsuk-input--error nhsuk-password-input__input nhsuk-js-password-input-input"
id
=
"example"
name
=
"example"
type
=
"password"
spellcheck
=
"false"
aria-describedby
=
"example-error"
autocomplete
=
"current-password"
autocapitalize
=
"none"
>
<
button
class
=
"nhsuk-button nhsuk-button--secondary nhsuk-button--small nhsuk-password-input__toggle nhsuk-js-password-input-toggle"
data-module
=
"nhsuk-button"
type
=
"button"
aria-label
=
"Show password"
aria-controls
=
"example"
hidden
>
Show
</
button
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
Name id | Type string | Description The ID of the input. Defaults to the value of name .
Name name | Type string | Description Required. The name of the input, which is submitted with the form data.
Name value | Type string | Description Optional initial value of the input.
Name disabled | Type boolean | Description If true , input will be disabled.
Name described By | Type string | Description One or more element IDs to add to the aria-describedby attribute, used to provide additional descriptive information for screenreader users.
Name label | Type object | Description Required. Options for the label component. See macro options for label .
Name hint | Type object | Description Options for the hint component. See macro options for hint .
Name error Message | Type object | Description Options for the error message component. The error message component will not display if you use a falsy value for errorMessage , for example false or null . See macro options for error Message .
Name prefix | Type object | Description Can be used to add a prefix to the password input component. See macro options for prefix .
Name suffix | Type object | Description Can be used to add a suffix to the password input component. See macro options for suffix .
Name code | Type boolean | Description If set to true , use a monospace font for codes or sequences.
Name width | Type integer | Description Optional fixed width for the text input component – 2 , 3 , 4 , 5 , 10 , 20 or 30 .
Name large | Type boolean | Description If set to true , larger input size will be used.
Name form Group | Type object | Description Additional options for the form group containing the text input component. See macro options for form Group .
Name classes | Type string | Description Classes to add to the input.
Name autocomplete | Type string | Description Attribute to meet WCAG success criterion 1.3.5: Identify input purpose . See the Autofill section in the HTML standard for full list of attributes that can be used. Default is "current-password" .
Name input Wrapper | Type object | Description Additional options for the wrapping element containing the password input component. See macro options for input Wrapper .
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the input.
Name show Password Text | Type string | Description Button text when the password is hidden. Defaults to "Show" .
Name hide Password Text | Type string | Description Button text when the password is visible. Defaults to "Hide" .
Name show Password Aria Label Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by showPasswordAriaLabel .
Name show Password Aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when the password is hidden. Defaults to "Show password" .
Name hide Password Aria Label Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by hidePasswordAriaLabel .
Name hide Password Aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when the password is visible. Defaults to "Hide password" .
Name password Shown Announcement Text | Type string | Description Announcement made to screen reader users when their password has become visible in plain text. Defaults to "Your password is visible" .
Name password Hidden Announcement Text | Type string | Description Announcement made to screen reader users when their password has been obscured and is not visible. Defaults to "Your password is hidden" .
Name button | Type object | Description Optional object allowing customisation of the toggle button. The button.attributes and button.html options are not supported. See button macro options using button component macro .

Name | Type | Description
Name text | Type string | Description Required. Required. If html is set, this is not required. Text to use within the prefix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. Required. If text is set, this is not required. HTML to use within the prefix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the prefix.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the prefix element.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the suffix. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the suffix. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the suffix element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the suffix element.

Name | Type | Description
Name classes | Type string | Description Classes to add to the form group (for example to show error state for the whole group).
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the form group.
Name before Input | Type object | Description Content to add before the input used by the text input component. See macro options for form Group before Input .
Name after Input | Type object | Description Content to add after the input used by the text input component. See macro options for form Group after Input .

Name | Type | Description
Name text | Type string | Description Required. Text to add before the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add before the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name text | Type string | Description Required. Text to add after the input. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add after the input. If html is provided, the text option will be ignored.

Name | Type | Description
Name classes | Type string | Description Classes to add to the wrapping element.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the wrapping element.

Name | Type | Description
Name variant | Type string | Description Optional variant of password input button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name classes | Type string | Description Classes to add to the button.

Name | Type | Description
Name id | Type string | Description The ID of the label.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the label. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the label. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire label component in a call block.
Name visually Hidden Text | Type string | Description A visually hidden suffix added to the label.
Name caption | Type object | Description Optional caption for the label. See macro options for caption .
Name for | Type string | Description The label for attribute, the ID of the input the label is associated with.
Name heading | Type object | Description Whether the label also acts as a heading. See macro options for heading .
Name is Page Heading | Type boolean | Description Deprecated in 10.6.1 (see GitHub) . Replaced by the heading option.
Name size | Type string | Description Size of the label – "s" , "m" , "l" or "xl" .
Name classes | Type string | Description Classes to add to the label tag.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the label tag.

```text
{%
from
"password-input/macro.njk"
import
passwordInput
%}
{{
passwordInput
({
label
: {
text
:
"Password"
},
errorMessage
: {
text
:
"Enter a password"
},
id
:
"example"
,
name
:
"example"
})
}}
```

Requires NHS.UK frontend 10.6.1 – check your version of NHS.UK frontend

If the user enters their account details incorrectly, do not reveal whether they got the username or password wrong. Clear any information entered into the password input.

Revealing the source of the error can help fraudsters break into people's accounts.

See how to handle incorrect login attempts and help users who forget their password in GOV.UK's Ask users for passwords pattern .

### Showing and hiding passwords

Hide the password by default until the user chooses to show it using the "Show" button. Users might not be in a private space when entering or creating a password, so hide passwords by default.

If you do choose to include 2 or more password inputs on a page, the "Show" and "Hide" toggles and labels for each password input must be different.

For example, you can label:

- the 1st input as "Password" with a toggle of "Show password"

- the 2nd input as "Re-enter password" with a toggle of "Show re-entered password"

### Avoid adding a "confirm password" field

It's not necessary to add a 2nd password field, also known as a "confirm password" field, particularly as this component allows users to show and hide passwords.

### Define the input's type as "password"

If the form is submitted when the input's text is visible, JavaScript will change the input type back to password . You must check this happens automatically.

This is to prevent browsers from remembering it as a value the user has entered before and potentially displaying it as an autofill option on non-password inputs.

### Use the autocomplete attribute

Use the autocomplete attribute on password inputs to help users complete forms faster.

Autocomplete indicates to browsers and password managers what kind of password is needed so it can be entered for the user.

Set the autocomplete attribute to new-password if the user is creating a password. Otherwise, use current-password .

Many browsers will autofill password inputs, even when the autocomplete attribute is missing or set to off .

### Allow copy and paste

The NCSC recommends that online services let people:

- use password managers

- copy and paste passwords

#### Copying text from password fields

Users can copy any text from a password field when it's set on "Show". This is a feature of browser behaviour and cannot be overridden.

This can be useful for users, for example to save a password that the browser has suggested into a separate password manager.

### Avoid restricting the user's input

Support all the characters users may need to enter a password, including numbers and symbols.

Set a minimum length of at least 12 characters.

If you need to set a maximum password length on the server to prevent buffer overflow attacks without discouraging strong passwords, allow at least 64 characters.

The NCSC password policy includes advice on technical solutions and reducing the burden on users.

Any restrictions must be identical wherever the user creates or enters a password. If you change the restrictions over time, you must continue to support existing user passwords or ask them to set a new one.

#### Do not use maxlength to restrict password length

Users will not get any feedback when they've reached the maxlength and their text input has been truncated. This happens when a user has pasted text from elsewhere or it's been autofilled by a password manager.

If a user exceeds the maximum length, show an error message instead. See GOV.UK's pattern for helping users to recover from validation errors .

### Do not spell-check or autocapitalise the user's input

Some browsers might automatically change what the user is typing when the input's text is visible, such as correcting spelling or automatically turning on upper case letters at the start of sentences.

You can tell browsers not to correct spellings by setting the spellcheck attribute to false .

Doing this can avoid making your service vulnerable to "spell-jacking" , where some spell-checking tools gather personal identifiable information, even user's passwords, from password input fields to send to third party services.

You can tell browsers not to autocapitalise values by setting the autocapitalize attribute to off .

### Known issues

Some apps and tools add their own native functionality to show and hide passwords.

These tools include:

- browsers (particularly when suggesting new passwords)

- password managers

- screen readers

We've tried to minimise duplicate functionality by hiding other types of "Show password" button where possible.

There are also other instances where a password could be shown or hidden without the use of a button, causing a mismatch with the button label. In other words, the user would see a button to show a password that's already visible.

GOV.UK found this mismatch happens in some browsers when:

- a keyboard shortcut is pressed

- a suggested password is created

## Accessibility

Follow WCAG 2.2 on accessible authentication (W3C) .

## Progressive enhancement

The password input component uses progressive enhancement and requires JavaScript for enhanced functionality.

When JavaScript is not available, users will see their browser's native password input without the "Show" button.

## Research on this component

GOV.UK decided that having a 2nd field is not helpful for users, particularly on password inputs with show and hide buttons.

We would like to see real-life examples from service teams and get your feedback.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
