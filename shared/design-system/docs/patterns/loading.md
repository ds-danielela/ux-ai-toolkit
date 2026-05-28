# Loading

**URL:** https://zeroheight.com/0b922d40b/v/latest/p/761fa1-loading

**Introduction:** If information takes an extended period of time to process or appear, we introduce a loading pattern to the user. Loading components visually help the user understand the experience is currently in a loading state. These loading states help assure to the user that progress is being made and even creates a sense of shorter load times.

---

## Usage

Use loading components to visually help the user understand the experience is currently in a loading state. Consider the context and use case when you choose an appropriate pattern for communicating the loading state.

### Full screen loading

**Navigating to another view (context switch)**

When navigating to another view, i.e. opening media from the patient details page, the application switches the view immediately. Loading skeletons are displayed until the content is loaded completely (see [skeleton](https://zeroheight.com/0b922d40b/p/953907)).

![](https://zeroheight-user-uploads.s3.eu-west-1.amazonaws.com/images/rbaS0CsYQNi5qTF9JhJhww.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=cc6fae1c9e1f07299ab7ed9a5ce1b8be7e810ec529ba09a4f5fe84a000ef3945)

**Navigating to another page on the same view (no context switch)**

When navigating to another page in the same view, i.e. navigating from Patients to Orders, the application switches the page immediately. Loading skeletons are displayed until the content is loaded completely (see [skeleton](https://zeroheight.com/0b922d40b/p/953907)).

![](https://zeroheight-user-uploads.s3.eu-west-1.amazonaws.com/images/y9DQ3f2GmsaTu6VUGVnUdQ.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=67754aaaa8565c5a6f7472e53bd915375cbe0abb8ddb3380f2a13a43e8f4bf68)

### Submitting

When processing a form, the button loading state should be used. This state shows a progress circle within the button.

The following example shows submitting a form presented in a modal dialog.

![](https://zeroheight-user-uploads.s3.eu-west-1.amazonaws.com/images/ku8BKIdydEC7jgcr13MDSQ.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d8feff78a65b5d88d62a707858b916f4eff6f251e6b0f9f99a3d6a2af3c97fc6)

Forms can also be placed within containers on a page. While initially the content is read only, the user can activate an editing mode. When submitting the editing mode, the button also shows a loading state.

![](https://zeroheight-user-uploads.s3.eu-west-1.amazonaws.com/images/xvBYzadyF4jus15ms8dsyA.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=fa309e9b6c32a65a8aeb938daebc0e8defe47219fc7951e952675bc5072b8448)

### Loading 3D content

Since adding 3D media may take several seconds, a determinate progress bar is displayed in this case.

![](https://zeroheight-user-uploads.s3.eu-west-1.amazonaws.com/images/AKKCeOUk1pblKRmavtbRLA.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=6ac9f53dfd3221e11bc55ab97d643f09633ce2ba18534ddfb9a74feb3e28a6ab)

### Progressive loading

When the user scrolls a page with a table that is not fully loaded, an indeterminate progress circle will be shown below the last loaded table row.

![](https://zeroheight-user-uploads.s3.eu-west-1.amazonaws.com/images/IMO0Z-sdxAZ8dUCdyYcb6g.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=26220686438d168d3cadaad9077bf7f06998bedb1c9abdeb5762e8da5a73cb64)

The same applies when the user scrolls a list within a container: an indeterminate progress circle will be shown below the last loaded content.

![](https://zeroheight-user-uploads.s3.eu-west-1.amazonaws.com/images/FMTvNd_XBwnTKgNp0pVKHA.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=c0a390dc989a5c192f6b2b0d9d00733511cec239ff60426ac340324d692fe110)

### Do's and Don'ts

Use the skeleton state for the initial page loading. Do not show multiple progress circles on one screen.

| Rule | Image | Caption | Description |
| :--- | :--- | :--- | :--- |
| Do | ![](https://zeroheight-user-uploads.s3.eu-west-1.amazonaws.com/images/12uhfoD7C4NQQO91L2Y36g.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=bf4286a0af0965ae309dfb31ec94f751455bf1c0b5413b39172c4ef45667de80) |   |   |
| Don't | ![](https://zeroheight-user-uploads.s3.eu-west-1.amazonaws.com/images/L3_YBE7-MbfHFFug6ZnZvA.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQK6SJI2PWU%2F20260508%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T133043Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=3df3313638c0f79ed083dd0015097af699f14151411e12df3d7da0fd0f4c731c) |   |   |
