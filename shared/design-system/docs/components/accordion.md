# Accordion

---
title: Accordion
url: https://zeroheight.com/0b922d40b/v/latest/p/435154-accordion
introduction: An accordion is a container that contains expandable sections.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅  |

![Accordion: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/26010c5d0ae5ba49009f65?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133055Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=96c2c7b11248996174762ed6c4978c3dea83136380b24e975bedb866caa15db6)

**Accordion: Preview**

---

---

## Design spec

![Accordion: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/23d8852efbdff36a53823d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133055Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=41f15c058c50e733235837b75994013de9a5c98b0b8414e5f00db5674d464596)

**Accordion: Design spec**

---

### Size and scaling

The height of the accordion depends on the content. The width of the accordion usually stretches to the width of its parent container (among several responsive layout columns). 

Use size variant to control typography and paddings:

**Base** - default spacing and type scale for most pages.

**Compact** - tighter spacing and smaller type for dense layouts (e.g., side sheets, modals).

Note: Size is not the same as responsive "Small mode". Use "Small mode" only for responsive layout S.

---

## Anatomy

The accordion can optionally be wrapped in container (1). 

![Accordion: Anatomy](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/8063dd4fc7af53dca4f692?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133055Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=7840dd1b9f8985c8b7c38af1ba8f2c9d5b5df2e59dff819a72ece87cf377c488)

**Accordion: Anatomy**

---

An accordion item contains the following elements:

1. Headline (title)
2. Subline (optional)
3. Chevron icon showing whether it is collapse/ expanded
4. Up to two optional actions
5. Body with text or individual content
6. A divider line at the bottom (excluding the last item)

![Accordion: Item anatomy](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1695baeb3c362bd5058c17?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133055Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=11db9c3c6691af18d2dc921dae1bd959b0b40e999606c11c89e97c2bfb213426)

**Accordion: Item anatomy**

---

---

## Usage

Use an accordion to group related information in collapsible sections.

The user can expand or collapse accordion items by clicking on the whole title area of the item (headline, subline, icon + padding). The chevron icon at the right indicates if the corresponding item is collapsed (chevron points down) or expanded (chevron points up). Depending on the configuration, either one or multiple items can be open at the same time.

**Skeleton state**

In its loading state, the accordion is represented by a simplified vertical stack of pill-shaped skeletons that reflect the structure of headers and content areas. The expand/collapse icons and buttons are omitted, and no interactive behavior is present.

![Accordion: Skeleton](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c52efb6882c3da6ad76df6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133055Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=48d2eb3c12cab07e6e0dbe9e78ff5d5086bf0e84b0d4c18d9ad31f26de777a39)

**Accordion: Skeleton**

---

### Content guidelines

* Keep the title short and specific.
* Use a subline to add context when the headline alone may be ambiguous. Keep the subline as short and concise as possible.

### Do's and don'ts

Write in sentence case.

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Do | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/563b474d54bf0019752fe8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133055Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=4e7c5f2837973556a909d39c9d01393399f09a08c9476bb83be334db2da584a9) |   |   |
| Don't | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1558f4c942979ce24ac564?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133055Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=29c2def1ff7130715f8dc55f6f3aa71cca61d6a302567b4633373883ab6234e8) |   |   |

Do not nest accordions. Use separate accordions instead.

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Do | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1f12dd56c5f6a65e56b7c2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133055Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=49f0143c2563d15e1641bbe2328cd3d07712a1ff8715a0615ca4e6ad8f28c30c) |   |   |
| Don't | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/404962ae30f3cd7fda7488?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133055Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=8b771a5a2448cd7ff7771390d487bd6420e30e0c2d5f6da5803f00918399518) |   |   |

Use the accordion wrapped in a container when it is placed stand-alone on a page. If it is part of another wrapping element, such as a side sheet, modal dialog, etc. it should not be wrapped in a container. 

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Do | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/78f9116533d68d8f7a3c27?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133055Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=175525e107ace94fe2b7a4373e890d472a6efe792997c52535d6e2bb7c5f3d1c) |   |   |
| Don't | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/8f6e00f48462ae1e2624d7?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133055Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=c726a8c71f9cee74fca4e576ac5141c1d5db1dd6a4c32bfe0a3f9dbba7485fbf) |   |   |

Use compact size variant for dense layouts.

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Do | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/963f57cde245986dc65de0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133055Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=91d1e2fbefd70a0477a1b390db1cdb8a760dfa2bcc21f8f45148ff25a48fb11e) |   |   |
| Don't | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/dae8fde66e54c670f63550?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133055Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=3f6f64f3cbf3f9a9a43d412410a757225f82d3a1800132f36d71e7ff03fc728f) |   |   |

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Accordion](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Accordion)
