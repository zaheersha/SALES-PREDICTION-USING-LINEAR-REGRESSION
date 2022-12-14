# -*- coding: utf-8 -*-
"""sale_preadiction.ipynb

Automatically generated by Colaboratory.

Original file is located at
"""

#important libaries to import-
import pandas as pd  #pandas [useful for loading the dataset]-numpy[to perform array]
import numpy as np

from google.colab import files        #uploading data into online notebook
uploaded = files.upload()

#to load the data
dataset = pd.read_csv('sales_prediction.csv')       
print(dataset)

#summarize dataset  
print(dataset.shape)           #no. of rows and columns
print(dataset.head(5))      #head(5)-top 5 values & tail(5)-bottom 5 values

#segregate dataset into x and y - inputs/outputs-independent/dependent variables
x = dataset.iloc[:, :-1].values
x

#segregate dataset into x and y - inputs/outputs-independent/dependent variables
y = dataset.iloc[:, -1].values
y

#spiliting the dataset into train and test-x_train&y_train is for train purpose where x_test&y_test is for test purpose.
from sklearn.model_selection  import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.25, random_state = 0)

#feacture scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
print(x_train)

#training 
from sklearn.linear_model import LogisticRegression
model = LogisticRegression() #loading the alg
model.fit(x_train,y_train)      #train

#prediction for all the test data 
y_pred = model.predict(x_test)

#to get the accuracy of the model
from sklearn.metrics import accuracy_score
print("accuracy of the model:{0}%".format(accuracy_score(y_test,y_pred)*100))

#deploying on teh project
#predicting , weather new customer with age and salary will buy or not

age = int(input("enter customer age : "))
salary = int(input("enter customer salary : "))
newCust = [[age,salary]]
result = model.predict(sc.transform(newCust))
print(result)
if result == 1:
  print("customer will buy ")
else:
  print("customer won't buy")