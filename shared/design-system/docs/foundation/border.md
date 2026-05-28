# Border

> Source: https://zeroheight.com/0b922d40b/v/latest/p/429dc0-border
> Introduction: Borders outline UI elements. Depending on the interaction state, border thickness and color can vary.

---

## Border width tokens

A set of border width tokens is provided to ensure consistent border styling across components.

---

## Usage

The style of a border is defined by several tokens: a corner radius token (see [Radius](https://zeroheight.com/0b922d40b/p/83fff6)), a border color token (see [Color](https://zeroheight.com/0b922d40b/p/847b05)) and a border width token.

**Applying border width tokens in Figma**

All border width tokens are provided as Figma variables, that can be applied to the stroke weight property.

### Do's and don'ts

- **Do**: Combine individual border tokens with the matching counterpart, e.g. the color "Border.Focus" with "Border.Width.Focus".
- **Don't**: Mix border color and width tokens from different semantic categories.

---

## Live preview

[Explore border width in Storybook Flutter](https://storybook-coreui-d2-euw3.d.dscore.com/#/Foundation/Border%20Width)
