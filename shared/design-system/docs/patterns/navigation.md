# Navigation

**URL:** https://zeroheight.com/0b922d40b/v/latest/p/81c606-navigation

**Introduction:** A comprehensible navigation concept offers the user orientation. At the same time, it is possible for the user to switch between the parts of the application at any time.

---

## Usage

### Navigation levels

We distinguish between two different navigation levels:

* Top level
* Detail level

Top level screens are represented by the items in the main menu. They usually contain several lists, i.e. in the home screen (1) or a list / table like in the top level table template (2).

![Navigation: Top level](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/cbab69bfa5bc17a38a180c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133045Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=fa28572600b6db23a5d45093cdc7e05ab043b1799a06f4f27e9df5495560e617)

**Navigation: Top level**

---

Detail level screens can be accessed through top level screens. They represent an object like i.e. in the second level gallery or generic second level screen template. Furthermore, a detail level screen can also be a wizard (2) or a focus mode screen, like a viewer (3).

![Navigation: Detail level](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/cb894efd13656ff1d16a78?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133045Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=30bf9b20d85d58dddf2bbd89ae69fc7150ade7106c3e65c3ca4149be3f948e03)

**Navigation: Detail level**

---

### Navigating

There are several ways to navigate at the same level or deeper into the application hierarchy. Via the main menu, the user can navigate to a top level screen from another top level screen (1a) or a detail level screen (1b). Within the content area of a screen, i.e. from a list item or table row, the user can navigate from a top level to a detail level screen (2a). Also within a detail level screen, the user can navigate to another detail level screen (2b). On a detail level screen, the back button allows the user to navigate back to the previous screen which might be a top level screen (3a) or another detail level screen (3b). The wizard is typically triggered by a button (4a) or an item on the top level or detail level screen. The same applies to focus mode screens (4b).

![Navigation: Navigating between levels](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/56076afd48a3b76fda735d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133045Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=f1fd30bb3060dc36d88bcefd4b6e4f777c36916261a0f9165e085cecf7006542)

**Navigation: Navigating between levels**

---

### Main menu

On top level screens, the corresponding item is selected in the main menu (1). As soon as the user navigates to detail level screen, no main menu item is selected (2).

![Navigation: Main menu](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6b815ce39534bb846f888a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133045Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=77cced97194e869ed8f08065a3012e0f14f1196e49e70116a2c2ee39a5cd1e77)

**Navigation: Main menu**

---

### Back navigation

On every detail level screen, there is a possibility to navigate back. It can either be included in the page header (1), the wizard top bar (2) or the focus mode header (3).

**Please note:** In the wizard top bar, the button contains a close icon to avoid confusion with the button that navigates to the previous step.

The back button in the page header should always be labeled according to the headline of the previous screens (i.e. "Patients" if you navigate from the patient list to a patient details page).

![Navigation: Back navigation](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/79300e4218cdbe8ddba0c5?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133045Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=e579bb21d671e5db651544afb7f29f1db7b52c871620512f13379c93cfecd12f)

**Navigation: Back navigation**

---

### Persist views

If the user changes to a certain tab and navigates from there (1), the user should be led back to exactly this view via the back button (2).

![Navigation: Persist views](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6e768cc959dbab37e391d2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133045Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=98290a7e0af824e060c233403fbe16fc57f588d26ad99a408801c35cd3b04c24)

**Navigation: Persist views**

---

### Do's and Don'ts

The label of the back button within the page header should match the headline of the corresponding top level screen.

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Do | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f4f6e4c893a1f3c5d9d8f9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133045Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=3a742465c8a49618d99c1b0caefdd1199d1ebda64322f33ac7bd7d5122c45b35) |   |   |
| Don't | ![](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/97c2671d80834ff5dbc588?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133045Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=e7ac8ea7ad4f1c3de1f92f40bc89e52a00a9cb3b4e9b56d2bc78e52c5bde4af8) |   |   |
