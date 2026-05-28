# Release notes

> Source: https://zeroheight.com/0b922d40b/v/latest/p/067517-release-notes

## 0.34.0

05.05.2026.

### **General notes**

This design system release includes introduction of the app indicator atom as a required element in the Focus mode header component, updates for multiple existing components outlined below and updating documentation that reflects these changes.

### **Tokens**

* Added gradient color token values for the app Indicator component background container

### **Components**

#### **New component**

* App Indicator: new component added as an atom. Currently hidden in the Figma library and used as a mandatory element in the Focus Mode header

#### **Component updates**

* Empty state: Now supports multiple buttons and optional illustration via new visibility properties

* Hero modal: Renamed *Body* to *Body widget* to avoid naming conflicts

* Focus mode: Focus mode header now includes the app Indicator as a required property

* Timeline stepper: Added support for numbered steps with new usage guidance

* Wizard: Top bar now supports a one-step variant via the *Multiple steps* boolean property

### **Documentation**

* New documentation for the app Indicator atom that is included as the mandatory element on the Focus mode header
* Expanded documentation on the empty state component guidelines
* Updated documentation on Size and scaling, Usage and Content guidelines and additional Do & Don't example that reflects changes of adding a one-step Wizard property
* Updated broken link to focus mode side sheet
* Updated minor typo in toggle button documentation

---

## 0.33.0

01.04.2026

### Tokens

**Color tokens**

* Update: Adjusted Icon/Interactive color to dsBlue600 / dsChartreuse400
* New: Added Border/On Imaging which is dsWhite for both themes to display borders on imaging media, such as X-rays

### Components

**Generic updates**

We are introducing Figma slots for component content. Previously replaceable content, marked with our custom "Swap me" component, is now wrapped in a slot to avoid breaking changes. This allows designers to replace content more easily without detaching components. While slots are still in beta, this is the first step toward broader slot usage, with more improvements planned for future releases.

**Accordion**

* Update: Introduced Slot for the Accordion custom content area to support individual content

**Alert dialog:**

* Update: Introduced a slot for the Alert dialog body to support custom content without detaching the instance

**AI side panel:**

* Update: Introduced a slot for the AI side panel to enable easy swapping of panel content

**Battery indicator**

* New component: Added a new "Battery indicator" component to the design system

**Card**

* Update: Applied Opacity/Disabled to status tags in the disabled state of the spacious card

**Container**

* Update: Introduced a slot for the container to enable easy swapping of content

**Empty state**

* Update: Added a boolean property for the button component (show/hide)

**Focus mode side sheet, stackable focus mode side sheet**

* Update: Introduced a slot for the side sheets to enable easy swapping of content

**Footer**

* Archived component. While previously available in Figma, it has not been owned or maintained as part of the design system

**Hero modal**

* Update: Introduced slots for the hero area and content area to support individual content

**Media selection**

* Archived component. While previously available in Figma, it has not been owned or maintained as part of the design system

**Media tile**

* Update: Applied Opacity/Disabled to tags within the media tile in the disabled state

**Modal**

* Added hints for designers about using a modal as an overlay in prototypes

**Page header**

* Update: The Page header component for the secondary level now includes up to two tags

**Popover**

* Update: Added "Individual content / Swap me" property through Figma's property panel
* Update: Added a boolean property for showing/hiding the "Body"

**Show more**

* New: Added a "Show more" component to toggle additional content on demand. It reveals hidden information without navigating away from the current context

### Icons

* New: Adapt-Seating-Area, Adjust-Contacts, Biocopy-Lower, Biocopy-Upper, Blockout, Form-Tool-Generic, Insertion-Axis, Inspection-Window, Not-For-Diagnosis, Realign-Implant, Rotate-Around-Blank-Axis, Rotate-Around-Insertion-Axis, Scale-Tool-Generic, Shape-Circle
* Updated: Implant-Centric-View, Die

### Templates

* Sign in & empty state: Detached instances from archived components (Footer)
* Sign in: Updated "Europa" to "Europe"
* Generic second level page template now features a slot
* Wizard template reworked to include slots for content

### Documentation

**Patterns**

* New: Added pattern "[Unavailable interactions](https://zeroheight.com/0b922d40b/p/8933e5)"
* New: Added pattern "[Highlighting differences](https://zeroheight.com/0b922d40b/p/2079ba)"
* Updated: Added "Snackbar" to the "Notifications" pattern page
* Updated: Added paragraph on "Divisions" for "Slider"

**Tab**

* Updated: Removed tab wrapping description in Figma and Zeroheight documentation.

**Snackbar**

* Updated: Updated content writing guidelines.

**Inconsistency collection hub**

* New: Added [inconsistency collection hub](https://www.figma.com/board/n5Pf33h6qyUjgeUrEgA67z/Inconsistency-Collection-Hub?node-id=0-1&t=7pTg13eAca24MHW8-1) page in [Common concepts](https://www.figma.com/files/1086799668771032914/project/199101082)

---

## 0.32.0

18.02.2026

### Components

**AI side panel**

* Update: Changed font size of headline to heading.Xl. Enabled wrapping of the headline text.

**Accordion**

* New: Accordion now has a new "Compact" mode, in addition to the default "Base" mode.
* New: We added an option to add a subline underneath the headline in an accordion item
* Update: Actions and Chevron have top alignment now (previously it was middle aligned)

**Media tile**

* Update: The type tag component used in the media tile is now optional.

**Tab**

* New: Added properties "Overflow start" and "Overflow end" along with documentation on the overflow behavior
* Updated: Removed "With icon" version for tab group, changed alignment of vertical tab group to center, enabled wrapping of label for vertical tabs

**Bugs**

* Cleanup: Got rid of deprecated "ghost" variables (like Gradients/AI/Surface Transparent) still being referenced in components file

### Graphics and illustrations

* New: added "Axano" and "Axano pure"
* Updated: renamed previous "Axano" illustration to "Axano simplified"

### Documentation

* New: Added contact us page
* New: Added support channels page

---

## 0.31.0

19.12.2025

### Tokens

**Number tokens**

* Hero Modal/Width, Hero Modal/Image Width, Hero Modal/Image Height

### Components

**Focus mode side sheets, focus mode stackable side sheet**

* Update: added properties "Has headline", "Has subline" and "Has close" button, headline and close button are optional now

**New component: Hero modal**

* Hero modal is used to introduce a new feature or communicate vital changes through visual and text messages. Hero modal uses fixed-size image, and supports theming (different media for light and dark modes)

**Segmented control**

* Segmented control component now includes up to five available options for both Type=Text and Type=Icon variants
* Updated documentation notes on Figma and ZeroHeight

**Side sheet**

* Update: added properties "Has subline" and "Has close" button, close button is optional now

**User menu**

* Updated label from "Log out" to "Sign out"

### Icons

* New: Analysis-Tools, Antagonist-Distance, Bone-Lower, Bone-Upper, Clear-Model-Border, Clear-Model-Border-Off, Collaboration, Device-DS-Primescan-Neo, Device-DS-Sensor, DI-Comparison, DI-DX-Matching, Image-Unfinished, Implant-Centric-View, Label, Layers, Manual-Mapping, Mic, Path, Prepped-Tooth, Sextant, Sextant-Anterior, Sextant-Posterior-Left, Sextant-Posterior-Right, Surgical-Guide, Tooth-Smooth, Undercut, Unlink

### Graphics and illustrations

* Updated order illustrations: Order/Service/Copy Denture
* Added order denture illustrations: Flexible Partial Denture, Metal Partial Denture, Full Denture, Copy Denture, Reference Denture, Full Denture/Original, Full Denture/Light, Full Denture/Light Reddish, Full Denture/Dark Reddish, Flexible Partial Denture/Original, Flexible Partial Denture/Light, Flexible Partial Denture/Light Reddish, Flexible Partial Denture/Dark Reddish
* Updated device illustrations: Primescan 2, Dias, Primemill (renamed to Primemill 1st generation), Axeos (renamed to Primevision 3D), Axano
* Added device illustrations: Axeos Orthophos XG, Axeos Orthophos S, Axeos Orthophos E, CEREC Primemill Lite, CEREC Go, CEREC Primemill 2nd generation, InLab MC X5, Primeprint cartridge, Laptop, DAC
* Added appearance manager illustrations

### Templates

**Sign in**

* Update: renamed template from "Login" to "Sign in", changed button label to "Sign in"

### Documentation

**Patterns**

Scrolling

* Included information that scrollbar should only appear on hover over the related container (*Scrolling within components* section)

### Storybook

* Added global control to skeletonize components

---

## 0.30.1

11.11.2025

### Tokens

**Number tokens**

* New: Added "Text/Fallback Font Korean"
* Update: renamed "Text/Fallback Font" to "Text/Fallback Font Chinese"

### Components

**List**

* Update: replaced fixed spacing between color dot and headline for list items by spacing token (Spacing.Component.XS)
* Update: fixed scaling of headline in list items

**Option list**

* Update: activated "Clip content" for all option list variations

**Table**

* Update: removed interactive behavior from skeletonized table rows

### Graphics and illustrations

* Placeholder
    * Update: changed colors to use newer color tokens from the current library
* Fixed the bug of scaling the Implant bridge illustration
* Implant bridge renamed to Implant Suprastructure

---

## 0.30.0

30.10.2025

### Tokens

**Number tokens**

* New: Snackbar/Max Width, Text/Blur/blurSigmaXFactor, Text/Blur/blurSigmaYFactor
* Deprecated: Border/Radius/Side Sheet

**Color tokens**

* New: Surface/Snackbar, Action On Contrast/Hovered, Action On Contrast/Pressed, Text On Contrast/Disabled, Surface/Skeleton 1, Surface/Skeleton 2, Icon/Read Only

**Animation tokens**

* New: Animation/Duration/Snackbar Short, Animation/Duration/Snackbar Extended, Animation/Duration/Skeleton Pulse

### Components

**Generic updates**

Added a skeleton state example to affected components: Accordion, Avatar, Card, Container, Dental chart, Focus mode toolbar and side sheet, List, Media tile, Side sheet, Table, Tag

**Annotations**

* Updated Annotation components are now available through [Figma file assets](https://www.figma.com/design/oAgLpndgCMWReJ89jmSeP6/Figma-file-assets?node-id=218-2), and are no longer part of the main Components Figma file
* Completely new design of the Annotations component
* Two different types of Annotations
    * Annotations for Design System Team
        * Uses subdued background for easier recognition
        * Includes an option to select the category related to the reviewed topic
        * Includes the ability to select a Reviewer (Design System Team)
        * Includes date stamp (can be toggled off via boolean property)
    * Annotations for UX Teams
        * Uses white background
        * Includes an option to select the category related to the discussed topic
        * Includes an option to use a checkbox / check off completed tasks / confirmed items, etc. (can be toggled off via boolean property)
        * Includes the ability to select an Author (UX Team member)
        * Includes date stamp (can be toggled off via boolean property)
* Standard Informative (Blue), Positive (Green), Advisory (Orange) and Red (Not supported) examples
* Standard 12-directional positions

**Button**

* New: Variation "On Contrast" added
* Button with option list Master component: Bug fix on chevron icon state for the *Open* example [Type=Actions button (text), Open=true]

**Card**

* Bug fixes for State property where SpaciousCard had an issue that the component switches back to the State:Default after changing the *Individual content Swap me Type* on the State property through Figma property panel
    * Applied same bug fixes on other component that use the SpaciousCard as well for *Individual content Swap me Type* (Accordion, AI side sheet, Side sheet, Timeline stepper)
* Updated: Corner radius (Standard/12px) for images on *Image Type*

**Dropdown**

* Dropdown with option list Master component: Bug fix on chevron icon state for the *Open* examples

**Focus mode side sheet**

* Update: Assigned Border/Radius/Large instead of Border/Radius/Side Sheet

**Option list**

* Bug fixes on *Option list* Master components
* Bug fixes on *Individual list items* and *Option list* Master components that now reflect all component states correctly
* Bug fixes on Option list's individual items *subline* piece - now sublines are displayed in correct color: Text/Subdued
* Updated correct Auto-Layout features

**Search field**

* Added component variant "Search field with suggestions" to replace deprecated DSList. It is now possible to append the Result list to the Search field.
* Highlighting individual characters or phrases in the Result list has been added.

**Skeleton**

* New: Added components for individual skeleton shapes.

**Snackbar**

* New: Snackbar component added.

**Timeline stepper**

* New: Timeline stepper component added. It comes in 3 flavors: Activities, Workflow, and Status.

### Icons

* New: Check-Circle-Filled, Close-Circle-Filled, Cloud-Connected-Filled, Cloud-Failed-Filled, Tooth-Design, Tooth-Move, Warning-Filled, Stepper-Active
* Updated: Material-and-Device
* Updated & renamed for consistency: Tooth-Form (used to be *Form*), Tooth-Shape (used to be *Shape*)

### Templates

* Second level gallery: added skeleton loading state
* Top level table: added skeleton loading state

### Documentation

**Components**

* Popover: Added documentation on scrolling behavior

**Patterns**

* Updated loading pattern documentation

---

## 0.29.0

23.07.2025

### Tokens

Primitives

* Deprecated: dsBlueViolet, dsCarrot, dsCranberry, dsSalmon, dsViolet, dsWatermelon, dsYellow
* New: dsBrandColorBarPink, dsBrandColorBarOrange, dsBrandColorBarChartreuse

Number tokens

* New: Border/Width/AI side panel color bar, Focus Mode Stackable Side Sheet/Min Height, Side Sheet/Width/Large, Side Sheet/Width/Medium, Side Sheet/Width/Small
* New: Color dot/Size/Base added. This token controls the size of newly added Color dot component.

Color tokens

* Deprecated: Visualisation/One through Visualisation/Seven
* New: Gradients/AI side panel color bar (Stop 1–4), Gradients/AI side panel transparency (Stop 1–2)

### Components

**Generic updates**

* **Date format:** Unified the date format used in various components and examples to be dd.mm.yyyy. Also used the interpunct for combining date and time.
* **File format**: Updated file format labels to appear in capital letters with no dot at the beginning.

**AI button**

* New: Added component

**AI side panel**

* New: Added component

**Card**

* Update: fixed auto-layout behavior of tags in spacious card
* Update: changed spacing in compact card grid examples to Layout.S

**Color dot**

* New: Color dot component added

**Dropdown**

* Update: added Color dot to Dropdown component, added Filled Color multi-selection variant.

**Focus mode stackable side sheet**

* Update: Adjusted min-height

**Info modal**

* Update: Fixed bug with fading effect on the left

**List**

* Update: added variant with Color dot to every list type

**Media selection**

* Update: changed headline to "Select media"

**Media tile**

* Update: changed text for empty media tile to "Drop files here or select media"

**Option list**

* Update: added Color dot for option list items, both standard and multiselect variants.

**Side sheet**

* Update: applied tokens for widths

**Slider**

* New: Added centered variation
* Update: added guidelines

**Tag**

* New: added Color tag component
* Update: added Color dot to Removable tag, Choice tag, and Choice tag group components.

### Icons

* New: Balance, Camera-Off, Detail, Form, Fullscreen-Mode-Close, Fullscreen-Mode-Open, Hole-Visualization, Manufacturing, Material-and-Device, Pin, Set-Model-Axis, Shape, Shipping, Speed, Sprue-Cut, Sprue-Not-Thinned, Sprue-Thinned, Sprue-Wide-Thinned

### Documentation

**Slider**

* Update: added documentation

---

## 0.28.0

10.04.2025

### Tokens

Content

* New: Content/Bullet/Level 1

Number tokens

* New: Spot illustration/Size S and Spot illustration/Size M

### Components

Generic Update: removed aspect ratio spacer fix since Figma introduced the capability to lock the aspect ratio.

**Checkbox**

* New: Added missing error state combinations

**Focus mode stackable side sheet**

* Update: updated shadow and headline text style, updated documentation

**Info button**

* Update: updated guidelines and removed disabled state

**Link**

* Update: removed underline from disabled inline link

**Password field**

* Update: fixes spacing between label and field

**Tab**

* Update: fixed cropping of border indicating the selected tab

**Utilities**

* New: Added components to annotate designs

### Icons

* New: Copy Denture, Reference-Denture, Partial-Denture-Flexible, Partial-Denture-Metal, Tooth-Remove, CBCT-Cylinder, Tooth-Insights

### Graphics and illustrations

* Updated: Swapped Order/Nightguard/Scalloped and Order/Nightguard/Straight full coverage
* Updated: Devices/Primescan 2

### Templates

**Wizard**

* Updated: Fixed bug with animated wizard steps

### Documentation

**Design guidelines**

* Update: Fixed text for edge cases

**Patterns**

* New: Contextual information

---

## 0.27.0

05.02.2025

### Tokens

**Decision tokens**

* New: Text/List Spacing

**Font styles**

* Updated: Introduced "List Spacing" in all font styles. This applies a spacing between items in a bullet list.

### Components

**Empty state**

* Update: Adjusted image size and spacing, included spot illustration

**Date input**

* Update: Added property for showing optional info button

**Dropdown**

* Update: Added property for showing optional info button

**Info button**

* New: Added component

**Info modal**

* New: Added component

**Password field**

* Update: Added property for showing optional info button

**Text area**

* Update: Added property for showing optional info button

**Text field**

* Update: Added property for showing optional info button

### Graphics and illustrations

* New: added spot illustrations

---

## 0.26.0

22.01.2025

### Tokens

**Decision tokens**

* New: Image background/Standard, Image background/Selected
* Updated: Action Tertiary/Hovered, Action Tertiary/Pressed

### Components

**Compact card**

* Update: new background for compact card variation with image

### Icons

* Update: Adult, Adult-Big, Child, Teenager
* New: Cut-Back-Facial, Cut-Back-Full, Cut-Back-No, Frontal-Area, Lingual-Collar, Order-Accepted, Order-Canceled, Order-Completed, Order-In-Manufacturing, Order-In-Review, Order-On-Hold, Order-Received, Order-Rejected, Order-Sent, Pediatric, Proximal-Contacts, Redo, Undo, Without-TMJ

### Graphics and illustrations

* New: added order illustrations

### Documentation

**Generic update**

Updated selection color in Zeroheight navigation according to new selection state.

**Date input**

* Update: added documentation on date ranges

**Slider**

* Update: added documentation on usage with input field

---

## 0.25.0

03.12.2024

### Tokens

**Decision tokens**

* New: Border.Selected Standard, Border. Selected Hovered, Border. Selected Pressed
* Update: Surface Selected.Standard, Surface Selected.Hovered, Surface Selected.Pressed, Surface Selected.Disabled
* Update & deprecated: Surface Emphasized Selected.Standard, Surface Emphasized Selected.Hovered, Surface Emphasized Selected.Pressed

### Components

Generic update: enhanced selection state

**Card**

* Update: changed border color for selected states

**Dental chart**

* Update: changed border color for selected states
* Update: added variation "To be extracted" for dental chart buttons

**Tag**

* Update: changed border color for selected states

### Templates

* Wizard: Fixed summary position for responsive layout S

### Documentation

**Foundation**

* Update: Added live preview to color, elevation, radius and border page

---

## 0.24.0

22.11.2024

### Components

**Dental chart**

* Update: Fixed issue with disappearing teeth for dark theme in prototyping mode

### Graphics and illustrations

* Update: Fixed issue with disappearing teeth for dark theme in prototyping mode

### Documentation

**Generic update**

* Renamed "Responsive Web" to "Components & Templates"
* Moved "Responsive Layout" and "Responsive spacing and typography" to "Foundation"
* Moved "Patterns" to separate category

**Patterns**

* New: Visually dividing information

**Foundation**

* New: Design principles
* New: Design guidelines

---

## 0.23.0

06.11.2024

### Components

Initial release of Figma variable based library

### Templates

Initial release of Figma variable based library

### Icons

Generic update: changed icon color to new variable based color

* New: Atlantis-Fixed-Bridge, Atlantis-Fixed-Hybrid, Atlantis-Implant-Bridge, Atlantis-Removable-2in1-Bridge, Atlantis-Removable-2in1-Hybrid, Atlantis-Removable-Atlantis-Bar, Atlantis-Removable-BridgeBase, Custom-Impression-Tray, Nightguard, Partial-Framework, Restoration-Final, Restoration-Temporary, Restorative-Positions, Thermoforming-Model
* Replaced: Aligner

---

## 0.22.0

13.09.2024

### Components

**Banner promotion**

* Archived component

**Breadcrumb**

* Archived component

**Compact card**

* Update: renamed variation "Illustration" to "Image"

**Date input**

* Added close button to date picker

**Logo**

* Archived component since it has been added with the illustrations library instead

**Main menu**

* Archived sub menu items

**Pagination**

* Archived component

**Spacious card**

* Update: changed content alignment to be always vertically centered

**Wizard**

* Changed icon in top bar to close icon

### Icons

* New: Segmentation-Preset-0, Segmentation-Preset-1, Segmentation-Preset-2, Segmentation-Preset-3

### Illustrations

* New: Logo

### Templates

* Loading: archived template
* Wizard: reflected icon change in top bar, corrected spacing for responsive layout S

---

## 0.21.0

24.07.2024

### Tokens

**Decision tokens**

* Update: renamed Surface.Drop target to Surface.Dropzone
* Update: renamed Border.DropTarget to Border.Width.Dropzone

### Components

**Container**

* Remove: Dropzone variation

**Compact card**

* Update: changed vertical content alignment for "Avatar" and "Icon" variation

**Dropzone overlay**

* New: Added component

**File upload**

* Archived component: Please use media tile dropzone state and dropzone overlay instead.

**Media tile**

* Update: renamed states

**Tag**

* New: added variation "Wrapping" for choice tag group
* Update: applied fade out effect for non wrapping variation on responsive layout S

**Wizard**

* Update: wizards steps can be interactive
* Update: added documentation on scrolling behaviour

### Icons

* New: Clean-Mode, Dental-Practice, Foot-Switch, Quality-Check
* Replaced: Instructions-For-Use, Pontic
* Archived: Bluetooth, Bluetooth-Connected, Bluetooth-Failed, Bluetooth-Off

### Templates

* Wizard: added variations for large content width

### Documentation

**Patterns**

* New: Added "Upload & browse media"

---

## 0.20.0

29.05.2024

### Tokens

**Primitives**

* New: added dsBlue100Transparent48, dsChartreuse800Transparent48, dsOpacity75

**Decision tokens**

* New: added Surface.Drop Target, Opacities.OnDrag

### Components

**Card**

* Removed: simple card due to redundancy
* Update: renamed selectable card to spacious card
* New: added compact card

**Media gallery**

* Update: defined min width for individual media tiles

**Media selection**

* Update: switched from modal dialog to side sheet layout

**Media tile**

* Removed: removed component property "Scale"
* Update: updated sizing behavior so that media tiles can be resized proportionally
* Update: added property "Filled" to differentiate between media tiles that serve as dropzone and media tiles that are filled with an image
* New: added new states "Highlight", "Drop target" and "On drag"

**Table**

* New: added "Landscape" layout for table in responsive layout S
* Update: added button to switch to "Landscape" layout for existing table in responsive layout S

### Icons

* New: 3D-Calibration, Backspace, Bleaching, Dentures, Device-Cart, Device-Edge, Frontal-Skull, Instructions-For-Use, Keyboard, Map-Pin-Filled, Map-Pin, Pontic, Save, Shift, Shift-Filled, Table-Layout-Portrait, Table-Layout-Landscape
* Update: Renamed following icons for consistency
    * Backward-Outlines > Backward
    * Drop-Empty > Drop
    * Forward-Outlines > Forward
    * Pause-Outlines > Pause
    * Play-Outlines > Play
    * Laterial-Ceph > Lateral-Ceph
    * Radiation > Radiation-Filled

---

## 0.19.0

05.04.2024

### Tokens

**Primitives**

* New: added dsDuration1200 for indeterminate progress circle filled

**Decision tokens**

* New: added Border.Width.InteractiveLarge

### Components

**Dental chart**

* Update: added opacity to tooth image in disabled state

**Focus mode sheet**

* Update: added variations with different widths

**Progress circle filled**

* New: added component

**Side Sheet**

* Update: added variations with different widths

---

## 0.18.0

01.03.2024

### Tokens

**Primitives**

* New: added Opacity, added dsDuration600, added dsRadius8

**Decision tokens**

* New: added Border.Radius.Medium, added Opacities.Disabled

### Components

**Accordion**

* Update: Fixed sizing of variation with individual content

**Card**

* Update: added opacity to image in disabled state

**Dental chart**

* New: Added further tooth conditions, added read-only state for teeth, added optional tooth details (for read-only mode)
* Update: added opacity to tooth image in disabled state

**Media tile**

* Update: added opacity to image in disabled state

**Segmented control**

* Update: Adjusted styling to emphasize selection

### Icons

* Update: Renamed IPR to IPR-Upper
* New: IPR-Lower

### Templates

Top level table

* Update: fixed table on responsive layout S

### Documentation

Generic update: Checked and updated wrong/outdated examples

New: Enabled theme switch for bright and dark in the upper left

---

## 0.17.0

02.02.2024

### Components

**Accordion**

* New: variation without wrapping container
* Update: Reintroduced actions in the header, changed behavior so that only the header is interactive, optimized spacing

**Dental chart**

* Update: added selection for "With condition" state

**File upload**

* Update: added optional file size limit

**Table**

* New: variation for multi-selection
* Update: optimizations for responsive layout S (reduced spacing, added sorting option)

### Icons

* New: Abutment, Abutment-Crown, Aligner, Attachment, Attachment-Remove, Bridge, Clasp, Crown, Die, Image-Assets, Inlay, IPR-Filled, Legend, Lingual, Onlay, Prescription, Root-Canal-Treatment, Sleeve, Telescope, Tooth-Movement, Veneer
* Update: Gingiva-Mask-Lower, Gingiva-Mask-Upper

---

## 0.16.0

12.01.2024

### Components

**Slider**

* Update: aligned options to show value indicator with development, adjusted scaling behavior, provided possible values in increments of 10

**Media tile**

* Update: Quality information is now displayed as a button

**Focus mode**

* Update: Reduced spacing between toolbars and side sheets to Spacing.Layout.XS

### Documentation

**Responsive Web**

* Slider: added documentation on the behavior of the value indicator

---

## 0.15.0

27.11.2023

### Tokens

**Primitives**

* New: added dsWhiteTransparency2 - 64

**Decision tokens**

* Update: changed values of Action Tertiary/Hover and Action Tertiary/Pressed

### Components

Generic update: Exposed properties of sub-components when applicable.

**Accordion**

* Update: changed component spacing to layout spacing

**Progress circle**

* Update: added background circle

**Progress menu**

* New: added component

**User menu**

* Update: changed state to boolean property for consistency

**Top bar**

* Update: unused icon buttons are initially hidden

### Documentation

**Responsive Web**

* Media gallery: added selection mode

---

## 0.14.0

26.10.2023

### Components

Generic update: Fixed icon clipping for various components.

**Dental chart**

* Update: Fixed position of tooth condition icon in light theme

**Popover**

* Update: Fixed button position

**Table**

* Update: Cell dropdown with selection button

**Notification center**

* Update: Changed name to notification menu to align with component in code

### Icons

* New: Gingiva-Mask-Lower, Gingiva-Mask-Upper, Scan-Body-Lower, Scan-Body-Upper

### Templates

* Wizard: Added variation with summary container

### Documentation

Generic update: Split documentation into several sections (About, Foundation, Responsive Web, Mobile Native App).

**Mobile Native App**

* Added first content

**Responsive Web**

* New: Responsive spacing and typography
* Wizard: Added example with summary container
* New Pattern: Navigation
* New Pattern: Text selection

---

## 0.13.0

05.09.2023

### Tokens

* New: Added additional typography styles for responsive layout S
* New: Added chart colors (corresponding to secondary brand colors)
* Update: Adjusted all shades of dsBlue

### Components

**Generic update**

* Added optimized variation for responsive layout S for each component.

**Focus mode global options**

* Update: added spacing to the right

**Top bar**

* Removed: removed full width variations

**Wizard top bar**

* Update: Changed logo to default for resp. layout S, indented Logo by 8px for all resolution

### Icons

* Removed Gingiva-Mask and Scan-body as they will be reworked

### Templates

* Update: Switched to optimized components and layout spacings for responsive layout S
* Update: removed selection in main menu for second level pages

---

## 0.12.0

21.08.2023

### Tokens

* New: Added color styles for manufacturing materials (only in Figma kit - not exported as tokens)

### Components

**Generic update:** Applied layout spacings to various components as a preparation for responsive layout S optimizations

* Accordion, Alert Dialog, Banner promotion, Card, Container, File upload, Focus mode side sheet, Footer, Modal, Notification center, Popover, Side sheet, Table

**Main menu**

* Update: Reintroduced "Jobs"

**Wizard top bar**

* Update: Renamed "Signed in" to "Second level" and "Signed out" to "Top level", added optional user menu for "Top level" variation

### Icons

* New: Battery-Charge, Battery-Empty, Battery-Full, Battery-High, Battery-Low, Battery-Mid, Extract, Gingiva-Mask, Invoice, Keep-Gap, Lab, Lan, Payment, Plan, Scan-body, Wifi-High, Wifi-Low, Wifi-Mid

---

## 0.11.0

20.07.2023

### Components

**Generic update: Added wrapping to various components**

* Alert dialog (buttons), Card (buttons, tags), Media gallery, Modal (buttons), Page header (description and tag), Popover (buttons), Tag (filter tag group)

**Banner promotion**

* New

**Button**

* Update: fixed icon clipping for button with option list

**Container**

* New: added variation for drop target

**File upload**

* Update: updated dropzone design

**Focus mode media frame**

* Update: fixed gripper position

**Form**

* Update: removed spacing between headline and subline, changed headline to heading2Xl, fixed notification

**Image tile legacy**

* Removed

**Main menu**

* Update: Changed "Jobs" to "Treatments"

**Media tile**

* New: added variation for upload and loading
* Update: Text can wrap

**Modal**

* New: added variation for drop target

**Status tag**

* New: added variation with icon and text
* Update: set width to hug for icon tag

### Graphics and Illustrations

* New: Edge device

### Templates

**Second level gallery**

* Update: Updated tabs and buttons

**Login**

* Update: Removed spacing between headline and subline

**Wizard**

* Update: Fixed screen height for responsive layout S

### Documentation

**Button**

* Update: Added documentation on "Enabled vs. disabled buttons"

**Dropdown**

* Update: adjusted multi-selection behaviour

**Modal**

* Update: Added documentation on "Enabled vs. disabled buttons"

**Common actions**

* Update: Added documentation on "Enabled vs. disabled buttons"

---

## 0.10.1

14.06.2023

### Components

Wizard

* Update: fixed resizing bug

### Templates

Wizard

* Update: incorporated resizing bug fix

---

## 0.10.0

13.06.2023

### Tokens

* New decision tokens: Surface/Critical subdued, Surface/Information subdued, Surface/Success subdued, Surface/Warning subdued
* New text tokens: text/textLgStrongUnderline, text/textBaseStrongUnderline, text/textSmStrongUnderline, text/textXsStrongUnderline

### Components

**Alert dialog**

* Update: changed background color for emphasized variations

**Banner**

* Update: removed left color indication, assigned new background colors, adjusted spacings, replaced optional buttons by optional inline link

**Breadcrumb**

* Update: changed icon color to subdued for chevrons, changed spacing for responsive layout S

**Card**

* Update: renamed property "Has actions" to "Has toolbar"
* New: added property "Has icon overflow button"

**Dental chart**

* Update: new teeth icons, added variations for different notations, removed jaw selection

**Inline notification**

* Update: removed left color indication, assigned new background colors, adjusted spacings

**Link**

* New: added inline variation for various text sizes

**Media tile**

* New: added error state

**Tag**

* Update: renamed input tag to removable tag

**Toast**

* Update: removed left color indication, assigned new background colors, adjusted spacings

**Spacings**

* Update: fixed layout and component spacing bug (dark theme only)

### Icons

* New: introduced tags to enhance discoverability
* New: 3D, Annotations, Bite-Close, Bite-Open, Bitewing, Canvas, Color-Calibration, Color-Mode, Contact-Visualisation, Cut-Tool, Image-Quality, Pan, Service
* Update: Arch-Lower, Arch-Upper, Buccal-Left, Buccal-Right, Jaw-Full, Jaw-Lower, Jaw-Upper, Labial, Scan-Lower-Jaw, Scan-Upper-Jaw

### Graphics and Illustrations

New: added variation for ratio 3:4 for various graphics

### Templates

**Second level gallery**

* Update: fixed bug for responsive layout S

### Documentation

**Cover page**

* Update: new cover image, added shortcut tiles

**Breadcrumb**

* New

**Dental chart**

* New

**Dropdown**

* Update: max. height 6,5 entries

**Modal**

* Update: adjusted scrollbar position in overflow behavior section

**Pagination**

* New

---

## 0.9.0

03.05.2023

### Components

**Generic update on components**

* Update: Fixed icon clipping in various components

**Typography**

* New: added components for all text styles

**Focus mode wizard**

* Update: replaced chevron icons with arrow icons

**Media tile**

* Update: fixed text alignment

**Option list**

* Update: fixed icon for items with sub-menu

**Page header**

* Update: reduced spacing between headline and subline

**Product selection card**

* Removed

**Notification center**

* New: added notification center

**Table**

* Update: moved actions in value column for responsive layout S

**Wizard**

* Update: Progress bar is shown full per default, removed "Current complete" variation, replaced checkmark by step number for completed steps, included step number in current step, increased width for responsive layout M
* New: added variations for each step selected

**Layout assets: Mobile status bar**

* New: added new helper component for mobile status bar for iOS and Android

### Icons

* Update: swapped Mirror-vertical and Mirror-horizontal, fixed scaling behavior for some icons

### Graphics and Illustrations

* New: added Speedfire

### Templates

**Wizard**

* Update: Included icons within buttons, changed font size of headline

**Settings page**

* New: Added settings page

### Documentation

**Notification center**

* New

**Wizard**

* Update: updated graphics and documentation

**Patterns**

* Common actions: removed wizard example

---

## 0.8.0

03.04.2023

### Components

**Page header**

* Update: Added optional status tag for second level pages

**Progress circle**

* Update: removed inverted variation

**Top bar**

* Update: fixed icon cropping in icon buttons

**Wizard top bar**

* Update: fixed icon cropping in icon buttons

### Icons

* Update: renamed "Thumps-Down" to "Thumbs-Down"
* Removed: Minus (is redundant to "Remove")

### Graphics and Illustrations

* Update: locked source images in device illustrations

### Templates

* Update: Changed picture on login
* New: Generic second level page

### Documentation

**Generic update**

* Updated links to storybook for all components as it moved to another location

**Card**

* Update: adjusted anatomy

**Dropdown**

* Update: added description for behavior or multi-selection dropdown

**Side sheet**

* Updated example with scrollbar

**Wizard**

* Update: fixed examples

**Empty state**

* Update: fixed titles

**Patterns**

* Update: Updated animations and graphics in Interaction, Scrolling, Loading to recent design

**Scrolling**

* Update: removed table from list of scrollable components

---

## 0.7.0

20.03.2023

### Tokens

* Updated colors: Palette/dsOrange700, Palette/dsNeutralGray100, Palette/dsNeutralGray800
* Updated decision tokens: Surface Selected/Standard, Surface Selected/Hovered, Surface Selected/Pressed, Surface Selected/Disabled, Surface Neutral/Standard, Surface Neutral/Hovered, Surface Neutral/Pressed, Surface Interactive/Disabled, Surface/Critical, Surface/Information, Surface/Success, Surface/Warning, Action Primary/Disabled, Action Secondary/Disabled, Action Destructive/Disabled

### Components

**Generic update and alignment for interactive states**

* Updated disabled state: Card, Button, Checkbox, Slider, Filter tag, Choice tag, Radio button
* Introduced Shadows for selected state: Card, Tag, Filter tag, Choice tag
* Adjusted border for selected state: Card, Filter tag, Choice tag

**Container**

* New: rules for placement and formatting of headlines

**Card**

* New: responsive layout s variation for card with image

**Focus mode media frame**

* Update: added property for showing indicators, added tag for image type, changed text color for default and selected state

**Focus mode side sheet**

* Update: title and close button are displayed next to each other

**Focus mode toolbar submenu**

* Update: changed shadow to elevation3

**List**

* Update: Text small, Headline not strong

**Logo**

* Update: adjusted resizing behavior

**Segmented control**

* Update: fixed icon clipping

**Side sheet**

* Update: title and close button are displayed next to each other

**Table**

* Update: Sorting behavior

**Toast**

* Update: fixed spacing between icon and text

**Tag**

* Update: selectable tag renamed to filter tag, removable tag renamed to input tag
* New: Choice tag and choice tag row

### Icons

* Update: Renamed "Shutdown" to "Power"
* New: Diameter, Inclination-Angle, Layers-Hide, Layers-Show, Line-Width, Map, Mirror-Horizontal, Mirror-Vertical, Panoramic-Curve-Edit, Repeat

### Templates

* New: Empty state, Loading, Login

### Documentation

Initial release

---

## 0.6.0

08.02.2023

### Components

**Banner**

* Update: Fixed resizing

**Card**

* New: Variation with image for simple and selectable card
* Update: Added interaction states for simple card, changed button alignment to left, removed shadow for disabled state

**Form**

* New: added simple and complex form

**Inline notification**

* Update: fixed button size

**List**

* Update: Adjusted spacing for items, removed border for last item
* New: added selected variant

**Logo**

* New: added compact variant
* Update: exchanged DS Core logo, introduced safe-space around logos

**Main menu**

* Update: updated to recent DS CORE navigation structure

**Page header**

* Update: replaced wrong button instance (dark theme only)

**Progress bar**

* Update: changed sequence of properties

**Progress circle**

* Update: renamed component to progress circle, changed sequence of properties
* New: added animated variations, added variation "icon disabled" as this is required for the loading button
* Remove: removed medium size

**Tab**

* Update: fixed clipping issues with focus state

**Table**

* Update: changed focus border to inside for table header cell

**Tag**

* Update: Fixed icon color for removable tag

**Toast**

* Update: Fixed spacing right

**Toggle button**

* New: added variation with label and label + icon

**Top bar**

* Update: uses compact logo on resp. layout S

**Wizard**

* Update: uses compact logo on resp. layout S

### Icons

* New: Call-Video, Drop-Empty, Drop-Filled, Gamma, Hand, Image-Add, Image-Remove, Message, Message-Read, Message-Received, Message-Sent, Message-Unread, Minimize, Mirroring, Phone, Print

### Graphics and Illustrations

* New: added device illustrations

---

## 0.5.0

08.12.2022

### Components

**Generic update on interactivity / prototyping**

* Removed selection on click for the following components: Card, Checkbox, Date Input, Dental Chart, Main Menu, Media tile, Option List, Radio button, Search, Segmented Control, Tab, Table, Tag, Text area, Text field, Toggle button

**Button with option list**

* Update: all option list items contain icons

**Main menu**

* Update: replaced Dentsply Sirona logo with DS CORE logo

**Removable tag**

* Update: only the icon is interactive

**Top bar**

* New: New variation "Full width main navigation" and "Full width back navigation"
* Update: updated spacings, removed "New" button

**Wizard**

* Update: Adjusted spacing top and bottom
* New: new variations for signed in and signed out

### Icons

* Update: fixed rotation of Chevron-Up-Double, Chevron-Down-Double

---

## 0.4.0

14.11.2022

### Tokens

* New color: palette.dsBlackTransparent48
* Update: Adjusted shadows for dark theme (Shadows.elevation1-4)
* Update: Adjusted Surface.Subdued for dark theme

### Components

**Alert dialog**

* Update: changed backgrounds of all variants to Surface.Standard
* Update: changed alignment of header items to top
* New: Added variants "Critical emphasized" and "Warning emphasized"

**Button**

* New: added state "Loading"
* New: added additional variants for "Button with option list"

**Date input**

* Update: fixed resizing issues
* New: added disabled state for days

**File upload**

* Update: splitted into file upload and media selection

**Focus mode**

* Update: added example for zoom control
* Update: fixed resizing issues for annotations in dark theme

**Gallery**

* Update: renamed to "Media gallery"
* Update: activated "Show details" and "Has actions" for individual media tiles
* Update: adjusted spacing between gallery rows

**Media selection**

* Update: included remove-button for media tiles on "My computer" tab, removed checkbox

**Media tile**

* Update: introduced tags, changed initial appearance to only show title

**Modal**

* Update: changed alignment of header items to top

**Option list**

* Update: fixed cropping

**Page header**

* New: Page header

**Segmented control**

* New: Variation with three button segments

**Universal action bar**

* Update: in responsive layout S filter and sort options are combined in an icon button with option list

### Icons

* New: Chevron-Up-Double, Chevron-Down-Double
* Update: Chevron-Down, Chevron-Left, Chevron-Left-Double, Chevron-Right, Chevron-Right-Double, Chevron-Up

### Templates

* Update: Included page header in top level table and second level gallery

---

## 0.3.0

14.10.2022

### Tokens

* New colors: Border.Annotation Critical, Border.Annotation Warning, Border.Annotation Success, Border.Annotation Information
* New border primitive tokens: dsBorderWidth4, dsBorderWidth8
* New border width tokens: Border.Width.AnnotationLight, Border.Width.AnnotationMedium, Border.Width.AnnotationBold

### Components

**Date input**

* Update: changed appearance of datepicker to Flutter possibilities
* Removed: Date picker modal

**Focus mode**

* New: Annotation, Media frame, Focus mode background, Focus mode side sheet
* New: Added "Annotation" as variation of Focus mode toolbar submenu
* Updated: changed elevation of Focus mode toolbar submenu

**Media tile**

* Updated: Checkbox is also visible in default state to support touch interaction

**Option list**

* Updated: activated "Clip content" so that content gets cropped

**Side sheet**

* Removed: moved Focus mode variation to Focus mode components

### Icons

* New: Circle-Filled, Line-Light, Line-Medium, Line-Bold

---

## 0.2.1

10.10.2022

### Components

**General**

* Adjusted page background to dsNeutralGray100 for light theme and dsNeutralGray800 for dark theme
* Added in-place descriptions for components.

**Button**

* Fixed: removed unnecessary token assignments from buttons and icon buttons

**Focus mode**

* Update: fixed icon cropping for icon buttons in toolbars

**User menu**

* Update: adjusted width to fit responsive layout S
* Update: fixed crash that occurred when inserting user menu button

**Documentation assets**

* Update: spacing components are now only sized according to their spacing rectangle
* New: added component spacing XL
* New: "Hide" variant for component spacings

### Templates

**General**

* Adjusted page background to dsNeutralGray100 for light theme and dsNeutralGray800 for dark theme

---

## 0.2.0

30.09.2022

### Tokens

**Colors light theme**

* Update: Action Primary.Disabled
* Update: changed sequence of palette colors to reflect logical order

**Colors dark theme**

* Update: Surface.Contrast, Surface Selected.Standard, Surface Selected.Hover, Surface Selected.Pressed, Surface Neutral.Standard, Surface Neutral.Hovered, Surface Neutral.Pressed, Surface Interactive.Disabled, Text.Disabled, Text.On Interactive, Text.On Primary, Text.On Critical, Text.On Contrast, Border.Standard, Border, Action Primary.Disabled, Action Secondary.Standard, Action Secondary.Disabled
* New: Surface Selected.Disabled
* Removed: Navigation Selected.Standard, Navigation Selected.Hovered, Navigation Selected.Pressed

### Components

**Drawer**

* Update: renamed drawer to side sheet

**Dropdown**

* Fixed: Dropdown help text covers dropdown menu

**Empty state**

* New: Empty state medium and large

**Focus mode**

* New: Focus mode global options
* Update: Focus mode header (adjusted buttons to match current concept)

**Option list**

* Update: changed color of disabled selection state of list items

**Segmented control**

* Update: changed color of disabled selection state

**Toggle button**

* Update: changed color of disabled selection state

**User menu**

* Update: removed border for open state

**Documentation assets**

* New: Layout spacing XL

### Templates

**General**

Harmonized sequence of component variants

**Second level gallery**

Update: corrected top bar for Resp. layout S

---

## 0.1.1

26.09.2022

### Components

Fixed table row size for resp. layout S

### Templates

Nest screen layouts in frames

---

## 0.1.0

25.09.2022

Initial release.
