#for checking elemnt present or not we use where" function/or any conditions can be checked
import numpy as np
a=np.array([1,2,3,4,5,6,7,4,5,6,4])

x=np.where(a==4)
print(x)

print("*"*900)
b=np.array([[1,2,3],[5,6,7],[4,5,6]])
print(b)
y=np.where(b==5)
print(y)


