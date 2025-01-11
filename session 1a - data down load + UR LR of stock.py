# data = pd.read_csv('j:/CSV_newstockdata1.csv')   
# df = pd.DataFrame(data)
# df = data.pct_change()

import pandas as pd
import yfinance as yf

df = pd.DataFrame()    # created a blank dataframe

tickers_list = ['TCS.NS', 'LT.NS', 'ACC.NS', 'ABB.NS', 'GAIL.NS']
df = yf.download(tickers_list,'2020-08-1')['Open']
# print (df)

df2 = df.dropna(axis=1,how='all')

print (df2.shape[1])

df2.to_csv('j:/Balaji_Test.csv')
read_CSV = pd.read_csv('j:/Balaji_Test.csv') 

daily_returns = df2.pct_change()
# print (read_CSV.tail())

stdev = daily_returns.std()
print (stdev)

last_price= df2.tail(1)
print (last_price)

UR = last_price * (1+stdev*2.33) 
print (UR)

((df2.pct_change()+1).cumprod()).plot(figsize=(10, 7))