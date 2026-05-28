# Tab

Tabs organize page content into different views.

---
title: Tab
url: https://zeroheight.com/0b922d40b/v/latest/p/05c87c-tab
introduction: Tabs organize page content into different views.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Tab: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/84f4dc4b9ccb92e4103b93)

**Tab: Preview**

---

## Design spec

![Tab: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/dac6ac8c3447cb79953824)

**Tab: Design spec**

### Size and scaling

#### Horizontal

The horizontal tab group has a fixed height and a variable width stretching to the parent container. Individual tabs have a fixed height and will shrink to the width of the label (plus optional icon) and its padding.

#### Vertical

The vertical tab group has a fixed width and a variable height stretching to the parent container. Individual tabs stretch to the parent container width and will shrink to the height of the label and its padding.

---

## Anatomy

The tab group contains the following elements:

1. One selected tab
2. Unselected tabs
3. Divider line
4. Overflow indication and buttons at the start and/or end (if applicable)

Individual tabs contain the following elements:

1. Label
2. Icon (optional)
3. Indicator line (if selected)

---

## Usage

Use tabs to enable users to switch between several views of a page within the same context. Only one tab can be selected at a time. Usually the first tab is preselected.

### Placement

The horizontal tab group is placed above the view that is switched with the tab group. The vertical tab group is placed at the left of the corresponding view.

### Overflow

To maintain usability, try to limit the number of tabs to avoid overflow. If the available space is insufficient, the tab group becomes scrollable. Individual tabs should never be truncated. In the overflow state:

* The tab group can be scrolled or swiped without displaying a scrollbar.
* A fade-out gradient at the edges indicates that additional tabs are available.
* Chevron icon buttons appear at the start and end of the tab group.
* If more tabs remain beyond the visible area, clicking a chevron scrolls to the next set of tabs.

### Custom icon color

In some cases it may be useful to color the icons on tabs (e.g. to indicate status).

### Content guidelines

* Always use clear and concise labels for tabs.

### Do's and don'ts

Write in sentence case.

Do not mix tabs with and without icons in the same group.

Do not truncate tab labels. If the space does not suffice, the tab group is scrollable.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Tab](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Tab)
