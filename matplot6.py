import  cv2
import  numpy as np

img = cv2.imread("car_green_screen.jpg")
video = cv2.VideoCapture("green_videoo.mp4")

while video.isOpened():
    _, frame = video.read()
    copy_img = np.copy(img)
    video_mask1 = np.array([0, 200, 0])
    video_mask2 = np.array([250, 255,250])
    mask = cv2.inRange(copy_img, video_mask1, video_mask2)
    img[mask != 0] = 0
    frame =cv2.resize(frame,(640,480))
    img =cv2.resize(img,(640,480))
    frame[img!=0]=0
    ready =frame + img
    cv2.imshow("image",ready)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()