#!/usr/bin/env python
# coding: utf-8

# ### Import Modul

# In[1]:


import numpy as np
import pandas as pd


# ### Series
# 
# ```s = pd.Series(data, index=index)```
# `data` dapat beberapa macam diataranya :
# - sebuah Python dictionary
# - sebuah ndarray
# - sebuah nilai scalar (seperti 5)

# ##### data dari ndarray

# In[3]:


s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
s


# In[4]:


s.index


# In[5]:


pd.Series(np.random.randn(5))


# #### Data dari dictionary

# In[6]:


d = {'b' : 1, 'a' : 0, 'c' : 2}
pd.Series(d)


# In[7]:


d = {'a' : 0., 'b' : 1., 'c' : 2.}
pd.Series(d)


# In[8]:


pd.Series(d, index=['b', 'c', 'd', 'a'])


# #### Data dari nilai scalar

# In[9]:


pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])


# #### Series is ndarray-like

# In[10]:


s[0]


# In[11]:


s[:3]


# In[12]:


s[s > s.median()]


# In[13]:


s[[4, 3, 1]]


# In[14]:


np.exp(s)


# #### Series is dict-like

# In[16]:


s['a']


# In[15]:


s['e'] = 12.
s


# In[17]:


'e' in s


# In[18]:


'f' in s


# jika label tidak mengandung karakter yang dimaksud akan muncul error

# In[19]:


s['f']


# jika tidak ingin mendapatkan error tapi digantikan dengan None maka bisa menggunakan method `get`

# In[20]:


s.get('f')
s.get('f', np.nan)


# #### Operasi vektor pelabelan menggunakan series

# In[21]:


s + s


# In[22]:


s * 2


# In[23]:


np.exp(s)


# In[24]:


s[1:] + s[:-1]


# #### Atribut Nama

# In[25]:


s = pd.Series(np.random.randn(5), name='something')
s


# In[26]:


s.name


# mengubah nama atribut series

# In[27]:


s2 = s.rename("different")
s2.name


# ### DataFrame
# DataFrame adalah struktur data berlabel 2 dimensi dengan kolom jenis yang berpotensi berbeda. Seperti series, DataFrame menerima berbagai macam input:
# 
# - Dict of 1D ndarrays, lists, dicts, or Series
# - 2-D numpy.ndarray
# - Structured or record ndarray
# - Sebuah Series
# - dari DataFrame yang lain

# #### Data dari Dict series atau Dict

# In[28]:


d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
df


# In[29]:


pd.DataFrame(d, index=['d', 'b', 'a'])


# In[30]:


pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])


# In[31]:


df.index


# In[32]:


df.columns


# #### Data dari Dict ndarrays / List

# In[33]:


d = {'one' : [1., 2., 3., 4.], 'two' : [4., 3., 2., 1.]}


# In[34]:


pd.DataFrame(d)
pd.DataFrame(d, index=['a', 'b', 'c', 'd'])


# #### Data dari Record Array Terstruktur

# In[36]:


data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])
data[:] = [(1,2.,'Hello'), (2,3.,"World")]
pd.DataFrame(data)


# In[37]:


pd.DataFrame(data, index=['first', 'second'])


# In[38]:


pd.DataFrame(data, columns=['C', 'A', 'B'])


# #### Dari sebuah list dictionary

# In[39]:


data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
pd.DataFrame(data2)


# In[40]:


pd.DataFrame(data2, index=['first', 'second'])


# In[41]:


pd.DataFrame(data2, columns=['a', 'b'])


# #### Dari sebuah Dictionary Tuple

# In[42]:


pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
              ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
              ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
              ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
              ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})


# #### Dari sebuah Series
# Hasilnya akan menjadi DataFrame dengan indeks yang sama dengan Series input, dan dengan satu kolom yang namanya adalah nama asli dari Series (hanya jika tidak ada nama kolom lain yang disediakan).

# #### Konstruktor Alternatif
# `DataFrame.from_dict` mengambil dict daro beberapa dict atau dict dari sebuah array sequences dan mengembalikan DataFrame

# In[43]:


pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]))


# In[44]:


pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]),
                       orient='index', columns=['one', 'two', 'three'])


# `DataFrame.from_records` mengambil daftar tupel atau ndarray dengan dtype terstruktur.

# In[45]:


data


# In[46]:


pd.DataFrame.from_records(data, index='C')


# #### Pemilihan kolom, penambahan, penghapusan

# In[47]:


df['one']


# In[48]:


df['three'] = df['one'] * df['two']
df['flag'] = df['one'] > 2
df


# Kolom dapat dihapus atau di-pop seperti dengan cara:

# In[49]:


del df['two']
three = df.pop('three')
df


# Ketika menggunakan nilai skalar itu secara alami akan disimpan untuk mengisi kolom:

# In[51]:


df['foo'] = 'bar'
df


# In[52]:


df['one_trunc'] = df['one'][:2]
df


# In[53]:


df.insert(1, 'bar', df['one'])
df


# #### Indexing / Selection
# 
# | Operation                      | Syntax          | Result     |
# |--------------------------------|-----------------|------------|
# | Select column	                 | `df[col]`       | Series     |
# | Select row by label            | `df.loc[label]` | Series     |
# | Select row by integer location | `df.iloc[loc]`  | Series     |
# | Slice rows                     | `df[5:10]`      | DataFrame  |
# | Select rows by boolean vector  | `df[bool_vec]`  | DataFrame  |
# 
# Seleksi baris, misalnya, mengembalikan Series yang indeksnya adalah kolom dari DataFrame:

# In[55]:


df.loc['b']


# In[56]:


df.iloc[2]


# #### Penjajaran Data dan Aritmatika

# In[57]:


df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])
df + df2


# In[58]:


df - df.iloc[0]


# In[59]:


index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=list('ABC'))
df


# In[60]:


type(df['A'])


# In[61]:


df - df['A']


# Operasi dengan skalar sama seperti biasanya:

# In[62]:


df * 5 + 2


# In[63]:


1 / df


# In[64]:


df ** 4


# Operator Boolean juga berfungsi:

# In[65]:


df1 = pd.DataFrame({'a' : [1, 0, 1], 'b' : [0, 1, 1] }, dtype=bool)
df2 = pd.DataFrame({'a' : [0, 1, 1], 'b' : [1, 1, 0] }, dtype=bool)
df1 & df2


# In[66]:


df1 | df2


# In[67]:


df1 ^ df2


# In[68]:


-df1

