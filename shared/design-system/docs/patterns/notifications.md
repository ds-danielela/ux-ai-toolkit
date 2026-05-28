# Notifications

**URL:** https://zeroheight.com/0b922d40b/v/latest/p/724668-notifications

**Introduction:** Notifications are used as a primary method communicate to the user. They range from granular messaging to system-wide messages.

---

![Notifications: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ca4d239b2841a16dbbc858?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133044Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=e118fc1e039607c09ba44ae66ef988b6f74a5b66aebf9cafd97f83ca7ac1cfe6)

**Notifications: Preview**

---

## Usage

Use notifications to update or inform the user of a status change that they should know about. They should be used in a timely manner with clear direction or message for the user.

### Notification types

Consider the context and use case when you choose an appropriate pattern for communicating a message to users.

| **Type** | **Usage** |
| --- | --- |
| [Alert dialog](https://zeroheight.com/0b922d40b/p/48505e) | Use alert dialogs to provide users with critical information that needs their immediate attention or action. When the alert dialog is open, the user cannot interact with the underlying content. Use alert dialogs sparingly, as the interrupt the user's workflow. |
| [Banner](https://zeroheight.com/0b922d40b/p/27f50c) | Use banners to provide users with non-disruptive messages about system or product level information that is not specific to a task. Banners are be placed above the top bar of a page. |
| [Empty state](https://zeroheight.com/0b922d40b/p/02a0dc) | Use the empty state when a page or section is empty or cannot be shown (for example, if an object no longer exists or a workflow is not supported for the user's resolution). |
| [Field validation](https://zeroheight.com/0b922d40b/p/523b03-text-field/t/62749d) | Use field validation to highlight affected text fields or other form components after validation. Field validation is used in conjunction with an inline notification above the form. |
| [Inline notification](https://zeroheight.com/0b922d40b/p/5697b4) | Use inline notifications to provide users with non-disruptive feedback or the status of an action related to the content shown on the page. Inline notifications are frequently used in conjunction with field validation in forms. |
| [Snackbar](https://zeroheight.com/0b922d40b/p/875abc) | Use snackbars to provide quick and lightweight feedback about a recently performed action or system event. Snackbars are displayed centered at the bottom of the screen and can optionally include an action. |
| [Toast](https://zeroheight.com/0b922d40b/p/25384c) | Use toasts to provide users with non-disruptive feedback or ephemeral status updates that are not necessarily related to the content on the page. Toasts slide in at the top right of the screen and usually disappear automatically after five seconds. |

### Find the right notification component

Use the decision tree below to quickly identify the most suitable notification pattern for your use case. Whether you're designing for urgency, visibility, or user interaction, this tool helps you make consistent, user-centered choices.

[Notification decision tree (Figma prototype)](https://www.figma.com/proto/DYW0yZ0ZrlDwir0MdaTnfJ/Decision-tree-for-notifications?page-id=2%3A18&node-id=2-1405&viewport=937%2C878%2C0.12&t=e6SeNlo05Lm2ok5s-1&scaling=contain&content-scaling=responsive&starting-point-node-id=2%3A1405&hotspot-hints=0&disable-default-keyboard-nav=1&hide-ui=1)

### Status types

A status type categorizes the notification that is being communicated. It is important to specify the status type in order to use the correct icon and color.

Most notification components support the following status types.

| **Type** | **Usage** |
| --- | --- |
| Critical | An issue has occurred that prevents further processing. |
| Warning | A problem or inconsistency has arisen. Users can carry on working, but might run into an error later on. |
| Success | An action has been performed without errors or warnings. |
| Information | You want to provide additional, non-critical information. |

The field validation is only available with the status type critical. The alert dialog includes emphasized variants for critical and warning intended for the medical context. Empty states can be used versatilely and therefore cannot be restricted to the above status types.

### Additional considerations

* Avoid showing multiple notifications to the user at once when possible. Too frequent or disruptive notifications can create a negative experience.
* The user should always be aware of the status of the system or a task. Critical messages should be communicated immediately.

### Content guidelines

* Give guidance. Explain the problem and, if possible, say how to fix it.
* Avoid saying "Something went wrong". Use it only if you really can't explain the problem.
* Don't put the blame on the user.

### Do's and Don'ts

Write in sentence case.

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Do | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/721fc6b3fad9c6833ab1df?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133044Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=8bf04d6aac4c0f0d9e5fc999cbe1421c612a42c03eaadf0a26e56489bc8dedd9) |   |   |
| Don't | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1ad70528adf61162ad93a6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133044Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=c9b9d6d39635d1bdb87298e9384eb27cf9265220582652f49a4380ba076ab459) |   |   |

Explain the problem and try to provide guidance on how to fix it.

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Do | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e57545c4b91df22f5a9326?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133044Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=82cf116ba3963cb42f0fbc25e0c2755856f32ea2894495b8486c9a837e1274ce) |   |   |
| Don't | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6eb20cbcd4f35c042d9c98?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133044Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=1ade9fefae11733551f55152f8626019c83fa478f615e642beef6873819241e5) |   |   |

Use proper icon and color combination for the notification components.

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Do | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b693802a73956c14c770c9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133044Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=9de0f2031de7db52edaaed5404de79354aa3a426f0c58c023c9897e89b3c48e2) |   |   |
| Don't | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6a13adec884c56e6e3e08d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133044Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=eec777f8673a67f61947bdfef09005c13145b576c101c1bdffdfa7cedb077d94) |   |   |

Stick to the provided variants and do not introduce custom icons or colors.

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Do | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a9f1fafb1554a453a2e853?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133044Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=faa253713d18983bc8069da4e7f1f3f3b8e2bea3826527fdad37c22d9b482369) |   |   |
| Don't | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a37b921359839fa168e4ef?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133044Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=81fe0060faf771623a6912a5f29c1ff5f6377f96f676782aedaa40a9b39f7f63) |   |   |
