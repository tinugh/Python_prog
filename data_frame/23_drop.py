#dropping the complete raw of missing value
#function:"dropna()"
import pandas as pd
df=pd.read_csv("C:/Users/Tinu/Downloads/python/missing_data1.csv",sep=',')
print(df)
print("---------------------------------------------------------------")
print(df.isna().sum())
print("-------------------------------------------------------------------")

#Calories
df.dropna(inplace=True)
print(df)

#Date
df.dropna(subset=['Date'],inplace=True)
print(df)














