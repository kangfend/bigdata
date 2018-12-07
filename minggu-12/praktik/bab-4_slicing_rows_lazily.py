import pandas as pd
import numpy as np


college = pd.read_csv('data/college.csv', index_col='INSTNM')
city = college['CITY']

print(college[10:20:2])
print(city[10:20:2])
print(college.index[4001])

start = 'Mesa Community College'
stop = 'Spokane Community College'
print(college[start:stop:1500])
print(city[start:stop:1500])
# print(college[:10, ['CITY', 'STABBR']])

first_ten_instnm = college.index[:10]
print(college.loc[first_ten_instnm, ['CITY', 'STABBR']])
