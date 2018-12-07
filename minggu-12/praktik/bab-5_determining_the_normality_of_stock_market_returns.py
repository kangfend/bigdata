import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython import InteractiveShell


inter = InteractiveShell()
inter.get_ipython().run_line_magic('matplotlib', 'inline')
pd.options.display.max_columns = 50

amzn = pd.read_csv('data/amzn_stock.csv', index_col='Date', parse_dates=['Date'])
print(amzn.head())

amzn_daily_return = amzn.Close.pct_change()
print(amzn_daily_return.head())

amzn_daily_return = amzn_daily_return.dropna()
print(amzn_daily_return.hist(bins=20))

mean = amzn_daily_return.mean()  
std = amzn_daily_return.std()
abs_z_score = amzn_daily_return.sub(mean).abs().div(std)
pcts = [abs_z_score.lt(i).mean() for i in range(1,4)]
print('{:.3f} fall within 1 standard deviation. '
      '{:.3f} within 2 and {:.3f} within 3'.format(*pcts))

def test_return_normality(stock_data):
    close = stock_data['Close']
    daily_return = close.pct_change().dropna()
    daily_return.hist(bins=20)
    mean = daily_return.mean() 
    std = daily_return.std()
    
    abs_z_score = abs(daily_return - mean) / std
    pcts = [abs_z_score.lt(i).mean() for i in range(1,4)]

    print('{:.3f} fall within 1 standard deviation. '
          '{:.3f} within 2 and {:.3f} within 3'.format(*pcts))

slb = pd.read_csv('data/slb_stock.csv', index_col='Date', parse_dates=['Date'])
print(test_return_normality(slb))
