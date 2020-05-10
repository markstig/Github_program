# Merge and Join, union(this is for columns) function, used frequently in database

import pandas as pd

students = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/016/Student_Score.xlsx', sheet_name='Students', index_col='ID')
scores = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/016/Student_Score.xlsx', sheet_name='Scores', index_col='ID')

# print(students)
# print(scores)

table = students.merge(scores, how='left', on='ID').fillna(0)  # how:用在哪个表上 on: 用那一列进行联立
# table = students.merge(scores, how='left').fillna(0)  # 如果未规定on的话，pandas会自动找有没有合适的去进行联立。 需要注意的是这里不能设置index，一旦设置index，index列就不属于普通列了。
# table = students.merge(scores, how='left', left_on='ID', right_on='ID').fillna(0)  # 如果左右的查找列名称不一样，要用分别定义好左右的名称。

# table = students.merge(scores, how='left', left_on=students.index, right_on=students.index).fillna(0)  # if we do this, we have to define the index_col at the beginning

table2 = students.join(scores, how='left').fillna(0)  # join可以找到左右的索引列并进行联立，建议用join


table.Score = table.Score.astype(int)  # 将列字段转换成整数
table2.Score = table.Score.astype(int)

print(table)
print(table2)
