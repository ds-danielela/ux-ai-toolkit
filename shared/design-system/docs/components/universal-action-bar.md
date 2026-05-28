# Universal action bar

The universal action bar can be used to group functionality above a table or container.

---
title: Universal action bar
url: https://zeroheight.com/0b922d40b/v/latest/p/983afa-universal-action-bar
introduction: The universal action bar can be used to group functionality above a table or container.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ⚪️ |

![Universal action bar: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b0a61c3512a09dbc5a30a0)

**Universal action bar: Preview**

---

## Design spec

![Universal action bar: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7fd5d131be9e61261bcf1a)

**Universal action bar: Design spec**

### Size and scaling

The universal action bar stretches to the available width provided by the parent container. The height of the universal action bar depends on its content.

---

## Anatomy

The universal action bar contains an optional search field at the left (1). Furthermore it contains one or more actions at the right (2). There can also be optional filters and sorting options (3).

On responsive layout S, those are combined in one icon button (4).

---

## Usage

Use a universal action bar to provide functionality such as search, sorting and filtering as well as actions above a table or container.

**Please note:** Corresponding layout templates already contain a universal action bar.

The action buttons at the right of the universal action bar can vary depending on the selection in the container below. Once one or more items are selected, the actions are replaced by actions that can be applied to the selection.

### Overflow behavior

For responsive layout S, the sort and filter options are combined in an icon button that opens an option list.

Similar to the page header, only one action button (next to filtering and sorting) should be displayed for responsive layout S. This button can optionally open an option list containing all possible actions.

### Do's and don'ts

Respond to the selection in the container below and only show actions that can be applied to the selection.

Don't overcrowd the universal action bar with too many actions.
