import pandas as pd
import numpy as np


pd.options.display.max_columns = 50

movie = pd.read_csv('data/movie.csv', index_col='movie_title')
print(movie.head())

criteria1 = movie.imdb_score > 8
criteria2 = movie.content_rating == 'PG-13'
criteria3 = (movie.title_year < 2000) | (movie.title_year >= 2010)
print(criteria2.head())

criteria_final = criteria1 & criteria2 & criteria3
print(criteria_final.head())

# movie.title_year < 2000 | movie.title_year > 2009
