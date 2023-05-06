# import numpy as np
# a=np.array([2,4,1,7,11,8,5])
# print(a)
#
# b=np.max(a)
# print(b)
# c=np.min(a)
# print(c)

import numpy as np
a=np.array([[2,4,1],[7,11,8],[3,4,5]])
print(a)

b=np.max(a)
print(b)
c=np.min(a)
print(c)

#row and column wise max and min
d=np.max(a,axis=1)#for row wise
print(d)
e=np.max(a,axis=0)#for column wise
print(e)

f=np.min(a,axis=1)
print(f)
g=np.min(a,axis=0)
print(g)

#this also has arg max n min based on the index






