# Wizard

A wizard is used to guide the user through complex workflows with several steps.

---
title: Wizard
url: https://zeroheight.com/0b922d40b/v/latest/p/908e33-wizard
introduction: A wizard is used to guide the user through complex workflows with several steps.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Wizard: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/87ec2aa6ca443d9c8a5e6a)

**Wizard: Preview**

---

## Design spec

![Wizard: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/8c7f79b7fa3fa5f130fc14)

**Wizard: Design spec**

### Size and scaling

The width of the wizard bar is fixed and depends on the responsive layout.

The width of the individual wizard steps depends on the content for visited and future steps. The current step stretches to the width of the parent container.

---

## Anatomy

The wizard contains a wizard bar within the top bar (1). The wizard step content is displayed within a container (2). Furthermore, an optional summary container (3) can be displayed next to it.

Onboarding wizards include a logo on the left (1). Wizards triggered from within the application contain a button to close the wizard on the left (2), a headline and optional subline (3) as well as the notification menu and an optional user menu button on the right (4).

The wizard bar contains several wizard steps. The current wizard step contains a step number (1) followed by a label (2). Visited and future steps are represented by their number (3 & 4). All steps contain a progress bar at the bottom (5).

The wizard step container includes the wizard step headline (1) and an optional subline (2) as well as the wizard step buttons (3).

Every step except for the last step contains a button to navigate to the next step (DSWizardStepButton.stepForward). Every step except for the first step contains a button to navigate to the previous step (DSWizardStepButton.stepBack). The last step contains a button to finish and submit the wizard (DSWizardStepButton.Finish).

---

## Usage

Use a wizard when the user needs to perform a task or goal that requires more than one step in a specific sequence.

### Truncation

If the space does not suffice to show the full wizard headline, it will be truncated with an ellipsis. The full label will then be available in a tooltip.

### Initial focus

When using a wizard, the user should land on the first editable component in the first step.

### Interaction

The user can navigate to the previous or next step by pressing the provided buttons. The first step of the wizard will include a primary action button that directs them to the next step.

The range of steps from the second step to the last step will include a primary action that directs them to the next step or finish. Also included is a secondary button at the bottom left that allows the user to go back to the previous step.

Steps that are optional will include a "Skip this step" tertiary button next to the primary action button.

Since visited and future steps are represented by their number, the name of the step is displayed in a tooltip.

### Validation

When the user clicks on the button to proceed to the next step, the input on the current page is validated. Inline notifications are used to present the user with any errors that occur.

### Scrolling

If there is not enough vertical space for the wizard content, a scrollbar is displayed on the right. This scrollbar can be used to scroll the wizard content, while the summary remains sticky at the top.

### Sub-steps

A wizard step can also contain sub-steps. In that case, the progress bar of the corresponding step represents the amount of sub-steps.

For steps with sub-steps, the label in the wizard step bar remains the same while the heading in the content area changes for each sub-step.

### Content guidelines

* When multiple steps are enabled, wizards should have a minimum of two steps and maximum of eight steps.
* Use "Continue" for the button that allows the user to move to the next step.
* The button that allows the user to submit the wizard should always use the format: [Active verb][object/resource], i.e. "Place order".

### Do's and don'ts

Use sentence case.

Do always show the wizard in a top bar when completing forms or a step of actions, or a focus mode toolbar when used within the focus mode.

Use a wizard variant without multiple steps (one-step wizard) to cover cases with actions that take place outside of DS Core, but don't have a dedicated layout.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Wizard%20scaffold%20(top%20bar)](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Wizard%20scaffold%20(top%20bar))

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Wizard%20Step%20Container](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Wizard%20Step%20Container)
