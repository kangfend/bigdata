#!/usr/bin/env python
# coding: utf-8

# # Chapter 1: Pandas Foundations
# 
# ## Daftar Topik
# * [Memahami anatomi DataFrame](#Memahami-anatomi-DataFrame)
# * [Mengakses Komponen DataFrame](#Mengakses-Komponen-DataFrame)
# * [Memahami Tipe Data](#Memahami-Tipe-Data)
# * [Memilih satu kolom dari data sebagai Series](#Memilih-satu-kolom-dari-data-sebagai-Series)
# * [Memanggil Method Series](#Memanggil-Method-Series)
# * [Bekerja dengan Operator pada Series](#Bekerja-dengan-Operator-pada-Series)
# * [Chaining Series methods together](#Chaining-Series-methods-together)
# * [Membuat Indeks lebih bermakna :D](#MembuatIndeks-lebih-bermakna-:D)
# * [Mengubah Nama Baris dan Kolom](#Mengubah-Nama-Baris-dan-Kolom)
# * [Membuat dan Menghapus Kolom](#Membuat-dan-Menghapus-Kolom)

# In[1]:


import pandas as pd
import numpy as np


# # Memahami anatomi DataFrame

# In[2]:


pd.set_option('max_columns', 8, 'max_rows', 10)


# In[3]:


movie = pd.read_csv('data/movie.csv')
movie.head()


# # Mengakses Komponen DataFrame

# In[4]:


columns = movie.columns
index = movie.index
data = movie.values


# In[5]:


columns


# In[6]:


index


# In[7]:


data


# In[8]:


type(index)


# In[9]:


type(columns)


# In[10]:


type(data)


# In[11]:


issubclass(pd.RangeIndex, pd.Index)


# In[12]:


index.values


# In[13]:


columns.values


# # Memahami Tipe Data

# In[14]:


movie = pd.read_csv('data/movie.csv')


# In[15]:


movie.dtypes


# In[16]:


movie.get_dtype_counts()


# # Memilih satu kolom dari data sebagai Series

# In[17]:


movie = pd.read_csv('data/movie.csv')


# In[18]:


movie['director_name']


# In[19]:


movie.director_name


# In[20]:


type(movie['director_name'])


# In[21]:


director = movie['director_name'] # simpan sarive ke variabel
director.name


# In[22]:


director.to_frame().head()


# # Memanggil Method Series

# In[23]:


s_attr_methods = set(dir(pd.Series))
len(s_attr_methods)


# In[24]:


df_attr_methods = set(dir(pd.DataFrame))
len(df_attr_methods)


# In[25]:


len(s_attr_methods & df_attr_methods)


# In[26]:


movie = pd.read_csv('data/movie.csv')
director = movie['director_name']
actor_1_fb_likes = movie['actor_1_facebook_likes']


# In[27]:


director.head()


# In[28]:


actor_1_fb_likes.head()


# In[29]:


pd.set_option('max_rows', 8)
director.value_counts()


# In[30]:


actor_1_fb_likes.value_counts()


# In[31]:


director.size


# In[32]:


director.shape


# In[33]:


len(director)


# In[34]:


director.count()


# In[35]:


actor_1_fb_likes.count()


# In[36]:


actor_1_fb_likes.quantile()


# In[37]:


actor_1_fb_likes.min(), actor_1_fb_likes.max(), actor_1_fb_likes.mean(), actor_1_fb_likes.median(), actor_1_fb_likes.std(), actor_1_fb_likes.sum()


# In[38]:


actor_1_fb_likes.describe()


# In[39]:


director.describe()


# In[40]:


actor_1_fb_likes.quantile(.2)


# In[41]:


actor_1_fb_likes.quantile([.1, .2, .3, .4, .5, .6, .7, .8, .9])


# In[42]:


director.isnull()


# In[43]:


actor_1_fb_likes_filled = actor_1_fb_likes.fillna(0)
actor_1_fb_likes_filled.count()


# In[44]:


actor_1_fb_likes_dropped = actor_1_fb_likes.dropna()
actor_1_fb_likes_dropped.size


# ## Masih ada lagi

# In[45]:


director.value_counts(normalize=True)


# In[46]:


director.hasnans


# In[47]:


director.notnull()


# # Bekerja dengan Operator pada Series

# In[48]:


pd.options.display.max_rows = 6


# In[49]:


5 + 9


# In[50]:


4 ** 2


# In[51]:


a = 10


# In[52]:


5 <= 9


# In[53]:


'abcde' + 'fg'


# In[54]:


not (5 <= 9)


# In[55]:


7 in [1, 2, 6]


# In[56]:


set([1,2,3]) & set([2,3,4])


# In[58]:


[1, 2, 3] - 3


# In[ ]:


a = set([1,2,3])     
a[0]


# ## Bersiap untuk memulai

# In[ ]:


movie = pd.read_csv('data/movie.csv')
imdb_score = movie['imdb_score']
imdb_score


# In[ ]:


imdb_score + 1


# In[ ]:


imdb_score * 2.5


# In[ ]:


imdb_score // 7


# In[ ]:


imdb_score > 7


# In[ ]:


director = movie['director_name']


# In[ ]:


director == 'James Cameron'


# ## Masih ada lagi!

# In[ ]:


imdb_score.add(1)              # imdb_score + 1


# In[ ]:


imdb_score.mul(2.5)            # imdb_score * 2.5


# In[ ]:


imdb_score.floordiv(7)         # imdb_score // 7


# In[ ]:


imdb_score.gt(7)               # imdb_score > 7


# In[ ]:


director.eq('James Cameron')   # director == 'James Cameron'


# In[ ]:


imdb_score.astype(int).mod(5)


# In[ ]:


a = type(1)


# In[ ]:


type(a)


# In[ ]:


a = type(imdb_score)


# In[ ]:


a([1,2,3])


# # Chaining Series methods together

# In[ ]:


movie = pd.read_csv('data/movie.csv')
actor_1_fb_likes = movie['actor_1_facebook_likes']
director = movie['director_name']


# In[ ]:


director.value_counts().head(3)


# In[ ]:


actor_1_fb_likes.isnull().sum()


# In[ ]:


actor_1_fb_likes.dtype


# In[ ]:


actor_1_fb_likes.fillna(0)                .astype(int)                .head()


# ## Masih ada lagi!

# In[ ]:


actor_1_fb_likes.isnull().mean()


# In[ ]:


(actor_1_fb_likes.fillna(0)
                 .astype(int)
                 .head())


# # Membuat Indeks lebih bermakna :D

# In[ ]:


movie = pd.read_csv('data/movie.csv')


# In[ ]:


movie.shape


# In[ ]:


movie2 = movie.set_index('movie_title')
movie2


# In[ ]:


pd.read_csv('data/movie.csv', index_col='movie_title')


# # Masih ada lagi!

# In[ ]:


movie2.reset_index()


# # Mengubah Nama Baris dan Kolom

# In[ ]:


movie = pd.read_csv('data/movie.csv', index_col='movie_title')


# In[ ]:


idx_rename = {'Avatar':'Ratava', 'Spectre': 'Ertceps'} 
col_rename = {'director_name':'Director Name', 
              'num_critic_for_reviews': 'Critical Reviews'} 


# In[ ]:


movie.rename(index=idx_rename, 
             columns=col_rename).head()


# ## Masih ada lagi!

# In[ ]:


movie = pd.read_csv('data/movie.csv', index_col='movie_title')
index = movie.index
columns = movie.columns

index_list = index.tolist()
column_list = columns.tolist()

index_list[0] = 'Ratava'
index_list[2] = 'Ertceps'
column_list[1] = 'Director Name'
column_list[2] = 'Critical Reviews'


# In[ ]:


print(index_list[:5])


# In[ ]:


print(column_list)


# In[ ]:


movie.index = index_list
movie.columns = column_list


# In[ ]:


movie.head()


# # Membuat dan Menghapus Kolom

# In[ ]:


movie = pd.read_csv('data/movie.csv')


# In[ ]:


movie['has_seen'] = 0


# In[ ]:


movie.columns


# In[ ]:


movie['actor_director_facebook_likes'] = (movie['actor_1_facebook_likes'] + 
                                              movie['actor_2_facebook_likes'] + 
                                              movie['actor_3_facebook_likes'] + 
                                              movie['director_facebook_likes'])


# In[ ]:


movie['actor_director_facebook_likes'].isnull().sum()


# In[ ]:


movie['actor_director_facebook_likes'] = movie['actor_director_facebook_likes'].fillna(0)


# In[ ]:


movie['is_cast_likes_more'] = (movie['cast_total_facebook_likes'] >= 
                                  movie['actor_director_facebook_likes'])


# In[ ]:


movie['is_cast_likes_more'].all()


# In[ ]:


movie = movie.drop('actor_director_facebook_likes', axis='columns')


# In[ ]:


movie['actor_total_facebook_likes'] = (movie['actor_1_facebook_likes'] + 
                                       movie['actor_2_facebook_likes'] + 
                                       movie['actor_3_facebook_likes'])

movie['actor_total_facebook_likes'] = movie['actor_total_facebook_likes'].fillna(0)


# In[ ]:


movie['is_cast_likes_more'] = movie['cast_total_facebook_likes'] >=                                   movie['actor_total_facebook_likes']
    
movie['is_cast_likes_more'].all()


# In[ ]:


movie['pct_actor_cast_like'] = (movie['actor_total_facebook_likes'] / 
                                movie['cast_total_facebook_likes'])


# In[ ]:


movie['pct_actor_cast_like'].min(), movie['pct_actor_cast_like'].max() 


# In[ ]:


movie.set_index('movie_title')['pct_actor_cast_like'].head()


# ## Masih ada lagi!

# In[ ]:


profit_index = movie.columns.get_loc('gross') + 1
profit_index


# In[ ]:


movie.insert(loc=profit_index,
                 column='profit',
                 value=movie['gross'] - movie['budget'])


# In[ ]:


movie.head()

