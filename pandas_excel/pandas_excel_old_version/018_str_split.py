# This is data transformation (merge, join or split)
import pandas as pd

employees = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/018/Employees.xlsx', index_col='ID')

df = employees['Full Name'].str.split(' ', expand=True)  # 设置了expand后才能正常进行空格分列， 默认分割符就是 ' '
# df = employees['Full Name'].str.split(n=3, expand=True)  # 切多少个，只保留前三个
employees['First Name'] = df[0]  # 将新数据Frame中的0列添加到employees的'First Name'列
employees['Last Name'] = df[1]

# print(df)

print(employees)
