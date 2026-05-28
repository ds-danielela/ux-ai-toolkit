# Option list

The option list is a list of items that the user can choose from.

---
title: Option list
url: https://zeroheight.com/0b922d40b/v/latest/p/08a681-option-list
introduction: The option list is a list of items that the user can choose from.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Option list: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b34b40621c15399465f409)

**Option list: Preview**

---

## Design spec

![Option list: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7934c3fa7c000b0180acb3)

**Option list: Design spec**

### Size and scaling

The height of the option list depends on the content.

If the option list is used in combination with a dropdown, the width corresponds to the dropdown field width. If it is used in combination with a button, the width is determined by the widest item.

---

## Anatomy

The option list (1) is usually expanded by a triggering UI component (2) such as a dropdown or a button.

The option list itself can contain the following elements:

1. Search field (optional)
2. List items
3. Scrollbar (if applicable)
4. One or more dividers (optional)

Depending on the configuration, option list items contain:

1. Icon (optional)
2. Label
3. Sublabel (optional)
4. Chevron icon to display a sub-menu
5. Checkboxes (in case of multi-selection)
6. Color dot component supplementing the Label

---

## Usage

The option list is already included in the corresponding components that are associated with it (i.e. dropdown, button with option list).

### Sorting

List most common options first or follow some other logical order.

### Position

Per default, the menu is positioned below the corresponding UI element. If the space below the trigger is not sufficient, the option list will be displayed above.

The horizontal position depends on the triggering UI element. In combination with a dropdown, the option lists width corresponds to the dropdown field width. If it is used in combination with a button, the width is determined by the widest item and the default alignment is to the right.

### Content guidelines

* Keep labels and optional text short and concise.
* Only provide a second row of text if it provides value for the user.

### Do's and don'ts

Write in sentence case.

In case of multi-selection, do not provide icons.

If an option list is representing actions, all items should have an icon.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Private/Option%20List](https://storybook-coreui-d2-euw3.d.dscore.com/#/Private/Option%20List)
