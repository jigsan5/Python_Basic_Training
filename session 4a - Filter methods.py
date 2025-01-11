# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 11:48:17 2023

@author: jignesh
"""


import pandas as pd
spotify_df = pd.read_csv('j:/spotify_weekly_chart.csv')
# print (spotify_df.head(15))
# print (spotify_df.info())


spotify_df['Artist'] = spotify_df['Artist'].str.strip() # remove spaces from Artist column 
spotify_df['Title'] = spotify_df['Title'].str.strip()  # remove spaces from Title column 

# Filtering 1 : select all rows where the value in the “Weeks” column is greater than 30
df1 = spotify_df['Wks'] > 30
print (df1)

#  Filter 2: select all rows where the value in the ‘Title’ column is ‘Sunflower’ and the value in the ‘Wks’ column is greater than 30
# df2 = (spotify_df['Title']=='Sunflower') & (spotify_df['Wks']>30) 
# print(type(df2))
# print (spotify_df.loc[df2]) 

# Filter 3 :filter by position instead of by condition, you can use .iloc. 
# The following code returns all rows in position 0 through 4, and the first 3 columns:
# print (spotify_df.iloc[:5, :3])

# Filter 4 : query function returns Data fram eobject 
# df3 = spotify_df.query('Title == "Sunflower" and Wks > 30')
# print (type(df3))
# print (df3)


# Filter 5 : Filter selcted Rows or COlumns
# df4 =spotify_df.filter(items=['Artist', 'Title']) 
# print (type(df4))
# print (df4)

# Filter 6 : select the 10 records with the most streams, here’s the code:
# df5 = spotify_df.nlargest(10, 'Streams')
# print (type(df5)) 
# print (df5)

# Filter 7 : All records with values between 20 and 30 in the ‘Wks’ column, inclusive
# df6 = spotify_df[spotify_df['Wks'].between(20,30)]
# print (type(df6)) 
# print (df6)

# # Filter 8 :select all rows where the “Artist” column includes the string “Doja Cat”
# df7 = spotify_df[spotify_df['Artist'].isin(['KAROL G'])]
# print (type(df7)) 
# print (df7)