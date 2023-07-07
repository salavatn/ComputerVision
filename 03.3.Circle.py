import cv2
import numpy as np

blank = np.zeros((500, 500, 3), np.uint8)

# Circle:
circle1 = ((250, 0), 75)
circle2 = ((100, 100), 35)

# Colors BGR:
BGR_Yellow = (0, 255, 255)
BGR_Blue = (255, 0, 0)

# Rectangle:
cv2.circle(img=blank, center=circle1[0], radius=circle1[1], color=BGR_Blue, thickness=3)
cv2.circle(img=blank, center=circle2[0], radius=circle2[1], color=BGR_Yellow, thickness=cv2.FILLED)

cv2.imshow("Circle", blank)
cv2.waitKey(0)
