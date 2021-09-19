import  matplotlib.pyplot as plt
import numpy as np

data ={'a' :np.arange(30),
       'b' :np.random.randint(0,30,30),
       'c' :np.random.randint(0,30,30)}

data['d'] =data['a'] +10*np.random.randn(30)
data['c'] =np.abs(data['c'])*80

plt.scatter('a','b',c='c',s='d', data=data)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
