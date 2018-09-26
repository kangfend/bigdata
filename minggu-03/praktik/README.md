# Struktur Data
Memahami struktur data di Python 3.7

<hr>

## 5.1. [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
Tipe data list (array) mempunyai beberapa method, dianratanya adalah :
- `list.append(x)` menambahkan item diakhir list
- `list.extend(iterable)` memperpanjang list dengan item dari perluangan
- `list.insert(i, x)` menambahkan item berdasarkan index
- `list.remove(x)` menghapus item berdasarkan value
- `list.pop([i])` menghapus item diakhir list
- `list.clear()` menghapus semua item
- `list.index(x[, start[, end]])`
- `list.count(x)` menghitung jumlah item
- `list.sort(key=None, reverse=False)` mengurutkan item
- `list.reverse()` membolak balik urutan item
- `list.copy()` menyalin isi dari list

```python
#!/usr/bin/python3.7

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))

print(fruits.count('tangerine'))

print(fruits.index('banana'))

print(fruits.index('banana', 4))  # Find next banana starting a position 4

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

fruits.pop()
print(fruits)
```

jika kode diatas dijalankan maka, akan menampilkan
```
2
0
3
6
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']
```

### 5.1.1. [Using Lists as Stacks](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks)
Ini hanya istilah penggunaan list sebagai stack (tumpukan) list, dimana ketika sebuah item ditambah maka akan ditempatkan dipaling akhir "_last-in, first-out_", untuk menambahkan item menggunakan `append()` dan untuk mengapus menggunakan `pop()`


### 5.1.2. [Using Lists as Queues](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues)
Kita dapat menggunakan list sebagai sebuah antrian dimana elemen yang paling pertama ditambahkan maka elemen itulah yang pertama diterima, menambahkan item diakhir list sangatlah cepat tapi sayangnya menambahkan diawal sangatlah lambat, karena semua elemen harus dibagi satu persatu. Contoh:

```python
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()
queue
```

jika kode diatas dijalankan maka akan menampilkan
```
deque(['Michael', 'Terry', 'Graham'])
```

### 5.1.3. [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
Ini adalah cara yang mudah untuk membuat list, menggunakan iterasi (perulanang), contoh:

```python
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
```

jika kode diatas dijalankan maka akan menampilkan list
```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
Perlu diketahui bahwa kode diatas akan membuat variabel `x` dan akan tetap dapat diakses dari luar blok perluangan, untuk mengatasi hal itu, dengan cara berikut ini:
```python
squares = list(map(lambda x: x**2, range(10)))
# atau
squares = [x**2 for x in range(10)]
```

kedua baris kode sama saja, tapi yang kedua lebih mudah dibaca dan singkat.

Dalam pebuatan list, dapat jika melibatkan penanganan kondisi seperti `if...else` dan dapat dilakukan hanya dengan satu baris saja, contoh :
```python
list_dengan if = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(list_dengan_if)
```

```python
list_dengan_if = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            list_dengan_if.append((x, y))

print(list_dengan_if)
```

kedua kode diatas akan sama saja, yaitu membuatkan list yang isinya seperti ini :
```
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

Perlu diketahui juga bahwa jika item list berupa `tuple` maka harus diapit dengan `(...)`, contoh:
```python
from math import pi
list_math = [str(round(pi, i)) for i in range(1, 6)]
```

### 5.1.4. [Nested List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)
Ini adalah list didalam list, karena list dapat menampung beberapa tipe data sekaligus
begitu juga dengan list yang ada didalamnya, contoh :
```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
```

kode berikut ini untuk mengubah urutan baris dan kolom matrix diatas
```python
ubah_urutan_matrix = [[row[i] for row in matrix] for i in range(4)]
print(ubah_urutan_matrix)
```

maka matrix tersebut akan menjadi
```
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

proses diatas akan lebih mudah jika menggunakan function `zip`
```python
matrix_dengan_zip = list(zip(*matrix))
print(matrix_dengan_zip)
```
dan menggunakan [unpacking Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments)

<hr>

## 5.2. [The del statement](https://docs.python.org/3/tutorial/datastructures.html#the-del-statement)
Jika di sub-bab sebelumnya menghapus item pada list menggunakan `remove()` atau `pop()`
maka ada cara lain yaitu dengan menggunakan keyword `del`, berikut ini adalah contoh untuk menghapus item berdasarkan index nya
```python
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
```

bisa juga menghapus dengan memanfaatkan slice
```python
del a[2:4]
print(a)
```
atau menghapus variable
```python
del a
```

<hr>

## 5.3. [Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
Sebelumnya kita melihat ada beberapa properti yang digunakan dalam list seperti `indexing` dan `slicing`, itu adalah dua contoh dari tipe data [_sequence_](https://docs.python.org/3/library/stdtypes.html#typesseq)
dan ada juga tipe data _sequence_ yang lainnya yaitu `tuple`.

Tuple adalah tipe data yang nilainya dipisahkan dengan koma
```python
t = 12345, 54321, 'hello!'
t[0]
print(t)
```

nilanya juga bisa _nested_
```python
u = t, (1, 2, 3, 4, 5)
print(u)
```

dan tuple adalah tipe data yang sifatnya _immutable_
```python
t[0] = 88888
```
kode diatas akan error seperti berikut ini:
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

dan tentunya dapat menampung beberapa object
```python
v = ([1, 2, 3], [3, 2, 1])
print(v)
```

Ini adalah tuple packing `t = 12345, 54321, 'hello!'` yang artinya variable `t`
mempunyai nilai bertipe data tuple dengan nilai `12345`, `54321`, `'hello!'`, operasi sebaliknya adalah

```python
x, y, z = t
print(t)
print(x)
print(y)
print(z)
```

<hr>

yang artinya setiap item yang ada didalam tuple milik variable `t` akan di _unpacking_ kemudian diserahkan ke variable `x`, `y`, `z`,
urutan _unpacking_ berjalan dengan baik untuk semua urutan yang ada disebelah kanan `=`

## 5.4. [Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
Python juga mempunyai tipe data lain yaitu sets, yang menyimpan nilainya tidak berurutan

```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)

print (a - b)
print(a | b)
print(a & b)
print(a ^ b)
```

kode diatas yang akan menampilkan
```
{'orange', 'banana', 'pear', 'apple'}
True
False
{'a', 'r', 'b', 'c', 'd'}
{'r', 'd', 'b'}
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
{'a', 'c'}
{'r', 'd', 'b', 'm', 'z', 'l'}
```

Sama dengan list dan tuple, sets juga mendukung penggunaan loop dan if didalamnya
```python
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
```

<hr>

## 5.5. [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

Tipe data lain pada Python yang dapat menyimpan banyak nilai yaitu _Dictionaries_
tipe data ini bukan hanya menyimpan nilai banyak juga dapat menyimpan nilai yang berbagai macam tipe datanya.
Berbeda dengan tipe data sebelumnya yang memiliki _sequence_ seperti `tuple` dan `list` yang diindeks menggunakan nomor
tipe data ini diindeks menggunakan _key_ yaitu sebuah kunci dimana kita dapat menggunakan key tersebut untuk mereferensi sebuah nilai untuk key tersebut

berikut ini adalah contoh penggunaanya :

```python
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('jack' not in tel)
```

jika kode diatas dijalankan akan menampilkan :
```
{'jack': 4098, 'sape': 4139, 'guido': 4127}
4098
{'jack': 4098, 'guido': 4127, 'irv': 4127}
['jack', 'guido', 'irv']
['guido', 'irv', 'jack']
True
False
```

Fungsi `dict()` dapat membuat dictionaries secara langsung dari urutan key-value yang berpasangan
```python
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
# Output
# {'sape': 4139, 'guido': 4127, 'jack': 4098}
```

Sebagai tambahan, pembuatan _dictionaries_ juga bisa menggunakan perluangan `for`
```python
print({x: x**2 for x in (2, 4, 6)})
# Output
# {2: 4, 4: 16, 6: 36}
```

Jika _key_ adalah string yang sederhana, lebih mudah jika kita menggunakan cara berikut ini
```python
print(dict(sape=4139, guido=4127, jack=4098))
# Output
# {'sape': 4139, 'guido': 4127, 'jack': 4098}
```

<hr>

## 5.6. [Looping Techniques](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques)
Ketika menggunakan perluangan pada _dictionaries_, key yang akan digunakan bisa didapatkan pada putaran yang sama menggunakan method `items()`

```python
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# Output
# gallahad the pure
# robin the brave
```

Ketika menggunakan perluangan untuk sebuah urutan, posisi indeks yang sesuai dengan nilainya bisa didapatkan menggunakan fungsi `enumerate()`

```python
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# Output
# 0 tic
# 1 tac
# 2 toe
```

Melakukan perulangan untuk dua atau lebih secara bersamaan, list dapat digabungkan menggunakan fungsi `zip()`

```python
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

 # Output
# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.
```

Untuk melakukan perulangan secara berurutan yang dibalik, dapat menggunakan fungsi `reversed()`

```python
for i in reversed(range(1, 10, 2)):
    print(i)

# Output
# 9
# 7
# 5
# 3
# 1
```

Untuk melakukan perulangan secara berurutan yang di urutkan, dapat menggunakan fungsi `sorted()`

```python
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# Output
# apple
# banana
# orange
# pear
```

Terkadang kita ingin memodifikasi list selama menjalankan perulangan, ada sebuah cara yang aman dan sederhana untuk melakukannya
yaitu dengan membuat list baru
```python
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

# Output
# [56.2, 51.7, 55.3, 52.5, 47.8]
```

<hr>

## 5.7. [More on Conditions](https://docs.python.org/3/tutorial/datastructures.html#more-on-conditions)
Kondisi yang digunakan oleh statement `while` dan `if` tidak hanya operator komparasi tapi bisa jadi mengandung operator lain
Operator komparasi `in` dan `not in` memeriksa apakah nilainya terdapat pada _sequence_ atau tidak
Operator `is` dan `is not` mengkomparasi sebuah objek yang sama persis, ini hanya akan berfungsi untuk objek yang bersifat `mutable`
seperti list. Semua operator komparasi mempunya prioritas yang sama, yang lebih rendah dari semua operator numerik

Operator komparasi pun dapat digabungkan, contohnya `a < b == c`, yang akan menguji apakah a kurang dari b kemudian b sama dengan c

Komparasi juga bisa dikombinasikan dengan _Boolean_ operator `and` dan `or`, dan hasil perbandingan atau ekspresi boolean lainnya dapat dinegasikan dengan `not`,
negasi prioritasnya lebih rendah dari operator.

Diantara operator diatas tidak memiliki prioritas tertinggi atau terendah, sehingga `A` dan `B` setara dengan `(A and (not B)) or C`,
boolean operator `and` dan `or` juga disebut dengan operator `short-circuit` yang mana keduanya akan mengevaluasi mulai dari kiri ke kanan

Dengan demikian kita dapat meng-assign hasil dari sebuah komparasi atau ekspresi boolean yang lainnya ke sebuah variabel, contohnya
```python
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

# Output
# 'Trondheim'
```

<hr>

## 5.8. [Comparing Sequences and Other Types](https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types)

Objek `sequence` bisa dikomparasikan dengan objek lainnya. Komparasi ini menggunakan pengurutan _lexicographical_

```
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```

## Selamat Belajar!
