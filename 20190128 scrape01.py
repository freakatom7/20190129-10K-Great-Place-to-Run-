# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:26:07 2019

@author: CPDS 6
"""
# download the webpage 
import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page
# check the download status
page.status_code

# import beautifulsoup library
from bs4 import BeautifulSoup

#create a class for beautifulsoup
soup = BeautifulSoup(page.content, 'html.parser')

# print out html content of the page using prettify function of beautifulsoup
print(soup.prettify())


