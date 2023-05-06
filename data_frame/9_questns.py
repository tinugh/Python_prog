#customer
#1:fnme,lname,age,loc,[data_frame]
#2:find total number of missing values
#3:missing values filled by india
#4:india fname,lname,age,prof
#5:india work and age above 40 fname,lnmae,age,prof
#6:us data collect
#7:us work ,age max 5 employee fname,lname,age,prof
#8:india work,age min 3 employee fname,lname,age,prof
#9:uk work age range btw 25 to 35(include)
#10:australia agr max 1 employee full data
#11:pilot prof age max 1 employees fname,lname,age,loc
#12:us and prof musician age max 1 employee full data



import pandas as pd
df=pd.read_csv('C:/Users/Tinu/Downloads/python/customer.unknown',sep=',',header=None)

df.columns=['id','fname','lname','age','prof','loc']
print(df)
print("'"*900)

#q2:
print(df.isna().sum())
print("========================================================")

#q3
df3=df.fillna("india")
print(df3)
print(df3.isna().sum())
print("=============================================")

#q4:
df4=df.loc[df['loc']=='india'] [['fname','lname','age','prof']]
print(df4)
print("------------------------------------------------------")

#q5:
df5=df.loc[(df['loc']=='india')&(df['age']>40)] [['fname','lname','age','prof']]
print(df5)
print("--------------------------------------------")

#q6:
df6=df.loc[df['loc']=='us']
print(df6)
print("--------------------------------------")

#q7:
df7=df.loc[df['loc']=='us'].sort_values(by='age') [['fname','lname','age','prof']].tail(5)
print(df7)
print("---------------------------------------------")

#q8:
df8=df.loc[df['loc']=='india'].sort_values(by='age') [['fname','lname','age','prof']].head(3)
print(df8)
print("---------------------------------------")

#q9:
df9=df.loc[(df['loc']=='uk')&(df['age']>=25)&(df['age']<=35)]
print(df9)
print("----------------------------------------------")

#q10:
df10=df.loc[df['loc']=='australia'].sort_values(by='age').tail(1)
print(df10)
print("---------------------------------------")

#q11:
df11=df.loc[df['prof']=='Pilot'].sort_values(by='age') [['fname','lname','age','prof']].tail(1)
print(df11)
print("---------------------------------------")

#q12:
df12=df.loc[(df['loc']=='us')&(df['prof']=='Musician')].sort_values(by='age').tail(1)
print(df12)









