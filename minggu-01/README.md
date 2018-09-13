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

Python berhasil diinstal!
