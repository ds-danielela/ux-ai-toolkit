# Dropzone overlay

---
title: Dropzone overlay
url: https://zeroheight.com/0b922d40b/v/latest/p/035be5-dropzone-overlay
introduction: The dropzone overlay indicates an area that accepts dropping of files.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Dropzone overlay: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/852ae78bc44c0e15884fab?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133105Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=59f4695d4a66359632e820fed98167a7965c5392a5531b0ff122552e8efe0060)

**Dropzone overlay: Preview**

---

## Design spec

![Dropzone overlay: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e414e1938714b4a5973901?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133105Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=fc8f9e03b8326e550ab7d6ca95d7f1fd5cc9178a045f0dd4e0ebcefd5d78f7c7)

**Dropzone overlay: Design spec**

---

### Size and scaling

The dropzone overlay stretches to the height and width of the respective area that accepts dropping of files (i.e. a container).

The width of the instruction at the bottom depends on the content and should respect a minimum distance to the edge of the overlay. If the text does not fit, it starts to wrap into another row.

---

## Anatomy

The dropzone overlay contains a semitransparent area (1) and an instruction at the bottom (2).

---

## Usage

The dropzone overlay appears, as soon as a file is dragged over an area (i.e. a container) that accepts file drops.

If the container is not fully visible, the instruction should be pinned at the bottom of the screen.

### Content guidelines

* The instruction should clearly communicate what happens to the dropped files.

### Do's and don'ts

If an area that accepts file drops does not contain any files yet, provide an empty state with clear instructions.

Only use the dropzone overlay if multiple files can be dropped in an unorganized way. If specific files are required, that need to be provided in a structured way, use the media tile dropzone instead.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Private/Dropzone%20overlay](https://storybook-coreui-d2-euw3.d.dscore.com/#/Private/Dropzone%20overlay)
