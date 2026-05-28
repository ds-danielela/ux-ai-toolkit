# Progress bar

The progress bar is used to show the current progress of a running process when vertical space is limited.

---
title: Progress bar
url: https://zeroheight.com/0b922d40b/v/latest/p/64b377-progress-bar
introduction: The progress bar is used to show the current progress of a running process when vertical space is limited.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Progress bar: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2f99255be4fd243fb3f52a)

**Progress bar: Preview**

---

## Design spec

![Progress bar: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/451ffb31443d5157c85d3a)

**Progress bar: Design spec**

### Size and scaling

The progress bar has a fixed height of 4 px. The width stretches to the parent container.

While the width of the indicator is dynamically changing for the determinate progress bar, the indicator of the indeterminate progress bar has a fixed width (one quarter of the whole progress bar width).

---

## Anatomy

The progress bar contains a track (1) representing the overall process. The bar indicator (2) either moves on top of the track or fills it to indicate how much the process has progressed.

---

## Usage

Use a progress bar to show the current progress of a running process when vertical space is limited.

A progress bar can be determinate or indeterminate.

| Type | Usage |
| --- | --- |
| Determinate progress bar | Use the determinate progress bar if the actual progress can be calculated. This variant should be used preferably, as the user gets an idea of how long he has to wait. |
| Indeterminate progress bar | Use the indeterminate progress bar if the actual progress cannot be determined. |

It is recommended to provide the progress bar with text describing what the progress is about and also percentages or numbers reflecting the current progress if applicable.

**Please note:** Some components, i.e. items of the notification center and wizard steps already contain a progress bar.

### Do's and don'ts

Do not embed text into a progress bar. Put it next to it instead.

Do not introduce semantic colors on a progress bar. To indicate a successful or critical outcome of a progress, use another [notification](https://zeroheight.com/0b922d40b/p/724668-notifications) mechanism instead (i.e. toast or alert dialog).

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Progress%20Bar](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Progress%20Bar)

---

## Hints for designers

**Animated progress bar**

If you want to add more dynamics to your prototype, use the animated version of the progress bar.

The default animation starts after a delay of 800 ms and takes 1500 ms. You can adjust these values individually in the "Prototype" tab.

To create a screen transition after the progress bar animation has expired, you have to sum the above values (in this case 800 ms + 1500 ms) and specify this value as "After delay" for the screen transition.
