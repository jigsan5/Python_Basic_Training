# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 19:47:37 2023

@author: jignesh
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

data = pd.read_csv('j:/HR-Employee-Attrition.csv')

# print (data.isna().any())

print (data['Attrition'].value_counts())
print (data['JobSatisfaction'].value_counts())

# Null Hypothesis : there is no significant relationship between ‘Attrition’ and ‘JobSatisfaction’.

print (pd.crosstab(data.Attrition, data.JobSatisfaction, margins=True))

ct = pd.crosstab(data.Attrition, data.JobSatisfaction, margins=True)

# print (ct.iloc[0:2,4].values)

obs = np.append(ct.iloc[0][0:4].values, ct.iloc[1][0:4].values)
print (obs) 

row_sum = ct.iloc[0:2,4].values
exp = []
for j in range(2):
    for val in ct.iloc[2,0:4].values:
        exp.append(val * row_sum[j] / ct.loc['All', 'All'])

print (exp)

chi_sq_stats = ((obs - exp)**2/exp).sum()
print (chi_sq_stats)

# dof = (number of categories in the first variable-1)*(number of categories in the second variable-1), 
# and it is (2–1)*(4–1) in this case, or 3.

dof = (len(row_sum)-1)*(len(ct.iloc[2,0:4].values)-1)
print (dof)

critical_value = 1 - stats.chi2.cdf(chi_sq_stats, dof)
print (critical_value)

# *******Use SciPy to double check*****
obs = np.array([ct.iloc[0][0:4].values,ct.iloc[1][0:4].values])
print (stats.chi2_contingency(obs)[0:3])
'''
# Another Case : 'Attrition' vs 'WorkLifeBalance'
ct = pd.crosstab(data.Attrition, data.WorkLifeBalance, margins=True)
print (ct)
obs = np.array([ct.iloc[0][0:4].values,ct.iloc[1][0:4].values])
print (stats.chi2_contingency(obs)[0:3])


# Another Case : 'Attrition' vs 'Education':
ct = pd.crosstab(data.Attrition, data.Education, margins=True)
print (ct)
obs = np.array([ct.iloc[0][0:5].values,ct.iloc[1][0:5].values])
print (stats.chi2_contingency(obs)[0:3])
# Since the p-value is high, we conclude that attrition is independent of education level.

# Another case : Attrition and Job Satisfaction is agnostic to department:
dep_counts = data['Department'].value_counts()
print (dep_counts)
ct = pd.crosstab(data.Attrition, data.Department, margins=True)
print (ct)

alpha = 0.05
for i in dep_counts.index[0:2]:
    sub_data = data[data.Department == i]
    ct = pd.crosstab(sub_data.Attrition, sub_data.WorkLifeBalance, margins=True)
    obs = np.array([ct.iloc[0][0:4].values,ct.iloc[1][0:4].values])
    print("For " + i + ": ")
    print(ct)
    print('With an alpha value of {}:'.format(alpha))
    if stats.chi2_contingency(obs)[1] <= alpha:
        print("Dependent relationship between Attrition and Work Life Balance")
    else:
        print("Independent relationship between Attrition and Work Life Balance")
    print("")

 
'''