# Masih Belajar Pandas

## Bab 4 - Selecting Subset of Data
### Selecting Series Data
```python
import pandas as pd
import numpy as np


college = pd.read_csv('data/college.csv', index_col='INSTNM')
city = college['CITY']
print(city.head())
print(city.iloc[3])
print(city.iloc[[10,20,30]])
print(city.iloc[4:50:10])
print(city.loc['Heritage Christian University'])

np.random.seed(1)
labels = list(np.random.choice(city.index, 4))
print(labels)
print(city.loc[labels])
print(city.loc['Alabama State University':'Reid State Technical College':10])
print(city['Alabama State University':'Reid State Technical College':10])
print(city.iloc[[3]])
print(city.loc['Reid State Technical College':'Alabama State University':10])
print(city.loc['Reid State Technical College':'Alabama State University':-10])
```
#### Output
```
INSTNM
Alabama A & M University                   Normal
University of Alabama at Birmingham    Birmingham
Amridge University                     Montgomery
University of Alabama in Huntsville    Huntsville
Alabama State University               Montgomery
Name: CITY, dtype: object

Huntsville
INSTNM
Birmingham Southern College                            Birmingham
George C Wallace State Community College-Hanceville    Hanceville
Judson College                                             Marion
Name: CITY, dtype: object

INSTNM
Alabama State University              Montgomery
Enterprise State Community College    Enterprise
Heritage Christian University           Florence
Marion Military Institute                 Marion
Reid State Technical College           Evergreen
Name: CITY, dtype: object

Florence
['Northwest HVAC/R Training Center', 'California State University-Dominguez Hills', 'Lower Columbia College', 'Southwest Acupuncture College-Boulder']
INSTNM
Northwest HVAC/R Training Center                Spokane
California State University-Dominguez Hills      Carson
Lower Columbia College                         Longview
Southwest Acupuncture College-Boulder           Boulder
Name: CITY, dtype: object

INSTNM
Alabama State University              Montgomery
Enterprise State Community College    Enterprise
Heritage Christian University           Florence
Marion Military Institute                 Marion
Reid State Technical College           Evergreen
Name: CITY, dtype: object

INSTNM
Alabama State University              Montgomery
Enterprise State Community College    Enterprise
Heritage Christian University           Florence
Marion Military Institute                 Marion
Reid State Technical College           Evergreen
Name: CITY, dtype: object

INSTNM
University of Alabama in Huntsville    Huntsville
Name: CITY, dtype: object

Series([], Name: CITY, dtype: object)
INSTNM
Reid State Technical College           Evergreen
Marion Military Institute                 Marion
Heritage Christian University           Florence
Enterprise State Community College    Enterprise
Alabama State University              Montgomery
Name: CITY, dtype: object
```

### Selecting DataFrame Rows
```python
import pandas as pd
import numpy as np


college = pd.read_csv('data/college.csv', index_col='INSTNM')
print(college.head())

pd.options.display.max_rows = 6
print(college.iloc[60])
print(college.loc['University of Alaska Anchorage'])
print(college.iloc[[60, 99, 3]])

labels = ['University of Alaska Anchorage',
          'International Academy of Hair Design',
          'University of Alabama in Huntsville']
print(college.loc[labels])
print(college.iloc[99:102])

start = 'International Academy of Hair Design'
stop = 'Mesa Community College'
print(college.loc[start:stop])
print(college.iloc[[60, 99, 3]].index.tolist())
```

#### Output
```
                                           CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV  MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                        ...
Alabama A & M University                 Normal     AL   1.0      0.0         ...            0.8284   0.1049            30300               33888
University of Alabama at Birmingham  Birmingham     AL   0.0      0.0         ...            0.5214   0.2422            39700             21941.5
Amridge University                   Montgomery     AL   0.0      0.0         ...            0.7795   0.8540            40100               23370
University of Alabama in Huntsville  Huntsville     AL   0.0      0.0         ...            0.4596   0.2640            45500               24097
Alabama State University             Montgomery     AL   1.0      0.0         ...            0.7554   0.1270            26600             33118.5
[5 rows x 26 columns]

CITY                  Anchorage
STABBR                       AK
HBCU                          0
                        ...
UG25ABV                  0.4386
MD_EARN_WNE_P10           42500
GRAD_DEBT_MDN_SUPP      19449.5
Name: University of Alaska Anchorage, Length: 26, dtype: object

CITY                  Anchorage
STABBR                       AK
HBCU                          0
                        ...
UG25ABV                  0.4386
MD_EARN_WNE_P10           42500
GRAD_DEBT_MDN_SUPP      19449.5
Name: University of Alaska Anchorage, Length: 26, dtype: object

                                            CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV  MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                         ...
University of Alaska Anchorage         Anchorage     AK   0.0      0.0         ...            0.2647   0.4386            42500             19449.5
International Academy of Hair Design       Tempe     AZ   0.0      0.0         ...            0.7346   0.3905            22200               10556
University of Alabama in Huntsville   Huntsville     AL   0.0      0.0         ...            0.4596   0.2640            45500               24097
[3 rows x 26 columns]

                                            CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV  MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                         ...
University of Alaska Anchorage         Anchorage     AK   0.0      0.0         ...            0.2647   0.4386            42500             19449.5
International Academy of Hair Design       Tempe     AZ   0.0      0.0         ...            0.7346   0.3905            22200               10556
University of Alabama in Huntsville   Huntsville     AL   0.0      0.0         ...            0.4596   0.2640            45500               24097
[3 rows x 26 columns]

                                         CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV  MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                      ...
International Academy of Hair Design    Tempe     AZ   0.0      0.0         ...            0.7346   0.3905            22200               10556
GateWay Community College             Phoenix     AZ   0.0      0.0         ...            0.2189   0.5832            29800                7283
Mesa Community College                   Mesa     AZ   0.0      0.0         ...            0.2207   0.4010            35200                8000
[3 rows x 26 columns]

                                         CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV  MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                      ...
International Academy of Hair Design    Tempe     AZ   0.0      0.0         ...            0.7346   0.3905            22200               10556
GateWay Community College             Phoenix     AZ   0.0      0.0         ...            0.2189   0.5832            29800                7283
Mesa Community College                   Mesa     AZ   0.0      0.0         ...            0.2207   0.4010            35200                8000
[3 rows x 26 columns]

['University of Alaska Anchorage', 'International Academy of Hair Design', 'University of Alabama in Huntsville']
```

### Selecting DataFrame rows and columns simultaneously
```python
import pandas as pd
import numpy as np


college = pd.read_csv('data/college.csv', index_col='INSTNM')
print(college.iloc[:3, :4])
print(college.loc[:'Amridge University', :'MENONLY'])
print(college.iloc[:, [4,6]].head())
print(college.loc[:, ['WOMENONLY', 'SATVRMID']])
print(college.iloc[[100, 200], [7, 15]])

rows = ['GateWay Community College', 'American Baptist Seminary of the West']
columns = ['SATMTMID', 'UGDS_NHPI']
print(college.loc[rows, columns])
print(college.iloc[5, -4])
print(college.loc['The University of Alabama', 'PCTFLOAN'])
print(college.iloc[90:80:-2, 5])

start = 'Empire Beauty School-Flagstaff'
stop = 'Arizona State University-Tempe'
print(college.loc[start:stop:-2, 'RELAFFIL'])

```

#### Output
```
                                           CITY STABBR  HBCU  MENONLY
INSTNM
Alabama A & M University                 Normal     AL   1.0      0.0
University of Alabama at Birmingham  Birmingham     AL   0.0      0.0
Amridge University                   Montgomery     AL   0.0      0.0
                                           CITY STABBR  HBCU  MENONLY

INSTNM
Alabama A & M University                 Normal     AL   1.0      0.0
University of Alabama at Birmingham  Birmingham     AL   0.0      0.0
Amridge University                   Montgomery     AL   0.0      0.0
                                     WOMENONLY  SATVRMID

INSTNM
Alabama A & M University                   0.0     424.0
University of Alabama at Birmingham        0.0     570.0
Amridge University                         0.0       NaN
University of Alabama in Huntsville        0.0     595.0
Alabama State University                   0.0     425.0

                                                    WOMENONLY  SATVRMID
INSTNM
Alabama A & M University                                  0.0     424.0
University of Alabama at Birmingham                       0.0     570.0
Amridge University                                        0.0       NaN
University of Alabama in Huntsville                       0.0     595.0
Alabama State University                                  0.0     425.0
The University of Alabama                                 0.0     555.0
Central Alabama Community College                         0.0       NaN
Athens State University                                   0.0       NaN
Auburn University at Montgomery                           0.0     486.0
Auburn University                                         0.0     575.0
Birmingham Southern College                               0.0     560.0
Chattahoochee Valley Community College                    0.0       NaN
Concordia College Alabama                                 0.0     420.0
South University-Montgomery                               0.0       NaN
Enterprise State Community College                        0.0       NaN
James H Faulkner State Community College                  0.0       NaN
Faulkner University                                       0.0       NaN
Gadsden State Community College                           0.0       NaN
New Beginning College of Cosmetology                      0.0       NaN
George C Wallace State Community College-Dothan           0.0       NaN
George C Wallace State Community College-Hancev...        0.0       NaN
George C Wallace State Community College-Selma            0.0       NaN
Herzing University-Birmingham                             0.0       NaN
Huntingdon College                                        0.0     510.0
Heritage Christian University                             0.0       NaN
J F Drake State Community and Technical College           0.0       NaN
Jacksonville State University                             0.0     495.0
Jefferson Davis Community College                         0.0       NaN
Jefferson State Community College                         0.0       NaN
John C Calhoun State Community College                    0.0       NaN
...                                                       ...       ...
Strayer University-Lawrenceville                          NaN       NaN
Strayer University-Piscataway                             NaN       NaN
Utah County Campus                                        NaN       NaN
L'esprit Academy - Royal Oak                              NaN       NaN
National Career Institute - Jersey City Branch            NaN       NaN
Strayer University-Cobb Campus                            NaN       NaN
Strayer University-Morrow Campus                          NaN       NaN
Strayer University-Roswell Campus                         NaN       NaN
Strayer University-Douglasville Campus                    NaN       NaN
Strayer University-Lithonia Campus                        NaN       NaN
Strayer University-Savannah Campus                        NaN       NaN
Strayer University-Augusta Campus                         NaN       NaN
Strayer University-Columbus                               NaN       NaN
Strayer University-Columbia Campus                        NaN       NaN
Strayer University-Charleston Campus                      NaN       NaN
Strayer University-Irving                                 NaN       NaN
Strayer University-Katy                                   NaN       NaN
Strayer University-Northwest Houston                      NaN       NaN
Strayer University-Plano                                  NaN       NaN
Strayer University-Cedar Hill                             NaN       NaN
Strayer University-North Dallas                           NaN       NaN
Strayer University-San Antonio                            NaN       NaN
Strayer University-Stafford                               NaN       NaN
WestMed College - Merced                                  NaN       NaN
Vantage College                                           NaN       NaN
SAE Institute of Technology  San Francisco                NaN       NaN
Rasmussen College - Overland Park                         NaN       NaN
National Personal Training Institute of Cleveland         NaN       NaN
Bay Area Medical Academy - San Jose Satellite L...        NaN       NaN
Excel Learning Center-San Antonio South                   NaN       NaN
[7535 rows x 2 columns]

                                       SATMTMID  UGDS_NHPI
INSTNM
GateWay Community College                   NaN     0.0029
American Baptist Seminary of the West       NaN        NaN

                                       SATMTMID  UGDS_NHPI
INSTNM
GateWay Community College                   NaN     0.0029
American Baptist Seminary of the West       NaN        NaN
0.401
0.401

INSTNM
Empire Beauty School-Flagstaff     0
Charles of Italy Beauty College    0
Central Arizona College            0
University of Arizona              0
Arizona State University-Tempe     0
Name: RELAFFIL, dtype: int64

INSTNM
Empire Beauty School-Flagstaff     0
Charles of Italy Beauty College    0
Central Arizona College            0
University of Arizona              0
Arizona State University-Tempe     0
Name: RELAFFIL, dtype: int64
```

### Selecting data with both integers and labels
```python
import pandas as pd
import numpy as np


college = pd.read_csv('data/college.csv', index_col='INSTNM')
col_start = college.columns.get_loc('UGDS_WHITE')
col_end = college.columns.get_loc('UGDS_UNKN') + 1
print(col_start, col_end)
print(college.iloc[:5, col_start:col_end])

row_start = college.index[10]
row_end = college.index[15]
print(college.loc[row_start:row_end, 'UGDS_WHITE':'UGDS_UNKN'])
```

#### Output
```
(10, 19)

                                     UGDS_WHITE  UGDS_BLACK  UGDS_HISP  UGDS_ASIAN  UGDS_AIAN  UGDS_NHPI  UGDS_2MOR  UGDS_NRA  UGDS_UNKN
INSTNM
Alabama A & M University                 0.0333      0.9353     0.0055      0.0019     0.0024     0.0019     0.0000    0.0059     0.0138
University of Alabama at Birmingham      0.5922      0.2600     0.0283      0.0518     0.0022     0.0007     0.0368    0.0179     0.0100
Amridge University                       0.2990      0.4192     0.0069      0.0034     0.0000     0.0000     0.0000    0.0000     0.2715
University of Alabama in Huntsville      0.6988      0.1255     0.0382      0.0376     0.0143     0.0002     0.0172    0.0332     0.0350
Alabama State University                 0.0158      0.9208     0.0121      0.0019     0.0010     0.0006     0.0098    0.0243     0.0137

                                          UGDS_WHITE  UGDS_BLACK  UGDS_HISP  UGDS_ASIAN  UGDS_AIAN  UGDS_NHPI  UGDS_2MOR  UGDS_NRA  UGDS_UNKN
INSTNM
Birmingham Southern College                   0.7983      0.1102     0.0195      0.0517     0.0102     0.0000     0.0051    0.0000     0.0051
Chattahoochee Valley Community College        0.4661      0.4372     0.0492      0.0127     0.0023     0.0035     0.0151    0.0000     0.0139
Concordia College Alabama                     0.0280      0.8758     0.0373      0.0093     0.0000     0.0000     0.0031    0.0466     0.0000
South University-Montgomery                   0.3046      0.6054     0.0153      0.0153     0.0153     0.0096     0.0000    0.0019     0.0326
Enterprise State Community College            0.6408      0.2435     0.0509      0.0202     0.0081     0.0029     0.0254    0.0012     0.0069
James H Faulkner State Community College      0.6979      0.2259     0.0320      0.0084     0.0177     0.0014     0.0152    0.0007     0.0009
```

### Speeding up scalar selection
```python
import pandas as pd
import numpy as np
from IPython import InteractiveShell

inter = InteractiveShell()

college = pd.read_csv('data/college.csv', index_col='INSTNM')
cn = 'Texas A & M University-College Station'
print(college.loc[cn, 'UGDS_WHITE'])
print(college.at[cn, 'UGDS_WHITE'])
print(inter.get_ipython().run_line_magic('timeit', "college.loc[cn, 'UGDS_WHITE']"))
print(inter.get_ipython().run_line_magic('timeit', "college.at[cn, 'UGDS_WHITE']"))

row_num = college.index.get_loc(cn)
col_num = college.columns.get_loc('UGDS_WHITE')
print(row_num, col_num)

print(inter.get_ipython().run_line_magic('timeit', 'college.iloc[row_num, col_num]'))
print(inter.get_ipython().run_line_magic('timeit', 'college.iat[row_num, col_num]'))
print(inter.get_ipython().run_line_magic('timeit', 'college.iloc[5, col_num]'))
print(inter.get_ipython().run_line_magic('timeit', 'college.iat[5, col_num]'))

state = college['STABBR']
print(state.iat[1000])
print(state.at['Stanford University'])
```

#### Output
```
0.6609999999999999
0.6609999999999999
42.9 µs ± 9.91 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
None
21.1 µs ± 1.61 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
None
3765 10
45.4 µs ± 8.26 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
None
22.2 µs ± 1.06 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
None
46.9 µs ± 10 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
None
31.6 µs ± 6.83 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
None
IL
CA
```

### Slicing rows lazily
```python
import pandas as pd
import numpy as np


college = pd.read_csv('data/college.csv', index_col='INSTNM')
city = college['CITY']

print(college[10:20:2])
print(city[10:20:2])
print(college.index[4001])

start = 'Mesa Community College'
stop = 'Spokane Community College'
print(college[start:stop:1500])
print(city[start:stop:1500])
# print(college[:10, ['CITY', 'STABBR']])

first_ten_instnm = college.index[:10]
print(college.loc[first_ten_instnm, ['CITY', 'STABBR']])
```

#### Output
```
                                             CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV  MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                          ...
Birmingham Southern College            Birmingham     AL   0.0      0.0         ...            0.4809   0.0152            44200               27000
Concordia College Alabama                   Selma     AL   1.0      0.0         ...            0.9333   0.2367            19900   PrivacySuppressed
Enterprise State Community College     Enterprise     AL   0.0      0.0         ...            0.2263   0.3399            24600                8273
Faulkner University                    Montgomery     AL   0.0      0.0         ...            0.7253   0.4589            37200               22000
New Beginning College of Cosmetology  Albertville     AL   0.0      0.0         ...            0.8553   0.3933              NaN                5500
[5 rows x 26 columns]

INSTNM
Birmingham Southern College              Birmingham
Concordia College Alabama                     Selma
Enterprise State Community College       Enterprise
Faulkner University                      Montgomery
New Beginning College of Cosmetology    Albertville
Name: CITY, dtype: object

Spokane Community College

                                                CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV  MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                             ...
Mesa Community College                          Mesa     AZ   0.0      0.0         ...            0.2207   0.4010            35200                8000
Hair Academy Inc-New Carrollton       New Carrollton     MD   0.0      0.0         ...            1.0000   0.5882            15200                9666
National College of Natural Medicine        Portland     OR   0.0      0.0         ...               NaN      NaN              NaN   PrivacySuppressed
[3 rows x 26 columns]

INSTNM
Mesa Community College                            Mesa
Hair Academy Inc-New Carrollton         New Carrollton
National College of Natural Medicine          Portland
Name: CITY, dtype: object

                                               CITY STABBR
INSTNM
Alabama A & M University                     Normal     AL
University of Alabama at Birmingham      Birmingham     AL
Amridge University                       Montgomery     AL
University of Alabama in Huntsville      Huntsville     AL
Alabama State University                 Montgomery     AL
The University of Alabama                Tuscaloosa     AL
Central Alabama Community College    Alexander City     AL
Athens State University                      Athens     AL
Auburn University at Montgomery          Montgomery     AL
Auburn University                            Auburn     AL
```

### Slicing lexicographically
```python
import pandas as pd
import numpy as np


college = pd.read_csv('data/college.csv', index_col='INSTNM')
# print(college.loc['Sp':'Su'])
college = college.sort_index()
print(college.head())

pd.options.display.max_rows = 6
print(college.loc['Sp':'Su'])

college = college.sort_index(ascending=False)
print(college.index.is_monotonic_decreasing)
print(college.loc['E':'B'])
print(college.loc['E':'B'])
```

#### Output
```
                                                           CITY STABBR  HBCU         ...          UG25ABV    MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                               ...
A & W Healthcare Educators                          New Orleans     LA   0.0         ...           0.6667                NaN             19022.5
A T Still University of Health Sciences              Kirksville     MO   0.0         ...              NaN             219800   PrivacySuppressed
ABC Beauty Academy                                      Garland     TX   0.0         ...           0.8286                NaN   PrivacySuppressed
ABC Beauty College Inc                              Arkadelphia     AR   0.0         ...           0.4688  PrivacySuppressed               16500
AI Miami International University of Art and De...        Miami     FL   0.0         ...           0.3262              29900               31000
[5 rows x 26 columns]

                                                 CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV    MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                              ...
Spa Tech Institute-Ipswich                    Ipswich     MA   0.0      0.0         ...            0.3906   0.7907              21500                6333
Spa Tech Institute-Plymouth                  Plymouth     MA   0.0      0.0         ...            0.4266   0.6250              21500                6333
Spa Tech Institute-Westboro                  Westboro     MA   0.0      0.0         ...            0.4545   0.6882              21500                6333
...                                               ...    ...   ...      ...         ...               ...      ...                ...                 ...
Stylemaster College of Hair Design           Longview     WA   0.0      0.0         ...            0.7024   0.4510              17000               13320
Styles and Profiles Beauty College             Selmer     TN   0.0      0.0         ...            0.7955   0.2400  PrivacySuppressed   PrivacySuppressed
Styletrends Barber and Hairstyling Academy  Rock Hill     SC   0.0      0.0         ...            1.0000   0.3529  PrivacySuppressed              9495.5
[201 rows x 26 columns]

True

                                                  CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV    MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                               ...
Dyersburg State Community College            Dyersburg     TN   0.0      0.0         ...            0.2493   0.3097              26800                7475
Dutchess Community College                Poughkeepsie     NY   0.0      0.0         ...            0.1936   0.1806              32500               10250
Dutchess BOCES-Practical Nursing Program  Poughkeepsie     NY   0.0      0.0         ...            0.6275   0.5430              36500                9500
...                                                ...    ...   ...      ...         ...               ...      ...                ...                 ...
BJ's Beauty & Barber College                    Auburn     WA   0.0      0.0         ...            0.6154   0.2917                NaN   PrivacySuppressed
BIR Training Center                            Chicago     IL   0.0      0.0         ...            0.6998   0.6741  PrivacySuppressed               15394
B M Spurr School of Practical Nursing        Glen Dale     WV   0.0      0.0         ...            0.0000   0.4444  PrivacySuppressed   PrivacySuppressed
[1411 rows x 26 columns]

                                                  CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV    MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                               ...
Dyersburg State Community College            Dyersburg     TN   0.0      0.0         ...            0.2493   0.3097              26800                7475
Dutchess Community College                Poughkeepsie     NY   0.0      0.0         ...            0.1936   0.1806              32500               10250
Dutchess BOCES-Practical Nursing Program  Poughkeepsie     NY   0.0      0.0         ...            0.6275   0.5430              36500                9500
...                                                ...    ...   ...      ...         ...               ...      ...                ...                 ...
BJ's Beauty & Barber College                    Auburn     WA   0.0      0.0         ...            0.6154   0.2917                NaN   PrivacySuppressed
BIR Training Center                            Chicago     IL   0.0      0.0         ...            0.6998   0.6741  PrivacySuppressed               15394
B M Spurr School of Practical Nursing        Glen Dale     WV   0.0      0.0         ...            0.0000   0.4444  PrivacySuppressed   PrivacySuppressed
[1411 rows x 26 columns]
```

## Bab 5 - Boolean Indexing
### Calculating boolean statistics
```python
```

#### Output
```
```

### Constructing multiple boolean conditions
```python
```

#### Output
```
```

### Filtering with boolean indexing
```python
```

#### Output
```
```

### Replicating boolean indexing with index selection
```python
```

#### Output
```
```

### Selecting with unique and sorted indexes
```python
```

#### Output
```
```

### Gaining perspective on stock prices
```python
```

#### Output
```
```

### Translating SQL WHERE clauses
```python
```

#### Output
```
```

### Determining the normality of stock market returns
```python
```

#### Output
```
```

### Improving readability of boolean indexing with the query method
```python
```

#### Output
```
```

### Preserving Series with the where method
```python
```

#### Output
```
```

### Masking DataFrame rows
```python
```

#### Output
```
```

### Selecting with booleans, integer location, and labels
```python
```

#### Output
```
```

## Bab 6 - Index Alignment
### Examining the Index object
```python
```

#### Output
```
```

### Producing Cartesian products
```python
```

#### Output
```
```

### Exploding indexes
```python
```

#### Output
```
```

### Filling values with unequal indexes
```python
```

#### Output
```
```

### Appending columns from different DataFrames
```python
```

#### Output
```
```

### Highlighting the maximum value from each column
```python
```

#### Output
```
```

### Replicating idxmax with method chaining
```python
```

#### Output
```
```

### Finding the most common maximum
```python
```

#### Output
```
```


## Bab 7 - Grouping for Aggregation, Filtration and Transformation
### Defining an aggregation
```python
```

#### Output
```
```

### Grouping and aggregating with multiple columns and functions
```python
```

#### Output
```
```

### Removing the MultiIndex after grouping
```python
```

#### Output
```
```

### Customizing an aggregation function
```python
```

#### Output
```
```

### Customizing aggregating functions with *args and **kwargs
```python
```

#### Output
```
```

### Examining the groupby object
```python
```

#### Output
```
```

### Filtering for states with a minority majority
```python
```

#### Output
```
```

### Transforming through a weight loss bet
```python
```

#### Output
```
```

### Calculating weighted mean SAT scores per state with apply
```python
```

#### Output
```
```

### Grouping by continuous variables
```python
```

#### Output
```
```

### Counting the total number of flights between cities
```python
```

#### Output
```
```

### Finding the longest streak of on-time flights
```python
```

#### Output
```
```
