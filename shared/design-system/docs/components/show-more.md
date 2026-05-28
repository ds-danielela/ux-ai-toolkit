# Show more

Show more toggles additional content on demand. It reveals hidden information without navigating away from the current context.

---
title: Show more
url: https://zeroheight.com/0b922d40b/v/latest/p/8653c7-show-more
introduction: Show more toggles additional content on demand. It reveals hidden information without navigating away from the current context.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Show more: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c937c6ad389ddd943864e7)

**Show more: Preview**

---

## Design spec

![Show more: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d360c4f3dd0b544338e114)

**Show more: Design spec**

### Size and scaling

The width of the show more component content area usually stretches to the width of its parent container. Its height depends on the content. The show more link itself does not stretch. Its width depends on the label and may vary with localization.

---

## Anatomy

The text variation consists of:

1. Text: A paragraph of text that is truncated after a defined number of lines in the collapsed version.
2. Standalone link with chevron: Toggles between collapsed and expanded state.

The individual content variation is always used together with preceding content, which is not part of the component. It consists of:

1. Expandable content area: Contains the content shown on interaction. Can include any combination of components.
2. Standalone link with chevron: Triggers the expansion or collapse of the content below.

---

## Usage

Use the show more component to reveal supplementary content inline without disrupting the reading flow. It is suitable for short sections where only one block of information needs to be expanded.

> **Please note:** Show more is not a replacement for an accordion. Use an accordion when multiple sections require clear grouping, their own headings, or independent expand and collapse behavior.

### Text variation

Use the text variation when the initial content and the expanded content form a single continuous text block. The text variation works best for brief descriptions, summaries, or explanatory text that does not require additional structure or embedded components.

#### Choosing between truncation with tooltip and show more

Use **truncation with tooltip** when the text is short, space is limited, and only a small portion of the text exceeds the available line length. This pattern is suited for labels, table cells, or any compact UI element where the full text is not essential for scanning and can be revealed on hover or focus.

Use **show more** when the text is longer, forms part of a paragraph, and cannot be meaningfully shortened with truncation.

### Individual content variation

Use the individual content variation when the expanded area contains components, structured information, or content with its own layout. This variation always requires preceding content outside of the component to provide context.

Show more works best when:

* only one area on the page needs to be expanded
* the extended content is secondary or nice-to-have
* the layout should remain compact and linear

#### Placement and spacing

When used with individual content, place show more at the bottom of a container or content block to reveal optional details, supporting information, or complementary components.

Use Spacing.Layout.M to separate preceding content.

### Content guidelines

* Keep the expanded content secondary. It should add optional detail, not critical information.
* Avoid long, complex structures inside the expandable area. Do not nest multiple show more components.
* Maintain a clear connection between the preceding visible content and the expanded content.
* Do not use show more to hide required actions, essential instructions, or error-relevant information.

### Do's and don'ts

Do not nest show more components and avoid placing multiple ones in the same section.

Place show more at the end of a container or content block when adding optional details. Don't position it randomly on the page or between unrelated elements.

Keep the expanded content simple and fully visible within the page flow. Don't place scrollable content inside because this creates nested scrolling.

Don't combine truncation and show more in the same text block.

Use the text variation only when the visible and expanded text form a continuous piece of writing.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Show%20more](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Show%20more)
