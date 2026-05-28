# Empty state

---
title: Empty state
url: https://zeroheight.com/0b922d40b/v/latest/p/02a0dc-empty-state
introduction: The empty state informs the user that there is no data to display and provides guidance on what to do next.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Empty state: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/02665b49c44682be87c6f2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133105Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=2246ca24a4e74111fe94cacd5e6e72d8c5691a0597799fdabf654044833549e2)

**Empty state: Preview**

---

## Design spec

![Empty state: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b9554df286adfa39d7d1b8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133105Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=f7b57f95fc5229bcff241a0abd51c0978a89551983d0396bdcc6e62a33964c0c)

**Empty state: Design spec**

---

### Size and scaling

The width of the empty state stretches to the width of its parent container (typically either a container or a blank page). The width of the text must not exceed 960 px (approximately 60 characters) to ensure readability. The height of the empty state usually depends on the content but can also be stretched to the parent container.

---

## Anatomy

An empty state contains the following elements:

1. Illustration (optional)
2. Headline
3. Body
4. One or more action(s) (optional)

---

## Usage

Use the empty state when:

* a page, section, or container contains no content
* content is not yet available or configured
* a search or filter returns no results
* content cannot be shown due to errors, permissions, or limitations

An empty state can be displayed:

* as a large empty state (page-level or major section)
* as a small empty state (within a component, container, or subsection)

### Empty state types

| **Type** | **Typical use case** | **Primary intent** | **Action behavior** |
| --- | --- | --- | --- |
| Empty content | First use, no data yet | Help users get started | Primary action allowed only if no other primary action exists on the screen |
| No results | Search or filters return no matches | Help users recover | Avoid primary actions, guidance only |
| Error / unsupported | Content cannot be displayed | Explain the limitation | Actions used sparingly |
| Cleared / completed | User completed or removed all items | Acknowledge completion | No primary action |

### Empty state sizes

Empty states are available in small and large variants. The size is determined by layout context, not by the empty state type.

**Large empty state** — Use when an entire page or major content area is empty, or the empty state is the primary focus of the screen.

**Small empty state** — Use when only part of the interface is empty, or content is embedded in a larger screen (tables, containers, side sheets).

### Actions and hierarchy

* Actions in empty states must follow the global action hierarchy (primary, secondary, tertiary).
* Only one primary action is allowed per screen, regardless of where it appears.
* Primary actions should remain in a stable and predictable location (for example: toolbar or page header).
* Empty states must not compete with or duplicate existing actions on the screen.

### Content guidelines

**Headline**
* Use sentence case
* Keep it short and specific
* Do not end headlines with a period
* Clearly describe the state or the next step

**Body text**
* Explain why the state is empty
* Help users understand what happens next
* Avoid technical jargon
* Keep it concise (1–2 sentences)

**Action labels**
* Use clear, verb-based labels (Create order, Upload file)
* Labels must reflect the actual outcome of the action
* Avoid generic labels (OK, Continue)

**Illustrations**
* Illustrations are optional
* Use approved empty state illustrations only
* Do not use icons, screenshots, or product imagery
* Illustrations are decorative and must not communicate essential information

### Do's and don'ts

Write in sentence case.

Only use illustrations within empty state. Do not use icons or images.

Provide coherent and solution-oriented messages. Avoid technical jargon.

Empty states must not compete with or duplicate existing actions on the screen. Only one primary action is allowed per screen.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Empty%20state](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Empty%20state)
