
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:17:53 2023

@author: jignesh
"""

import pandas as pd # loading entire  liabreary in our script
from pandas import DataFrame
import yfinance as yf

tickers=['GAIL.NS','HDFCLIFE.NS','SHREECEM.NS','LT.NS','ACC.NS']


# tickers=['ADANIPORTS.NS','ASIANPAINT.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJFINANCE.NS','BAJAJFINSV.NS','BPCL.NS',
#           'BHARTIARTL.NS','BRITANNIA.NS','CIPLA.NS','COALINDIA.NS','DIVISLAB.NS','DRREDDY.NS','EICHERMOT.NS',
#           'GAIL.NS','GRASIM.NS','HCLTECH.NS','HDFCBANK.NS','HDFCLIFE.NS','HEROMOTOCO.NS','HINDALCO.NS',
#           'HINDUNILVR.NS','HDFC.NS','ICICIBANK.NS','ITC.NS','IOC.NS','INDUSINDBK.NS','INFY.NS','JSWSTEEL.NS',
#           'KOTAKBANK.NS','LT.NS','M&M.NS','MARUTI.NS','NTPC.NS','NESTLEIND.NS','ONGC.NS','POWERGRID.NS',
#           'RELIANCE.NS','SBILIFE.NS','SHREECEM.NS','SBIN.NS','SUNPHARMA.NS','TCS.NS','TATAMOTORS.NS',
#           'TATASTEEL.NS','TECHM.NS','TITAN.NS','UPL.NS','ULTRACEMCO.NS','WIPRO.NS']

df1=pd.DataFrame()
for i1 in tickers:
    df1[i1]=yf.download(i1,start='2023-01-01', end= '2024-03-06')['Adj Close']

daily_returns=df1.pct_change()
stdev=daily_returns.std()
last_price= df1.tail(1)

UR = last_price * (1+stdev*1.64)
LR = last_price * (1-stdev*1.64)
    
# print (last_price)
# print(stdev)
# print (UR)
# print (LR)

final=pd.concat([UR,LR],axis=0)

# print (final)
# print (daily_returns)
# df1=df1.set_index(pd.DatetimeIndex(df1['Date'].values))

final.to_csv('j:/CSV_newstockdata1.csv')            # stock data
print("done1")



