import pandas as pd
import numpy as np


pd.options.display.max_columns = 50

employee = pd.read_csv('data/employee.csv')
print(employee.DEPARTMENT.value_counts().head())
print(employee.GENDER.value_counts())
print(employee.BASE_SALARY.describe().astype(int))

depts = ['Houston Police Department-HPD', 'Houston Fire Department (HFD)']
criteria_dept = employee.DEPARTMENT.isin(depts)
criteria_gender = employee.GENDER == 'Female'
criteria_sal = (employee.BASE_SALARY >= 80000) & \
               (employee.BASE_SALARY <= 120000)

criteria_final = criteria_dept & criteria_gender & criteria_sal
select_columns = ['UNIQUE_ID', 'DEPARTMENT', 'GENDER', 'BASE_SALARY']
print(employee.loc[criteria_final, select_columns].head())

criteria_sal = employee.BASE_SALARY.between(80000, 120000)
top_5_depts = employee.DEPARTMENT.value_counts().index[:5]
criteria = ~employee.DEPARTMENT.isin(top_5_depts)
print(employee[criteria].head())
