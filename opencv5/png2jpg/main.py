import os
import sys
import cv2

image = cv2.imread('MyPic.png', cv2.IMREAD_GRAYSCALE)

if image is None:
    print('Failed to read image from file')
    sys.exit(1)
success = cv2.imwrite('MyPic-grey.jpg', image)
if not success:
    print('Failed to write to file')
    sys.exit(1)



