#!/usr/bin/python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.cross_validation import train_test_split

# Load the diabetes dataset
#df = pd.read_csv('data_fei.csv')
#print(df.columns)
f = open("data.txt")
f.readline()  # skip the header
data = np.loadtxt(f)
train, test = train_test_split(data, test_size = 0.1)

train_X = train[:,:-2];
train_Y = train[:,-1];
test_X = test[:,:-2];
test_Y = test[:,-1];

#print test_X

regr = linear_model.LinearRegression()
regr.fit(train_X, train_Y)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((regr.predict(test_X) - test_Y) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(test_X, test_Y))

