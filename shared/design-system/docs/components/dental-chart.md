# Dental chart

---
title: Dental chart
url: https://zeroheight.com/0b922d40b/v/latest/p/19ffd6-dental-chart
introduction: The dental chart allows the user to select one or more teeth or to specify details for specific teeth.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Dental chart: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e21ae7128f363bf14d0092?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133104Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=c9fef415b88e6bc5877a10d47e76eb8db1ee8767146e259dc3bcd0fd6ecacbc7)

**Dental chart: Preview**

---

## Design spec

![Dental chart: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/fe4997d3bdf8a90318fcca?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133104Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=27ae16cf4983f7f94291db30e237e78046115dff35ee14bddc2a58613c04b711)

**Dental chart: Design spec**

---

### Size and scaling

The dental chart width can either be stretched to its parent container. In that case the individual buttons stretch accordingly, respecting a minimum width of 40px. Alternatively, the dental chart is as wide as its content.

The height of the dental chart and its buttons is fixed. If horizontal space does not suffice, the dental chart can be scrolled. 

---

## Anatomy

The dental chart contains various buttons. Each button contains the following elements: 

1. Tooth number
2. Tooth illustration
3. Condition (optional)
4. Tooth annotation (only for read mode)

---

## Usage

Use the dental chart to allow the user to select one or more teeth or to specify details for specific teeth. 

**Selecting teeth**

For some flows, e.g. placing a restoration order, teeth have to be selected. In this case, the tooth is selected when the user clicks on it and deselected when clicking again. 

**Specify details**

For other flows, more details must be specified for the selected tooth. These can for example be retrieved in a popover that appears when you click on the tooth. 

**Notation**

The dental chart supports three notations: the FDI notation (following ISO 3950), the universal notation as well as the Palmer notation. The user is able to switch between the notations in the user settings.

If the Palmer notation is used, an identifier for the jaw (i.e. UR, UL, LR, LL) must always be added when referring to the selection in the dental chart. 

**Responsive layout S**

If the dental chart is used on smaller viewports (i.e. responsive layout S), it can be scrolled / swiped horizontally.

**Read only mode**

If no changes can be made to the teeth, i.e. on the work sheet or in the treatment detail screen, the read only state should be used. In the read only state, backgrounds, borders and shadows of the individual teeth are omitted. 

**Tooth annotations**

Certain workflows require further details to be displayed, i.e. where an attachment should be placed or where IPR is necessary during an aligner treatment or if a tooth needs to be extracted before placing an implant.

**Skeleton state**

When loading, the dental chart is displayed as two simplified rows of box-shaped skeletons, representing the individual tooth buttons. All shadows and interactive styling are removed to reduce visual noise and maintain a clean, neutral appearance.

### Content guidelines

* Combine the dental chart with a description telling the user what to do next. 

### Do's and don'ts

Stick to the provided variants and do not introduce custom icons or colors.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Dental%20Chart](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Dental%20Chart)

---

## Hints for designers

**Read only mode**

In order to switch the dental chart into read only mode, all teeth need to be selected and set to "Read only". To quickly select all teeth, select the dental chart and press the "Return" key two times.
