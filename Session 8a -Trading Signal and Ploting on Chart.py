# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 16:18:58 2023

@author: jignesh
"""

import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Download stock data
tickers = ['TCS.NS']
df = yf.download(tickers, '2018-04-05', '2023-08-14')

# Calculate moving averages
df['df_10'] = df['Close'].rolling(window=10).mean()
df['df_15'] = df['Close'].rolling(window=15).mean()

# Generate trading signals
df['Signal'] = 0
df['Signal'][15:] = np.where(df['df_15'][15:] > df['df_10'][15:], 1, -1)

# Drop NaN rows
df = df.dropna(axis=0)
df['new_position'] = df['Signal'].diff()

# Filter buy and sell signals
df_buy_positiononly = df[df['new_position'] == 2]
df_sell_positiononly = df[df['new_position'] == -2]

# Create a line chart for the stock price
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], label='Stock Price', color='blue', linewidth=2)

# Overlay buy signals (green up arrows)
plt.scatter(df_buy_positiononly.index, df_buy_positiononly['Close'], marker='^', color='green', label='Buy Signal')

# Overlay sell signals (red down arrows)
plt.scatter(df_sell_positiononly.index, df_sell_positiononly['Close'], marker='v', color='red', label='Sell Signal')

# Add labels, legend, and title
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.title('Stock Price with Trading Signals')

# Show the chart
plt.grid()
plt.show()
