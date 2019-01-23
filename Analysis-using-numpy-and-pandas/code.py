# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data_file=path # path for the file
data=np.genfromtxt(data_file, delimiter=",", skip_header=1)

print("\nData: \n\n", data)

print("\nType of data: \n\n", type(data))
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
census=np.concatenate((data,new_record),axis=0)


# --------------
#Code starts here
age= census[0:,0:1]

max_age=age.max()

min_age=age.min()

age_mean= age.mean()

age_std = age.std()


# --------------
#Code starts here
import numpy  as np
import pandas as pd 
df = pd.read_csv(path)
a=df[df['race']==0]
race_0=np.array(a)
b=df[df['race']==1]
race_1=np.array(b)  
c=df[df['race']==2]
race_2=np.array(c)  
d=df[df['race']==3]
race_3=np.array(d)  
e=df[df['race']==4]
race_4=np.array(e)    

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=848



minority_race= 3


# --------------
#Code starts here
senior_citizen=df[df['age']>60]
senior_citizens=np.array(senior_citizen)
working_hours_sum=senior_citizen['hours-per-week'].sum()

senior_citizens_len=len(senior_citizen)

avg_working_hours=working_hours_sum/senior_citizens_len

print(avg_working_hours)


# --------------
#Code starts here
highs=df[df['education-num']>10]
lows=df[df['education-num']<=10]
high=np.array(highs)
low=np.array(lows)

avg_pay_high=highs['income'].sum()/len(highs['income'])
avg_pay_low=lows['income'].sum()/len(lows['income'])

print(avg_pay_high, 
avg_pay_low)


