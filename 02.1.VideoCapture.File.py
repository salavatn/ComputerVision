import cv2

file = "Videos/Road-Construction.mp4"
video = cv2.VideoCapture(file)

while video.isOpened():
    status, capture = video.read()
    if status is True:
        cv2.imshow("Video Capture", capture)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows()
