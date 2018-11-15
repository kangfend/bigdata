
# Chapter 1: Pandas Foundations

## Daftar Topik
* [Memahami anatomi DataFrame](#Memahami-anatomi-DataFrame)
* [Mengakses Komponen DataFrame](#Mengakses-Komponen-DataFrame)
* [Memahami Tipe Data](#Memahami-Tipe-Data)
* [Memilih satu kolom dari data sebagai Series](#Memilih-satu-kolom-dari-data-sebagai-Series)
* [Memanggil Method Series](#Memanggil-Method-Series)
* [Bekerja dengan Operator pada Series](#Bekerja-dengan-Operator-pada-Series)
* [Chaining Series methods together](#Chaining-Series-methods-together)
* [Membuat Indeks lebih bermakna :D](#MembuatIndeks-lebih-bermakna-:D)
* [Mengubah Nama Baris dan Kolom](#Mengubah-Nama-Baris-dan-Kolom)
* [Membuat dan Menghapus Kolom](#Membuat-dan-Menghapus-Kolom)


```python
import pandas as pd
import numpy as np
```

# Memahami anatomi DataFrame


```python
pd.set_option('max_columns', 8, 'max_rows', 10)
```


```python
movie = pd.read_csv('data/movie.csv')
movie.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>director_name</th>
      <th>num_critic_for_reviews</th>
      <th>duration</th>
      <th>...</th>
      <th>actor_2_facebook_likes</th>
      <th>imdb_score</th>
      <th>aspect_ratio</th>
      <th>movie_facebook_likes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Color</td>
      <td>James Cameron</td>
      <td>723.0</td>
      <td>178.0</td>
      <td>...</td>
      <td>936.0</td>
      <td>7.9</td>
      <td>1.78</td>
      <td>33000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Color</td>
      <td>Gore Verbinski</td>
      <td>302.0</td>
      <td>169.0</td>
      <td>...</td>
      <td>5000.0</td>
      <td>7.1</td>
      <td>2.35</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Color</td>
      <td>Sam Mendes</td>
      <td>602.0</td>
      <td>148.0</td>
      <td>...</td>
      <td>393.0</td>
      <td>6.8</td>
      <td>2.35</td>
      <td>85000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Color</td>
      <td>Christopher Nolan</td>
      <td>813.0</td>
      <td>164.0</td>
      <td>...</td>
      <td>23000.0</td>
      <td>8.5</td>
      <td>2.35</td>
      <td>164000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>Doug Walker</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>12.0</td>
      <td>7.1</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 28 columns</p>
</div>



# Mengakses Komponen DataFrame


```python
columns = movie.columns
index = movie.index
data = movie.values
```


```python
columns
```




    Index(['color', 'director_name', 'num_critic_for_reviews', 'duration',
           'director_facebook_likes', 'actor_3_facebook_likes', 'actor_2_name',
           'actor_1_facebook_likes', 'gross', 'genres', 'actor_1_name',
           'movie_title', 'num_voted_users', 'cast_total_facebook_likes',
           'actor_3_name', 'facenumber_in_poster', 'plot_keywords',
           'movie_imdb_link', 'num_user_for_reviews', 'language', 'country',
           'content_rating', 'budget', 'title_year', 'actor_2_facebook_likes',
           'imdb_score', 'aspect_ratio', 'movie_facebook_likes'],
          dtype='object')




```python
index
```




    RangeIndex(start=0, stop=4916, step=1)




```python
data
```




    array([['Color', 'James Cameron', 723.0, ..., 7.9, 1.78, 33000],
           ['Color', 'Gore Verbinski', 302.0, ..., 7.1, 2.35, 0],
           ['Color', 'Sam Mendes', 602.0, ..., 6.8, 2.35, 85000],
           ...,
           ['Color', 'Benjamin Roberds', 13.0, ..., 6.3, nan, 16],
           ['Color', 'Daniel Hsia', 14.0, ..., 6.3, 2.35, 660],
           ['Color', 'Jon Gunn', 43.0, ..., 6.6, 1.85, 456]], dtype=object)




```python
type(index)
```




    pandas.core.indexes.range.RangeIndex




```python
type(columns)
```




    pandas.core.indexes.base.Index




```python
type(data)
```




    numpy.ndarray




```python
issubclass(pd.RangeIndex, pd.Index)
```




    True




```python
index.values
```




    array([   0,    1,    2, ..., 4913, 4914, 4915])




```python
columns.values
```




    array(['color', 'director_name', 'num_critic_for_reviews', 'duration',
           'director_facebook_likes', 'actor_3_facebook_likes',
           'actor_2_name', 'actor_1_facebook_likes', 'gross', 'genres',
           'actor_1_name', 'movie_title', 'num_voted_users',
           'cast_total_facebook_likes', 'actor_3_name',
           'facenumber_in_poster', 'plot_keywords', 'movie_imdb_link',
           'num_user_for_reviews', 'language', 'country', 'content_rating',
           'budget', 'title_year', 'actor_2_facebook_likes', 'imdb_score',
           'aspect_ratio', 'movie_facebook_likes'], dtype=object)



# Memahami Tipe Data


```python
movie = pd.read_csv('data/movie.csv')
```


```python
movie.dtypes
```




    color                       object
    director_name               object
    num_critic_for_reviews     float64
    duration                   float64
    director_facebook_likes    float64
                                ...   
    title_year                 float64
    actor_2_facebook_likes     float64
    imdb_score                 float64
    aspect_ratio               float64
    movie_facebook_likes         int64
    Length: 28, dtype: object




```python
movie.get_dtype_counts()
```




    float64    13
    int64       3
    object     12
    dtype: int64



# Memilih satu kolom dari data sebagai Series


```python
movie = pd.read_csv('data/movie.csv')
```


```python
movie['director_name']
```




    0           James Cameron
    1          Gore Verbinski
    2              Sam Mendes
    3       Christopher Nolan
    4             Doug Walker
                  ...        
    4911          Scott Smith
    4912                  NaN
    4913     Benjamin Roberds
    4914          Daniel Hsia
    4915             Jon Gunn
    Name: director_name, Length: 4916, dtype: object




```python
movie.director_name
```




    0           James Cameron
    1          Gore Verbinski
    2              Sam Mendes
    3       Christopher Nolan
    4             Doug Walker
                  ...        
    4911          Scott Smith
    4912                  NaN
    4913     Benjamin Roberds
    4914          Daniel Hsia
    4915             Jon Gunn
    Name: director_name, Length: 4916, dtype: object




```python
type(movie['director_name'])
```




    pandas.core.series.Series




```python
director = movie['director_name'] # simpan sarive ke variabel
director.name
```




    'director_name'




```python
director.to_frame().head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>director_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>James Cameron</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Gore Verbinski</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Sam Mendes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Christopher Nolan</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Doug Walker</td>
    </tr>
  </tbody>
</table>
</div>



# Memanggil Method Series


```python
s_attr_methods = set(dir(pd.Series))
len(s_attr_methods)
```




    464




```python
df_attr_methods = set(dir(pd.DataFrame))
len(df_attr_methods)
```




    460




```python
len(s_attr_methods & df_attr_methods)
```




    399




```python
movie = pd.read_csv('data/movie.csv')
director = movie['director_name']
actor_1_fb_likes = movie['actor_1_facebook_likes']
```


```python
director.head()
```




    0        James Cameron
    1       Gore Verbinski
    2           Sam Mendes
    3    Christopher Nolan
    4          Doug Walker
    Name: director_name, dtype: object




```python
actor_1_fb_likes.head()
```




    0     1000.0
    1    40000.0
    2    11000.0
    3    27000.0
    4      131.0
    Name: actor_1_facebook_likes, dtype: float64




```python
pd.set_option('max_rows', 8)
director.value_counts()
```




    Steven Spielberg      26
    Woody Allen           22
    Clint Eastwood        20
    Martin Scorsese       20
                          ..
    Enrique Begne          1
    Álex de la Iglesia     1
    Adrienne Shelly        1
    Russ Meyer             1
    Name: director_name, Length: 2397, dtype: int64




```python
actor_1_fb_likes.value_counts()
```




    1000.0     436
    11000.0    206
    2000.0     189
    3000.0     150
              ... 
    216.0        1
    859.0        1
    225.0        1
    334.0        1
    Name: actor_1_facebook_likes, Length: 877, dtype: int64




```python
director.size
```




    4916




```python
director.shape
```




    (4916,)




```python
len(director)
```




    4916




```python
director.count()
```




    4814




```python
actor_1_fb_likes.count()
```




    4909




```python
actor_1_fb_likes.quantile()
```




    982.0




```python
actor_1_fb_likes.min(), actor_1_fb_likes.max(), \
actor_1_fb_likes.mean(), actor_1_fb_likes.median(), \
actor_1_fb_likes.std(), actor_1_fb_likes.sum()
```




    (0.0, 640000.0, 6494.488490527602, 982.0, 15106.986883848185, 31881444.0)




```python
actor_1_fb_likes.describe()
```




    count      4909.000000
    mean       6494.488491
    std       15106.986884
    min           0.000000
    25%         607.000000
    50%         982.000000
    75%       11000.000000
    max      640000.000000
    Name: actor_1_facebook_likes, dtype: float64




```python
director.describe()
```




    count                 4814
    unique                2397
    top       Steven Spielberg
    freq                    26
    Name: director_name, dtype: object




```python
actor_1_fb_likes.quantile(.2)
```




    510.0




```python
actor_1_fb_likes.quantile([.1, .2, .3, .4, .5, .6, .7, .8, .9])
```




    0.1      240.0
    0.2      510.0
    0.3      694.0
    0.4      854.0
            ...   
    0.6     1000.0
    0.7     8000.0
    0.8    13000.0
    0.9    18000.0
    Name: actor_1_facebook_likes, Length: 9, dtype: float64




```python
director.isnull()
```




    0       False
    1       False
    2       False
    3       False
            ...  
    4912     True
    4913    False
    4914    False
    4915    False
    Name: director_name, Length: 4916, dtype: bool




```python
actor_1_fb_likes_filled = actor_1_fb_likes.fillna(0)
actor_1_fb_likes_filled.count()
```




    4916




```python
actor_1_fb_likes_dropped = actor_1_fb_likes.dropna()
actor_1_fb_likes_dropped.size
```




    4909



## Masih ada lagi


```python
director.value_counts(normalize=True)
```




    Steven Spielberg      0.005401
    Woody Allen           0.004570
    Clint Eastwood        0.004155
    Martin Scorsese       0.004155
                            ...   
    Enrique Begne         0.000208
    Álex de la Iglesia    0.000208
    Adrienne Shelly       0.000208
    Russ Meyer            0.000208
    Name: director_name, Length: 2397, dtype: float64




```python
director.hasnans
```




    True




```python
director.notnull()
```




    0        True
    1        True
    2        True
    3        True
            ...  
    4912    False
    4913     True
    4914     True
    4915     True
    Name: director_name, Length: 4916, dtype: bool



# Bekerja dengan Operator pada Series


```python
pd.options.display.max_rows = 6
```


```python
5 + 9
```




    14




```python
4 ** 2
```




    16




```python
a = 10
```


```python
5 <= 9
```




    True




```python
'abcde' + 'fg'
```




    'abcdefg'




```python
not (5 <= 9)
```




    False




```python
7 in [1, 2, 6]
```




    False




```python
set([1,2,3]) & set([2,3,4])
```




    {2, 3}




```python
[1, 2, 3] - 3
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-58-a6218e425718> in <module>()
    ----> 1 [1, 2, 3] - 3
    

    TypeError: unsupported operand type(s) for -: 'list' and 'int'



```python
a = set([1,2,3])     
a[0]
```

## Bersiap untuk memulai


```python
movie = pd.read_csv('data/movie.csv')
imdb_score = movie['imdb_score']
imdb_score
```


```python
imdb_score + 1
```


```python
imdb_score * 2.5
```


```python
imdb_score // 7
```


```python
imdb_score > 7
```


```python
director = movie['director_name']
```


```python
director == 'James Cameron'
```

## Masih ada lagi!


```python
imdb_score.add(1)              # imdb_score + 1
```


```python
imdb_score.mul(2.5)            # imdb_score * 2.5
```


```python
imdb_score.floordiv(7)         # imdb_score // 7
```


```python
imdb_score.gt(7)               # imdb_score > 7
```


```python
director.eq('James Cameron')   # director == 'James Cameron'
```


```python
imdb_score.astype(int).mod(5)
```


```python
a = type(1)
```


```python
type(a)
```


```python
a = type(imdb_score)
```


```python
a([1,2,3])
```

# Chaining Series methods together


```python
movie = pd.read_csv('data/movie.csv')
actor_1_fb_likes = movie['actor_1_facebook_likes']
director = movie['director_name']
```


```python
director.value_counts().head(3)
```


```python
actor_1_fb_likes.isnull().sum()
```


```python
actor_1_fb_likes.dtype
```


```python
actor_1_fb_likes.fillna(0)\
                .astype(int)\
                .head()
```

## Masih ada lagi!


```python
actor_1_fb_likes.isnull().mean()
```


```python
(actor_1_fb_likes.fillna(0)
                 .astype(int)
                 .head())
```

# Membuat Indeks lebih bermakna :D


```python
movie = pd.read_csv('data/movie.csv')
```


```python
movie.shape
```


```python
movie2 = movie.set_index('movie_title')
movie2
```


```python
pd.read_csv('data/movie.csv', index_col='movie_title')
```

# Masih ada lagi!


```python
movie2.reset_index()
```

# Mengubah Nama Baris dan Kolom


```python
movie = pd.read_csv('data/movie.csv', index_col='movie_title')
```


```python
idx_rename = {'Avatar':'Ratava', 'Spectre': 'Ertceps'} 
col_rename = {'director_name':'Director Name', 
              'num_critic_for_reviews': 'Critical Reviews'} 
```


```python
movie.rename(index=idx_rename, 
             columns=col_rename).head()
```

## Masih ada lagi!


```python
movie = pd.read_csv('data/movie.csv', index_col='movie_title')
index = movie.index
columns = movie.columns

index_list = index.tolist()
column_list = columns.tolist()

index_list[0] = 'Ratava'
index_list[2] = 'Ertceps'
column_list[1] = 'Director Name'
column_list[2] = 'Critical Reviews'
```


```python
print(index_list[:5])
```


```python
print(column_list)
```


```python
movie.index = index_list
movie.columns = column_list
```


```python
movie.head()
```

# Membuat dan Menghapus Kolom


```python
movie = pd.read_csv('data/movie.csv')
```


```python
movie['has_seen'] = 0
```


```python
movie.columns
```


```python
movie['actor_director_facebook_likes'] = (movie['actor_1_facebook_likes'] + 
                                              movie['actor_2_facebook_likes'] + 
                                              movie['actor_3_facebook_likes'] + 
                                              movie['director_facebook_likes'])
```


```python
movie['actor_director_facebook_likes'].isnull().sum()
```


```python
movie['actor_director_facebook_likes'] = movie['actor_director_facebook_likes'].fillna(0)
```


```python
movie['is_cast_likes_more'] = (movie['cast_total_facebook_likes'] >= 
                                  movie['actor_director_facebook_likes'])
```


```python
movie['is_cast_likes_more'].all()
```


```python
movie = movie.drop('actor_director_facebook_likes', axis='columns')
```


```python
movie['actor_total_facebook_likes'] = (movie['actor_1_facebook_likes'] + 
                                       movie['actor_2_facebook_likes'] + 
                                       movie['actor_3_facebook_likes'])

movie['actor_total_facebook_likes'] = movie['actor_total_facebook_likes'].fillna(0)
```


```python
movie['is_cast_likes_more'] = movie['cast_total_facebook_likes'] >= \
                                  movie['actor_total_facebook_likes']
    
movie['is_cast_likes_more'].all()
```


```python
movie['pct_actor_cast_like'] = (movie['actor_total_facebook_likes'] / 
                                movie['cast_total_facebook_likes'])
```


```python
movie['pct_actor_cast_like'].min(), movie['pct_actor_cast_like'].max() 
```


```python
movie.set_index('movie_title')['pct_actor_cast_like'].head()
```

## Masih ada lagi!


```python
profit_index = movie.columns.get_loc('gross') + 1
profit_index
```


```python
movie.insert(loc=profit_index,
                 column='profit',
                 value=movie['gross'] - movie['budget'])
```


```python
movie.head()
```
