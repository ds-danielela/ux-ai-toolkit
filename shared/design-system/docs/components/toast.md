# Toast

Toasts are cross-system messages that slide in and out of a page and provide non-disruptive information.

---
title: Toast
url: https://zeroheight.com/0b922d40b/v/latest/p/25384c-toast
introduction: Toasts are cross-system messages that slide in and out of a page and provide non-disruptive information.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Toast: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d76d15c483fe90029b6bd8)

**Toast: Preview**

---

## Design spec

![Toast: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0a07484e9c2ce618709bc4)

**Toast: Design spec**

### Size and scaling

The toast has a fixed width for responsive layouts M - XL. For responsive layout S, it stretches to the available width (considering the margin). The height depends on its content.

---

## Anatomy

The toast contains the following elements:

* Icon indicating the notification type
* Headline
* Body
* Close button
* Actions (optional)

---

## Usage

Use toasts to provide users with non-disruptive feedback or ephemeral status updates that are not necessarily related to the content on the page.

Toast notifications disappear automatically after five seconds if the user's mouse cursor is positioned outside the toast. During that time, the user can also click on the close button to hide the toast immediately. If actions are shown, the toast persists until dismissed. After the toast is dismissed, the user could review it in the notification menu.

Toasts slide in from the right of the screen.

When multiple toast notifications are shown to the user, they should be stacked vertically with the newest one shown on top.

### Status types

| Type | Usage |
| --- | --- |
| Critical | An issue has occurred that prevents further processing. |
| Warning | A problem or inconsistency has arisen. Users can carry on working, but might run into an error later on. |
| Success | An action has been performed without errors or warnings. |
| Information | You want to provide additional, non-critical information. |

### Content guidelines

* Keep the headline short and specific.
* The buttons should be labeled using descriptive words for the actions such as Delete, or Keep. Vague words like OK or Cancel should be avoided.

### Do's and don'ts

Write in sentence case.

Avoid unnecessary words and articles in the toast headline, such as "the", "an" or "a".

Do not use toasts for critical notifications that require immediate user interaction, use an alert dialog instead. Only use toasts for ephemeral status updates.

Stick to the provided variants and do not introduce custom icons or colors.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Toast](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Toast)
