# Modal

---
title: Modal
url: https://zeroheight.com/0b922d40b/v/latest/p/51c11c-modal
introduction: A modal shows additional content in a layer above the page.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Modal: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b6e66293f7d56c0e5b608a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133114Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=89cc934544968dc4ea502d708c126be3fc91bf453efa44724e46595067a5ac66)

**Modal: Preview**

---

## Design spec

![Modal: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/157fba892bedd8f6e6dc07?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133114Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=b88a9c86f3ca17a8bc5542947f3eb5b4abe685048a1ecc791876d460a2f35240)

**Modal: Design spec**

---

### Size and scaling

The height of the modal depends on the content. The maximum height of the modal should ensure a distance of **Spacing.Layout.M** to the top and bottom of the screen. If the content cannot be displayed completely even in the maximum height of the modal, the content of the modal is scrollable.

The width of the modal depends on the respective variant (small, medium, large) as well as on the responsive layout.

The modal is horizontally and vertically centered on the screen. 

---

## Anatomy

The modal (1) is accompanied by a semitransparent overlay (2) covering the whole underlying screen.

The modal contains a headline (3) and a close button (4), individual content (5) and actions at the bottom (6).   

---

## Usage

Use a modal to present additional information to the user or to request input needed to complete a user's workflow.

When the modal is open, an overlay blocks the content below. The user cannot interact with the underlying content until the modal is closed. 

Use modals sparingly, as they interrupt the user's workflow. 

There are several sizes of modals. Choose the size depending on the use case.

| **Size** | **Usage** |
| --- | --- |
| Small | Use the small modal for confirmations or very simple forms. |
| Medium | Use the medium modal for more complex forms. |
| Large | Use the large modal for information or interaction that requires a lot of space. |
| Fullscreen (Only resp. layout S) | For responsive layout S, the medium and large sized modal are represented by the fullscreen variation. |

### Overflow behavior

If the vertical space does not suffice to display the content, the content is scrollable while the header and actions are fixed.

### Enabled vs. disabled buttons

Do not use the disabled state of the primary button, even if not all data is filled yet. There is a risk that the user does not understand why the button is disabled. Instead of disabling the button, show an inline notification explaining what needs to be done. 

### Content guidelines

* Keep the headline short and specific. If applicable, the headline should match the label of the button triggering the modal. 

When it comes to buttons, follow these 3 simple rules:

* Make them distinguishable from one another. Users can't mix them up or confuse them.
* Make them contextual. Don't just write Yes/No. If possible, add full context at least to the primary button e.g. Delete account or Share media.
* Use the same verb in the headline and on the primary button.

### Do's and don'ts

Write in sentence case.

Do not use the disabled state of the primary button, even if not all data is filled yet. There is a risk that the user does not understand why the button is disabled. 

Avoid triggering another modal from the actions within a modal.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Modal%20Dialog](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Modal%20Dialog)

---

## Hints for designers

**Prototype behavior for modal overlays**

We recommend using Figma's overlay functionality for modals in prototypes, as it improves file performance and keeps prototypes lighter and more responsive. Use "Mouse down" trigger to open overlay (instead of "On click"). This prevents the triggering element from remaining in a pressed state after the modal opens. With "On click", the pressed state may persist behind the overlay, or even after closing it, leading to inconsistent interaction behavior.
