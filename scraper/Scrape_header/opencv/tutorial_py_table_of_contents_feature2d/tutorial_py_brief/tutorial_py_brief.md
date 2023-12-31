

OpenCV: BRIEF (Binary Robust Independent Elementary Features)

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
* [Feature Detection and Description](../../db/d27/tutorial_py_table_of_contents_feature2d.html "../../db/d27/tutorial_py_table_of_contents_feature2d.html")

BRIEF (Binary Robust Independent Elementary Features)  

## Goal

In this chapter

* We will see the basics of BRIEF algorithm

## Theory

We know SIFT uses 128-dim vector for descriptors. Since it is using floating point numbers, it takes basically 512 bytes. Similarly SURF also takes minimum of 256 bytes (for 64-dim). Creating such a vector for thousands of features takes a lot of memory which are not feasible for resource-constraint applications especially for embedded systems. Larger the memory, longer the time it takes for matching.

But all these dimensions may not be needed for actual matching. We can compress it using several methods like PCA, LDA etc. Even other methods like hashing using LSH (Locality Sensitive Hashing) is used to convert these SIFT descriptors in floating point numbers to binary strings. These binary strings are used to match features using Hamming distance. This provides better speed-up because finding hamming distance is just applying XOR and bit count, which are very fast in modern CPUs with SSE instructions. But here, we need to find the descriptors first, then only we can apply hashing, which doesn't solve our initial problem on memory.

BRIEF comes into picture at this moment. It provides a shortcut to find the binary strings directly without finding descriptors. It takes smoothened image patch and selects a set of \(n\_d\) (x,y) location pairs in an unique way (explained in paper). Then some pixel intensity comparisons are done on these location pairs. For eg, let first location pairs be \(p\) and \(q\). If \(I(p) < I(q)\), then its result is 1, else it is 0. This is applied for all the \(n\_d\) location pairs to get a \(n\_d\)-dimensional bitstring.

This \(n\_d\) can be 128, 256 or 512. OpenCV supports all of these, but by default, it would be 256 (OpenCV represents it in bytes. So the values will be 16, 32 and 64). So once you get this, you can use Hamming Distance to match these descriptors.

One important point is that BRIEF is a feature descriptor, it doesn't provide any method to find the features. So you will have to use any other feature detectors like SIFT, SURF etc. The paper recommends to use CenSurE which is a fast detector and BRIEF works even slightly better for CenSurE points than for SURF points.

In short, BRIEF is a faster method feature descriptor calculation and matching. It also provides high recognition rate unless there is large in-plane rotation.

## STAR(CenSurE) in OpenCV

STAR is a feature detector derived from CenSurE. Unlike CenSurE however, which uses polygons like squares, hexagons and octagons to approach a circle, Star emulates a circle with 2 overlapping squares: 1 upright and 1 45-degree rotated. These polygons are bi-level. They can be seen as polygons with thick borders. The borders and the enclosed area have weights of opposing signs. This has better computational characteristics than other scale-space detectors and it is capable of real-time implementation. In contrast to SIFT and SURF, which find extrema at sub-sampled pixels that compromises accuracy at larger scales, CenSurE creates a feature vector using full spatial resolution at all scales in the pyramid. 

## BRIEF in OpenCV

Below code shows the computation of BRIEF descriptors with the help of CenSurE detector.

note, that you need [opencv contrib](https://github.com/opencv/opencv_contrib "https://github.com/opencv/opencv_contrib")) to use this. 

import numpy as npimport cv2 as cvfrom matplotlib import pyplot as pltimg = [cv.imread](../../d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56 "../../d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56")('simple.jpg', cv.IMREAD\_GRAYSCALE)# Initiate FAST detectorstar = cv.xfeatures2d.StarDetector\_create()# Initiate BRIEF extractorbrief = cv.xfeatures2d.BriefDescriptorExtractor\_create()# find the keypoints with STARkp = star.detect(img,None)# compute the descriptors with BRIEFkp, des = brief.compute(img, kp)[print](../../df/d57/namespacecv_1_1dnn.html#a43417dcaeb3c1e2a09b9d948e234c366 "../../df/d57/namespacecv_1_1dnn.html#a43417dcaeb3c1e2a09b9d948e234c366")( brief.descriptorSize() )[print](../../df/d57/namespacecv_1_1dnn.html#a43417dcaeb3c1e2a09b9d948e234c366 "../../df/d57/namespacecv_1_1dnn.html#a43417dcaeb3c1e2a09b9d948e234c366")( des.shape ) The function brief.getDescriptorSize() gives the \(n\_d\) size used in bytes. By default it is 32. Next one is matching, which will be done in another chapter.

## Additional Resources

1. Michael Calonder, Vincent Lepetit, Christoph Strecha, and Pascal Fua, "BRIEF: Binary Robust
Independent Elementary Features", 11th European Conference on Computer Vision (ECCV), Heraklion, Crete. LNCS Springer, September 2010.
2. [LSH (Locality Sensitive Hashing)](https://en.wikipedia.org/wiki/Locality-sensitive_hashing "https://en.wikipedia.org/wiki/Locality-sensitive_hashing") at wikipedia.

---

Generated on Wed Oct 4 2023 23:37:11 for OpenCV by  [![doxygen](../../doxygen.png)](http://www.doxygen.org/index.html "http://www.doxygen.org/index.html") 1.8.13

//<![CDATA[
addTutorialsButtons();
//]]>

