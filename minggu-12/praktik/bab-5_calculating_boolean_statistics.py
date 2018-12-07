import pandas as pd
import numpy as np


pd.options.display.max_columns = 50

movie = pd.read_csv('data/movie.csv', index_col='movie_title')
print(movie.head())

movie_2_hours = movie['duration'] > 120
print(movie_2_hours.head(10))
print(movie_2_hours.sum())
print(movie_2_hours.mean())
print(movie_2_hours.describe())
print(movie['duration'].dropna().gt(120).mean())
print(movie_2_hours.value_counts(normalize=True))

actors = movie[['actor_1_facebook_likes', 'actor_2_facebook_likes']].dropna()
print((actors['actor_1_facebook_likes'] > actors['actor_2_facebook_likes']).mean())
