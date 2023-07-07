import cv2

file = "Images/monkey.jpg"
picture = cv2.imread(filename=file, flags=1)
cv2.imshow(winname="The original photo", mat=picture)
cv2.waitKey(delay=0)

'picture = cv2.imread(filename=file, flags=1)   # cv2.IMREAD_COLOR'
'picture = cv2.imread(filename=file, flags=-1)  # cv2.IMREAD_UNCHANGED'
'picture = cv2.imread(filename=file, flags=0)   # cv2.IMREAD_GRAYSCALE'
'cv2.waitKey(delay=0)                           # 0 - None, 1000 = 1 second'
