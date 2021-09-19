import matplotlib.pyplot as plt
import  numpy as np
import  matplotlib.image as img
import  cv2

x =np.arange(0,10)
# plt.plot(x,np.exp(x),label ="Plot")
plt.plot(x,np.sin(x),label ="Plot")
plt.plot(x,np.cos(x),label ="Plot")
plt.plot(x,np.sqrt(x),label ="Plot")
plt.show()
