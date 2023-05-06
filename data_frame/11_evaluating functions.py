# #evaluating functions are:it cannot be directly performed so first group must be performed
# COUNT
# SUM
# MAX
# MIN
# MEAN

#count:#for finding corresponding column count
#step1:grouping the counting value
#syntax:newdfnme=olddfname.groupby('colname')['colname'].count()
import pandas as pd
df=pd.read_csv('C:/Users/Tinu/Downloads/python/customer.unknown',sep=',',header=None)

df.columns=['id','fname','lname','age','prof','loc']
print(df)
print("'"*900)

df1=df.groupby('prof')['prof'].count()
print(df1)
print("-----------------------------------------------")

#for ascendng order
df2=df.groupby('prof')['prof'].count().sort_values()
print(df2)
print("-----------------------------------------")
#for descending
df3=df.groupby('prof')['prof'].count().sort_values(ascending=False)
print(df3)
print("--------------------------------------")

#each country count
df4=df.groupby('loc')['loc'].count().sort_values(ascending=False)
print(df4)






















