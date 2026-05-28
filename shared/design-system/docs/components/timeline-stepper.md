# Timeline stepper

The timeline stepper displays a timeline of tasks or workflows and tracks user progress or provides users with information about their place in the process.

---
title: Timeline stepper
url: https://zeroheight.com/0b922d40b/v/latest/p/969ad9-timeline-stepper
introduction: The timeline stepper displays a timeline of tasks or workflows and tracks user progress or provides users with information about their place in the process.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Timeline stepper: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b158c7cc5ee24513e493bc)

**Timeline stepper: Preview**

---

## Design spec

![Timeline stepper: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/4ec7d566d94c0c7a2b92fa)

**Timeline stepper: Design spec**

### Size and scaling

Responsiveness is built into the timeline stepper, allowing it to adapt to the container it is placed in. For responsive layout S, number tokens "small" are used. The height depends on its content.

---

## Anatomy

The timeline stepper is comprised of steps stacked vertically.

1. Header (optional)
2. Multiple steps, stacked vertically

Each step includes:

1. Icon (can include numeric value)
2. Headline
3. Subline (optional)
4. Leading line (used only when there is a step preceding)
5. Progress line (used only when there is a step following)
6. Error/validation text (used with "Failed" step, optional)
7. Expandable content (optional)
8. Action buttons (optional)

---

## Usage

Use the timeline stepper to display a timeline of tasks or workflows to track user progress or provide users with information about their place in the process.

| Use case | Characteristics | Usage |
| --- | --- | --- |
| Chronological log | Passive, linear history | Suitable for activity logs, audit trails, or event histories where steps are immutable and not progress-oriented. |
| Guided, vertical user steps | Active, possibly non-linear, guided | Suitable for workflows where users are guided step by step but can move back and forth. |
| Status tracking | Passive, linear state progression | Suitable for order tracking or request processing flows. |
| Linear multi-step workflow | Active, linear, guided | Use for full-screen processes and workflows that require significant space. |

### Icon usage

Steps in the timeline stepper have default icons associated with their type. Icons in color are used to signify important events such as Completed, Warning, or Failed, as well as the Active step the user is in.

### Numbered steps

Use numbered steps to communicate the user's position within a workflow at a glance. Numbers are only used for active and future steps. Completed, warning, and error states must use semantic colors and status icons.

### Non-linear workflows

The workflow variation of the timeline stepper component allows users to move through a series of steps in a non-linear manner. Users can jump between steps freely.

### Supplements

* Each step can have an action bar with one or more buttons.
* Each step can have its own expandable content.

### Collapsability rules

A step in the workflow can be collapsible. In workflows that require collapsible steps, only one step should remain expanded at a time.

### Skeleton state

The timeline stepper supports two levels of skeleton loading, depending on whether the whole component or only the content inside a step is still loading.

When the entire timeline stepper is loading, all step elements are replaced by neutral skeleton shapes:

* Icons are represented by circle skeletons.
* Headlines and sublines are represented by pill skeletons.
* Expandable content collapses to its default closed state.
* Status colors and state-specific icons are not rendered.

### Content guidelines

* Be brief, as space is limited. Headlines and sublines longer than three lines are truncated.
* Use interpunct (·) on dates.
* Ensure step action buttons make a logical connection to the headline.

### Do's and don'ts

Use the timeline stepper for short and simple workflows.

Use the timeline stepper for linear processes and workflows. Do not make the user switch contexts.

Use the timeline stepper's approved icon set and states. Do not modify or customise provided icons.

When linking inside steps, keep links inline and meaningful.

Do not combine numbered steps with non-numbered steps within the same workflow.

Avoid long sequences that require excessive scanning or scrolling.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Timeline%20stepper](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Timeline%20stepper)
