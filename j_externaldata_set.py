#external data set

#how to change external dataset into dataframe'
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
print(df.head())
print(df.tail())
print(df.describe(include='all'))
print(df.dtypes)

#calculate total number of missing value
print(df.isna().sum())
#for filling missing value:
#filna()" function is used
df1=df.fillna('india')
print(df1)
print(df1.isna().sum())












