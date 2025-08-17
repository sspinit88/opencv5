import cv2

img = cv2.imread('img.png')
cv2.imshow('img window name', img)
cv2.waitKey()
cv2.destroyWindow()