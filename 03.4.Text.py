import cv2
import numpy as np

blank = np.zeros((500, 500, 3), np.uint8)

# Circle:
text_x_y = (150, 75)
BGR_Blue = (255, 0, 0)

# Text:
cv2.putText(img=blank,
            text="MESSAGE",
            org=text_x_y,
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.8,
            color=BGR_Blue,
            thickness=2)

cv2.imshow("Circle", blank)
cv2.waitKey(0)
