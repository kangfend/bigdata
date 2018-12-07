import pandas as pd
import numpy as np


pd.options.display.max_columns = 50

employee = pd.read_csv('data/employee.csv')
depts = ['Houston Police Department-HPD', 'Houston Fire Department (HFD)']
select_columns = ['UNIQUE_ID', 'DEPARTMENT', 'GENDER', 'BASE_SALARY']
qs = "DEPARTMENT in @depts "          "and GENDER == 'Female' "          "and 80000 <= BASE_SALARY <= 120000"
        
emp_filtered = employee.query(qs)
print(emp_filtered[select_columns].head())

top10_depts = employee.DEPARTMENT.value_counts().index[:10].tolist()
qs = "DEPARTMENT not in @top10_depts and GENDER == 'Female'"
employee_filtered2 = employee.query(qs)
print(employee_filtered2[['DEPARTMENT', 'GENDER']].head())
