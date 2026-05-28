# Table

Tables are used for displaying information divided into multiple rows and columns. They allow users to quickly scan, compare or also manipulate large amounts of data.

---
title: Table
url: https://zeroheight.com/0b922d40b/v/latest/p/64dd20-table
introduction: Tables are used for displaying information divided into multiple rows and columns. They allow users to quickly scan, compare or also manipulate large amounts of data.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Table: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f345abc7b6115a9fb4cf02)

**Table: Preview**

---

## Design spec

![Table: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/59aef55eae1b01b10cdee9)

**Table: Design spec**

### Size and scaling

The table width depends on the container that wraps it. The height usually depends on the table content but can also be defined on the parent container.

The table cells stretch to the available width. The height of the table cells depends on their content. The content of table cells can wrap to a maximum of three lines.

---

## Anatomy

The table is wrapped in a container (1) and contains several table rows (2). For responsive layout M - XL, one header row is displayed at the top of the table (3). Each table row contains a divider line (4) at the bottom (excluding the last row).

For responsive layout S, there are different layout options:

1. Portrait
2. Landscape

The user can switch the layout option with an icon button above the table (3).

---

## Usage

Use a table to allow users to quickly scan, compare or also manipulate large amounts of data.

### Sorting

The table is initially always sorted by one column. The user can adjust the sorting by clicking on another column header. Clicking once on a column header leads to descending sorting. Clicking once again, the sorting sequence changes to ascending. Only one column can be sorted at a time.

### Scrolling

Responsive layout M-XL: When the application layout requires the table to scroll vertically, the header row remains sticky with the table rows moving underneath as the user scrolls down. Horizontal scrolling should be avoided if possible.

Responsive layout S - Landscape: The header row remains sticky with the table rows moving underneath as the user scrolls down. When scrolling horizontally, the first column also remains sticky.

Responsive layout S - Portrait: The whole table container is scrollable when the application layout requires the table to scroll vertically.

### Cell alignment

Columns can be either left-aligned or right-aligned. Column headers should always align to their corresponding content.

| Alignment | Usage |
| --- | --- |
| Left | Use left-alignment for text and qualitative numbers, including phone numbers, dates, IDs and postal codes. |
| Right | Use right alignment for quantitative numbers including money, quantities, measures, and percentages. |

### Truncation

The content of table cells can wrap to a maximum of three lines. After that, truncation with an ellipsis is applied. A tooltip shows the whole text.

### Interaction

By default, clicking on the whole table row navigates to another screen, like the details screen for the corresponding object.

#### Single-selection

If single-selection should be possible in a table, radio buttons are displayed in the first column. Clicking on the whole table row changes the selection to the corresponding table row.

#### Multi-selection

If multi-selection should be possible in a table, checkboxes are displayed in the first column. The checkbox in the header checks or unchecks all items. Clicking on the whole table row selects or deselects the corresponding table row.

### Skeleton state

The table component is skeletonized by displaying a simplified grid structure that mirrors its rows and columns. Each cell is represented by a pill- or circle-shaped skeleton. Interactive elements such as buttons and checkboxes are omitted.

### Content guidelines

* Keep the column headers short and specific.
* Include units of measurement symbols in the table header cells so they aren't repeated throughout every single column.

### Do's and don'ts

Write in sentence case.

If there are no entries in a table, display the empty state instead of a table with no rows.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Table](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Table)

---

## Hints for designers

**Resp. layout S - Landscape layout**

Please note: To manage the content of the columns that are initially not visible, temporarily uncheck "Clip content" on the layer "Columns". As this variation is built on a column based approach, interactive states for the rows are not provided.
