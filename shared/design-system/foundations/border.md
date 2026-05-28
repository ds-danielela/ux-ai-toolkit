# Border

Borders outline UI elements. Depending on the interaction state, border thickness and color can vary.

---

## Border Width Tokens

| Token | Width | Usage |
|---|---|---|
| `Border.Width.Standard` | 1px | Standard border for buttons, form fields, etc. |
| `Border.Width.Dropzone` | 2px | Highlights components that accept file drops on hover, e.g. media tile |
| `Border.Width.Critical` | 2px | Form fields in validation state |
| `Border.Width.Focus` | 2px | Focus state of interactive components such as buttons, form fields, etc. |
| `Border.Width.Interactive` | 2px | Progress circle and small interactive components such as checkboxes, radio buttons, etc. |
| `Border.Width.Interactive Large` | 2px | Progress circle filled |
| `Border.Width.Selection` | 2px | — |
| `Border.Width.Annotation Light` | 2px | Light annotation in Canvas |
| `Border.Width.Annotation Medium` | 4px | Medium annotation in Canvas |
| `Border.Width.Annotation Bold` | 8px | Bold annotation in Canvas |

---

## Usage

The style of a border is defined by a combination of three tokens:

- **Corner radius** — see *Radius*
- **Border color** — see *Color*
- **Border width** — defined by the tokens above

### Applying Border Width Tokens in Figma

All border width tokens are provided as Figma variables and can be applied to the **stroke weight** property.

---

## Dos and Don'ts

### ✅ Do — Match border tokens with their counterparts

Always combine border width and border color tokens that correspond to the same state. For example, pair `Border.Focused` (color) with `Border.Width.Focus` (width).

### ❌ Don't — Mix tokens from different states

Do not combine tokens from mismatched states, e.g. do not use `Border.Focused` (color) with `Border.Width.Critical` (width).
