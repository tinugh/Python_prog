#2d 3*4matrix

import numpy as np
a=np.array([[1,2,3,4],[4,5,6,7],[6,7,8,9]])
print(a)

#for changing the order of matrix we use reshape" functn
print("*"*100)
b=a.reshape([4,3])
print(b)

#total number of elemnts must be same for reshaping
print("*"*1000)
c=a.reshape([6,2])
print(c)