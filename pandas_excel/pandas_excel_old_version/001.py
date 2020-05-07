import pandas as pd

# # 创建空文件
# df = pd.DataFrame()
# df.to_excel("c:/users/mark.a.li/onedrive/business/temp/markpython/pandas_excel/001/output.xlsx")
#
# print('Done!')

# # 创建带数据的文件（自动创建一列索引）
# df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Tim', 'Victor', 'Nick']})
# df.to_excel("c:/users/mark.a.li/onedrive/business/temp/markpython/pandas_excel/001/output.xlsx")
# print('Done!')

# 创建带数据的文件，并定义一列为索引
df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Tim', 'Victor', 'Nick']})
df = df.set_index('ID')
print(df)
df.to_excel("c:/users/mark.a.li/onedrive/business/temp/markpython/pandas_excel/001/output.xlsx")
print('Done!')
