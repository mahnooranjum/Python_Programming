'''
    Author: Mahnoor Anjum 
    Description:
        2D data sampler 
'''

import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
import numpy as np
import cv2



mat = mpimg.imread('data/img.png')  

fig, ax = plt.subplots(1,1,figsize=(5,5))
ax.imshow(mat) 
x = fig.ginput(2)
p1 = x[0]
p2 = x[1]
m = (p1[1] - p2[1])/(p1[0] - p2[0]) 

plt.close('all')

(Y, X, C) = mat.shape

#x = np.arange(0, X)
x = np.arange(0, X)
x = [int(i) for i in x]
x = np.array(x)
y = np.round(m*x + (p2[1] - m*p2[0]))
y = [int(i) for i in y]

y = np.array(y)

if p1[1]>p2[1]:
    y[y > p1[1]] = p1[1]
    y[y < p2[1]] = p2[1]
else:
    y[y > p2[1]] = p2[1]
    y[y < p1[1]] = p1[1]

    
fig, ax = plt.subplots(1,1,figsize=(5,5))
ax.imshow(mat) 
ax.plot(x,y)
ax.scatter(p1[0], p1[1], c ='b')
ax.scatter(p2[0], p2[1], c ='r')
_ = fig.ginput(1)
plt.close('all')


