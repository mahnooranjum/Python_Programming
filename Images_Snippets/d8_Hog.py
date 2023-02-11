'''
    Author: Mahnoor Anjum
    Description:
        Autocolorization
'''

import cv2 
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('data/original.jpg', 0)

winSize = (20,20)
blockSize = (10,10)
blockStride = (5,5)
cellSize = (10,10)
nbins = 9
derivAperture = 1
winSigma = -1.
histogramNormType = 0
L2HysThreshold = 0.2
gammaCorrection = 1
nlevels = 64
useSignedGradients = False
hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,histogramNormType,L2HysThreshold,gammaCorrection,nlevels, useSignedGradients)

winStride = (8,8)
padding = (8,8)
locations = ((10,20),)
hist = hog.compute(image,winStride,padding,locations)
plt.hist(hist)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.subplot(121),plt.imshow(image,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge'), plt.xticks([]), plt.yticks([])


