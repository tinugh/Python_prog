#condition satisfying data collection:'filter'
#function:"loc"

#syntax :
#newdfname=olddfname.loc[dfname['colname']condition]
import pandas as pd
lst=[[101,'vinay','k',27,'bigdata',100000],
     [102,'manu','j',20,'doctor',20000],
     [103,'rahul','m',23,'python',40000],
     [104,'kiran','l',30,'bigdata',38000]]
df=pd.DataFrame(lst)

df.columns=['id','fname','lname','age','prof','salary']
print(df)

print("*"*900)
df1=df.loc[df['age']>28] [['fname','lname','age','prof']]
print(df1)













