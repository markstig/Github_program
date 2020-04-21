import pandas as pd

students = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/019/Students.xlsx', index_col='ID')

temp = students[['Test_1', 'Test_2', 'Test_3']]  # get a sub dataframe
# print(temp)
# tempsum = temp.sum()  # sum from top to bottom
# print(tempsum)

row_sum = temp.sum(axis=1)
row_mean = temp.mean(axis=1)
# print(row_sum)
# print(row_mean)

students['Total'] = row_sum
students['Average'] = row_mean

col_mean = students[['Test_1', 'Test_2', 'Test_3']].mean()
col_mean['Name'] = 'Summary'
# print(col_mean)
students = students.append(col_mean, ignore_index=True)  # append会生成一个新的dataframe， 所以要用等号引用新的

print(students)
