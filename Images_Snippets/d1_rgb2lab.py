'''
    Author: Mahnoor Anjum
    Description:
        Autocolorization
'''

import cv2 

image = cv2.imread('data/original.png')
cv2.imshow('original',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow('lab',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('lab2bgr',cv2.cvtColor(image, cv2.COLOR_LAB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()