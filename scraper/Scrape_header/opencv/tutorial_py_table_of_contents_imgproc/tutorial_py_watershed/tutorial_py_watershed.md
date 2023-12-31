

OpenCV: Image Segmentation with Watershed Algorithm

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
* [Image Processing in OpenCV](../../d2/d96/tutorial_py_table_of_contents_imgproc.html "../../d2/d96/tutorial_py_table_of_contents_imgproc.html")

Image Segmentation with Watershed Algorithm  

## Goal

In this chapter,

* We will learn to use marker-based image segmentation using watershed algorithm
* We will see: **[cv.watershed()](../../d3/d47/group__imgproc__segmentation.html#ga3267243e4d3f95165d55a618c65ac6e1 "Performs a marker-based image segmentation using the watershed algorithm. ")**

## Theory

Any grayscale image can be viewed as a topographic surface where high intensity denotes peaks and hills while low intensity denotes valleys. You start filling every isolated valleys (local minima) with different colored water (labels). As the water rises, depending on the peaks (gradients) nearby, water from different valleys, obviously with different colors will start to merge. To avoid that, you build barriers in the locations where water merges. You continue the work of filling water and building barriers until all the peaks are under water. Then the barriers you created gives you the segmentation result. This is the "philosophy" behind the watershed. You can visit the [CMM webpage on watershed](http://cmm.ensmp.fr/~beucher/wtshed.html "http://cmm.ensmp.fr/~beucher/wtshed.html") to understand it with the help of some animations.

But this approach gives you oversegmented result due to noise or any other irregularities in the image. So OpenCV implemented a marker-based watershed algorithm where you specify which are all valley points are to be merged and which are not. It is an interactive image segmentation. What we do is to give different labels for our object we know. Label the region which we are sure of being the foreground or object with one color (or intensity), label the region which we are sure of being background or non-object with another color and finally the region which we are not sure of anything, label it with 0. That is our marker. Then apply watershed algorithm. Then our marker will be updated with the labels we gave, and the boundaries of objects will have a value of -1.

## Code

Below we will see an example on how to use the Distance Transform along with watershed to segment mutually touching objects.

Consider the coins image below, the coins are touching each other. Even if you threshold it, it will be touching each other.

![water_coins.jpg](../../water_coins.jpg)

image
 We start with finding an approximate estimate of the coins. For that, we can use the Otsu's binarization. 

import numpy as npimport cv2 as cvfrom matplotlib import pyplot as pltimg = [cv.imread](../../d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56 "../../d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56")('coins.png')assert img is not None, "file could not be read, check with os.path.exists()"gray = [cv.cvtColor](../../d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab "../../d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab")(img,cv.COLOR\_BGR2GRAY)ret, thresh = [cv.threshold](../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57 "../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57")(gray,0,255,cv.THRESH\_BINARY\_INV+cv.THRESH\_OTSU) Result:

![water_thresh.jpg](../../water_thresh.jpg)

image
 Now we need to remove any small white noises in the image. For that we can use morphological opening. To remove any small holes in the object, we can use morphological closing. So, now we know for sure that region near to center of objects are foreground and region much away from the object are background. Only region we are not sure is the boundary region of coins.

So we need to extract the area which we are sure they are coins. Erosion removes the boundary pixels. So whatever remaining, we can be sure it is coin. That would work if objects were not touching each other. But since they are touching each other, another good option would be to find the distance transform and apply a proper threshold. Next we need to find the area which we are sure they are not coins. For that, we dilate the result. Dilation increases object boundary to background. This way, we can make sure whatever region in background in result is really a background, since boundary region is removed. See the image below.

![water_fgbg.jpg](../../water_fgbg.jpg)

image
 The remaining regions are those which we don't have any idea, whether it is coins or background. Watershed algorithm should find it. These areas are normally around the boundaries of coins where foreground and background meet (Or even two different coins meet). We call it border. It can be obtained from subtracting sure\_fg area from sure\_bg area. 

# noise removalkernel = np.ones((3,3),np.uint8)opening = [cv.morphologyEx](../../d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f "../../d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f")(thresh,cv.MORPH\_OPEN,kernel, iterations = 2)# sure background areasure\_bg = [cv.dilate](../../d4/d86/group__imgproc__filter.html#ga4ff0f3318642c4f469d0e11f242f3b6c "../../d4/d86/group__imgproc__filter.html#ga4ff0f3318642c4f469d0e11f242f3b6c")(opening,kernel,iterations=3)# Finding sure foreground areadist\_transform = [cv.distanceTransform](../../d7/d1b/group__imgproc__misc.html#ga25c259e7e2fa2ac70de4606ea800f12f "../../d7/d1b/group__imgproc__misc.html#ga25c259e7e2fa2ac70de4606ea800f12f")(opening,cv.DIST\_L2,5)ret, sure\_fg = [cv.threshold](../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57 "../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57")(dist\_transform,0.7\*dist\_transform.max(),255,0)# Finding unknown regionsure\_fg = np.uint8(sure\_fg)unknown = [cv.subtract](../../d2/de8/group__core__array.html#gaa0f00d98b4b5edeaeb7b8333b2de353b "../../d2/de8/group__core__array.html#gaa0f00d98b4b5edeaeb7b8333b2de353b")(sure\_bg,sure\_fg) See the result. In the thresholded image, we get some regions of coins which we are sure of coins and they are detached now. (In some cases, you may be interested in only foreground segmentation, not in separating the mutually touching objects. In that case, you need not use distance transform, just erosion is sufficient. Erosion is just another method to extract sure foreground area, that's all.)

![water_dt.jpg](../../water_dt.jpg)

image
 Now we know for sure which are region of coins, which are background and all. So we create marker (it is an array of same size as that of original image, but with int32 datatype) and label the regions inside it. The regions we know for sure (whether foreground or background) are labelled with any positive integers, but different integers, and the area we don't know for sure are just left as zero. For this we use **[cv.connectedComponents()](../../d3/dc0/group__imgproc__shape.html#gaedef8c7340499ca391d459122e51bef5 "computes the connected components labeled image of boolean image ")**. It labels background of the image with 0, then other objects are labelled with integers starting from 1.

But we know that if background is marked with 0, watershed will consider it as unknown area. So we want to mark it with different integer. Instead, we will mark unknown region, defined by unknown, with 0. 

# Marker labellingret, markers = [cv.connectedComponents](../../d3/dc0/group__imgproc__shape.html#gac2718a64ade63475425558aa669a943a "../../d3/dc0/group__imgproc__shape.html#gac2718a64ade63475425558aa669a943a")(sure\_fg)# Add one to all labels so that sure background is not 0, but 1markers = markers+1# Now, mark the region of unknown with zeromarkers[unknown==255] = 0 See the result shown in JET colormap. The dark blue region shows unknown region. Sure coins are colored with different values. Remaining area which are sure background are shown in lighter blue compared to unknown region.

![water_marker.jpg](../../water_marker.jpg)

image
 Now our marker is ready. It is time for final step, apply watershed. Then marker image will be modified. The boundary region will be marked with -1. 

markers = [cv.watershed](../../d3/d47/group__imgproc__segmentation.html#ga3267243e4d3f95165d55a618c65ac6e1 "../../d3/d47/group__imgproc__segmentation.html#ga3267243e4d3f95165d55a618c65ac6e1")(img,markers)img[markers == -1] = [255,0,0] See the result below. For some coins, the region where they touch are segmented properly and for some, they are not.

![water_result.jpg](../../water_result.jpg)

image
## Additional Resources

1. CMM page on [Watershed Transformation](http://cmm.ensmp.fr/~beucher/wtshed.html "http://cmm.ensmp.fr/~beucher/wtshed.html")

## Exercises

1. OpenCV samples has an interactive sample on watershed segmentation, watershed.py. Run it, Enjoy it, then learn it.

---

Generated on Wed Oct 4 2023 23:37:11 for OpenCV by  [![doxygen](../../doxygen.png)](http://www.doxygen.org/index.html "http://www.doxygen.org/index.html") 1.8.13

//<![CDATA[
addTutorialsButtons();
//]]>

