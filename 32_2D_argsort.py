import numpy as np
a=np.array([[3,1,6,4],[0,9,2,6],[4,6,1,0],[7,3,4,1]])
print(a)

print("*"*900)
b=np.argsort(a)
print(b)

print("*"*900)
c=np.argsort(a,axis=0)
print(c)

