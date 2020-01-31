#
#   M Wes-J
#   
#   Created: Jan 30th, 2020
#
#   Shape Detection with Fourier Descriptors

import cv2 as cv
import matplotlib.pyplot as plt

# To show the results
plt.figure()

# import image
img = cv.imread('shapes.jpg')
plt.subplot(2,1,1)   # add OG image to plot
plt.title('OG img')
plt.imshow(img, cmap='gray', interpolation='bicubic') # nearest, bilinear, bicubic

plt.show()
