import  cv2
import  numpy as np
import  matplotlib.pyplot as plt

# Image known
img1 =cv2.imread('car_green_screen.jpg')
img1 =cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2  = cv2.imread("sky.jpg")
img2  = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
# Copy image
copy_img = np.copy(img1)

# Get Size
green_img = np.array([0,200,0])
green_img2 = np.array([255,255,255])

# Maska
maska = cv2.inRange(copy_img,green_img,green_img2)
plt.imshow(maska,cmap='gray')

# Background image
copy_img[maska!=0] =[0,0,0]

# Backround maska image known
img2 =img2[:450,:660]
img2[maska==0] =[0,0,0]

# add copy image to the img2
ready =copy_img +img2
plt.imshow(ready)
plt.show()
