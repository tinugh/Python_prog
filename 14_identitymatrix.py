#identity matrix:diagonal elemnt 1and other elemnts 0

#eg:
#[1 0]
#[0 1]

#note: identity matrix only works in square matrix

#functn: "identity"
import numpy as np
a=np.identity(3,dtype=int)
print(a)
print(a.dtype)