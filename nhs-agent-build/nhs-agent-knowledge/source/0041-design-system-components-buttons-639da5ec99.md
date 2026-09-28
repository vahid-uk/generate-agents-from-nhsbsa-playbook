# Buttons – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/buttons/

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

# Form elements – Buttons

Use buttons to help users carry out an action on a page like starting an application or saving their progress.

## When to use buttons

Use buttons to start transactional journeys and carry out actions, like saving information.

## When not to use buttons

Do not use buttons as links: to pages which are not part of your user journey from 1 flat content page to another to external websites Try not to have multiple buttons on a page. Follow GOV.UK guidance on structuring forms and starting with one thing per page . How to use buttons We have 5 kinds of button: primary buttons secondary buttons warning buttons smaller buttons disabled buttons Align the primary action button to the left edge of your form. On smaller screens, such as on mobile, buttons stretch across the screen's width. This makes them easier to press for users holding a phone in their right hand. Do not decrease the height of buttons to less than our smaller buttons . Primary buttons There are 2 versions of the primary button: the default version and the reverse version. Open this example in a new tab : buttons HTML code for buttons Nunjucks code for buttons HTML code for buttons Copy code < button class = "nhsuk-button" data-module = "nhsuk-button" type = "submit" > Continue </ button > Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons Nunjucks code for buttons Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the button. Name element Type string Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided. Name text Type string Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored. Name html Type string Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block. Name name Type string Description Name for the button. If href is provided, this has no effect. Name type Type string Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The button value attribute. If href is provided, this has no effect. Name disabled Type boolean Description Whether the button should be disabled. If href is provided, this has no effect. Name href Type string Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided. Name variant Type string Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" . Name small Type boolean Description If set to true , smaller button size will be used. Name classes Type string Description Classes to add to the button. Name attributes Type object Description HTML attributes (for example data attributes) to add to the button. Name aria Label Type string Description Button text exposed to assistive technologies, like screen readers, when only an icon is used. Name prevent Double Click Type boolean Description Prevent accidental double clicks on submit buttons from submitting forms multiple times. Name icon Type object Description Can be used to add an icon to the button. See macro options for icon . Options for icon object Name Type Description Name name Type string Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" . Name html Type string Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored. Name placement Type string Description Required. Placement of the icon within the button – "start" or "end" . Copy code {% from "button/macro.njk" import button %} {{ button ({ text : "Continue" }) }} Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons When to use a primary button Use a primary button for the main call to action on a page, for example to help users start an application or save their progress. Use only 1 primary button on a page. Having more than 1 reduces their impact and makes it harder for users to know what to do next. Primary buttons on dark backgrounds To show a white button on dark backgrounds, add the variant: "reverse" option using Nunjucks. For HTML add the nhsuk-button--reverse class to the button. Make sure all users can see the button. The background colour must have a contrast ratio of at least 3:1 with white to meet WCAG 2.2 success criterion 1.4.11 Non-text Contrast, level AA (W3C) . Open this example in a new tab : buttons reverse HTML code for buttons reverse Nunjucks code for buttons reverse HTML code for buttons reverse Copy code < button class = "nhsuk-button nhsuk-button--reverse" data-module = "nhsuk-button" type = "submit" > Continue </ button > Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons reverse Nunjucks code for buttons reverse Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the button. Name element Type string Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided. Name text Type string Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored. Name html Type string Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block. Name name Type string Description Name for the button. If href is provided, this has no effect. Name type Type string Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The button value attribute. If href is provided, this has no effect. Name disabled Type boolean Description Whether the button should be disabled. If href is provided, this has no effect. Name href Type string Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided. Name variant Type string Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" . Name small Type boolean Description If set to true , smaller button size will be used. Name classes Type string Description Classes to add to the button. Name attributes Type object Description HTML attributes (for example data attributes) to add to the button. Name aria Label Type string Description Button text exposed to assistive technologies, like screen readers, when only an icon is used. Name prevent Double Click Type boolean Description Prevent accidental double clicks on submit buttons from submitting forms multiple times. Name icon Type object Description Can be used to add an icon to the button. See macro options for icon . Options for icon object Name Type Description Name name Type string Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" . Name html Type string Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored. Name placement Type string Description Required. Placement of the icon within the button – "start" or "end" . Copy code {% from "button/macro.njk" import button %} {{ button ({ text : "Continue" , variant : "reverse" }) }} Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons reverse Secondary buttons There are 2 versions of the secondary button. By default, the secondary button is transparent and has no colour. Use it on the page background colour ( nhsuk-colour("grey-5") ). Open this example in a new tab : buttons secondary HTML code for buttons secondary Nunjucks code for buttons secondary HTML code for buttons secondary Copy code < button class = "nhsuk-button nhsuk-button--secondary" data-module = "nhsuk-button" type = "submit" > Find my location </ button > Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons secondary Nunjucks code for buttons secondary Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the button. Name element Type string Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided. Name text Type string Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored. Name html Type string Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block. Name name Type string Description Name for the button. If href is provided, this has no effect. Name type Type string Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The button value attribute. If href is provided, this has no effect. Name disabled Type boolean Description Whether the button should be disabled. If href is provided, this has no effect. Name href Type string Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided. Name variant Type string Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" . Name small Type boolean Description If set to true , smaller button size will be used. Name classes Type string Description Classes to add to the button. Name attributes Type object Description HTML attributes (for example data attributes) to add to the button. Name aria Label Type string Description Button text exposed to assistive technologies, like screen readers, when only an icon is used. Name prevent Double Click Type boolean Description Prevent accidental double clicks on submit buttons from submitting forms multiple times. Name icon Type object Description Can be used to add an icon to the button. See macro options for icon . Options for icon object Name Type Description Name name Type string Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" . Name html Type string Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored. Name placement Type string Description Required. Placement of the icon within the button – "start" or "end" . Copy code {% from "button/macro.njk" import button %} {{ button ({ text : "Find my location" , variant : "secondary" }) }} Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons secondary You can make the button white when you use it on darker backgrounds. Use the variant: "secondary-solid" Nunjucks option to maintain colour contrast, or in HTML add the nhsuk-button--secondary-solid class. Open this example in a new tab : buttons secondary solid HTML code for buttons secondary solid Nunjucks code for buttons secondary solid HTML code for buttons secondary solid Copy code < button class = "nhsuk-button nhsuk-button--secondary-solid" data-module = "nhsuk-button" type = "submit" > Find my location </ button > Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons secondary solid Nunjucks code for buttons secondary solid Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the button. Name element Type string Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided. Name text Type string Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored. Name html Type string Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block. Name name Type string Description Name for the button. If href is provided, this has no effect. Name type Type string Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The button value attribute. If href is provided, this has no effect. Name disabled Type boolean Description Whether the button should be disabled. If href is provided, this has no effect. Name href Type string Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided. Name variant Type string Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" . Name small Type boolean Description If set to true , smaller button size will be used. Name classes Type string Description Classes to add to the button. Name attributes Type object Description HTML attributes (for example data attributes) to add to the button. Name aria Label Type string Description Button text exposed to assistive technologies, like screen readers, when only an icon is used. Name prevent Double Click Type boolean Description Prevent accidental double clicks on submit buttons from submitting forms multiple times. Name icon Type object Description Can be used to add an icon to the button. See macro options for icon . Options for icon object Name Type Description Name name Type string Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" . Name html Type string Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored. Name placement Type string Description Required. Placement of the icon within the button – "start" or "end" . Copy code {% from "button/macro.njk" import button %} {{ button ({ text : "Find my location" , variant : "secondary-solid" }) }} Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons secondary solid When to use a secondary button Use a secondary button either: for secondary actions on a page when an action needs less prominence, for example because it is optional Pages with too many calls to action make it hard for users to know what to do next. Before adding lots of secondary buttons, try to simplify the page or break the content down across multiple pages. Warning buttons Open this example in a new tab : buttons warning HTML code for buttons warning Nunjucks code for buttons warning HTML code for buttons warning Copy code < button class = "nhsuk-button nhsuk-button--warning" data-module = "nhsuk-button" type = "submit" > Yes, delete this vaccine </ button > Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons warning Nunjucks code for buttons warning Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the button. Name element Type string Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided. Name text Type string Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored. Name html Type string Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block. Name name Type string Description Name for the button. If href is provided, this has no effect. Name type Type string Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The button value attribute. If href is provided, this has no effect. Name disabled Type boolean Description Whether the button should be disabled. If href is provided, this has no effect. Name href Type string Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided. Name variant Type string Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" . Name small Type boolean Description If set to true , smaller button size will be used. Name classes Type string Description Classes to add to the button. Name attributes Type object Description HTML attributes (for example data attributes) to add to the button. Name aria Label Type string Description Button text exposed to assistive technologies, like screen readers, when only an icon is used. Name prevent Double Click Type boolean Description Prevent accidental double clicks on submit buttons from submitting forms multiple times. Name icon Type object Description Can be used to add an icon to the button. See macro options for icon . Options for icon object Name Type Description Name name Type string Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" . Name html Type string Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored. Name placement Type string Description Required. Placement of the icon within the button – "start" or "end" . Copy code {% from "button/macro.njk" import button %} {{ button ({ text : "Yes, delete this vaccine" , variant : "warning" }) }} Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons warning When to use a warning button Warning buttons are designed to make users think carefully before they use them. They are only effective if used very sparingly. Most services should not need one. Only use warning buttons for actions with serious destructive consequences that a user cannot easily undo, for example permanently deleting an account. For important destructive actions like this, include an additional step to confirm it. Use another style of button for the initial call to action, and a warning button for the final confirmation. Do not rely on the red colour of a warning button to communicate the serious nature of the action. This is because not all users will be able to see the colour or understand what it means. Make sure the context and button text make clear what will happen if the user selects it. Smaller buttons Use them sparingly. First try using a standard button. Open this example in a new tab : buttons smaller button HTML code for buttons smaller button Nunjucks code for buttons smaller button HTML code for buttons smaller button Copy code < button class = "nhsuk-button nhsuk-button--small" data-module = "nhsuk-button" type = "submit" > Apply filters </ button > Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons smaller button Nunjucks code for buttons smaller button Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the button. Name element Type string Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided. Name text Type string Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored. Name html Type string Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block. Name name Type string Description Name for the button. If href is provided, this has no effect. Name type Type string Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The button value attribute. If href is provided, this has no effect. Name disabled Type boolean Description Whether the button should be disabled. If href is provided, this has no effect. Name href Type string Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided. Name variant Type string Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" . Name small Type boolean Description If set to true , smaller button size will be used. Name classes Type string Description Classes to add to the button. Name attributes Type object Description HTML attributes (for example data attributes) to add to the button. Name aria Label Type string Description Button text exposed to assistive technologies, like screen readers, when only an icon is used. Name prevent Double Click Type boolean Description Prevent accidental double clicks on submit buttons from submitting forms multiple times. Name icon Type object Description Can be used to add an icon to the button. See macro options for icon . Options for icon object Name Type Description Name name Type string Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" . Name html Type string Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored. Name placement Type string Description Required. Placement of the icon within the button – "start" or "end" . Copy code {% from "button/macro.njk" import button %} {{ button ({ text : "Apply filters" , small : true }) }} Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons smaller button Only use smaller buttons when one of these applies: space is limited, for example in a card or panel there are several actions of a similar priority that a user can take, for example on a staff-facing system Open this example in a new tab : buttons smaller group HTML code for buttons smaller group Nunjucks code for buttons smaller group HTML code for buttons smaller group Copy code < div class = "nhsuk-button-group nhsuk-button-group--small" > < button class = "nhsuk-button nhsuk-button--small" data-module = "nhsuk-button" type = "submit" > Update results </ button > < button class = "nhsuk-button nhsuk-button--secondary nhsuk-button--small" data-module = "nhsuk-button" type = "submit" > Clear filters </ button > </ div > Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons smaller group Nunjucks code for buttons smaller group Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the button. Name element Type string Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided. Name text Type string Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored. Name html Type string Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block. Name name Type string Description Name for the button. If href is provided, this has no effect. Name type Type string Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The button value attribute. If href is provided, this has no effect. Name disabled Type boolean Description Whether the button should be disabled. If href is provided, this has no effect. Name href Type string Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided. Name variant Type string Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" . Name small Type boolean Description If set to true , smaller button size will be used. Name classes Type string Description Classes to add to the button. Name attributes Type object Description HTML attributes (for example data attributes) to add to the button. Name aria Label Type string Description Button text exposed to assistive technologies, like screen readers, when only an icon is used. Name prevent Double Click Type boolean Description Prevent accidental double clicks on submit buttons from submitting forms multiple times. Name icon Type object Description Can be used to add an icon to the button. See macro options for icon . Options for icon object Name Type Description Name name Type string Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" . Name html Type string Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored. Name placement Type string Description Required. Placement of the icon within the button – "start" or "end" . Copy code {% from "button/macro.njk" import button %} < div class = "nhsuk-button-group nhsuk-button-group--small" > {{ button ({ text : "Update results" , small : true }) }} {{ button ({ text : "Clear filters" , small : true , variant : "secondary" }) }} </ div > Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons smaller group Do not mix up button sizes within button groups. For example, do not group a smaller button with a standard button. Only use 1 primary button in a group. Open this example in a new tab : buttons smaller inline HTML code for buttons smaller inline Nunjucks code for buttons smaller inline HTML code for buttons smaller inline Copy code < div class = "nhsuk-form-group" > < label class = "nhsuk-label" for = "product-code" > Product code </ label > < div class = "nhsuk-input-wrapper" > < input class = "nhsuk-input nhsuk-input--code nhsuk-input--width-10" id = "product-code" name = "productCode" type = "text" > < button class = "nhsuk-button nhsuk-button--small" data-module = "nhsuk-button" type = "submit" > Find </ button > </ div > </ div > Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons smaller inline Nunjucks code for buttons smaller inline Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the button. Name element Type string Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided. Name text Type string Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored. Name html Type string Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block. Name name Type string Description Name for the button. If href is provided, this has no effect. Name type Type string Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The button value attribute. If href is provided, this has no effect. Name disabled Type boolean Description Whether the button should be disabled. If href is provided, this has no effect. Name href Type string Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided. Name variant Type string Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" . Name small Type boolean Description If set to true , smaller button size will be used. Name classes Type string Description Classes to add to the button. Name attributes Type object Description HTML attributes (for example data attributes) to add to the button. Name aria Label Type string Description Button text exposed to assistive technologies, like screen readers, when only an icon is used. Name prevent Double Click Type boolean Description Prevent accidental double clicks on submit buttons from submitting forms multiple times. Name icon Type object Description Can be used to add an icon to the button. See macro options for icon . Options for icon object Name Type Description Name name Type string Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" . Name html Type string Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored. Name placement Type string Description Required. Placement of the icon within the button – "start" or "end" . Copy code {% from "button/macro.njk" import button %} {% from "input/macro.njk" import input %} {{ input ({ label : { text : "Product code" }, id : "product-code" , name : "productCode" , width : 10 , code : true , formGroup : { afterInput : { html : button ({ text : "Find" , small : true }) } } }) }} Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons smaller inline Smaller buttons can be used inline with text inputs when the button relates specifically to the input, for example a code lookup. Disabled buttons Disabled buttons have poor contrast and can confuse some users. Only use them if user research shows it makes things easier for users to understand. Colour contrast All our buttons pass AA guidelines for colour contrast. The disabled versions of the buttons do not meet accessibility colour contrast ratios. If your team has discovered a user need for disabled buttons, use them carefully and test them with users with access needs. Grouping buttons Use a button group when 2 or more buttons are placed together. The buttons will display side by side on wider screens. On smaller screens, such as on mobile, they'll appear above each other. Open this example in a new tab : buttons button group HTML code for buttons button group Nunjucks code for buttons button group HTML code for buttons button group Copy code < div class = "nhsuk-button-group" > < button class = "nhsuk-button" data-module = "nhsuk-button" type = "submit" > Continue </ button > < button class = "nhsuk-button nhsuk-button--secondary" data-module = "nhsuk-button" type = "submit" > Save and come back later </ button > </ div > Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons button group Nunjucks code for buttons button group Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the button. Name element Type string Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided. Name text Type string Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored. Name html Type string Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block. Name name Type string Description Name for the button. If href is provided, this has no effect. Name type Type string Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The button value attribute. If href is provided, this has no effect. Name disabled Type boolean Description Whether the button should be disabled. If href is provided, this has no effect. Name href Type string Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided. Name variant Type string Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" . Name small Type boolean Description If set to true , smaller button size will be used. Name classes Type string Description Classes to add to the button. Name attributes Type object Description HTML attributes (for example data attributes) to add to the button. Name aria Label Type string Description Button text exposed to assistive technologies, like screen readers, when only an icon is used. Name prevent Double Click Type boolean Description Prevent accidental double clicks on submit buttons from submitting forms multiple times. Name icon Type object Description Can be used to add an icon to the button. See macro options for icon . Options for icon object Name Type Description Name name Type string Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" . Name html Type string Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored. Name placement Type string Description Required. Placement of the icon within the button – "start" or "end" . Copy code {% from "button/macro.njk" import button %} < div class = "nhsuk-button-group" > {{ button ({ text : "Continue" }) }} {{ button ({ text : "Save and come back later" , variant : "secondary" }) }} </ div > Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons button group Any links within a button group will automatically align with the buttons. Open this example in a new tab : buttons button group link HTML code for buttons button group link Nunjucks code for buttons button group link HTML code for buttons button group link Copy code < div class = "nhsuk-button-group" > < button class = "nhsuk-button" data-module = "nhsuk-button" type = "submit" > Continue </ button > < a href = "#" class = "nhsuk-link" > Cancel </ a > </ div > Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons button group link Nunjucks code for buttons button group link Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the button. Name element Type string Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided. Name text Type string Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored. Name html Type string Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block. Name name Type string Description Name for the button. If href is provided, this has no effect. Name type Type string Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The button value attribute. If href is provided, this has no effect. Name disabled Type boolean Description Whether the button should be disabled. If href is provided, this has no effect. Name href Type string Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided. Name variant Type string Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" . Name small Type boolean Description If set to true , smaller button size will be used. Name classes Type string Description Classes to add to the button. Name attributes Type object Description HTML attributes (for example data attributes) to add to the button. Name aria Label Type string Description Button text exposed to assistive technologies, like screen readers, when only an icon is used. Name prevent Double Click Type boolean Description Prevent accidental double clicks on submit buttons from submitting forms multiple times. Name icon Type object Description Can be used to add an icon to the button. See macro options for icon . Options for icon object Name Type Description Name name Type string Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" . Name html Type string Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored. Name placement Type string Description Required. Placement of the icon within the button – "start" or "end" . Copy code {% from "button/macro.njk" import button %} < div class = "nhsuk-button-group" > {{ button ({ text : "Continue" }) }} < a href = "#" class = "nhsuk-link" > Cancel </ a > </ div > Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons button group link Button text Write button text in sentence case, describing the action it performs. For example: "Start now" on the start page of your service "Log in" to an account a user has already created "Continue" whether the service saves or does not save a user's information "Save and continue" when the service saves a user's information but your research shows you need to reassure them that it does "Save and come back later" when a user can save their information and come back later "Add another" to add another item to a list or group "Pay" to make a payment "Confirm and send" on a Check answers page that does not have any legal content a user must agree to "Confirm and save" on a Check answers page on a staff-facing service or where data is not being sent to another person or system "Accept and send" on a Check answers page that has legal content a user must agree to "Log out" when a user is logged in to an account You may need to include more or different words to better describe the action. For example, "Add another address" and "Accept and claim a tax refund". Stop users from accidentally sending information more than once Sometimes, users double click buttons because they: have used operating systems where they have to double click items to make them work are experiencing a slow connection which means they are not given feedback on their action quickly enough have motor impairments such as hand tremors which cause them to click the button involuntarily In some cases, this can mean their information is sent twice. For example, the GOV.UK Notify team discovered that a number of users were receiving invitations twice, because the person sending them was double clicking the "send" button. If your research shows that users are frequently sending information twice, you can configure the button to ignore the 2nd click. To do this, set the data-prevent-double-click attribute to true . You can do this directly in the HTML or, if you're using Nunjucks, you can use the Nunjucks macro as shown in this example. Open this example in a new tab : buttons prevent double click HTML code for buttons prevent double click Nunjucks code for buttons prevent double click HTML code for buttons prevent double click Copy code < button class = "nhsuk-button" data-module = "nhsuk-button" data-prevent-double-click = "true" type = "submit" > Confirm and send </ button > Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons prevent double click Nunjucks code for buttons prevent double click Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the button. Name element Type string Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided. Name text Type string Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored. Name html Type string Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored. Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block. Name name Type string Description Name for the button. If href is provided, this has no effect. Name type Type string Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The button value attribute. If href is provided, this has no effect. Name disabled Type boolean Description Whether the button should be disabled. If href is provided, this has no effect. Name href Type string Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided. Name variant Type string Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" . Name small Type boolean Description If set to true , smaller button size will be used. Name classes Type string Description Classes to add to the button. Name attributes Type object Description HTML attributes (for example data attributes) to add to the button. Name aria Label Type string Description Button text exposed to assistive technologies, like screen readers, when only an icon is used. Name prevent Double Click Type boolean Description Prevent accidental double clicks on submit buttons from submitting forms multiple times. Name icon Type object Description Can be used to add an icon to the button. See macro options for icon . Options for icon object Name Type Description Name name Type string Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" . Name html Type string Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored. Name placement Type string Description Required. Placement of the icon within the button – "start" or "end" . Copy code {% from "button/macro.njk" import button %} {{ button ({ text : "Confirm and send" , preventDoubleClick : true }) }} Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend Close : buttons prevent double click This feature will prevent double clicks for users that have JavaScript enabled. However, you should also think about the issue server-side to protect against attacks. In the case of slow connections, aim to give the user information about what's happening, for example by showing a loading spinner or a modal, before using data-prevent-double-click . Research We based our buttons on the GOV.UK designs. But because our logo is a blue rectangle and a number of our components (including panel headings) have squared edges, we decided that GOV.UK buttons did not stand out enough. The square buttons did not look clickable next to the other square components. We made the buttons more "buttony" by rounding the corners (adding corner radiuses). There is research to suggest that rounded corners make things more clickable. Our testing confirmed this. Users were able to complete tasks using buttons and they did not confuse them with non-clickable components. Help us improve this guidance Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public. Feed back or share insights on GitHub Read more about how to feed back or share insights . If you have any questions, get in touch with the service manual team. Updates to this page Updated: June 2026

- to pages which are not part of your user journey

- from 1 flat content page to another

- to external websites

Try not to have multiple buttons on a page. Follow GOV.UK guidance on structuring forms and starting with one thing per page .

## How to use buttons

We have 5 kinds of button:

- primary buttons

- secondary buttons

- warning buttons

- smaller buttons

- disabled buttons

Align the primary action button to the left edge of your form.

On smaller screens, such as on mobile, buttons stretch across the screen's width. This makes them easier to press for users holding a phone in their right hand.

Do not decrease the height of buttons to less than our smaller buttons .

### Primary buttons

There are 2 versions of the primary button: the default version and the reverse version.

- HTML code for buttons

- Nunjucks code for buttons

```text
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

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the button.
Name element | Type string | Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided.
Name text | Type string | Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block.
Name name | Type string | Description Name for the button. If href is provided, this has no effect.
Name type | Type string | Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The button value attribute. If href is provided, this has no effect.
Name disabled | Type boolean | Description Whether the button should be disabled. If href is provided, this has no effect.
Name href | Type string | Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided.
Name variant | Type string | Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name small | Type boolean | Description If set to true , smaller button size will be used.
Name classes | Type string | Description Classes to add to the button.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the button.
Name aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when only an icon is used.
Name prevent Double Click | Type boolean | Description Prevent accidental double clicks on submit buttons from submitting forms multiple times.
Name icon | Type object | Description Can be used to add an icon to the button. See macro options for icon .

Name | Type | Description
Name name | Type string | Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" .
Name html | Type string | Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored.
Name placement | Type string | Description Required. Placement of the icon within the button – "start" or "end" .

```text
{%
from
"button/macro.njk"
import
button
%}
{{
button
({
text
:
"Continue"
})
}}
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

#### When to use a primary button

Use a primary button for the main call to action on a page, for example to help users start an application or save their progress.

Use only 1 primary button on a page. Having more than 1 reduces their impact and makes it harder for users to know what to do next.

#### Primary buttons on dark backgrounds

To show a white button on dark backgrounds, add the variant: "reverse" option using Nunjucks. For HTML add the nhsuk-button--reverse class to the button.

Make sure all users can see the button. The background colour must have a contrast ratio of at least 3:1 with white to meet WCAG 2.2 success criterion 1.4.11 Non-text Contrast, level AA (W3C) .

- HTML code for buttons reverse

- Nunjucks code for buttons reverse

```text
<
button
class
=
"nhsuk-button nhsuk-button--reverse"
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

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the button.
Name element | Type string | Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided.
Name text | Type string | Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block.
Name name | Type string | Description Name for the button. If href is provided, this has no effect.
Name type | Type string | Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The button value attribute. If href is provided, this has no effect.
Name disabled | Type boolean | Description Whether the button should be disabled. If href is provided, this has no effect.
Name href | Type string | Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided.
Name variant | Type string | Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name small | Type boolean | Description If set to true , smaller button size will be used.
Name classes | Type string | Description Classes to add to the button.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the button.
Name aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when only an icon is used.
Name prevent Double Click | Type boolean | Description Prevent accidental double clicks on submit buttons from submitting forms multiple times.
Name icon | Type object | Description Can be used to add an icon to the button. See macro options for icon .

Name | Type | Description
Name name | Type string | Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" .
Name html | Type string | Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored.
Name placement | Type string | Description Required. Placement of the icon within the button – "start" or "end" .

```text
{%
from
"button/macro.njk"
import
button
%}
{{
button
({
text
:
"Continue"
,
variant
:
"reverse"
})
}}
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

### Secondary buttons

There are 2 versions of the secondary button.

By default, the secondary button is transparent and has no colour. Use it on the page background colour ( nhsuk-colour("grey-5") ).

- HTML code for buttons secondary

- Nunjucks code for buttons secondary

```text
<
button
class
=
"nhsuk-button nhsuk-button--secondary"
data-module
=
"nhsuk-button"
type
=
"submit"
>
Find my location
</
button
>
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the button.
Name element | Type string | Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided.
Name text | Type string | Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block.
Name name | Type string | Description Name for the button. If href is provided, this has no effect.
Name type | Type string | Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The button value attribute. If href is provided, this has no effect.
Name disabled | Type boolean | Description Whether the button should be disabled. If href is provided, this has no effect.
Name href | Type string | Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided.
Name variant | Type string | Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name small | Type boolean | Description If set to true , smaller button size will be used.
Name classes | Type string | Description Classes to add to the button.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the button.
Name aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when only an icon is used.
Name prevent Double Click | Type boolean | Description Prevent accidental double clicks on submit buttons from submitting forms multiple times.
Name icon | Type object | Description Can be used to add an icon to the button. See macro options for icon .

Name | Type | Description
Name name | Type string | Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" .
Name html | Type string | Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored.
Name placement | Type string | Description Required. Placement of the icon within the button – "start" or "end" .

```text
{%
from
"button/macro.njk"
import
button
%}
{{
button
({
text
:
"Find my location"
,
variant
:
"secondary"
})
}}
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

You can make the button white when you use it on darker backgrounds. Use the variant: "secondary-solid" Nunjucks option to maintain colour contrast, or in HTML add the nhsuk-button--secondary-solid class.

- HTML code for buttons secondary solid

- Nunjucks code for buttons secondary solid

```text
<
button
class
=
"nhsuk-button nhsuk-button--secondary-solid"
data-module
=
"nhsuk-button"
type
=
"submit"
>
Find my location
</
button
>
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the button.
Name element | Type string | Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided.
Name text | Type string | Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block.
Name name | Type string | Description Name for the button. If href is provided, this has no effect.
Name type | Type string | Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The button value attribute. If href is provided, this has no effect.
Name disabled | Type boolean | Description Whether the button should be disabled. If href is provided, this has no effect.
Name href | Type string | Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided.
Name variant | Type string | Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name small | Type boolean | Description If set to true , smaller button size will be used.
Name classes | Type string | Description Classes to add to the button.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the button.
Name aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when only an icon is used.
Name prevent Double Click | Type boolean | Description Prevent accidental double clicks on submit buttons from submitting forms multiple times.
Name icon | Type object | Description Can be used to add an icon to the button. See macro options for icon .

Name | Type | Description
Name name | Type string | Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" .
Name html | Type string | Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored.
Name placement | Type string | Description Required. Placement of the icon within the button – "start" or "end" .

```text
{%
from
"button/macro.njk"
import
button
%}
{{
button
({
text
:
"Find my location"
,
variant
:
"secondary-solid"
})
}}
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

#### When to use a secondary button

Use a secondary button either:

- for secondary actions on a page

- when an action needs less prominence, for example because it is optional

Pages with too many calls to action make it hard for users to know what to do next. Before adding lots of secondary buttons, try to simplify the page or break the content down across multiple pages.

### Warning buttons

- HTML code for buttons warning

- Nunjucks code for buttons warning

```text
<
button
class
=
"nhsuk-button nhsuk-button--warning"
data-module
=
"nhsuk-button"
type
=
"submit"
>
Yes, delete this vaccine
</
button
>
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the button.
Name element | Type string | Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided.
Name text | Type string | Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block.
Name name | Type string | Description Name for the button. If href is provided, this has no effect.
Name type | Type string | Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The button value attribute. If href is provided, this has no effect.
Name disabled | Type boolean | Description Whether the button should be disabled. If href is provided, this has no effect.
Name href | Type string | Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided.
Name variant | Type string | Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name small | Type boolean | Description If set to true , smaller button size will be used.
Name classes | Type string | Description Classes to add to the button.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the button.
Name aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when only an icon is used.
Name prevent Double Click | Type boolean | Description Prevent accidental double clicks on submit buttons from submitting forms multiple times.
Name icon | Type object | Description Can be used to add an icon to the button. See macro options for icon .

Name | Type | Description
Name name | Type string | Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" .
Name html | Type string | Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored.
Name placement | Type string | Description Required. Placement of the icon within the button – "start" or "end" .

```text
{%
from
"button/macro.njk"
import
button
%}
{{
button
({
text
:
"Yes, delete this vaccine"
,
variant
:
"warning"
})
}}
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

#### When to use a warning button

Warning buttons are designed to make users think carefully before they use them. They are only effective if used very sparingly. Most services should not need one.

Only use warning buttons for actions with serious destructive consequences that a user cannot easily undo, for example permanently deleting an account.

For important destructive actions like this, include an additional step to confirm it. Use another style of button for the initial call to action, and a warning button for the final confirmation.

Do not rely on the red colour of a warning button to communicate the serious nature of the action. This is because not all users will be able to see the colour or understand what it means. Make sure the context and button text make clear what will happen if the user selects it.

### Smaller buttons

Use them sparingly. First try using a standard button.

- HTML code for buttons smaller button

- Nunjucks code for buttons smaller button

```text
<
button
class
=
"nhsuk-button nhsuk-button--small"
data-module
=
"nhsuk-button"
type
=
"submit"
>
Apply filters
</
button
>
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the button.
Name element | Type string | Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided.
Name text | Type string | Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block.
Name name | Type string | Description Name for the button. If href is provided, this has no effect.
Name type | Type string | Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The button value attribute. If href is provided, this has no effect.
Name disabled | Type boolean | Description Whether the button should be disabled. If href is provided, this has no effect.
Name href | Type string | Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided.
Name variant | Type string | Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name small | Type boolean | Description If set to true , smaller button size will be used.
Name classes | Type string | Description Classes to add to the button.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the button.
Name aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when only an icon is used.
Name prevent Double Click | Type boolean | Description Prevent accidental double clicks on submit buttons from submitting forms multiple times.
Name icon | Type object | Description Can be used to add an icon to the button. See macro options for icon .

Name | Type | Description
Name name | Type string | Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" .
Name html | Type string | Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored.
Name placement | Type string | Description Required. Placement of the icon within the button – "start" or "end" .

```text
{%
from
"button/macro.njk"
import
button
%}
{{
button
({
text
:
"Apply filters"
,
small
:
true
})
}}
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

Only use smaller buttons when one of these applies:

- space is limited, for example in a card or panel

- there are several actions of a similar priority that a user can take, for example on a staff-facing system

- HTML code for buttons smaller group

- Nunjucks code for buttons smaller group

```text
<
div
class
=
"nhsuk-button-group nhsuk-button-group--small"
>
<
button
class
=
"nhsuk-button nhsuk-button--small"
data-module
=
"nhsuk-button"
type
=
"submit"
>
Update results
</
button
>
<
button
class
=
"nhsuk-button nhsuk-button--secondary nhsuk-button--small"
data-module
=
"nhsuk-button"
type
=
"submit"
>
Clear filters
</
button
>
</
div
>
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the button.
Name element | Type string | Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided.
Name text | Type string | Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block.
Name name | Type string | Description Name for the button. If href is provided, this has no effect.
Name type | Type string | Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The button value attribute. If href is provided, this has no effect.
Name disabled | Type boolean | Description Whether the button should be disabled. If href is provided, this has no effect.
Name href | Type string | Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided.
Name variant | Type string | Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name small | Type boolean | Description If set to true , smaller button size will be used.
Name classes | Type string | Description Classes to add to the button.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the button.
Name aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when only an icon is used.
Name prevent Double Click | Type boolean | Description Prevent accidental double clicks on submit buttons from submitting forms multiple times.
Name icon | Type object | Description Can be used to add an icon to the button. See macro options for icon .

Name | Type | Description
Name name | Type string | Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" .
Name html | Type string | Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored.
Name placement | Type string | Description Required. Placement of the icon within the button – "start" or "end" .

```text
{%
from
"button/macro.njk"
import
button
%}
<
div
class
=
"nhsuk-button-group nhsuk-button-group--small"
>
{{
button
({
text
:
"Update results"
,
small
:
true
})
}}
{{
button
({
text
:
"Clear filters"
,
small
:
true
,
variant
:
"secondary"
})
}}
</
div
>
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

Do not mix up button sizes within button groups. For example, do not group a smaller button with a standard button. Only use 1 primary button in a group.

- HTML code for buttons smaller inline

- Nunjucks code for buttons smaller inline

```text
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
"nhsuk-label"
for
=
"product-code"
>
Product code
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
"nhsuk-input nhsuk-input--code nhsuk-input--width-10"
id
=
"product-code"
name
=
"productCode"
type
=
"text"
>
<
button
class
=
"nhsuk-button nhsuk-button--small"
data-module
=
"nhsuk-button"
type
=
"submit"
>
Find
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

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the button.
Name element | Type string | Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided.
Name text | Type string | Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block.
Name name | Type string | Description Name for the button. If href is provided, this has no effect.
Name type | Type string | Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The button value attribute. If href is provided, this has no effect.
Name disabled | Type boolean | Description Whether the button should be disabled. If href is provided, this has no effect.
Name href | Type string | Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided.
Name variant | Type string | Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name small | Type boolean | Description If set to true , smaller button size will be used.
Name classes | Type string | Description Classes to add to the button.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the button.
Name aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when only an icon is used.
Name prevent Double Click | Type boolean | Description Prevent accidental double clicks on submit buttons from submitting forms multiple times.
Name icon | Type object | Description Can be used to add an icon to the button. See macro options for icon .

Name | Type | Description
Name name | Type string | Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" .
Name html | Type string | Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored.
Name placement | Type string | Description Required. Placement of the icon within the button – "start" or "end" .

```text
{%
from
"button/macro.njk"
import
button
%}
{%
from
"input/macro.njk"
import
input
%}
{{
input
({
label
: {
text
:
"Product code"
},
id
:
"product-code"
,
name
:
"productCode"
,
width
:
10
,
code
:
true
,
formGroup
: {
afterInput
: {
html
:
button
({
text
:
"Find"
,
small
:
true
})
}
  }
}) }}
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

Smaller buttons can be used inline with text inputs when the button relates specifically to the input, for example a code lookup.

### Disabled buttons

Disabled buttons have poor contrast and can confuse some users. Only use them if user research shows it makes things easier for users to understand.

#### Colour contrast

All our buttons pass AA guidelines for colour contrast. The disabled versions of the buttons do not meet accessibility colour contrast ratios. If your team has discovered a user need for disabled buttons, use them carefully and test them with users with access needs.

### Grouping buttons

Use a button group when 2 or more buttons are placed together. The buttons will display side by side on wider screens. On smaller screens, such as on mobile, they'll appear above each other.

- HTML code for buttons button group

- Nunjucks code for buttons button group

```text
<
div
class
=
"nhsuk-button-group"
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
<
button
class
=
"nhsuk-button nhsuk-button--secondary"
data-module
=
"nhsuk-button"
type
=
"submit"
>
Save and come back later
</
button
>
</
div
>
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the button.
Name element | Type string | Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided.
Name text | Type string | Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block.
Name name | Type string | Description Name for the button. If href is provided, this has no effect.
Name type | Type string | Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The button value attribute. If href is provided, this has no effect.
Name disabled | Type boolean | Description Whether the button should be disabled. If href is provided, this has no effect.
Name href | Type string | Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided.
Name variant | Type string | Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name small | Type boolean | Description If set to true , smaller button size will be used.
Name classes | Type string | Description Classes to add to the button.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the button.
Name aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when only an icon is used.
Name prevent Double Click | Type boolean | Description Prevent accidental double clicks on submit buttons from submitting forms multiple times.
Name icon | Type object | Description Can be used to add an icon to the button. See macro options for icon .

Name | Type | Description
Name name | Type string | Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" .
Name html | Type string | Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored.
Name placement | Type string | Description Required. Placement of the icon within the button – "start" or "end" .

```text
{%
from
"button/macro.njk"
import
button
%}
<
div
class
=
"nhsuk-button-group"
>
{{
button
({
text
:
"Continue"
})
}}
{{
button
({
text
:
"Save and come back later"
,
variant
:
"secondary"
})
}}
</
div
>
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

Any links within a button group will automatically align with the buttons.

- HTML code for buttons button group link

- Nunjucks code for buttons button group link

```text
<
div
class
=
"nhsuk-button-group"
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
<
a
href
=
"#"
class
=
"nhsuk-link"
>
Cancel
</
a
>
</
div
>
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the button.
Name element | Type string | Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided.
Name text | Type string | Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block.
Name name | Type string | Description Name for the button. If href is provided, this has no effect.
Name type | Type string | Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The button value attribute. If href is provided, this has no effect.
Name disabled | Type boolean | Description Whether the button should be disabled. If href is provided, this has no effect.
Name href | Type string | Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided.
Name variant | Type string | Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name small | Type boolean | Description If set to true , smaller button size will be used.
Name classes | Type string | Description Classes to add to the button.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the button.
Name aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when only an icon is used.
Name prevent Double Click | Type boolean | Description Prevent accidental double clicks on submit buttons from submitting forms multiple times.
Name icon | Type object | Description Can be used to add an icon to the button. See macro options for icon .

Name | Type | Description
Name name | Type string | Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" .
Name html | Type string | Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored.
Name placement | Type string | Description Required. Placement of the icon within the button – "start" or "end" .

```text
{%
from
"button/macro.njk"
import
button
%}
<
div
class
=
"nhsuk-button-group"
>
{{
button
({
text
:
"Continue"
})
}}
<
a
href
=
"#"
class
=
"nhsuk-link"
>
Cancel
</
a
>
</
div
>
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

### Button text

Write button text in sentence case, describing the action it performs. For example:

- "Start now" on the start page of your service

- "Log in" to an account a user has already created

- "Continue" whether the service saves or does not save a user's information

- "Save and continue" when the service saves a user's information but your research shows you need to reassure them that it does

- "Save and come back later" when a user can save their information and come back later

- "Add another" to add another item to a list or group

- "Pay" to make a payment

- "Confirm and send" on a Check answers page that does not have any legal content a user must agree to

- "Confirm and save" on a Check answers page on a staff-facing service or where data is not being sent to another person or system

- "Accept and send" on a Check answers page that has legal content a user must agree to

- "Log out" when a user is logged in to an account

You may need to include more or different words to better describe the action. For example, "Add another address" and "Accept and claim a tax refund".

### Stop users from accidentally sending information more than once

Sometimes, users double click buttons because they:

- have used operating systems where they have to double click items to make them work

- are experiencing a slow connection which means they are not given feedback on their action quickly enough

- have motor impairments such as hand tremors which cause them to click the button involuntarily

In some cases, this can mean their information is sent twice.

For example, the GOV.UK Notify team discovered that a number of users were receiving invitations twice, because the person sending them was double clicking the "send" button.

If your research shows that users are frequently sending information twice, you can configure the button to ignore the 2nd click.

To do this, set the data-prevent-double-click attribute to true . You can do this directly in the HTML or, if you're using Nunjucks, you can use the Nunjucks macro as shown in this example.

- HTML code for buttons prevent double click

- Nunjucks code for buttons prevent double click

```text
<
button
class
=
"nhsuk-button"
data-module
=
"nhsuk-button"
data-prevent-double-click
=
"true"
type
=
"submit"
>
Confirm and send
</
button
>
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the button.
Name element | Type string | Description Deprecated in 10.6.0 (see GitHub) . HTML element for the button – "input" , "button" or "a" . In most cases you will not need to set this as it will be configured automatically if href is provided.
Name text | Type string | Description Required. If html or ariaLabel is set, this is not required. Text for the button. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text or ariaLabel is set, this is not required. HTML for the button. If html is provided, the text option will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire button component in a call block.
Name name | Type string | Description Name for the button. If href is provided, this has no effect.
Name type | Type string | Description Type of button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The button value attribute. If href is provided, this has no effect.
Name disabled | Type boolean | Description Whether the button should be disabled. If href is provided, this has no effect.
Name href | Type string | Description The button href attribute. If set, the button will use an <a> tag automatically unless type is provided.
Name variant | Type string | Description Optional variant of button – "brand" , "login" , "reverse" , "secondary" , "secondary-solid" or "warning" .
Name small | Type boolean | Description If set to true , smaller button size will be used.
Name classes | Type string | Description Classes to add to the button.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the button.
Name aria Label | Type string | Description Button text exposed to assistive technologies, like screen readers, when only an icon is used.
Name prevent Double Click | Type boolean | Description Prevent accidental double clicks on submit buttons from submitting forms multiple times.
Name icon | Type object | Description Can be used to add an icon to the button. See macro options for icon .

Name | Type | Description
Name name | Type string | Description Required. Icon name for the button – for example, "search" , "arrow-right" , "plus" or "minus" .
Name html | Type string | Description Required. HTML to use for the icon, as an alternative to the name option. If html is provided, the name option will be ignored.
Name placement | Type string | Description Required. Placement of the icon within the button – "start" or "end" .

```text
{%
from
"button/macro.njk"
import
button
%}
{{
button
({
text
:
"Confirm and send"
,
preventDoubleClick
:
true
})
}}
```

Requires NHS.UK frontend 10.5.0 – check your version of NHS.UK frontend

This feature will prevent double clicks for users that have JavaScript enabled. However, you should also think about the issue server-side to protect against attacks.

In the case of slow connections, aim to give the user information about what's happening, for example by showing a loading spinner or a modal, before using data-prevent-double-click .

## Research

We based our buttons on the GOV.UK designs. But because our logo is a blue rectangle and a number of our components (including panel headings) have squared edges, we decided that GOV.UK buttons did not stand out enough. The square buttons did not look clickable next to the other square components.

We made the buttons more "buttony" by rounding the corners (adding corner radiuses). There is research to suggest that rounded corners make things more clickable.

Our testing confirmed this. Users were able to complete tasks using buttons and they did not confuse them with non-clickable components.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
