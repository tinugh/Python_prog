#how to handle missing values

import pandas as pd
df=pd.read_csv("C:/Users/Tinu/Downloads/python/missing_data1.csv",sep=',')
print(df)
print("---------------------------------------------------------------")
print(df.isna().sum())
print("-------------------------------------------------------------------")
#for filling
# df1=df.fillna(200)
# print(df1)

#without creating new dtaframe
# df.fillna(200,inplace=True)
# print(df)
print('------------------------------------------------------------')
#replace only for specific column
#eg:for filling missing value of Calories
# df['Calories'].fillna(250,inplace=True)
# print(df)
# print("-------------------------------")

#date
# df['Date'].fillna('2020/12/22',inplace=True)
# print(df)

#for filling we use:mean,median,mode
#mean=====> average
#median=====>ascen order,then middile value
#mode======>most frequent value

#mean
print("------------------------------------------------------------------------------------")
x=df['Calories'].mean()
print(x)
df['Calories'].fillna(x,inplace=True)
print(df)
print("---------------------------------------------------------------------------------------------------")

#median
x=df['Calories'].median()
print(x)
df['Calories'].fillna(x,inplace=True)
print(df)
print("---------------------------------------------------------------------------------------------------")

#mode
x=df['Calories'].mode()[0]
print(x)
df['Calories'].fillna(x,inplace=True)
print(df)
print("---------------------------------------------------------------------------------------------------")





















