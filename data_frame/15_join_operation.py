#combination of two data frames'

#4 types of join operations
#1;normal/inner join
#2;left outer join
#3;right outer join
#4;full outer join

#df1
# 101 vinay k 24 bigdata 1000
# 102 lijo m  23 python  2000

#df2
# btech  1234  m  102
# bsc    6870  f  103
# msc    9876  m  101

#101 vinay k 24 bigdata 1000 msc    9876  m
#102 lijo m  23 python  2000 btech  1234  m  102

#syntax:
#newdfname=pd.merge(df1,df2,on='colname',how='inner')

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
print(df1)
print(df2)
print("--------------------------------------------------------------------------------------------------")

#newdfname=pd.merge(df1,df2,on='colname',how='inner')
df3=pd.merge(df1,df2,on='id',how='inner')
print(df3)






























