import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('../Pandas_CoalPublic/coalpublic2013.xls', skiprows=3, index_col= 'Year')
print(df.head())
#print(df.dtypes)
#print(type(df))

#TO view multiple or desired columns only
#print(df[['MSHA ID', 'Mine Name', 'Mine Type']])
#print(df.columns)
#print(df.info())

#Find sum of a column
#total = df['Production (short tons)'].sum()
#print(total)


#insert a column in the sixth position
#df.insert(4, "column1", np.nan)
#print(df.head())

#summation of all column rows
#sum_row=df[['Production (short tons)', 'Labor Hours']].sum()
#df_sum=pd.DataFrame(sum_row)
#df_sum=df_sum.reindex(df.columns)
#print(df_sum)

#Create subtotal of Labor hours
#df_sub=df[["MSHA ID","Labor Hours"]].groupby('MSHA ID').sum()
#print(df_sub)

#requirement = df[df['MSHA ID']==100851]
#requirement.to_excel('requirement.xlsx')
#print(requirement)

#Finding conditional value with desired columns
#Hours_less_than_20000 = df[df['Labor Hours'] > 20000][['MSHA ID', 'Mine Name', 'Mine State']]
#Hours_less_than_20000.to_excel('Hours_less_than_20000.xlsx')
#print(Hours_less_than_20000)

#Find the details of "Mine Name" where name starts with 'P'
#P_MineName = df[df['Mine Name'].str.match('P.*')==True]
#P_MineName.to_excel('P_MineName.xlsx')
#print(df[df['Mine Name'].str.match('P.*')==True])

#FIND DATA with specific MSHA ID
#print(df[df["MSHA ID"].isin([102976,103380])])

#Finding data from Mine Name Column where Customers name is :
#customers = ["Shoal Creek Mine", "Piney Woods Preparation Plant"]
#Special_customers = df['Mine Name'].isin(customers)
#spc = df[Special_customers]
#spc.to_excel('spc.xlsx')

sorted_by_production = df.sort_values(['Production (short tons)'], ascending=False).head(10)
sorted_by_production['Production (short tons)'].head(10).plot(kind='barh')
plt.show()
