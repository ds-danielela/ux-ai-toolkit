# Checkbox

---
title: Checkbox
url: https://zeroheight.com/0b922d40b/v/latest/p/546c9e-checkbox
introduction: Checkboxes allow users to choose one ore multiple items from a list of individual items, or to mark one individual item as selected.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Checkbox: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/83f15efbe1a8cff262d216?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133059Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=28b9c5ea3d0368fb3417ee7d58a1a4f7256e01f51b4985a6e89e07fa58fdaf46)

**Checkbox: Preview**

---

## Design spec

![Checkbox: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/edb3609c0e2293b1623588?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133059Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=2de6f93f15e7a421fb5b93824417da02a1864fe7c72ac1edb35aa1e606a86407)

**Checkbox: Design spec**

---

### Size and scaling

The checkbox group width stretches to the parent container. The height depends on the content.

---

## Anatomy

The checkbox (1) is usually combined with a label (2). Additional information can optionally be displayed in a sublabel (3).

![Checkbox: Anatomy](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/98781f3d948f4033e00378?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133059Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=62e9020273a2b5be85560c2711a8a94dc38906d796d90262c44dfd79dc360810)

**Checkbox: Anatomy**

---

## Usage

Use a checkbox to offer the user an independent or non-exclusive choice. The state of the checkbox should toggle when clicking on the checkbox or the corresponding label.

Checkboxes can also be nested hierarchically. For example, if only one sub-entry was selected, the corresponding parent element changes to tri-state.

Standalone checkboxes (without a label) are only used when their connection to other components is clear and they give sufficient context — for example for multi-selection within tables.

### Sorting

In a checkbox group, list most common options first or follow some other logical order. As it is language depended, alphabetical sorting is not recommended.

### Switch vs checkbox

Use switches to communicate activation (turning an option on or off), whereas checkboxes are best used for communicating selection (i.e. table rows, a list of related options).

Unlike checkboxes, switches do not have an indeterminate state. If you need to show an indeterminate state, i.e. when representing an hierarchical selection, use checkboxes.

If a single binary yes/no choice is provided and its meaning is obvious, use a checkbox.

### Error state

Checkboxes can have an error state to indicate that a selection is mandatory before proceeding.

### Content guidelines

* Always use clear and concise labels for checkboxes.
* If you are tight on space, consider rewording the label. Long labels may wrap to a second line, and this is preferable to truncation.

### Do's and don'ts

Do not use commas or semicolons at the end of each line.

Use checkboxes for non-exclusive choices, if the options can be selected independently of each other. If the user can only select one option from a list, use a radio button instead.

Write in sentence case.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Checkbox](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Checkbox)
