import pandas as pd

df = pd.read_excel('writeExcel1.xls')
print("::: pd.read_excel() example::: \n")
print(df)

df.to_excel("writeExcel.xls")




df = pd.read_csv('readCSV.csv')
print('"::: pd.read_csv() example::: \n')
print(df)

df.to_csv('writeCSV.csv')

