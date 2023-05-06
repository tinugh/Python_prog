#1: fname lname age loc
#2:age>22
#3:age equal to 24 fnmae,lname,phno
#4:chennai wrk fname,lname,age,phno

import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/Tinu/Downloads/python/sample4.txt",sep=',',header=None)

df.columns=['id','fname','lname','age','phno','loc']
print(df)
print('=================================================================')
i
df1=df.loc[df['age']>22]
print(df1)
print('===================================================================')

df2=df.loc[df['age']==24] [['fname','lname','phno']]
print(df2)
print('============================================================================')

df3=df.loc[df['loc']=='chennai'] [['fname','lname','age','phno']]
print(df3)








