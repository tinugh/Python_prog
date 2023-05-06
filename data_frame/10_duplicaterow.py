#for duplicate row drop we use :
#drop_duplicates()
import pandas as pd
lst=[[101,'vinay','k',27,'bigdata',100000],
     [102,'manu','j',20,'doctor',20000],
     [103,'rahul','m',23,'python',40000],
     [104,'kiran','l',30,'bigdata',38000],
     [103,'rahul','m',23,'python',40000],
     [104,'kiran','l',30,'bigdata',38000]]
df=pd.DataFrame(lst)

df.columns=['id','fname','lname','age','prof','salary']
print(df)

print("*"*900)
df1=df.drop_duplicates()
print(df1)
print("-----------------------------------------------")

#how to drop a column
#syntax: newdf_name=olddfname.drop(['colname'],axis=1)

df1=df.drop(["id"],axis=1)
print(df1)
print("------------------------")

#for multiple columns:
df2=df.drop(["id","fname"],axis=1)
print(df2)




















