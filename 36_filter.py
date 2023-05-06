#filter: elemnt satisfying condition

import numpy as np
a=np.array([2,4,6,3,5,7,12,1,14,17,9])
print(a)

# b=np.where(a>4),filter
# print(b)#undex values
#
# #for elemnts
# c=b>4
# d=a[c]
# print(d)

#for even number
b=a%2==0
c=a[b]
print(c)













