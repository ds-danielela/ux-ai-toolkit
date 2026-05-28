# App indicator

---
title: App indicator
url: https://zeroheight.com/0b922d40b/v/latest/p/2601c1-app-indicator
introduction: App indicator is a UI element that identifies which app the user is in within the DS Core by helping them recognize the app at a glance, which reduces reduces ambiguity.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![App indicator: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/8b75be3e912397dbb37a8f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133056Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=e7579fe75bf582f865c1d88c76e38c0050179eb957aee526a7d44e143d09f352)

**App indicator: Preview**

---

## Design spec

![App indicator: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c963bf463d3e9eff5d6256?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133056Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=744bfd0bf0f3750b6ed2b5f84b4076d771526a7611b024ef1aaf16dc7721a66b)

**App indicator: Design spec**

---

### Size and scaling

App indicator component comes in one size that is used only within the focus mode header. Both the width and height are fixed regardless on where they are used.

---

## Anatomy

App indicator consists of the following elements:

1. Container
2. Icon

Container is a background that uses a dedicated color style gradient associated with the app (1). Icon used is also connected directly to the app (2).

![App indicator: Anatomy](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6a210e3211f45e1a226104?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133056Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=df60e4b25b4b00a2b1490ab553c0fb27213e4d6bc656ec8b8a9310cc845ed41b)

**App indicator: Anatomy**

---

## Usage

App indicator component is used as a mandatory element within the focus mode header in the top-left area, next to the patient unique identifier. Tooltip appears while hovering over the app indicator to preview the application name to the user. The same tooltip is displayed while long-pressing on the app indicator on touch devices like mobile.

**Correct usage:** App indicator can only be used within the Focus mode header (top-left). For now, there are no other supported cases to use this component elsewhere.

![App indicator: Usage](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/30db22da868daab9d935e0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133056Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=ebd799c787a99803071e601f758ca9c95823d3cca4ce19d07b95ba51558132a3)

**App indicator: Usage**

---

### Content guidelines

* Use appropriate app indicator and tooltip label for the context of the application

**Missing app indicator:** If an app indicator related to a specific application is missing from the available variants, please submit a request to have it added.

### Do's and don'ts

Don't change the placement of the app indicator on the focus mode header. App indicator is positioned left of the patient unique identifier.

Don't change the color of the container. Each gradient color style is connected and associated with specific app.

Don't change the color of the icon. Icons on the app indicator should only use the Icon/Standard color token.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Private/App%20indicator](https://storybook-coreui-d2-euw3.d.dscore.com/#/Private/App%20indicator)
