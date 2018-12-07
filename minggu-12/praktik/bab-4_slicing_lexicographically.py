import pandas as pd
import numpy as np


college = pd.read_csv('data/college.csv', index_col='INSTNM')
# print(college.loc['Sp':'Su'])
college = college.sort_index()
print(college.head())

pd.options.display.max_rows = 6
print(college.loc['Sp':'Su'])

college = college.sort_index(ascending=False)
print(college.index.is_monotonic_decreasing)
print(college.loc['E':'B'])
print(college.loc['E':'B'])
