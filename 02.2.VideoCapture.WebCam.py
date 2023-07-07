import cv2

webcam = cv2.VideoCapture(0)

while webcam.isOpened():
    status, capture = webcam.read()
    if status is True:
        cv2.imshow("Video Capture", capture)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

webcam.release()
cv2.destroyAllWindows()
