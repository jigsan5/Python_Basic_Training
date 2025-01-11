# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 20:06:06 2023

@author: jignesh
"""

# The goodness of fit test
observed = [54,38,8]
expectation = [45,35,20]
   
x = sum([(o-e)**2./e for o,e in zip(observed,expectation)])
#chi square = 9.257


#import chi2 from scipy to get the critical value
from scipy.stats import chi2
alpha = 0.05 # confidence level 
df = 2
cr=chi2.ppf(q=1-alpha,df=df)
#critical value is 5.991

