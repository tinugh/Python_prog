import pandas as pd
df1=pd.read_csv("C:/Users/Tinu/Downloads/python/custom.txt",sep=',',header=None)
df1.columns=['id','name','age','loc','salary']
print(df1)
print("--------------------------------------------------------------------")
df2=pd.read_csv("C:/Users/Tinu/Downloads/python/order.txt",sep=',',header=None)
df2.columns=['purchase_id','date','id','amount']
print(df2)
print("------------------------------------------------------------------------")

#1:join common fields
df=pd.merge(df1,df2,on='id',how='inner')
print(df)
print("-----------------------------------------------------------------------------")

#2:age >24 name age loc data amonut
df3 = df[df['age'] > 24][['name', 'age', 'loc', 'date', 'amount']]
print(df3)
print("------------------------------------------------")

#3:age ,xm 1 emplo name age loc sal dte amnt
df4=df.sort_values(by='age') [['name','age','loc','salary','date','amount']].tail(1)
print(df4)
print("----------------------------------------------------------------------------")

#4:mxm amnt pay empl nme age sala data amount
df5=df.sort_values(by='amount') [['name','age','salary','date','amount']]
print(df5)
print("--------------------------------------------------------------------------------")

#5:latest date name age salry date amount
df6=df.sort_values(by='date') [['name','age','salary','date','amount']].tail(1)
print(df6)












