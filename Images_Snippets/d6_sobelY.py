'''
    Author: Mahnoor Anjum
    Description:
        Autocolorization
    Reference:
        pyimagesearch
'''

import cv2 
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('data/original.jpg', 0)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

edges = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=7) 
  

plt.subplot(121),plt.imshow(image,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge'), plt.xticks([]), plt.yticks([])
