import pandas as pd

# 将文件读取到内存， 注意需要关闭文件才能读取。
people = pd.read_excel('/users/markli/onedrive/study /temp/markpython/pandas_excel/002/people.xlsx')
print(people.shape)
print(people.columns)

# print(people) # 不建议这样操作， 1 机器吃不消， 2 打出来也看不了

# 一般调取head，看看头部或者尾部都有什么数据, head()默认看数值区域内5行
print(people.head(3))
print("=============================================")
print(people.tail(3))
