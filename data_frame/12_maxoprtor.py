#max
#syntax:newdfname=olddfname.groupby('colname')['colname'].max()
#each proff count
#each location count
#each profession max salary
#each location max salary

import pandas as pd
df=pd.read_csv('C:/Users/Tinu/Downloads/python/customer.unknown',sep=',',header=None)

df.columns=['id','fname','lname','age','prof','loc']
print(df)
print("'"*900)


