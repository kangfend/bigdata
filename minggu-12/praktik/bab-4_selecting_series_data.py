import pandas as pd
import numpy as np


college = pd.read_csv('data/college.csv', index_col='INSTNM')
city = college['CITY']
print(city.head())
print(city.iloc[3])
print(city.iloc[[10,20,30]])
print(city.iloc[4:50:10])
print(city.loc['Heritage Christian University'])

np.random.seed(1)
labels = list(np.random.choice(city.index, 4))
print(labels)
print(city.loc[labels])
print(city.loc['Alabama State University':'Reid State Technical College':10])
print(city['Alabama State University':'Reid State Technical College':10])
print(city.iloc[[3]])
print(city.loc['Reid State Technical College':'Alabama State University':10])
print(city.loc['Reid State Technical College':'Alabama State University':-10])