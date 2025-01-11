# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 17:04:50 2023

@author: jignesh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


# Load historical stock price data for 4 stocks
# Replace 'stock1.csv', 'stock2.csv', 'stock3.csv', and 'stock4.csv' with your data
# df = yf.download('^NSEI', start = '2022-07-01', end = '2023-08-14')

stock1_data = yf.download('TCS.NS', '2021-01-01', '2023-08-14')
stock2_data = yf.download('INFY.NS', '2021-01-01', '2023-08-14')
stock3_data = yf.download('ABB.NS', '2021-01-01', '2023-08-14')
stock4_data = yf.download('ACC.NS', '2021-01-01', '2023-08-14')

# Calculate daily returns for each stock
returns1 = stock1_data['Adj Close'].pct_change()
returns2 = stock2_data['Adj Close'].pct_change()
returns3 = stock3_data['Adj Close'].pct_change()
returns4 = stock4_data['Adj Close'].pct_change()

# Combine returns into a DataFrame
portfolio_returns = pd.DataFrame({
    'Stock1': returns1,
    'Stock2': returns2,
    'Stock3': returns3,
    'Stock4': returns4
})


# Assume a risk-free rate (e.g., 10-year 7% GoI yield)
risk_free_rate = 0.02  # Replace with the actual risk-free rate

# Calculate the mean and standard deviation of portfolio returns
mean_returns = portfolio_returns.mean()
std_returns = portfolio_returns.std()

# # Calculate the Sharpe ratio for each stock
sharpe_ratios = (mean_returns - risk_free_rate) / std_returns


# # Calculate the overall portfolio Sharpe ratio (assuming equal weights)
portfolio_weights = [0.25, 0.25, 0.25, 0.25]  # Adjust weights as needed
portfolio_return = np.dot(mean_returns, portfolio_weights)
portfolio_std = np.sqrt(np.dot(portfolio_weights, np.dot(portfolio_returns.cov(), portfolio_weights)))
portfolio_sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_std

# # Print Sharpe ratios for individual stocks
print("Individual Stock Sharpe Ratios:")
print(sharpe_ratios)

# # Print portfolio Sharpe ratio
print("\nPortfolio Sharpe Ratio:")
print(portfolio_sharpe_ratio)

# # Plot the historical portfolio returns
portfolio_cumulative_return = (1 + portfolio_returns).cumprod()
plt.plot(portfolio_cumulative_return.index, portfolio_cumulative_return, label='Portfolio')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.title('Portfolio Cumulative Returns')
plt.legend()
plt.show()





