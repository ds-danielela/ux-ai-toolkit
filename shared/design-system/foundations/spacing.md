# Spacing

A set of defined spacing tokens enables consistent and harmonious spacing within components and layouts.

---

## Layout Spacings

Used to separate components within a building block or a page layout.

> **Note:** For responsive layout S, layout spacing values differ. See *Responsive Spacing and Typography* for details.

| Token | Size (Default / Small) | Usage |
|---|---|---|
| `Spacing.Layout.XL` | 80px / 48px | Very large distinction between sections |
| `Spacing.Layout.L` | 48px / 24px | Vertical spacing between different sections on a page, e.g. containers |
| `Spacing.Layout.M` | 24px / 16px | Spacing between form columns and rows; spacing between components; inner spacing of spacious cards, containers, modals; horizontal spacing between different subsections on a page |
| `Spacing.Layout.S` | 16px / 12px | Reduced spacing between components; spacing within compact cards and media tiles |
| `Spacing.Layout.XS` | 8px | Inner vertical spacing above page headline; spacing between very closely related components, e.g. buttons in a toolbar |

---

## Component Spacings

Used for spacings within a component.

| Token | Size | Usage |
|---|---|---|
| `Spacing.Component.XL` | 48px | Horizontal inner padding for top bar |
| `Spacing.Component.L` | 24px | — |
| `Spacing.Component.M` | 16px | Spacing between headline and individual content (accordions, cards, ...); horizontal inner spacing for buttons, text fields, etc. |
| `Spacing.Component.S` | 12px | Horizontal inner spacing within main menu items and vertical tabs |
| `Spacing.Component.XS` | 8px | Horizontal spacing between text and icon within buttons, optional list items, etc.; vertical padding for buttons, text fields, etc. |
| `Spacing.Component.XXS` | 4px | Spacing between dropdown field and menu; outer spacing around tooltip; inner vertical spacing within very small components such as tooltip and slider value flag |

---

## Usage

Use **component spacings** for spacings within a component. Use **layout spacings** to separate components within a building block or a page layout.

### Using Spacings in Figma

Since layout spacing values vary depending on the responsive layout, spacings respond automatically to the mode switch. See *Responsive Spacing and Typography* for details.

There are two ways to apply spacing tokens in Figma:

**As variables in auto layouts** — when placing components at a consistent distance (e.g. in a form layout), apply spacing variables directly in the auto layout gap and padding fields.

**As spacing components** — all spacing tokens are also available as Figma components. Use these when building complex layouts with multiple different spacings to clearly communicate screen hierarchy during handoff.

> **Note:** Spacing components can be visually hidden using the **Hide** property while still occupying space. However, it is recommended to keep spacings visible when handing screens off to development.

---

## Dos and Don'ts

### ✅ Do — Stick to provided spacing tokens

Always use the defined spacing tokens. They ensure visual consistency and respond correctly to responsive mode changes.

### ❌ Don't — Introduce custom spacing values

Do not create custom spacing values that approximate an existing token. Always use the nearest defined token instead.
