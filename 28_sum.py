import numpy as np
a=np.array([2,3,4,5,6])
print(a)

#sum functn
b=np.sum(a)
print(b)

c=np.arange(1,13).reshape(4,3)
print(c)

print("*"*900)
#sum:
#1:axis=0,column wise sum
d=np.sum(c,axis=0)
print(d)

print("*"*900)
#2:axis=1,row wise sum
e=np.sum(c,axis=1)
print(e)


