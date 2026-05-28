# Progress menu

The progress menu collects long-lasting activities such as uploads or downloads.

---
title: Progress menu
url: https://zeroheight.com/0b922d40b/v/latest/p/32398b-progress-menu
introduction: The progress menu collects long-lasting activities such as uploads or downloads.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Progress menu: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/fe3a87cc40bf9f69b2a132)

**Progress menu: Preview**

---

## Design spec

![Progress menu: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c63fb8c8b6d9172d5c6392)

**Progress menu: Design spec**

### Size and scaling

Similar to the icon button, the progress menu button has a fixed width and height of 40 px.

The progress menu has a fixed width of 400 px for responsive layout M - XL and 328 px for responsive layout S. The height depends on the number of contained items.

---

## Anatomy

The progress menu (1) is triggered by the progress menu button (2). The progress menu button is a tertiary icon button containing an indeterminate progress bar. The upper part of the menu includes a title (3) as well as optional tertiary button to cancel outstanding tasks (4).

The main part of the progress menu includes list items (5).

Progressing list items contain a determinate progress circle (1), successfully progressed items contain an icon (2). All list items contain a headline with the file name (3) and a description (4). An optional icon button (5) can be used to remove uploaded files or to cancel progressing items. Potentially failed or cancelled items include an icon (7) and an icon button to retry (8).

---

## Usage

Use the progress menu to provide the user with access to long-lasting activities such as uploads or downloads. The progress menu button is shown, once a long-lasting activity has been triggered. If the user clicks on the progress menu button, the progress menu is shown below. The progress menu is closed again when the user clicks on the progress menu button or on the area outside the menu.

After all tasks have been finished, the progress menu button disappears and a toast displays the respective outcome:

* If all tasks were finished successfully, a success toast is displayed with the number of tasks.
* If there were errors for one or more tasks, an error toast should be displayed showing how many tasks have been finished successfully and how many tasks resulted in errors.

### Position

The progress menu is right-aligned with the progress menu button. If there is not enough horizontal space on the right, like on responsive layout S, it will be shifted accordingly.

### Do's and don'ts

Only show a progress menu button if the task(s) take longer than a few seconds.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Progress%20Menu](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Progress%20Menu)
