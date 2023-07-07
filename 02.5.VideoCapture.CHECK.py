import cv2

webcam = cv2.VideoCapture(0)

while webcam.isOpened():
    status, capture = webcam.read()
    capture_gray = cv2.cvtColor(src=capture, code=cv2.COLOR_BGR2GRAY)

    if status is True:
        cv2.imshow("Video Original", capture)
        cv2.imshow("Video GRAY", capture_gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

webcam.release()
cv2.destroyAllWindows()
