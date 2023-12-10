# seoul_bikes_predictions
Machine Learning project using regression model to predict the number of rented bikes per day and per hour.

<br>

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
**Steps :**
- **Setting up instructions**
- **Cleaning  & Analyse the Data**
- **Normalize the Data**
- **Experimental Training**
- **Hyperparameter's Tuning of LGBMRegressor**
- **Flask API**

<br>

## Instructions for Setting Up and Running the Flask Web Application

### 1. Download the File
Download the `seoul_bikes_predictions` file in `.zip` format from the shared space on Github.

### 2. Unzip and Place the Folder
Unzip the folder and place it in your desired location on your local machine.

### 3. Launch Python Environment
Launch a Python environment, such as Anaconda. If you are using a specific conda environment, activate it with the command:
*conda enable env_name*

### 4. Navigate to the Project Directory
Open a terminal and navigate to the `seoul_bikes_predictions-main/code/api/` directory using the command:
cd path/to/seoul_bikes_predictions-main/code/api/

### 5. Launch the Flask Web Application
Within the `api` directory, there is an `app.py` file which is used to launch the Flask web application. Execute the application by running the command:
*flask –app app.py execute*

### 6. Access the Application
After executing the command, you will typically see a message like: `* Running on http://127.0.0.1:5000`. Open a web browser and go to `http://127.0.0.1:5000`. The form for the application should be displayed.

<br>

## Cleaning & Analyse the Data,
- **No missing values**
- **Convert Categorical Data by Mapping**

**More about Date feature :**
- We created 3 new columns : **Day**, **Month**, **Day of Week**.
- We don't add Year because the dataset starts in 1/12/2017 and ends the 30/11/2018, so in majority, Year is just represented by 2018.
- After this, we dropped Date.

**Quick view of the distribution of each data :**
![A screenshot of a computer program Description automatically generated](images/distribution.png)
- In a quick view, we can see that few continuous features are not well distributed, especially Snowfall, Rainfall, Visibility and Solar Radiation.
- For categorical data, None Functioning Day are under represented.

**Distribution of Rented Bike Count in depends of Categorical Features :**
![A screenshot of a computer program Description automatically generated](images/cat_distribution.png)
We can see that feature 'Functioning Day' will not be useful because there are 0 counted rented bike when it is not a functioning day.  \\
So, we don't need Functioning Day column, so :
- First, we drop all rows where the day is not a functioning Day.
- After, we drop all the column.

**Correlation :**
![A screenshot of a computer program Description automatically generated](images/corr.png)
We need to drop 'Dew point temperature(°C)' because :
- it is to much correlate with 'Temperature(°C)'
- but 'Temperature(°C)' has a better correlation with 'Rented Bike Count'
Moreover, we added Day of week which have the smaller correlation with Rented Bike Count, but we didn't dropped it, we will see later why.

**Day of Week's Analysis :**
**Frequency of the number of bikes rented depending on the day of the week :**
![A screenshot of a computer program Description automatically generated](images/day_week_distrib.png)

Day of Week seems to not get an impact on Rented Bike Count. Because each day has the same frequency.

Perhaps, if we combine Day of Week with Hour, We can see interesting behaviors in the average number of bikes rented depending on the day of the week and time of day.
![A screenshot of a computer program Description automatically generated](images/day_week_hour.png)
For example, we can see :
- We can see that, for each day, at 18 hour, there are a lot of rented bike. It can be explain by the fact that people go back to work or go out during the weekend .
- At 8 hour, a lot of bikes are rented, except for the weekend. It can be explain by the fact that people go to work at this hour.
- So the Rented Bikes Dataset highlights the behaviors of the inhabitants of seoul
In conclusion, Keeping Day of Week is very interesting, it potentially increases Hour feature importance.

<br>

## Normalize the Data
**Visualization of continuous values :**
![A screenshot of a computer program Description automatically generated](images/continuous_distri.png)
- 'Rented Bike Count' is not normally distributed.
- 'Wind speed (m/s)' is not normally distributed.
- 'Temperature(°C)' doesn't need transformation.
- 'Humidity(%)' doesn't need transformation.
- We can't apply normalization at 'Visibility (10m)', 'Solar Radiation (Mj/m2)', 'Rainfall(mm)' and 'Snowfall (cm)'.
  
**Normalization methods on Rented Bike COunt :**
![A screenshot of a computer program Description automatically generated](images/rented_bike_count.png)
We applied square root on it.

**Normalization methods on Wind Speed :**
![A screenshot of a computer program Description automatically generated](images/wind_speed.png)
We applied square root on it.

<br>

## Sample of Final Dataset
![A screenshot of a computer program Description automatically generated](images/final_df.PNG)

<br>

## Experimental Training
We tried several models on our dataset with different test size :
- models : ** **
- test_sizes : **[0.1, 0.2]**

We conduct experiments with 10% and 20% of our data set aside as the test set. This approach allows us to understand how the model performs under different proportions of training and testing data, providing insights into the model's robustness and generalizability.

We use the following 3 metrics to evaluate the performance of the different regression models :
<br>

### Mean Absolute Error (MAE)
The Mean Absolute Error measures the average of the absolute errors between predictions and actual values. It is simply the average of the absolute difference between each prediction and the real value. The formula for MAE is:

`MAE = 1/n * Σ|y_i - ŷ_i|`

where `y_i` is the actual value and `ŷ_i` is the predicted value. MAE gives an idea of the magnitude of errors in the predictions, ignoring their direction (positive or negative). A lower MAE indicates better model performance.

### Root Mean Squared Error (RMSE)
RMSE is similar to MAE but gives more weight to larger errors as it squares the errors before averaging and then takes the square root of the average to obtain RMSE. The formula for RMSE is:

`RMSE = sqrt(1/n * Σ(y_i - ŷ_i)²)`

RMSE is useful when larger errors are particularly undesirable. A lower RMSE value indicates better model performance.

### R² Score (Coefficient of Determination)
The R² score measures the proportion of the variance in the dependent variable that is predictable from the independent variables in the model. The formula for R² is:

`R² = 1 - (Σ(y_i - ŷ_i)² / Σ(y_i - ȳ)²)`

where `ȳ` is the average of the actual values. The R² score is a measure of how well a model fits the data. A score of 1 indicates a perfect fit, while a score of 0 would mean the model is no better than simply predicting the mean of the dependent variable for all observations.


  
![A screenshot of a computer program Description automatically generated](images/ex.PNG)

<br>


The best model by looking at metrics is LGMBRegressor.

<br>

### LGBMRegressor
**LightGBM (Light Gradient Boosting Machine)** is a gradient boosting framework that uses tree-based learning algorithms. It's designed for distributed and efficient training, particularly on large datasets. LGBMRegressor is used for regression tasks and is known for its high performance and speed.

**First Results Visualization :**

![A screenshot of a computer program Description automatically generated](images/res1.png)
- Our results are good, in majority the error is close to the line y = 0. However, we can see some disparities for few values which are getting big error values.

<br>

## Hyperparameter's Tuning of LGBMRegressor
We runned a grid search for hyperparameters of LGBMRegressor.
**First to gain time complexity, we found a good n_estimator :**
- This parameter defines the number of trees (or base learners) to be built in the ensemble.
- In Gradient Boosting algorithms, such as LightGBM, trees are built sequentially. Each tree corrects the errors made by the previous ones. The final prediction is the sum of the predictions from all trees. Increasing n_estimators in gradient boosting typically improves the model's performance, but it may also increase the risk of overfitting. \\
So more we increase it, more our model is efficient. Perhaps, it will also increase time complexity.
- So, in this part, we will try to chose a good n_estimators between 200 and 6000 based on when the mae, rmse and r2 score don't change a lot when we increase it.

![A screenshot of a computer program Description automatically generated](images/n_estim.png)
We decided to keep n_estimator=3000, because after we don't gain a lot of accuracy.

After, we used grid search and tried to find the optimal model based on rmse score :
**Our optimized Logistic Regression model is:**

{
**- 'colsample_bytree': 0.6,**
**- 'learning_rate': 0.1,**
**- 'max_depth': 12,**
**- 'n_estimators': 3000,**
**- 'num_leaves': 40,**
**- 'subsample': 0.6**
}

**Parameters meanings :**

**- colsample_bytree:** This parameter controls the fraction of features (columns) to be randomly sampled for each tree. A value of 0.6 means that, for each tree, 60% of the features will be used.

**- learning_rate:** Also known as the shrinkage or step size, it determines the impact of each tree on the final prediction. A lower learning rate requires more trees but can result in better generalization. A common starting value is 0.1.

**- max_depth:** This parameter limits the maximum depth of each tree. A value of 12 means that no tree will have a depth greater than 12.
**- n_estimators:** The number of boosting rounds or trees to be built. In this case, 3000 trees will be created in the ensemble.

**- num_leaves:** It controls the maximum number of leaves for each tree. Higher values make the model more complex but can lead to overfitting. A value of 40 means that each tree can have up to 40 leaves.

subsample: It controls the fraction of data points (rows) to be randomly sampled for each tree. A value of 0.6 indicates that 60% of the data will be used for building each tree.

<br>

**Final Results :**

**- MAE = 67.04**
**- RMSE = 125.4**
**- R2 = 96 %**

**Previous score in comparaison :**

**- MAE = 73.6**
**- RMSE = 138.6**
**- R2 = 95%**

