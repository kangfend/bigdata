import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython import InteractiveShell

inter = InteractiveShell()
inter.get_ipython().run_line_magic('matplotlib', 'inline')
pd.options.display.max_columns = 50

movie = pd.read_csv('data/movie.csv', index_col='movie_title')
fb_likes = movie['actor_1_facebook_likes'].dropna()
print(fb_likes.head())
print(fb_likes.describe(percentiles=[.1, .25, .5, .75, .9]).astype(int))
print(fb_likes.describe(percentiles=[.1,.25,.5,.75,.9]))
print(fb_likes.hist())

criteria_high = fb_likes < 20000
print(criteria_high.mean().round(2))
print(fb_likes.where(criteria_high).head())
print(fb_likes.where(criteria_high, other=20000).head())

criteria_low = fb_likes > 300
fb_likes_cap = fb_likes.where(criteria_high, other=20000).where(criteria_low, 300)
print(fb_likes_cap.head())
print(len(fb_likes), len(fb_likes_cap))
print(fb_likes_cap.hist())

fb_likes_cap2 = fb_likes.clip(lower=300, upper=20000)
print(fb_likes_cap2.equals(fb_likes_cap))
