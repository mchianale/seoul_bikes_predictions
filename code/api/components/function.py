# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 19:54:08 2023

@author: Matteo
"""
from datetime import datetime
import json
import requests
import pandas as pd
import numpy as np

#Data 
days_of_week = {
    'Monday' : 0,
    'Tuesday' : 1,
    'Wednesday' : 2,
    'Thursday' : 3,
    'Friday' : 4,
    'Saturday' : 5,
    'Sunday' : 6
}

seasons = {'Winter' : 0,
           'Spring' : 1,
           'Summer' : 2,
           'Autumn' : 3}

def get_day_and_month_season(date_string):
    # Convert the date string to a datetime object
    date_object = datetime.strptime(date_string, '%Y-%m-%d') #'%d/%m/%Y')
 
    # Extract day and month
    day = date_object.day
    month = date_object.month
    print(day, month)
    #extract day of week
    day_of_week = days_of_week[date_object.strftime("%A")]
    # Determine the season based on the month
    season = seasons[get_season(month)]
    
    return int(day), day_of_week, int(month), int(season)

def get_season(month):
    if 3 <= month <= 5:
        return 'Spring'
    elif 6 <= month <= 8:
        return 'Summer'
    elif 9 <= month <= 11:
        return 'Autumn'
    else:
        return 'Winter'
    

def isHoliday(date_string):
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    year_string = str(date_object.year)
    date_object =  date_object.strftime('%Y-%m-%d')
 
    url = 'https://date.nager.at/api/v3/PublicHolidays/' + year_string + '/KR'
    response = requests.get(url)
    response_data = json.loads(response.content)
    
    public_holidays = [public_holiday['date'] for public_holiday in response_data]
    
    for i, public_holiday in enumerate(public_holidays):
        if public_holiday == date_object:
            return response_data[i]['name'], 1
        
    return 'False', 0
    
def getHour(hour_string):
    hour_string = hour_string.split(':')[0]
    if hour_string[0] == '0':
        return hour_string[0]
    else:
        return hour_string
    
    
def getData(inputQueries):
    valid = True
    try:
        date_string = inputQueries[0]
        day, day_of_week, month, season = get_day_and_month_season(date_string)
        try:
            holiday_name, holiday = isHoliday(date_string)   
             
        except:
            holiday = 0
            holiday_name = 'False'
      
    except:
        inputQueries[0] = 'error'
        valid = False
    try:
        hour = int(getHour(inputQueries[1]))
    except:
        inputQueries[1] = 'error'
        valid = False
        
    try:
        temperature = float(inputQueries[2])
    except:
        inputQueries[2] = 'error'
        valid = False
    
    try:
        humidity = float(inputQueries[3])
    except:
        inputQueries[3] = 'error'
        valid = False
 
    
    try:
        wind_speed = np.sqrt(float(inputQueries[4]))
    except:
        inputQueries[4] = 'error'
        valid = False
    
    try:
        visibility = float(inputQueries[5])
    except:
        inputQueries[5] = 'error'
        valid = False
        
 
    try:
        solar_radiation = float(inputQueries[6])
    except:
        inputQueries[6] = 'error'
        valid = False
        
    try:
        rainfall = float(inputQueries[7])
    except:
        inputQueries[7] = 'error'
        valid = False
        
    try:
        snowfall = float(inputQueries[8])
    except:
        inputQueries[8] = 'error'
        valid = False
        
    if valid:
        data = [[hour, temperature, humidity, 
                wind_speed, visibility, solar_radiation,
                rainfall, snowfall, season, holiday, day_of_week, day, month]]
        
        return data, inputQueries, holiday_name
    
    return None,inputQueries, None



def read_metrics_from_file(path):
   metrics = []
   f = open(path, 'r') 
   lines =f.readlines()
   for line in lines:
       metrics.append(float(line.strip()))
   
   return metrics

 
