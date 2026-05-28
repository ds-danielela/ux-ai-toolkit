# Search

A search field lets users quickly find relevant content.

---
title: Search
url: https://zeroheight.com/0b922d40b/v/latest/p/36c5ff-search
introduction: A search field lets users quickly find relevant content.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Search field: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0b09178dbfaceda9013c8d)

**Search field: Preview**

---

## Design spec

![Search: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b3a8b24f4d68ba5d7bd8eb)

**Search: Design spec**

### Size and scaling

The width of the search field depends on its parent container, while the height remains fixed. For search fields with suggestions, the height of the result list varies based on available space. On large screens, display 6 full items plus a partially visible 7th; on small screens, display 3 full items plus a partially visible 4th. The result list appears above any content positioned below it and uses a higher stacking order.

---

## Anatomy

The search field consists of:

1. Magnifying glass icon
2. Placeholder / input text
3. An icon to reset (appears on the right after the user has entered something)

The search field with suggestions additionally consists of:

4. Result list items, with optional sublabels
5. Lazy-loading indicator (if applicable)
6. Scrollbar (if applicable)
7. Hint area, used to provide additional information when no results are found or while results are loading

---

## Usage

Use the search field to help users quickly find relevant content.

It functions as a filter, narrowing large datasets to specific results. The search is triggered as soon as the user starts typing, dynamically removing items that don't match the given criteria. After a search is initiated, a reset icon appears. The search field can be placed within the universal action bar above a table or container.

The search can also be displayed above an option list, e.g. within a dropdown.

### No search results

Use the empty state if no items match the given criteria.

If using search field with suggestions, display the appropriate status message instead of query results.

### Suggestions list loading states

When using a suggestion list, display "Loading results" with an indeterminate progress indicator while data is being fetched.

Use lazy loading when the list of results is too long to display at once, and additional items need to be retrieved dynamically.

### Do's and don'ts

Always provide a placeholder text when the search field is empty.

Do not use a search field on a small set of data.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Search%20Field](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Search%20Field)
