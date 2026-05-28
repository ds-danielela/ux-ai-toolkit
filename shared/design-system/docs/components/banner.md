# Banner

---
title: Banner
url: https://zeroheight.com/0b922d40b/v/latest/p/27f50c-banner
introduction: Banners are static messages about system or product level information that is not specific to a task.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Banner: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ed9125b95c60749cc0ee23?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133057Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=5b0c792daae2fa4c894a4f30529e1440cbf5084468f846b63ecab95b292c7a35)

**Banner: Preview**

---

## Design spec

![Banner: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7cc3fb97d2aa07a9aa7698?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133057Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=cf29ce29d2da0851c13d2d62f066580065f01b981ffa347d15c91862d9b31048)

**Banner: Design spec**

---

### Size and scaling

The banner stretches to the available width provided by the parent container. The height depends on its content.

The optional link is displayed on the right of the body text. If the horizontal space does not suffice, the body text and optional link wrap.

---

## Anatomy

The banner contains the following elements:

1. Icon indicating the notification type
2. Headline (optional)
3. Body
4. Action (optional)
5. Close button (optional)

![Banner: Anatomy](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/9062c5f6d1d7573bafda27?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133057Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d19319bf5b2d1e2da52286f6020d68d710500f48928d2f4d122559247719bda3)

**Banner: Anatomy**

---

## Usage

Use banners to provide users with non-disruptive messages about system or product level information that is not specific to a task.

Banners should be placed above the page content. 

**Status types**

A status type categorizes the notification that is being communicated. It is important to specify the status type in order to use the correct icon and color.

| **Type** | **Usage** |
| --- | --- |
| Critical | An issue has occurred that prevents further processing. |
| Warning | A problem or inconsistency has arisen. Users can carry on working, but might run into an error later on. |
| Success | An action has been performed without errors or warnings. |
| Information | You want to provide additional, non-critical information. |

**Transition**

To emphasize the appearance of the banner, an animation can be used when initially entering a screen. When navigating to another screen, the banner stays and should not be animated again. 

### Content guidelines

* Be clear with the message. If more text is necessary to explain the situation, use the detailed variation and expand on the context within the message.
* Actions presented within notifications should be directional, and clear on intent. e.g. Learn more, Get started.

### Do's and don'ts

Write in a clear sentence format.

Use only one banner at a time, do not stack to hide previous messages.

Use proper icon and color combination for the notification.

Stick to the provided variants and do not introduce custom icons or colors.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Banner](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Banner)
