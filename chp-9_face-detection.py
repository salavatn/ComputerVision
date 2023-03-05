# FACE DETECTION
# URL: https://youtu.be/WQeoO7MI0Bs?t=6033

import cv2

file = "Images/men2.jpeg"
img = cv2.imread(file)

# haarcascade_frontalface_default = "venv/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml"
# haarcascade_frontalface_alt = "venv/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_alt.xml"
haarcascade_frontalface_alt2 = "venv/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_alt2.xml"
# haarcascade_frontalface_alt_tree = "venv/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_alt_tree.xml"
# haarcascade_frontalcatface = "venv/lib/python3.9/site-packages/cv2/data/haarcascade_frontalcatface.xml"
# haarcascade_frontalcatface_extended = "venv/lib/python3.9/site-packages/cv2/data/haarcascade_frontalcatface_extended.xml"
# haarcascade_profileface = "venv/lib/python3.9/site-packages/cv2/data/haarcascade_profileface.xml"

faceCascade = cv2.CascadeClassifier(haarcascade_frontalface_alt2)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in faces:
    cv2.rectangle(img=img, pt1=(x, y), pt2=(x+w, y+h), color=(0, 255, 0), thickness=2)

cv2.imshow("haarcascade_frontalface_alt2.xml", img)

cv2.waitKey(0)
