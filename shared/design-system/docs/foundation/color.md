# Color

> Source: https://zeroheight.com/0b922d40b/v/latest/p/847b05-color
> Introduction: The DS Design System with two themes: light and dark. The default theme is the light theme.

---

## Color palette

Both color themes are derived from the general color palette. The color palette is composed of the two primary colors **dsBlue** and **dsChartreuse**, **dsNeutralGray** and the semantic colors **dsGreen**, **dsRed**, **dsOrange** and **dsPetrol**.

---

## Color decision tokens

For each theme there is a set of color decision tokens. These refer to the global color palette and provide semantic meaning to the colors. Both themes contain the same color decision tokens, but with different palette color values assigned.

The color tokens naming pattern references the UI elements the color refers to, the color role and the corresponding interaction state.

### Fill colors: Background and surface

Each theme has a standard background color. Components that are placed on the background such as cards, containers, drawers etc. use the surface color.

### Interactive

Use the surface interactive colors for selected interactive states, i.e. for tabs, checkboxes, etc.

### Actions

The color tokens "Action" are intended for buttons in the respective variants and states.

### Foreground colors: Text, icon and border

Foreground colors are used for text, icon and borders. To create visual hierarchy, a subdued variant is available.

### Semantic colors

Depending on the type of component, different strategies are used to express the status via colors.

* Semantic tags are indicated with a colored background.
* For feedback components like notifications, banners, etc. the status is displayed using a colored icon, border and background.
* Semantic color for text should only be used for the status "critical", i.e. for validation of input fields.

### Interaction states

If the user interacts with a component, the appearance slightly changes. The hover and pressed state are highlighted with a subtle change of the background color. The focus state is indicated with an additional 2px outline.

### Selection

The selected state indicates option list items, cards, etc. that are chosen by the user or by the system.

---

## Usage

**Using colors in Figma**

All color tokens are provided as Figma variables and can be applied as "Fill".

Please note that the variables are scoped. Text colors can only be assigned to the fill of text layers and border colors can only be assigned to borders.

**Theme switch / modes**

The light theme is activated per default. In order to switch to the dark theme, the mode needs to be set to "Dark". This can be done for a whole page in Figma or for certain frames or even layers by clicking on the mode icon.

Learn more about modes in Figma on the [Figma help page](https://help.figma.com/hc/en-us/articles/15343816063383-Modes-for-variables).

### Do's and don'ts

- **Do**: In design and development, use color decision tokens rather than colors directly from the global color palette. They simplify applying color in a consistent, reusable, and scalable way.
- **Don't**: Use raw palette colors directly in designs or code.
- **Do**: Use colors according to their intended purpose.
- **Don't**: Apply colors outside their intended semantic role (e.g., using an action color for text).

---

## Live preview

[Explore colors in Storybook Flutter](https://storybook-coreui-d2-euw3.d.dscore.com/#/Foundation/Colors)
