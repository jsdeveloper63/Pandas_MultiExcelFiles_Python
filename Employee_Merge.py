import numpy as np
import pandas as pd
from openpyxl.workbook import Workbook

df1 = pd.read_excel('../Pandas_CoalPublic/employee.xlsx', index_col = 'emp_id')
df2 = pd.read_excel('../Pandas_CoalPublic/employee_sheet2.xlsx',index_col = 'emp_id')
df3 = pd.read_excel('../Pandas_CoalPublic/employee_sheet3.xlsx', index_col = 'emp_id')

df = pd.concat([df1, df2, df3])
print(df)

#files = ('../Pandas_CoalPublic/employee.xlsx', '../Pandas_CoalPublic/employee_sheet2.xlsx', '../Pandas_CoalPublic/employee_sheet3.xlsx')
#merger = pd.DataFrame()

#for file in files:
#    df = pd.read_excel(file, index_col='emp_id')
#    merger = merger.append(df)


#merger.to_excel('merger.xlsx')
#print(merger)
