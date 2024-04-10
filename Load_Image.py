import cv2
import random

img = cv2.imread('nature.png', 1)

for i in range(360):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 100), random.randint(0, 150), random.randint(0, 250)]

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
