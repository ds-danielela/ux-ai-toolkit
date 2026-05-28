# List

---
title: List
url: https://zeroheight.com/0b922d40b/v/latest/p/37109e-list
introduction: A list contains multiple similar items.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![List: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0d887dea52f5c2f1da9082?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133113Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=644965d84a83ad5217098db557345fecce4279e28a5244439df8621b949b86d6)

**List: Preview**

---

## Design spec

![List: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/65b9566fec2daffaa63e6b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133113Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=34e65a49e005bf3f9a714cd9c20e3db7343791854b2ce3185146c36edfc0829e)

**List: Design spec**

---

### Size and scaling

The height of the list depends on the content but can also be set by the parent container. The width of the list stretches to the width of its parent container. 

---

## Anatomy

A list contains several list items. Each list item has a headline (1) and body (2). It can additionally have actions (3). Each list item contains a divider line (4) at the bottom (excluding the last item). List items can also contain icons (5) or images (6) or avatars (7). Within the file upload, the icon can also be replaced by a progress circle (8). The headline can also be supplemented by a color dot (9).

---

## Usage

Use a list to present a set of simple and similar data. For more complex data, use a table instead. 

**Sorting**

Order list items in a logical way. In a list of comments with an input field below to add a new comment, new comments should be added to the bottom of the list.

**Skeleton state**

The list component uses a flexible skeleton layout that adapts to the structure of its items. Each list item is represented by a simplified arrangement of skeleton shapes—such as circles for avatars or icons, boxes for images, and pills for text content. Interactive elements like buttons are omitted to avoid implying functionality during loading. If a color dot is part of the item, it is shown as a neutral, non-colored skeleton circle.

### Content guidelines

* Keep the headline short and specific.
* All list items within one list should be structured in the same way. 

### Do's and don'ts

The structure of items in a list should be similar. 

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/List](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/List)
