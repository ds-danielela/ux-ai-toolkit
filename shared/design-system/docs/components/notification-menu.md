# Notification menu

The notification menu collects cross-system messages.

---
title: Notification menu
url: https://zeroheight.com/0b922d40b/v/latest/p/697f1e-notification-menu
introduction: The notification menu collects cross-system messages.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Notification menu: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/bf6d3487d9cebef33021ed)

**Notification menu: Preview**

---

## Design spec

![Notification menu: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1b5a075aebabd3929c836f)

**Notification menu: Design spec**

### Size and scaling

See [side sheet](https://zeroheight.com/0b922d40b/p/7675c3).

---

## Anatomy

The notification menu contains the following elements:

1. Side sheet
2. Actions
3. Notifications

If there are no notifications, the empty state is displayed (4).

![Notification menu: Anatomy](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ba41c748a86da7831e05da)

**Notification menu: Anatomy**

---

Individual notifications contain the following elements:

1. Icon indicating the notification type
2. Headline
3. Body
4. Timestamp
5. Actions
6. Divider line at the bottom (excluding the last item)

![Notification menu: Anatomy items](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c44010f32c50d0775fd119)

**Notification menu: Anatomy items**

---

## Usage

The notification menu is displayed at the right edge of the screen within a side sheet and covers the content below. It appears if the user clicks on the notification button in the top bar. The notification menu closes by clicking on the close button or by clicking somewhere outside the notification menu.

All messages that appear as toasts are listed in the notification menu as individual notifications. The notifications are sorted by timestamp. New notifications are added on top.

The notification button in the top bar, that opens the notification menu can be combined with a notification badge. The notification badge represents the type of the most severe notification.

The option list of the notifications contains all actions that were available in the corresponding toast. Furthermore, the option to dismiss individual notifications should be provided. If the user chooses "Dismiss", the notification is removed from the list. If the user chooses another action (i.e. Show order), the notification menu is closed and the user is taken to the corresponding screen.

The notification itself can also be clickable. "Dismiss all" will remove all notifications within the notification menu.

### Do's and don'ts

The type and content of individual notifications should match the corresponding toast.

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Do | (image) |   |   |
| Don't | (image) |   |   |

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Notification%20Menu](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Notification%20Menu)
