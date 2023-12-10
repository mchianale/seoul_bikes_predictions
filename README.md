# seoul_bikes_predictions
Machine Learning project using regression model to predict the number of rented bikes per day and per hour.

**Dataset :**
[Link To Dataset](https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand) 
**Initial Dataset :**
- **Date:** year-month-day
- **Rented Bike count:** Count of bikes rented at each hour
- **Hour:** Hour of the day
- **Temperature:** Temperature in Celsius
- **Humidity:** Percentage (%)
- **Windspeed:** Speed in m/s
- **Visibility:** 10m
- **Dew point temperature:** Temperature in Celsius
- **Solar radiation:** MJ/m2
- **Rainfall:** mm
- **Snowfall:** cm
- **Seasons:** Winter, Spring, Summer, Autumn
- **Holiday:** Holiday/No holiday
- **Functional Day:** NoFunc (Non-Functional Hours), Fun (Functional hours)

**Goal :**
In a first part, we trained a regression model to predict Rented Bike Count.
By saving this model, we create a flask api with a form html page, to run the model on inputs features values.
Steps :
- **Cleaning the Data**
- **Normalize the Data**
- **Experimental Training**
- **Hyperparameter's Tuning of LGBMRegressor**
- **Flask API**

## Cleaning & Analisyze the Data,
- **No missing values**
- **Convert Categorical Data by Mapping**

**More about Date feature :**
- We created 3 new columns : **Day**, **Month**, **Day of Week**.
- We don't add Year because the dataset starts in 1/12/2017 and ends the 30/11/2018, so in majority, Year is just represented by 2018.
- After this, we dropped Date.

**Quick view of the distribution of each data :**
![A screenshot of a computer program Description automatically generated](images/distribution.png)
