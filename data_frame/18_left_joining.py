#left outer joining:
#it returns all the rows from left dataframe,plus matche value from right table or null in case of no matching predicate

import numpy as np
import pandas as pd
lst1=[[101,'vinay',20,'python'],
      [102,'kiran',30,'flutter'],
      [103,'lijo',22,'bigdata'],
      [104,'manu',23,'python']]
lst2=[['btech','alpy',200000,104],
      ['msc','coc',332000,105],
      ['bsc','calicut',4000000,106],
      ['btech','alpy',24000,101]]
df1=pd.DataFrame(lst1,columns=['id','fname','age','prof'])
df2=pd.DataFrame(lst2,columns=['qualif','loc','salary','id'])

df3=pd.merge(df1,df2,on='id',how='left')
print(df3)

