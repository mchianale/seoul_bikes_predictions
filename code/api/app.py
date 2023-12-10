# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 18:23:17 2023

@author: Matteo
"""

from flask import Flask, request, render_template
import pickle
import os
from lightgbm import LGBMRegressor
from datetime import datetime
import numpy as np
from components.function import *
#Load our model information
model_path = os.path.join(os.getcwd(), 'components', 'LGBMRegressor.sav')
load_model = pickle.load(open(model_path, 'rb'))
results_path = os.path.join(os.getcwd(), 'components', 'results.txt')
metrics = read_metrics_from_file(results_path)
 
MAE = str(round(metrics[0]))


app = Flask("__name__")


q = ""

@app.route("/")
def loadPage():
	return render_template('home.html', query="")

 
@app.route("/", methods=['POST'])
def custom():
    
    inputQueries = []
    
    for i in range(1, 10):
        inputQueries.append(request.form['query' + str(i)])

    data, upDateQueries, holiday_name = getData(inputQueries)
    
    if data:
        prediction = str(round(load_model.predict(data)[0]**2)) + ' ± ' + MAE     
        return render_template('home.html', 
                               output1=prediction,
                               output2=holiday_name,
                               query1=inputQueries[0], 
                               query2=inputQueries[1], 
                               query3=inputQueries[2], 
                               query4=inputQueries[3], 
                               query5=inputQueries[4],
                               query6=inputQueries[5],
                               query7=inputQueries[6],
                               query8=inputQueries[7], 
                               query9=inputQueries[8])
    
    return render_template('home.html',
                            output1='',
                            output2='',
                            query1=upDateQueries[0],
                            query2=upDateQueries[1],
                            query3=upDateQueries[2],
                            query4=upDateQueries[3],
                            query5=upDateQueries[4],
                            query6=upDateQueries[5],
                            query7=upDateQueries[6],
                            query8=upDateQueries[7], 
                            query9=upDateQueries[8]) 
    
      

 
     		 
app.run()