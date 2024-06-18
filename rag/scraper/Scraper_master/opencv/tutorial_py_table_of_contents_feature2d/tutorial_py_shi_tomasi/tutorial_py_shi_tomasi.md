
# Goal

In this chapter,

* We will learn about the another corner detector: Shi-Tomasi Corner Detector
* We will see the function: **[cv.goodFeaturesToTrack()](../../dd/d1a/group__imgproc__feature.html#ga1d6bb77486c8f92d79c8793ad995d541 "Determines strong corners on an image.")**

# Theory

In last chapter, we saw Harris Corner Detector. Later in 1994, J. Shi and C. Tomasi made a small modification to it in their paper **Good Features to Track** which shows better results compared to Harris Corner Detector. The scoring function in Harris Corner Detector was given by:

\[R = \lambda\_1 \lambda\_2 - k(\lambda\_1+\lambda\_2)^2\]

Instead of this, Shi-Tomasi proposed:

\[R = \min(\lambda\_1, \lambda\_2)\]

If it is a greater than a threshold value, it is considered as a corner. If we plot it in \(\lambda\_1 - \lambda\_2\) space as we did in Harris Corner Detector, we get an image as below:

![](../../shitomasi_space.png)

image
From the figure, you can see that only when \(\lambda\_1\) and \(\lambda\_2\) are above a minimum value, \(\lambda\_{\min}\), it is considered as a corner(green region).

# Code

OpenCV has a function, **[cv.goodFeaturesToTrack()](../../dd/d1a/group__imgproc__feature.html#ga1d6bb77486c8f92d79c8793ad995d541 "Determines strong corners on an image.")**. It finds N strongest corners in the image by Shi-Tomasi method (or Harris Corner Detection, if you specify it). As usual, image should be a grayscale image. Then you specify number of corners you want to find. Then you specify the quality level, which is a value between 0-1, which denotes the minimum quality of corner below which everyone is rejected. Then we provide the minimum euclidean distance between corners detected.

With all this information, the function finds corners in the image. All corners below quality level are rejected. Then it sorts the remaining corners based on quality in the descending order. Then function takes first strongest corner, throws away all the nearby corners in the range of minimum distance and returns N strongest corners.

In below example, we will try to find 25 best corners: 

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = [cv.imread](../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8 "../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8")('blox.jpg')
gray = [cv.cvtColor](../../d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab "../../d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab")(img,cv.COLOR\_BGR2GRAY)

corners = [cv.goodFeaturesToTrack](../../dd/d1a/group__imgproc__feature.html#ga1d6bb77486c8f92d79c8793ad995d541 "../../dd/d1a/group__imgproc__feature.html#ga1d6bb77486c8f92d79c8793ad995d541")(gray,25,0.01,10)
corners = np.int0(corners)

for i in corners:
 x,y = i.ravel()
 [cv.circle](../../d6/d6e/group__imgproc__draw.html#gaf10604b069374903dbd0f0488cb43670 "../../d6/d6e/group__imgproc__draw.html#gaf10604b069374903dbd0f0488cb43670")(img,(x,y),3,255,-1)

plt.imshow(img),plt.show()
[cv::imread](../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8 "../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8")CV\_EXPORTS\_W Mat imread(const String &filename, int flags=IMREAD\_COLOR)Loads an image from a file.
[cv::cvtColor](../../d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab "../../d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab")void cvtColor(InputArray src, OutputArray dst, int code, int dstCn=0)Converts an image from one color space to another.
[cv::circle](../../d6/d6e/group__imgproc__draw.html#gaf10604b069374903dbd0f0488cb43670 "../../d6/d6e/group__imgproc__draw.html#gaf10604b069374903dbd0f0488cb43670")void circle(InputOutputArray img, Point center, int radius, const Scalar &color, int thickness=1, int lineType=LINE\_8, int shift=0)Draws a circle.
[cv::goodFeaturesToTrack](../../dd/d1a/group__imgproc__feature.html#ga1d6bb77486c8f92d79c8793ad995d541 "../../dd/d1a/group__imgproc__feature.html#ga1d6bb77486c8f92d79c8793ad995d541")void goodFeaturesToTrack(InputArray image, OutputArray corners, int maxCorners, double qualityLevel, double minDistance, InputArray mask=noArray(), int blockSize=3, bool useHarrisDetector=false, double k=0.04)Determines strong corners on an image.
 See the result below:

![](../../shitomasi_block1.jpg)

image
This function is more appropriate for tracking. We will see that when its time comes.

# Additional Resources

# Exercises
