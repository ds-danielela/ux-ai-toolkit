# Inline notification

---
title: Inline notification
url: https://zeroheight.com/0b922d40b/v/latest/p/5697b4-inline-notification
introduction: Inline notifications provide users with non-disruptive feedback or the status of an action related to the content shown on the page.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Inline notification: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/02ae9d876101425717a851?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133112Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=a22152a734f64a4bb3c776b8da093123b3b206df83e6729b85b62fef78e9b7d9)

**Inline notification: Preview**

---

## Design spec

![Inline notification: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/65bd467bf2a82b509c3256?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133112Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=99d2c5f81ee814d0306631f8addc87f1f26cab14863e7659e4d7eaf55620a17a)

**Inline notification: Design spec**

---

### Size and scaling

The inline notification stretches to the available width provided by the parent container. The height depends on its content.

The optional link is displayed on the right of the body text. If the horizontal space does not suffice, the body text and optional link wrap.

---

## Anatomy

The inline notification contains the following elements: 

1. Icon indicating the notification type
2. Headline (optional)
3. Body
4. Action (optional)
5. Close button (optional)

---

## Usage

Use inline notifications to provide users with non-disruptive feedback or the status of an action related to the content shown on the page.

Inline notifications should be placed above the related content. The following example shows an inline notification for an incomplete form. The inline notification is displayed above the form, after the user has pressed the button to submit the form.

### Status types

A status type categorizes the notification that is being communicated. It is important to specify the status type in order to use the correct icon and color.

| **Type** | **Usage** |
| --- | --- |
| Critical | An issue has occurred that prevents further processing. |
| Warning | A problem or inconsistency has arisen. Users can carry on working, but might run into an error later on. |
| Success | An action has been performed without errors or warnings. |
| Information | You want to provide additional, non-critical information. |

### Content guidelines

* Be clear with the message. If more text is necessary to explain the situation, use the variation with header and expand on the context within the message.
* Actions presented within notifications should be directional, and clear on intent. e.g. Learn more, Get started.

### Do's and don'ts

Write in a clear sentence format.

Use only one inline notification at a time, do not stack to hide previous messages.

Use proper icon and color combination for the notification.

Stick to the provided variants and do not introduce custom icons or colors. 

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Inline%20Notification](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Inline%20Notification)
