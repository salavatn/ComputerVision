import cv2
import numpy as np
import math

# file = "/Users/salavat/Pictures/cards.jpeg"
file = "Images/wokrplace.png"

book = [[3591, 2270], [3644, 2960], [2553, 2141], [2464, 2779]]
keyboard1 = [[1756, 2236], [2483, 1742], [2048, 2501], [2780, 1951]]
keyboard2 = [[1147, 2106], [1673, 1502], [1661, 2315], [2135, 1648]]
monitor = [[1894, 165], [3778, 476], [1796, 1139], [3497, 1582]]
notepad = [[1518, 1201], [1339, 1632], [690, 1122], [422, 1527]]


def perspective_transform(points, image):
    pt_A = points[0]
    pt_B = points[1]
    pt_C = points[2]
    pt_D = points[3]

    photo = cv2.imread(image)

    line1 = (pt_A, pt_B)
    line2 = (pt_C, pt_D)
    red = (0, 0, 255)

    width = int(math.sqrt((pt_A[0] - pt_B[0]) ** 2 + (pt_A[1] - pt_B[1]) ** 2))
    height = int(math.sqrt((pt_A[0] - pt_C[0]) ** 2 + (pt_A[1] - pt_C[1]) ** 2))

    cv2.line(img=photo, pt1=line1[0], pt2=line1[1], color=red, thickness=5)
    cv2.line(img=photo, pt1=line2[0], pt2=line2[1], color=red, thickness=5)

    pts1 = np.float32([pt_A, pt_B, pt_C, pt_D])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(photo, matrix, (width, height))

    cv2.imshow("Original", photo)
    cv2.imshow("Perspective Transformation", imgOutput)

    cv2.waitKey(0)


perspective_transform(keyboard1, file)
