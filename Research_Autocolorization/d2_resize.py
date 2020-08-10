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

image = cv2.resize(image, (0,0), fx=0.2, fy=0.2) 
cv2.imshow('small',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
