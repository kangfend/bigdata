import pandas as pd
import numpy as np
from IPython import InteractiveShell

inter = InteractiveShell()
pd.options.display.max_columns = 50

college = pd.read_csv('data/college.csv')
college2 = college.set_index('STABBR')
print(college2.index.is_monotonic)

college3 = college2.sort_index()
print(college3.index.is_monotonic)
print(inter.get_ipython().run_line_magic('timeit', "college[college['STABBR'] == 'TX']"))
print(inter.get_ipython().run_line_magic('timeit', "college2.loc['TX']"))
print(inter.get_ipython().run_line_magic('timeit', "college3.loc['TX']"))

college_unique = college.set_index('INSTNM')
print(college_unique.index.is_unique)

college[college['INSTNM'] == 'Stanford University']
print(college_unique.loc['Stanford University'])
print(inter.get_ipython().run_line_magic('timeit', "college[college['INSTNM'] == 'Stanford University']"))
print(inter.get_ipython().run_line_magic('timeit', "college_unique.loc['Stanford University']"))

college.index = college['CITY'] + ', ' + college['STABBR']
college = college.sort_index()
print(college.head())
print(college.loc['Miami, FL'].head())
print(inter.get_ipython().run_cell_magic('timeit', '', "crit1 = college['CITY'] == 'Miami' \ncrit2 = college['STABBR'] == 'FL'\ncollege[crit1 & crit2]"))
print(inter.get_ipython().run_line_magic('timeit', "college.loc['Miami, FL']"))
print(college[(college['CITY'] == 'Miami') & (college['STABBR'] == 'FL')].equals(college.loc['Miami, FL']))
