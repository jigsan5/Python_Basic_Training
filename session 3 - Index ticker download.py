# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 18:41:09 2023

@author: jignesh
"""

import yfinance as yf
import pandas as pd

# Read and print the stock tickers that make up S&P500
tickers = pd.read_html(https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
print(tickers.head())

# Get the data for this tickers from yahoo finance
data = yf.download(tickers.Symbol.to_list(),'2021-1-1','2021-7-12', auto_adjust=True)['Close']
print(data.head())

tickers = pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50')[2]
print(tickers.head())
tickers['new_symbol'] = tickers['Symbol'].astype(str) + '.NS' 
print(tickers.head())

# Get the data for this tickers from yahoo finance
data = yf.download(tickers.new_symbol.to_list(),'2023-08-10','2023-8-17', auto_adjust=True)['Close']
print(data.head())