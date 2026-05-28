# Container

---
title: Container
url: https://zeroheight.com/0b922d40b/v/latest/p/24be69-container
introduction: Containers logically group ui components, such as tiles, etc. Unlike cards, containers are not interactive, but can contain actions.
---

| Design (Figma Toolkit) | Code (Storybook) |
| --- | --- |
| ✅ | ✅ |

![Container: Preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/5b411968bcf0b93a462624?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133108Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=f5a5242f84463484f35c4e4ad5fd734589f5a88d3ce499f4e8aa14f10eed0890)

**Container: Preview**

---

## Design spec

![Container: Design spec](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3dc206821a32f095df71d9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133108Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=e27e0002fdb68252f5aec64a1e6f6982c2b607cbb08f9c6155ffba4e7eb8a259)

**Container: Design spec**

---

### Size and scaling

The height of the container usually depends on the content but can also be stretched to the parent container. The width of the container usually stretches to the width of its parent container (among several responsive layout columns). 

---

## Anatomy

The container is a rounded box (1) that wraps other components (2), like i.e. a table, list, form etc. 

---

## Usage

Use a container to logically enclose related content like a form, gallery, etc.

**Please note:** Some components, like tables and lists and accordions are already wrapped in a container. 

**Container headlines**

The placement of the container headline and its formatting depend on the context.

A wizard step consists of one container. The headline is positioned at the top within the container and uses the text style **Text.heading2xl**.  

If there is only one large container on a basic page, e.g. a media gallery or table, the page header or tabs represent the headline. 

If a page contains multiple containers, the headline (if needed) should be placed inside the containers and uses the text style **Text.headingXl**. 

If further structuring is required, headlines can be used to separate groups of containers.  

**Skeleton state**

The container component adapts its skeleton state based on the content it holds. To maintain clarity and reduce visual noise, only essential structural elements are represented using simplified skeleton shapes. Static elements—such as known headlines—should remain visible to improve perceived performance and layout stability. Interactive elements—such as buttons or form controls—are removed during loading to avoid misleading affordances. Nested components (e.g., avatars, dental chart) should use their own dedicated skeleton styles to ensure consistency across the system.

### Content guidelines

* Only related information should be wrapped within one container.

### Do's and don'ts

Containers themselves are not clickable. To provide actions, you can offer buttons inside containers.

To provide multiple actions or a choice of options, you can wrap cards within a container.

---

## Live preview

[https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Container](https://storybook-coreui-d2-euw3.d.dscore.com/#/Components/Container)
