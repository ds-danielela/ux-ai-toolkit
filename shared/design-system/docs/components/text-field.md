# Text field

A text field allows the user to edit a single-line text.

---
title: Text field
url: https://zeroheight.com/0b922d40b/v/latest/p/523b03-text-field
introduction: A text field allows the user to edit a single-line text.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Text field: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a093a797f995ae9e3923b3)

**Text field: Preview**

---

## Design spec

![Text field: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/675e57f42e5cccd905c1fc)

**Text field: Design spec**

### Size and scaling

The width of the text field depends on the parent container. The height is fixed (input text / icon plus spacing).

---

## Anatomy

A text field contains the following elements:

1. Label
2. Text field
3. Input / placeholder text
4. Icon (optional)
5. Help text (optional)
6. Error message (in case of an error)
7. Info button (optional)

---

## Usage

Use a text field to enable users to enter a single line plain text, i.e. name, email, password, etc.

As a general rule, the width of the input field should be large enough to show the longest valid data, if layout bounds are not overrun.

### Required fields

Only ask the user for information that is really needed. Therefore, there is no need to mark required fields. If in an exceptional case a field is optional, this should be indicated by the addition "(optional)" to the label.

### Help text

Use help text below the text field to provide the user with information on how to fill out the text field or why the information is necessary. If an error is detected during validation, the error message replaces the help text.

### Placeholder text

Placeholder text is displayed inside the input field and disappears as soon as the user focuses the field. Since placeholder text is not accessible it should only be used for non-critical information.

### Numeric field

Within numeric fields, text is right aligned and combined with a unit. The unit cannot be overwritten.

### Content guidelines

* Keep labels, placeholder text, help text and error text short and concise.
* The help text should not simply repeat the label or placeholder information.
* Provide error messages that guide users to solve the problem.

### Do's and don'ts

Use sentence case for label, placeholder text, help text and error text.

Do not mark required fields as the user should be asked only for information that is really needed.

Do not repeat the label or placeholder information with the helper text. Avoid redundant information.

Provide useful error messages that guide users to solve the problem.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Text%20Field%20(Input%20Field)](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Text%20Field%20(Input%20Field))

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Text%20Field%20(numeric)](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Text%20Field%20(numeric))
