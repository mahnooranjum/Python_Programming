'''
    Author: Mahnoor Anjum 
    Description:
        Intersection Test
    
    Reference:
        www.geeksforgeeks.org
    
    For a given point triplet (A, B, C), 
    we can determine the orientation by 
    inspecting at the sign of the cross product of AB × BC 

    If AB × BC > 0, counterclockwise.
    If AB × BC < 0, clockwise.
    Otherwise, if AB × BC = 0, collinear.
    
'''

import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
import numpy as np
import cv2

def orientation(a,b,c):
    
    val = (float(b[1] - a[1]) * (c[0] - b[0])) - \
          (float(b[0] - a[0]) * (c[1] - b[1])) 
    if (val > 0): 
        return 1 #anticlockwise
    elif (val < 0): 
        return 2 #clockwise
    else: 
        return 0

def onSegment(a, b, p): 
    if ( (b[0] <= max(a[0], p[0])) and (b[0] >= min(a[0], p[0])) and 
           (b[1] <= max(a[1], p[1])) and (b[1] >= min(a[1], p[1]))): 
        return True
    return False

def check_intersect(a,b,c,d):
    
    # a b c, a b d, c d a, c d b
    o1 = orientation(a, b, c) 
    o2 = orientation(a, b, d) 
    o3 = orientation(c, d, a) 
    o4 = orientation(c, d, b) 
    
    # General case 
    if ((o1 != o2) and (o3 != o4)): 
        return 1
  
    # Special Cases 
  
    # a , b and c are colinear and c lies on segment ab 
    if ((o1 == 0) and onSegment(a, c, b)): 
        return 1
  
    # a , b and d are colinear and d lies on segment ab 
    if ((o2 == 0) and onSegment(a, d, b)): 
        return 1
  
    # c , d and a are colinear and a lies on segment cd 
    if ((o3 == 0) and onSegment(c, a, d)): 
        return 1
  
    # c , d and b are colinear and b lies on segment cd 
    if ((o4 == 0) and onSegment(c, b, d)): 
        return 1
  
    # If none of the cases 
    return 0
  
mat = mpimg.imread('data/img.png')  

fig, ax = plt.subplots(1,1,figsize=(5,5))
ax.imshow(mat) 
x = fig.ginput(4)
plt.close('all')

points = []
for i in x:
    points.append(i)
    
# x, y = [], []
# for i in points:
#     x.append(i[0])
#     y.append(i[1])
    
intersect = check_intersect(points[0], points[1],\
                            points[2], points[3])


