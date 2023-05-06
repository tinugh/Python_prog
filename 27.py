#round floor ceil

import numpy as np
a=np.array([[1.2,2.3,3.4,5.5],[4.6,8.7,8.7,5.3],[2.1,3.2,4.1,6.5],[9.5,7.8,6.3,5.2]])
print(a)

#1:floor
#to discard decimal part
# [1 2 3 4]
# [5 6 7 8]
# ........

#syntax:
print("*"*900)
b=np.floor(a)
print(a)

#2:ceil
print("*"*900)
c=np.ceil(a)
print(c)

#3:round

#0.5> converts to highest
#0.5< converts to lowest

print("*"*900)
d=np.round(a)
print(d)
# [[1.2 2.3 3.4 5. ]
#  [4.6 8.7 8.7 5.3]
#  [2.1 3.2 4.1 6.5]
#  [9.5 7.8 6.3 5.2]]\

#note: in case of odd number it rounds to highest and in case of even number it rounds to lowest










