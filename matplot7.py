import matplotlib.pyplot as plt
import numpy as np
import cv2

img1 =plt.imread('car_green_screen.jpg')
plt.figure(figsize=(12,3))
plt.subplot(141)
plt.imshow(img1)
plt.subplot(142)
plt.imshow(img1[:,:,0],cmap='gray')
plt.subplot(143)
plt.imshow(img1[:,:,1],cmap='gray')
plt.subplot(144)
plt.imshow(img1[:,:,2],cmap='gray')

plt.show()


