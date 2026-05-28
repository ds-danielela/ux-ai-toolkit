# Alert dialog

---
title: Alert dialog
url: https://zeroheight.com/0b922d40b/v/latest/p/48505e-alert-dialog
introduction: Alert dialogs are highly disruptive notifications that provide users with critical information that needs their attention or action.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Alert dialog: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/62ba9fe2991812daa398dc?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133056Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=781a07c281d6331882ef416c7b23d299ba7ae9d2d8a68693275d93577422f3ab)

**Alert dialog: Preview**

---

## Design spec

![Alert dialog: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/5f64112c294ceab10c54bd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133056Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=e839349dea8951a53bd13a9a4499fce45827bafa03bacf3e6ab95fba83715fda)

**Alert dialog: Design spec**

---

### Size and scaling

For the alert dialog, the modal variation "Small" is used.

The height of the modal depends on the content. The maximum height of the modal should ensure a distance of Spacing.Layout.M to the top and bottom of the screen. If the content cannot be displayed completely even in the maximum height of the modal, the content of the modal is scrollable.

When the header is too long for the available horizontal space, it wraps.

![Alert: Header overflow](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/91d56281b85ce4595d2503?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133056Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=ad0ae6939d576b151a2ce346a7288144ecd8f6f1c2d6c6cbfdbb6f9bdcae6319)

**Alert: Header overflow**

---

## Anatomy

The alert dialog contains the following elements: 

1. Semitransparent overlay overing the whole underlying screen
2. Colored bar indicating the notification type
3. Icon indicating the notification type
4. Headline
5. Close button
6. Body content: either a paragraph of text or individual content
7. Actions

![Alert: Anatomy](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/25cd49c6205d3ed405a293?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133056Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=ac24c0e44c1c1f58a1ad983d6ae81c8ca7e01120c0161f8b33689a796942e9c0)

**Alert: Anatomy**

---

## Usage

Use alert dialogs to provide users with critical information that needs their immediate attention or action.

When the alert dialog is open, an overlay blocks the content below. The user cannot interact with the underlying content until the dialog is closed. 

Use alert dialogs sparingly, as the interrupt the user's workflow. 

### Status types

A status type categorizes the notification that is being communicated. It is important to specify the status type in order to use the correct icon and color.

| **Type** | **Usage** |
| --- | --- |
| Critical | An issue has occurred that prevents further processing. |
| Critical emphasized | Emphasized version of "Critical" to be used in a medical context. |
| Warning | A problem or inconsistency has arisen. Users can carry on working, but might run into an error later on. |
| Warning emphasized | Emphasized version of "Warning" to be used in a medical context. |
| Success | An action has been performed without errors or warnings. |
| Information | You want to provide additional, non-critical information. |

### Content guidelines

* Keep the headline short and specific.
* The buttons should be labeled using descriptive words for the actions such as Delete, or Keep. Vague words like OK or Cancel should be avoided.
* The body provides space for additional context and guidance. It supports flexible content and can adapt to different message structures depending on the use case.

### Do's and don'ts

Write in sentence case.

Use only one alert dialog at a time, do not stack to hide previous messages.

Use alert dialogs sparingly. Do not use them for excessive confirmations.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Alert%20Dialog](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Alert%20Dialog)
