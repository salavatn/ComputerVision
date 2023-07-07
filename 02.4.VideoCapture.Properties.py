import cv2

file = "Videos/Road-Construction.mp4"
video = cv2.VideoCapture(file)

print("Get the video file/webcam properties:")
print(f"{video.get(cv2.CAP_PROP_FRAME_WIDTH)}\t- Frame Width \n"
      f"{video.get(cv2.CAP_PROP_FRAME_HEIGHT)}\t- Frame Height \n"
      f"{video.get(cv2.CAP_PROP_FPS)}\t- FPS \n"
      f"{video.get(cv2.CAP_PROP_POS_MSEC)}  \t- MSEC \n"
      f"{video.get(cv2.CAP_PROP_FRAME_COUNT)}\t- Frame Count \n"
      f"{video.get(cv2.CAP_PROP_BRIGHTNESS)}  \t- Brightness \n"
      f"{video.get(cv2.CAP_PROP_CONTRAST)}  \t- Contrast \n"
      f"{video.get(cv2.CAP_PROP_SATURATION)}  \t- Saturation \n"
      f"{video.get(cv2.CAP_PROP_HUE)}  \t- Hue \n"
      f"{video.get(cv2.CAP_PROP_GAIN)}  \t- Gain \n"
      f"{video.get(cv2.CAP_PROP_CONVERT_RGB)}  \t- Convert RGB")

video.release()
cv2.destroyAllWindows()
