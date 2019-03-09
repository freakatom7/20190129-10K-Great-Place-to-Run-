# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:13:26 2019

@author: freakatom7
"""
# import libraries
# urllib is used to open urls
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from urllib.request import urlopen
from bs4 import BeautifulSoup

#to display the plotted chart between the code 
%matplotlib inline

# specify url containing the datasets
 url = "http://www.hubertiming.com/results/2017GPTR10K"
 
 #get html of the page
 html = urlopen(url)
 
 #to parse raw html text into python objects
 soup = BeautifulSoup(html, 'lxml')
 type(soup)
 
 #Extract webpage title
 title = soup.title
 print(title)
 
 # use find_all() to find useful tags within the webpage
 # a for hyperlinks
 # table for tables
 # tr for table rows 
 # th for table headers
 # td table cells
 
 soup.find_all('a')
 
 # to extract the text without their attributes
 all_links = soup.find_all("a")
 for link in all_links:
     print(link.get("href"))
 
#print out first 10 rows for sanity check
rows = soup.find_all('tr')
print(rows[:10])

# create for loop that iterates through table rows and prints out the cells of the rows
for row in rows:
    row_td = row.find_all('td')
print(row_td)
type(row_td)

# to remove html tags from the tags
# pass the strings into beautifulsoup 
# get_text() to etxract without html tags
str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()
print(cleantext)

# generate an empty list
# extract in between html tags for each row
# append it to the assigned list

import re
list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '', str_cells))
    list_rows.append(clean2)
    
print(clean2)
type(clean2)

# convert the extracted list into dataframe
df = pd.DataFrame(list_rows)
df.head(10)

# the elements in the rows are still in unwanted format
# split 0 column into multiple columns at , position
df1 = df[0].str.split(',', expand=True)
df1.head(10)

# data has unwanted square brackets surrounding each row
# strip method to remove it
df1[0] = df1[0].str.strip('[')
df1.head(10)

# get table headers
col_labels = soup.find_all('th')

all_header = []
col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
all_header.append(cleantext2)
print(all_header)

# convert the list of headers into dataframe
df2 = pd.DataFrame(all_header)
df2.head()

# split 0 column into multiple columns at comma
df3 = df2[0].str.split(',', expand =True)
df3.head() 

# concat df3 and df1
frames = [df3, df1]

df4 = pd.concat(frames)
df4.head(10)

# assign first row to be table header
df5 = df4.rename(columns=df4.iloc[0])
df5.head()

# get overview of the data
df5.info()
df5.shape

# drop all rows with missing values 
df6 = df5.dropna(axis=0, how='any')

# table header is replicated in first row in df5
# drop it using drop function
df7 = df6.drop(df6.index[0])
df7.head()

# repair the header title
df7.rename(columns={'[Place': 'Place'},inplace=True)
df7.rename(columns={' Team]': 'Team'},inplace=True)
df7.head()

# remove closing bracket for cells in Team column
df7['Team'] = df7['Team'].str.strip(']')
df7.head()

# DONE CLEANING DATA! 
# enter analysis part 


