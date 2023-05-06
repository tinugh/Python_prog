#1 to 50
import numpy as np
import pandas as pd
a=pd.Series(range(1,51))
print(a)

b=pd.Series([i for i in range(1,51)])
print(b)

#for first five rows:head
print(a.head())
print(a.head(8))

print(a.tail(3))
print(a.tail())