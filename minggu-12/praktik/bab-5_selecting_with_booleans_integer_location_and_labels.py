import pandas as pd
import numpy as np


pd.options.display.max_columns = 50

movie = pd.read_csv('data/movie.csv', index_col='movie_title')
c1 = movie['content_rating'] == 'G'
c2 = movie['imdb_score'] < 4
criteria = c1 & c2

movie_loc = movie.loc[criteria]
print(movie_loc.head())
print(movie_loc.equals(movie[criteria]))

# movie_iloc = movie.iloc[criteria]
movie_iloc = movie.iloc[criteria.values]
print(movie_iloc.equals(movie_loc))
print(movie.loc[criteria.values])

criteria_col = movie.dtypes == np.int64
print(criteria_col.head())
print(movie.loc[:, criteria_col].head())
print(movie.iloc[:, criteria_col.values].head())

cols = ['content_rating', 'imdb_score', 'title_year', 'gross']
print(movie.loc[criteria, cols].sort_values('imdb_score'))

col_index = [movie.columns.get_loc(col) for col in cols]
print(col_index)
print(movie.iloc[criteria.values, col_index].sort_values('imdb_score'))

a = criteria.values
print(a[:5])
print(len(a), len(criteria))
print(movie.loc[[True, False, True], [True, False, False, True]])
