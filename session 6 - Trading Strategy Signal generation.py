# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 18:18:03 2023

@author: jignesh
"""

import yfinance as yf

df = yf.download('TCS.NS', start = '2022-02-20', end = '2023-03-03')
df['MA10'] = df['Close'].rolling(window=10).mean()
df['MA20'] = df['Close'].rolling(window=20).mean()

df['Signal'] = 0

for i in range(len(df)):
    if (df.iloc[i,6] < df.iloc[i,7]) and (df.iloc[i,3] > df.iloc[i-1,3]*1.02):
        df.iloc [i,8]=1

# conditional filter of rows 
print (df[df['Signal']==1])