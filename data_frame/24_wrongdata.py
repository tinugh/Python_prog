#how to handle wrong data

#wrong data eg:
#height  weight
#175     60
#188     75
#400     80>>>>>>>>>>wrong format data(height=>400 which is impossible)
#176     68

import pandas as pd
df=pd.read_csv("C:/Users/Tinu/Downloads/python/missing_data1.csv",sep=',')
print(df)
print("---------------------------------------------------------------")
print(df.isna().sum())
print("-------------------------------------------------------------------")

#for removing the wrong data:that is from 7th row and Duration column
#syntax:
df.loc[7,'Duration']=50
print(df)

#find:
#Calories=====>above 375
#Calories======>mean
print("-------------------------------------------------")

x = df['Calories'].mean()
for i in df.index:
    if(df.loc[i,'Calories']>375):
        df.loc[i,'Calories']=x
print(df)




























