#
#   M Wes-J
#   
#   Created: Jan 30th, 2020
#
#   Shape Detection with Fourier Descriptors

import cv2 as cv
import matplotlib.pyplot as plt



def importImg(file):
    img = cv.imread(file)
    return img

def showImg(img):
    plt.title('OG img')
    plt.imshow(img, cmap='gray', interpolation='bicubic') # nearest, bilinear, bicubic

def showCircle(xx, yy, radius):
    circle = plt.Circle((xx, yy), radius, color='r', fill=False)
    plt.gcf().gca().add_artist(circle)



########################################################################################################################



# To show the results
plt.figure()

f = 'shapes.jpg'
img = importImg(f)
# """



# """
showImg(img)

plt.show()