# Info modal

---
title: Info modal
url: https://zeroheight.com/0b922d40b/v/latest/p/48830f-info-modal
introduction: The info modal is a specific modal which displays further information to the user if requested.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Info modal: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c9ee225db9afc67f6878df?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133112Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=e199147ecff869977e4f28e0ae47d648d8cf7575446f6813bf857c93fad07395)

**Info modal: Preview**

---

## Design spec

![Info modal: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6c11cea1d22211cbaf9d44?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133112Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=592067cbf26848a182fbdd1758ec3e1574a23b43dd23d391b467e9d80b2252fa)

**Info modal: Design spec**

---

### Size and scaling

Depending on the amount of columns, a different size variation of the modal is used.

| **Number of columns** | **Modal size** |
| --- | --- |
| 1 | Small |
| 2 | Medium |
| 3 | Large |
| 4 | Large |

The individual columns stretch to the body width of the modal dialog, considering a minimum width of 272px per column. If not all columns can be displayed completely, the modal content can be scrolled horizontally.

---

## Anatomy

The info modal is a modal (1) that contains one or more information columns (2).

Each info column can contain the following elements:

1. Image
2. Headline
3. Body: either a paragraph of text (a) or a bullet list (b)

---

## Usage

Use the info modal to display further information to the user if requested. The info modal is typically triggered by the info button.

### Content guidelines

* Use clear, concise language that directly addresses the user's need for information. Avoid adding unnecessary details or redundant content.
* Each modal should provide information about a single subject or feature to prevent overwhelming the user. If multiple topics need to be covered, consider separate modals or linking to additional resources.

### Do's and don'ts

Provide a balanced amount of information in all columns.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Info%20modal%20dialog](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Info%20modal%20dialog)
