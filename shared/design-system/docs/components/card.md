# Card

---
title: Card
url: https://zeroheight.com/0b922d40b/v/latest/p/172ef8-card
introduction: Cards are interactive surfaces that display content. They can either be used for a selection or for navigation.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Card: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/666f113e5b9b707169212e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133058Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=eff2f09ba3463b0e29acc2cfde517c13c6ed7b0e4f8c1f8aaf8abefc7a622f7a)

**Card: Preview**

---

## Design spec

![Card: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ae67e83e0142018f9bd3dd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133058Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=498caf86becb690948b5d975c7b00be934d828bef69425a06e4850ed5c635ff5)

**Card: Design spec**

---

### Size and scaling

The height of the card usually depends on the content but can also be stretched according to the height of other cards in the same row. Multiple cards can be displayed in a row, thus their width depends on the definition of how many cards should be displayed in one row.

---

## Anatomy

The spacious card is a rounded box (1) with a headline (2) and body text (3) and/or individual content. It could also contain an optional image (4) and status tags (5) in addition. A card can optionally contain a toolbar (6) or one icon overflow button (7).

The compact card is an additional variation that is optimized for choosing a service or similar in wizards. It also contains a label (1) and an optional sublabel (2). In addition it either contains an avatar (3), an icon (4) or an image (5).

---

## Usage

Use a card to enable the user to navigate or for a selection that is more prominent and includes flexible content. Unlike the container, the card is clickable.

**Displaying multiple cards in a group**

The height of all cards in one row should be aligned. If one card contains multiple lines of text, the remaining cards in the same row stretch to the same height while the text is vertically centered.

**Disabled state**

In the disabled state, the card component applies reduced opacity to image and status tags when present. All textual content adopts the designated disabled color. In addition, all shadows are removed, reducing visual prominence while preserving the component's overall structure.

**Skeleton state**

In the skeleton state, the card component is displayed as a simplified layout that mirrors its overall structure. Content areas are represented by box- and pill-shaped skeletons, depending on the type of content they hold. All shadows and interactive elements—such as buttons—are removed to reduce visual noise and avoid implying interactivity.

### Content guidelines

* Keep the headline short and specific.

### Do's and don'ts

Write in sentence case.

When providing a set of cards for selection or navigation, the structure of all cards should be similar.

Spacious cards either contain a toolbar or one icon overflow button. Do not provide both.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Card%20(compact)](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Card%20(compact))

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Card%20(spacious)](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Card%20(spacious))
