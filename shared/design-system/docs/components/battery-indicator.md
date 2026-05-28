# Battery indicator

---
title: Battery indicator
url: https://zeroheight.com/0b922d40b/v/latest/p/5898e9-battery-indicator
introduction: Battery indicator component shows current battery level or a charging status. It standardizes how battery statuses are displayed so that the users can quickly understand battery availability for a specific device.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ⚪️ |

![Battery indicator-Full](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/967421c0857d6634a36aa2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133057Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=b8b08029f5a37576eb36a964f9dd66b77e2cab2a8b35e4a8a371b7f845e66b6b)

**Battery indicator-Full**

---

## Design spec

![Battery indicator: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/70dbc28f3c6212c5eff05c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133057Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=548b3a4e00d5e9bf1ce3fb4face6757733c0802b99c05eb3011a32dc375229a9)

**Battery indicator: Design spec**

---

### Size and scaling

The size of the battery indicator is the same on all screen sizes, except for responsive mobile where the numeric percentage value text is excluded.

---

## Anatomy

The battery indicator contains the following elements:

1. Battery icon
2. Percentage value text (not required on responsive layout S)

![Battery indicator: Anatomy](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/fad1594652f2e8ca4b2371?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133057Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d4398bedf55bcf5f2b2bafef7232b25bdf0a9ff3b6061ceb12f7896c354d370d)

**Battery indicator: Anatomy**

---

## Usage

Use a battery indicator component whenever the users needs to understand power status at a glance, and where the battery level affects usability. The usage of this component is appropriate in contexts where the power availability influences user decisions or when the low battery status requires timely awareness. As there currently are no global specifications, the ownership on when should the low battery indicator be shown for specific devices in on the application-level / device level. Percentage value text can be manually adjusted as needed to reflect additional updates in the battery levels, if necessary.

### Content guidelines

* Use the appropriate percentage value text to reflect battery status level

### Do's and don'ts

Percentage value text always goes after the battery indicator icon.

Always show the percentage value text of a battery for all M, L and XL screen sizes. The only exception to hide percentage value text is for responsive mobile screens (S) in order to preserve screen real estate.

Don't use custom adjustments to the color, like for example updating the border and text value properties on low battery indicator status.

---

## Live preview

[https://storybook-app-dot-lightning-ui-poc.ey.r.appspot.com/#/stories/button](https://storybook-app-dot-lightning-ui-poc.ey.r.appspot.com/#/stories/button)
