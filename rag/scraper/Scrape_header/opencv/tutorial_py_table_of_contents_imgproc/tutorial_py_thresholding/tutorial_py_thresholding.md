
## Goal

* In this tutorial, you will learn simple thresholding, adaptive thresholding and Otsu's thresholding.
* You will learn the functions **[cv.threshold](../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57 "Applies a fixed-level threshold to each array element. ")** and **[cv.adaptiveThreshold](../../d7/d1b/group__imgproc__misc.html#ga72b913f352e4a1b1b397736707afcde3 "Applies an adaptive threshold to an array. ")**.

## Simple Thresholding

Here, the matter is straight-forward. For every pixel, the same threshold value is applied. If the pixel value is smaller than the threshold, it is set to 0, otherwise it is set to a maximum value. The function **[cv.threshold](../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57 "Applies a fixed-level threshold to each array element. ")** is used to apply the thresholding. The first argument is the source image, which **should be a grayscale image**. The second argument is the threshold value which is used to classify the pixel values. The third argument is the maximum value which is assigned to pixel values exceeding the threshold. OpenCV provides different types of thresholding which is given by the fourth parameter of the function. Basic thresholding as described above is done by using the type [cv.THRESH\_BINARY](../../d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576a147222a96556ebc1d948b372bcd7ac59 " "). All simple thresholding types are:

* [cv.THRESH\_BINARY](../../d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576a147222a96556ebc1d948b372bcd7ac59 " ")
* [cv.THRESH\_BINARY\_INV](../../d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576a19120b1a11d8067576cc24f4d2f03754 " ")
* [cv.THRESH\_TRUNC](../../d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576ac7e89a5e95490116e7d2082b3096b2b8 " ")
* [cv.THRESH\_TOZERO](../../d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576a0e50a338a4b711a8c48f06a6b105dd98 " ")
* [cv.THRESH\_TOZERO\_INV](../../d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576a47518a30aae90d799035bdcf0bb39a50 " ")

See the documentation of the types for the differences.

The method returns two outputs. The first is the threshold that was used and the second output is the **thresholded image**.

This code compares the different simple thresholding types: 

import cv2 as cvimport numpy as npfrom matplotlib import pyplot as pltimg = [cv.imread](../../d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56 "../../d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56")('gradient.png', cv.IMREAD\_GRAYSCALE)assert img is not None, "file could not be read, check with os.path.exists()"ret,thresh1 = [cv.threshold](../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57 "../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57")(img,127,255,cv.THRESH\_BINARY)ret,thresh2 = [cv.threshold](../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57 "../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57")(img,127,255,cv.THRESH\_BINARY\_INV)ret,thresh3 = [cv.threshold](../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57 "../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57")(img,127,255,cv.THRESH\_TRUNC)ret,thresh4 = [cv.threshold](../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57 "../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57")(img,127,255,cv.THRESH\_TOZERO)ret,thresh5 = [cv.threshold](../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57 "../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57")(img,127,255,cv.THRESH\_TOZERO\_INV)titles = ['Original Image','BINARY','BINARY\_INV','TRUNC','TOZERO','TOZERO\_INV']images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]for i in range(6): plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255) plt.title(titles[i]) plt.xticks([]),plt.yticks([])plt.show() NoteTo plot multiple images, we have used the plt.subplot() function. Please checkout the matplotlib docs for more details.
The code yields this result:

![threshold.jpg](../../threshold.jpg)

image
## Adaptive Thresholding

In the previous section, we used one global value as a threshold. But this might not be good in all cases, e.g. if an image has different lighting conditions in different areas. In that case, adaptive thresholding can help. Here, the algorithm determines the threshold for a pixel based on a small region around it. So we get different thresholds for different regions of the same image which gives better results for images with varying illumination.

In addition to the parameters described above, the method [cv.adaptiveThreshold](../../d7/d1b/group__imgproc__misc.html#ga72b913f352e4a1b1b397736707afcde3 "Applies an adaptive threshold to an array. ") takes three input parameters:

The **adaptiveMethod** decides how the threshold value is calculated:

* [cv.ADAPTIVE\_THRESH\_MEAN\_C](../../d7/d1b/group__imgproc__misc.html#ggaa42a3e6ef26247da787bf34030ed772cad0c5199ae8637a6b195062fea4789fa9 "../../d7/d1b/group__imgproc__misc.html#ggaa42a3e6ef26247da787bf34030ed772cad0c5199ae8637a6b195062fea4789fa9"): The threshold value is the mean of the neighbourhood area minus the constant **C**.
* [cv.ADAPTIVE\_THRESH\_GAUSSIAN\_C](../../d7/d1b/group__imgproc__misc.html#ggaa42a3e6ef26247da787bf34030ed772caf262a01e7a3f112bbab4e8d8e28182dd "../../d7/d1b/group__imgproc__misc.html#ggaa42a3e6ef26247da787bf34030ed772caf262a01e7a3f112bbab4e8d8e28182dd"): The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant **C**.

The **blockSize** determines the size of the neighbourhood area and **C** is a constant that is subtracted from the mean or weighted sum of the neighbourhood pixels.

The code below compares global thresholding and adaptive thresholding for an image with varying illumination: 

import cv2 as cvimport numpy as npfrom matplotlib import pyplot as pltimg = [cv.imread](../../d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56 "../../d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56")('sudoku.png', cv.IMREAD\_GRAYSCALE)assert img is not None, "file could not be read, check with os.path.exists()"img = [cv.medianBlur](../../d4/d86/group__imgproc__filter.html#ga564869aa33e58769b4469101aac458f9 "../../d4/d86/group__imgproc__filter.html#ga564869aa33e58769b4469101aac458f9")(img,5)ret,th1 = [cv.threshold](../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57 "../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57")(img,127,255,cv.THRESH\_BINARY)th2 = [cv.adaptiveThreshold](../../d7/d1b/group__imgproc__misc.html#ga72b913f352e4a1b1b397736707afcde3 "../../d7/d1b/group__imgproc__misc.html#ga72b913f352e4a1b1b397736707afcde3")(img,255,cv.ADAPTIVE\_THRESH\_MEAN\_C,\ cv.THRESH\_BINARY,11,2)th3 = [cv.adaptiveThreshold](../../d7/d1b/group__imgproc__misc.html#ga72b913f352e4a1b1b397736707afcde3 "../../d7/d1b/group__imgproc__misc.html#ga72b913f352e4a1b1b397736707afcde3")(img,255,cv.ADAPTIVE\_THRESH\_GAUSSIAN\_C,\ cv.THRESH\_BINARY,11,2)titles = ['Original Image', 'Global Thresholding (v = 127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']images = [img, th1, th2, th3]for i in range(4): plt.subplot(2,2,i+1),plt.imshow(images[i],'gray') plt.title(titles[i]) plt.xticks([]),plt.yticks([])plt.show() Result:

![ada_threshold.jpg](../../ada_threshold.jpg)

image
## Otsu's Binarization

In global thresholding, we used an arbitrary chosen value as a threshold. In contrast, Otsu's method avoids having to choose a value and determines it automatically.

Consider an image with only two distinct image values (*bimodal image*), where the histogram would only consist of two peaks. A good threshold would be in the middle of those two values. Similarly, Otsu's method determines an optimal global threshold value from the image histogram.

In order to do so, the [cv.threshold()](../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57 "Applies a fixed-level threshold to each array element. ") function is used, where [cv.THRESH\_OTSU](../../d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576a95251923e8e22f368ffa86ba8bce87ff "flag, use Otsu algorithm to choose the optimal threshold value ") is passed as an extra flag. The threshold value can be chosen arbitrary. The algorithm then finds the optimal threshold value which is returned as the first output.

Check out the example below. The input image is a noisy image. In the first case, global thresholding with a value of 127 is applied. In the second case, Otsu's thresholding is applied directly. In the third case, the image is first filtered with a 5x5 gaussian kernel to remove the noise, then Otsu thresholding is applied. See how noise filtering improves the result. 

import cv2 as cvimport numpy as npfrom matplotlib import pyplot as pltimg = [cv.imread](../../d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56 "../../d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56")('noisy2.png', cv.IMREAD\_GRAYSCALE)assert img is not None, "file could not be read, check with os.path.exists()"# global thresholdingret1,th1 = [cv.threshold](../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57 "../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57")(img,127,255,cv.THRESH\_BINARY)# Otsu's thresholdingret2,th2 = [cv.threshold](../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57 "../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57")(img,0,255,cv.THRESH\_BINARY+cv.THRESH\_OTSU)# Otsu's thresholding after Gaussian filteringblur = [cv.GaussianBlur](../../d4/d86/group__imgproc__filter.html#gaabe8c836e97159a9193fb0b11ac52cf1 "../../d4/d86/group__imgproc__filter.html#gaabe8c836e97159a9193fb0b11ac52cf1")(img,(5,5),0)ret3,th3 = [cv.threshold](../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57 "../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57")(blur,0,255,cv.THRESH\_BINARY+cv.THRESH\_OTSU)# plot all the images and their histogramsimages = [img, 0, th1, img, 0, th2, blur, 0, th3]titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)', 'Original Noisy Image','Histogram',"Otsu's Thresholding", 'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]for i in range(3): plt.subplot(3,3,i\*3+1),plt.imshow(images[i\*3],'gray') plt.title(titles[i\*3]), plt.xticks([]), plt.yticks([]) plt.subplot(3,3,i\*3+2),plt.hist(images[i\*3].ravel(),256) plt.title(titles[i\*3+1]), plt.xticks([]), plt.yticks([]) plt.subplot(3,3,i\*3+3),plt.imshow(images[i\*3+2],'gray') plt.title(titles[i\*3+2]), plt.xticks([]), plt.yticks([])plt.show() Result:

![otsu.jpg](../../otsu.jpg)

image
### How does Otsu's Binarization work?

This section demonstrates a Python implementation of Otsu's binarization to show how it actually works. If you are not interested, you can skip this.

Since we are working with bimodal images, Otsu's algorithm tries to find a threshold value (t) which minimizes the **weighted within-class variance** given by the relation:

\[\sigma\_w^2(t) = q\_1(t)\sigma\_1^2(t)+q\_2(t)\sigma\_2^2(t)\]

where

\[q\_1(t) = \sum\_{i=1}^{t} P(i) \quad \& \quad q\_2(t) = \sum\_{i=t+1}^{I} P(i)\]

\[\mu\_1(t) = \sum\_{i=1}^{t} \frac{iP(i)}{q\_1(t)} \quad \& \quad \mu\_2(t) = \sum\_{i=t+1}^{I} \frac{iP(i)}{q\_2(t)}\]

\[\sigma\_1^2(t) = \sum\_{i=1}^{t} [i-\mu\_1(t)]^2 \frac{P(i)}{q\_1(t)} \quad \& \quad \sigma\_2^2(t) = \sum\_{i=t+1}^{I} [i-\mu\_2(t)]^2 \frac{P(i)}{q\_2(t)}\]

It actually finds a value of t which lies in between two peaks such that variances to both classes are minimal. It can be simply implemented in Python as follows: 

img = [cv.imread](../../d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56 "../../d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56")('noisy2.png', cv.IMREAD\_GRAYSCALE)assert img is not None, "file could not be read, check with os.path.exists()"blur = [cv.GaussianBlur](../../d4/d86/group__imgproc__filter.html#gaabe8c836e97159a9193fb0b11ac52cf1 "../../d4/d86/group__imgproc__filter.html#gaabe8c836e97159a9193fb0b11ac52cf1")(img,(5,5),0)# find normalized\_histogram, and its cumulative distribution functionhist = [cv.calcHist](../../d6/dc7/group__imgproc__hist.html#ga6ca1876785483836f72a77ced8ea759a "../../d6/dc7/group__imgproc__hist.html#ga6ca1876785483836f72a77ced8ea759a")([blur],[0],None,[256],[0,256])hist\_norm = hist.ravel()/hist.sum()Q = hist\_norm.cumsum()bins = np.arange(256)fn\_min = np.infthresh = -1for i in range(1,256): p1,p2 = np.hsplit(hist\_norm,[i]) # probabilities q1,q2 = Q[i],Q[255]-Q[i] # cum sum of classes if q1 < 1.e-6 or q2 < 1.e-6: continue b1,b2 = np.hsplit(bins,[i]) # weights # finding means and variances m1,m2 = np.sum(p1\*b1)/q1, np.sum(p2\*b2)/q2 v1,v2 = np.sum(((b1-m1)\*\*2)\*p1)/q1,np.sum(((b2-m2)\*\*2)\*p2)/q2 # calculates the minimization function fn = v1\*q1 + v2\*q2 if fn < fn\_min: fn\_min = fn thresh = i# find otsu's threshold value with OpenCV functionret, otsu = [cv.threshold](../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57 "../../d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57")(blur,0,255,cv.THRESH\_BINARY+cv.THRESH\_OTSU)[print](../../df/d57/namespacecv_1_1dnn.html#a43417dcaeb3c1e2a09b9d948e234c366 "../../df/d57/namespacecv_1_1dnn.html#a43417dcaeb3c1e2a09b9d948e234c366")( "{} {}".[format](../../db/de0/group__core__utils.html#ga0cccdb2f73859309b0611cf70b1b9409 "../../db/de0/group__core__utils.html#ga0cccdb2f73859309b0611cf70b1b9409")(thresh,ret) )## Additional Resources

1. Digital Image Processing, Rafael C. Gonzalez

## Exercises

1. There are some optimizations available for Otsu's binarization. You can search and implement it.

