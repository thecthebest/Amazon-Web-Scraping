# Libraries

#library for making http requests
import requests
# library for parsing html files
from bs4 import BeautifulSoup
# library for working with csv files
import csv
# library for working with datetime
import datetime as dt

# url of the website
URL = 'https://www.amazon.co.uk/Levis-Classic-Twill-Baseball-Black/dp/B00FOI1JJ4/ref=sr_1_7?crid=1T3KFV41JZN4T&keywords=cap&qid=1655196251&sprefix=cap%2Caps%2C64&sr=8-7'
# request header used by user agent that sends request on behalf of the client
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
# sending the request
response = requests.get(URL, headers=headers)
# parsing the html page
soup1 = BeautifulSoup(response.content, "html.parser")
# making the response more readable
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
# extracting title and price information
title = soup2.find(id='productTitle').get_text().strip()
# target a specific html element with id and then select a child element 'span'
price = soup2.find(id='corePrice_feature_div').select('span')[1].get_text().strip()[1:]
# Date
date = dt.date.today()

# Creating list
header = ['Title', 'Price', 'Date']
data = [title, price, date]

# create a csv file
with open('AmzWebScraperDataSet.csv', 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
