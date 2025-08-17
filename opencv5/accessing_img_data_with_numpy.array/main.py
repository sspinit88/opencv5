import cv2

img = cv2.imread('pic-0.png', cv2.IMREAD_COLOR)

# if img is not None:
#     img[0, 0] = [255, 255, 255]
#     cv2.imwrite('white-pixel-first.png', img)

img[0, 0, 2] = 255 # sets the value of a pixel's red channel
cv2.imwrite('red-pixel-first.png', img)

# img[0, 0, 0] = 255 # blue channel
# cv2.imwrite('blue-pixel-first.png', img)

# img[:, :, 1] = 255 # take all pixels from all raws and columns and set green value
# cv2.imwrite('green.png', img)

# print(img.shape)<
# print(img.size)
# print(img.dtype)

my_roi = img[0:100, 0:100]
img[200:300, 200:300] = my_roi
cv2.imwrite('roi.png', img)