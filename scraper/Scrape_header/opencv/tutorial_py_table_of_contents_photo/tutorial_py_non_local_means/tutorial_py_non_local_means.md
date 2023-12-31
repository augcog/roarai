

OpenCV: Image Denoising

 MathJax.Hub.Config({
 extensions: ["tex2jax.js", "TeX/AMSmath.js", "TeX/AMSsymbols.js"],
 jax: ["input/TeX","output/HTML-CSS"],
});
//<![CDATA[
MathJax.Hub.Config(
{
 TeX: {
 Macros: {
 matTT: [ "\\[ \\left|\\begin{array}{ccc} #1 & #2 & #3\\\\ #4 & #5 & #6\\\\ #7 & #8 & #9 \\end{array}\\right| \\]", 9],
 fork: ["\\left\\{ \\begin{array}{l l} #1 & \\mbox{#2}\\\\ #3 & \\mbox{#4}\\\\ \\end{array} \\right.", 4],
 forkthree: ["\\left\\{ \\begin{array}{l l} #1 & \\mbox{#2}\\\\ #3 & \\mbox{#4}\\\\ #5 & \\mbox{#6}\\\\ \\end{array} \\right.", 6],
 forkfour: ["\\left\\{ \\begin{array}{l l} #1 & \\mbox{#2}\\\\ #3 & \\mbox{#4}\\\\ #5 & \\mbox{#6}\\\\ #7 & \\mbox{#8}\\\\ \\end{array} \\right.", 8],
 vecthree: ["\\begin{bmatrix} #1\\\\ #2\\\\ #3 \\end{bmatrix}", 3],
 vecthreethree: ["\\begin{bmatrix} #1 & #2 & #3\\\\ #4 & #5 & #6\\\\ #7 & #8 & #9 \\end{bmatrix}", 9],
 cameramatrix: ["#1 = \\begin{bmatrix} f\_x & 0 & c\_x\\\\ 0 & f\_y & c\_y\\\\ 0 & 0 & 1 \\end{bmatrix}", 1],
 distcoeffs: ["(k\_1, k\_2, p\_1, p\_2[, k\_3[, k\_4, k\_5, k\_6 [, s\_1, s\_2, s\_3, s\_4[, \\tau\_x, \\tau\_y]]]]) \\text{ of 4, 5, 8, 12 or 14 elements}"],
 distcoeffsfisheye: ["(k\_1, k\_2, k\_3, k\_4)"],
 hdotsfor: ["\\dots", 1],
 mathbbm: ["\\mathbb{#1}", 1],
 bordermatrix: ["\\matrix{#1}", 1]
 }
 }
}
);
//]]>

 (function() {
 var cx = '002541620211387084530:kaexgxg7oxu';
 var gcse = document.createElement('script');
 gcse.type = 'text/javascript';
 gcse.async = true;
 gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
 var s = document.getElementsByTagName('script')[0];
 s.parentNode.insertBefore(gcse, s);
 })();

|  |  |
| --- | --- |
| Logo | OpenCV
 4.8.0-dev

Open Source Computer Vision |

var searchBox = new SearchBox("searchBox", "../../search",false,'Search');

$(function() {
 initMenu('../../',true,false,'search.php','Search');
 $(document).ready(function() { init\_search(); });
});

* [OpenCV-Python Tutorials](../../d6/d00/tutorial_py_root.html "../../d6/d00/tutorial_py_root.html")
* [Computational Photography](../../d0/d07/tutorial_py_table_of_contents_photo.html "../../d0/d07/tutorial_py_table_of_contents_photo.html")

Image Denoising  

## Goal

In this chapter,

* You will learn about Non-local Means Denoising algorithm to remove noise in the image.
* You will see different functions like **[cv.fastNlMeansDenoising()](../../d1/d79/group__photo__denoise.html#ga4c6b0031f56ea3f98f768881279ffe93 "Perform image denoising using Non-local Means Denoising algorithm http://www.ipol.im/pub/algo/bcm_non_local_means_denoising/ with several computational optimizations. Noise expected to be a gaussian white noise. ")**, **[cv.fastNlMeansDenoisingColored()](../../d1/d79/group__photo__denoise.html#ga03aa4189fc3e31dafd638d90de335617 "Modification of fastNlMeansDenoising function for colored images. ")** etc.

## Theory

In earlier chapters, we have seen many image smoothing techniques like Gaussian Blurring, Median Blurring etc and they were good to some extent in removing small quantities of noise. In those techniques, we took a small neighbourhood around a pixel and did some operations like gaussian weighted average, median of the values etc to replace the central element. In short, noise removal at a pixel was local to its neighbourhood.

There is a property of noise. Noise is generally considered to be a random variable with zero mean. Consider a noisy pixel, \(p = p\_0 + n\) where \(p\_0\) is the true value of pixel and \(n\) is the noise in that pixel. You can take large number of same pixels (say \(N\)) from different images and computes their average. Ideally, you should get \(p = p\_0\) since mean of noise is zero.

You can verify it yourself by a simple setup. Hold a static camera to a certain location for a couple of seconds. This will give you plenty of frames, or a lot of images of the same scene. Then write a piece of code to find the average of all the frames in the video (This should be too simple for you now ). Compare the final result and first frame. You can see reduction in noise. Unfortunately this simple method is not robust to camera and scene motions. Also often there is only one noisy image available.

So idea is simple, we need a set of similar images to average out the noise. Consider a small window (say 5x5 window) in the image. Chance is large that the same patch may be somewhere else in the image. Sometimes in a small neighbourhood around it. What about using these similar patches together and find their average? For that particular window, that is fine. See an example image below:

![nlm_patch.jpg](../../nlm_patch.jpg)

image
 The blue patches in the image looks the similar. Green patches looks similar. So we take a pixel, take small window around it, search for similar windows in the image, average all the windows and replace the pixel with the result we got. This method is Non-Local Means Denoising. It takes more time compared to blurring techniques we saw earlier, but its result is very good. More details and online demo can be found at first link in additional resources.

For color images, image is converted to CIELAB colorspace and then it separately denoise L and AB components.

## Image Denoising in OpenCV

OpenCV provides four variations of this technique.

1. **[cv.fastNlMeansDenoising()](../../d1/d79/group__photo__denoise.html#ga4c6b0031f56ea3f98f768881279ffe93 "Perform image denoising using Non-local Means Denoising algorithm http://www.ipol.im/pub/algo/bcm_non_local_means_denoising/ with several computational optimizations. Noise expected to be a gaussian white noise. ")** - works with a single grayscale images
2. **[cv.fastNlMeansDenoisingColored()](../../d1/d79/group__photo__denoise.html#ga03aa4189fc3e31dafd638d90de335617 "Modification of fastNlMeansDenoising function for colored images. ")** - works with a color image.
3. **[cv.fastNlMeansDenoisingMulti()](../../d1/d79/group__photo__denoise.html#gaf4421bf068c4d632ea7f0aa38e0bf172 "Modification of fastNlMeansDenoising function for images sequence where consecutive images have been ...")** - works with image sequence captured in short period of time (grayscale images)
4. **[cv.fastNlMeansDenoisingColoredMulti()](../../d1/d79/group__photo__denoise.html#gaa501e71f52fb2dc17ff8ca5e7d2d3619 "Modification of fastNlMeansDenoisingMulti function for colored images sequences. ")** - same as above, but for color images.

Common arguments are:

* h : parameter deciding filter strength. Higher h value removes noise better, but removes details of image also. (10 is ok)
* hForColorComponents : same as h, but for color images only. (normally same as h)
* templateWindowSize : should be odd. (recommended 7)
* searchWindowSize : should be odd. (recommended 21)

Please visit first link in additional resources for more details on these parameters.

We will demonstrate 2 and 3 here. Rest is left for you.

### 1. [cv.fastNlMeansDenoisingColored()](../../d1/d79/group__photo__denoise.html#ga03aa4189fc3e31dafd638d90de335617 "Modification of fastNlMeansDenoising function for colored images. ")

As mentioned above it is used to remove noise from color images. (Noise is expected to be gaussian). See the example below: 

import numpy as npimport cv2 as cvfrom matplotlib import pyplot as pltimg = [cv.imread](../../d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56 "../../d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56")('die.png')dst = [cv.fastNlMeansDenoisingColored](../../d1/d79/group__photo__denoise.html#ga03aa4189fc3e31dafd638d90de335617 "../../d1/d79/group__photo__denoise.html#ga03aa4189fc3e31dafd638d90de335617")(img,None,10,10,7,21)plt.subplot(121),plt.imshow(img)plt.subplot(122),plt.imshow(dst)plt.show() Below is a zoomed version of result. My input image has a gaussian noise of \(\sigma = 25\). See the result:

![nlm_result1.jpg](../../nlm_result1.jpg)

image
### 2. [cv.fastNlMeansDenoisingMulti()](../../d1/d79/group__photo__denoise.html#gaf4421bf068c4d632ea7f0aa38e0bf172 "Modification of fastNlMeansDenoising function for images sequence where consecutive images have been ...")

Now we will apply the same method to a video. The first argument is the list of noisy frames. Second argument imgToDenoiseIndex specifies which frame we need to denoise, for that we pass the index of frame in our input list. Third is the temporalWindowSize which specifies the number of nearby frames to be used for denoising. It should be odd. In that case, a total of temporalWindowSize frames are used where central frame is the frame to be denoised. For example, you passed a list of 5 frames as input. Let imgToDenoiseIndex = 2 and temporalWindowSize = 3. Then frame-1, frame-2 and frame-3 are used to denoise frame-2. Let's see an example. 

import numpy as npimport cv2 as cvfrom matplotlib import pyplot as pltcap = [cv.VideoCapture](../../d8/dfe/classcv_1_1VideoCapture.html "../../d8/dfe/classcv_1_1VideoCapture.html")('vtest.avi')# create a list of first 5 framesimg = [cap.read()[1] for i in range(5)]# convert all to grayscalegray = [[cv.cvtColor](../../d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab "../../d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab")(i, cv.COLOR\_BGR2GRAY) for i in img]# convert all to float64gray = [np.float64(i) for i in gray]# create a noise of variance 25noise = np.random.randn(\*gray[1].shape)\*10# Add this noise to imagesnoisy = [i+noise for i in gray]# Convert back to uint8noisy = [np.uint8(np.clip(i,0,255)) for i in noisy]# Denoise 3rd frame considering all the 5 framesdst = [cv.fastNlMeansDenoisingMulti](../../d1/d79/group__photo__denoise.html#ga723ffde1969430fede9241402e198151 "../../d1/d79/group__photo__denoise.html#ga723ffde1969430fede9241402e198151")(noisy, 2, 5, None, 4, 7, 35)plt.subplot(131),plt.imshow(gray[2],'gray')plt.subplot(132),plt.imshow(noisy[2],'gray')plt.subplot(133),plt.imshow(dst,'gray')plt.show() Below image shows a zoomed version of the result we got:

![nlm_multi.jpg](../../nlm_multi.jpg)

image
 It takes considerable amount of time for computation. In the result, first image is the original frame, second is the noisy one, third is the denoised image.

## Additional Resources

1. [http://www.ipol.im/pub/art/2011/bcm\_nlm/](http://www.ipol.im/pub/art/2011/bcm_nlm/ "http://www.ipol.im/pub/art/2011/bcm_nlm/") (It has the details, online demo etc. Highly recommended to visit. Our test image is generated from this link)
2. [Online course at coursera](https://www.coursera.org/course/images "https://www.coursera.org/course/images") (First image taken from here)

## Exercises

---

Generated on Wed Oct 4 2023 23:37:11 for OpenCV by  [![doxygen](../../doxygen.png)](http://www.doxygen.org/index.html "http://www.doxygen.org/index.html") 1.8.13

//<![CDATA[
addTutorialsButtons();
//]]>

