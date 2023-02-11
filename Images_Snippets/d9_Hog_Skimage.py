'''
    Author: Mahnoor Anjum
    Description:
        Autocolorization
    Reference
        Analyticsvidhya
'''

from skimage.io import imread, imshow
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt

image = imread('data/original.jpg')
imshow(image)
print(image.shape)

'''
    The orientations are the number of buckets we want to create. 
    Since I want to have a 9 x 1 matrix, 
    I will set the orientations to 9
    
    pixels_per_cell defines the size of the cell for which
    we create the histograms. 
'''

fd, hog_image = hog(image, orientations=9, pixels_per_cell=(2, 2), 
                    cells_per_block=(10, 10), visualize=True, multichannel=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), sharex=True, sharey=True) 

ax1.imshow(image, cmap=plt.cm.gray) 
ax1.set_title('Input image') 

# Rescale histogram for better display 
hog_image = exposure.rescale_intensity(hog_image, in_range=(0, 10)) 

ax2.imshow(hog_image, cmap=plt.cm.gray) 
ax2.set_title('Histogram of Oriented Gradients')

plt.show()