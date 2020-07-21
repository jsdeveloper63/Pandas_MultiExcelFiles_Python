import pandas as pd
import numpy as np
from datetime import date

df = pd.read_excel('../Pandas_CoalPublic/employee.xlsx', date_format='%m/%d/%Y')

print(df)
#print(df.dtypes)

#find a list of employees where hire_date> 01-01-07.
#Hiring_Data = df[df['hire_date'] > '01-01-2007']
#Hiring_Data.to_excel('Hiring_Data.xlsx')
#print(Hiring_Data)

#sort the records by the hire_date column.
#result = df.sort_values('hire_date')
#print(result)

# find a list of employees where hire_date between two specific month and year.
#Specific_mon_yr = df[(df['hire_date'] >='Jan-2005') & (df['hire_date'] <= 'Dec-2006')]
#Specific_mon_yr.to_excel('Specific_mon_yr.xlsx')
#print(Specific_mon_yr)

#find a list of employees of a specified year
#df2 = df.set_index(['hire_date'])
#result = df2["2005"]
#print(result)

#convert the data to use the hire_date as the index
#result = df.set_index(['hire_date'])
#print(result)

#sort based on multiple given columns
#result = df.sort_values(by=['last_name','first_name'],ascending=[0,0])
#print(result)
