# Card – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/card/

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

# Content presentation – Card

Use a card to visually group related content and actions to help users do what they need to more quickly.

## When to use a card

Use a card to visually group related content and actions to help users do what they need to more quickly. You can group several cards together.

If you are grouping cards to create a hub page (sometimes called a landing page), use the hub page pattern .

## When not to use a card

Do not use a card to highlight content on a page of long form content.

Before using a card, consider using:

- the care card pattern to help users decide when and where to get care

- details

- an expander

- inset text

- tabs

- a warning callout

## How to use a card

There are two types of cards: primary card secondary card Both cards can be clickable or non-clickable. A card can include different elements, such as: a heading text a link or links You can also add an image or add actions . If you include a link, the link should mirror the heading of the page it links to. For clickable cards, avoid wrapping the entire card in an anchor tag as this can be a difficult experience for screen reader users. Keep the card short so it is easy to scan for relevant and actionable information. Primary card Primary cards are more visually prominent than secondary cards. Primary card clickable Open this example in a new tab : card primary card clickable HTML code for card primary card clickable Nunjucks code for card primary card clickable HTML code for card primary card clickable Copy code < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-one-quarter nhsuk-card-group__item" > < div class = "nhsuk-card nhsuk-card--clickable" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1" > < span role = "text" > < span class = "nhsuk-u-visually-hidden" > Applicants: </ span > 91 </ span > </ h2 > < a href = "#/applicants" class = "nhsuk-card__link" > Applicants </ a > </ div > </ div > </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card primary card clickable Nunjucks code for card primary card clickable Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the card. Name heading Type object Description Required. Heading of the card component. See macro options for heading . Name heading Html Type string Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option. Name heading Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option. Name heading Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option. Name heading Level Type integer Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option. Name heading Id Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option. Name heading Visually Hidden Text Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option. Name href Type string Description The card link href attribute. Name clickable Type boolean Description If set to true , then the whole card will become a clickable card variant. Name variant Type string Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" . Name type Type string Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option. Name feature Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option. Name primary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option. Name secondary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option. Name warning Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option. Name img U R L Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option. Name img A L T Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option. Name image Type object Description Can be used to add an image to the card component. See macro options for image . Name description Type object Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description . Name description Html Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option. Name actions Type object Description Can be used to add actions to the card component. See macro options for actions . Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block. Name classes Type string Description Classes to add to the card. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card. Options for heading component Name Type Description Name id Type string Description The ID of the heading. Name text Type string Description Required. If html is set, this is not required. Text for the heading. Name html Type string Description Required. If text is set, this is not required. HTML for the heading. Name visually Hidden Text Type string Description Optional visually hidden prefix used before the heading. Name size Type string Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" . Name level Type integer Description Optional heading level. Defaults to 2 . Name classes Type string Description Classes to add to the heading. Name attributes Type object Description HTML attributes (for example data attributes) to add to the heading. Options for image object Name Type Description Name src Type string Description Required. The URL of the image in the card. Name alt Type string Description The alternative text of the image in the card. Name html Type string Description HTML to use for the image content. If html is provided, the src and alt options will be ignored. Options for description object Name Type Description Name text Type string Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored. Name classes Type string Description Classes to add to the card content. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card content. Options for actions object Name Type Description Name items Type array Description Array of actions as links for use in the card component. See macro options for actions items . Name classes Type string Description Classes to add to the actions wrapper. Options for actions items array objects Name Type Description Name id Type string Description The ID of the action item. Name text Type string Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios. Name name Type string Description Name for the action as a button. If href is provided, this has no effect. Name type Type string Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The value attribute for the action as a button. If href is provided, this has no effect. Name href Type string Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided. Name classes Type string Description Classes to add to the action item. Name attributes Type object Description HTML attributes (for example data attributes) to add to the action item. Copy code {% from "card/macro.njk" import card %} < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-one-quarter nhsuk-card-group__item" > {% call card ({ heading : { text : "91" , visuallyHiddenText : "Applicants" , classes : "nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1" }, clickable : true }) %} < a href = "#/applicants" class = "nhsuk-card__link" > Applicants </ a > {% endcall %} </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card primary card clickable Primary card with chevron The chevron icon on this primary card makes it even more prominent. There is only a clickable version of this card. Read about how to use primary cards with chevrons in the hub page pattern . Open this example in a new tab : card primary card HTML code for card primary card Nunjucks code for card primary card HTML code for card primary card Copy code < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-two-thirds nhsuk-card-group__item" > < div class = "nhsuk-card nhsuk-card--clickable nhsuk-card--primary" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-heading-m" > < a class = "nhsuk-card__link" href = "#" > GPs </ a > </ h2 > < p class = "nhsuk-card__description" > About GP services, including how to find and register with a local GP and how to book an appointment </ p > < svg class = "nhsuk-icon nhsuk-icon--chevron-right-circle" xmlns = "http://www.w3.org/2000/svg" viewBox = "0 0 24 24" width = "16" height = "16" focusable = "false" aria-hidden = "true" > < path d = "M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-.3 5.8a1 1 0 1 0-1.5 1.4l2.9 2.8-2.9 2.8a1 1 0 0 0 1.5 1.4l3.5-3.5c.4-.4.4-1 0-1.4Z" /> </ svg > </ div > </ div > </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card primary card Nunjucks code for card primary card Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the card. Name heading Type object Description Required. Heading of the card component. See macro options for heading . Name heading Html Type string Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option. Name heading Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option. Name heading Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option. Name heading Level Type integer Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option. Name heading Id Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option. Name heading Visually Hidden Text Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option. Name href Type string Description The card link href attribute. Name clickable Type boolean Description If set to true , then the whole card will become a clickable card variant. Name variant Type string Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" . Name type Type string Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option. Name feature Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option. Name primary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option. Name secondary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option. Name warning Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option. Name img U R L Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option. Name img A L T Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option. Name image Type object Description Can be used to add an image to the card component. See macro options for image . Name description Type object Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description . Name description Html Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option. Name actions Type object Description Can be used to add actions to the card component. See macro options for actions . Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block. Name classes Type string Description Classes to add to the card. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card. Options for heading component Name Type Description Name id Type string Description The ID of the heading. Name text Type string Description Required. If html is set, this is not required. Text for the heading. Name html Type string Description Required. If text is set, this is not required. HTML for the heading. Name visually Hidden Text Type string Description Optional visually hidden prefix used before the heading. Name size Type string Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" . Name level Type integer Description Optional heading level. Defaults to 2 . Name classes Type string Description Classes to add to the heading. Name attributes Type object Description HTML attributes (for example data attributes) to add to the heading. Options for image object Name Type Description Name src Type string Description Required. The URL of the image in the card. Name alt Type string Description The alternative text of the image in the card. Name html Type string Description HTML to use for the image content. If html is provided, the src and alt options will be ignored. Options for description object Name Type Description Name text Type string Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored. Name classes Type string Description Classes to add to the card content. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card content. Options for actions object Name Type Description Name items Type array Description Array of actions as links for use in the card component. See macro options for actions items . Name classes Type string Description Classes to add to the actions wrapper. Options for actions items array objects Name Type Description Name id Type string Description The ID of the action item. Name text Type string Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios. Name name Type string Description Name for the action as a button. If href is provided, this has no effect. Name type Type string Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The value attribute for the action as a button. If href is provided, this has no effect. Name href Type string Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided. Name classes Type string Description Classes to add to the action item. Name attributes Type object Description HTML attributes (for example data attributes) to add to the action item. Copy code {% from "card/macro.njk" import card %} < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-two-thirds nhsuk-card-group__item" > {{ card ({ heading : { text : "GPs" , size : "m" }, description : "About GP services, including how to find and register with a local GP and how to book an appointment" , href : "#" , clickable : true , variant : "primary" }) }} </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card primary card Primary card non-clickable Use the non-clickable card when you are using more than 1 link. Open this example in a new tab : card primary card non clickable HTML code for card primary card non clickable Nunjucks code for card primary card non clickable HTML code for card primary card non clickable Copy code < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-two-thirds nhsuk-card-group__item" > < div class = "nhsuk-card" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-heading-m" > < a class = "nhsuk-card__link" href = "/#" > Berrylands Pharmacy </ a > </ h2 > < p > Ewell Road, Surbiton, KT6 6EZ < br /> Phone: < a href = "#" > 01111 111 111 </ a > < br /> Email: < a href = "#" > organisation@nhs.net </ a > </ p > < p > < a href = "#" > Get directions (opens in Google Maps) </ a > </ p > </ div > </ div > </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card primary card non clickable Nunjucks code for card primary card non clickable Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the card. Name heading Type object Description Required. Heading of the card component. See macro options for heading . Name heading Html Type string Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option. Name heading Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option. Name heading Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option. Name heading Level Type integer Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option. Name heading Id Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option. Name heading Visually Hidden Text Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option. Name href Type string Description The card link href attribute. Name clickable Type boolean Description If set to true , then the whole card will become a clickable card variant. Name variant Type string Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" . Name type Type string Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option. Name feature Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option. Name primary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option. Name secondary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option. Name warning Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option. Name img U R L Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option. Name img A L T Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option. Name image Type object Description Can be used to add an image to the card component. See macro options for image . Name description Type object Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description . Name description Html Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option. Name actions Type object Description Can be used to add actions to the card component. See macro options for actions . Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block. Name classes Type string Description Classes to add to the card. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card. Options for heading component Name Type Description Name id Type string Description The ID of the heading. Name text Type string Description Required. If html is set, this is not required. Text for the heading. Name html Type string Description Required. If text is set, this is not required. HTML for the heading. Name visually Hidden Text Type string Description Optional visually hidden prefix used before the heading. Name size Type string Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" . Name level Type integer Description Optional heading level. Defaults to 2 . Name classes Type string Description Classes to add to the heading. Name attributes Type object Description HTML attributes (for example data attributes) to add to the heading. Options for image object Name Type Description Name src Type string Description Required. The URL of the image in the card. Name alt Type string Description The alternative text of the image in the card. Name html Type string Description HTML to use for the image content. If html is provided, the src and alt options will be ignored. Options for description object Name Type Description Name text Type string Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored. Name classes Type string Description Classes to add to the card content. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card content. Options for actions object Name Type Description Name items Type array Description Array of actions as links for use in the card component. See macro options for actions items . Name classes Type string Description Classes to add to the actions wrapper. Options for actions items array objects Name Type Description Name id Type string Description The ID of the action item. Name text Type string Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios. Name name Type string Description Name for the action as a button. If href is provided, this has no effect. Name type Type string Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The value attribute for the action as a button. If href is provided, this has no effect. Name href Type string Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided. Name classes Type string Description Classes to add to the action item. Name attributes Type object Description HTML attributes (for example data attributes) to add to the action item. Copy code {% from "card/macro.njk" import card %} {% set cardDescriptionHtml %} < p > Ewell Road, Surbiton, KT6 6EZ < br /> Phone: < a href = "#" > 01111 111 111 </ a > < br /> Email: < a href = "#" > organisation@nhs.net </ a > </ p > < p > < a href = "#" > Get directions (opens in Google Maps) </ a > </ p > {% endset %} < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-two-thirds nhsuk-card-group__item" > {{ card ({ heading : { text : "Berrylands Pharmacy" , size : "m" }, description : { html : cardDescriptionHtml }, href : "/#" , clickable : false }) }} </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card primary card non clickable Secondary card The secondary card has less visual impact than the primary cards. When used with other cards, use the secondary card to group less important content or actions. Secondary card clickable This card is also used in the hub page pattern . Open this example in a new tab : card secondary card HTML code for card secondary card Nunjucks code for card secondary card HTML code for card secondary card Copy code < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-two-thirds nhsuk-card-group__item" > < div class = "nhsuk-card nhsuk-card--clickable nhsuk-card--secondary" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-heading-m" > < a class = "nhsuk-card__link" href = "#" > Services A to Z </ a > </ h2 > < p class = "nhsuk-card__description" > Use our service finder to find other health services </ p > </ div > </ div > </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card secondary card Nunjucks code for card secondary card Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the card. Name heading Type object Description Required. Heading of the card component. See macro options for heading . Name heading Html Type string Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option. Name heading Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option. Name heading Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option. Name heading Level Type integer Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option. Name heading Id Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option. Name heading Visually Hidden Text Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option. Name href Type string Description The card link href attribute. Name clickable Type boolean Description If set to true , then the whole card will become a clickable card variant. Name variant Type string Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" . Name type Type string Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option. Name feature Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option. Name primary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option. Name secondary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option. Name warning Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option. Name img U R L Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option. Name img A L T Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option. Name image Type object Description Can be used to add an image to the card component. See macro options for image . Name description Type object Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description . Name description Html Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option. Name actions Type object Description Can be used to add actions to the card component. See macro options for actions . Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block. Name classes Type string Description Classes to add to the card. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card. Options for heading component Name Type Description Name id Type string Description The ID of the heading. Name text Type string Description Required. If html is set, this is not required. Text for the heading. Name html Type string Description Required. If text is set, this is not required. HTML for the heading. Name visually Hidden Text Type string Description Optional visually hidden prefix used before the heading. Name size Type string Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" . Name level Type integer Description Optional heading level. Defaults to 2 . Name classes Type string Description Classes to add to the heading. Name attributes Type object Description HTML attributes (for example data attributes) to add to the heading. Options for image object Name Type Description Name src Type string Description Required. The URL of the image in the card. Name alt Type string Description The alternative text of the image in the card. Name html Type string Description HTML to use for the image content. If html is provided, the src and alt options will be ignored. Options for description object Name Type Description Name text Type string Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored. Name classes Type string Description Classes to add to the card content. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card content. Options for actions object Name Type Description Name items Type array Description Array of actions as links for use in the card component. See macro options for actions items . Name classes Type string Description Classes to add to the actions wrapper. Options for actions items array objects Name Type Description Name id Type string Description The ID of the action item. Name text Type string Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios. Name name Type string Description Name for the action as a button. If href is provided, this has no effect. Name type Type string Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The value attribute for the action as a button. If href is provided, this has no effect. Name href Type string Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided. Name classes Type string Description Classes to add to the action item. Name attributes Type object Description HTML attributes (for example data attributes) to add to the action item. Copy code {% from "card/macro.njk" import card %} < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-two-thirds nhsuk-card-group__item" > {{ card ({ heading : { text : "Services A to Z" , size : "m" }, description : "Use our service finder to find other health services" , href : "#" , clickable : true , variant : "secondary" }) }} </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card secondary card Secondary card non-clickable Use the non-clickable card when you have more than 1 link in the content. Open this example in a new tab : card secondary card non clickable HTML code for card secondary card non clickable Nunjucks code for card secondary card non clickable HTML code for card secondary card non clickable Copy code < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-two-thirds nhsuk-card-group__item" > < div class = "nhsuk-card nhsuk-card--secondary" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-heading-m" > Help from NHS 111 </ h2 > < p > If you're worried about a symptom and not sure what help you need, NHS 111 can tell you what to do next. </ p > < p > Go to < a href = "#" > NHS 111 online </ a > or < a href = "#" > call 111 </ a > . </ p > < p > For a life-threatening emergency call 999. </ p > </ div > </ div > </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card secondary card non clickable Nunjucks code for card secondary card non clickable Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the card. Name heading Type object Description Required. Heading of the card component. See macro options for heading . Name heading Html Type string Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option. Name heading Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option. Name heading Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option. Name heading Level Type integer Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option. Name heading Id Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option. Name heading Visually Hidden Text Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option. Name href Type string Description The card link href attribute. Name clickable Type boolean Description If set to true , then the whole card will become a clickable card variant. Name variant Type string Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" . Name type Type string Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option. Name feature Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option. Name primary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option. Name secondary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option. Name warning Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option. Name img U R L Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option. Name img A L T Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option. Name image Type object Description Can be used to add an image to the card component. See macro options for image . Name description Type object Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description . Name description Html Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option. Name actions Type object Description Can be used to add actions to the card component. See macro options for actions . Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block. Name classes Type string Description Classes to add to the card. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card. Options for heading component Name Type Description Name id Type string Description The ID of the heading. Name text Type string Description Required. If html is set, this is not required. Text for the heading. Name html Type string Description Required. If text is set, this is not required. HTML for the heading. Name visually Hidden Text Type string Description Optional visually hidden prefix used before the heading. Name size Type string Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" . Name level Type integer Description Optional heading level. Defaults to 2 . Name classes Type string Description Classes to add to the heading. Name attributes Type object Description HTML attributes (for example data attributes) to add to the heading. Options for image object Name Type Description Name src Type string Description Required. The URL of the image in the card. Name alt Type string Description The alternative text of the image in the card. Name html Type string Description HTML to use for the image content. If html is provided, the src and alt options will be ignored. Options for description object Name Type Description Name text Type string Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored. Name classes Type string Description Classes to add to the card content. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card content. Options for actions object Name Type Description Name items Type array Description Array of actions as links for use in the card component. See macro options for actions items . Name classes Type string Description Classes to add to the actions wrapper. Options for actions items array objects Name Type Description Name id Type string Description The ID of the action item. Name text Type string Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios. Name name Type string Description Name for the action as a button. If href is provided, this has no effect. Name type Type string Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The value attribute for the action as a button. If href is provided, this has no effect. Name href Type string Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided. Name classes Type string Description Classes to add to the action item. Name attributes Type object Description HTML attributes (for example data attributes) to add to the action item. Copy code {% from "card/macro.njk" import card %} {% set cardDescriptionHtml %} < p > If you're worried about a symptom and not sure what help you need, NHS 111 can tell you what to do next. </ p > < p > Go to < a href = "#" > NHS 111 online </ a > or < a href = "#" > call 111 </ a > . </ p > < p > For a life-threatening emergency call 999. </ p > {% endset %} < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-two-thirds nhsuk-card-group__item" > {{ card ({ heading : { text : "Help from NHS 111" , size : "m" }, description : { html : cardDescriptionHtml }, variant : "secondary" }) }} </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card secondary card non clickable Adding an image Only use cards with images if you have evidence that they help your users, for example, where you can show that they motivate users. Images in a card will be displayed above the heading and text. The image is set as a decorative image by default, with the alternative text being null. Image card clickable Open this example in a new tab : card with image HTML code for card with image Nunjucks code for card with image HTML code for card with image Copy code < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-one-half nhsuk-card-group__item" > < div class = "nhsuk-card nhsuk-card--clickable" > < img class = "nhsuk-card__img" src = "https://assets.nhs.uk/prod/images/A_0218_exercise-main_FKW1X7.width-690.jpg" alt = "" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-heading-m" > < a class = "nhsuk-card__link" href = "#" > Exercise </ a > </ h2 > < p class = "nhsuk-card__description" > Programmes, workouts and tips to get you moving and improve your fitness and wellbeing </ p > </ div > </ div > </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card with image Nunjucks code for card with image Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the card. Name heading Type object Description Required. Heading of the card component. See macro options for heading . Name heading Html Type string Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option. Name heading Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option. Name heading Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option. Name heading Level Type integer Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option. Name heading Id Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option. Name heading Visually Hidden Text Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option. Name href Type string Description The card link href attribute. Name clickable Type boolean Description If set to true , then the whole card will become a clickable card variant. Name variant Type string Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" . Name type Type string Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option. Name feature Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option. Name primary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option. Name secondary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option. Name warning Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option. Name img U R L Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option. Name img A L T Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option. Name image Type object Description Can be used to add an image to the card component. See macro options for image . Name description Type object Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description . Name description Html Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option. Name actions Type object Description Can be used to add actions to the card component. See macro options for actions . Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block. Name classes Type string Description Classes to add to the card. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card. Options for heading component Name Type Description Name id Type string Description The ID of the heading. Name text Type string Description Required. If html is set, this is not required. Text for the heading. Name html Type string Description Required. If text is set, this is not required. HTML for the heading. Name visually Hidden Text Type string Description Optional visually hidden prefix used before the heading. Name size Type string Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" . Name level Type integer Description Optional heading level. Defaults to 2 . Name classes Type string Description Classes to add to the heading. Name attributes Type object Description HTML attributes (for example data attributes) to add to the heading. Options for image object Name Type Description Name src Type string Description Required. The URL of the image in the card. Name alt Type string Description The alternative text of the image in the card. Name html Type string Description HTML to use for the image content. If html is provided, the src and alt options will be ignored. Options for description object Name Type Description Name text Type string Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored. Name classes Type string Description Classes to add to the card content. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card content. Options for actions object Name Type Description Name items Type array Description Array of actions as links for use in the card component. See macro options for actions items . Name classes Type string Description Classes to add to the actions wrapper. Options for actions items array objects Name Type Description Name id Type string Description The ID of the action item. Name text Type string Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios. Name name Type string Description Name for the action as a button. If href is provided, this has no effect. Name type Type string Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The value attribute for the action as a button. If href is provided, this has no effect. Name href Type string Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided. Name classes Type string Description Classes to add to the action item. Name attributes Type object Description HTML attributes (for example data attributes) to add to the action item. Copy code {% from "card/macro.njk" import card %} < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-one-half nhsuk-card-group__item" > {{ card ({ image : { src : "https://assets.nhs.uk/prod/images/A_0218_exercise-main_FKW1X7.width-690.jpg" }, heading : { text : "Exercise" , size : "m" }, description : "Programmes, workouts and tips to get you moving and improve your fitness and wellbeing" , href : "#" , clickable : true }) }} </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card with image Image card non-clickable Open this example in a new tab : card with image non clickable HTML code for card with image non clickable Nunjucks code for card with image non clickable HTML code for card with image non clickable Copy code < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-one-half nhsuk-card-group__item" > < div class = "nhsuk-card" > < img class = "nhsuk-card__img" src = "https://assets.nhs.uk/prod/images/A_0218_exercise-main_FKW1X7.width-690.jpg" alt = "" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-heading-m" > Exercise </ h2 > < p > The < a href = "#" > benefits of exercise </ a > and < a href = "#" > why we should sit less </ a > </ p > </ div > </ div > </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card with image non clickable Nunjucks code for card with image non clickable Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the card. Name heading Type object Description Required. Heading of the card component. See macro options for heading . Name heading Html Type string Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option. Name heading Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option. Name heading Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option. Name heading Level Type integer Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option. Name heading Id Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option. Name heading Visually Hidden Text Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option. Name href Type string Description The card link href attribute. Name clickable Type boolean Description If set to true , then the whole card will become a clickable card variant. Name variant Type string Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" . Name type Type string Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option. Name feature Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option. Name primary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option. Name secondary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option. Name warning Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option. Name img U R L Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option. Name img A L T Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option. Name image Type object Description Can be used to add an image to the card component. See macro options for image . Name description Type object Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description . Name description Html Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option. Name actions Type object Description Can be used to add actions to the card component. See macro options for actions . Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block. Name classes Type string Description Classes to add to the card. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card. Options for heading component Name Type Description Name id Type string Description The ID of the heading. Name text Type string Description Required. If html is set, this is not required. Text for the heading. Name html Type string Description Required. If text is set, this is not required. HTML for the heading. Name visually Hidden Text Type string Description Optional visually hidden prefix used before the heading. Name size Type string Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" . Name level Type integer Description Optional heading level. Defaults to 2 . Name classes Type string Description Classes to add to the heading. Name attributes Type object Description HTML attributes (for example data attributes) to add to the heading. Options for image object Name Type Description Name src Type string Description Required. The URL of the image in the card. Name alt Type string Description The alternative text of the image in the card. Name html Type string Description HTML to use for the image content. If html is provided, the src and alt options will be ignored. Options for description object Name Type Description Name text Type string Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored. Name classes Type string Description Classes to add to the card content. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card content. Options for actions object Name Type Description Name items Type array Description Array of actions as links for use in the card component. See macro options for actions items . Name classes Type string Description Classes to add to the actions wrapper. Options for actions items array objects Name Type Description Name id Type string Description The ID of the action item. Name text Type string Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios. Name name Type string Description Name for the action as a button. If href is provided, this has no effect. Name type Type string Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The value attribute for the action as a button. If href is provided, this has no effect. Name href Type string Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided. Name classes Type string Description Classes to add to the action item. Name attributes Type object Description HTML attributes (for example data attributes) to add to the action item. Copy code {% from "card/macro.njk" import card %} {% set cardDescriptionHtml %} < p > The < a href = "#" > benefits of exercise </ a > and < a href = "#" > why we should sit less </ a > </ p > {% endset %} < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-one-half nhsuk-card-group__item" > {{ card ({ image : { src : "https://assets.nhs.uk/prod/images/A_0218_exercise-main_FKW1X7.width-690.jpg" }, heading : { text : "Exercise" , size : "m" }, description : { html : cardDescriptionHtml }, clickable : false }) }} </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card with image non clickable Adding actions You can add links for 1 or more actions to a card. They show below the heading on small screens and right-aligned on bigger screens. Card actions cannot be used on clickable cards. They can be used in summary cards . Open this example in a new tab : card card actions HTML code for card card actions Nunjucks code for card card actions HTML code for card card actions Copy code < div class = "nhsuk-card" > < div class = "nhsuk-card__heading-container" > < h2 class = "nhsuk-card__heading nhsuk-heading-m" > Template: Appointment invitation 1 </ h2 > < ul class = "nhsuk-card__actions" > < li class = "nhsuk-card__action" > < a class = "nhsuk-link" href = "#" > Edit < span class = "nhsuk-u-visually-hidden" > (Template: Appointment invitation 1) </ span > </ a > </ li > < li class = "nhsuk-card__action" > < a class = "nhsuk-link" href = "#" > Delete < span class = "nhsuk-u-visually-hidden" > (Template: Appointment invitation 1) </ span > </ a > </ li > </ ul > </ div > < div class = "nhsuk-card__content" > < p > < strong > SenderID </ strong > : NHS Blood Test </ p > < p > ((firstName)) ((lastName)), you are due for your NHS blood test. Book your appointment or find out more at < a href = "#" > http://www.nhs.uk/service-name-invite </ a > </ p > </ div > </ div > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card card actions Nunjucks code for card card actions Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the card. Name heading Type object Description Required. Heading of the card component. See macro options for heading . Name heading Html Type string Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option. Name heading Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option. Name heading Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option. Name heading Level Type integer Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option. Name heading Id Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option. Name heading Visually Hidden Text Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option. Name href Type string Description The card link href attribute. Name clickable Type boolean Description If set to true , then the whole card will become a clickable card variant. Name variant Type string Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" . Name type Type string Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option. Name feature Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option. Name primary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option. Name secondary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option. Name warning Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option. Name img U R L Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option. Name img A L T Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option. Name image Type object Description Can be used to add an image to the card component. See macro options for image . Name description Type object Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description . Name description Html Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option. Name actions Type object Description Can be used to add actions to the card component. See macro options for actions . Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block. Name classes Type string Description Classes to add to the card. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card. Options for heading component Name Type Description Name id Type string Description The ID of the heading. Name text Type string Description Required. If html is set, this is not required. Text for the heading. Name html Type string Description Required. If text is set, this is not required. HTML for the heading. Name visually Hidden Text Type string Description Optional visually hidden prefix used before the heading. Name size Type string Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" . Name level Type integer Description Optional heading level. Defaults to 2 . Name classes Type string Description Classes to add to the heading. Name attributes Type object Description HTML attributes (for example data attributes) to add to the heading. Options for image object Name Type Description Name src Type string Description Required. The URL of the image in the card. Name alt Type string Description The alternative text of the image in the card. Name html Type string Description HTML to use for the image content. If html is provided, the src and alt options will be ignored. Options for description object Name Type Description Name text Type string Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored. Name classes Type string Description Classes to add to the card content. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card content. Options for actions object Name Type Description Name items Type array Description Array of actions as links for use in the card component. See macro options for actions items . Name classes Type string Description Classes to add to the actions wrapper. Options for actions items array objects Name Type Description Name id Type string Description The ID of the action item. Name text Type string Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios. Name name Type string Description Name for the action as a button. If href is provided, this has no effect. Name type Type string Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The value attribute for the action as a button. If href is provided, this has no effect. Name href Type string Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided. Name classes Type string Description Classes to add to the action item. Name attributes Type object Description HTML attributes (for example data attributes) to add to the action item. Copy code {% from "card/macro.njk" import card %} {% set cardDescriptionHtml %} < p > < strong > SenderID </ strong > : NHS Blood Test </ p > < p > ((firstName)) ((lastName)), you are due for your NHS blood test. Book your appointment or find out more at < a href = "#" > http://www.nhs.uk/service-name-invite </ a > </ p > {% endset %} {{ card ({ heading : { text : "Template: Appointment invitation 1" , size : "m" }, actions : { items : [ { text : "Edit" , href : "#" }, { text : "Delete" , href : "#" } ] }, description : { html : cardDescriptionHtml }, clickable : false }) }} Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card card actions Add a short, relevant and unique card heading which identifies what the card contains. When a screen reader reads out a card action, it also reads out the card heading, making each action link unique. Write link text that makes it clear what will happen when you click the action. Keep it short and do not add more than 3 actions. Examples of card actions include: delete appointment edit appointment update issue approve application cancel order If the card title includes the word "appointment", for example, you may only need the words "edit" or "delete" in the link text. If a card action cannot easily be undone or might have serious consequences, consider adding a warning or asking the user for confirmation. Grouping cards You can group multiple cards to show a collection of related topics or highlight key information and figures. If you are grouping cards to create a hub page (sometimes called a landing page), use the hub page pattern . Card width We define the width of the cards using the grid system. For example, nhsuk-grid-column-one-half is used to make the cards half width. Open this example in a new tab : card group half HTML code for card group half Nunjucks code for card group half HTML code for card group half Copy code < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-one-half nhsuk-card-group__item" > < div class = "nhsuk-card nhsuk-card--clickable nhsuk-card--primary" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-heading-m" > < a class = "nhsuk-card__link" href = "#" > GPs </ a > </ h2 > < p class = "nhsuk-card__description" > About GP services, including how to find and register with a local GP and how to book an appointment </ p > < svg class = "nhsuk-icon nhsuk-icon--chevron-right-circle" xmlns = "http://www.w3.org/2000/svg" viewBox = "0 0 24 24" width = "16" height = "16" focusable = "false" aria-hidden = "true" > < path d = "M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-.3 5.8a1 1 0 1 0-1.5 1.4l2.9 2.8-2.9 2.8a1 1 0 0 0 1.5 1.4l3.5-3.5c.4-.4.4-1 0-1.4Z" /> </ svg > </ div > </ div > </ li > < li class = "nhsuk-grid-column-one-half nhsuk-card-group__item" > < div class = "nhsuk-card nhsuk-card--clickable nhsuk-card--primary" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-heading-m" > < a class = "nhsuk-card__link" href = "#" > Hospitals </ a > </ h2 > < p class = "nhsuk-card__description" > About NHS hospitals, booking and changing appointments with the NHS e-Referral Service and going into hospital </ p > < svg class = "nhsuk-icon nhsuk-icon--chevron-right-circle" xmlns = "http://www.w3.org/2000/svg" viewBox = "0 0 24 24" width = "16" height = "16" focusable = "false" aria-hidden = "true" > < path d = "M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-.3 5.8a1 1 0 1 0-1.5 1.4l2.9 2.8-2.9 2.8a1 1 0 0 0 1.5 1.4l3.5-3.5c.4-.4.4-1 0-1.4Z" /> </ svg > </ div > </ div > </ li > < li class = "nhsuk-grid-column-one-half nhsuk-card-group__item" > < div class = "nhsuk-card nhsuk-card--clickable nhsuk-card--primary" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-heading-m" > < a class = "nhsuk-card__link" href = "#" > Dentists </ a > </ h2 > < p class = "nhsuk-card__description" > About NHS dental services, how to find an NHS dentist and how much treatment costs </ p > < svg class = "nhsuk-icon nhsuk-icon--chevron-right-circle" xmlns = "http://www.w3.org/2000/svg" viewBox = "0 0 24 24" width = "16" height = "16" focusable = "false" aria-hidden = "true" > < path d = "M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-.3 5.8a1 1 0 1 0-1.5 1.4l2.9 2.8-2.9 2.8a1 1 0 0 0 1.5 1.4l3.5-3.5c.4-.4.4-1 0-1.4Z" /> </ svg > </ div > </ div > </ li > < li class = "nhsuk-grid-column-one-half nhsuk-card-group__item" > < div class = "nhsuk-card nhsuk-card--clickable nhsuk-card--primary" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-heading-m" > < a class = "nhsuk-card__link" href = "#" > Prescriptions </ a > </ h2 > < p class = "nhsuk-card__description" > Find out about prescriptions including charges, repeat prescriptions and if you can get free prescriptions </ p > < svg class = "nhsuk-icon nhsuk-icon--chevron-right-circle" xmlns = "http://www.w3.org/2000/svg" viewBox = "0 0 24 24" width = "16" height = "16" focusable = "false" aria-hidden = "true" > < path d = "M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-.3 5.8a1 1 0 1 0-1.5 1.4l2.9 2.8-2.9 2.8a1 1 0 0 0 1.5 1.4l3.5-3.5c.4-.4.4-1 0-1.4Z" /> </ svg > </ div > </ div > </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card group half Nunjucks code for card group half Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the card. Name heading Type object Description Required. Heading of the card component. See macro options for heading . Name heading Html Type string Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option. Name heading Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option. Name heading Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option. Name heading Level Type integer Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option. Name heading Id Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option. Name heading Visually Hidden Text Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option. Name href Type string Description The card link href attribute. Name clickable Type boolean Description If set to true , then the whole card will become a clickable card variant. Name variant Type string Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" . Name type Type string Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option. Name feature Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option. Name primary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option. Name secondary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option. Name warning Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option. Name img U R L Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option. Name img A L T Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option. Name image Type object Description Can be used to add an image to the card component. See macro options for image . Name description Type object Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description . Name description Html Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option. Name actions Type object Description Can be used to add actions to the card component. See macro options for actions . Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block. Name classes Type string Description Classes to add to the card. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card. Options for heading component Name Type Description Name id Type string Description The ID of the heading. Name text Type string Description Required. If html is set, this is not required. Text for the heading. Name html Type string Description Required. If text is set, this is not required. HTML for the heading. Name visually Hidden Text Type string Description Optional visually hidden prefix used before the heading. Name size Type string Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" . Name level Type integer Description Optional heading level. Defaults to 2 . Name classes Type string Description Classes to add to the heading. Name attributes Type object Description HTML attributes (for example data attributes) to add to the heading. Options for image object Name Type Description Name src Type string Description Required. The URL of the image in the card. Name alt Type string Description The alternative text of the image in the card. Name html Type string Description HTML to use for the image content. If html is provided, the src and alt options will be ignored. Options for description object Name Type Description Name text Type string Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored. Name classes Type string Description Classes to add to the card content. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card content. Options for actions object Name Type Description Name items Type array Description Array of actions as links for use in the card component. See macro options for actions items . Name classes Type string Description Classes to add to the actions wrapper. Options for actions items array objects Name Type Description Name id Type string Description The ID of the action item. Name text Type string Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios. Name name Type string Description Name for the action as a button. If href is provided, this has no effect. Name type Type string Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The value attribute for the action as a button. If href is provided, this has no effect. Name href Type string Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided. Name classes Type string Description Classes to add to the action item. Name attributes Type object Description HTML attributes (for example data attributes) to add to the action item. Copy code {% from "card/macro.njk" import card %} < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-one-half nhsuk-card-group__item" > {{ card ({ heading : { text : "GPs" , size : "m" }, description : "About GP services, including how to find and register with a local GP and how to book an appointment" , href : "#" , clickable : true , variant : "primary" }) }} </ li > < li class = "nhsuk-grid-column-one-half nhsuk-card-group__item" > {{ card ({ heading : { text : "Hospitals" , size : "m" }, description : "About NHS hospitals, booking and changing appointments with the NHS e-Referral Service and going into hospital" , href : "#" , clickable : true , variant : "primary" }) }} </ li > < li class = "nhsuk-grid-column-one-half nhsuk-card-group__item" > {{ card ({ heading : { text : "Dentists" , size : "m" }, description : "About NHS dental services, how to find an NHS dentist and how much treatment costs" , href : "#" , clickable : true , variant : "primary" }) }} </ li > < li class = "nhsuk-grid-column-one-half nhsuk-card-group__item" > {{ card ({ heading : { text : "Prescriptions" , size : "m" }, description : "Find out about prescriptions including charges, repeat prescriptions and if you can get free prescriptions" , href : "#" , clickable : true , variant : "primary" }) }} </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card group half For thirds, use nhsuk-grid-column-one-third . Open this example in a new tab : card group third HTML code for card group third Nunjucks code for card group third HTML code for card group third Copy code < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-one-third nhsuk-card-group__item" > < div class = "nhsuk-card nhsuk-card--clickable" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-heading-m" > < a class = "nhsuk-card__link" href = "#" > 5 steps to mental wellbeing </ a > </ h2 > < p class = "nhsuk-card__description" > Practical advice to help you feel mentally and emotionally better </ p > </ div > </ div > </ li > < li class = "nhsuk-grid-column-one-third nhsuk-card-group__item" > < div class = "nhsuk-card nhsuk-card--clickable" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-heading-m" > < a class = "nhsuk-card__link" href = "#" > Healthy weight </ a > </ h2 > < p class = "nhsuk-card__description" > Check your BMI using our healthy weight calculator and find out if you &#39; re a healthy weight </ p > </ div > </ div > </ li > < li class = "nhsuk-grid-column-one-third nhsuk-card-group__item" > < div class = "nhsuk-card nhsuk-card--clickable" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-heading-m" > < a class = "nhsuk-card__link" href = "#" > Exercise </ a > </ h2 > < p class = "nhsuk-card__description" > Programmes, workouts and tips to get you moving and improve your fitness and wellbeing </ p > </ div > </ div > </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card group third Nunjucks code for card group third Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the card. Name heading Type object Description Required. Heading of the card component. See macro options for heading . Name heading Html Type string Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option. Name heading Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option. Name heading Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option. Name heading Level Type integer Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option. Name heading Id Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option. Name heading Visually Hidden Text Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option. Name href Type string Description The card link href attribute. Name clickable Type boolean Description If set to true , then the whole card will become a clickable card variant. Name variant Type string Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" . Name type Type string Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option. Name feature Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option. Name primary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option. Name secondary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option. Name warning Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option. Name img U R L Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option. Name img A L T Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option. Name image Type object Description Can be used to add an image to the card component. See macro options for image . Name description Type object Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description . Name description Html Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option. Name actions Type object Description Can be used to add actions to the card component. See macro options for actions . Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block. Name classes Type string Description Classes to add to the card. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card. Options for heading component Name Type Description Name id Type string Description The ID of the heading. Name text Type string Description Required. If html is set, this is not required. Text for the heading. Name html Type string Description Required. If text is set, this is not required. HTML for the heading. Name visually Hidden Text Type string Description Optional visually hidden prefix used before the heading. Name size Type string Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" . Name level Type integer Description Optional heading level. Defaults to 2 . Name classes Type string Description Classes to add to the heading. Name attributes Type object Description HTML attributes (for example data attributes) to add to the heading. Options for image object Name Type Description Name src Type string Description Required. The URL of the image in the card. Name alt Type string Description The alternative text of the image in the card. Name html Type string Description HTML to use for the image content. If html is provided, the src and alt options will be ignored. Options for description object Name Type Description Name text Type string Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored. Name classes Type string Description Classes to add to the card content. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card content. Options for actions object Name Type Description Name items Type array Description Array of actions as links for use in the card component. See macro options for actions items . Name classes Type string Description Classes to add to the actions wrapper. Options for actions items array objects Name Type Description Name id Type string Description The ID of the action item. Name text Type string Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios. Name name Type string Description Name for the action as a button. If href is provided, this has no effect. Name type Type string Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The value attribute for the action as a button. If href is provided, this has no effect. Name href Type string Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided. Name classes Type string Description Classes to add to the action item. Name attributes Type object Description HTML attributes (for example data attributes) to add to the action item. Copy code {% from "card/macro.njk" import card %} < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-one-third nhsuk-card-group__item" > {{ card ({ heading : { text : "5 steps to mental wellbeing" , size : "m" }, description : "Practical advice to help you feel mentally and emotionally better" , href : "#" , clickable : true }) }} </ li > < li class = "nhsuk-grid-column-one-third nhsuk-card-group__item" > {{ card ({ heading : { text : "Healthy weight" , size : "m" }, description : "Check your BMI using our healthy weight calculator and find out if you're a healthy weight" , href : "#" , clickable : true }) }} </ li > < li class = "nhsuk-grid-column-one-third nhsuk-card-group__item" > {{ card ({ heading : { text : "Exercise" , size : "m" }, description : "Programmes, workouts and tips to get you moving and improve your fitness and wellbeing" , href : "#" , clickable : true }) }} </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card group third When using thirds or quarters, check your content on smaller screens as the cards become narrow. Avoid adding paragraphs of text that will become hard to read. For quarters, use nhsuk-grid-column-one-quarter . Open this example in a new tab : card group quarter HTML code for card group quarter Nunjucks code for card group quarter HTML code for card group quarter Copy code < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-one-quarter nhsuk-card-group__item" > < div class = "nhsuk-card nhsuk-card--clickable" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1" > < span role = "text" > < span class = "nhsuk-u-visually-hidden" > Applicants: </ span > 91 </ span > </ h2 > < a href = "#/applicants" class = "nhsuk-card__link" > Applicants </ a > </ div > </ div > </ li > < li class = "nhsuk-grid-column-one-quarter nhsuk-card-group__item" > < div class = "nhsuk-card nhsuk-card--clickable" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1" > < span role = "text" > < span class = "nhsuk-u-visually-hidden" > Jobs: </ span > 23 </ span > </ h2 > < a href = "#/jobs" class = "nhsuk-card__link" > Jobs </ a > </ div > </ div > </ li > < li class = "nhsuk-grid-column-one-quarter nhsuk-card-group__item" > < div class = "nhsuk-card nhsuk-card--clickable" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1" > < span role = "text" > < span class = "nhsuk-u-visually-hidden" > Services: </ span > 8 </ span > </ h2 > < a href = "#/services" class = "nhsuk-card__link" > Services </ a > </ div > </ div > </ li > < li class = "nhsuk-grid-column-one-quarter nhsuk-card-group__item" > < div class = "nhsuk-card nhsuk-card--clickable" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1" > < span role = "text" > < span class = "nhsuk-u-visually-hidden" > Messages: </ span > 33 </ span > </ h2 > < a href = "#/messages" class = "nhsuk-card__link" > Messages </ a > </ div > </ div > </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card group quarter Nunjucks code for card group quarter Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the card. Name heading Type object Description Required. Heading of the card component. See macro options for heading . Name heading Html Type string Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option. Name heading Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option. Name heading Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option. Name heading Level Type integer Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option. Name heading Id Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option. Name heading Visually Hidden Text Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option. Name href Type string Description The card link href attribute. Name clickable Type boolean Description If set to true , then the whole card will become a clickable card variant. Name variant Type string Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" . Name type Type string Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option. Name feature Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option. Name primary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option. Name secondary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option. Name warning Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option. Name img U R L Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option. Name img A L T Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option. Name image Type object Description Can be used to add an image to the card component. See macro options for image . Name description Type object Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description . Name description Html Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option. Name actions Type object Description Can be used to add actions to the card component. See macro options for actions . Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block. Name classes Type string Description Classes to add to the card. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card. Options for heading component Name Type Description Name id Type string Description The ID of the heading. Name text Type string Description Required. If html is set, this is not required. Text for the heading. Name html Type string Description Required. If text is set, this is not required. HTML for the heading. Name visually Hidden Text Type string Description Optional visually hidden prefix used before the heading. Name size Type string Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" . Name level Type integer Description Optional heading level. Defaults to 2 . Name classes Type string Description Classes to add to the heading. Name attributes Type object Description HTML attributes (for example data attributes) to add to the heading. Options for image object Name Type Description Name src Type string Description Required. The URL of the image in the card. Name alt Type string Description The alternative text of the image in the card. Name html Type string Description HTML to use for the image content. If html is provided, the src and alt options will be ignored. Options for description object Name Type Description Name text Type string Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored. Name classes Type string Description Classes to add to the card content. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card content. Options for actions object Name Type Description Name items Type array Description Array of actions as links for use in the card component. See macro options for actions items . Name classes Type string Description Classes to add to the actions wrapper. Options for actions items array objects Name Type Description Name id Type string Description The ID of the action item. Name text Type string Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios. Name name Type string Description Name for the action as a button. If href is provided, this has no effect. Name type Type string Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The value attribute for the action as a button. If href is provided, this has no effect. Name href Type string Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided. Name classes Type string Description Classes to add to the action item. Name attributes Type object Description HTML attributes (for example data attributes) to add to the action item. Copy code {% from "card/macro.njk" import card %} < ul class = "nhsuk-grid-row nhsuk-card-group" > < li class = "nhsuk-grid-column-one-quarter nhsuk-card-group__item" > {% call card ({ heading : { text : "91" , visuallyHiddenText : "Applicants" , classes : "nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1" }, clickable : true }) %} < a href = "#/applicants" class = "nhsuk-card__link" > Applicants </ a > {% endcall %} </ li > < li class = "nhsuk-grid-column-one-quarter nhsuk-card-group__item" > {% call card ({ heading : { text : "23" , visuallyHiddenText : "Jobs" , classes : "nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1" }, clickable : true }) %} < a href = "#/jobs" class = "nhsuk-card__link" > Jobs </ a > {% endcall %} </ li > < li class = "nhsuk-grid-column-one-quarter nhsuk-card-group__item" > {% call card ({ heading : { text : "8" , visuallyHiddenText : "Services" , classes : "nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1" }, clickable : true }) %} < a href = "#/services" class = "nhsuk-card__link" > Services </ a > {% endcall %} </ li > < li class = "nhsuk-grid-column-one-quarter nhsuk-card-group__item" > {% call card ({ heading : { text : "33" , visuallyHiddenText : "Messages" , classes : "nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1" }, clickable : true }) %} < a href = "#/messages" class = "nhsuk-card__link" > Messages </ a > {% endcall %} </ li > </ ul > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card group quarter Accessibility Heading level and size Use headings correctly to reflect the page structure. If you need to, change the default h2 heading. Here's an example of replacing the default h2 heading with an h3 . Open this example in a new tab : card heading level HTML code for card heading level Nunjucks code for card heading level HTML code for card heading level Copy code < div class = "nhsuk-card" > < div class = "nhsuk-card__content" > < h3 class = "nhsuk-card__heading" > Heading level 3 </ h3 > < p class = "nhsuk-card__description" > Card description text goes here </ p > </ div > </ div > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card heading level Nunjucks code for card heading level Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the card. Name heading Type object Description Required. Heading of the card component. See macro options for heading . Name heading Html Type string Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option. Name heading Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option. Name heading Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option. Name heading Level Type integer Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option. Name heading Id Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option. Name heading Visually Hidden Text Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option. Name href Type string Description The card link href attribute. Name clickable Type boolean Description If set to true , then the whole card will become a clickable card variant. Name variant Type string Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" . Name type Type string Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option. Name feature Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option. Name primary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option. Name secondary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option. Name warning Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option. Name img U R L Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option. Name img A L T Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option. Name image Type object Description Can be used to add an image to the card component. See macro options for image . Name description Type object Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description . Name description Html Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option. Name actions Type object Description Can be used to add actions to the card component. See macro options for actions . Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block. Name classes Type string Description Classes to add to the card. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card. Options for heading component Name Type Description Name id Type string Description The ID of the heading. Name text Type string Description Required. If html is set, this is not required. Text for the heading. Name html Type string Description Required. If text is set, this is not required. HTML for the heading. Name visually Hidden Text Type string Description Optional visually hidden prefix used before the heading. Name size Type string Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" . Name level Type integer Description Optional heading level. Defaults to 2 . Name classes Type string Description Classes to add to the heading. Name attributes Type object Description HTML attributes (for example data attributes) to add to the heading. Options for image object Name Type Description Name src Type string Description Required. The URL of the image in the card. Name alt Type string Description The alternative text of the image in the card. Name html Type string Description HTML to use for the image content. If html is provided, the src and alt options will be ignored. Options for description object Name Type Description Name text Type string Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored. Name classes Type string Description Classes to add to the card content. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card content. Options for actions object Name Type Description Name items Type array Description Array of actions as links for use in the card component. See macro options for actions items . Name classes Type string Description Classes to add to the actions wrapper. Options for actions items array objects Name Type Description Name id Type string Description The ID of the action item. Name text Type string Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios. Name name Type string Description Name for the action as a button. If href is provided, this has no effect. Name type Type string Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The value attribute for the action as a button. If href is provided, this has no effect. Name href Type string Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided. Name classes Type string Description Classes to add to the action item. Name attributes Type object Description HTML attributes (for example data attributes) to add to the action item. Copy code {% from "card/macro.njk" import card %} {{ card ({ heading : { text : "Heading level 3" , level : 3 }, description : "Card description text goes here" }) }} Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card heading level You can change the size of the heading using heading typography styles . When using Nunjucks, you can set the size of card headings using the size option, for example: size: "s" . You can use sizes xxs , xs , s , m , l , xl . Open this example in a new tab : card heading size HTML code for card heading size Nunjucks code for card heading size HTML code for card heading size Copy code < div class = "nhsuk-card" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-heading-l" > Heading size large </ h2 > < p class = "nhsuk-card__description" > Card description text goes here </ p > </ div > </ div > < div class = "nhsuk-card" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-heading-m" > Heading size medium </ h2 > < p class = "nhsuk-card__description" > Card description text goes here </ p > </ div > </ div > < div class = "nhsuk-card" > < div class = "nhsuk-card__content" > < h2 class = "nhsuk-card__heading nhsuk-heading-s" > Heading size small </ h2 > < p class = "nhsuk-card__description" > Card description text goes here </ p > </ div > </ div > Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card heading size Nunjucks code for card heading size Nunjucks macro options Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text. Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated". If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits . Primary options Name Type Description Name id Type string Description The ID of the card. Name heading Type object Description Required. Heading of the card component. See macro options for heading . Name heading Html Type string Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option. Name heading Classes Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option. Name heading Size Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option. Name heading Level Type integer Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option. Name heading Id Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option. Name heading Visually Hidden Text Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option. Name href Type string Description The card link href attribute. Name clickable Type boolean Description If set to true , then the whole card will become a clickable card variant. Name variant Type string Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" . Name type Type string Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option. Name feature Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option. Name primary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option. Name secondary Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option. Name warning Type boolean Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option. Name img U R L Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option. Name img A L T Type string Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option. Name image Type object Description Can be used to add an image to the card component. See macro options for image . Name description Type object Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description . Name description Html Type string Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option. Name actions Type object Description Can be used to add actions to the card component. See macro options for actions . Name caller Type nunjucks-block Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block. Name classes Type string Description Classes to add to the card. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card. Options for heading component Name Type Description Name id Type string Description The ID of the heading. Name text Type string Description Required. If html is set, this is not required. Text for the heading. Name html Type string Description Required. If text is set, this is not required. HTML for the heading. Name visually Hidden Text Type string Description Optional visually hidden prefix used before the heading. Name size Type string Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" . Name level Type integer Description Optional heading level. Defaults to 2 . Name classes Type string Description Classes to add to the heading. Name attributes Type object Description HTML attributes (for example data attributes) to add to the heading. Options for image object Name Type Description Name src Type string Description Required. The URL of the image in the card. Name alt Type string Description The alternative text of the image in the card. Name html Type string Description HTML to use for the image content. If html is provided, the src and alt options will be ignored. Options for description object Name Type Description Name text Type string Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored. Name classes Type string Description Classes to add to the card content. Name attributes Type object Description HTML attributes (for example data attributes) to add to the card content. Options for actions object Name Type Description Name items Type array Description Array of actions as links for use in the card component. See macro options for actions items . Name classes Type string Description Classes to add to the actions wrapper. Options for actions items array objects Name Type Description Name id Type string Description The ID of the action item. Name text Type string Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored. Name html Type string Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored. Name visually Hidden Text Type string Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios. Name name Type string Description Name for the action as a button. If href is provided, this has no effect. Name type Type string Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided. Name value Type string Description The value attribute for the action as a button. If href is provided, this has no effect. Name href Type string Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided. Name classes Type string Description Classes to add to the action item. Name attributes Type object Description HTML attributes (for example data attributes) to add to the action item. Copy code {% from "card/macro.njk" import card %} {{ card ({ heading : { text : "Heading size large" , size : "l" }, description : "Card description text goes here" }) }} {{ card ({ heading : { text : "Heading size medium" , size : "m" }, description : "Card description text goes here" }) }} {{ card ({ heading : { text : "Heading size small" , size : "s" }, description : "Card description text goes here" }) }} Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend Close : card heading size Research We have tested cards on the NHS website, summary care record and NHS login help centre. We found that they helped users: scan for relevant information decide where to go next Help us improve this guidance Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public. Feed back or share insights on GitHub Read more about how to feed back or share insights . If you have any questions, get in touch with the service manual team. Updates to this page Updated: June 2026

- primary card

- secondary card

Both cards can be clickable or non-clickable.

A card can include different elements, such as:

- a heading

- text

- a link or links

You can also add an image or add actions . If you include a link, the link should mirror the heading of the page it links to.

For clickable cards, avoid wrapping the entire card in an anchor tag as this can be a difficult experience for screen reader users.

Keep the card short so it is easy to scan for relevant and actionable information.

### Primary card

Primary cards are more visually prominent than secondary cards.

#### Primary card clickable

- HTML code for card primary card clickable

- Nunjucks code for card primary card clickable

```text
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-quarter nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable"
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
"nhsuk-card__heading nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1"
>
<
span
role
=
"text"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Applicants:
</
span
>
91
</
span
>
</
h2
>
<
a
href
=
"#/applicants"
class
=
"nhsuk-card__link"
>
Applicants
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
Name id | Type string | Description The ID of the card.
Name heading | Type object | Description Required. Heading of the card component. See macro options for heading .
Name heading Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name heading Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option.
Name heading Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option.
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name heading Id | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option.
Name heading Visually Hidden Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option.
Name href | Type string | Description The card link href attribute.
Name clickable | Type boolean | Description If set to true , then the whole card will become a clickable card variant.
Name variant | Type string | Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option.
Name feature | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option.
Name primary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option.
Name secondary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option.
Name warning | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option.
Name img U R L | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option.
Name img A L T | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option.
Name image | Type object | Description Can be used to add an image to the card component. See macro options for image .
Name description | Type object | Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description .
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name actions | Type object | Description Can be used to add actions to the card component. See macro options for actions .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block.
Name classes | Type string | Description Classes to add to the card.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading.
Name visually Hidden Text | Type string | Description Optional visually hidden prefix used before the heading.
Name size | Type string | Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" .
Name level | Type integer | Description Optional heading level. Defaults to 2 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name src | Type string | Description Required. The URL of the image in the card.
Name alt | Type string | Description The alternative text of the image in the card.
Name html | Type string | Description HTML to use for the image content. If html is provided, the src and alt options will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the card content.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card content.

Name | Type | Description
Name items | Type array | Description Array of actions as links for use in the card component. See macro options for actions items .
Name classes | Type string | Description Classes to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If href is provided, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If href is provided, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"card/macro.njk"
import
card
%}
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-quarter nhsuk-card-group__item"
>
{%
call
card
({
heading
: {
text
:
"91"
,
visuallyHiddenText
:
"Applicants"
,
classes
:
"nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1"
},
clickable
:
true
}) %}
<
a
href
=
"#/applicants"
class
=
"nhsuk-card__link"
>
Applicants
</
a
>
{%
endcall
%}
</
li
>
</
ul
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

#### Primary card with chevron

The chevron icon on this primary card makes it even more prominent.

There is only a clickable version of this card.

Read about how to use primary cards with chevrons in the hub page pattern .

- HTML code for card primary card

- Nunjucks code for card primary card

```text
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-two-thirds nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable nhsuk-card--primary"
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
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
GPs
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
About GP services, including how to find and register with a local GP and how to book an appointment
</
p
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--chevron-right-circle"
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
"M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-.3 5.8a1 1 0 1 0-1.5 1.4l2.9 2.8-2.9 2.8a1 1 0 0 0 1.5 1.4l3.5-3.5c.4-.4.4-1 0-1.4Z"
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
Name id | Type string | Description The ID of the card.
Name heading | Type object | Description Required. Heading of the card component. See macro options for heading .
Name heading Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name heading Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option.
Name heading Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option.
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name heading Id | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option.
Name heading Visually Hidden Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option.
Name href | Type string | Description The card link href attribute.
Name clickable | Type boolean | Description If set to true , then the whole card will become a clickable card variant.
Name variant | Type string | Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option.
Name feature | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option.
Name primary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option.
Name secondary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option.
Name warning | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option.
Name img U R L | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option.
Name img A L T | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option.
Name image | Type object | Description Can be used to add an image to the card component. See macro options for image .
Name description | Type object | Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description .
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name actions | Type object | Description Can be used to add actions to the card component. See macro options for actions .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block.
Name classes | Type string | Description Classes to add to the card.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading.
Name visually Hidden Text | Type string | Description Optional visually hidden prefix used before the heading.
Name size | Type string | Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" .
Name level | Type integer | Description Optional heading level. Defaults to 2 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name src | Type string | Description Required. The URL of the image in the card.
Name alt | Type string | Description The alternative text of the image in the card.
Name html | Type string | Description HTML to use for the image content. If html is provided, the src and alt options will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the card content.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card content.

Name | Type | Description
Name items | Type array | Description Array of actions as links for use in the card component. See macro options for actions items .
Name classes | Type string | Description Classes to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If href is provided, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If href is provided, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"card/macro.njk"
import
card
%}
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-two-thirds nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"GPs"
,
size
:
"m"
},
description
:
"About GP services, including how to find and register with a local GP and how to book an appointment"
,
href
:
"#"
,
clickable
:
true
,
variant
:
"primary"
})
}}
</
li
>
</
ul
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

#### Primary card non-clickable

Use the non-clickable card when you are using more than 1 link.

- HTML code for card primary card non clickable

- Nunjucks code for card primary card non clickable

```text
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-two-thirds nhsuk-card-group__item"
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
<
a
class
=
"nhsuk-card__link"
href
=
"/#"
>
Berrylands Pharmacy
</
a
>
</
h2
>
<
p
>
Ewell Road, Surbiton, KT6 6EZ
<
br
/>
Phone:
<
a
href
=
"#"
>
01111 111 111
</
a
>
<
br
/>
Email:
<
a
href
=
"#"
>
organisation@nhs.net
</
a
>
</
p
>
<
p
>
<
a
href
=
"#"
>
Get directions (opens in Google Maps)
</
a
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
Name id | Type string | Description The ID of the card.
Name heading | Type object | Description Required. Heading of the card component. See macro options for heading .
Name heading Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name heading Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option.
Name heading Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option.
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name heading Id | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option.
Name heading Visually Hidden Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option.
Name href | Type string | Description The card link href attribute.
Name clickable | Type boolean | Description If set to true , then the whole card will become a clickable card variant.
Name variant | Type string | Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option.
Name feature | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option.
Name primary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option.
Name secondary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option.
Name warning | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option.
Name img U R L | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option.
Name img A L T | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option.
Name image | Type object | Description Can be used to add an image to the card component. See macro options for image .
Name description | Type object | Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description .
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name actions | Type object | Description Can be used to add actions to the card component. See macro options for actions .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block.
Name classes | Type string | Description Classes to add to the card.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading.
Name visually Hidden Text | Type string | Description Optional visually hidden prefix used before the heading.
Name size | Type string | Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" .
Name level | Type integer | Description Optional heading level. Defaults to 2 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name src | Type string | Description Required. The URL of the image in the card.
Name alt | Type string | Description The alternative text of the image in the card.
Name html | Type string | Description HTML to use for the image content. If html is provided, the src and alt options will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the card content.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card content.

Name | Type | Description
Name items | Type array | Description Array of actions as links for use in the card component. See macro options for actions items .
Name classes | Type string | Description Classes to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If href is provided, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If href is provided, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"card/macro.njk"
import
card
%}
{%
set
cardDescriptionHtml
%}
<
p
>
Ewell Road, Surbiton, KT6 6EZ
<
br
/>
Phone:
<
a
href
=
"#"
>
01111 111 111
</
a
>
<
br
/>
Email:
<
a
href
=
"#"
>
organisation@nhs.net
</
a
>
</
p
>
<
p
>
<
a
href
=
"#"
>
Get directions (opens in Google Maps)
</
a
>
</
p
>
{%
endset
%}
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-two-thirds nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"Berrylands Pharmacy"
,
size
:
"m"
},
description
: {
html
: cardDescriptionHtml
      },
href
:
"/#"
,
clickable
:
false
})
}}
</
li
>
</
ul
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Secondary card

The secondary card has less visual impact than the primary cards.

When used with other cards, use the secondary card to group less important content or actions.

#### Secondary card clickable

This card is also used in the hub page pattern .

- HTML code for card secondary card

- Nunjucks code for card secondary card

```text
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-two-thirds nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable nhsuk-card--secondary"
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
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
Services A to Z
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
Use our service finder to find other health services
</
p
>
</
div
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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the card.
Name heading | Type object | Description Required. Heading of the card component. See macro options for heading .
Name heading Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name heading Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option.
Name heading Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option.
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name heading Id | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option.
Name heading Visually Hidden Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option.
Name href | Type string | Description The card link href attribute.
Name clickable | Type boolean | Description If set to true , then the whole card will become a clickable card variant.
Name variant | Type string | Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option.
Name feature | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option.
Name primary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option.
Name secondary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option.
Name warning | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option.
Name img U R L | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option.
Name img A L T | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option.
Name image | Type object | Description Can be used to add an image to the card component. See macro options for image .
Name description | Type object | Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description .
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name actions | Type object | Description Can be used to add actions to the card component. See macro options for actions .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block.
Name classes | Type string | Description Classes to add to the card.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading.
Name visually Hidden Text | Type string | Description Optional visually hidden prefix used before the heading.
Name size | Type string | Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" .
Name level | Type integer | Description Optional heading level. Defaults to 2 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name src | Type string | Description Required. The URL of the image in the card.
Name alt | Type string | Description The alternative text of the image in the card.
Name html | Type string | Description HTML to use for the image content. If html is provided, the src and alt options will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the card content.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card content.

Name | Type | Description
Name items | Type array | Description Array of actions as links for use in the card component. See macro options for actions items .
Name classes | Type string | Description Classes to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If href is provided, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If href is provided, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"card/macro.njk"
import
card
%}
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-two-thirds nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"Services A to Z"
,
size
:
"m"
},
description
:
"Use our service finder to find other health services"
,
href
:
"#"
,
clickable
:
true
,
variant
:
"secondary"
})
}}
</
li
>
</
ul
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

#### Secondary card non-clickable

Use the non-clickable card when you have more than 1 link in the content.

- HTML code for card secondary card non clickable

- Nunjucks code for card secondary card non clickable

```text
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-two-thirds nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--secondary"
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
Help from NHS 111
</
h2
>
<
p
>
If you're worried about a symptom and not sure what help you need, NHS 111 can tell you what to do next.
</
p
>
<
p
>
Go to
<
a
href
=
"#"
>
NHS 111 online
</
a
>
or
<
a
href
=
"#"
>
call 111
</
a
>
.
</
p
>
<
p
>
For a life-threatening emergency call 999.
</
p
>
</
div
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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the card.
Name heading | Type object | Description Required. Heading of the card component. See macro options for heading .
Name heading Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name heading Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option.
Name heading Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option.
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name heading Id | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option.
Name heading Visually Hidden Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option.
Name href | Type string | Description The card link href attribute.
Name clickable | Type boolean | Description If set to true , then the whole card will become a clickable card variant.
Name variant | Type string | Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option.
Name feature | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option.
Name primary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option.
Name secondary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option.
Name warning | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option.
Name img U R L | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option.
Name img A L T | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option.
Name image | Type object | Description Can be used to add an image to the card component. See macro options for image .
Name description | Type object | Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description .
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name actions | Type object | Description Can be used to add actions to the card component. See macro options for actions .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block.
Name classes | Type string | Description Classes to add to the card.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading.
Name visually Hidden Text | Type string | Description Optional visually hidden prefix used before the heading.
Name size | Type string | Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" .
Name level | Type integer | Description Optional heading level. Defaults to 2 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name src | Type string | Description Required. The URL of the image in the card.
Name alt | Type string | Description The alternative text of the image in the card.
Name html | Type string | Description HTML to use for the image content. If html is provided, the src and alt options will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the card content.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card content.

Name | Type | Description
Name items | Type array | Description Array of actions as links for use in the card component. See macro options for actions items .
Name classes | Type string | Description Classes to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If href is provided, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If href is provided, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"card/macro.njk"
import
card
%}
{%
set
cardDescriptionHtml
%}
<
p
>
If you're worried about a symptom and not sure what help you need, NHS 111 can tell you what to do next.
</
p
>
<
p
>
Go to
<
a
href
=
"#"
>
NHS 111 online
</
a
>
or
<
a
href
=
"#"
>
call 111
</
a
>
.
</
p
>
<
p
>
For a life-threatening emergency call 999.
</
p
>
{%
endset
%}
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-two-thirds nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"Help from NHS 111"
,
size
:
"m"
},
description
: {
html
: cardDescriptionHtml
      },
variant
:
"secondary"
})
}}
</
li
>
</
ul
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Adding an image

Only use cards with images if you have evidence that they help your users, for example, where you can show that they motivate users.

Images in a card will be displayed above the heading and text. The image is set as a decorative image by default, with the alternative text being null.

#### Image card clickable

- HTML code for card with image

- Nunjucks code for card with image

```text
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable"
>
<
img
class
=
"nhsuk-card__img"
src
=
"https://assets.nhs.uk/prod/images/A_0218_exercise-main_FKW1X7.width-690.jpg"
alt
=
""
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
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
Exercise
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
Programmes, workouts and tips to get you moving and improve your fitness and wellbeing
</
p
>
</
div
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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the card.
Name heading | Type object | Description Required. Heading of the card component. See macro options for heading .
Name heading Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name heading Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option.
Name heading Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option.
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name heading Id | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option.
Name heading Visually Hidden Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option.
Name href | Type string | Description The card link href attribute.
Name clickable | Type boolean | Description If set to true , then the whole card will become a clickable card variant.
Name variant | Type string | Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option.
Name feature | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option.
Name primary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option.
Name secondary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option.
Name warning | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option.
Name img U R L | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option.
Name img A L T | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option.
Name image | Type object | Description Can be used to add an image to the card component. See macro options for image .
Name description | Type object | Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description .
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name actions | Type object | Description Can be used to add actions to the card component. See macro options for actions .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block.
Name classes | Type string | Description Classes to add to the card.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading.
Name visually Hidden Text | Type string | Description Optional visually hidden prefix used before the heading.
Name size | Type string | Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" .
Name level | Type integer | Description Optional heading level. Defaults to 2 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name src | Type string | Description Required. The URL of the image in the card.
Name alt | Type string | Description The alternative text of the image in the card.
Name html | Type string | Description HTML to use for the image content. If html is provided, the src and alt options will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the card content.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card content.

Name | Type | Description
Name items | Type array | Description Array of actions as links for use in the card component. See macro options for actions items .
Name classes | Type string | Description Classes to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If href is provided, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If href is provided, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"card/macro.njk"
import
card
%}
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
{{
card
({
image
: {
src
:
"https://assets.nhs.uk/prod/images/A_0218_exercise-main_FKW1X7.width-690.jpg"
},
heading
: {
text
:
"Exercise"
,
size
:
"m"
},
description
:
"Programmes, workouts and tips to get you moving and improve your fitness and wellbeing"
,
href
:
"#"
,
clickable
:
true
})
}}
</
li
>
</
ul
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

#### Image card non-clickable

- HTML code for card with image non clickable

- Nunjucks code for card with image non clickable

```text
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card"
>
<
img
class
=
"nhsuk-card__img"
src
=
"https://assets.nhs.uk/prod/images/A_0218_exercise-main_FKW1X7.width-690.jpg"
alt
=
""
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
Exercise
</
h2
>
<
p
>
The
<
a
href
=
"#"
>
benefits of exercise
</
a
>
and
<
a
href
=
"#"
>
why we should sit less
</
a
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
Name id | Type string | Description The ID of the card.
Name heading | Type object | Description Required. Heading of the card component. See macro options for heading .
Name heading Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name heading Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option.
Name heading Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option.
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name heading Id | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option.
Name heading Visually Hidden Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option.
Name href | Type string | Description The card link href attribute.
Name clickable | Type boolean | Description If set to true , then the whole card will become a clickable card variant.
Name variant | Type string | Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option.
Name feature | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option.
Name primary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option.
Name secondary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option.
Name warning | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option.
Name img U R L | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option.
Name img A L T | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option.
Name image | Type object | Description Can be used to add an image to the card component. See macro options for image .
Name description | Type object | Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description .
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name actions | Type object | Description Can be used to add actions to the card component. See macro options for actions .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block.
Name classes | Type string | Description Classes to add to the card.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading.
Name visually Hidden Text | Type string | Description Optional visually hidden prefix used before the heading.
Name size | Type string | Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" .
Name level | Type integer | Description Optional heading level. Defaults to 2 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name src | Type string | Description Required. The URL of the image in the card.
Name alt | Type string | Description The alternative text of the image in the card.
Name html | Type string | Description HTML to use for the image content. If html is provided, the src and alt options will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the card content.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card content.

Name | Type | Description
Name items | Type array | Description Array of actions as links for use in the card component. See macro options for actions items .
Name classes | Type string | Description Classes to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If href is provided, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If href is provided, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"card/macro.njk"
import
card
%}
{%
set
cardDescriptionHtml
%}
<
p
>
The
<
a
href
=
"#"
>
benefits of exercise
</
a
>
and
<
a
href
=
"#"
>
why we should sit less
</
a
>
</
p
>
{%
endset
%}
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
{{
card
({
image
: {
src
:
"https://assets.nhs.uk/prod/images/A_0218_exercise-main_FKW1X7.width-690.jpg"
},
heading
: {
text
:
"Exercise"
,
size
:
"m"
},
description
: {
html
: cardDescriptionHtml
      },
clickable
:
false
})
}}
</
li
>
</
ul
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

### Adding actions

You can add links for 1 or more actions to a card. They show below the heading on small screens and right-aligned on bigger screens.

Card actions cannot be used on clickable cards.

They can be used in summary cards .

- HTML code for card card actions

- Nunjucks code for card card actions

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
Template: Appointment invitation 1
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
Edit
<
span
class
=
"nhsuk-u-visually-hidden"
>
(Template: Appointment invitation 1)
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
Delete
<
span
class
=
"nhsuk-u-visually-hidden"
>
(Template: Appointment invitation 1)
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
p
>
<
strong
>
SenderID
</
strong
>
: NHS Blood Test
</
p
>
<
p
>
((firstName)) ((lastName)), you are due for your NHS blood test. Book your appointment or find out more at
<
a
href
=
"#"
>
http://www.nhs.uk/service-name-invite
</
a
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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the card.
Name heading | Type object | Description Required. Heading of the card component. See macro options for heading .
Name heading Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name heading Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option.
Name heading Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option.
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name heading Id | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option.
Name heading Visually Hidden Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option.
Name href | Type string | Description The card link href attribute.
Name clickable | Type boolean | Description If set to true , then the whole card will become a clickable card variant.
Name variant | Type string | Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option.
Name feature | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option.
Name primary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option.
Name secondary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option.
Name warning | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option.
Name img U R L | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option.
Name img A L T | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option.
Name image | Type object | Description Can be used to add an image to the card component. See macro options for image .
Name description | Type object | Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description .
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name actions | Type object | Description Can be used to add actions to the card component. See macro options for actions .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block.
Name classes | Type string | Description Classes to add to the card.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading.
Name visually Hidden Text | Type string | Description Optional visually hidden prefix used before the heading.
Name size | Type string | Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" .
Name level | Type integer | Description Optional heading level. Defaults to 2 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name src | Type string | Description Required. The URL of the image in the card.
Name alt | Type string | Description The alternative text of the image in the card.
Name html | Type string | Description HTML to use for the image content. If html is provided, the src and alt options will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the card content.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card content.

Name | Type | Description
Name items | Type array | Description Array of actions as links for use in the card component. See macro options for actions items .
Name classes | Type string | Description Classes to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If href is provided, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If href is provided, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"card/macro.njk"
import
card
%}
{%
set
cardDescriptionHtml
%}
<
p
>
<
strong
>
SenderID
</
strong
>
: NHS Blood Test
</
p
>
<
p
>
((firstName)) ((lastName)), you are due for your NHS blood test. Book your appointment or find out more at
<
a
href
=
"#"
>
http://www.nhs.uk/service-name-invite
</
a
>
</
p
>
{%
endset
%}
{{
card
({
heading
: {
text
:
"Template: Appointment invitation 1"
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
"Edit"
,
href
:
"#"
},
      {
text
:
"Delete"
,
href
:
"#"
}
    ]
  },
description
: {
html
: cardDescriptionHtml
  },
clickable
:
false
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Add a short, relevant and unique card heading which identifies what the card contains. When a screen reader reads out a card action, it also reads out the card heading, making each action link unique.

Write link text that makes it clear what will happen when you click the action. Keep it short and do not add more than 3 actions.

Examples of card actions include:

- delete appointment

- edit appointment

- update issue

- approve application

- cancel order

If the card title includes the word "appointment", for example, you may only need the words "edit" or "delete" in the link text.

If a card action cannot easily be undone or might have serious consequences, consider adding a warning or asking the user for confirmation.

### Grouping cards

You can group multiple cards to show a collection of related topics or highlight key information and figures.

If you are grouping cards to create a hub page (sometimes called a landing page), use the hub page pattern .

#### Card width

We define the width of the cards using the grid system. For example, nhsuk-grid-column-one-half is used to make the cards half width.

- HTML code for card group half

- Nunjucks code for card group half

```text
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable nhsuk-card--primary"
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
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
GPs
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
About GP services, including how to find and register with a local GP and how to book an appointment
</
p
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--chevron-right-circle"
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
"M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-.3 5.8a1 1 0 1 0-1.5 1.4l2.9 2.8-2.9 2.8a1 1 0 0 0 1.5 1.4l3.5-3.5c.4-.4.4-1 0-1.4Z"
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
</
li
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable nhsuk-card--primary"
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
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
Hospitals
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
About NHS hospitals, booking and changing appointments with the NHS e-Referral Service and going into hospital
</
p
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--chevron-right-circle"
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
"M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-.3 5.8a1 1 0 1 0-1.5 1.4l2.9 2.8-2.9 2.8a1 1 0 0 0 1.5 1.4l3.5-3.5c.4-.4.4-1 0-1.4Z"
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
</
li
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable nhsuk-card--primary"
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
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
Dentists
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
About NHS dental services, how to find an NHS dentist and how much treatment costs
</
p
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--chevron-right-circle"
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
"M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-.3 5.8a1 1 0 1 0-1.5 1.4l2.9 2.8-2.9 2.8a1 1 0 0 0 1.5 1.4l3.5-3.5c.4-.4.4-1 0-1.4Z"
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
</
li
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable nhsuk-card--primary"
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
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
Prescriptions
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
Find out about prescriptions including charges, repeat prescriptions and if you can get free prescriptions
</
p
>
<
svg
class
=
"nhsuk-icon nhsuk-icon--chevron-right-circle"
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
"M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-.3 5.8a1 1 0 1 0-1.5 1.4l2.9 2.8-2.9 2.8a1 1 0 0 0 1.5 1.4l3.5-3.5c.4-.4.4-1 0-1.4Z"
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
Name id | Type string | Description The ID of the card.
Name heading | Type object | Description Required. Heading of the card component. See macro options for heading .
Name heading Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name heading Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option.
Name heading Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option.
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name heading Id | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option.
Name heading Visually Hidden Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option.
Name href | Type string | Description The card link href attribute.
Name clickable | Type boolean | Description If set to true , then the whole card will become a clickable card variant.
Name variant | Type string | Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option.
Name feature | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option.
Name primary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option.
Name secondary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option.
Name warning | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option.
Name img U R L | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option.
Name img A L T | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option.
Name image | Type object | Description Can be used to add an image to the card component. See macro options for image .
Name description | Type object | Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description .
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name actions | Type object | Description Can be used to add actions to the card component. See macro options for actions .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block.
Name classes | Type string | Description Classes to add to the card.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading.
Name visually Hidden Text | Type string | Description Optional visually hidden prefix used before the heading.
Name size | Type string | Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" .
Name level | Type integer | Description Optional heading level. Defaults to 2 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name src | Type string | Description Required. The URL of the image in the card.
Name alt | Type string | Description The alternative text of the image in the card.
Name html | Type string | Description HTML to use for the image content. If html is provided, the src and alt options will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the card content.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card content.

Name | Type | Description
Name items | Type array | Description Array of actions as links for use in the card component. See macro options for actions items .
Name classes | Type string | Description Classes to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If href is provided, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If href is provided, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"card/macro.njk"
import
card
%}
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"GPs"
,
size
:
"m"
},
description
:
"About GP services, including how to find and register with a local GP and how to book an appointment"
,
href
:
"#"
,
clickable
:
true
,
variant
:
"primary"
})
}}
</
li
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"Hospitals"
,
size
:
"m"
},
description
:
"About NHS hospitals, booking and changing appointments with the NHS e-Referral Service and going into hospital"
,
href
:
"#"
,
clickable
:
true
,
variant
:
"primary"
})
}}
</
li
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"Dentists"
,
size
:
"m"
},
description
:
"About NHS dental services, how to find an NHS dentist and how much treatment costs"
,
href
:
"#"
,
clickable
:
true
,
variant
:
"primary"
})
}}
</
li
>
<
li
class
=
"nhsuk-grid-column-one-half nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"Prescriptions"
,
size
:
"m"
},
description
:
"Find out about prescriptions including charges, repeat prescriptions and if you can get free prescriptions"
,
href
:
"#"
,
clickable
:
true
,
variant
:
"primary"
})
}}
</
li
>
</
ul
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

For thirds, use nhsuk-grid-column-one-third .

- HTML code for card group third

- Nunjucks code for card group third

```text
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-third nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable"
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
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
5 steps to mental wellbeing
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
Practical advice to help you feel mentally and emotionally better
</
p
>
</
div
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
"nhsuk-grid-column-one-third nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable"
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
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
Healthy weight
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
Check your BMI using our healthy weight calculator and find out if you
&#39;
re a healthy weight
</
p
>
</
div
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
"nhsuk-grid-column-one-third nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable"
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
<
a
class
=
"nhsuk-card__link"
href
=
"#"
>
Exercise
</
a
>
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
Programmes, workouts and tips to get you moving and improve your fitness and wellbeing
</
p
>
</
div
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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the card.
Name heading | Type object | Description Required. Heading of the card component. See macro options for heading .
Name heading Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name heading Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option.
Name heading Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option.
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name heading Id | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option.
Name heading Visually Hidden Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option.
Name href | Type string | Description The card link href attribute.
Name clickable | Type boolean | Description If set to true , then the whole card will become a clickable card variant.
Name variant | Type string | Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option.
Name feature | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option.
Name primary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option.
Name secondary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option.
Name warning | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option.
Name img U R L | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option.
Name img A L T | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option.
Name image | Type object | Description Can be used to add an image to the card component. See macro options for image .
Name description | Type object | Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description .
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name actions | Type object | Description Can be used to add actions to the card component. See macro options for actions .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block.
Name classes | Type string | Description Classes to add to the card.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading.
Name visually Hidden Text | Type string | Description Optional visually hidden prefix used before the heading.
Name size | Type string | Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" .
Name level | Type integer | Description Optional heading level. Defaults to 2 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name src | Type string | Description Required. The URL of the image in the card.
Name alt | Type string | Description The alternative text of the image in the card.
Name html | Type string | Description HTML to use for the image content. If html is provided, the src and alt options will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the card content.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card content.

Name | Type | Description
Name items | Type array | Description Array of actions as links for use in the card component. See macro options for actions items .
Name classes | Type string | Description Classes to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If href is provided, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If href is provided, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"card/macro.njk"
import
card
%}
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-third nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"5 steps to mental wellbeing"
,
size
:
"m"
},
description
:
"Practical advice to help you feel mentally and emotionally better"
,
href
:
"#"
,
clickable
:
true
})
}}
</
li
>
<
li
class
=
"nhsuk-grid-column-one-third nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"Healthy weight"
,
size
:
"m"
},
description
:
"Check your BMI using our healthy weight calculator and find out if you're a healthy weight"
,
href
:
"#"
,
clickable
:
true
})
}}
</
li
>
<
li
class
=
"nhsuk-grid-column-one-third nhsuk-card-group__item"
>
{{
card
({
heading
: {
text
:
"Exercise"
,
size
:
"m"
},
description
:
"Programmes, workouts and tips to get you moving and improve your fitness and wellbeing"
,
href
:
"#"
,
clickable
:
true
})
}}
</
li
>
</
ul
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

When using thirds or quarters, check your content on smaller screens as the cards become narrow. Avoid adding paragraphs of text that will become hard to read.

For quarters, use nhsuk-grid-column-one-quarter .

- HTML code for card group quarter

- Nunjucks code for card group quarter

```text
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-quarter nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable"
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
"nhsuk-card__heading nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1"
>
<
span
role
=
"text"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Applicants:
</
span
>
91
</
span
>
</
h2
>
<
a
href
=
"#/applicants"
class
=
"nhsuk-card__link"
>
Applicants
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
li
>
<
li
class
=
"nhsuk-grid-column-one-quarter nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable"
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
"nhsuk-card__heading nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1"
>
<
span
role
=
"text"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Jobs:
</
span
>
23
</
span
>
</
h2
>
<
a
href
=
"#/jobs"
class
=
"nhsuk-card__link"
>
Jobs
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
li
>
<
li
class
=
"nhsuk-grid-column-one-quarter nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable"
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
"nhsuk-card__heading nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1"
>
<
span
role
=
"text"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Services:
</
span
>
8
</
span
>
</
h2
>
<
a
href
=
"#/services"
class
=
"nhsuk-card__link"
>
Services
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
li
>
<
li
class
=
"nhsuk-grid-column-one-quarter nhsuk-card-group__item"
>
<
div
class
=
"nhsuk-card nhsuk-card--clickable"
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
"nhsuk-card__heading nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1"
>
<
span
role
=
"text"
>
<
span
class
=
"nhsuk-u-visually-hidden"
>
Messages:
</
span
>
33
</
span
>
</
h2
>
<
a
href
=
"#/messages"
class
=
"nhsuk-card__link"
>
Messages
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
Name id | Type string | Description The ID of the card.
Name heading | Type object | Description Required. Heading of the card component. See macro options for heading .
Name heading Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name heading Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option.
Name heading Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option.
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name heading Id | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option.
Name heading Visually Hidden Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option.
Name href | Type string | Description The card link href attribute.
Name clickable | Type boolean | Description If set to true , then the whole card will become a clickable card variant.
Name variant | Type string | Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option.
Name feature | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option.
Name primary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option.
Name secondary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option.
Name warning | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option.
Name img U R L | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option.
Name img A L T | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option.
Name image | Type object | Description Can be used to add an image to the card component. See macro options for image .
Name description | Type object | Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description .
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name actions | Type object | Description Can be used to add actions to the card component. See macro options for actions .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block.
Name classes | Type string | Description Classes to add to the card.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading.
Name visually Hidden Text | Type string | Description Optional visually hidden prefix used before the heading.
Name size | Type string | Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" .
Name level | Type integer | Description Optional heading level. Defaults to 2 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name src | Type string | Description Required. The URL of the image in the card.
Name alt | Type string | Description The alternative text of the image in the card.
Name html | Type string | Description HTML to use for the image content. If html is provided, the src and alt options will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the card content.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card content.

Name | Type | Description
Name items | Type array | Description Array of actions as links for use in the card component. See macro options for actions items .
Name classes | Type string | Description Classes to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If href is provided, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If href is provided, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"card/macro.njk"
import
card
%}
<
ul
class
=
"nhsuk-grid-row nhsuk-card-group"
>
<
li
class
=
"nhsuk-grid-column-one-quarter nhsuk-card-group__item"
>
{%
call
card
({
heading
: {
text
:
"91"
,
visuallyHiddenText
:
"Applicants"
,
classes
:
"nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1"
},
clickable
:
true
}) %}
<
a
href
=
"#/applicants"
class
=
"nhsuk-card__link"
>
Applicants
</
a
>
{%
endcall
%}
</
li
>
<
li
class
=
"nhsuk-grid-column-one-quarter nhsuk-card-group__item"
>
{%
call
card
({
heading
: {
text
:
"23"
,
visuallyHiddenText
:
"Jobs"
,
classes
:
"nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1"
},
clickable
:
true
}) %}
<
a
href
=
"#/jobs"
class
=
"nhsuk-card__link"
>
Jobs
</
a
>
{%
endcall
%}
</
li
>
<
li
class
=
"nhsuk-grid-column-one-quarter nhsuk-card-group__item"
>
{%
call
card
({
heading
: {
text
:
"8"
,
visuallyHiddenText
:
"Services"
,
classes
:
"nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1"
},
clickable
:
true
}) %}
<
a
href
=
"#/services"
class
=
"nhsuk-card__link"
>
Services
</
a
>
{%
endcall
%}
</
li
>
<
li
class
=
"nhsuk-grid-column-one-quarter nhsuk-card-group__item"
>
{%
call
card
({
heading
: {
text
:
"33"
,
visuallyHiddenText
:
"Messages"
,
classes
:
"nhsuk-u-font-size-64 nhsuk-u-margin-bottom-1"
},
clickable
:
true
}) %}
<
a
href
=
"#/messages"
class
=
"nhsuk-card__link"
>
Messages
</
a
>
{%
endcall
%}
</
li
>
</
ul
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## Accessibility

### Heading level and size

Use headings correctly to reflect the page structure. If you need to, change the default h2 heading.

Here's an example of replacing the default h2 heading with an h3 .

- HTML code for card heading level

- Nunjucks code for card heading level

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
h3
class
=
"nhsuk-card__heading"
>
Heading level 3
</
h3
>
<
p
class
=
"nhsuk-card__description"
>
Card description text goes here
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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the card.
Name heading | Type object | Description Required. Heading of the card component. See macro options for heading .
Name heading Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name heading Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option.
Name heading Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option.
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name heading Id | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option.
Name heading Visually Hidden Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option.
Name href | Type string | Description The card link href attribute.
Name clickable | Type boolean | Description If set to true , then the whole card will become a clickable card variant.
Name variant | Type string | Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option.
Name feature | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option.
Name primary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option.
Name secondary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option.
Name warning | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option.
Name img U R L | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option.
Name img A L T | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option.
Name image | Type object | Description Can be used to add an image to the card component. See macro options for image .
Name description | Type object | Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description .
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name actions | Type object | Description Can be used to add actions to the card component. See macro options for actions .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block.
Name classes | Type string | Description Classes to add to the card.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading.
Name visually Hidden Text | Type string | Description Optional visually hidden prefix used before the heading.
Name size | Type string | Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" .
Name level | Type integer | Description Optional heading level. Defaults to 2 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name src | Type string | Description Required. The URL of the image in the card.
Name alt | Type string | Description The alternative text of the image in the card.
Name html | Type string | Description HTML to use for the image content. If html is provided, the src and alt options will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the card content.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card content.

Name | Type | Description
Name items | Type array | Description Array of actions as links for use in the card component. See macro options for actions items .
Name classes | Type string | Description Classes to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If href is provided, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If href is provided, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"card/macro.njk"
import
card
%}
{{
card
({
heading
: {
text
:
"Heading level 3"
,
level
:
3
},
description
:
"Card description text goes here"
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

You can change the size of the heading using heading typography styles .

When using Nunjucks, you can set the size of card headings using the size option, for example: size: "s" . You can use sizes xxs , xs , s , m , l , xl .

- HTML code for card heading size

- Nunjucks code for card heading size

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
"nhsuk-card__heading nhsuk-heading-l"
>
Heading size large
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
Card description text goes here
</
p
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
Heading size medium
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
Card description text goes here
</
p
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
"nhsuk-card__heading nhsuk-heading-s"
>
Heading size small
</
h2
>
<
p
class
=
"nhsuk-card__description"
>
Card description text goes here
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

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the card.
Name heading | Type object | Description Required. Heading of the card component. See macro options for heading .
Name heading Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Required. Replaced by the heading.html option.
Name heading Classes | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.classes option.
Name heading Size | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.size option.
Name heading Level | Type integer | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.level option.
Name heading Id | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.id option.
Name heading Visually Hidden Text | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the heading.visuallyHiddenText option.
Name href | Type string | Description The card link href attribute.
Name clickable | Type boolean | Description If set to true , then the whole card will become a clickable card variant.
Name variant | Type string | Description Optional variant of card – "feature" , "primary" , "secondary" , "warning" , "non-urgent" , "urgent" or "emergency" .
Name type | Type string | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant option.
Name feature | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "feature" option.
Name primary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "primary" option.
Name secondary | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "secondary" option.
Name warning | Type boolean | Description Deprecated in 10.4.0 (see GitHub) . Replaced by the variant: "warning" option.
Name img U R L | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.src option.
Name img A L T | Type string | Description Deprecated in 10.3.0 (see GitHub) . Replaced by the image.alt option.
Name image | Type object | Description Can be used to add an image to the card component. See macro options for image .
Name description | Type object | Description Description to use within the card content. If descriptionHtml is provided, the description option will be ignored. See macro options for description .
Name description Html | Type string | Description Deprecated in 10.6.0 (see GitHub) . Replaced by the description.html option.
Name actions | Type object | Description Can be used to add actions to the card component. See macro options for actions .
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire card component in a call block.
Name classes | Type string | Description Classes to add to the card.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card.

Name | Type | Description
Name id | Type string | Description The ID of the heading.
Name text | Type string | Description Required. If html is set, this is not required. Text for the heading.
Name html | Type string | Description Required. If text is set, this is not required. HTML for the heading.
Name visually Hidden Text | Type string | Description Optional visually hidden prefix used before the heading.
Name size | Type string | Description Size of the heading – "xxs" , "xs" , "s" , "m" , "l" or "xl" .
Name level | Type integer | Description Optional heading level. Defaults to 2 .
Name classes | Type string | Description Classes to add to the heading.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the heading.

Name | Type | Description
Name src | Type string | Description Required. The URL of the image in the card.
Name alt | Type string | Description The alternative text of the image in the card.
Name html | Type string | Description HTML to use for the image content. If html is provided, the src and alt options will be ignored.

Name | Type | Description
Name text | Type string | Description Required. If html is set, this is not required. Text to use within the card content. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within the card content. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the card content.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the card content.

Name | Type | Description
Name items | Type array | Description Array of actions as links for use in the card component. See macro options for actions items .
Name classes | Type string | Description Classes to add to the actions wrapper.

Name | Type | Description
Name id | Type string | Description The ID of the action item.
Name text | Type string | Description Required. If html is set, this is not required. Text to use within each action item. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. If text is set, this is not required. HTML to use within each action item. If html is provided, the text option will be ignored.
Name visually Hidden Text | Type string | Description Actions rely on context from the surrounding content so may require additional accessible text. Text supplied to this option is appended to the end. Use html for more complicated scenarios.
Name name | Type string | Description Name for the action as a button. If href is provided, this has no effect.
Name type | Type string | Description Type of action as a button – "button" , "submit" or "reset" . Defaults to "submit" unless href is provided.
Name value | Type string | Description The value attribute for the action as a button. If href is provided, this has no effect.
Name href | Type string | Description Required. The action href attribute. If set, the action will use an <a> tag automatically unless type is provided.
Name classes | Type string | Description Classes to add to the action item.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the action item.

```text
{%
from
"card/macro.njk"
import
card
%}
{{
card
({
heading
: {
text
:
"Heading size large"
,
size
:
"l"
},
description
:
"Card description text goes here"
})
}}
{{
card
({
heading
: {
text
:
"Heading size medium"
,
size
:
"m"
},
description
:
"Card description text goes here"
})
}}
{{
card
({
heading
: {
text
:
"Heading size small"
,
size
:
"s"
},
description
:
"Card description text goes here"
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## Research

We have tested cards on the NHS website, summary care record and NHS login help centre. We found that they helped users:

- scan for relevant information

- decide where to go next

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: June 2026
