# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 # code starts here
house= pd.read_csv(path)
bank=pd.DataFrame(house)
categorical_var=bank.select_dtypes(include = ['object'])
print(categorical_var)
numerical_var = bank.select_dtypes(include=['number'])
print(numerical_var)




# code ends here


# --------------
# code starts here

banks=bank.drop('Loan_ID',axis=1)

bank_mode=banks.mode()
banks.isnull().sum()
banks=banks.fillna(bank.mode)
banks.isnull().sum()

#code ends here


# --------------
avg_loan_amount=pd.pivot_table(data=banks,index=['Gender', 'Married', 'Self_Employed'],values=['LoanAmount'],aggfunc='mean')
avg_loan_amount


# --------------
# code starts here
loan_approved_se=banks['Self_Employed'][(banks['Self_Employed'] == 'Yes' )&( banks['Loan_Status'] == 'Y')].count()

loan_approved_nse=banks['Self_Employed'][(banks['Self_Employed'] == 'No' )&( banks['Loan_Status'] == 'Y')].count()


percentage_se=(loan_approved_se/614)*100

percentage_nse=(loan_approved_nse/614)*100
# code ends here


# --------------
# code starts here
loan_term=banks['Loan_Amount_Term'].apply(lambda x:x/12)
big_loan_term=len(loan_term[loan_term>=25])



# code ends here


# --------------
# code starts here
loan_groupby=banks.groupby(by='Loan_Status')

loan_groupby=loan_groupby[['ApplicantIncome', 'Credit_History']]

mean_values=loan_groupby.mean()




# code ends here


