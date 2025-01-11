import pandas as pd 
import yfinance as yf

df = yf.download('^NSEI', start = '2022-07-01', end = '2023-08-14')
# df1.to_csv('j:/CSV_newstockdata1.csv')   

# 1. Calculating Average Price
df['new_average']= df['Close'].mean()

# 2. Calculating Simple Rate of Return - Fierstprice and Last Price  
simple_return = ((df['Close'][-1] - df['Close'][0]) / df['Close'][0])*100
print (df['Close'][-1])

# 3. Calculating Daily Returns--method 1 
df['t-1']=df['Close'].shift(1)
df['Daily Return_method1']=((df['Close']-df['t-1'])/df['t-1'])*100

# 4. Calculating Daily Returns--method 2 
df['Daily Return_method2'] = (df['Close'].pct_change(1)) *100

# 4.Calculating Standard Deviation
std_dev = df['Close'].std()
round(std_dev,2)

# 5. Calculating Minimum & Maximum Values
minimum_value = df['Close'].min()
round(minimum_value,2)

maximum_value = df['Close'].max()
round(maximum_value,2)

# 6. Calculating Simple Moving Average
df['MA5'] = df['Close'].rolling(window=5).mean()
df['MA20'] = df['Close'].rolling(window=20).mean()

# 7. Calculating Correlation
df2 = yf.download('INFY.NS', start = '2022-07-01', end = '2023-08-14')
correlation = df['Close'].corr(df2['Close'], method = 'pearson')
print (round(correlation, 2))

# 8. Calculating Beta.
      # NIFTY is an index that tracks the performance of 50 companies. 
      # We will calculate INFOSYS beta against NSE. 
      # INFY’s beta = correlation x (INFY’s standard dev / NIFTY’s standard dev)

df3 = yf.download('INFY', start = '2022-07-01', end = '2023-03-02')
df3['Daily Return_INFY'] =df3['Close'].pct_change(1)

correlation_NIFTY_INFY = df3['Daily Return_INFY'].corr(df['Daily Return_method2'])
NIFTY_std_returns = round(df['Daily Return_method2'].std()/100,3)
INFY_std_returns = round(df3['Daily Return_INFY'].std(),3)
INFY_beta = correlation_NIFTY_INFY * (INFY_std_returns/NIFTY_std_returns)
print (round(INFY_beta,2))
print (df['Close'].describe())

