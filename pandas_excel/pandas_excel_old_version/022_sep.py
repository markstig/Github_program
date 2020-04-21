import pandas as pd

students1 = pd.read_csv('/users/markli/onedrive/study/temp/markpython/pandas_excel/022/Students.csv',  index_col='ID')
students2 = pd.read_csv('/users/markli/onedrive/study/temp/markpython/pandas_excel/022/Students.tsv', sep='\t', index_col='ID')
students3 = pd.read_csv('/users/markli/onedrive/study/temp/markpython/pandas_excel/022/Students.txt', sep='|', index_col='ID')

print(students1)
print(students2)
print(students3)
