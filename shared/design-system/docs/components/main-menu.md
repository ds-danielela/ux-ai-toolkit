# Main menu

---
title: Main menu
url: https://zeroheight.com/0b922d40b/v/latest/p/813a83-main-menu
introduction: The main menu allows the user to switch between the top level pages of the application.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Main menu: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/bfadb00e8f94d509e7cff8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133113Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=dd2a4aecf713ced64115363e8a7bcf709745643271c55eb3cc50c6f39464d3d0)

**Main menu: Preview**

---

## Design spec

![Main menu: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/af13ac6c88e39161c795e2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133113Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=aa209652cdab873ab8f49d2c28030c2ce23aeea1599fe2c8e2d51f63de5cb84f)

**Main menu: Design spec**

---

### Size and scaling

The size of the main menu depends on the responsive layout. 

Responsive layout L - XL: The menu has a fixed width of 256 px when expanded and 72 px when collapsed. The height stretches to the page height.

Responsive layout S - M: The menu has a fixed width of 256 px when shown. The height stretches to the page height.

---

## Anatomy

The main menu contains the following elements:

1. Icon button with burger icon to show/expand or hide/collapse the main menu. 
2. Logo
3. Menu items

---

## Usage

Use the main menu in top and second level pages. 

**Please note:** Corresponding layout templates already contain a main menu.

Depending on the viewport, the behavior / visibility of the main menu is slightly different. 

### Responsive layout L and XL

For responsive layout L and XL, the main menu is displayed at the left side of the screen. It can be collapsed by clicking on the burger icon button. In the collapsed state, the items are limited to the icon only. In the collapsed state, the menu is fully functional: Clicking on a menu item opens the corresponding page. Clicking on the burger icon button collapses the main menu again.

### Responsive layout S and M

For responsive layout S and M the main menu is initially not visible. By clicking on the burger icon button, the main menu is displayed as an overlay and covers the content below. The main menu is closed again when the user selects an item, clicks on the burger icon button or on the area outside the menu.

### Content guidelines

* Always use clear and concise labels for the menu items. 

### Do's and don'ts

Use icons for all top level menu items. 

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Templates/Scrollable%20Page%20With%20Main%20Menu](https://storybook-coreui-d2-euw3.d.dscore.com/#/Templates/Scrollable%20Page%20With%20Main%20Menu)
