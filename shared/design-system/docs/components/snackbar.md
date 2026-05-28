# Snackbar

Snackbars are temporary messages that give immediate feedback about a user action.

---
title: Snackbar
url: https://zeroheight.com/0b922d40b/v/latest/p/875abc-snackbar
introduction: Snackbars are temporary messages that give immediate feedback about a user action.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Snackbar: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/cfa4f6b4f2b8b20d4425e8)

**Snackbar: Preview**

---

## Design spec

![Snackbar: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d77e981acbdb84b2b2e4eb)

**Snackbar: Design spec**

### Size and scaling

The size of the snackbar adjusts to the content inside. The snackbar can grow to accommodate content until it reaches the maximum width of 800 px for responsive layout M - XL. When the snackbar contains more text, it wraps.

On responsive layout size S, the snackbar also automatically adjusts its width based on the content.

If the width does not suffice, the action can wrap into a new line.

---

## Anatomy

The snackbar contains the following elements:

1. Surrounding box
2. Body text
3. Icon or progress circle (optional)
4. Action (optional)
5. Inline link (optional)

---

## Usage

Use a snackbar to provide quick and lightweight feedback on a recently performed action or system occurrence. Snackbars are temporary messages that give immediate feedback about a user action. They communicate the success or failure of an action, with an optional button to revert a decision or correct a failure. Snackbars are designed not to distract or require significant cognitive effort.

### Positioning

The snackbar is displayed at the bottom of the screen, ensuring a spacing of "Layout.M" from the bottom edge of the screen and to the sides.

When the snackbar would obstruct crucial UI elements such as a pinned toolbar, it is moved upward so that it has "Spacing.Layout.M" spacing from the top edge of the pinned toolbar component.

### Actions

* Snackbars use a button "On Contrast" variation for actions.
* A snackbar offers a maximum of one action to be performed.
* Actions include cancelling an upload or transfer (Cancel), undoing an action that was taken (Undo), retrying an action that failed (Retry), or viewing or navigating to an item that was just created (View).
* When the snackbar action is clicked, it could trigger a confirmation snackbar.

### Motion and timing

* The snackbar appears by sliding up from the bottom of the screen and disappears after the set duration by sliding down.
* If the snackbar contains longer text and/or an action, it disappears after 5000 ms.
* If the snackbar contains one line of text and no action, it disappears after 3000 ms.
* A snackbar that communicates an error briefly vibrates shortly after sliding in.

### Persistence rules

Snackbars can be persistent in the following cases:

* If the snackbar contains an action that blocks further user progress, such as "Try again".
* If the snackbar informs the user of connectivity issues that prevent progress.
* If the snackbar communicates an ongoing action such as uploading or downloading files.
* If the snackbar has the mouse cursor hovering over it or has keyboard focus.

### Combination with progress menu

During long-lasting activities such as uploads or downloads, a progress menu appears at the top of the interface. In this case, a snackbar informs users that the system is processing the selected files.

### Only one snackbar at a time

To maintain clarity and avoid overwhelming users, only one snackbar should be visible at any given moment. If multiple messages are triggered in quick succession, they should be queued and displayed one after the other.

### Content guidelines

* Be efficient, not conversational. Don't use filler words like "You have," "Successfully," or "We."
* Prioritize scannability. Users glance at snackbars, they don't read them.
* Use 1 sentence whenever possible. Max 2 short sentences (~90 characters total).
* Never put a full stop at the end of the message, even if it's a full sentence.

| Type | Writing guidelines | Example |
| --- | --- | --- |
| Success | Formula: [Noun] + [Verb -ed] + [optional context]. E.g.: Share sent. | (image) |
| Critical | Formula: Couldn't + [Action] + [Object]. E.g.: Couldn't upgrade plan Try again. | (image) |
| Loading | Formula: [Verb -ing] + [Noun]…. E.g.: Copying resources…. | (image) |

### Do's and don'ts

Use snackbar for feedback, acknowledgements, internet connection status, or file upload status. Do not use snackbar for global messaging, engagement or marketing communication.

Do not mix and match colors and icons of snackbar.

Provide follow-up for actions performed through snackbar actions undo and try again.

Use recognizable and plain actions: cancel, undo, view, retry.

Don't stack snackbars. If you need to display more than one snackbar, wait or expedite the dismissal of the previous one.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Snackbar](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Snackbar)

---

## Hints for designers

**Max. width**

If the content exceeds this width, you must manually activate the "Max. width" option to prevent layout issues and maintain proper text wrapping.
