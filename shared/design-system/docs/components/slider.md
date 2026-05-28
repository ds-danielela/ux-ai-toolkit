# Slider

Sliders are used to adjust a numerical parameter by dragging a pointer on a scale of given values or by clicking on the corresponding area of the scale.

---
title: Slider
url: https://zeroheight.com/0b922d40b/v/latest/p/2508f3-slider
introduction: Sliders are used to adjust a numerical parameter by dragging a pointer on a scale of given values or by clicking on the corresponding area of the scale.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Slider: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/44056652e99385d74269b1)

**Slider: Preview**

---

## Design spec

![Slider: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/cbc29e217bbefa2f62d5af)

**Slider: Design spec**

### Size and scaling

The slider height depends on its content. The width of the slider stretches to the parent container.

---

## Anatomy

The slider contains the following elements:

1. Label
2. Track
3. Thumb
4. Minimum and maximum values (optional)
5. Value label (optional)
6. Divisions (optional)

The slider can also be combined with a numeric input field (7), including an optional reset button (8).

---

## Usage

Use sliders if you want the user to enter a numeric value and the accuracy is not important. If there are only certain values available on the slider, the index automatically snaps in at these points ("discrete" variation).

### Centered

This slider variant is initialized with the thumb positioned at the center, representing a neutral or zero value. It typically supports a symmetrical value range, enabling users to select both negative and positive values by dragging the thumb left or right, respectively. This pattern is particularly useful for controls where deviation from a baseline is meaningful (e.g., ±100), such as image adjustments or offset parameters.

### Value label

The current value of the slider can optionally be displayed above the track. Three options are available for displaying the label value:

* Never display
* Display during interaction (default)
* Always display

### Slider with input field

The slider can also be combined with a numeric input field. Changing the value in the input field also affects the slider pointer position and vice versa. If the slider is combined with an input field, the value label should not be displayed.

If the space does not suffice to show the full label, it will be truncated with an ellipsis. The full label will then be available in a tooltip.

### Providing value outside slider's range

When the input value exceeds the slider's maximum, it is clamped to the maximum allowed value upon exiting the input field.

### Divisions

Divisions define a set of discrete, evenly distributed values along the slider track. When divisions are enabled, the slider behaves as a discrete control rather than a continuous one. Divisions are visualized as vertical lines along the track. The thumb snaps to the nearest division while being dragged.

### Content guidelines

* Keep slider labels short and concise.
* Use only universally recognisable icons, like "reset" or "show/hide" for slider control.

### Do's and don'ts

Write in Sentence case.

Do not use the slider for ranges that are extremely large i.e. 1-1000, or too small i.e. 1-3. Do not use the discrete version if there are only few intervals, e.g. 2-3.

Do not use ambiguous icons as slider icon button.

When showing several sliders with input fields below each other, the width of the input fields should be aligned.

Use the centered slider variation when the control represents a deviation from a neutral or zero baseline. Ensure the value range is symmetric (e.g., -100 to 100).

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Slider](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Slider)
