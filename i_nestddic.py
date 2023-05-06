import pandas as pd
#nested list
dic={'id':[101,102,103,104,105],
     'fname':['kiran','manu','anu','rahul','richard'],
     'lname':['k','l','k','j','m'],
     'age':[20,20,22,21,24],
     'location':['alpy','kochi','tvm','alpy','malp'],
     'phno':[67576364,45564787,67899889,809099,6563464]}

df=pd.DataFrame(dic)
print(df)
