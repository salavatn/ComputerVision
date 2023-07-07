import cv2
import numpy as np

blank = np.zeros((512, 512, 3), np.uint8)

# Lines:
line_1 = ((10, 50), (400, 50))
line_2 = ((10, 60), (400, 60))
line_3 = ((10, 70), (400, 70))

# Colors BGR:
BGR_Blue = (255, 0, 0)
BGR_Green = (0, 255, 0)
BGR_Red = (0, 0, 255)

cv2.line(img=blank, pt1=line_1[0], pt2=line_1[1], color=BGR_Blue, thickness=1)
cv2.line(img=blank, pt1=line_2[0], pt2=line_2[1], color=BGR_Green, thickness=2)
cv2.line(img=blank, pt1=line_3[0], pt2=line_3[1], color=BGR_Red, thickness=4)

cv2.imshow("Lines", blank)
cv2.waitKey(0)
