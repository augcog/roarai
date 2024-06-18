
# Goal

In this chapter

* We will see how to match features in one image with others.
* We will use the Brute-Force matcher and FLANN Matcher in OpenCV

# Basics of Brute-Force Matcher

Brute-Force matcher is simple. It takes the descriptor of one feature in first set and is matched with all other features in second set using some distance calculation. And the closest one is returned.

For BF matcher, first we have to create the BFMatcher object using **[cv.BFMatcher()](../../d3/da1/classcv_1_1BFMatcher.html "Brute-force descriptor matcher.")**. It takes two optional params. First one is normType. It specifies the distance measurement to be used. By default, it is [cv.NORM\_L2](../../d2/de8/group__core__array.html#ggad12cefbcb5291cf958a85b4b67b6149fa7bacbe84d400336a8f26297d8e80e3a2 "../../d2/de8/group__core__array.html#ggad12cefbcb5291cf958a85b4b67b6149fa7bacbe84d400336a8f26297d8e80e3a2"). It is good for SIFT, SURF etc ([cv.NORM\_L1](../../d2/de8/group__core__array.html#ggad12cefbcb5291cf958a85b4b67b6149fab55c78ff204a979026c026ea19de65c9 "../../d2/de8/group__core__array.html#ggad12cefbcb5291cf958a85b4b67b6149fab55c78ff204a979026c026ea19de65c9") is also there). For binary string based descriptors like ORB, BRIEF, BRISK etc, [cv.NORM\_HAMMING](../../d2/de8/group__core__array.html#ggad12cefbcb5291cf958a85b4b67b6149fa4b063afd04aebb8dd07085a1207da727 "../../d2/de8/group__core__array.html#ggad12cefbcb5291cf958a85b4b67b6149fa4b063afd04aebb8dd07085a1207da727") should be used, which used Hamming distance as measurement. If ORB is using WTA\_K == 3 or 4, [cv.NORM\_HAMMING2](../../d2/de8/group__core__array.html#ggad12cefbcb5291cf958a85b4b67b6149fa7fab9cda83e79380cd273c49de8e3231 "../../d2/de8/group__core__array.html#ggad12cefbcb5291cf958a85b4b67b6149fa7fab9cda83e79380cd273c49de8e3231") should be used.

Second param is boolean variable, crossCheck which is false by default. If it is true, Matcher returns only those matches with value (i,j) such that i-th descriptor in set A has j-th descriptor in set B as the best match and vice-versa. That is, the two features in both sets should match each other. It provides consistent result, and is a good alternative to ratio test proposed by D.Lowe in SIFT paper.

Once it is created, two important methods are *BFMatcher.match()* and *BFMatcher.knnMatch()*. First one returns the best match. Second method returns k best matches where k is specified by the user. It may be useful when we need to do additional work on that.

Like we used [cv.drawKeypoints()](../../d4/d5d/group__features2d__draw.html#ga5d2bafe8c1c45289bc3403a40fb88920 "Draws keypoints.") to draw keypoints, **[cv.drawMatches()](../../d4/d5d/group__features2d__draw.html#gad8f463ccaf0dc6f61083abd8717c261a "Draws the found matches of keypoints from two images.")** helps us to draw the matches. It stacks two images horizontally and draw lines from first image to second image showing best matches. There is also **cv.drawMatchesKnn** which draws all the k best matches. If k=2, it will draw two match-lines for each keypoint. So we have to pass a mask if we want to selectively draw it.

Let's see one example for each of SIFT and ORB (Both use different distance measurements).

## Brute-Force Matching with ORB Descriptors

Here, we will see a simple example on how to match features between two images. In this case, I have a queryImage and a trainImage. We will try to find the queryImage in trainImage using feature matching. ( The images are /samples/data/box.png and /samples/data/box\_in\_scene.png)

We are using ORB descriptors to match features. So let's start with loading images, finding descriptors etc. 

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img1 = [cv.imread](../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8 "../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8")('box.png',cv.IMREAD\_GRAYSCALE) # queryImage
img2 = [cv.imread](../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8 "../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8")('box\_in\_scene.png',cv.IMREAD\_GRAYSCALE) # trainImage

# Initiate ORB detector
orb = cv.ORB\_create()

# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
[cv::imread](../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8 "../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8")CV\_EXPORTS\_W Mat imread(const String &filename, int flags=IMREAD\_COLOR)Loads an image from a file.
 Next we create a BFMatcher object with distance measurement [cv.NORM\_HAMMING](../../d2/de8/group__core__array.html#ggad12cefbcb5291cf958a85b4b67b6149fa4b063afd04aebb8dd07085a1207da727 "../../d2/de8/group__core__array.html#ggad12cefbcb5291cf958a85b4b67b6149fa4b063afd04aebb8dd07085a1207da727") (since we are using ORB) and crossCheck is switched on for better results. Then we use Matcher.match() method to get the best matches in two images. We sort them in ascending order of their distances so that best matches (with low distance) come to front. Then we draw only first 10 matches (Just for sake of visibility. You can increase it as you like) 

# create BFMatcher object
bf = [cv.BFMatcher](../../d3/da1/classcv_1_1BFMatcher.html "../../d3/da1/classcv_1_1BFMatcher.html")(cv.NORM\_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
img3 = [cv.drawMatches](../../d4/d5d/group__features2d__draw.html#gad8f463ccaf0dc6f61083abd8717c261a "../../d4/d5d/group__features2d__draw.html#gad8f463ccaf0dc6f61083abd8717c261a")(img1,kp1,img2,kp2,matches[:10],None,flags=cv.DrawMatchesFlags\_NOT\_DRAW\_SINGLE\_POINTS)

plt.imshow(img3),plt.show()
[cv::BFMatcher](../../d3/da1/classcv_1_1BFMatcher.html "../../d3/da1/classcv_1_1BFMatcher.html")Brute-force descriptor matcher.**Definition** features2d.hpp:1247
[cv::drawMatches](../../d4/d5d/group__features2d__draw.html#gad8f463ccaf0dc6f61083abd8717c261a "../../d4/d5d/group__features2d__draw.html#gad8f463ccaf0dc6f61083abd8717c261a")void drawMatches(InputArray img1, const std::vector< KeyPoint > &keypoints1, InputArray img2, const std::vector< KeyPoint > &keypoints2, const std::vector< DMatch > &matches1to2, InputOutputArray outImg, const Scalar &matchColor=Scalar::all(-1), const Scalar &singlePointColor=Scalar::all(-1), const std::vector< char > &matchesMask=std::vector< char >(), DrawMatchesFlags flags=DrawMatchesFlags::DEFAULT)Draws the found matches of keypoints from two images.
 Below is the result I got:

![](../../matcher_result1.jpg)

image
## What is this Matcher Object?

The result of matches = bf.match(des1,des2) line is a list of DMatch objects. This DMatch object has following attributes:

* DMatch.distance - Distance between descriptors. The lower, the better it is.
* DMatch.trainIdx - Index of the descriptor in train descriptors
* DMatch.queryIdx - Index of the descriptor in query descriptors
* DMatch.imgIdx - Index of the train image.

## Brute-Force Matching with SIFT Descriptors and Ratio Test

This time, we will use BFMatcher.knnMatch() to get k best matches. In this example, we will take k=2 so that we can apply ratio test explained by D.Lowe in his paper. 

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img1 = [cv.imread](../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8 "../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8")('box.png',cv.IMREAD\_GRAYSCALE) # queryImage
img2 = [cv.imread](../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8 "../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8")('box\_in\_scene.png',cv.IMREAD\_GRAYSCALE) # trainImage

# Initiate SIFT detector
sift = cv.SIFT\_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# BFMatcher with default params
bf = [cv.BFMatcher](../../d3/da1/classcv_1_1BFMatcher.html "../../d3/da1/classcv_1_1BFMatcher.html")()
matches = bf.knnMatch(des1,des2,k=2)

# Apply ratio test
good = []
for m,n in matches:
 if m.distance < 0.75\*n.distance:
 good.append([m])

# cv.drawMatchesKnn expects list of lists as matches.
img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags\_NOT\_DRAW\_SINGLE\_POINTS)

plt.imshow(img3),plt.show()
 See the result below:

![](../../matcher_result2.jpg)

image
# FLANN based Matcher

FLANN stands for Fast Library for Approximate Nearest Neighbors. It contains a collection of algorithms optimized for fast nearest neighbor search in large datasets and for high dimensional features. It works faster than BFMatcher for large datasets. We will see the second example with FLANN based matcher.

For FLANN based matcher, we need to pass two dictionaries which specifies the algorithm to be used, its related parameters etc. First one is IndexParams. For various algorithms, the information to be passed is explained in FLANN docs. As a summary, for algorithms like SIFT, SURF etc. you can pass following: 

FLANN\_INDEX\_KDTREE = 1
index\_params = dict(algorithm = FLANN\_INDEX\_KDTREE, trees = 5)
 While using ORB, you can pass the following. The commented values are recommended as per the docs, but it didn't provide required results in some cases. Other values worked fine.: 

FLANN\_INDEX\_LSH = 6
index\_params= dict(algorithm = FLANN\_INDEX\_LSH,
 table\_number = 6, # 12
 key\_size = 12, # 20
 multi\_probe\_level = 1) #2
 Second dictionary is the SearchParams. It specifies the number of times the trees in the index should be recursively traversed. Higher values gives better precision, but also takes more time. If you want to change the value, pass search\_params = dict(checks=100).

With this information, we are good to go. 

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img1 = [cv.imread](../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8 "../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8")('box.png',cv.IMREAD\_GRAYSCALE) # queryImage
img2 = [cv.imread](../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8 "../../d4/da8/group__imgcodecs.html#gab32ee19e22660912565f8140d0f675a8")('box\_in\_scene.png',cv.IMREAD\_GRAYSCALE) # trainImage

# Initiate SIFT detector
sift = cv.SIFT\_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# FLANN parameters
FLANN\_INDEX\_KDTREE = 1
index\_params = dict(algorithm = FLANN\_INDEX\_KDTREE, trees = 5)
search\_params = dict(checks=50) # or pass empty dictionary

flann = [cv.FlannBasedMatcher](../../dc/de2/classcv_1_1FlannBasedMatcher.html "../../dc/de2/classcv_1_1FlannBasedMatcher.html")(index\_params,search\_params)

matches = flann.knnMatch(des1,des2,k=2)

# Need to draw only good matches, so create a mask
matchesMask = [[0,0] for i in range(len(matches))]

# ratio test as per Lowe's paper
for i,(m,n) in enumerate(matches):
 if m.distance < 0.7\*n.distance:
 matchesMask[i]=[1,0]

draw\_params = dict(matchColor = (0,255,0),
 singlePointColor = (255,0,0),
 matchesMask = matchesMask,
 flags = cv.DrawMatchesFlags\_DEFAULT)

img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,\*\*draw\_params)

plt.imshow(img3,),plt.show()
[cv::FlannBasedMatcher](../../dc/de2/classcv_1_1FlannBasedMatcher.html "../../dc/de2/classcv_1_1FlannBasedMatcher.html")Flann-based descriptor matcher.**Definition** features2d.hpp:1294
 See the result below:

![](../../matcher_flann.jpg)

image
# Additional Resources

# Exercises
