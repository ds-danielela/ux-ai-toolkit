# Hero modal

---
title: Hero modal
url: https://zeroheight.com/0b922d40b/v/latest/p/41c5d9-hero-modal
introduction: Hero modal introduces new feature through visual and text message.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Hero modal: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c86f5c66234c9b4cb00c5a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133106Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=be53b6fffb78231fa1917e5ab7d223b97cb1ccf90cf7cf4ebbed074358556122)

**Hero modal: Preview**

---

## Design spec

![Hero modal: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/8e2462961416fc0636fd4f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133106Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=56d0e3b23180a302c720f7287ebd48d6357db11b416942e310f947f17815d6aa)

**Hero modal: Design spec**

---

### Size and scaling

The height of the hero modal depends on the content. The maximum height must ensure a distance of **Spacing.Layout.M** to the top and bottom of the screen. If the content cannot be displayed completely within this maximum height, the content becomes scrollable.

The hero modal is centered horizontally and vertically on the screen.

---

## Anatomy

The hero modal contains:

1. Semitransparent overlay covering the whole underlying screen
2. Hero area: Image or individual content such as animation
3. Close button
4. Headline
5. Body content: either a paragraph of text or individual content
6. Actions at the bottom

---

## Usage

Use a hero modal to introduce new features or explain functionality. Images may differ between light and dark modes to ensure optimal readability.

Hero modals do not offer a fullscreen variation unlike other modal types. When the hero modal is open, an overlay blocks the underlying content. The user cannot interact with the content below until the modal is closed.

A hero modal can contain a single acknowledging action, such as "Acknowledge", or present several steps in a sequence. In a multi-step flow, the modal can provide previous and next actions, with a primary closing action at the end of the series. The modal can be closed through its action buttons, and an additional close option is provided by the close button in the top right.

Use hero modals sparingly, as they interrupt the user's workflow.

### Hero area

The hero area is not limited to a static image. It may also include individual visual content, such as animated or dynamic elements. The consuming team is responsible for implementing this content.

### Content area

In addition to a single text block, the hero modal can support structured layouts, for example a two-column list of bullet points. The implementation of custom content and layout is handled by the consuming team.

### Overflow behavior

If the content of the hero modal exceeds the available space, only the header and the body become scrollable. The image and the actions remain fixed in place. This ensures that the visual introduction and the primary actions stay visible at all times while the user scrolls through the explanatory content.

### Content guidelines

* Keep the headline short and specific, focusing on the core value of the feature.
* The body text should describe user benefits and provide only the information needed to understand the update. Avoid overloading the modal with unnecessary details.
* Avoid technical jargon unless it is essential to the user's workflow.
* Use clear and purposeful language for the actions.
* Acknowledgment buttons are allowed and should guide the user forward. Examples include "Got it", "Continue", or "I understand".
* Hero modals may also include call-to-action buttons such as "Enable" or "Try out" when the feature requires activation or invites interaction.
* In multi-step flows, use "Next" and "Previous" to guide users through the sequence.
* The final step should end with a clear confirming action.

### Do's and don'ts

Use simple, focused visuals and wording that speak directly to user needs, and avoid cluttered imagery or long explanations. The image should clearly highlight the feature, and the body copy should stay short and concise so the user can understand the benefit quickly and return to their task.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Hero%20modal](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Hero%20modal)
