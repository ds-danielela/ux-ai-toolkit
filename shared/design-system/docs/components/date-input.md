# Date input

---
title: Date input
url: https://zeroheight.com/0b922d40b/v/latest/p/1214b6-date-input
introduction: The date input is used to allow the user to specify or quickly choose a date.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Date input: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ee48a3157b6c453ca73fab?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133103Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=1d459090ec8b4c95cdb2d206e57f1e3d97a9881a4009c34ab3a5a72ef69acca7)

**Date input: Preview**

---

## Design spec

![Date input: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3fcf3498b7160cb337cc7f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133103Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=2cc2718088bd270714c059e4a04bada91aa8661ecb2829c42ba0705facde3538)

**Date input: Design spec**

---

### Size and scaling

The width of the date input field depends on the parent container. The height is fixed (input text / icon plus spacing). The width and height of the date picker is fixed. The date picker is always right aligned.

---

## Anatomy

A date input contains the following elements:

1. Label
2. Date input field
3. Selected date / placeholder text
4. Calendar icon
5. Date picker
6. Helper text (optional)
7. Error message (in case of an error)
8. Info button (optional)

---

## Usage

Use a date input to allow the user to specify a date by typing or quickly choosing it in the date picker that is shown when clicking on the calendar icon.

If the field is empty, a placeholder indicates the expected format. 

The date picker initially opens in day mode. In that mode, all days of a month are shown in a grid format. Clicking on the arrows on the top right switches to the previous / next month. Clicking on the month and year on the top left switches to year mode. Clicking on one year or on the month and year on the top left switches to day mode again. 

### Date ranges

The design system does not provide a dedicated date range picker component yet. Thus, it is recommended to use two individual date input fields to capture the start and end dates of a range.

If the "To" field is left blank and the user presses "Apply", it will be set to the current date.

If no "From" date is specified, a locale-specific term in the button indicates that the date range includes anytime before the specified "To" date.

### Content guidelines

* Keep labels, placeholder text, helper text and error message short and concise. 
* The helper text should not simply repeat the label or placeholder information.
* Provide error messages that guide users to solve the problem. 

### Do's and don'ts

Use sentence case for label, placeholder text, helper text and error message.

Provide a useful default value only if applicable. I.e. when entering a date of birth, pre-filling the field with the current date does not provide added value.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Date%20Input%20Field](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Date%20Input%20Field)
