# Spacing

> Source: https://zeroheight.com/0b922d40b/v/latest/p/944aaa-spacing
> Introduction: A set of defined spacing tokens enables consistent and harmonious spacing within components and layouts.

---

## Layout spacings

Please note: For responsive layout S, the layout spacings differ (see [Responsive spacings and typography](https://dentsplysirona.zeroheight.com/styleguide/s/82440/p/24f1b2-reponsive-spacing-and-typography)).

---

## Component spacings

Component spacings are used for spacing within individual components.

---

## Usage

Use component spacings for spacings within a component. Use layout spacings to separate components within a building block or a page layout.

**Using spacings in Figma**

There are different ways to use the available spacing tokens in Figma. Since layout spacing values vary depending on the responsive layout, spacings respond to the mode switch (see [Responsive spacing and typography](https://dentsplysirona.zeroheight.com/styleguide/s/82440/p/24f1b2-reponsive-spacing-and-typography)).

**Use spacings as variables in auto layouts**

If you want to place components at a homogeneous distance, for example in a form layout, it makes sense to use spacing variables in the auto layout.

**Use spacing components**

All spacing tokens are also provided as Figma components. It makes sense to use these when building complex layouts that has different spacings to emphasize the screen hierarchy.

**Please note:** Spacing components can be visually hidden by activating the "Hide" property while still occupying the space. However, it is recommended to not hide spacings when handing screens off to development.

### Do's and don'ts

- **Do**: Stick to the provided spacings and do not introduce custom values that are close to the provided ones.
- **Don't**: Use arbitrary spacing values outside the token system.

---

## Live preview

[Explore spacing in Storybook Flutter](https://storybook-coreui-d2-euw3.d.dscore.com/#/Foundation/Spacing)
