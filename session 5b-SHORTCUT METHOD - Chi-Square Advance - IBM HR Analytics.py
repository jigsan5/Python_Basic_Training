# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 16:52:14 2023

@author: jignesh
"""
import pandas as pd
from scipy.stats import chi2_contingency

data= pd.read_csv('j:/HR-Employee-Attrition.csv')


print (data.columns)
# print (data['Attrition'].values)
# print (data['Attrition'].value_counts())
print (data['Department'].value_counts())
# print (data.isna().any())
print (data['Attrition'].value_counts())
print (data['JobSatisfaction'].value_counts())

ov_table = pd.crosstab(data['Attrition'], data['Department']) 

chi2, p, dof, expected = chi2_contingency(ov_table)
print (chi2)
print (p)
print (dof)
print (expected)

alpha = 0.05  # Significance level

print(f"Chi-squared test statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of freedom: {dof}")
print("Expected frequencies:")
print(expected)

if p < alpha:
    print("Reject the null hypothesis: There is a significant association between the variables.")
else:
    print("Fail to reject the null hypothesis: There is no significant association between the variables.")


# contingency_table = pd.crosstab(index=[data['Attrition'], data['JobSatisfaction'],data['Department']], columns=data['Over18'])