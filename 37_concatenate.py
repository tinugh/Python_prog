#concatenate:joining two array

import numpy as np
a=np.array([1,3,5,7,9])
b=np.array([2,4,6,8])

c=np.concatenate((a,b))
print(c)