#moviesfile
import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/Tinu/Downloads/python/movies_cleaned_new.csv",sep=",")
print(df)

#1:
print("row count =",len(df))
print("---------------------------------------------------------------------------------------")

#2:
df2=df.drop_duplicates()
print(df2)
print("row count:",len(df2))
print("-----------------------------------------------------------------------------------------")

#3:Sort data set by release year in des order
df3=df.sort_values(by='year',ascending=False)
print(df3)
print("------------------------------------------------------------------------------------------")

#4:.Find rating mxm 5 movies name,year,rating
df4=df.sort_values(by='rating',ascending=False)[['name','year','rating']].head(5)
print(df4)
print("-------------------------------------------------------------------------------------------")

#5. Find rating minimum 3 movies name,year,rtaing
df5=df.sort_values(by='rating',ascending=False)[['name','year','rating']].tail(5)
print(df5)
print("---------------------------------------------------------------------------------------------")

#6. Find Each year release movie count [count desc order]
df6=df.groupby('year')['year'].count().sort_values(ascending=False)
print(df6)
print("-----------------------------------------------------------------------------------------------")

#7: Each rating count [count desc order]
df7=df.groupby('rating')['rating'].count().sort_values(ascending=False)
print(df7)
print("-------------------------------------------------------------------------------------------------")

#8: 2008 and rating above 3 [collect]
#A. row count
df8=df.loc[(df['year']==2008)&(df['rating']>3)]
print(df8)
print("row count",len(df8))
print("---------------------------------------------------------------------------------------------------")

#9: Find duration mxm 1 movies name,year,rating,duration
df9=df.sort_values(by='duration')[['name','year','rating','duration']].tail(1)
print(df9)
print("-------------------------------------------------------------------------------------------------")

#10:Find rating mnm 1 movies name,year,rating,duration
df10=df.sort_values(by='duration')[['name','year','rating','duration']].head(1)
print(df10)
print("--------------------------------------------------------------------------------------------------")

#11: Rating above 4 and relase year above 2005
#A. Rating mxm movies full data
#B. Rating mnm movies full data
df11=df.loc[(df['rating']>4)&(df['year']>2005)]
print(df11)
a=df11.groupby('rating').max()
print(a)
b=df11.groupby('rating').min()
print(b)
print("----------------------------------------------------------------------------------------------------")

#12:2008 movies count
df12=df.loc[df['year']==2008]
print("2008 movie count:",len(df12))
print("----------------------------------------------------------------------------------------------------")

#13:1975-2000 movies collect
#A. Row count
df13=df.loc[(df['year']>1975)&(df['year']<2000)]
print(df13)
print("row count:",len(df13))
print("---------------------------------------------------------------------------------------------------")

#14:1975-2000 and rating above 3.5 total row count
df14=df.loc[(df['year']>1975)&(df['year']<2000)&(df['rating']>3.5)]
print(df14)
print("row count:",len(df14))

































