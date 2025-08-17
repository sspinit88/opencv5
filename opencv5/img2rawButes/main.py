import os

import cv2 as cv
import numpy

## Make an array of 120,000 random bytes.
# randomByteArray = bytearray(os.urandom(120000))
# flatNumpyArray = numpy.array(randomByteArray)

## Convert the array to make a 400x300 grayscale image.
# grayImg = flatNumpyArray.reshape(300, 400)
# cv.imwrite('RandomGray.png', grayImg)

## Convert the array to make a 400x100 color image.
# bgrImg = flatNumpyArray.reshape(100, 400, 3)
# cv.imwrite('RandomColor.png', bgrImg)

imgs = [];
imgs.append(numpy.random.randint(0, 255, 120000).reshape(300, 400))
imgs.append(numpy.random.randint(0, 255, 120000).reshape(100, 400, 3))

for i, item in enumerate(imgs):
    cv.imwrite(f'pic-{i}.png', item)

