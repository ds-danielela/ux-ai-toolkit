# Popover

The popover is an elevated layer that contains detailed information about a certain part of the user interface.

---
title: Popover
url: https://zeroheight.com/0b922d40b/v/latest/p/257994-popover
introduction: The popover is an elevated layer that contains detailed information about a certain part of the user interface.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Popover: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a481d85e9bfa4b4c010c8c)

**Popover: Preview**

---

## Design spec

![Popover: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3308bf282a4db27d59552d)

**Popover: Design spec**

### Size and scaling

The width of the popover is fixed. The height depends on its content.

---

## Anatomy

A popover can contain the following elements:

1. Nubbin (optional)
2. Headline
3. Body
4. Close button (optional)
5. Action(s) (optional)
6. Image (optional)

---

## Usage

Use a popover to show detailed information about a certain part of the user interface or to highlight a new feature or the new location of a feature.

### Positioning

Popovers can appear to the right (1a, 1b, 1c), left (2a, 2b, 2c), top (3a, 3b, 3c), or bottom (4a, 4b, 4c) of the triggering UI component. Content and placement within the experience will determine which position should be used. If the popover is explaining a new feature(s), it can be pointing part of the experience or placed in the lower right of the screen (5).

### Interaction

Popovers can either be presented on page load or displayed after pressing a triggering UI component. There are two variations for the closing behavior of popovers:

* Non-Modal Popover (DSPopoverAnchor): The popover can either be closed by clicking on the close button or by clicking on the triggering UI component.
* Modal Popover (DSModalPopoverAnchor): The popover can also be closed by clicking outside of it.

### Scrolling behavior

**Behavior on page scroll**

* Modal popover: Automatically closes when the user interacts with the background, including scrolling.
* Non-modal popover: The popover remains open and attached to the anchor element, moving along with it as the user scrolls the page. If the anchor element scrolls out of view, the popover sticks to the edge of the screen.

**Handling large content**

Popovers can contain scrollable content to accommodate longer information. The close button remains sticky at the top of the popover.

### Content guidelines

* Keep the headline and body clear and concise.

### Do's and don'ts

Keep the popover to the recommended size and do not make it too large or overly descriptive.

Only use one popover at a time, do not show multiple popovers at once.

Don't use to communicate critical information. Consider using a modal or a notification mechanism instead.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Popover%20anchor%20(non%20modal)](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Popover%20anchor%20(non%20modal))

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Popover%20anchor%20(modal)](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Popover%20anchor%20(modal))
