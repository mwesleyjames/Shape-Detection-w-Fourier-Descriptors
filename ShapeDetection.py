#   M Wes-J
#
#   Created: Jan 30th, 2020
#
#   Shape Detection with Fourier Descriptors

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"figure.max_open_warning": 0})

# OPEN IMAGE
#   params:
#     file  = image filename
#     color = import color scheme
#   return:
#     img   = image variable
def importImg(file, color):
    img = cv.imread(file, color)
    return img


# SHOW IMAGE
#   params:
#     img   = image variable
#     color = import color scheme
def showImg(img, color):
    plt.title("OG img")
    plt.imshow(img, cmap="gray", interpolation="bicubic")
    # nearest, bilinear, bicubictt


def showCircle(xx, yy, radius):
    circle = plt.Circle((xx, yy), radius, color="r", fill=False)
    plt.gcf().gca().add_artist(circle)

def hist(img):
    hist = []
    print()
    for i in range(0,256):
        hist.append(len(np.where(img == i)[0]))
        if hist[i] > 0:
            print(i, ':', hist[i])

def showLine(xStart, yStart, xEnd, yEnd):
    plt.plot([xStart, xEnd], [yStart, yEnd], linewidth=1, ls="dashed", color="r", marker="o", ms=2.5)


#################################################################################


# To show the results
plt.figure()

f = "shapes.jpg"
color = 0  # gray=0, BGR=1
img = importImg(f, color)

# ""

# Create Circle:
edges = cv.Canny(img, 100, 200)  # TODO: what is 100 & 200 ?
print(type(edges[0][0]))
print(np.shape(edges))
# e = np.ndarray(np.shape(edges)[0], np.shape(edges)[1], dtype=np.uint8)
# e[:,:,3] = (edges[:,:,0] > 250)

# Fourier Descriptor - [c]
c = []

# ""

showImg(img, color)
showImg(edges, color)
showCircle(0, 0, 100)
showCircle(250, 250, 100)
showLine(250, 250, 25, 25)
plt.show()
#plt.savefig("figure.png")