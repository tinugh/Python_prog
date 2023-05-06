import numpy as np
a=np.array([6,1,9,5,4,3])
print(a)

#for iterating each elemnts from the matrix
for i in a:
    print(i)

print("*"*900)
#2d iteration each elemnts
b=np.array([[1,3,4,5],[5,6,7,8],[8,7,6,5],[6,5,4,3]])
print(b)

for i in b:
    for j in i:
        print(j)

#3D iteration each elemnts
c=np.array([[[1,3,4,5],[5,6,7,8],[8,7,6,5],[6,5,4,3]]])
for i in c:
    for j in i:
        for k in j:
            print(k)



























