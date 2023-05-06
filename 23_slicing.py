import numpy as np
a=np.array([2,3,4,5,8,9])
print(a)

#4*4
import numpy as np
a=np.array([[1,2,3,4],[4,5,6,7],[3,4,5,6],[7,8,9,0]])
print(a)

#slicing
#syntax:[row,column]
print(a[:2,:3])#row=0,1  columns=0,1,2

print(a[:3,:3])
print(a[1:4,:3])

print(a[1:4:2,1:])
print(a[0:4:2,:])
print(a[2::2,1::2])


#zeroth column of the data
print(a[:,:1])
print(a[:,0])
#zeroth row of the data
print(a[0,:])

#zeroth row and column of data
print(a[0,0])
print(a[:1,:1])






