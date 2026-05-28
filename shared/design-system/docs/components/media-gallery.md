# Media gallery

---
title: Media gallery
url: https://zeroheight.com/0b922d40b/v/latest/p/637680-media-gallery
introduction: A gallery shows a collection of media tiles.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Media gallery: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d3931dae1db134da7ec3c3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133113Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=08e8c1e6adacbe8f546712d8ff8f7b217a96d9d3a5422c3fa3425301c393bd29)

**Media gallery: Preview**

---

## Design spec

![Media gallery: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/60a9023afb699cb87dc768?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133113Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=7532e143ea1d737c57b204a10c9eeb7f0fc3a102424f7111d630c7f775a5f23e)

**Media gallery: Design spec**

---

### Size and scaling

The media gallery stretches to the available width provided by the parent container. While the spacing between the media tiles is always fixed, the width of the tiles adjusts according to the available space.

The height of the media gallery depends on the content (number of contained media tiles).

If the parent container has a width from 584px to 1200px, the space is evenly divided into four columns. For containers with a smaller or wider width, the space is divided evenly based on a minimum width per tile (128px for small resolutions, 282px for large resolutions).

---

## Anatomy

The media gallery contains one or more sections with:

* A headline (optional)
* Media tiles

---

## Usage

Use a media gallery for a collection of graphical objects (media tiles), such as patient images.

A media gallery can be grouped by certain criteria, i.e. date or media type.

**Selection mode**

By default, clicking on a media tile opens a new view, e.g. the preview of the media. Ticking the checkbox of a media tile activates selection mode for all media tiles. In the selection mode, clicking on an entire media tile leads to the selection/deselection of the respective media tile. Furthermore, the actions in the universal action bar are replaced by actions that can be applied to the selection.

**Skeleton state**

The media gallery skeleton reflects its core layout: a single-line skeleton pill for the headline followed by a grid of media tiles in skeleton state. Each tile includes a large box-shaped placeholder for the image and pill-shaped skeletons for the title and optional subline. Interactive elements are intentionally left out to preserve a clean and neutral appearance.

### Content guidelines

* All media tiles in a gallery should either display details or not.

### Do's and don'ts

Provide a useful default grouping and sorting order, i.e. show recent media first on a patient's detail page. The headlines of the gallery sections should always reflect the selected grouping. 

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Media%20Tile%20Sliver%20Grid](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Media%20Tile%20Sliver%20Grid)

---

## Hints for designers

**Sizing**

In the media gallery, the width of the individual tiles is set to "Fill" in combination with a minimum width. If there is an incomplete row, such as the bottom row, the width for the tile in this row is set to fixed, as it would otherwise take up the entire width. As soon as the parent container is resized, the other tiles will adjust their width. The width of the tile in the incomplete row then has to be manually adjusted to this value so that all tiles are the same size again.
