#chennai work and age =24  fname,lname,age,phno

import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/Tinu/Downloads/python/sample4.txt",sep=',',header=None)

df.columns=['id','fname','lname','age','phno','loc']
print(df)
print('============================================')

df1=df.loc[(df['age']==24)&(df['loc']=='chennai')]
print(df1)