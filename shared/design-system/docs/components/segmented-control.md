# Segmented control

A segmented control represents a selection of two or three options. Only one option can be active at the same time.

---
title: Segmented control
url: https://zeroheight.com/0b922d40b/v/latest/p/53abd9-segmented-control
introduction: A segmented control represents a selection of two or three options. Only one option can be active at the same time.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Segmented control: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6839073b5967487672f852)

**Segmented control: Preview**

---

## Design spec

![Segmented control: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/931c1cbb925fae0f5f0797)

**Segmented control: Design spec**

### Size and scaling

The segmented control width either stretches to the parent container or depends on the widest item. All items have the same width. The height is fixed (label / icon plus spacing).

---

## Anatomy

The segmented control contains up to five buttons that either include labels (1) or icons (2).

---

## Usage

Use a segmented control to switch between different modes or views, i.e. a list and a tile view.

All options of a segmented control are visible to the user at all times. Instead of labels, icons can also be used to support visual differentiation of options. In this case the label of an element can be displayed as a tooltip. Within one segmented control, either entries with text or with icons should be displayed.

Segmented controls with icons should always be accompanied by tooltips.

### Default state

Only provide a default selection if the user's choice is not critical. Otherwise, do not preselect an option. Once one button segment has been selected, the user cannot return to having no segment selected.

### Content guidelines

* The individual button segment labels should be descriptive and specific.

### Do's and don'ts

Within one segmented control, use either entries with text or with icons.

Use icons in button segments only if the metaphor is universally understood.

Write in sentence case.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Segmented%20Control](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Segmented%20Control)
