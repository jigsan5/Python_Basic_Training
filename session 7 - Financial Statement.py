# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 17:36:34 2023

@author: jignesh
"""

import yfinance as yf
import pandas as pd

tcs = yf.Ticker("TCS.NS")
v = tcs.balance_sheet

# d = tcs.calendar()

tcsinfo = tcs.info

'''
# print (tcsinfo['marketCap'])
# bs1 =tcs.balance_sheet

# print (tcs.history(period="max"))
 print (tcs.dividends)

tcs.dividends.plot()

tcs = yf.Ticker("tcs.NS")

# # get all stock info
info_1= tcs.info

# get historical market data
# hist = tcs.history(period="1mo")
# print (hist)

# # show meta information about the history (requires history() to be called first)
# print (tcs.history_metadata)

# show actions (dividends, splits, capital gains)

print (tcs.actions)
print (tcs.dividends)
print (tcs.splits)
# print (tcs.capital_gains)  # only for mutual funds & etfs

# # show share count
# print (tcs.get_shares_full(start="2022-01-01", end=None))
# tcs.get_shares_full(start="2022-01-01", end=None).plot()

# show financials:
# - income statement
print (tcs.income_stmt)
print (tcs.quarterly_income_stmt) 

# - balance sheet
print (tcs.balance_sheet)
print (tcs.quarterly_balance_sheet)

# # # - cash flow statement
# print (tcs.cashflow)
# print (tcs.quarterly_cashflow)

# # see `Ticker.get_income_stmt()` for more options

# show holders
print (tcs.major_holders)
print (tcs.institutional_holders)
print (tcs.mutualfund_holders)

# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.
print (tcs.earnings_dates)

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
print (tcs.isin)

# # show news
# print (tcs.news)

# # 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, and 3mo
# data = yf.download('TCS.NS',start="2023-08-16", end="2023-08-17",interval="5m")['Close']
# print (data)

'''
