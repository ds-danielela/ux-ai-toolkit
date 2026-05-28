# Responsive Spacing and Typography

To ensure a balanced and efficient layout across all responsive layouts, layout spacings and typography adapt to the screen size.

---

## Token Structure

Numerical variables are provided for two modes to achieve adaptation of layout spacings and text styles for responsive layout S:

| Mode | Applies to |
|---|---|
| **Not small** | All responsive layouts M – XL |
| **Small** | Responsive layout S only |

In most cases, Small mode values are smaller since less space is available.

### Layout Spacing Values

| Token | Not small | Small |
|---|---|---|
| `Spacing.Layout.XS` | 8px | 6px |
| `Spacing.Layout.S` | 16px | 12px |
| `Spacing.Layout.M` | 24px | 16px |
| `Spacing.Layout.L` | 48px | 24px |
| `Spacing.Layout.XL` | 80px | 48px |

### Typography Values

For text styles, only the font size is adjusted in Small mode — the line height remains the same. This is because many component sizes are determined by line height. Headlines that align with a button (e.g. in a modal dialog) also keep the same line height.

| Token | Not small | Small |
|---|---|---|
| `Text.heading5xl` | 64px | 48px |
| `Text.heading4xl` | 48px | 32px |
| `Text.heading3xl` | 32px | 24px |
| `Text.heading2xl` | 24px | 20px |
| `Text.headingXl` | 20px | 16px |
| `Text.headingBase` | 16px | 14px |
| `Text.textLg` | 18px | 16px |

---

## Usage

### Usage in Figma

The **Not small** mode is activated by default. To switch to Small mode, set **Number-Tokens** to **Small**. This can be done for:

- A whole page
- Specific frames
- Individual layers

This is done by clicking the mode icon in Figma.

> **Note:** Layout templates and dedicated components for responsive layout S are already provided with Small mode activated.

> **Note:** When selecting a text layer with a text style, Figma only displays the font size and line height values for the default (Not small) mode regardless of which mode is active. Mode-specific values can be verified using **Dev Mode**.

### Usage in Flutter

`DSTokens.forFormFactor()` automatically changes the token set based on the `themeType` and `formFactor`. Since `DSTokens.forFormFactor()` is already used by `DSTheme`, this change will likely happen automatically.

---

## Dos and Don'ts

### ✅ Do — Use Small mode only for responsive layout S

Apply the Small mode and dedicated component variations exclusively when designing for responsive layout S.

### ❌ Don't — Apply Small mode to larger layouts

Do not use Small mode tokens or component variations for layouts M and above, as this will result in insufficient spacing and reduced readability.
