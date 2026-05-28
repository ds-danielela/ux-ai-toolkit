# Highlighting differences

**URL:** https://zeroheight.com/0b922d40b/v/latest/p/2079ba-highlighting-differences

**Introduction:** Highlighting differences visually marks values that are not identical across compared items.

---

![Highlighting differences: examples](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/319f4ff826d9eb45360e26?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=8e0af638a64c86cd73278e4be92ec1a5cf3f39bf4eef2b61373c8fc94879bced)

**Highlighting differences: examples**

---

## Usage

When users compare or merge records, they need to quickly identify what is different and make confident decisions. In patient merging, incorrect decisions can lead to data inconsistencies or medical risks. Highlighting differences makes discrepancies immediately visible and reduces cognitive load.

### When to use

Use highlighting differences when:

* Comparing two or more data sets side by side
* Supporting merge or conflict resolution flows
* Reviewing changes before confirmation
* Identifying inconsistencies in critical data (e.g. patient details)

Do not use it for:

* General emphasis or styling
* Non-comparative content
* Decorative purposes

### Pattern description

Highlighting differences visually marks values that are not identical across compared items. In the patient merge use case, differing values are highlighted using **Surface/Warning** color token. Differences are emphasized using both color (warning token) and text styling (e.g. bold) to provide a strong and unambiguous visual signal. This ensures:

* Immediate visibility of discrepancies
* Consistent semantic meaning across the system
* Alignment with existing status and feedback patterns
* Legibility and consistency between light and dark modes

![Highlighting differences: visualisation](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1d7f2bf8de160bfd8c414e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=00dff6748f207d57a6ae1afdf6c1af1ac4d926bdd022fa47d34c26ed177cd0d0)

**Highlighting differences: visualisation**

---

### Do's and Don'ts

Highlight only differing values, don't highlight entire cards or sections unnecessarily.

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Do | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d2ecd0baa6f50dd5185e4f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=378035ba4cc2a656700878f74705dd8b3a1ee8720e944bd12ae65920ed89cdd9) |   |   |
| Don't | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/23ce488c542d7fd9c69bc7?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=8a8ec9281df47b100bf6bad05d26c85fc90a8e5984df9ee1d1ee61bc91530f5c) |   |   |

Keep selection and difference highlighting visually separate, do not use custom highlighting colors.

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Do | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b329829b9f1c1c5a2739ad?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=a9d5f51369861f91d46916119a423e3b689cdd6eaf61d1574d4de923b41038b1) |   |   |
| Don't | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/fda433a24a1009ffbd2c62?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=303e97dc550fd0217683b71a74d5a1bad9c8eeed583e0ed8ed85c63545276011) |   |   |
