# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df= pd.read_csv(path)

pa=df[df['fico']>700].shape[0]

total=df.shape[0]

p_a=pa/total

df1=df[df['purpose']=='debt_consolidation']
pb=df[df['purpose']=='debt_consolidation'].shape[0]

p_b= pb/total

p_b

pab=(df[(df['purpose']=='debt_consolidation') & (df['fico']>700)]).shape[0]

p_a_b=pab/total

result=p_a_b==p_a
print(result)




# code ends here


# --------------
# code starts here
problp=df[df['paid.back.loan'] == 'Yes'].shape[0]

prob_lp=problp/total

probcs=df[df['credit.policy'] == 'Yes'].shape[0]

prob_cs=probcs/total

prob_pd_cs=0.8323182100683655

new_df=df[df['paid.back.loan'] == 'Yes' ]
bayes=(prob_pd_cs*prob_lp)/prob_cs
bayes= np.around(bayes,decimals=4)
print(bayes)



# code ends here


# --------------
# code starts here
import seaborn as sns
sns.countplot(df['paid.back.loan'])
plt.show()
df1 = df[df['paid.back.loan']=='No']
sns.countplot(df['purpose'][df['paid.back.loan']=='No'])
plt.show()
# code ends here


# --------------
# code starts here
inst_median=df['installment'].median()

inst_mean =df['installment'].mean()
plt.hist(df['installment'])
plt.show()
plt.hist(df['log.annual.inc'])
plt.show()



# code ends here


