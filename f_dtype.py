import pandas as pd
a=pd.Series([4,5,6,7,8,9,10],dtype=float)
print(a)
print("*"*900)

dic={'id':101,'fname':'vinay','lname':'k','age':30,'prof':'doctor','salary':50000}
b=pd.Series(dic)
print(b)
#for changing the objectives we use "index" function
#ie:
c=pd.Series(dic,index=['fname','lname','id','age','prof','salary'])
print(c)