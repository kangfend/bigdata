import pandas as pd
import numpy as np
from IPython import InteractiveShell


inter = InteractiveShell()
pd.options.display.max_columns = 50


college = pd.read_csv('data/college.csv')
print(college[college['STABBR'] == 'TX'].head())

college2 = college.set_index('STABBR')
print(college2.loc['TX'].head())

print(inter.get_ipython().run_line_magic('timeit', "college[college['STABBR'] == 'TX']"))
print(inter.get_ipython().run_line_magic('timeit', "college2.loc['TX']"))
print(inter.get_ipython().run_line_magic('timeit', "college2 = college.set_index('STABBR')"))

states =['TX', 'CA', 'NY']
print(college[college['STABBR'].isin(states)])
print(college2.loc[states].head())
