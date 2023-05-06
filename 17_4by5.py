#4*5=====>5*4=====>10*2

import numpy as np
a=np.array([[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[1,2,3,4,5]])
print(a)

print("*"*1000)

b=a.reshape([5,4])
print(b)

print("*"*1000)

c=a.reshape([10,2])
print(c)





