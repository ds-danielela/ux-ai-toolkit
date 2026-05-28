# Progress circle

The progress circle is used to show the current progress of a running process when space is limited in both dimensions.

---
title: Progress circle
url: https://zeroheight.com/0b922d40b/v/latest/p/05d95e-progress-circle
introduction: The progress circle is used to show the current progress of a running process when space is limited in both dimensions.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Progress circle: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/737877c05402a93212fcc5)

**Progress circle: Preview**

---

## Design spec

![Progress circle: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b72fc212935c5683c55e3c)

**Progress circle: Design spec**

### Size and scaling

Progress circle has a width and height of 24 px with a thickness of 2 px.

---

## Anatomy

The progress circle contains a circle (1) with an indicator (2) that either rotates on the circle or fills it to indicate how much the process has progressed.

---

## Usage

Use a progress circle to show the current progress of a running process when space is limited in both dimensions, i.e. within button or in a file upload item.

A progress circle can be determinate or indeterminate.

| Type | Usage |
| --- | --- |
| Determinate progress circle | Use the determinate progress circle if the actual progress can be calculated. This variant should be used preferably, as the user gets an idea of how long he has to wait. |
| Indeterminate progress circle | Use the indeterminate progress circle if the actual progress cannot be determined. |

The color of the progress circle depends on the usage.

### Do's and don'ts

Do not embed text into a progress circle. Put it next to it instead.

Do not introduce semantic colors on a progress circle. To indicate a successful or critical outcome of a progress, use another [notification](https://zeroheight.com/0b922d40b/p/724668-notifications) mechanism instead. In a file upload item, the progress circle is replaced by an icon.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Progress%20Circle](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Progress%20Circle)

---

## Hints for designers

**Animated progress circle**

If you want to add more dynamics to your prototype, use the animated version of the progress circle. The default animation of the determinate progress circle starts after a delay of 1 ms. The individual animations from 25 - 50 %, 50 - 75 %, 75 - 100 % have a duration of 300 ms.

To create a screen transition after the progress circle has been filled, you have to at least sum the above values (to i.e. 1000 ms) and specify this value as "After delay" for the screen transition.
