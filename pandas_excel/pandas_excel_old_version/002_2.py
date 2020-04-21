import pandas as pd

# # 设置默认读取的第一行的值， 如果源文件上面都是空的，pandas会自动跳过，此时不用设置header
# people = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/002/people_2.xlsx', header = 1)
#
# print(people.columns)


# # Set columns with pandas
# people = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/002/people_3.xlsx', header=None)  # Tell pandas that this file didn't have columns now
# people.columns = ['ID', 'Type', 'Title', 'FirstName', 'MiddleName', 'LastName']
# print(people.columns)
# people = people.set_index('ID')  # set the new index, or use this: people.set_index('ID', inplace = True)
# # make a new file with the new columns
# people.to_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/002/people_3_with_columns.xlsx')
# print('Done!')


# Set index column
df = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/002/people.xlsx', index_col='ID')
print(df.head())
