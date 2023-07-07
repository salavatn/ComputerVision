import cv2


# Section 1: template for detection Frontal Face
frontal_face = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")


# Section 2: connect to WebCame and show video in 640x480 pixels
webcam = cv2.VideoCapture(0)
webcam.set(3, 640)  # Width
webcam.set(4, 480)  # Height


# Section 3: display and detect face 
while webcam.isOpened():
    ret, frame = webcam.read()

    # Part-1: Check is reading successfully
    if not ret:
        break

    # Part-2: Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Part-3: Detect faces
    faces = frontal_face.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Part-4: Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Part-5: Display the resulting frame
    cv2.imshow("Video Capture", frame)

    # Part-6: Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Section4: release the webcam and destroy the windows
webcam.release()
cv2.destroyAllWindows()
