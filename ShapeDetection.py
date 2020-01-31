#
#   M Wes-J
#   
#   Created: Jan 30th, 2020
#
#   Shape Detection with Fourier Descriptors

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt



def importImg(file):
    img = cv.imread(file)
    return img

def showImg(img):
    plt.title('OG img')
    plt.imshow(img, cmap='gray', interpolation='nearest') # nearest, bilinear, bicubic

def showCircle(xx, yy, radius):
    circle = plt.Circle((xx, yy), radius, color='r', fill=False)
    plt.gcf().gca().add_artist(circle)

def hist(img):
    hist = []
    print()
    for i in range(0,256):
        hist.append(len(np.where(img == i)[0]))
        if hist[i] > 0:
            print(i, ':', hist[i])



########################################################################################################################



# To show the results
plt.figure()

f = 'shapes.jpg'
img = importImg(f)
# """

mask = cv.Canny(img, 200, 0)
hist(mask)

# while (len(np.where(img == 255)[0])):
#     shape = []
#     y = list(np.where(img == 255))[0]
#     print(len(y))

# """
plt.subplot(1,2,1)
showImg(img)

plt.subplot(1,2,2)
showImg(mask)


plt.show()