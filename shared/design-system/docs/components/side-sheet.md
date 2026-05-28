# Side sheet

Side sheets slide in from the left or right edge of the screen.

---
title: Side sheet
url: https://zeroheight.com/0b922d40b/v/latest/p/7675c3-side-sheet
introduction: Side sheets slide in from the left or right edge of the screen.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Side sheet: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a20c85c18c17b8fd1cbdf6)

**Side sheet: Preview**

---

## Design spec

![Side sheet: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c5aae4cda2ef0bd76e6688)

**Side sheet: Design spec**

### Size and scaling

The side sheet stretches to the full height of the screen. The width of the side sheet depends on the respective variant (small, medium, large). If the width exceeds the available screen width, the side sheet stretches to the full width of the screen.

---

## Anatomy

The side sheet contains the following elements:

1. Headline, optionally accompanied by subline (optional)
2. Close button (optional)
3. Individual content

---

## Usage

Use a side sheet to provide context-sensitive actions and information on demand.

The side sheet overlaps the underlying content. The side sheet closes when the user clicks on the close button or another terminating action button within the side sheet (like Cancel or Submit). For responsive layout M - XL, the user can also close the side sheet by clicking on the area outside of the side sheet.

**Overflow**

If the vertical space does not suffice, the side sheet content can be scrollable. Close button, headline and subline will stay sticky. Headline and subline can wrap and should not be truncated.

**Please note:** In focus mode, a separate component "Focus mode side sheet" is used.

**Hiding headline and close button**

The headline and close button in a side sheet should only be omitted in exceptional cases where saving vertical space is critical. If the close button is removed, ensure that the side sheet can still be dismissed through an alternative, clearly discoverable mechanism.

**Skeleton state**

In its skeleton state, the side sheet is displayed as a simplified container, reflecting the general layout without revealing specific content. Static elements may remain visible to improve perceived performance and layout stability.

### Content guidelines

* Keep the headline short and specific.

### Do's and don'ts

Do not use the side sheet to display a notification message to the user or ask for confirmation. Use an alert dialog or modal instead.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Side%20Sheet](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Side%20Sheet)
