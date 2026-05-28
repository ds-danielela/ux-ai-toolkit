# Color Guidelines

---

## Color Palette

Both color themes are derived from the general color palette.

The color palette is composed of two primary colors — **dsBlue** and **dsChartreuse** — plus **dsNeutralGray** and the semantic colors **dsGreen**, **dsRed**, **dsOrange**, and **dsPetrol**.

### Neutrals

#### dsNeutralGray

| Token | Value |
|---|---|
| dsNeutralGray/50 | `#F5F5F5` |
| dsNeutralGray/100 | `#EBEBEB` |
| dsNeutralGray/200 | `#D7D7D7` |
| dsNeutralGray/300 | `#BDBDBD` |
| dsNeutralGray/400 | `#A4A4A4` |
| dsNeutralGray/500 | `#8A8A8A` |
| dsNeutralGray/600 | `#717171` |
| dsNeutralGray/700 | `#575757` |
| dsNeutralGray/800 | `#313131` |
| dsNeutralGray/900 | `#242424` |
| dsNeutralGray/950 | `#121212` |

#### dsWhite / dsBlack

| Token | Value |
|---|---|
| dsWhite | `#FFFFFF` |
| dsBlack | `#000000` |

---

### Branding

#### dsBlue

| Token | Value |
|---|---|
| dsBlue/50 | `#E6EEFF` |
| dsBlue/100 | `#D1E1FF` |
| dsBlue/200 | `#9EC0FF` |
| dsBlue/300 | `#71A2FE` |
| dsBlue/400 | `#3E81FE` |
| dsBlue/500 | `#0F62FE` |
| dsBlue/600 | `#014BD5` |
| dsBlue/700 | `#0139A3` |
| dsBlue/800 | `#00266B` |
| dsBlue/900 | `#001438` |

#### dsChartreuse

| Token | Value |
|---|---|
| dsChartreuse/50 | `#FDFFF0` |
| dsChartreuse/100 | `#FBFFDB` |
| dsChartreuse/200 | `#F7FFB8` |
| dsChartreuse/300 | `#F3FF99` |
| dsChartreuse/400 | `#EFFF75` |
| dsChartreuse/500 | `#EBFF51` |
| dsChartreuse/600 | `#E3FF0F` |
| dsChartreuse/700 | `#B4CC00` |
| dsChartreuse/800 | `#758500` |
| dsChartreuse/900 | `#3B4200` |

---

### Semantic

#### dsGreen

| Token | Value |
|---|---|
| dsGreen/50 | `#ECF9F2` |
| dsGreen/100 | `#D5F1E2` |
| dsGreen/200 | `#AFE4C8` |
| dsGreen/300 | `#84D6AB` |
| dsGreen/400 | `#5AC88E` |
| dsGreen/500 | `#3BB273` |
| dsGreen/600 | `#2F8E5B` |
| dsGreen/700 | `#246B45` |
| dsGreen/800 | `#18492F` |
| dsGreen/900 | `#0B2216` |

#### dsRed

| Token | Value |
|---|---|
| dsRed/50 | `#FDE7EA` |
| dsRed/100 | `#FCD4D9` |
| dsRed/200 | `#F8A5AE` |
| dsRed/300 | `#F57A88` |
| dsRed/400 | `#F2505F` |
| dsRed/500 | `#EF233C` |
| dsRed/600 | `#CC0F25` |
| dsRed/700 | `#980B1C` |
| dsRed/800 | `#640712` |
| dsRed/900 | `#340409` |

#### dsOrange

| Token | Value |
|---|---|
| dsOrange/50 | `#FEF5EC` |
| dsOrange/100 | `#FCEBD9` |
| dsOrange/200 | `#F9D7B3` |
| dsOrange/300 | `#F7C48D` |
| dsOrange/400 | `#F4B067` |
| dsOrange/500 | `#F19A3E` |
| dsOrange/600 | `#E47E11` |
| dsOrange/700 | `#A75C0C` |
| dsOrange/800 | `#723F08` |
| dsOrange/900 | `#391F04` |

#### dsPetrol

| Token | Value |
|---|---|
| dsPetrol/50 | `#EAF5FA` |
| dsPetrol/100 | `#D5EBF6` |
| dsPetrol/200 | `#A8D5EB` |
| dsPetrol/300 | `#7EC1E2` |
| dsPetrol/400 | `#50AAD8` |
| dsPetrol/500 | `#2D94C8` |
| dsPetrol/600 | `#24759E` |
| dsPetrol/700 | `#1B5A79` |
| dsPetrol/800 | `#123B4F` |
| dsPetrol/900 | `#091F2A` |

---

### Chart

| Token | Value |
|---|---|
| dsBrandDarkPink | `#FF56FF` |
| dsBrandDarkOrange | `#FFA702` |
| dsBrandDarkChartreuse | `#CFEA00` |
| dsBrandLightBlue01 | `#8EDDFF` |
| dsBrandLightGreen01 | `#00B1AF` |
| dsBrandLavender01 | `#9253FF` |

---

## Color Decision Tokens

For each theme there is a set of color decision tokens. These refer to the global color palette and provide semantic meaning to the colors.

Both themes contain the same color decision tokens, but with different palette color values assigned.

### Token Naming Pattern

The color token naming pattern references three parts:

```
Action Primary.Hovered
└─────┘ └─────┘ └──────┘
UI element  Color role  Interaction state
```

- **UI element** — the component or layer the color applies to (e.g. `Action`, `Surface`, `Text`, `Icon`, `Border`)
- **Color role** — the semantic role within that element (e.g. `Primary`, `Standard`, `Critical`)
- **Interaction state** — the user interaction state (e.g. `Standard`, `Hovered`, `Pressed`, `Disabled`)

---

## Fill Color: Background and Surface

Each theme has a standard background color. Components placed on the background — such as cards, containers, drawers, etc. — use the surface color.

| Token | Usage |
|---|---|
| `Background.Standard` | Page-level background |
| `Surface.Standard` | Cards, containers, drawers placed on the background |

### Interactive Surfaces

Use the surface interactive colors for selected interactive states — i.e. tabs, checkboxes, etc.

| Token | Usage |
|---|---|
| `Surface.Interactive.Standard` | Default selected/active state |
| `Surface.Interactive.Hovered` | Hovered selected state |
| `Surface.Interactive.Pressed` | Pressed selected state |
| `Surface.Interactive.Disabled` | Disabled selected state |
| `Border.Interactive` | Interactive border, e.g. focus rings on interactive elements |

### Selected Surfaces

The selected state indicates option list items, cards, etc. that are chosen by the user or by the system.

| Token | Usage |
|---|---|
| `Surface.Selected.Standard` | Default selected state |
| `Surface.Selected.Hovered` | Hovered selected state |
| `Surface.Selected.Pressed` | Pressed selected state |
| `Surface.Selected.Disabled` | Disabled selected state |

---

## Actions

The color tokens `Action` are intended for buttons in their respective variants and states.

| Variant | Token | Usage |
|---|---|---|
| Primary | `Action.Primary.Standard` | Primary CTA buttons |
| Secondary | `Action.Secondary.Standard` | Secondary buttons |
| Destructive | `Action.Destructive.Standard` | Delete / destructive action buttons |

---

## Foreground Colors: Text, Icon and Border

Foreground colors are used for text, icons, and borders. A subdued variant is available to create visual hierarchy.

| Token | Usage |
|---|---|
| `Text.Standard` | Default body and label text |
| `Text.Subdued` | Supporting, secondary, or placeholder text |
| `Border.Standard` | Default borders on containers and dividers |

---

## Semantic Colors

Depending on the type of component, different strategies are used to express status via color.

### Semantic Tags
Semantic tags are indicated with a colored background.

| Token | Usage |
|---|---|
| `Surface.Critical` | Background for critical status tags |
| `Surface.Warning` | Background for warning status tags |
| `Surface.Success` | Background for success status tags |
| `Surface.Information` | Background for information status tags |

### Feedback Components
For feedback components like notifications and banners, the status is displayed using a colored icon, border, and background.

| Token | Usage |
|---|---|
| `Icon.Critical`, `Icon.Warning`, `Icon.Success`, `Icon.Information` | Semantic icon color |
| `Border.Critical`, `Border.Warning`, `Border.Success`, `Border.Information` | Semantic border color |
| `Surface.Critical` (subdued), `Surface.Warning` (subdued), ... | Subdued background for banners and notifications |

### Semantic Text
Semantic color for text should only be used for the **critical** status — i.e. for validation of input fields.

| Token | Usage |
|---|---|
| `Text.Critical` | Validation error messages, critical inline text only |

---

## Interaction States

When a user interacts with a component, the appearance changes slightly.

| State | Behaviour |
|---|---|
| **Hovered** | Subtle background color change |
| **Pressed** | Slightly stronger background color change |
| **Focused** | Additional 2px outline using `Border.Focused` |

| Token | Usage |
|---|---|
| `Action.Secondary.Standard` | Default resting state |
| `Action.Secondary.Hovered` | On hover |
| `Action.Secondary.Pressed` | On press/click |
| `Border.Focused` | 2px focus outline on keyboard navigation |

---

## Usage in Figma

All color tokens are provided as **Figma variables** and can be applied as **Fill**.

> **Note:** Variables are scoped. Text colors can only be assigned to the fill of text layers. Border colors can only be assigned to borders.

### Theme Switch / Modes

The light theme is activated by default. To switch to the dark theme, set the mode to **Dark**. This can be done for:

- A whole page
- Specific frames
- Individual layers

This is done by clicking the mode icon in Figma. See the [Figma help page](https://help.figma.com) for more on modes.

---

## Dos and Don'ts

### ✅ Do — Use color decision tokens

Always use color decision tokens in design and development. They simplify applying color in a consistent, reusable, and scalable way.

```
✅ Action.Primary.Standard
```

### ❌ Don't — Use raw palette values directly

Never use colors directly from the global color palette in components or code.

```
❌ Primitives.Palette.dsBlue500
```

### ✅ Do — Use colors according to their intended purpose

Apply each token only for its defined role (e.g. use `Text.Critical` for error messages, not for decorative text).

### ❌ Don't — Use colors outside their intended purpose

Do not repurpose tokens for visual effects that differ from their semantic meaning (e.g. do not use `Surface.Critical` for a non-error highlighted card).
