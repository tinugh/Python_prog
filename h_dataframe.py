#2d datas
#nested lst
import pandas as pd
lst=[[101,'vinay','k',27,'bigdata',100000],
     [102,'manu','j',20,'doctor',20000],
     [103,'rahul','m',23,'python',40000],
     [104,'kiran','l',30,'bigdata',38000]]
df=pd.DataFrame(lst)

df.columns=['id','fname','lname','age','prof','salary']
print(df)

print("*"*900)
print(df.head(2))
print(df.tail(2))
print("*"*900)
#for print column name
print(df.columns)


#describe() function:
#summrised form

print(df.describe())

print("'"*9000)
#for othr tha numerical vlues ie object
print(df.describe(include='O'))

#for complete value
print("*"*900)
print(df.describe(include='all'))
#here NaN" means not a number

#how to add new columns
df['gender']=['m','m','f','f']
print(df)


df['loc']=['alpy','coc','alpy','tvm']
print(df)














