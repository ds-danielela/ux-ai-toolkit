# Common actions

**URL:** https://zeroheight.com/0b922d40b/v/latest/p/33bf1c-common-actions

**Introduction:** Actions trigger functions, such as creating an order or sharing a file. Actions are displayed as buttons. Common types of actions are add, cancel, close, delete.

---

## Anatomy

Depending on the use case, common actions are placed in different locations on the screen:

1. Follow-up actions for a view like i.e. focus mode are displayed in the top right of the view.
2. Follow-up actions within cards, containers with forms, modal dialogs, etc. are displayed in the bottom of the corresponding component.
3. The closing action for temporary views such as popovers, modal dialogs, side sheets, etc. is placed in the top right of the corresponding component.
4. Inline actions for list items, table rows, etc. are displayed in the right of the corresponding component.

![Common actions: Anatomy](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f5876e072313eb950bcef3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133041Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=65553d7ae4c540f804e1b562ebc5c5030976d56161b62cc7191db6d483be702e)

**Common actions: Anatomy**

---

## Usage

Actions trigger functions, navigate the user to different areas of the experience, and are differentiated from the navigation. Depending on what the action is, styles differ.

* High emphasis action: use a single primary button with all others being secondary
* Medium emphasis action: use a secondary button
* Low emphasis action: use a tertiary button
* Very low emphasis action (such as close or overflow of actions): use a tertiary icon button

### Action types

The following list contains typical common actions and their usage.

| **Action** | **Usage** |
| --- | --- |
| Add | Inserting an item to an existing list or set |
| Back | Moving from one step to the previous in a sequence / wizard |
| Cancel / Decline | Stops a current action or closes a component |
| Clear | Removes information from a field or selection |
| Close | Dismisses or terminates a modal, menu, or flow |
| Copy | Creates an identical instance |
| Delete | Permanently removes or destroys an object |
| Edit | Creates a state where data or values can be changed |
| Continue | Moving from one step to the next in a sequence / wizard |
| Refresh | Reloads data when the displayed view has not synchronized with the source |
| Remove | Clearing from a list or item. If information is removed, it can be recovered. |
| Reset | Reverts to the latest saved data |

### Top action placement

Common actions are displayed on the top right of most views. Depending on the use case or view, they are included within the following components.

| **Component** | **Usage** |
| --- | --- |
| [Page header](https://zeroheight.com/0b922d40b/p/788503) | Common actions which relate to the entire view should be included in the page header. On a patient detail view, this could be actions such as creating a DI scan or a simulation. |
| [Universal action bar](https://zeroheight.com/0b922d40b/p/983afa) | Common actions which refer to a table or media gallery should be included in a universal action bar. |
| Focus mode local actions | Common actions which refer to a focus mode view, such as the viewer, outcome simulation, etc. should be included in the focus mode local actions. |

When you place common actions in one the above listed components, consider the following sequence starting from the right:

1. Primary
2. Secondary
3. Tertiary

![Common actions: Top sequence](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7d22e29cac098c3832ab5c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133041Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=4f15e2208bf255fb8ff5a2f31ce2c1a460ed157d21ee4ab663b8dfca449c5370)

**Common actions: Top sequence**

---

### Bottom action placement

#### Cards, containers, notification components

In cards, containers and notification components, such as toasts, common actions are placed in the bottom left.

![Common actions: Placement container](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d0736fd9431bd8290b030d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133041Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=aaf5f7f1342e17226a5807c9b12853bca73440d381228f612305f8d6e2c895ef)

**Common actions: Placement container**

---

#### Wizard

In the wizard page container, the button to navigate to the next page or to finish the wizard is on the right. The button to navigate to the previous step is on the left.

![Common actions: Wizard](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/435377640ef3afa0b30742?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133041Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=3804f385562353d41277a90d468e81183192e129d3a4f0b96897b7dbdfa43378)

**Common actions: Wizard**

---

#### Modal dialogs

In modal dialogs, common actions are placed in the bottom right.

![Common actions: Placement modal](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2a0c017e9db90800da3d79?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133041Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=823b13c6524892b23472fd5079ae07f22bed3bf2ae3bda8305fa6f2ac2e250e4)

**Common actions: Placement modal**

---

### Closing action placement

The closing action in the top right is always displayed as a tertiary icon button with a close icon.

![Common actions: Placement closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/83c8f1b37a3fef5705c933?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133041Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=512ce4773542bbe23a33f91969e02857dd470afde0c4590e88454815493284f9)

**Common actions: Placement closing**

---

### Inline action placement

Inline actions within list items, table rows, media tiles etc. are usually displayed as tertiary icon buttons due to the lack of space. If there should be several actions, they can be combined in a icon button with option list.

![Common actions: Placement media](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/85f6958ee388e50892c254?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133041Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=1d5a8f608b8d51f496f79747eb8fda032cf68ed79d0ea586410cb8c82175cee3)

**Common actions: Placement media**

---

### Enabled vs. disabled buttons

Do not use the disabled state of the primary button, even if not all data is filled yet. There is a risk that the user does not understand why the button is disabled. Instead of disabling the button, show an inline notification explaining what needs to be done.

If the state of buttons depends on a selection like i.e. in the universal action bar, only active buttons should be displayed initially. Once a selection is performed, the actions that can be applied to the selection can be shown.

### Additional considerations

* Group related actions together and arrange actions in accordance to importance. Align in the order from right to left.

### Content guidelines

* Follow [button component guidelines](https://zeroheight.com/0b922d40b/p/156acf)

### Do's and Don'ts

Group related actions together and arrange them in accordance to importance. Don't center align semantic or secondary actions.

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Do | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/86e45745c2214601e0ea6c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133041Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=2a7f53630f32851d3fd0adde330ed58c4dd276028f6f49f3b75a8f145bab4a3d) |   |   |
| Don't | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3221e8cf13612a50c16e43?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133041Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=70283e812d144cd5200da10d29ebe3ff0e2ea49e420826bbedf0e16b906356c4) |   |   |

Avoid showing multiple primary buttons on the same page.

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Do | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/555381c16f1a721429f683?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133041Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=90954ba0d654755ea16fc75d25daf4ede99d536fc7c5350b73af2f4e7e1b03a2) |   |   |
| Don't | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ddb8a6b00bbfd58dae23bd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133041Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=7c62cb61e5e074929c3324bd26643b1523494fda7c93bf0e99582475899cead4) |   |   |
