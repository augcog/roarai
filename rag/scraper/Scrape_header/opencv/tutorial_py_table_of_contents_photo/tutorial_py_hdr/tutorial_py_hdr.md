
## Goal

In this chapter, we will

* Learn how to generate and display HDR image from an exposure sequence.
* Use exposure fusion to merge an exposure sequence.

## Theory

High-dynamic-range imaging (HDRI or HDR) is a technique used in imaging and photography to reproduce a greater dynamic range of luminosity than is possible with standard digital imaging or photographic techniques. While the human eye can adjust to a wide range of light conditions, most imaging devices use 8-bits per channel, so we are limited to only 256 levels. When we take photographs of a real world scene, bright regions may be overexposed, while the dark ones may be underexposed, so we canât capture all details using a single exposure. HDR imaging works with images that use more than 8 bits per channel (usually 32-bit float values), allowing much wider dynamic range.

There are different ways to obtain HDR images, but the most common one is to use photographs of the scene taken with different exposure values. To combine these exposures it is useful to know your cameraâs response function and there are algorithms to estimate it. After the HDR image has been merged, it has to be converted back to 8-bit to view it on usual displays. This process is called tonemapping. Additional complexities arise when objects of the scene or camera move between shots, since images with different exposures should be registered and aligned.

In this tutorial we show 2 algorithms (Debevec, Robertson) to generate and display HDR image from an exposure sequence, and demonstrate an alternative approach called exposure fusion (Mertens), that produces low dynamic range image and does not need the exposure times data. Furthermore, we estimate the camera response function (CRF) which is of great value for many computer vision algorithms. Each step of HDR pipeline can be implemented using different algorithms and parameters, so take a look at the reference manual to see them all.

## Exposure sequence HDR

In this tutorial we will look on the following scene, where we have 4 exposure images, with exposure times of: 15, 2.5, 1/4 and 1/30 seconds. (You can download the images from [Wikipedia](https://en.wikipedia.org/wiki/High-dynamic-range_imaging "https://en.wikipedia.org/wiki/High-dynamic-range_imaging"))

![exposures.jpg](../../exposures.jpg)

image
### 1. Loading exposure images into a list

The first stage is simply loading all images into a list. In addition, we will need the exposure times for the regular HDR algorithms. Pay attention for the data types, as the images should be 1-channel or 3-channels 8-bit (np.uint8) and the exposure times need to be float32 and in seconds.

import cv2 as cvimport numpy as np# Loading exposure images into a listimg\_fn = ["img0.jpg", "img1.jpg", "img2.jpg", "img3.jpg"]img\_list = [[cv.imread](../../d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56 "../../d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56")(fn) for fn in img\_fn]exposure\_times = np.array([15.0, 2.5, 0.25, 0.0333], dtype=np.float32)### 2. Merge exposures into HDR image

In this stage we merge the exposure sequence into one HDR image, showing 2 possibilities which we have in OpenCV. The first method is Debevec and the second one is Robertson. Notice that the HDR image is of type float32, and not uint8, as it contains the full dynamic range of all exposure images.

# Merge exposures to HDR imagemerge\_debevec = [cv.createMergeDebevec](../../d6/df5/group__photo__hdr.html#gaa8eab36bc764abb2a225db7c945f87f9 "../../d6/df5/group__photo__hdr.html#gaa8eab36bc764abb2a225db7c945f87f9")()hdr\_debevec = merge\_debevec.process(img\_list, times=exposure\_times.copy())merge\_robertson = [cv.createMergeRobertson](../../d6/df5/group__photo__hdr.html#ga460d4a1df1a7e8cdcf7445bb87a8fb78 "../../d6/df5/group__photo__hdr.html#ga460d4a1df1a7e8cdcf7445bb87a8fb78")()hdr\_robertson = merge\_robertson.process(img\_list, times=exposure\_times.copy())### 3. Tonemap HDR image

We map the 32-bit float HDR data into the range [0..1]. Actually, in some cases the values can be larger than 1 or lower the 0, so notice we will later have to clip the data in order to avoid overflow.

# Tonemap HDR imagetonemap1 = [cv.createTonemap](../../d6/df5/group__photo__hdr.html#gabcbd653140b93a1fa87ccce94548cd0d "../../d6/df5/group__photo__hdr.html#gabcbd653140b93a1fa87ccce94548cd0d")(gamma=2.2)res\_debevec = tonemap1.process(hdr\_debevec.copy())### 4. Merge exposures using Mertens fusion

Here we show an alternative algorithm to merge the exposure images, where we do not need the exposure times. We also do not need to use any tonemap algorithm because the Mertens algorithm already gives us the result in the range of [0..1].

# Exposure fusion using Mertensmerge\_mertens = [cv.createMergeMertens](../../d6/df5/group__photo__hdr.html#ga79d59aa3cb3a7c664e59a4b5acc1ccb6 "../../d6/df5/group__photo__hdr.html#ga79d59aa3cb3a7c664e59a4b5acc1ccb6")()res\_mertens = merge\_mertens.process(img\_list)### 5. Convert to 8-bit and save

In order to save or display the results, we need to convert the data into 8-bit integers in the range of [0..255].

# Convert datatype to 8-bit and saveres\_debevec\_8bit = np.clip(res\_debevec\*255, 0, 255).astype('uint8')res\_robertson\_8bit = np.clip(res\_robertson\*255, 0, 255).astype('uint8')res\_mertens\_8bit = np.clip(res\_mertens\*255, 0, 255).astype('uint8')[cv.imwrite](../../d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce "../../d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce")("ldr\_debevec.jpg", res\_debevec\_8bit)[cv.imwrite](../../d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce "../../d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce")("ldr\_robertson.jpg", res\_robertson\_8bit)[cv.imwrite](../../d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce "../../d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce")("fusion\_mertens.jpg", res\_mertens\_8bit)## Results

You can see the different results but consider that each algorithm have additional extra parameters that you should fit to get your desired outcome. Best practice is to try the different methods and see which one performs best for your scene.

### Debevec:

![ldr_debevec.jpg](../../ldr_debevec.jpg)

image
### Robertson:

![ldr_robertson.jpg](../../ldr_robertson.jpg)

image
### Mertenes Fusion:

![fusion_mertens.jpg](../../fusion_mertens.jpg)

image
## Estimating Camera Response Function

The camera response function (CRF) gives us the connection between the scene radiance to the measured intensity values. The CRF if of great importance in some computer vision algorithms, including HDR algorithms. Here we estimate the inverse camera response function and use it for the HDR merge.

# Estimate camera response function (CRF)cal\_debevec = [cv.createCalibrateDebevec](../../d6/df5/group__photo__hdr.html#ga7fed9707ad5f2cc0e633888867109f90 "../../d6/df5/group__photo__hdr.html#ga7fed9707ad5f2cc0e633888867109f90")()crf\_debevec = cal\_debevec.process(img\_list, times=exposure\_times)hdr\_debevec = merge\_debevec.process(img\_list, times=exposure\_times.copy(), response=crf\_debevec.copy())cal\_robertson = [cv.createCalibrateRobertson](../../d6/df5/group__photo__hdr.html#gae77813a21cd351a596619e5ff013be5d "../../d6/df5/group__photo__hdr.html#gae77813a21cd351a596619e5ff013be5d")()crf\_robertson = cal\_robertson.process(img\_list, times=exposure\_times)hdr\_robertson = merge\_robertson.process(img\_list, times=exposure\_times.copy(), response=crf\_robertson.copy())The camera response function is represented by a 256-length vector for each color channel. For this sequence we got the following estimation:

![crf.jpg](../../crf.jpg)

image
## Additional Resources

1. Paul E Debevec and Jitendra Malik. Recovering high dynamic range radiance maps from photographs. In ACM SIGGRAPH 2008 classes, page 31. ACM, 2008. [[66]](../../d0/de3/citelist.html#CITEREF_DM97 "../../d0/de3/citelist.html#CITEREF_DM97")
2. Mark A Robertson, Sean Borman, and Robert L Stevenson. Dynamic range improvement through multiple exposures. In Image Processing, 1999. ICIP 99. Proceedings. 1999 International Conference on, volume 3, pages 159â163. IEEE, 1999. [[222]](../../d0/de3/citelist.html#CITEREF_RB99 "../../d0/de3/citelist.html#CITEREF_RB99")
3. Tom Mertens, Jan Kautz, and Frank Van Reeth. Exposure fusion. In Computer Graphics and Applications, 2007. PG'07. 15th Pacific Conference on, pages 382â390. IEEE, 2007. [[184]](../../d0/de3/citelist.html#CITEREF_MK07 "../../d0/de3/citelist.html#CITEREF_MK07")
4. Images from [Wikipedia-HDR](https://en.wikipedia.org/wiki/High-dynamic-range_imaging "https://en.wikipedia.org/wiki/High-dynamic-range_imaging")

## Exercises

1. Try all tonemap algorithms: [cv::TonemapDrago](../../da/d53/classcv_1_1TonemapDrago.html "Adaptive logarithmic mapping is a fast global tonemapping algorithm that scales the image in logarith..."), [cv::TonemapMantiuk](../../de/d76/classcv_1_1TonemapMantiuk.html "This algorithm transforms image to contrast using gradients on all levels of gaussian pyramid...") and [cv::TonemapReinhard](../../d0/dec/classcv_1_1TonemapReinhard.html "This is a global tonemapping operator that models human visual system. ")
2. Try changing the parameters in the HDR calibration and tonemap methods.

