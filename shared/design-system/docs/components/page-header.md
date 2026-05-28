# Page header

The page header is displayed at the top of several page types. It mainly contains the headline of the page and other options if needed.

---
title: Page header
url: https://zeroheight.com/0b922d40b/v/latest/p/788503-page-header
introduction: The page header is displayed at the top of several page types. It mainly contains the headline of the page and other options if needed.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Page header: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/33919df4ececbcddef161c)

**Page header: Preview**

---

## Design spec

![Page header: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/64954127d2d6471bb863ee)

**Page header: Design spec**

### Size and scaling

The page header width stretches to the available width. The height depends on its content.

---

## Anatomy

The page header can contain the following elements:

1. Headline
2. Subline (optional)
3. Status tag(s) (optional and only on second level pages)
4. Actions (optional)
5. Back button (only on second level pages)

---

## Usage

Use the page header in the main content area of top and second level pages.

**Please note:** Corresponding layout templates already contain a page header.

### Overflow behavior

In general, not more than three buttons should be displayed in the page header. Further options can be revealed with an option list.

For responsive layout S, only one button should be displayed in the page header. This button can optionally open an option list containing all possible actions.

### Scrolling behavior

The page header can either scroll away or stay sticky. When it is sticky and the user scrolls the page, the page headers appearance is reduced:

* The back button scrolls away.
* The headline gets smaller.
* The spacing is reduced.
* The optional page description disappears.

### Content guidelines

* Keep the headline short and specific.
* On second level pages, the back button label should match the headline of the corresponding top level screen.

### Do's and don'ts

Use sentence case for headline and description.

Don't overcrowd the page header with too many actions.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Templates/Scrollable%20Page%20With%20Main%20Menu](https://storybook-coreui-d2-euw3.d.dscore.com/#/Templates/Scrollable%20Page%20With%20Main%20Menu)
