import pandas as pd
import numpy as np

page_001 = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/028/Students.xlsx', sheet_name='Page_001')
page_002 = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/028/Students.xlsx', sheet_name='Page_002')

students = pd.concat([page_001, page_002]).reset_index(drop=True)
# students = pd.concat([page_001, page_002], axis=1)

# students['Age'] = 25
# students['Age'] = np.repeat(25, len(students))
# students['Age'] = np.arange(0, len(students))
# students.drop(columns=['Age', 'Score'], inplace=True)


students.insert(1, column='Foo', value=np.repeat('foo', len(students)))  # 默认inplace is True
students.rename(columns={'Foo': 'FOO', 'Name': 'NAME'}, inplace=True)

students['ID'] = students['ID'].astype(float)
for i in range(5, 15):
    students['ID'].at[i] = np.nan

students.dropna(inplace=True)  # 横向扫描一行，只要有na就都删除

print(students)
