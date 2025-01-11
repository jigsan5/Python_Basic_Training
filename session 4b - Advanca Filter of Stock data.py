# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 13:11:58 2023

@author: jignesh
"""

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import yfinance as yf


aapl = yf.download('AAPL' ,'2006-10-1')
# print (aapl.head())

# # Inspect the index 
# print(aapl.index)

# # Inspect the columns
# print(aapl.columns)

# # Select only the last 10 observations of `Close`
# ts = aapl['Close'][-10:]
# print (ts)

# # Check the type of `ts` 
# print (type(ts))

# # Inspect the rows of November-December 2006
# print(aapl.loc[pd.Timestamp('2006-11-01'):pd.Timestamp('2006-12-31')].head())

# # Inspect the rows of 2007 
# print(aapl.loc['2022'])

# # Inspect November 2006
# print(aapl.iloc[22:43])

# # # Inspect the 'Open' and 'Close' values at 2006-11-01 and 2006-12-01
# print(aapl.iloc[[22,43], [0, 3]])

# # Sample 20 rows
# sample = aapl.sample(20)
# print(sample)

# Add a column `diff` to `aapl` 
aapl['diff'] = aapl.Open - aapl.Close
print (aapl['diff'])

# Delete the new `diff` column
del aapl['diff']

# Plot the closing prices for `aapl`
aapl['Close'].plot(grid=True)
# Show the plot
plt.show()

