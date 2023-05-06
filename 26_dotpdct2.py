import numpy as np
# a=np.array([[1,3,5],[5,4,3],[4,6,7]])
# b=np.array([[3,6,1],[4,6,7],[4,3,8]])
# c=np.dot(a,b)
# print(c)




#row order must be equal to column order
a=np.arange(1,10).reshape(3,3)
b=np.arange(1,7).reshape(3,2)
c=np.dot(a,b)
print(c)

