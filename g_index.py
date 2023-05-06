import pandas as pd
a=pd.Series([4,5,6,7,8,9,1,11,15],index=[2,3,0,5,8,7,4,1,6])
print(a)

b=pd.Series([2,3,4,5,6,7])
c=pd.Series([1,3,5,6,7,8])
print(b)
print(c)

#for adding
d=b.add(c)
print(d)

#for subt
e=b.subtract(c)
print(e)
print("*"*900)

#for multiplying
f=b.multiply(c)
print(f)
print("*"*900)

#for divide
g=b.div(c)
print(g)
