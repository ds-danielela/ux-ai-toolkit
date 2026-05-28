# Media tile

---
title: Media tile
url: https://zeroheight.com/0b922d40b/v/latest/p/35ddbc-media-tile
introduction: Media tiles can be used to list graphical objects, such as patient images, etc.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Media tile: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/aaddbc52ed265770f85478?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133114Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=e643253ff793ce827f8fa07dc643cbbc3c82137d5ceaa08baa8bcff25c103674)

**Media tile: Preview**

---

## Design spec

![Media tile: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/20229151f7543511dcdead?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133114Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=f2ce1cd458483139bbb68af0b5d18a17ade949118cb6563564ca23d414be419f)

**Media tile: Design spec**

---

### Size and scaling

The size of the media tile depends on the available space provided by the parent container (see media gallery).

If the text does not fit, it can wrap.

The image thumbnail itself should always be square. If necessary, the original image will be cropped horizontally or vertically from the center depending on its orientation.

---

## Anatomy

A filled media tile contains the following elements:

1. Image thumbnail
2. Tag for the image type (optional)
3. Checkbox for selection (optional)
4. Label
5. Sublabel (optional)
6. Prominent action (optional - for Quality info of DI scans)
7. Actions (optional)

A media tile can also be empty and serve as a dropzone. In that case it contains the following elements:

1. Dashed border
2. Instruction
3. Link to open the media selection
4. Progress circle while uploading

If no image is available, an icon can be shown instead. 

In case of an error, the media tile is highlighted with a red border (1). A status tag with icon is displayed on the left (2). The status tag should display a tooltip with the error message (3).

**Skeleton state**

The media tile is represented by a simplified layout that reflects its core structure: a large box-shaped skeleton for the image, followed by pill-shaped skeletons for the title and, if present, the subline. All interactive elements—such as buttons, checkboxes, and tags—are omitted to maintain a clean and neutral appearance.

---

## Usage

Use a media tile to list graphical objects, such as patient images. Media tiles are usually part of a gallery.

A media tile can have one or more actions. In case of more than one action, the button reveals all options in an option list. 

### Content guidelines

* All media tiles in a gallery should either display details or not.

### Do's and don'ts

Only use media tiles for listing graphical objects, such as patient images. Do not use them for listing actions or similar.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Media%20Tile](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Media%20Tile)

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Media%20Tile%20Empty%20Dropzone](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Media%20Tile%20Empty%20Dropzone)

---

## Hints for designers

**Sizing**

Since version 0.20.0 of the Figma toolkit, media tiles can be scaled proportionally. When inserting an individual tile from the library, the width is set to fixed. If you would like to combine multiple media tiles in a grid, you can wrap them in an auto-layout. If you set the width of the individual tiles to "Fill", their width will respond to the width of the parent container.
