# Button

---
title: Button
url: https://zeroheight.com/0b922d40b/v/latest/p/156acf-button
introduction: Buttons are clickable elements that trigger actions.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Button: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a713b06efa7585c4f45831?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133058Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=3802af21a205ec3a59dcc84b3754dca4af20207e9f00e45e91f8602716dcbaa1)

**Button: Preview**

---

## Design spec

![Button: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e196e17250f306553c271c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133058Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=27f34a279e6a0dbc4aee39d222269060338a5c5de568727c9bec70c9ce70c473)

**Button: Design spec**

---

### Size and scaling

The button width depends on the content of the button. In rare cases (or for small form factors), the width can be stretched to the parent container. The height is fixed (label / icon plus spacing).

---

## Anatomy

Buttons can contain a label (1), an icon (2) or both. 

![Button: Anatomy](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/61af990b275afe669dea19?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133058Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=3bfdacae19efff535e4d1ec20e73dbdea9f6e703f3178d7fba63073665c15c7d)

**Button: Anatomy**

---

## Usage

There are several types and variations of button. Choose the type of button depending on the use case.

| **Type** | **Usage** |
| --- | --- |
| Primary | Use the primary button as a call-to-action, engaging the user to follow the primary path of the application user flow. There should only be one primary button per screen (not including the top bar, modal dialog, or drawer). |
| Secondary | Use secondary buttons for actions that are important, but aren't the primary action. Usually the secondary buttons is paired with a primary button, offering an alternative path to the user flow. |
| Tertiary | Use tertiary buttons for supporting functions not directly associated with primary or alternate paths of the application user flow. As the appearance is quite subtle, tertiary buttons mainly occur in toolbars (such as the universal action bar or top bar). |
| Destructive | Use the destructive button for actions that could have destructive effects (for example, delete or remove). It should be used sparingly. |
| On Contrast | Use this button style on surfaces with a contrasting color, i.e. the snackbar. |

| **Variation** | **Usage** |
| --- | --- |
| Text | Use a text button as a default if the button appears alone or in a small group of buttons (e.g. in a form). |
| Icon and text | Use icons in buttons when additional clarity is required and the icon is highly relevant to the action (i.e. an arrow left for navigating back). Icons can also support the prominence of a button. However, they should not be used for decoration. |
| Icon | Use icon buttons only if the metaphor is universally understood. Icon buttons should be used when space is limited, e.g. in focus mode toolbars. Icon only buttons should always be combined with a tooltip. |

### Positioning

In general, buttons close to data or content that they directly impact.

When used in combination, the primary button should be positioned furthest to the right. Further buttons should be positioned to the left of the primary button in order of hierarchy.

### Loading

The button changes to loading state if the action takes a while and thus the button should be blocked. In the loading state, a circular progress indicator is displayed instead of the icon. If a button does not have an icon, the progress indicator replaces the label but the button should keep its original size.

### Enabled vs. disabled buttons

Do not use the disabled state of the primary button, even if not all data is filled yet. There is a risk that the user does not understand why the button is disabled. Instead of disabling the button, show an inline notification explaining what needs to be done.

If the state of buttons depends on a selection like i.e. in the universal action bar, only active buttons should be displayed initially. Once a selection is performed, the actions that can be applied to the selection can be shown. 

### Content guidelines

* Text maximum is one row.
* Text is centered.
* Button labels should be descriptive and specific. Don't just write Yes/No. If possible, add full context at least to the primary button e.g. Delete account or Share media.

### Do's and don'ts

Write in sentence case.

Button labels should be concise. Unnecessary words and articles, such as "the", "an" or "a" should be avoided.

Avoid using negations like "No/Not" in button labels.

Do not use custom colors for button backgrounds, labels or icons. The colors of different button variations have been designed to be consistent and accessible.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Button](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Button)

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Button%20(actions)](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Button%20(actions))

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Button%20(selection)](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Button%20(selection))

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Button%20(multi-selection)](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Button%20(multi-selection))

---

## Hints for designers

**Icon color**

Once you have replaced the default icon by another icon, the icon color does not update accordingly. Thus, you need to manually change the icon color with the following steps:

1. Select the icon
2. Click on the icon color (Icon/Standard)
3. Choose the corresponding color (i.e. Icon/On Primary or Icon/Destructive,...)

**Loading state**

By using component properties, we intended to keep the component structure simple. As a consequence, this requires some manual steps when switching a button with icon and text to loading state.  

1. Select the state "Loading"
2. Expand the button's layer structure
3. Show the label again by clicking on the closed eye in the layers panel
