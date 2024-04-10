import cv2
import numpy as np

img = cv2.imread('nature.png', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = np.intp(cv2.goodFeaturesToTrack(gray, 100, 0.75, 5))
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 10, (0, 255, 255), -1)

for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x : int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)

print("No. of corners detected: ", len(corners))

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
