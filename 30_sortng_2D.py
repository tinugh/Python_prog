import numpy as np
a=np.array([[2,3,4,5],[6,7,8,9],[4,3,4,5],[4,6,3,2]])
print(a)
print("*"*900)
#sorting:
b=np.sort(a)
print(b)#row wise sorting[asc order] similar to axis=1

print("*"*900)
c=np.sort(a,axis=0)
print(c)#column wise
