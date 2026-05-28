# Dropdown

---
title: Dropdown
url: https://zeroheight.com/0b922d40b/v/latest/p/509c11-dropdown
introduction: The dropdown is used for selection of one or more options from a list of predefined options while the component only occupies a small space.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Dropdown: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/4ff7ca812365e1ff36409c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133104Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=dce47a8fd15cb0917c8102f71d6f13f1d14ef59a72aa5d4426290f3470c200e1)

**Dropdown: Preview**

---

## Design spec

![Dropdown: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/108b22e0c25c1773070e44?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133104Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=8daa2de7783f7931e1e925090a7a28a0c5c86d08042eb24ef11145a189cf3c54)

**Dropdown: Design spec**

---

### Size and scaling

The width of the dropdown depends on the parent container. The height is fixed (input text / icon plus spacing). The height of the dropdown menu varies based on available space. On large screens, display 6 full items plus a partially visible 7th before showing a scrollbar; on small screens, display 3 full items plus a partially visible 4th.

---

## Anatomy

A dropdown contains the following elements:

1. Label
2. Text field
3. Selected option / placeholder text
4. Reset option (optional)
5. Chevron icon
6. Option list
7. Help text (optional)
8. Error text (in case of an error)
9. Info button (optional)

---

## Usage

Use a dropdown if you would like the user to choose from a list of i.e. five predefined options or more. If space is critical and the options do not need to be seen at first glance, a dropdown can also be used. 

As a general rule, the width of the dropdown field should be large enough to show the longest valid data, if layout bounds are not overrun. 

### Default state

Only provide a default selection if the user's choice is not critical. Otherwise, do not preselect an option. Once one option has been selected, the user cannot return to having no dropdown option selected unless the "resetable" option is active.

### Placeholder text

If no option is preselected, the placeholder text for dropdowns is usually "Select". 

### Sorting

In a dropdown menu, list most common options first or follow some other logical order. 

### Menu position

Per default, the menu is positioned below the dropdown. If the space below the dropdown is not sufficient, the menu will be displayed above the dropdown.

### Dropdown with search

Especially if a dropdown has a lot of entries, offering a search is recommended. 

### Multi-selection

The dropdown can also be used to provide multi-selection. In that case, the selected options are listed as input tags within the dropdown field. It is possible to define two orders for tags: alphabetical and the order of selection.

Additionally, already selected items can optionally be listed on top, separated by a divider. The reordering applies after closing the dropdown. 

The dropdown supports multiselection of list items with color dot (i.e. materials). Once selected, colored variant of Removable tag is being displayed within the input field.

### Content guidelines

* Keep labels, placeholder text, helper text and error message short and concise. 
* The helper text should not simply repeat the label or placeholder information.
* Provide error messages that guide users to solve the problem.

### Do's and don'ts

Use sentence case for label, placeholder text, options, helper text and error message.

Do not mark required dropdowns as the user should be asked only for information that is really needed. 

Do not repeat the label or placeholder information with the helper text. Avoid redundant information.

Provide useful error messages that guide users to solve the problem. 

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Dropdown](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Dropdown)

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Dropdown%20(multi-selection)](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Dropdown%20(multi-selection))
