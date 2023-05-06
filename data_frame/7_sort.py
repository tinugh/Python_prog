#sorting can be done in ascending and descending order
#syntax:
#newdfname=olddfnme.sort_values(by='colnme')

import pandas as pd
lst=[[101,'vinay','k',27,'bigdata',100000],
     [102,'manu','j',20,'doctor',20000],
     [103,'rahul','m',23,'python',40000],
     [104,'kiran','l',30,'bigdata',38000]]
df=pd.DataFrame(lst)

df.columns=['id','fname','lname','age','prof','salary']
print(df)

print("*"*900)

df1=df.sort_values(by='age')
print(df1)
print("-------------------------------------------------------------------------------------")

df2=df.sort_values(by='age',ascending=False)
print(df2)

#obj can also be sorted 'a to z'














