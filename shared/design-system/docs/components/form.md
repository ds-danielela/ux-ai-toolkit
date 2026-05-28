# Form

---
title: Form
url: https://zeroheight.com/0b922d40b/v/latest/p/39721f-form
introduction: Forms are groups of related inputs to allow users to enter data, submit information, or configure settings.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ⚪️ |

![Form: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/56f9c58968a13090f817bc?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133106Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=b5c3c270dbc00c356f50208f7a10c5feb672a156446f5db345c6db3f0219641e)

**Form: Preview**

---

## Design spec

![Form: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/53a64d25408cbf1aa44746?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133106Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=0adf8714e38574331c94c8dba264647a66e5f2ccfb013973e7a2424c1b7d995a)

**Form: Design spec**

---

### Size and scaling

The form stretches to the available width provided by the parent container. The height depends on its content.

---

## Anatomy

The simple form contains the following elements: 

1. Several form components, such as text fields, dropdowns, date input fields, ...
2. Buttons to cancel or submit the form (exception: not when used in a modal)
3. An inline notification (in case of one or more issues after validation)

The complex form contains the following elements: 

1. Headline
2. Subline (optional)
3. Several form components, such as text fields, dropdowns, date input fields, ...
4. Buttons to cancel or submit the form (exception: not when used in a modal)
5. An inline notification (in case of one or more issues after validation)

---

## Usage

Use a form to allow users to enter data, submit information, or configure settings.

Typical use cases are: 

* Sign up/login to an account
* Taking a survey
* Placing an order or purchasing a product
* Registering for a service
* Configuring settings (e.g. enabling notifications)
* Providing feedback

### Button placement

Forms are usually placed in a container and are left-aligned. If a form is used in a different context, e.g. a modal, the positioning rules of the respective component must be taken into account.

### Enabled vs. disabled buttons

Do not use the disabled state of the primary button, even if not all data is filled yet. There is a risk that the user does not understand why the button is disabled. Instead of disabling the button, show an inline notification explaining what needs to be done.

### Validation

A form is validated after the user has pressed the button to submit the form. If it is going to take a while to process a form, communicate that to the user by using the loading state for the primary button.

### Content guidelines

* Follow the guidelines for the various input components.

### Do's and don'ts

When using a form in the wizard or modal, follow the respective button positioning rules, i.e. right-align buttons in a modal. 

Do not use the disabled state of the primary button, even if not all data is filled yet. There is a risk that the user does not understand why the button is disabled. 
