import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython import InteractiveShell


inter = InteractiveShell()
inter.get_ipython().run_line_magic('matplotlib', 'inline')
pd.options.display.max_columns = 50

slb = pd.read_csv('data/slb_stock.csv', index_col='Date', parse_dates=['Date'])
print(slb.head())

slb_close = slb['Close']
slb_summary = slb_close.describe(percentiles=[.1, .9])
print(slb_summary)

upper_10 = slb_summary.loc['90%']
lower_10 = slb_summary.loc['10%']
criteria = (slb_close < lower_10) | (slb_close > upper_10)
slb_top_bottom_10 = slb_close[criteria]

slb_close.plot(color='black', figsize=(12,6))
slb_top_bottom_10.plot(marker='o', style=' ', ms=4, color='lightgray')

xmin = criteria.index[0]
xmax = criteria.index[-1]
print(plt.hlines(y=[lower_10, upper_10], xmin=xmin, xmax=xmax,color='black'))

slb_close.plot(color='black', figsize=(12,6))
plt.hlines(y=[lower_10, upper_10], 
           xmin=xmin, xmax=xmax,color='lightgray')
plt.fill_between(x=criteria.index, y1=lower_10,
                 y2=slb_close.values, color='black')
plt.fill_between(x=criteria.index,y1=lower_10,
                 y2=slb_close.values, where=slb_close < lower_10,
                 color='lightgray')
plt.fill_between(x=criteria.index, y1=upper_10, 
                 y2=slb_close.values, where=slb_close > upper_10,
                 color='lightgray')
