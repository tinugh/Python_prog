import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/Tinu/Downloads/python/missing_data1.csv',sep=',')
print(df)
print("'"*900)
print(df.head())
print(df.tail())

print("'"*900)
print(df.columns)
print(df.dtypes)
print("'"*900)
print(df.isna().sum())

df1=df.fillna('500')
print(df1)
print(df1.isna().sum())