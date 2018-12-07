import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython import InteractiveShell


inter = InteractiveShell()
pd.options.display.max_columns = 50

movie = pd.read_csv('data/movie.csv', index_col='movie_title')
c1 = movie['title_year'] >= 2010
c2 = movie['title_year'].isnull()
criteria = c1 | c2
print(movie.mask(criteria).head())

movie_mask = movie.mask(criteria).dropna(how='all')
print(movie_mask.head())

movie_boolean = movie[movie['title_year'] < 2010]
print(movie_boolean.head())
print(movie_mask.equals(movie_boolean))

print(movie_mask.shape == movie_boolean.shape)
print(movie_mask.dtypes == movie_boolean.dtypes)

from pandas.testing import assert_frame_equal
assert_frame_equal(movie_boolean, movie_mask, check_dtype=False)

print(inter.get_ipython().run_line_magic('timeit', "movie.mask(criteria).dropna(how='all')"))
print(inter.get_ipython().run_line_magic('timeit', "movie[movie['title_year'] < 2010]"))
