

import pandas as pd

df=pd.read_csv('C:/Users/Tinu/Downloads/python/customer.unknown',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','loc']
print(df)






print("''''''''''''''''''''''''''''''''''''''''''''''")
df1=df[['fname','lname','age']]
print(df1)