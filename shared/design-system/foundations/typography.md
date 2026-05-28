# Typography

## Typeface

DS CORE uses the typeface **Be Vietnam Pro**, available on [Google Fonts](https://fonts.google.com/specimen/Be+Vietnam+Pro).

For languages that require special characters not covered by Be Vietnam Pro, **Noto Sans** is used as a fallback.

---

## Typography Decision Tokens

Typography tokens are a composition of individual typography properties: font size, line height, font weight, and letter spacing. A range of styles covers different purposes across the UI.

> **Note:** For responsive layout S, the "Small" token values apply. See *Responsive Spacing and Typography* for details.

| Token | Size (Default / Small) | Line-height | Font weight | Letter spacing | Usage |
|---|---|---|---|---|---|
| `Text.heading5xl` | 64px / 48px | 72px / 56px | SemiBold | -2.5% | Landing pages |
| `Text.heading4xl` | 48px / 32px | 56px / 40px | SemiBold | -2.5% | Landing pages |
| `Text.heading3xl` | 32px / 24px | 40px / 32px | SemiBold | -2.5% | Page header |
| `Text.heading2xl` | 24px / 20px | 32px | SemiBold | -2.5% | Headline in modals, side sheets, ... |
| `Text.headingXl` | 20px / 16px | 28px / 24px | SemiBold | -2.5% | Section headline |
| `Text.headingBase` | 16px / 14px | 24px | SemiBold | -2.5% | Subsection headline |
| `Text.textLg` | 18px / 16px | 28px / 24px | Regular | -2.5% | Landing page text |
| `Text.textLgStrong` | 18px / 16px | 28px / 24px | SemiBold | -2.5% | — |
| `Text.textBase` | 16px / 14px | 24px | Regular | -2.5% | Base text size |
| `Text.textBaseStrong` | 16px / 14px | 24px | SemiBold | -2.5% | Headline in cards, notifications, ... |
| `Text.textSm` | 14px / 12px | 20px | Regular | -2.5% | Help and validation text on form fields, list item body |
| `Text.textSmStrong` | 14px / 12px | 20px | SemiBold | -2.5% | — |
| `Text.textXs` | 12px / 10px | 16px | Regular | -2.5% | Small tags |
| `Text.textXsStrong` | 12px / 10px | 16px | SemiBold | -2.5% | Small avatar |
| `Text.textAction` | 14px | 24px | SemiBold | -2.5% | Buttons |

---

## Usage

### Using Typography in Figma

All typography tokens are provided as **Figma text styles**, composed of individual Figma variables. Since font size varies depending on the responsive layout, text styles respond automatically to the mode switch.

See *Responsive Spacing and Typography* for details on mode switching.

---

## Dos and Don'ts

### ✅ Do — Pair font styles with a valid text color token

Always combine a typography token with a valid color token from the text palette (e.g. `Text.Standard`, `Text.Subdued`, `Text.Disabled`, `Text.Critical`).

### ❌ Don't — Apply typography without a color token

Do not use raw color values or leave text unstyled. All text must use a defined text color token to ensure consistency across themes.
