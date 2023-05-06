#custom
#order
import pandas as pd

#total number of rows
df1=pd.read_csv("C:/Users/Tinu/Downloads/python/custom.txt",sep=',',header=None)
df1.columns=['id','name','age','loc','sal']
df2=pd.read_csv("C:/Users/Tinu/Downloads/python/order.txt",sep=',',header=None)
df2.columns=['oid','date','time','rate','sal']

df3=pd.merge(df1.df2,on='sal',how='outer')
print(len(df3))