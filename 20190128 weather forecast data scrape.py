# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 11:14:19 2019

@author: CPDS 6
"""
#download the webpage 
import requests
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
page

#check download status
page.status_code 

# import beautifulsoup library
from bs4 import BeautifulSoup
 #create the class to parse the page
soup = BeautifulSoup(page.content, 'html.parser')

#find the div with seven-day-forecast and assign to seven_day
seven_day = soup.find(id="seven-day-forecast")

# find each individual forecast inside seven_day
forecast_items = seven_day.find_all(class_="tombstone-container")

#forecast for tonight
tonight = forecast_items[0]

print(tonight.prettify())

# inside the forecast itme "tonight", there are 4 elements we can extract
# said items are period-name, title, short-desc, temp temp-low 
# extract period-name, short-desc, temp
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

print(period)
print(short_desc)
print(temp)


#extract title from img (the main image)
img = tonight.find("img")
desc = img['title']

# now extract everything at once
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods

print(desc)

# can apply the same method to the other elements
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

print(short_descs)
print(temps)
print(descs)

#combine extracted data into pandas dataframe 
# import pandas 
import pandas as pd
weather = pd.DataFrame({
        "period": periods, 
        "short_desc": short_descs, 
        "temp": temps, 
        "desc":descs
    })

#sample analysis on dataframe
#pull out numeric temperature values 
temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
temp_nums

#find mean of all highs and lows 
weather["temp_num"].mean()

#select rows that happen at night 
is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
is_night

weather[is_night]

