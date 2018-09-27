# 6. [Modules](https://docs.python.org/3/tutorial/modules.html#modules)
Ketika menuliskan kode program yang sangat panjang menggunakan _Python Interpreter (shell)_
kode yang ditulis akan hilang jika shell ditutup, permasalahan ini dapat diatas dengan
membuat suatu berkas yang berekstensi `.py` ini yang kemudian disebut membuat _script_.

Semakin berkembangnya program yang kita buat, rasanya akan masuk akal jika kita membagi
script tersebut menjadi beberapa potongan agar tidak perlu lagi menyalin potongan kode
ke setiap program, nah ini yang kemudian disebut sebagai _module_. Module adalah berkas yang
mengandung script Python, dan module pun juga dapat mengimpor atau menggunakan module lainnya.
Membuat module pastinyakita berikan nama bukan? nah nama module yang kita buat ini dapat diakses
dengan variabel global yakni `__name__`.

Buatlah berkas dengan nama misal `fibo.py`, kemudian tulislah kode berikut :
```python
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```
kemudian impor modulnya
```python
import fibo
```
setelah diimpor fungsi-fungsi yang ada didalam modul fibo.py siap digunakan
```python
print(fibo.fib(1000))
print(fibo.fib(1000))
print(fibo.__name__)
```
maka akan menghasilkan
```
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
'fibo'
```
jika ingin sering menggunakan fungsi tersebut, dapat di-assign ke variabel lokal
```python
fib = fibo.fib
print(fib(500))

# Output
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

## 6.1. [More on Modules](https://docs.python.org/3/tutorial/modules.html#more-on-modules)
Satu modul bisa mengandung statement yang dapat dieksekusi dan juga pendefinisian fungsi.
statement tersebut dapat digunakan untuk menginisialisasi modul. Setiap modul memiliki
simbol secara private yang digunakan sebagai simbol global oleh seluruh fungsi yang didefinisikan didalamnya.

Berikut ini cara mengimpor module secara spesifik:
```python
from fibo import fib, fib2
print(fib(500))
# Output
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
jika ingin mengimport semua isi dari modul (function, variable, class, dll) gunakan `*` :
```python
from fibo import *
print(fib(500))
# Output
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
jika module yang dibuat memiliki nama yang panjang atau kurang enak dibaca,
bisa saja diubah namanya pada saat impor dengan cara tambahkan `as` kemudian nama pengganti
```python
import fibo as fib
print(fib.fib(500))
# Output
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
bagaimana jika bukan nama modul yang diubah seperti class, function, variable, dll? bisa juga
menggunakan `as` tapi diawali menggunakan `form`
```python
from fibo import fib as fibonacci
print(fib.fib(500))
# Output
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
> Jika menggunakan shell. Untuk alasan efisiensi, setiap modul hanya dapat
diimpor satu kali dalam satu sesi interpreter, jika kamu melakukan perubahan nama
modul maka harus merestart sesi shell, atau bisa juga reload dengan cara `import importlib; importlib.reload(nama_modul)`

### 6.1.1. [Executing modules as scripts](https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts)
Kita dapat mengeksekusi modul secara langsung pada saat menjalankan berkas Python
dengan cara menambahkan `if` dengan kondisi komparasi nama modul, didalam berkas modul, contoh

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```
jika menjalankan module melalui command line artinya module tersebut dieksekusi
dan dianggap sebagai modul `__main__`. berikut cara menggunakannya
```
$ python fibo.py 50
```

### 6.1.2. [The Module Search Path](https://docs.python.org/3/tutorial/modules.html#the-module-search-path)
Bagaimana Python mencari module yang diimpor? Pertama-tama Python akan mencari
_built-in module_ dengan nama yang dimaksud, jika tidak ditemukan,
maka akan mencari module dengan nama yang dimaksud misal `fibo.py` didalam direktori
yang diberikan oleh variabel [sys.path](https://docs.python.org/3/library/sys.html#sys.path).
variable tersebut menginisialisasi dari lokasi berikut :

- Direktori yang mengandung script tersebut (direktori kerja saat ini)
- [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)
- Standar yang tergantung pada saat instalasi Python

Setelah inisialisasi program Python memodifikasi `sys.path`. Yang artinya script
tersebut akan dimuat, bukan module dengan nama yang sama.

> Informasi lebih detil [Standard Module](https://docs.python.org/3/tutorial/modules.html#tut-standardmodules)

### 6.1.3. ["Compiled" Python files](https://docs.python.org/3/tutorial/modules.html#compiled-python-files)
Untuk mempercepat proses import module, Python akan meng-_chache_ module yang dibutuhkan
kemudian menyimpannya kedalam direktori `__pycache__` dengan format nama `module.version.pyc`
dimana version yang dimaksud adalah versi yang dihasilkan dari _compiler_.

Beberapa anjuran untuk yang ahli :
- Gunakan `-0` atau `-00` pada perintah Python untuk mengurangi ukuran modul yang dikompilasi.
yang mana `-0` akan menghilangkan `assert statements`, dan `-00` akan menghilangkan `assert statements` dan `__doc__` string.
- `.pcy` hanya mempercepat proses memuat module, bukan mempercepat program yang dibangun
- [compileall](https://docs.python.org/3/library/compileall.html#module-compileall)
dapat membuat `.pyc` untuk semua berkas modul didalam satu direktori
- lihat lebih detil di [PEP 3147](https://www.python.org/dev/peps/pep-3147)
yang memuat flow-chart keputusan dari proses ini

<hr>

## 6.2. [Standard Modules](https://docs.python.org/3/tutorial/modules.html#standard-modules)

<hr>

## 6.3. [The dir() Function]()

<hr>

## 6.4. [Packages](https://docs.python.org/3/tutorial/modules.html#the-dir-function)
### 6.4.1. [Importing * From a Package](https://docs.python.org/3/tutorial/modules.html#packages)
### 6.4.2. [Intra-package References](https://docs.python.org/3/tutorial/modules.html#intra-package-references)
### 6.4.3. [Packages in Multiple Directories](https://docs.python.org/3/tutorial/modules.html#packages-in-multiple-directories)
