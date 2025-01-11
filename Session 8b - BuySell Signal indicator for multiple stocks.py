# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 08:37:44 2023

@author: jignesh
"""

import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

tickers = ['TCS.NS','LT.NS']
df = yf.download(tickers ,'2023-04-05','2023-08-14')['Close']

df_10= df.rolling(window=10).mean() 
df_12= df.rolling(window=12).mean() 

df_signal =pd.DataFrame()
for s in df.index:
    for c in tickers:
        # print (df.loc[s,c]) 
        if df_12.loc[s,c] > df_10.loc[s,c]:
            df_signal.loc[s,c]= 'Buy'
        else :
            df_signal.loc[s,c]= 'Sell'
            
            
df_master = pd.concat([df,df_10,df_12,df_signal],axis=1)

df_master = df_master.dropna(axis=0)
       


    