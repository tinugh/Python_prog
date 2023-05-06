#1: total no of rows
#2:each proff count [descnding order]
#3:each country count [desc]
#4:each proff max sala [desc]
#5:each country min sala
#6:each proff total slary
#7:each proff average salary
#8:each proff min age

import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/Tinu/Downloads/python/customer5.txt",sep=',',header=None)
df.columns=['id','fname','lname','age','prof','loc','salary']
print(df)

print("----------------------------------------------------------------------------")
#2:
df2=df.groupby('prof') ['prof'].count().sort_values(ascending=False)
print(df2)
print("-----------------------------------------------------------------------------------")

#3:
df3=df.groupby('loc') ['loc'].count().sort_values(ascending=False)
print(df3)
print("-----------------------------------------------------------------------------------")

#4:
df4=df.groupby('prof') ['salary'].max().sort_values(ascending=False)
print(df4)
print("------------------------------------------------------------------------------------------")

#5:
df5=df.groupby('loc') ['salary'].min().sort_values(ascending=False)
print(df5)
print("----------------------------------------------------------------------------------------------------")

#6:
df6=df.groupby('prof') ['salary'].sum().sort_values(ascending=False)
print(df6)
print("---------------------------------------------------------------------------------------------------------")


#7
df7=df.groupby('prof') ['salary'].mean().sort_values(ascending=False)
print(df7)
print('----------------------------------------------------------------------------------------------------')

#1:
df1=len(df)
print(df1)
