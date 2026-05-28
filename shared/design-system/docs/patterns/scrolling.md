# Scrolling

**URL:** https://zeroheight.com/0b922d40b/v/latest/p/744c9a-scrolling

**Introduction:** Different scrolling patterns affect how page content behaves when scrolling.

---

## Usage

### Page scrolling

In most cases the page is scrollable as a whole.

In this case the user can scroll by using the scrollbar or by using the system specific scroll gesture on the page content area.

![Scrolling: Area](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2f9ea9d5356c18628eb5b9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133045Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=b9a9e8b36ac09737b54830d08b7e15aa6130c583348c736ad7d4d8729e0d20d0)

**Scrolling: Area**

---

**Sticky components**

By default, the top bar is always sticky. This means that content slides underneath it when the user scrolls.

![](https://zeroheight-user-uploads.s3.eu-west-1.amazonaws.com/images/FHhKUEj47T8X8ImbZ-SaOw.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133045Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=5feb0766cb02759ef5bd709ce50dc4ceb1e3d375b78380e004a74364010702ca)

In order to still provide the user with orientation and access to critical functions while scrolling, additional UI components can be sticky:

* [Page header](https://zeroheight.com/0b922d40b/p/788503)
* [Tabs](https://zeroheight.com/0b922d40b/p/05c87c)
* [Universal action bar](https://zeroheight.com/0b922d40b/p/983afa)

**Please note:** While top bar, tabs and universal action bar do not change the appearance when scrolling, the page headers appearance is reduced for optimizing the space for the content (see [page header](https://zeroheight.com/0b922d40b/p/788503)).

The following example shows a media gallery in which the page header, universal action bar, and tabs remain sticky. When switching to another tab, the scroll state of the whole page is preserved (the page header appearance remains reduced).

![](https://zeroheight-user-uploads.s3.eu-west-1.amazonaws.com/images/g94BHa9OHkLPToefvguWzg.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133045Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=430859df78983242949963a5678bf66c167495a70b9a4cff3b396b071ffe7ae1)

### Scrolling within components

Individual components can also be scrollable, as listed below. Scrollbar should only appear when the user hovers over the respective area of the container.

Components that support internal scrolling:

* [Accordion item](https://zeroheight.com/0b922d40b/p/435154-accordion)
* [Container](https://zeroheight.com/0b922d40b/p/24be69-container)
* [Main menu](https://zeroheight.com/0b922d40b/p/813a83-main-menu)
* [Modal](https://zeroheight.com/0b922d40b/p/51c11c-modal)
* [Option list](https://zeroheight.com/0b922d40b/p/08a681-option-list)
* [Popover](https://zeroheight.com/0b922d40b/p/257994-popover)
* [Side sheet](https://zeroheight.com/0b922d40b/p/7675c3-side-sheet)
* [Text area](https://zeroheight.com/0b922d40b/p/87c9c9-text-area)

### Do's and Don'ts

When using sticky UI components, make sure that all components above are also sticky in order not to confuse the user.

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Don't | ![](https://zeroheight-user-uploads.s3.eu-west-1.amazonaws.com/images/GzppzvFLg3K45Rx0IveTOg.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133045Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=f882a6c037e5d1c98fb43060b393031c79f0ccd8ab830b4a69170ffda7a2931c) |   |   |
