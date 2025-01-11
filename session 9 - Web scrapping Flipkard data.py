# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 10:46:51 2023

@author: jignesh
"""

import bs4
from bs4 import BeautifulSoup as bs
import requests

link='https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29'

page = requests.get(link)

# print (page.content) # HTML content of the page and it’s in string format.

soup = bs(page.content, 'html.parser') #it gives us the visual representation of data
# print(soup.prettify())

name=soup.find('div',class_="_4rR01T")
print(name)

# to get just the name we will use the below code
print (name.text)

#get rating of a product
rating=soup.find('div',class_="_3LWZlK")
# print(rating)
print (rating.text)


# #get other details and specifications of the product
# specification=soup.find('div',class_="fMghEO")
# print (specification.text)

# # If we want to get each specification separately then we will run the below code.
# for each in specification:
#     spec=each.find_all('li',class_='rgWa7D')
#     print(spec[0].text)
#     print(spec[1].text)
#     print(spec[2].text)
#     print(spec[4].text)
#     print(spec[5].text)
#     print(spec[7].text)
    
#get price of the product
price=soup.find('div',class_='_30jeq3 _1_WHN1')
print (price.text)

# Extract all data on the page  
products=[]              #List to store the name of the product
prices=[]                #List to store price of the product
ratings=[]               #List to store rating of the product
apps = []                #List to store supported apps                
os = []                  #List to store operating system
hd = []                  #List to store resolution
sound = []               #List to store sound output

for data in soup.findAll('div',class_='_3pLy-c row'):
        names=data.find('div', attrs={'class':'_4rR01T'})
        price=data.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
        rating=data.find('div', attrs={'class':'_3LWZlK'})
        specification = data.find('div', attrs={'class':'fMghEO'})
        
        for each in specification:
            col=each.find_all('li', attrs={'class':'rgWa7D'})
            app =col[0].text
            os_ = col[1].text
            # hd_ = col[2].text
            # sound_ = col[3].text
        products.append(names.text) # Add product name to list
        prices.append(price.text) # Add price to list
        apps.append(app)# Add supported apps specifications to list
        os.append(os_) # Add operating system specifications to list
        # hd.append(hd_) # Add resolution specifications to list
        # sound.append(sound_) # Add sound specifications to list
        ratings.append(rating.text)   #Add rating specifications to list
# After executing the above code, all the features are extracted and stored in the respective lists.

# #printing the length of list
print(len(products))
print(len(ratings))
print(len(prices))
print(len(apps))
# print(len(sound))
print(len(os))
# print(len(had))

# Storing the data into the structured format in the Data Frame.

import pandas as pd
df=pd.DataFrame({'Product Name':products,'Supported_apps':apps,'OS':os,'Price':prices,'Rating':ratings})
print (df.head(10))
