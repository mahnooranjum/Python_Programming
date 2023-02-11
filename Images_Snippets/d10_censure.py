'''
    Author: Mahnoor Anjum
    Description:
        Detection
'''
from skimage import data
from skimage import transform
from skimage.feature import CENSURE
from skimage.color import rgb2gray
import cv2

import matplotlib.pyplot as plt


img_orig = cv2.imread('data/original.jpg',0)

detector = CENSURE(non_max_threshold=0.05, line_threshold=20)

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 6))

detector.detect(img_orig)

ax.imshow(img_orig, cmap=plt.cm.gray)
ax.scatter(detector.keypoints[:, 1], detector.keypoints[:, 0],
              2 ** detector.scales, facecolors='none', edgecolors='r')
ax.set_title("Censure")
plt.tight_layout()
plt.show()