import pandas as pd
import numpy as np
from IPython import InteractiveShell

inter = InteractiveShell()

college = pd.read_csv('data/college.csv', index_col='INSTNM')
cn = 'Texas A & M University-College Station'
print(college.loc[cn, 'UGDS_WHITE'])
print(college.at[cn, 'UGDS_WHITE'])
print(inter.get_ipython().run_line_magic('timeit', "college.loc[cn, 'UGDS_WHITE']"))
print(inter.get_ipython().run_line_magic('timeit', "college.at[cn, 'UGDS_WHITE']"))

row_num = college.index.get_loc(cn)
col_num = college.columns.get_loc('UGDS_WHITE')
print(row_num, col_num)

print(inter.get_ipython().run_line_magic('timeit', 'college.iloc[row_num, col_num]'))
print(inter.get_ipython().run_line_magic('timeit', 'college.iat[row_num, col_num]'))
print(inter.get_ipython().run_line_magic('timeit', 'college.iloc[5, col_num]'))
print(inter.get_ipython().run_line_magic('timeit', 'college.iat[5, col_num]'))

state = college['STABBR']
print(state.iat[1000])
print(state.at['Stanford University'])