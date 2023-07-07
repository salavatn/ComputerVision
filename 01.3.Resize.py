import cv2

file = "Images/car.jpeg"

picture = cv2.imread(file)
pic_Resized = cv2.resize(src=picture, dsize=(450, 200))
pic_Cropped = picture[117:309, 8:593]

cv2.imwrite("Images/CroppedImage.jpg", pic_Cropped)
cv2.imwrite("Images/ResizedImage.jpg", pic_Resized)

cv2.waitKey(0)
