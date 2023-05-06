import numpy as np
import pandas as pd
a=pd.Series([1,2,3,4])
b=pd.Series([8,7,3,4])

print(a)
print(b)

#append
c=a.append(b,ignore_index=True)
print(c)