# Switch

The switch allows the user to activate or deactivate an option.

---
title: Switch
url: https://zeroheight.com/0b922d40b/v/latest/p/7699c7-switch
introduction: The switch allows the user to activate or deactivate an option.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Switch: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c7ffa55921ab51e792758c)

**Switch: Preview**

---

## Design spec

![Switch: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1bf0c0a2ec82e8a1411105)

**Switch: Design spec**

### Size and scaling

The switch has a fixed width of 40px and a fixed height of 24px.

---

## Anatomy

The switch (1) is usually combined with a label (2). Additional information can optionally be displayed in a sublabel (3).

---

## Usage

Use a switch to allow the user to activate or deactivate an option. The state of the switch should toggle when clicking on the switch or the corresponding label. If multiple switches are used in the same group, every item represents a non-exclusive choice that is not dependent on the state of other items from that group.

### Switch vs checkbox

Use switches to communicate activation (turning an option on or off), whereas checkboxes are best used for communicating selection (i.e. table rows, a list of related options).

Unlike checkboxes, switches do not have an indeterminate state. If you need to show an indeterminate state, i.e. when representing a hierarchical selection, use checkboxes.

If a single binary yes/no choice is provided and its meaning is obvious, use a checkbox.

### Content guidelines

* Always use clear and concise labels for switches.

### Do's and don'ts

Do not include terms like on/off in the label. The switch alone is representing the state change in a sufficient way.

Use switches for turning on/off a small set of independent options. For larger sets or related options, use checkboxes instead.

Write in sentence case.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Switch](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Switch)
