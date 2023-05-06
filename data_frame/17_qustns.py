#pass students name roll no

import pandas as pd
df1=pd.read_csv("C:/Users/Tinu/Downloads/python/student.unknown",sep=",",header=None)
df1.columns=['name','id']
print(df1)
print("-----------------------------------------------------------------------------------")
df2=pd.read_csv("C:/Users/Tinu/Downloads/python/results.unknown",sep=",",header=None)
df2.columns=['id','status']
print(df2)
print("-------------------------------------------------------------------------------------")

df3=pd.merge(df1,df2,on='id',how='inner').loc[df2['status']=='pass'] [['name','id','status']]
print(df3)
print("---------------------------------------------")
#
# df4=df3.loc[df3['status']=='pass'] [['name','id']]
# print(df4)