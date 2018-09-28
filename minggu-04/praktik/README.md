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
menggunakan `as` tapi diawali menggunakan `from`
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
Python interpreter memiliki module standard yang kemudian disebut sebagai
"Library Reference", beberapa module sudah berada didalam interpreter Python
ini memungkinkan akses ke sebuah operasi yang bukan bagian dari Python.
Kumpulan module tersebut adalah opsi konfigurasi dan tergantung pada platform yang digunakan,
contohnya seperti module `winreg` yang hanya dapat ditemukan di sistem operasi Windows,
tapi ada juga module yang ada disemua platform seperti `sys` yang sudah termasuk didalam
interpreter Python.

Variable `sys.ps1` dan `sys.ps2` contoh :
```python
import sys
print(sys.ps1)
print(sys.ps2)
sys.ps1 = 'C> '
print('Yuck!')

# Output
# '>>> '
# '... '
# Yuck!
# C>
```

kedua vairable diatas hanya dapat digunakan didalam mode interaktif

variable `sys.path` adalah daftar string yang menentukan jalur penelusuran
interpreter untuk modul. Ini diinisialisasi ke jalur default yang diambil
dari envirounment variable `PYTHONPATH`, atau dari bawaan (default) jika
`PYTHONPATH` tidak diatur. Anda dapat memodifikasinya menggunakan operasi
daftar standar:

```python
import sys
sys.path.append('/ufs/guido/lib/python')
```

<hr>

## 6.3. [The dir() Function]()
Fungsi `dir()` digunakan untuk mencari nama module yang didefinisikan
```python
import fibo, sys
print(dir(fibo))
print(dir(sys))
```

kode diatas akan menampilkan list string berisi nama module
```
['__name__', 'fib', 'fib2']
['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',
 '__package__', '__stderr__', '__stdin__', '__stdout__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe',
 '_home', '_mercurial', '_xoptions', 'abiflags', 'api_version', 'argv',
 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder',
 'call_tracing', 'callstats', 'copyright', 'displayhook',
 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix',
 'executable', 'exit', 'flags', 'float_info', 'float_repr_style',
 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencoding', 'getobjects', 'getprofile', 'getrecursionlimit',
 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettotalrefcount',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path',
 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1',
 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit',
 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout',
 'thread_info', 'version', 'version_info', 'warnoptions']
```

jika tidak diberikan argument maka `dir()` akan menampilkan list yang kita buat
```python
a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
print(dir())

# Output
# ['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```
> Yang ditampilkan adalah : variables, modules, functions, etc.

jika ingin menampilkan built-in variable dan function tambahkan argument `builtins`
```python
import builtins
print(dir(builtins))
```
maka akan menampilkan
```
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
```

<hr>

## 6.4. [Packages](https://docs.python.org/3/tutorial/modules.html#the-dir-function)
Ada sebuah cara untuk mengelompokkan modules agar kode Python terorganisir, entah itu
`function`, `class`, `variable` dan lainnya, ini yang kemudian disebut sebagai *package*
jika sebuah module mempunya submodule maka cara mengaksesnya adalah dengan dot (`.`)
berikut ini adalah contoh struktur module yang dikelompokkan sehingga membentuk sebuah package

```
./mocostore
├── app
│   ├── __init__.py
│   ├── admin
│   │   └── user
│   │       ├── account
│   │       │   └── ...py
│   │       ├── books
│   │       │   └── ...py
│   │       ├── dashboard
│   │       │   └── ...py
│   │       └── project
│   │           └── ...py
│   ├── admin
│   │   └── user
│   │       ├── account
│   │       │   └── ...py
│   │       ├── book
│   │       │   └── ...py
│   │       ├── member
│   │       │   └── ...py
│   │       ├── project
│   │       │   └── ...py
│   │       └── __init__.py
│   ├── templates
│   │   └── admin
│   │       ├── account
│   │       │   └── ...html
│   │       ├── books
│   │       │   └── ...html
│   │       ├── dashboard
│   │       │   └── ...html
│   │       ├── project
│   │       │   └── ...html
│   │       └── layout.html
│   └── utils
│       ├── database.py
│       ├── encoder.py
│       ├── helper.py
│       ├── hooks.py
│       ├── jinja.py
│       ├── mailer.py
│       ├── parsedatetime.py
│       └── ...
├── config.py
├── requirements.txt
└── run.py
```
berkas `__init__.py` wajib dibuat jika ingin membuat suatu package, berkas `__init__.py`
bisa saja tidak terisi kode apapun.

Sebagai contoh, kita akan memanggil module `database` yang berada didalam package
`utils` :
```python
import app.utils.database.connect
```
jika dengan cara diatas maka item yang terakhir haruslah module atau subpackage
*bukan* `class`, `function`, atau `variable`.

atau bisa juga menggunakan from
```python
from app.utils.database import connect
```

Jikang menggunakan `from package import item` maka item yang dimaksudkan bisa jadi
submodule (atau subpackage) dari sebuah package, atau yang pendefinisian lainnya
seperti `function`, `class`, atau `variable`. Jika yang kita memanggil dengan nama yang salah
atau yang dipanggil tidak ada maka akan mengembalikan error [*ImportError*](https://docs.python.org/3/library/exceptions.html#ImportError)

### 6.4.1. [Importing * From a Package](https://docs.python.org/3/tutorial/modules.html#packages)
### 6.4.2. [Intra-package References](https://docs.python.org/3/tutorial/modules.html#intra-package-references)
### 6.4.3. [Packages in Multiple Directories](https://docs.python.org/3/tutorial/modules.html#packages-in-multiple-directories)

<hr>

# 7. [Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
## 7.1. [Fancier Output Formatting](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting)
### 7.1.1. [Formatted String Literals](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)
### 7.1.2. [The String format() Method](https://docs.python.org/3/tutorial/inputoutput.html#the-string-format-method)
### 7.1.3. [Manual String Formatting](https://docs.python.org/3/tutorial/inputoutput.html#manual-string-formatting)
### 7.1.4. [Old string formatting](https://docs.python.org/3/tutorial/inputoutput.html#old-string-formatting)

<hr>

## 7.2. [Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
### 7.2.1. [Methods of File Objects](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects)
### 7.2.2. [Saving structured data with json](https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json)

<hr>

# 8. [Errors and Exceptions]()
## 8.1. [Syntax Errors]()
<hr>
## 8.2. [Exceptions]()
<hr>
## 8.3. [Handling Exceptions]()
<hr>
## 8.4. [Raising Exceptions]()
<hr>
## 8.5. [User-defined Exceptions]()
<hr>
## 8.6. [Defining Clean-up Actions]()
<hr>
## 8.7. [Predefined Clean-up Actions]()

<hr>

# 9. [Classes]()
## 9.1. [A Word About Names and Objects]()
<hr>
## 9.2. [Python Scopes and Namespaces]()
### 9.2.1. [Scopes and Namespaces Example]()
<hr>
## 9.3. [A First Look at Classes]()
### 9.3.1. [Class Definition Syntax]()
### 9.3.2. [Class Objects]()
### 9.3.3. [Instance Objects]()
### 9.3.4. [Method Objects]()
### 9.3.5. [Class and Instance Variables]()
<hr>
## 9.4. [Random Remarks]()
<hr>
## 9.5. [Inheritance]()
### 9.5.1. [Multiple Inheritance]()
<hr>
## 9.6. [Private Variables]()
<hr>
## 9.7. [Odds and Ends]()
<hr>
## 9.8. [Iterators]()
<hr>
## 9.9. [Generators]()
<hr>
## 9.10. [Generator Expressions]()
