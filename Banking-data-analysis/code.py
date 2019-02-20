# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  



# path        [File location variable]

#Code starts here
data = pd.read_csv(path)

sample_size=2000
data_sample=data.sample(n=sample_size,random_state=0)

data_sample.head()

sample_mean=317.61

sample_std=207.65

z_critical = stats.norm.ppf(q = 0.95)  
margin_of_error=7.64

a=325.25
b=309.97
confidence_interval=(b,a)


true_mean=data['installment'].mean()










# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
for i in range(len(sample_size)):
    m=[]
    for j in range(1000):
        sample=sample_size==sample_size[i]
        m.append(np.mean(sample))
    mean_series=pd.Series(m)
    plt.hist(mean_series)


# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
data['int.rate']=data['int.rate'].str.replace('%','')

data['int.rate']=pd.to_numeric(data['int.rate'], errors='coerce')

data['int.rate']=data['int.rate']/100

from scipy import stats
from statsmodels.stats.weightstats import ztest


z_statistic,p_value=ztest(x1=data[data['purpose']=='small_business']['int.rate'],value=data['int.rate'].mean(),alternative='larger')

p_value


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
z_statistic,p_value=ztest(x1=data[data['paid.back.loan']=='No']['installment'],x2= data[data['paid.back.loan']=='Yes']['installment'])


# --------------


#Code starts here

#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                    df = 6)   # Df = number of variable categories(in purpose) - 1

yes=(data['purpose'][data['paid.back.loan']=='Yes']).value_counts()

no=(data['purpose'][data['paid.back.loan']=='No']).value_counts()

observed=pd.concat([yes.transpose(),no.transpose()],axis=1,keys=['Yes','No'])

chi2, p, dof, ex=chi2_contingency(observed)

print(chi2, p, dof, ex)

chi2_contingency==critical_value


