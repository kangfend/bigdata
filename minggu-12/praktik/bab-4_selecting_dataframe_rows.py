import pandas as pd
import numpy as np


college = pd.read_csv('data/college.csv', index_col='INSTNM')
print(college.head())

pd.options.display.max_rows = 6
print(college.iloc[60])
print(college.loc['University of Alaska Anchorage'])
print(college.iloc[[60, 99, 3]])

labels = ['University of Alaska Anchorage',
          'International Academy of Hair Design',
          'University of Alabama in Huntsville']
print(college.loc[labels])
print(college.iloc[99:102])

start = 'International Academy of Hair Design'
stop = 'Mesa Community College'
print(college.loc[start:stop])
print(college.iloc[[60, 99, 3]].index.tolist())
