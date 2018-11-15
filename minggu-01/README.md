# Langkah-langkah instalasi Python
Berikut ini adalah langkah-langkah instalasi Python 3.7 di Linux pada Ubuntu/Debian menggunakan APT (Package Manager)

1. Jalankan perintah berikut ini
```bash
sudo apt install -y python3.7 python3.7-dev
```

Setelah menjalankan perintah tersebut biasanya akan ditanyai password user, kemudian pada proses instalasi kurang lebih akan muncul seperti berikut :

```
bigdata on  master [!?] via bigdata took 9s
➜ sudo apt install -y python3.7 python3.7-dev
Alias tip: _ apt install -y python3.7 python3.7-dev
[sudo] password for ayam:
Reading package lists... Done
Building dependency tree
Reading state information... Done
python3.7 is already the newest version (3.7.0~b3-1).
The following additional packages will be installed:
  libpython3.7 libpython3.7-dev
The following NEW packages will be installed:
  libpython3.7 libpython3.7-dev python3.7-dev
0 upgraded, 3 newly installed, 0 to remove and 9 not upgraded.
Need to get 4.370 kB of archives.
After this operation, 22,3 MB of additional disk space will be used.
Get:1 http://kambing.ui.ac.id/ubuntu bionic/universe amd64 libpython3.7 amd64 3.7.0~b3-1 [1.507 kB]
Get:2 http://kambing.ui.ac.id/ubuntu bionic/universe amd64 libpython3.7-dev amd64 3.7.0~b3-1 [2.361 kB]
Get:3 http://kambing.ui.ac.id/ubuntu bionic/universe amd64 python3.7-dev amd64 3.7.0~b3-1 [501 kB]
Fetched 4.370 kB in 22s (198 kB/s)
Selecting previously unselected package libpython3.7:amd64.
(Reading database ... 265602 files and directories currently installed.)
Preparing to unpack .../libpython3.7_3.7.0~b3-1_amd64.deb ...
Unpacking libpython3.7:amd64 (3.7.0~b3-1) ...
Selecting previously unselected package libpython3.7-dev:amd64.
Preparing to unpack .../libpython3.7-dev_3.7.0~b3-1_amd64.deb ...
Unpacking libpython3.7-dev:amd64 (3.7.0~b3-1) ...
Selecting previously unselected package python3.7-dev.
Preparing to unpack .../python3.7-dev_3.7.0~b3-1_amd64.deb ...
Unpacking python3.7-dev (3.7.0~b3-1) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...
Setting up libpython3.7:amd64 (3.7.0~b3-1) ...
Setting up libpython3.7-dev:amd64 (3.7.0~b3-1) ...
Processing triggers for man-db (2.8.3-2) ...
Setting up python3.7-dev (3.7.0~b3-1) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...
```

2. Jalankan perintah berikut untuk memeriksa instalasi Python
```bash
python3.7
```

maka akan muncul prompt Python CLI
```bash
bigdata on  master [!?] via bigdata took 46s
➜ python3.7
Python 3.7.0b3 (default, Mar 30 2018, 04:35:22)
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hey there!")
Hey there!
>>>
```

**Python berhasil diinstal!**

# Memulai Belajar Python
RTFM (Read The F#ck Manual) di [dokumentasi resmi Python 3.7](https://docs.python.org/3/tutorial/index.html)

## 2. Using the Python Interpreter
### 2.1. [Invoking the Interpreter](https://docs.python.org/3/tutorial/interpreter.html#invoking-the-interpreter)
```bash
bigdata on  master [!] via bigdata took 7s
➜ which python3.7
/home/ayam/.virtualenvs/bigdata/bin/python3.7
```
> Python executable pada komputer saya berada di `/usr/bin/python3.7` namun saya
menggunakan virtualenv sehingga python yang tampil diatas adalah Python executale dari virtualenv

Berikut ini adalah Python shell yang sedang dijalankan
```bash
bigdata on  master via bigdata took 14s
➜ python3.7
Python 3.7.0b3 (default, Mar 30 2018, 04:35:22)
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Untuk keluar dari Python shell tekan CTRL+D atau mengeksekusi perintah `exit()`.

Cara lain untuk mengeksekusi perintah python pada command line adalah dengan
menambahkan opsi `-c` diikuti dengan syntax yang diapit dengan tanda petik
ganda (`"`) Contoh:
```bash
python -c "import uuid; print(uuid.uuid4().hex)"
```
Dengan menjalankan perintah diatas maka akan muncul kode unik semrawut yang
dibuat oleh modul `UUID`

#### 2.1.1. [Argument Passing](https://docs.python.org/3/tutorial/interpreter.html#argument-passing)
Menambahkan argumen pada command line

Buat file dengan nama `argument-passing.py` kemudian tuliskan berikut ini
```python
import sys
print(sys.argv[2])
```

Jalankan kode diatas menggunakan
```bash
python minggu-02/argument-passing.py "Saya dipanggil dari commandline"
```

maka akan muncul
```
Saya dipanggil dari commandline
```

#### 2.1.2. [Interactive Mode](https://docs.python.org/3/tutorial/interpreter.html#interactive-mode)
Menggunakan mode interaktif Python

```bash
bigdata on  master [!?] via bigdata took 46s
➜ python3.7
Python 3.7.0b3 (default, Mar 30 2018, 04:35:22)
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

`>>>` baris ini adalah perintah utama
`...` adalah baris _continuation_ atau perintah harus dilanjutkan diawali
dengan `tab` kemudian perintah

Contohnya sebagai berikut
```
>>> mahasiswa = True
>>> if mahasiswa:
...     print('You are mahasiswa!')
...
You are mahasiswa!
>>>
```

**Selamat Belajar!**
