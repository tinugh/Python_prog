

import pandas as pd
df=pd.read_csv('C:/Users/Tinu/Downloads/python/customer.unknown',sep=',')
print(df)
print("'"*900)

df1=df[['fname','lname','age']]
print(df1)