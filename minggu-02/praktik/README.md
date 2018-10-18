# Memahami Pengendalian Kondisi

## 4. [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools)
Selain `while` untuk perulangan Python seperti pada bahasa pemrograman lainnya
yaitu mempunyai statement untuk mengendalikan sebuah kondisi dan alur.

### 4.1. [if Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
```
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 45
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Single')
... else:
...     print('More')
...
More
>>>
```

Statement diatas mempunyai 4 kondisi penanganan

### 4.2. [for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)

Berikut ini adalah contoh penggunaan perulangan menggunakan `for`
```
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12
```

Contoh diatas mterdapat 3 buah nilai yang disimpan pada variable `words`
dengan tipe data list yang artinya, kita hanya bisa menggunakan for pada suatu
nilai atau variable yang sifatnya `iterable`

### 4.3. [The range() Function](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)
Fungsi `range()` memudahkan kita pada saat kita ingin melakukan iterasi dengan
pengurutan nomor, karena fungsi `range` dapat men-_generate_ sebuah deret aritmetika

Contoh
```
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
```

`range` seperti `list` yang sifatnya iterable dan memulai index mulai dari `0`

kita dapat membuat suatu perulangan menggunakan fungsi `range` dengan
memberikan rentan tertentu, contoh:
```
>>> coba = list(range(0, 10, 3))
>>> print(', '.join(coba))
0, 3, 6, 9
```

contoh diatas, fungsi range menerima 3 argument :
1. `0` titik awal perluangan
2. `10` jumlah iterasi
3. `3` rentan (lompatan) disebut juga sebagai _step_

### 4.4. [break and continue Statements, and else Clauses on Loops](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
Pada saat kita melakukan perulangan mungkin terdapat sebuah kondisi dimana kita
harus menghentikan atau melompatinya

- jika menggunakan `for`
`else` statement akan dieksekusi dan menghentikan proses looping jika list telah habis
- jika menggunakan whila
`else` satatement akan dieksekusi dan menghentika proses looping jika
kondisinya `False`
- `break` statement akan dieksekusi jika kita menghendaki terjadinya suatu kondisi tertentu

Contoh
```
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # berhenti karena tidak menemukan sebuah faktor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

### 4.5. [pass Statements](https://docs.python.org/3/tutorial/controlflow.html#pass-statements)
`pass` tidak melakukan apapun, ini digunakan ketika suatu blok statement mengharuskan adanya kelanjutan dari program.

biasanya digunakan kita kita membuat suatu `class` tapi kita belum ingin
menuliskan body dari class itu sendiri, contoh :
```
>>> class KelasKosong:
...     pass
...
>>>
```

bisa juga digunakan didalam statement `while`
```
>>> while True:
...     pass
...
^CTraceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
>>>
```

proses looping akan dihentikan ketika pengguna menekan CTRL+C

dan bisa juga digunakan untuk mendefinisikan sebuah fungsi yang kosong
(seperti contoh `class` diatas)
```
>>> def fungsi_kosong():
...     pass
...
```

### 4.6. [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
Sebuah fungsi digunakan untuk meringkas atau membungkus suatu proses sehingga
dapat dipanggil untuk digunakan lagi, ini biasa disebut `reusable code`

membuat sebuah fungsi sangatlah mudah, tulis keyword `def` diikuti dengan nama
fungsi kemudian parameternya diapit dengan buka dan tutup kurung. Fungsi juga
dapat mempunyai sebuah "dokumentasi" (opsional) atau biasa disebut
_string literal_ sebagai penjelasan untuk penulis kode dari fungsi itu sendiri contoh:
```
>>> def fib(n):
...     """Print a Fibonacci series up to n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
>>>
```
fungsi diatas untuk menampilkan bilangan fibonacci sampai ke _n_

### 4.7. More on Defining Functions
#### 4.7.1. [Default Argument Values](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values)
Argument pada sebuah fungsi dapat diberikan nilai default, contoh

```
>>> def ask_ok(prompt, retries=4, reminder='Please try again!'):
...     while True:
...         ok = input(prompt)
...         if ok in ('y', 'ye', 'yes'):
...             return True
...         if ok in ('n', 'no', 'nop', 'nope'):
...             return False
...         retries = retries - 1
...         if retries < 0:
...             raise ValueError('invalid user response')
...         print(reminder)
...
>>> ask_ok('Do you really want to quit?')
Do you really want to quit?
Please try again!
Do you really want to quit?y
True
>>> ask_ok('OK to overwrite the file?', 2)
OK to overwrite the file?y
True
>>> ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
OK to overwrite the file?yes
True
>>>
```
Keyword `in` digunakan untuk memerika apakah yang kita masukan terdaftar atau tidak

> Default value hanya akan dievaluasi sekali saja, sehingga nilai yang dimasukkan akan berbeda jika menggunakan `immutable`

#### 4.7.2. [Keyword Arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)
Sebuah fungsi juga dapat dipanggil menggunakan _keyword argument_ dengan format `nama_argumen=nilai`
```
>>> def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.")
...     print("-- Lovely plumage, the", type)
...     print("-- It's", state, "!")
...
>>> parrot(action='VOOOOOM', voltage=1000000)
-- This parrot wouldn't VOOOOOM if you put 1000000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff !
```

**Tetapi** perlu diingat bahwa pemanggilan fungsi harus benar, contoh berikut ini
akan menghasilkan error karena argument yang diberikan tidak benar
```
parrot()                     # tidak ada argument
parrot(voltage=5.0, 'dead')  # non-keyword argument setelah keyword argument
parrot(110, voltage=220)     # duplicate value untuk argument yang sama
parrot(actor='John Cleese')  # keyword argument tidak diketahui
```

> urutan argument pada saat pemanggilan tidaklah penting

Untuk urusan pemanggilan keyword argument dengan cara diatas cukup membuat pusing
maka dari itu, Python memperkenalkan cara yang lebih singkat yang menerima sebuah
`dictionary` yang mana mengandung semua keyword yang diberikan, cara menggunakannya
adalah menambahkan `**name` untuk argument yang mempunyai default value dan `*name`
untuk argument biasa, berikut contohnya :

```
>>> def cheeseshop(kind, *arguments, **keywords):
...     print("-- Do you have any", kind, "?")
...     print("-- I'm sorry, we're all out of", kind)
...     for arg in arguments:
...         print(arg)
...     print("-" * 40)
...     for kw in keywords:
...         print(kw, ":", keywords[kw])
...
>>> cheeseshop("Limburger", "It's very runny, sir.",
...            "It's really very, VERY runny, sir.",
...            shopkeeper="Michael Palin",
...            client="John Cleese",
...            sketch="Cheese Shop Sketch")
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
```

#### 4.7.4. [Unpacking Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists)
Digunakan ketika argumen sudah ada dalam `list` atau `tuple` tetapi perlu
dibongkar untuk panggilan fungsi yang membutuhkan argumen posisi terpisah
```
>>> list(range(3, 6))
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))
[3, 4, 5]
```

Dengan cara yang sama, dictionary dapat menyampaikan keyword argument dengan operator `**`

```
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```

#### 4.7.5. [Lambda Expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
Lambda expression sebenarnya sama dengan fungsi namun tidak memiliki nama atau biasa
disebut `anonymous function` fungsi ini mengembalikan penjumlahan dari dua buah argument.
Lambda sangat berguna dan menulisnya cukup singkat karena hanya membutuhkan satu baris saja
dan bisa langsung di _assign_ ke variable

```
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```

Secara semantik fungsi ini adalah _syntactic sugar_ nya fungsi biasa

```
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

Contoh diatas digunakan untuk sebuah fungsi yang argument nya harus fungsi

#### 4.7.6. [Documentation Strings](https://docs.python.org/3/tutorial/controlflow.html#documentation-strings)
Document String atau sering juga disebut "Doc String" adalah sebuah komentar yang diberikan
penulis kode untuk sebuah fungsim, ini sangat membantu sekali dalam debugging atau
ketika kode kita dilihat oleh orang lain yang ingin memahaminya

Aturannya :
1. Baris pertama haruslah singkat atau ringkasan singkat dari tujuan fungsi dibuat
2. Jika ingin lebih dari satu baris maka baris kedua haruslah kosong
3. menggunakan string `"""`

```
>>> def my_function():
...     """Do nothing, but document it.
...
...     No, really, it doesn't do anything.
...     """
...     pass
...
>>> print(my_function.__doc__)
Do nothing, but document it.

    No, really, it doesn't do anything.
```

#### 4.7.7. [Function Annotations](https://docs.python.org/3/tutorial/controlflow.html#function-annotations)
Anotasi pada fungsi adalah informasi metadata yang bersifat opsional tentang tipe data,
lebih jelasnya [PEP 3107](https://www.python.org/dev/peps/pep-3107) dan
[PEP 484](https://www.python.org/dev/peps/pep-0484)

Annotations disimpan pada atribut `__annotations__` dan tidak memberikan dampak
apapun pada bagian fungsi.

Anotasi pada parameter didefinisikan dengan `:` setelah nama parameter, sedangkan
Anotasi untuk return didefinisikan dengan `->` setelah tutup kurung parameter dan sebelum `:`.

```
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs
```

#### 4.8. [Intermezzo: Coding Style](https://docs.python.org/3/tutorial/controlflow.html#intermezzo-coding-style)
Jika kita menulis kode sampai ratusan bahkan ribuan baris, dan dengan algoritma
maupun alur yang rumit maka sudah saatnya membahas tentang gaya penulisan pada Python

Karena mempermudah orang lain untuk membaca kode yang kita tulis merupakan
ide yang baik bukan?, untuk itu, mengadopsi gaya penulisan kode yang bagus sangat
membantu.

Python mempunyai "kamus" gaya penulisan kode yang sudah banyak dipakai untuk
memperkenalkan gaya penulisan kode yang sangat mudah dibaca dan menyenangkan mata
dan setiap Pythonista harus membacanya, berikut ini adalah beberapa poin
penting yang harus diketahui :

1. Gunakan 4 spasi untuk indentasi, dan tidak ada tab
2. Wrap baris kode sampai 79 karakter
3. Gunakan baris kosong untuk memberikan jarak setiap fungsi dan kelas
4. Gunakan docstring
5. Gunakan spasi untuk operator dan setelah koma mis: `a = f(1, 2) + g(3, 4)`
6. Konsisten memberikan nama fungsi dan kelas, `CamelCase` untuk nama kelas dan
`lower_case_with_underscores` untuk nama fungsi
7. Jangan gunakan _fancy encodings_ secara default `UTF-8` dan `ASCII` berjalan dengan baik
8. Juga, jangan gunakan _non-ASCII characters in identifiers_

**Selamat Belajar!**
