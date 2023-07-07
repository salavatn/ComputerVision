import cv2
import numpy as np

blank = np.zeros((500, 500, 3), np.uint8)

# Rectangle:
rectangle_Q = ((50, 50), (450, 200))
rectangle_H = ((100, 250), (400, 350))

# Colors BGR:
BGR_Blue = (255, 0, 0)
BGR_Green = (0, 255, 0)
BGR_Red = (0, 0, 255)

# Rectangle:
cv2.rectangle(img=blank, pt1=rectangle_Q[0], pt2=rectangle_Q[1], color=BGR_Green, thickness=2)
cv2.rectangle(img=blank, pt1=rectangle_H[0], pt2=rectangle_H[1], color=BGR_Blue, thickness=cv2.FILLED)

cv2.imshow("Rectangle", blank)
cv2.waitKey(0)
