# Unavailable interactions

**URL:** https://zeroheight.com/0b922d40b/v/latest/p/8933e5-unavailable-interactions

**Introduction:** An unavailable interaction occurs when the interface prevents the user from carrying out an intended action. Choosing the right treatment matters because it shapes how users understand what is possible and why. This page outlines a framework for deciding when to disable, hide, validate, or explain an interaction based on its constraint type.

---

## Disabled state

### What is a disabled state?

A disabled state is a condition in which the component is present, but not interactive. In our system, the disabled state is shown as a slightly toned-down version of the component to indicate temporary unavailability without removing it from context. When a component is disabled, it cannot be focused, activated, or used to trigger any action.

![Disabled: Example](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b298f57c1d590f2ebdb0a9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=60cbb72f055775308ec6d254c5a065a99d671e251d489a349f0f614b16e1037e)

**Disabled: Example**

---

### The issue with disabled states

Disabled states introduce several accessibility, usability, and cognitive challenges. While they signal that an action is unavailable, they often leave users without guidance on what to do next.

#### Accessibility limitations

Disabled components cannot receive focus and are often announced poorly, or not at all, by assistive technologies. Their toned-down appearance can also reduce contrast, making them harder to perceive for users with low vision. While WCAG does not require inactive user interface components to meet non-text contrast requirements, these limitations can still create real usability and perception issues ([WCAG 2.1, SC 1.4.11 Non-text Contrast](https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html)).

#### Lack of guidance

Disabled components rarely communicate what the user needs to do to enable them. This can create confusion, stall task progress, and increase frustration.

#### Poor discoverability

When a disabled component becomes enabled, users often fail to notice the change because the state transition is subtle, especially when the disabled state is only slightly toned down.

#### Increased cognitive load

Even though disabled components are inactive, they still occupy visual space and compete for attention. They add options the user cannot act on, which can clutter the interface.

## Guidelines

### Constraint types

Unavailable actions can arise from different types of constraints, and each requires a different interaction strategy. To support more consistent decisions across products, the following framework helps identify the nature of the constraint before selecting a treatment. The constraint types table below summarizes the constraint types and the suitable treatments for each. Use it as a reference when evaluating how to handle unavailable actions. Questions or edge cases may come up as you apply this guidance. When in doubt, [contact the design system team](https://zeroheight.com/0b922d40b/p/839fe0-contact-us) for clarification and support.

| **Constraint type** | **Description** | **Recommended treatment** |
| --- | --- | --- |
| [Boundary limits](https://zeroheight.com/0b922d40b/v/0/p/8933e5-unavailable-interactions/t/f66c940eeb) | System limit reached (min/max) | Disable |
| [Missing requirements](https://zeroheight.com/0b922d40b/v/0/p/8933e5-unavailable-interactions/t/2a88224d89) | Missing input or unmet condition | Keep enabled + validate |
| [Temporary conditions](https://zeroheight.com/0b922d40b/v/0/p/8933e5-unavailable-interactions/t/fd2e14ec47) | Loading, processing, async state | Loading state or disable + explanation |
| [Permission or policy restriction](https://zeroheight.com/0b922d40b/v/0/p/8933e5-unavailable-interactions/t/0e83cf065a) | Role-based or regulatory restriction | Hide or disable + explanation |
| [Context-specific irrelevance](https://zeroheight.com/0b922d40b/v/0/p/8933e5-unavailable-interactions/t/4d05ae0912) | Action does not apply in this context | Hide |

#### Boundary limits

Boundary limits occur when users reach the natural edges of what the system can do at this moment. These limits are built-in and predictable, not caused by errors or missing requirements. Typical examples include reaching a minimum or maximum value, an already full selection limit, or trying to trigger an action that has no further effect. These moments don't require the user to fix anything. The system is simply telling them "you're already at the limit".

**Recommended treatment**

Use a disabled state to communicate that the interaction cannot go further. Because boundary limits are usually self-explanatory, additional messaging is often unnecessary. If the limit is not visually obvious, a small, contextual hint can help clarify why the interaction is unavailable. **Example:** Reaching the minimum zoom level in canvas.

![Disabled: Boundary](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/818346dc054e308887766c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=7c16346f348e53fa1a4d1b206114c66b9bd448aaab3318bf1909e28aa4b03c2c)

**Disabled: Boundary**

---

#### Missing requirements

Missing requirements occur when the user can complete an interaction, but only after providing something essential. This could be a required input, a missing selection, or a condition that has not yet been met. The key is that the user has the power to resolve the issue directly.

**Recommended treatment**

Do not disable the interaction. When the user attempts it, validate and provide clear, inline guidance that points to exactly what needs attention. This approach keeps the path forward visible and avoids the frustration of a "mystery disabled button". Use concise and helpful messaging near the field or element that needs fixing. Validation is most effective when it appears close to the cause, not only at the top or bottom of a form. **Example:** The button to submit a form is always active. The form is validated after the user has pressed this button. Error messaging should appear as validation states on the form field, and with an inline notification at the top.

![](https://zeroheight-user-uploads.s3.eu-west-1.amazonaws.com/images/qjQKFuuMv4zocbbsVhLlaQ.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=46c9e298a400a4e46e1f4ebd231365c7962b531c10aa0afc6426613e6d3acc98)

#### Temporary conditions

Temporary conditions occur when the system is working and cannot support the interaction at this moment. The system might be loading data, syncing, processing a file, or performing an operation that takes time to complete. The interaction is unavailable only for this short duration. During these moments, the goal is to show that progress is happening and that the user does not need to act again.

**Recommended treatment**

Use the button's loading state when the action triggers processing. The loading state is disabled and includes a progress circle, which makes it clear that the system is working. Items that are not buttons can also become temporarily unavailable. For example, a spacious card representing a device can be disabled when the device is already in use. The disabled state communicates that the item cannot be interacted with right now and becomes available again once the device is free. Temporary conditions represent a short pause, not a removal. Hiding the interaction would make the interface feel unstable or unpredictable. **Example:** The button loading state indicates that the system is processing data.

![](https://zeroheight-user-uploads.s3.eu-west-1.amazonaws.com/images/ROqVr_jvGG2XMERcTIj35Q.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d35b8ad2419e46367567caddbf6157bf215c4d803839c10f0a7cd31add4ebc66)

#### Permission or policy restriction

Permission and policy constraints occur when an interaction is restricted because of user roles, access levels, licensing, or compliance rules. The user is not allowed to perform the interaction, either temporarily or permanently, depending on the system setup. These restrictions are not caused by missing inputs or temporary system work. They are intentional safeguards that protect data, structure, and responsibilities.

**Recommended treatment**

Hide restricted interactions when the user does not need to be aware of them. This prevents unnecessary visual noise and avoids the frustration of being shown things the user will never be able to do. Hiding also supports a cleaner mental model, where the interface only reflects the capabilities that belong to the user's role.

Choose hiding when:

* The action is irrelevant for the user's role
* The user cannot gain the required permission through normal workflows
* The restricted capability does not impact their tasks
* Surfacing it adds confusion without value
* Seeing the disabled action would feel unfair or discouraging

Keep the interaction visible but disabled only when awareness is useful or meaningful. Disabled interactions can support onboarding, help users understand how responsibilities are split, or serve as an upgrade cue if your product model uses that pattern. In these cases, pair the disabled state with a short explanation, such as a tooltip or inline notification.

Choose disabled visibility when:

* The user benefits from knowing the capability exists
* It clarifies team responsibilities
* It helps users understand why another person can perform an action
* It supports permission requests or upgrade flows
* The user could gain access later through a clear process

![Disabled: Permission](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7f6ec5b753ecde9829101c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=efe2b892818fbe0779be45f9929bd591d15bf6d41a686b6151219dc4bd005dc0)

**Disabled: Permission**

---

#### Context-specific irrelevance

Context-specific irrelevance occurs when an interaction simply does not make sense in the user's current situation. The interaction might be valid in other modes, on other selections, or at a different point in the workflow, but in this moment it does not apply. Nothing is wrong, nothing is missing, and no rule is being broken. The interaction is just not meaningful right now.

**Recommended treatment**

Hide the interaction in these cases. Visibility should reflect relevance. Showing controls that do not apply creates noise, forces users to interpret unavailable options, and can give the impression that something is broken or restricted. Hiding helps the interface feel focused and intentional, especially in complex tools or multi-step workflows. If the context changes and the interaction becomes relevant again, it should appear in a predictable and stable location so users can build confidence in where to find it. **Example:** The action buttons at the right of the universal action bar can vary depending on the selection in the container below. Below, only one button is displayed initially, allowing the user to upload media.

![Disabled: Context 1](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3f1c4bb63e2f5998cd377f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=a8155db2a584550698212d2ce3d059df3644b8b5f16069ba5389a7c655bde38b)

**Disabled: Context 1**

---

Once one or more media tiles are selected, the actions are replaced by actions that can be applied to the selection.

![Disabled: Context 2](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/82275f1adc7f8fe480bb8e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=b3f64b83154bdaa59c1d7950cf37fca53ed3774a282135087680ab7212dbee41)

**Disabled: Context 2**

---

### Do's and Don'ts

Keep the submit button enabled and show inline validation that explains what needs fixing.

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Do | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/fbaa3269ab38d077fa8a42?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d53c6574c35624232018e594fc5c79b9b2958225226d2cc8c67041f495cd8f7b) |   |   |
| Don't | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/27ac3d3a8fc020030ce1ff?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=7e40fd355d403eb677158faaea03cd1e28cdd76abcc331c96b79b19a3d44dcf9) |   |   |

When using the disabled state, provide a short, contextual explanation if the reason isn't obvious.

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Do | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/317e20a804be228d4e1145?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=9446606d4179e071ef714bd8422701e13459da626b9c5ce1cee2a1cd1567510c) |   |   |
| Don't | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/69d8b593971f214606036a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=02c4a642489c35e67d81e3e3256a872c23ae549278e0e6e1526a9c5b2d15009c) |   |   |
