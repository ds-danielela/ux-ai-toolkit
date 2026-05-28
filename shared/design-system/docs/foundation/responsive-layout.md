# Responsive layout

> Source: https://zeroheight.com/0b922d40b/v/latest/p/30f818-responsive-layout
> Introduction: The responsive layout ensures a consistent and appropriate display across different screen sizes and orientations.

---

## Responsive layouts

| Layout name | Resolution | Columns | Gutter (px) | Margin (px) | Column sizing behavior |
| --- | --- | --- | --- | --- | --- |
| **Responsive layout XL** | > 1600px | 12 | 24 | 48 | Stretch to a maximum of 1752 pixels |
| **Responsive layout L** | 1240 - 1599px | 12 | 24 | 48 | Stretch |
| **Responsive layout M** | 840 - 1239px | 12 | 24 | 24 | Stretch |
| **Responsive layout S** | < 840px | 4 | 16 | 16 | Stretch |

---

## Anatomy

The layout consists of several **columns**. The number and width of the columns depends on the respective screen size.

**Gutters** are the gaps between the columns and help separating the content.

The **margin** specifies the outer margin of the layout, thus the space between the columns and the left and right edge of the screen.

---

## Usage

It is recommended to consider all responsive layouts when designing.

* UI components and content should be positioned among the columns.
* Components can span multiple columns.
* The gutter should be used to separate UI components / UI regions.

**Please note:** Some components, like main menu and table, are provided with different variations for different responsive layouts.

### Very large screens

In general, the width of the columns is fluid and scales according to the resolution. For very large screens (if the content width >= 1752px) the content has a fixed width and will be displayed centered.

**Applying layout grids in Figma**

All available responsive layouts are provided as Figma grid styles. Their visibility can be toggled by pressing "Shift + G".

**Please note:** All layout templates already contain the respective layout grid.

### Do's and don'ts

Consider all responsive layouts when designing.

- **Do**: Use the component variation that has been designed for the respective responsive layout.
- **Don't**: Mix component variations intended for different responsive layouts.

---

## Live Preview

[Explore responsive layout in Storybook Flutter](https://storybook-coreui-d2-euw3.d.dscore.com/#/Foundation/Responsive%20Body)
