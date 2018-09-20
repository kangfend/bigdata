# Struktur Data
Memahami struktur data di Python 3.7

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

