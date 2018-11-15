# Jupyter in a Nutshell!

## Apa itu Jupyter?
Jupyter adalah ekosistem atau lingkungan untuk bekerja dengan kode, dokumentasi,
dan lain-lain, Jupyter berjalan diatas Kernel Protocol IPython secara default namun dapat
menggunakan kernel lain seperti IRKernel dan IJulia dan IPython menggunakan Javascript sebagai
front-end nya, selain itu Jupyter juga disebut sebagai Interactive Computing sama seperti
IPython karena IPython lah yang mendasari pembuatan Jupyter ini.

## Apa fungsi Jupyter?
Jupyter berfungsi sebagai _interactive computing_ yang mana memudahkan kita menulis kode secara interaktif dengan penulisan kode yang nyamana, Jupyter dapat digunakan :
1. Menulis Kode
2. Menulis Dokumentasi
3. Menulis persamaan/formula matematika
4. Menjalankan Bash Command
5. Dll

## Instalasi Jupyter
Menginstal Jupyter dapat dilakukan dengan dua cara yaitu, instalasi menggunakan PIP atau Package Manager
bawaan distribusi sistem yang dipakai, berikut ini adalah cara instalasi dari kedua pilihan tersebut :
1. Instalasi menggunakan Pip
Instalasi menggunakan pip sama seperti instal pustaka lain, berikut ini perintahnya:
```bash
pip install jupyter-notebook
```
2. Instalasi menggunakan Package Manager Distro
Instalasi dengan cara ini menurut saya paling sip karena, biarkan sistem yang mengatur, caranya jalankan perintah berikut
```bash
sudo pacman -S jupyter-notebook
```

> Saya menggunakan Arch Linux, jika anda menggunakan linux lain silakan sesuaikan dengan package manager yang dimiliki seperti, APT (Debian/Ubuntu) atau Yum (Fedora/Centos).

## Menggunakan Jupyter
Menggunakan Jupyter pun sangat mudah hanya perlu menjalankan perintah berikut:
```bash
jupyter notebook
```

<hr/>

# Jupyter Notebook Quickstart
## Configuration
Jupyter memilik berkas konfigurasi yang dapat kita manfaatkan agar Jupyter berjalan dengan sesuai selera kita,
contohnya adalah kita mengubah direktori kerja (working directory) notebook yang mana dapat mengubah
direktori secara default saat notebook dibuka, sebelum mengubah direktori kerja kita perlu men-generate
konfigurasi jupyter terlebih dahulu dengan cara 

```bash
jupyter-notebook --generate-config
```

dengan perintah tersebut maka konfigurasi jupyter akan dibuatkan didirektori `$HOME/.jupyter/jupyter_notebook_config.py` berkas inilah yang digunakan untuk menyimpan konfigurasi-konfigurasi yang digunakan oleh jupyter.

<hr />
