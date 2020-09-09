'''
    Author: Mahnoor Anjum
    Description:
        Patch 2D
'''

import cv2 
from sklearn.feature_extraction import image
import matplotlib.pyplot as plt

im = plt.imread('data/original.png')
patches = image.extract_patches_2d(im, (100, 100))

plt.imshow(im)

p = 5
fig, ax = plt.subplots(p, p, figsize=(16, 8), sharex=True, sharey=True) 

k = 100000
for i in range(p):
    for j in range(p):
        ax[i, j].imshow(patches[k]) 
        k=k+1
