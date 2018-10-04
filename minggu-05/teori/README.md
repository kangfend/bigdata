# Panduan Data Engineer (Bagian 3)
[Tulisan asli di Medium](https://medium.com/@rchang/a-beginners-guide-to-data-engineering-the-series-finale-2cc92ff14b0)

## Ikhtisar
Di bagian ketiga ini (terakhir) akan dibahas tentang konsep dari framework data engineering
dan membedah pola desain untuk membangung framework tersebut, kemudian akan fokus ke
beberapa contoh spesifik yang sering digunakan oleh AriBnb, yang bertujuan agar pembaca
dapat mengembangkan sendiri untuk abstraksi framework.

## Skenario Umum
1. data modeling and schema design
2. identify relevant fact and dimension tables
3. joining the tables to create a final denormalized table
4. backfill all the historical data

Meski melakukan tahap-tahap diatas sangat bermanfaat, namun melakukan pekerjaan
seperti itu dirasa _repetitive_ (berulang-ulang) dan nyatanya pekerjaan ini
sudah dilakukan sehari-hari oleh data scientist. Sedangkan, alur kerja ini dapat
diotomasikan (setidaknya sebagian).

## From Pipelines To Frameworks
Seperti yang telah dibahas pada [bagian 2](../minggu-04/teori/README.md),
DAG milik Airflow bisa jadi sangat kompleks, terkadang, komputasi data bahkan
mengikuti aliran kontrol seperti logika. Sebagai contohnya :
1. Untuk membuat percabangan aliran data dapat menggunakan
[BranchPythonOperator](https://airflow.incubator.apache.org/concepts.html#branching)
2. Jika alur kerja dapat berlanjut hanya jika suatu kondisi terpenuhi dapat menggunakan
[ShortCircuitOpeartor](https://github.com/apache/incubator-airflow/blob/master/airflow/example_dags/example_short_circuit_operator.py#L34-L35)

Operator-operator tersebut, dikombinasikan dengan prinsip **configuration as code**
agar ETL Airflow lebih serba guna dan fleksibel.

Sejauh ini, pembahasan terbatas pada desain _single_, _standalone_, _pipeline_, namun
kita dapat menerapkan prinsip yang sama untuk pembuatan _pipeline generation_ adalah
sebuah cara untuk menghasilkan GAD secara terprogram dan secara dinamis dengan cepat.
Pada dasarnya, inilah yang dikerjakan oleh *framework data engineering* (menghasilkan
instansiasi yang berbeda dari DAG milik Airflow dan mengotomatisasi alur kerja data), sebagaimana
yang dikatakan oleh Maxime (pembuat Airflow) :

> To build workflows dynamically from code ... A very simple example would
be an Airflow script that reads a YAML config file with a list of table names,
and creates a little workflow for each table, that may do things like loading
the table into a target database, perhaps apply rules from the config file
around sampling, data retention, anonymization … Now you have this
abstraction … you can create new chunks of workflows without doing much work.
It turns out there are tons of use cases for this type of approach.

Tools tersebut sangatlah penting bagi data scientist untuk meningkatkan data
_value chain<sup>[[1]](#value-chain)</sup>_ lebih cepat.

Implikasi dari kerangka kerja ini sangatlah dalam karena secara drastis
meningkatkan cara kerja data scientist. Ini adalah teknologi yang memungkinkan
para data scientist untuk memberikan _value at scale_.

## Pola Desain untuk Framework Data Engineering
![Pola Desain untuk Framework Data Engineering](https://cdn-images-1.medium.com/max/1000/1*iDfX-IBcwGu8R0PbiXw-Bg.png)

### 1. Incremental Computation Framework

### 2. Backfill Framework

### 3. Global Metrics Framework

### 4. Experimentation Reporting Framework

## Kesimpulan

## Footnote
### _value chain_
