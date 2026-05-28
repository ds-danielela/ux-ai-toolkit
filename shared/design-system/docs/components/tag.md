# Tag

Tags are used to label or categorize items.

---
title: Tag
url: https://zeroheight.com/0b922d40b/v/latest/p/40b4d0-tag
introduction: Tags are used to label or categorize items.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Tag: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d3eeadd7fc657321c039fe)

**Tag: Preview**

---

## Design spec

![Tag: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2c21adf2a3d19de6092452)

**Tag: Design spec**

### Size and scaling

The size of tags depends on their content (icon, label and spacing). Contrast tags with icon are circular and have a fixed width and height.

The width of the filter tag group and choice tag group depends on the available width provided by the parent container.

---

## Anatomy

Tags can either contain an icon (1), a label (2), or a color dot and a label (3). Filter and removable tags always contain both, icon and label. Status tags can contain icon, text or both.

A filter tag group contains a headline (1) and filter tags (2).

A choice tag group contains several choice tags (1).

A color tag comes in two flavors: color tag (1) and choice tag with color (2).

---

## Usage

There are several types and variations of tags. Choose the type depending on the use case.

| Type / Variation | Usage |
| --- | --- |
| Normal | Use the tag variation normal to display category information within components like cards, containers, list items or table rows. |
| Contrast / Contrast with icon | Use the tag variation contrast to display category information on a surface that requires contrast, like within media tiles. |
| Filter tag | Use the filter tag within a tag group to allow the user to choose multiple categories. |
| Removable tag | Use the removable tag within a dropdown or search field that allows multi-selection. |
| Choice tag | Use the choice tag group to provide the user with a set of choices where space is limited and yet all options should be visible at once. |
| Status tag | Use the status tag to display status information within components like cards, containers, list or table rows. |
| Color tag variants | Use color tag to display color and material related information in tables, cards, page details, and other non-editable places. |

**Tag sizes**

Tags and status tags are available in the sizes small and base.

**Choice tags on responsive layout S**

If the choice tags are used on smaller viewports and wrapping is not activated, they can be scrolled / swiped horizontally.

**Skeleton state**

In the skeleton state, tags and status tags are displayed as simplified pill-shaped skeletons without any text or color.

### Content guidelines

* Keep labels short and concise. Try to limit it to one word only.

### Do's and don'ts

Stick to the provided variants as they are designed to ensure sufficient contrast. Do not apply custom text colors.

Ensure the chosen color is clearly displayed. Do not use filter tag, or alternative icons that could obscure or misrepresent this information.

Keep tags grouped together based on their purpose. Avoid mixing tags that serve different functions.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Tag](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Tag)

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Tag%20(removable)](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Tag%20(removable))

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Tag%20Group%20(choice)](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Tag%20Group%20(choice))

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Tag%20Group%20(filter)](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Tag%20Group%20(filter))
