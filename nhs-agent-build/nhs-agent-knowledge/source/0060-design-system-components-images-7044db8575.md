# Images – NHS digital service manual

Source URL: https://service-manual.nhs.uk/design-system/components/images/

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

# Content presentation – Images

Use images only if there is a real user need. Avoid unnecessary decoration.

- HTML code for images

- Nunjucks code for images

```text
<
figure
class
=
"nhsuk-image"
>
<
img
class
=
"nhsuk-image__img"
src
=
"/assets/image-example-stretch-marks-600w.jpg"
alt
=
"Close-up of a person
&#39;
s tummy showing a number of creases in the skin under their belly button. Shown on light brown skin."
sizes
=
"(max-width: 768px) 100vw, 66vw"
srcset
=
"/assets/image-example-stretch-marks-600w.jpg 600w, /assets/image-example-stretch-marks-1000w.jpg 1000w"
>
<
figcaption
class
=
"nhsuk-image__caption"
>
Stretch marks can be pink, red, brown, black, silver or purple. They usually start off darker and fade over time.
</
figcaption
>
</
figure
>
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

Use options to customise the appearance, content and behaviour of a component when using a macro, for example, changing the text.

Some options are required for the macro to work. These are marked as "Required" in the option description. Deprecated options are marked as "Deprecated".

If you're using Nunjucks macros in production with "html" options, or ones ending with "html", you must sanitise the HTML to protect against cross-site scripting exploits .

Name | Type | Description
Name id | Type string | Description The ID of the image.
Name src | Type string | Description Required. The source location of the image. If html is provided, the src , srcset , sizes and alt options will be ignored.
Name srcset | Type string | Description A list of image source URLs and their respective sizes. Separate each image with a comma.
Name sizes | Type string | Description A list of screen sizes for the browser to load the correct image from the srcset images.
Name alt | Type string | Description The alt text of the image. Defaults to "" . If html is provided, the src , srcset , sizes and alt options will be ignored.
Name html | Type string | Description Required. If src is set, this is not required. HTML to use within the image component. If html is provided, the src , srcset , sizes and alt options will be ignored.
Name caller | Type nunjucks-block | Description Not strictly an option but supports the call block as an alternative to the html option. To use it, you will need to wrap the entire image component in a call block.
Name caption | Type object | Description Optional caption for the image. See macro options for caption .
Name background | Type string | Description Background colour for the image component – "card" or false . Defaults to "card" . To remove the background colour, set background to false .
Name border | Type boolean | Description If set to false , removes the border-bottom from the image component.
Name width | Type string | Description Width of the image component. You can pass any design system grid width here – for example, "one-third" , "two-thirds" or "one-half" . Defaults to "two-thirds" .
Name classes | Type string | Description Classes to add to the image component.
Name attributes | Type object | Description HTML attributes (for example data attributes) to add to the image component.

Name | Type | Description
Name text | Type string | Description Required. Text to add within the caption. If html is provided, the text option will be ignored.
Name html | Type string | Description Required. HTML to add within the caption. If html is provided, the text option will be ignored.
Name classes | Type string | Description Classes to add to the figcaption element.

```text
{%
from
"images/macro.njk"
import
image
%}
{{
image
({
src
:
"/assets/image-example-stretch-marks-600w.jpg"
,
sizes
:
"(max-width: 768px) 100vw, 66vw"
,
srcset
:
"/assets/image-example-stretch-marks-600w.jpg 600w, /assets/image-example-stretch-marks-1000w.jpg 1000w"
,
alt
:
"Close-up of a person's tummy showing a number of creases in the skin under their belly button. Shown on light brown skin."
,
caption
: {
text
:
"Stretch marks can be pink, red, brown, black, silver or purple. They usually start off darker and fade over time."
}
})
}}
```

Requires NHS.UK frontend 10.6.0 – check your version of NHS.UK frontend

## When to use images

Informative images that meet real user needs can be very important on health services, especially where they help users identify specific health problems and get the treatment they need.

We've also found users with some access needs (such as dyslexia) navigate health information through images. Images help them orient themselves and they separate out the content.

But having unnecessary or decorative images can frustrate users, especially on information pages or transactional journeys.

## How to use images

Images should flow with the text content, not appear too prominent or isolated.

We recommend stacking images. We've found that gallery views (images side by side) confuse users.

### Captions

The image component is made up of 2 elements:

- the image

- a caption underneath it in a white box

Not all images need captions. If you use them:

- write a full sentence ending with a full stop

- keep captions short – ideally 1 sentence but no more than 2

- start the caption with a number if the images show a sequence

- do not duplicate alt-text ( alternative text )

The caption assumes that the user can either see the image or read the alt-text. Use it to explain what you want users to conclude from it, for example, how serious their symptom is or what stage their condition has reached.

In the above example, the alt-text is "Close-up of a person's tummy showing a number of creases in the skin under their belly button. Shown on light brown skin." The caption explains that stretch marks can be different colours and fade over time.

### Accessibility

Do not use images that have words in them, because screen readers will not be able to read the words.

#### Alternative text (alt-text)

Images must have text alternatives that describe the information or function they represent. This makes sure that people with disabilities can understand them.

When using an image (or the img element), specify a text alternative with the alt attribute.

Alt-text is not usually visible but is read out by screen readers or displayed if an image does not load or if images have been switched off.

Read more about alt-text in the guidance on using alt-text for images in content .

#### Long descriptions

With complex images, like images of skin symptoms, long descriptions help people who face barriers due to sight loss. Find out how to provide a long description in our skin symptoms guidance .

## Research

In testing we found gallery views (images side by side) confused users. Users either missed the images in the right hand column or they didn't know how to interpret the sequence. To get around this we recommend stacking images.

We also found that users clicked images in gallery views, expecting them to appear larger in a pop-up modal. When we increased the size of the images and stacked them in 1 column (not 2), we didn't see anyone clicking on them to expand them.

## Help us improve this guidance

Share insights or feedback and take part in the discussion. We use GitHub as a collaboration space. All the information on it is open to the public.

Read more about how to feed back or share insights .

If you have any questions, get in touch with the service manual team.

## Updates to this page

Updated: January 2025
