# Panduan Data Engineer (Bagian 2)
[Tulisan asli di Medium](https://medium.com/@rchang/a-beginners-guide-to-data-engineering-part-ii-47c4e7cbda71)

## Ikhtisar
Di panduan bagian ini agak rumit karena akan membahas detil secara teknis bagaimana
membangun _data pipelines_ yang baik menggunakan: Python, Airflow, dan SQL. Dibagian
ini akan membedah suatu anatomi dari Airflow Job, dan akan belajar menggunakan sensors,
operators, transformasi, loading datam, dan transfer untuk opersional konsep dari ekstraksi data.

## Pengetahuan Dasar Wajib
Yang sangat penting untuk diketahui sebagai landasan dasar:
1. Data Modeling
Adalah proses penataan dan pengorganisasian data, selain mendefinisikan
dan mengatur data, pemodelan data juga dapat menerapkan batasan
pada data yang ditempatkan di dalam struktur. Ketika membangun
_Online Analytical Processing System_ perancang memfokuskan kepada generasi wawasan
data dapat di-_query_ dan dikomputasikan dengan mudah.
2. Star Schema
Membuat skema tabel agar lebih sederhana, dan menghilangkan redundansi, sehingga
mengurangi penggunaan `JOIN` pada query disebut normalisasi data. Disamping normalisasi
data, ada cara yang lebih mudah untuk meng-query dari tabel-tabel utuh (wide table)
karena metriks dan dimensi sudah tergabung, dan ini akan mempersulit proses pipelines ETL karena
untuk kerja nya tidak modular
3. Data Partitioning
Salah satu teknik terbaik untuk meningkatkan performa query adalah dengan mempartisi data,
alih-alih menyimpan data di satu wadah yang sama, kita dapat membagi nya menjadi
beberapa bagian yang independent. Data dari suatu bagian yang sama akan sama partisinya,
yang artinya data akan mudah dan cepat diakses, dan ini akan sangat meningkatkan performa query.
4. Backfilling Historical Data
Keuntungan lain dari mempartisi data adalah memudahkan data backfilling, karena ketika ETL dibangung
artinya itu menghitung metriks dan dimensi ke "depan" bukan ke "belakang", sering kali kita akan
meninjau kembali pergerakan data historis. Dengan begitu, kita perlu mengkomputasi
metriks dan dimensi di masa lalu, proses ini disebut _data backfilling_.

## Anatomi Pipeline Airflow
Setelah mendapatkan pemahaman dasar dari konsep partisi data dan dimensi tabel, kemudian backfilling data
saatnya kita menggabungkan semuanya menjadi suatu ETL job dan menempatkannya di Airflow

### Mendefinisikan Directed Acylic Graph (DAG)

### Operators: Sensors, Operators, and Transfers

## ETL Best Practices
1. Partition Data Tables
2. Load Data Incrementally
3. Enforce Idempotency
4. Parameterize Workflow
5. Add Data Checks Early and Often
6. Build Useful Alerts & Monitoring System

## Kesimpulan
