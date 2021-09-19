import cv2

video = cv2.VideoCapture("1.mp4")

while video.isOpened():
    _, img1 = video.read()

    cv2.rectangle(img1, (537, 100), (637, 0), (0, 0, 0), -1)
    cv2.imshow("Video", img1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()