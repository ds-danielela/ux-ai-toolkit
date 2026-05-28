# Radius

Rounded corners provide a friendlier look to an application. A set of border radius tokens enables a harmonious and consistent shape of UI elements.

---

## Border Radius Tokens

| Token | Radius | Usage |
|---|---|---|
| `Border.Radius.Pill` | 999px | Tags, etc. |
| `Border.Radius.Large` | 16px | Larger components such as containers, modal dialogs, etc. |
| `Border.Radius.Standard` | 12px | Standard border radius for buttons, form fields, etc. |
| `Border.Radius.Medium` | 8px | Inner part of segmented control |
| `Border.Radius.Small` | 4px | Small components such as checkboxes, etc. |
| `Border.Radius.Sharp` | 0px | Elements that should not have rounded corners |

---

## Usage

Rounded corners typically feel more friendly and accessible, while sharp edges appear more formal and structured.

### Applying Border Radius in Figma

All border radius tokens are provided as Figma variables and can be applied to the **corner radius** property.

While most tokens are generic, component-specific radius tokens such as `Border.Radius.Side Sheet` respond to the mode switch. See *Responsive Spacing and Typography* for details.

---

## Dos and Don'ts

### ✅ Do — Reflect hierarchy when nesting elements

When nesting elements inside one another, use a slightly smaller radius for the child element to visually reflect the containment hierarchy.

### ❌ Don't — Use the same radius for parent and child

Applying identical radii to both a container and its inner element flattens the visual hierarchy and makes nesting unclear.
