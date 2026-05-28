# Tooltip

A tooltip displays additional information upon hovering or long-press (for touch devices).

---
title: Tooltip
url: https://zeroheight.com/0b922d40b/v/latest/p/696f5b-tooltip
introduction: A tooltip displays additional information upon hovering or long-press (for touch devices).
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Tooltip: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6ede3a70444104642d8af1)

**Tooltip: Preview**

---

## Design spec

![Tooltip: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c883789f140ffcf2891b72)

**Tooltip: Design spec**

### Size and scaling

The tooltip will shrink to the width of the text.

---

## Anatomy

The tooltip (2) is placed next to the corresponding trigger UI element (1).

---

## Usage

Use a tooltip:

* To describe icon buttons.
* To provide the user with relevant information that does not need to be seen at first glance.
* If text is truncated due to limited available space.

If you want to display more information and include images or further actions, use an info modal instead.

### Placement

The tooltip is placed close to the corresponding trigger UI element. The default position is below and centered. Depending on the available space, the tooltip can also be displayed above, left or right of the triggering UI element.

### Timing

The tooltip is displayed as long as the user hovers over the corresponding trigger UI element.

### Content guidelines

* The tooltip should be short and concise. Ideally it should not contain more than a few words.

### Do's and don'ts

Write in Sentence case.

Keep the text short and simple. Avoid tooltips with multiple lines.

Tooltips only contain text. If you want to include other components, such as buttons or links, use a popover instead.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Tooltip](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Tooltip)
