# Pustaka Standar di Python

# 10. [Brief Tour of the Standard Library](https://docs.python.org/3/tutorial/stdlib.html)
Tur singkat untuk Pustaka Standar Python

## 10.1. [Operating System Interface](https://docs.python.org/3/tutorial/stdlib.html#operating-system-interface)
Modul [os](https://docs.python.org/3/library/os.html#module-os) menyediakan
lusinan fungsi untuk berinteraksi dengan sistem operasi:
```python
import os
print(os.getcwd()) # Return the current working directory
os.chdir('/home/ayam/Code/bigdata') # Change current working directory
print(os.system('mkdir today')) # Run the command mkdir in the system shell
```

kode diatas akan mengubah working directory kemudian akan membuat folder bernama "today"
```
/home/ayam/Code/bigdata
0
```

*Perhatian :* gunakan `import os` jangan `from os import *` karena akan membuat _shadowing_
[os.open()](https://docs.python.org/3/library/os.html#os.open) pada fungsi built-in
[open()](https://docs.python.org/3/library/functions.html#open) dan itu penggunaannya
akan jauh berbeda.

Fungsi built-in [dir()](https://docs.python.org/3/library/functions.html#dir) dan
[help()](https://docs.python.org/3/library/functions.html#help) berguna sekali untuk
bekerja dengan module yang besar seperti `os` :
```python
print(dir(os)) # <returns a list of all module functions>
print(help(os)) # <returns an extensive manual page created from the module's docstrings>
```

Untuk mengoperasikan tugas-tugas manajemen berkas, dapat menggunakan module
[shutil](https://docs.python.org/3/library/shutil.html#module-shutil) yang menyediakan
high-level interface dan mudah untuk digunakan, contoh :
```python
import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/today', 'also-today')
```

## 10.2. [File Wildcards](https://docs.python.org/3/tutorial/stdlib.html#file-wildcards)
Modul [glob](https://docs.python.org/3/library/glob.html#module-glob) menyediakan
fungsi untuk membuat daftar file dari pencarian direktori wildcard:

```python
import glob
print(glob.glob('*.py'))
```

## 10.3. [Command Line Arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
Untuk membaca argumen pada command-line yang dijalakan dapat menggunakan module [sys](https://docs.python.org/3/library/sys.html#module-sys)
```python
import sys
print(sys.argv)
```
jalankan kode diatas dengan cara :
```
$ python minggu-05/praktik/src/10_3-command-line-arguments.py satu dua tiga empat
```
maka akan menampilkan
```
['minggu-05/praktik/src/10_3-command-line-arguments.py', 'satu', 'dua', 'tiga', 'empat']
```
untuk pemrosesan command-line akan lebih powerfull dan fleksibel jika menggunakan module
[getopt](https://docs.python.org/3/library/getopt.html#module-getopt) yang disediakan oleh module
[argparse](https://docs.python.org/3/library/argparse.html#module-argparse).

## 10.4. [Error Output Redirection and Program Termination](https://docs.python.org/3/tutorial/stdlib.html#error-output-redirection-and-program-termination)
Modul [sys](https://docs.python.org/3/library/sys.html#module-sys) juga memiliki
atribut untuk _stdin_, _stdout,_ dan _stderr_. _stderr_ digunakan untuk menampilkan pesan
kesalahan.

```python
print(sys.stderr.write('Warning, log file not found starting a new one\n'))
```

jika dijalankan akan menampilkan
```
Warning, log file not found starting a new one
47
```

## 10.5. [String Pattern Matching](https://docs.python.org/3/tutorial/stdlib.html#string-pattern-matching)
Untuk pencocokan dan manipulasi yang kompleks terhadap string, regular expresion
(Regex) menawarkan solusi yang ringkas dan optimal:
```python
import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
```
akan menampilkan
```
['foot', 'fell', 'fastest']
cat in the hat
```

jika hanya pencocokan dengan string yang sederhana, method string lebih singkat dan mudah
```python
print('tea for too'.replace('too', 'two'))
"""Output
tea for two
"""
```

## 10.6. [Mathematics](https://docs.python.org/3/tutorial/stdlib.html#mathematics)
Modul [math](https://docs.python.org/3/library/math.html#module-math) memberikan
akses ke fungsi pustaka C yang mendasari untuk operasi floating point:
```python
import math
print(math.cos(math.pi / 4))
print(math.log(1024, 2))

"""Output
0.7071067811865476
10.0
"""
```

Modul [random](https://docs.python.org/3/library/random.html#module-random) menyediakan
alat untuk membuat pilihan secara acak:
```python
import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10)) # sampling without replacement
print(random.random()) # random float
print(random.randrange(6)) # random integer chosen from range(6)

"""Output
'apple'
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
0.17970987693706186
"""
```

Modul [statistics](https://docs.python.org/3/library/statistics.html#module-statistics)
untuk keperluan menghitung statistika dasar seperti: _mean_, _median_, _varians_, dll. Dari data numerik:

```python
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))

"""Output
1.6071428571428572
1.25
1.3720238095238095
"""
```
> Proyek [SciPy](https://scipy.org) mempunyai lebih banyak module untuk komputasi numerik.

## 10.7. [Internet Access](https://docs.python.org/3/tutorial/stdlib.html#internet-access)
Ada sejumlah modul untuk dapat mengakses internet dan memproses protokol internet.
Dua yang paling sederhana adalah [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request)
untuk mengambil data dari URL dan [smtplib](https://docs.python.org/3/library/smtplib.html#module-smtplib)
untuk mengirim email:
```python
from urllib.request import urlopen
with urlopen('https://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)


import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
server.quit()

"""Output
<BR>Oct. 04, 09:26:26 UTC
"""
```

> Contoh pengiriman email dengan smptplib, membutuhakn mail server dari localhost

## 10.8. [Dates and Times](https://docs.python.org/3/tutorial/stdlib.html#dates-and-times)
Modul [datetime](https://docs.python.org/3/library/datetime.html#module-datetime) menyediakan
kelas-kelas untuk memanipulasi tanggal dan waktu dengan cara yang sederhana maupun yang rumit.

```python
# dates are easily constructed and formatted
from datetime import date
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# dates support calendar arithmetic
birthday = date(1995, 12, 4)
age = now - birthday
print(age.days)

"""Output
2018-10-04
10-04-18. 04 Oct 2018 is a Thursday on the 04 day of October.
8340
"""
```

## 10.9. [Data Compression](https://docs.python.org/3/tutorial/stdlib.html#data-compression)
Beberapa modul yang mendukung untuk kompresi data diantaranya :
[zlib](https://docs.python.org/3/library/zlib.html#module-zlib), [gzip](https://docs.python.org/3/library/gzip.html#module-gzip),
[bz2](https://docs.python.org/3/library/bz2.html#module-bz2), [lzma](https://docs.python.org/3/library/lzma.html#module-lzma),
[zipfile](https://docs.python.org/3/library/zipfile.html#module-zipfile) dan [tarfile](https://docs.python.org/3/library/tarfile.html#module-tarfile).

```python
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(s))

"""Output
41
37
b'witch which has which witches wrist watch'
226805979
"""
```

## 10.10. [Performance Measurement](https://docs.python.org/3/tutorial/stdlib.html#performance-measurement)
Beberapa pengguna Python mengembangkan minat yang mendalam untuk mengetahui
kinerja relatif dari pendekatan yang berbeda untuk masalah yang sama. Python
menyediakan alat pengukuran yang menjawab pertanyaan-pertanyaan itu dengan segera.
Modul [timeit](https://docs.python.org/3/library/timeit.html#module-timeit)
dengan cepat menunjukkan keunggulan kinerja sederhana:

```python
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

"""Output
0.08620166899981996
0.046212379000280635
"""
```

## 10.11. [Quality Control](https://docs.python.org/3/tutorial/stdlib.html#quality-control)
## 10.12. [Batteries Included](https://docs.python.org/3/tutorial/stdlib.html#batteries-included)

<hr>

# 11. [Brief Tour of the Standard Library — Part II](https://docs.python.org/3/tutorial/stdlib2.html)

## 11.1. [Output Formatting](https://docs.python.org/3/tutorial/stdlib2.html#output-formatting)

## 11.2. [Templating](https://docs.python.org/3/tutorial/stdlib2.html#templating)

## 11.3. [Working with Binary Data Record Layouts](https://docs.python.org/3/tutorial/stdlib2.html#working-with-binary-data-record-layouts)

## 11.4. [Multi-threading](https://docs.python.org/3/tutorial/stdlib2.html#multi-threading)

## 11.5. [Logging](https://docs.python.org/3/tutorial/stdlib2.html#logging)

## 11.6. [Weak References](https://docs.python.org/3/tutorial/stdlib2.html#weak-references)

## 11.7. [Tools for Working with Lists](https://docs.python.org/3/tutorial/stdlib2.html#tools-for-working-with-lists)

## 11.8. [Decimal Floating Point Arithmetic](https://docs.python.org/3/tutorial/stdlib2.html#decimal-floating-point-arithmetic)

<hr />

# Memahami Lingkungan Kerja dan Paket di Python

# 12. [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)

## 12.1. [Introduction](https://docs.python.org/3/tutorial/venv.html#introduction)

## 12.2. [Creating Virtual Environments](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments)

## 12.3. [Managing Packages with pip](https://docs.python.org/3/tutorial/venv.html#managing-packages-with-pip)

**Selamat Belajar!**