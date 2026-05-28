# Responsive spacing and typography

> Source: https://zeroheight.com/0b922d40b/v/latest/p/24f1b2-reponsive-spacing-and-typography
> Introduction: To ensure a balanced and efficient layout among all responsive layouts, layout spacings and typography adapt to the screen size.

---

## Token structure

To achieve an adaptation of layout spacings and text styles for responsive layout S, numerical variables are provided for two modes:

* **Not small**: applies to all responsive layouts from M - XL
* **Small**: applies to responsive layout S

In most cases, the values for the Small mode are smaller as less space is available.

For the text styles, mostly only the font-size was adjusted and the line-height remained the same. This is due to the fact that the size of many components is determined by the line-height. Other examples are headlines that align with a button (i.e. in a modal dialog) and therefore keep the same line-height.

## Usage

**Usage in Figma**

The "Not small" mode is activated per default. In order to switch to the small mode, "Number-Tokens" must be set to "Small". This can be done for a whole page in Figma or for certain frames or even layers by clicking on the mode icon.

**Please note:** Layout templates and dedicated components for responsive layout S are already provided with "Small" mode activated.

**Please note:** When selecting a text layer with a text style, it only displays the font size and line height values for the default mode (Not small), no matter which mode is activated. The mode specific values can be double checked when using the Dev Mode.

**Usage in Flutter**

DSTokens.forFormFactor() automatically changes the token set used based on the themeType and formFactor. DSTokens.forFormFactor() is already used by DSTheme so you will likely see this change automatically.

### Do's and don'ts

- **Do**: Use the "Small" mode and dedicated component variations only when designing for responsive layout S.
- **Don't**: Use the "Small" mode for layouts larger than responsive layout S.
