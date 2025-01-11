# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 18:30:54 2023

@author: jignesh
"""
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import yfinance as yf

aapl = yf.download('TCS.NS', start='2006-10-1',  end=datetime.datetime(2012, 1, 1))
print (aapl.head())
print(aapl.index) # Inspect the index 
print(aapl.columns) # Inspect the columns
ts = aapl['Close'][-10:] # Select only the last 10 observations of `Close`
type(ts) # Check the type of `ts` 

'''
# Inspect the rows of November-December 2006
print(aapl.loc[pd.Timestamp('2006-11-01'):pd.Timestamp('2006-12-31')].head())
# # Inspect the rows of 2007 
# print(aapl.loc['2007'].head())
# # Inspect November 2006
# print(aapl.iloc[22:43])
# # Inspect the 'Open' and 'Close' values at 2006-11-01 and 2006-12-01
# print(aapl.iloc[[22,43], [0, 3]])

# Add a column `diff` to `aapl` 
aapl['diff'] = aapl['Open'] - aapl['Close']
# Delete the new `diff` column
del aapl['diff'] 
aapl.drop(['Open', 'High','Low','Adj Close','Volume'], axis=1, inplace=True)

# Plot the closing prices for `aapl`
aapl['Close'].plot(grid=True)
plt.show() # Show the plot

aapl['daily_return'] = aapl['Close'].pct_change()
aapl['daily_return_anothermethod'] = aapl['Close'] / aapl['Close'].shift(1) - 1
aapl['daily_Log_return'] = np.log(aapl['Close'].pct_change())
# print (aapl)

# Plot the distribution of `daily_pct_c`
aapl['daily_return'].hist(bins=50)
plt.show()
# Pull up summary statistics
print(aapl['daily_return'].describe())

# Calculate the cumulative daily returns
cum_daily_return = (1 + aapl['daily_return']).cumprod()
print(cum_daily_return)

# Resample the cumulative daily return to cumulative monthly return 
cum_monthly_return = cum_daily_return.resample("M").mean()
print(cum_monthly_return)

# Calculate the moving average
moving_avg = aapl['Close'].rolling(window=40).mean()
print (moving_avg[-10])

# Short moving window rolling mean
aapl['40'] = aapl['Close'].rolling(window=40).mean()
# Long moving window rolling mean
aapl['252'] = aapl['Close'].rolling(window=252).mean()
# Plot the adjusted closing price, the short and long windows of rolling means
aapl[['Close', '40', '252']].plot()

# Volatility 

min_periods = 75 # Define the minumum of periods to consider 
vol = aapl['daily_return'].rolling(min_periods).std() * np.sqrt(min_periods) # volatility calculation
vol.plot(figsize=(10, 8))
plt.show()
'''

# ******Trading Strategy****** 
# Initialize the short and long windows
short_window = 40
long_window = 100

# Initialize the `signals` DataFrame with the `signal` column
signals = pd.DataFrame(index=aapl.index)
signals['signal'] = 0.0

# Create short simple moving average over the short window
signals['short_mavg'] = aapl['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Create long simple moving average over the long window
signals['long_mavg'] = aapl['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()


# Initialize the plot figure
fig = plt.figure()

# Add a subplot and label for y-axis
ax1 = fig.add_subplot(111,  ylabel='Price in $')

# Plot the closing price
aapl['Close'].plot(ax=ax1, color='r', lw=2.)

# Plot the short and long moving averages
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

# Plot the buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index, 
         signals.short_mavg[signals.positions == 1.0],
         '^', markersize=10, color='m')
         
# Plot the sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index, 
         signals.short_mavg[signals.positions == -1.0],
         'v', markersize=10, color='k')
         
# Show the plot
plt.show()


# *******Backtesting A Strategy******
# Implementation Of A Simple Backtester With Pandas

# Set the initial capital
initial_capital= float(100000.0)

# Create a DataFrame `positions`
positions = pd.DataFrame(index=signals.index).fillna(0.0)
# Buy a 100 shares
positions['AAPL'] = 100*signals['signal']   
# Initialize the portfolio with value owned   
portfolio = positions.multiply(aapl['Close'], axis=0)
# Store the difference in shares owned 
pos_diff = positions.diff()
# Add `holdings` to portfolio
portfolio['holdings'] = (positions.multiply(aapl['Close'], axis=0)).sum(axis=1)
# Add `cash` to portfolio
portfolio['cash'] = initial_capital - (pos_diff.multiply(aapl['Close'], axis=0)).sum(axis=1).cumsum()   
# Add `total` to portfolio
portfolio['total'] = portfolio['cash'] + portfolio['holdings']

# Add `returns` to portfolio
portfolio['returns'] = portfolio['total'].pct_change()
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Portfolio value in $')

# Plot the equity curve in dollars
portfolio['total'].plot(ax=ax1, lw=2.)

# Plot the "buy" trades against the equity curve
ax1.plot(portfolio.loc[signals.positions == 1.0].index, 
         portfolio.total[signals.positions == 1.0],
         '^', markersize=10, color='m')

# Plot the "sell" trades against the equity curve
ax1.plot(portfolio.loc[signals.positions == -1.0].index, 
         portfolio.total[signals.positions == -1.0],
         'v', markersize=10, color='k')

# Show the plot
plt.show()

# ***** Evaluating Moving Average Crossover Strategy
# Sharpe Ratio

# Isolate the returns of your strategy
returns = portfolio['returns']
# annualized Sharpe ratio
sharpe_ratio = np.sqrt(252) * (returns.mean() / returns.std())
# Print the Sharpe ratio
print(sharpe_ratio)

# Maximum Drawdown¶
# Define a trailing 252 trading day window
window = 252
# Calculate the max drawdown in the past window days for each day
rolling_max = aapl['Close'].rolling(window, min_periods=1).max()
daily_drawdown = aapl['Close']/rolling_max - 1.0

# Calculate the minimum (negative) daily drawdown
max_daily_drawdown = daily_drawdown.rolling(window, min_periods=1).min()

# Plot the results
daily_drawdown.plot()
max_daily_drawdown.plot()

# Show the plot
plt.show()

# Compound Annual Growth Rate (CAGR)
# Get the number of days in `aapl`
days = (aapl.index[-1] - aapl.index[0]).days

# Calculate the CAGR 
cagr = ((((aapl['Close'][-1]) / aapl['Close'][1])) ** (365.0/days)) - 1

# Print CAGR
print(cagr)


'''
# Resample `aapl` to business months, take last observation as value 
monthly = aapl.resample('BM').apply(lambda x: x[-1])
# Calculate the monthly percentage change
monthly.pct_change()
# Resample `aapl` to quarters, take the mean as value per quarter
quarter = aapl.resample("4M").mean()
# Calculate the quarterly percentage change
quarter.pct_change()
'''