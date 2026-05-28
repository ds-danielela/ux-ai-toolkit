# Skeleton

Skeleton components provide a lightweight visual placeholder that mimics the structure of content before it fully loads, helping users perceive faster performance and reducing cognitive load during wait times.

---
title: Skeleton
url: https://zeroheight.com/0b922d40b/v/latest/p/953907-skeleton
introduction: Skeleton components provide a lightweight visual placeholder that mimics the structure of content before it fully loads, helping users perceive faster performance and reducing cognitive load during wait times.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Skeleton: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d39af49069053fe17973f6)

**Skeleton: Preview**

---

## Design spec

![Skeleton: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/869facbe96a99d4f037e1e)

**Skeleton: Design spec**

### Size and scaling

Skeleton elements should match the dimensions of the content they represent, ensuring a seamless transition once the actual data is loaded.

---

## Anatomy

Skeletons offer a set of predefined shapes that should be selected based on the anatomy of the component being loaded. The following shapes are available:

1. Box
2. Pill
3. Circle

---

## Usage

Use skeleton components to indicate loading states during initial page loads, such as after navigating to a new view.

Only use skeleton states on container-based components like tiles and structured lists or data-based components like data tables and cards. In most cases, action components (e.g. buttons, input fields, checkboxes, toggles) do not need to have a skeleton state.

Skeleton states can be applied to:

* Accordion
* Avatar
* Card
* Container
* Dental chart
* Focus mode toolbar
* Focus mode side sheet
* List
* Media tile
* Side Sheet
* Table
* Tag
* Timeline stepper

When designing skeleton states, distinguish between:

* Static content (e.g., known headlines, persistent controls): These may remain visible to improve clarity and layout stability.
* Dynamic content (e.g., user data, lists, charts): These should be represented using skeleton shapes to indicate pending content.

### Styling

Skeleton components use a neutral, uniform color regardless of the final content's styling.

| Shape | Usage | Design specifics |
| --- | --- | --- |
| Box | Used for media elements like images and for structural components such as toolbars or containers to simplify layout during loading. | The corner radius is determined by the corner radius of the component being loaded. |
| Circle | Used for icons, avatars, or other circular UI elements. | - |
| Pill | Used for text lines and tags. | For skeletons representing text, the font size (specifically the ascent) determines the height of the skeleton shape (not the line-height). |

### Simplified appearance

**Display as skeleton leafs**

To maintain clarity during loading, some components should appear as a single skeleton element:

* Avatar
* Dental chart button
* Focus mode toolbar
* Tag

**Exclude from skeletonizing**

Buttons in variations should be excluded from skeleton states when nested within larger components. Although they should not be displayed, the space should be reserved.

### Motion and timing

To prevent a flashing effect, the skeleton state should remain visible for a minimum of 1000 milliseconds, even if the actual content loads faster. A subtle pulsing animation is applied in a continuous loop to indicate that content is actively loading.

### Providing dummy data

To ensure skeleton loaders closely resemble the final content and improve perceived performance, each team is responsible for supplying dummy data when the exact data is not available at load time.

### Content guidelines

* Match the layout of the final content as closely as possible to ensure a smooth transition once data is loaded.
* Size and shape should reflect the dimensions of the component being loaded.
* Do not include interactive elements such as buttons or links in skeleton states.
* Simplify complex components by representing them as a single skeleton shape when appropriate.

### Do's and don'ts

Use skeletons that match the size and layout of the final content to ensure a smooth transition.

Apply a neutral, consistent color to avoid implying meaning or status. Don't show status colors or content-specific styling in skeletons.

---

## Hints for designers

**Skeleton sizes**

Skeleton shapes should reflect the content as it appears after loading as closely as possible. The skeleton pill is available in different sizes.

Bind the height of the skeleton pill to a text size variable to apply dynamic resizing for small responsive layouts.
