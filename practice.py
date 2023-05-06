import numpy as np
import pandas as pd
a=pd.Series([1,3,5,7])
b=pd.Series([2,4,6,8])

c=a.append(b,ignore_index=True)
print(c)



