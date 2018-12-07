import pandas as pd
import numpy as np


college = pd.read_csv('data/college.csv', index_col='INSTNM')
col_start = college.columns.get_loc('UGDS_WHITE')
col_end = college.columns.get_loc('UGDS_UNKN') + 1
print(col_start, col_end)
print(college.iloc[:5, col_start:col_end])

row_start = college.index[10]
row_end = college.index[15]
print(college.loc[row_start:row_end, 'UGDS_WHITE':'UGDS_UNKN'])
