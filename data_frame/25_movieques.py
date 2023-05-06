#1: data frame
#2:find total number of missing values
#3:rting=====>mean()
#4:duration====>median()
#5:duration 7500, duration mean replace
#pure data set=====>document

#1: data frame
import pandas as pd
df=pd.read_csv("C:/Users/Tinu/Downloads/python/movies.csv",sep=',',header=None)
df.columns=['id','name','year','rating','duration']
print(df)
print("-----------------------------------------------------")

#2:find total number of missing values
print(df.isna().sum())
print("----------------------------------------------------------------")

#3:rting=====>mean()
x=df['rating'].mean()
print(x)
df['rating'].fillna(x,inplace=True)
print(df)
df1=df.isna().sum()
print(df1)
print("-------------------------------------------------------------------------------------------")

#4:duration====>median()
y=df['duration'].median()
print(y)
df['rating'].fillna(y,inplace=True)
print(df)
df2=df.isna().sum()
print(df2)
print("----------------------------------------------------------------------------------------------------------")

#5:duration>7500, duration mean replace
z=df['duration'].mean()
for i in df.index:
    if df.loc[i,'duration']>7500:
        df.loc[i,'duration']=x
print(df)
print("-------------------------------------------------------------------------------")

#pure data set=====>document
df.to_csv('/Home/Downloads/python/movies_new.csv',index=None)
print(df)























