# Text area

Text areas indicate that users can input multiple lines of data.

---
title: Text area
url: https://zeroheight.com/0b922d40b/v/latest/p/87c9c9-text-area
introduction: Text areas indicate that users can input multiple lines of data.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Text area: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c3bc7e753b19a36f90cb91)

**Text area: Preview**

---

## Design spec

![Text area: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/767fbeff195e4e903b9340)

**Text area: Design spec**

### Size and scaling

The width and height of the text area depend on the parent container.

---

## Anatomy

A text area contains the following elements:

1. Label
2. Text area
3. Input / placeholder text
4. Help text (optional)
5. Error text (in case of an error)
6. Info button (optional)

---

## Usage

Use a text area to enable users to enter a multi line plain text, i.e. a message or comment.

As a general rule, the width and height of the text area should be large enough to show the longest valid data, if layout bounds are not overrun.

### Required fields

Only ask the user for information that is really needed. Therefore, there is no need to mark required fields. If in an exceptional case a field is optional, this should be indicated by the addition "(optional)" to the label.

### Help text

Use help text below the text field to provide the user with information on how to fill out the text area or why the information is necessary. If an error is detected during validation, the error message replaces the help text.

### Placeholder text

Placeholder text is displayed inside the text area and disappears as soon as the user focuses the text area. Since placeholder text is not accessible it should only be used for non-critical information.

### Content guidelines

* Keep labels, placeholder text, help text and error text short and concise.
* The help text should not simply repeat the label or placeholder information.
* Provide error messages that guide users to solve the problem.

### Do's and don'ts

Use sentence case for label, placeholder text, help text and error text.

Do not mark required fields as the user should be asked only for information that is really needed.

Do not repeat the label or placeholder information with the help text. Avoid redundant information.

Provide useful error messages that guide users to solve the problem.

Use the text area only if you expect input with more than one line. Otherwise use an input field.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Text%20Field%20(Input%20Field)](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Text%20Field%20(Input%20Field))
