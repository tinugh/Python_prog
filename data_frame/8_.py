#Age mxm 1 employee  fnme lnme aage loc
#age minim 2 employ fnm,lnm,age,phon


import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/Tinu/Downloads/python/sample4.txt",sep=',',header=None)

df.columns=['id','fname','lname','age','phno','loc']
print(df)
print('============================================')
df1=df.sort_values(by='age',ascending=False) [['fname','lname','age','loc']].head(1)
print(df1)
print("========================================")

df2=df.sort_values(by='age') [['fname','lname','age','phno']].head(2)
print(df2)

print("========================================================================================")
#chennai work age max 1 emp fname lnme age phno loc
#method:loc,sort,colm,head/tail
df3=df.loc[(df['loc']=='chennai')].sort_values(by='age',ascending=False) [['fname','lname','age','phno']].head(1)
print(df3)





