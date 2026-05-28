# Radius

> Source: https://zeroheight.com/0b922d40b/v/latest/p/83fff6-radius
> Introduction: Rounded corners provide a friendlier look to an application. A set of border radius tokens enables a harmonious and consistent shape of UI elements.

---

## Border radius tokens

A set of border radius tokens is provided for consistent corner rounding across components and layouts.

---

## Usage

Rounded corners typically feel more friendly and accessible, while sharp edges can appear more formal and structured.

**Applying border radius in Figma**

All border radius tokens are provided as Figma variables, that can be applied to the corner radius property. While most border radius tokens are generic, component specific radius tokens, such as Border.Radius.Side Sheet respond to the mode switch (see [Responsive spacing and typography](https://dentsplysirona.zeroheight.com/styleguide/s/82440/p/24f1b2-reponsive-spacing-and-typography)).

### Do's and don'ts

- **Do**: When nesting elements, ensure to visually reflect the hierarchy, by i.e. using a slightly smaller radius for the child element.
- **Don't**: Apply the same radius to both parent and child elements when nesting — this breaks visual hierarchy.

---

## Live preview

[Explore radius in Storybook Flutter](https://storybook-coreui-d2-euw3.d.dscore.com/#/Foundation/Border%20Radius)
