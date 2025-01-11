# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 18:58:48 2024

@author: jignesh
"""

import pandas as pd # loading entire  liabreary in our script
from pandas_datareader import data as wb # importing only 1 module from data 
from pandas import DataFrame
import yfinance as yf

tickers=['GAIL.NS','HDFCLIFE.NS']

# type , how to access data , insert, append,extend, pop , clear , remove
# Looping list  
print (type(tickers))

tickers.append('ACC.NS')
tickers.insert(2, 'INFY.NS')
tickers.append('LT.NS')
print (tickers[2:4])
print (tickers)

tickers.remove(tickers[1])
print (tickers)

tickers[2]=5
print (tickers)

print(len(tickers))

# if 5 in tickers:
#     print('ok')

for i in range(len(tickers)):
    if tickers[i]=='LT.NS':
        print(i)
        
for i in range(len(tickers)):
    print (tickers[i])
    if tickers[i]=='INFY.NS':
        break


    
    
        
