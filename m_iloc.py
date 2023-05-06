#for reading the mid data of a file we use "iloc" function

import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/Tinu/Downloads/python/customer.unknown',sep=',')
print(df)
print("'"*900)

#headertag:column name presented file or
#absented file; must enter header=None" function
df=pd.read_csv('C:/Users/Tinu/Downloads/python/customer.unknown',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','loc']
print(df)

df1=df.iloc[3]
print(df1)

df2=df.iloc[3:9:2]
print(df2)

df3=df.iloc[:,3:5]
print(df3)

#x seperation>>>>>>all value except last column
#y seperation>>>>>>last column


x=df.iloc[:,:-1]
print(x)

y=df.iloc[:,-1]
print(y)


