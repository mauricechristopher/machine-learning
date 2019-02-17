# Imagine you’re looking for a job as a software engineer. And you spotted a company that you want to work for. 
# You already have 4 years of experience working as a developer, and you want to see how much you can make working
#  in this company based on the number of years of experience you have. 	

# Well, the good news is you have a dataset of the salary of all the employees in the company and their number 
# of years of experience respectively. This is the perfect opportunity to apply linear regression to predict your salary! 

# You must be able to visualize the result with a scatter plot by using Matplotlib library. 
# The image below is the end result of the test set that is expected to be displayed.

import numpy
import matplotlib.pyplot as plot
import pandas
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pandas.read_csv('data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 1/3, random_state = 0)

regressor = LinearRegression()

regressor.fit(xTrain, yTrain)

yPrediction = regressor.predict(xTest)

plot.scatter(xTrain, yTrain, color = 'red')
plot.plot(xTrain, regressor.predict(xTrain), color = 'blue')
plot.title('Salary vs Experience (Training set)')
plot.xlabel('Years of Experience')
plot.ylabel('Salary')
plot.show()