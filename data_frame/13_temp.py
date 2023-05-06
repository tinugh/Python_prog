import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/Tinu/Downloads/python/Temperature.unknown",sep=' ',header=None)

df.columns=['year','temp']
print(df)
print("---------------------------------------------")


#max tmp of all yr

df1=df.groupby('year')['temp'].max().sort_values(ascending=False)
print(df1)

#min operator
#newdfname=olddfname.groupby('colnme')['colname].min()
print("--------------------------------------------------------------------------------------")
#each yr min tmp
df2=df.groupby('year')['temp'].min().sort_values(ascending=False)
print(df2)


#sum:
#newdfname=olddfname.groupby('colnme')['colname].sum()
print("-----------------------------------------------------------------------------")
df3=df.groupby('year') ['temp'].sum().sort_values()
print(df3)
print("--------------------------------------------------------------------------------------------------")
#mean:
#newdfname=olddfname.groupby('colnme')['colname].mean()
df4=df.groupby('year') ['temp'].mean().sort_values()
print(df4)


















