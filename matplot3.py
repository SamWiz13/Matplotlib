import matplotlib.pyplot as plt
import  numpy as np
import  matplotlib.image as img
import  cv2


plt.figure(figsize=(15,18))

for i in range(30):
    img1 =np.random.randint(10,size=(8,8))
    plt.subplot(5,6,i+1)
    plt.imshow(img1)
plt.show()
