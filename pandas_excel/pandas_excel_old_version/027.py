import pandas as pd

page_001 = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/027/Students.xlsx', sheet_name='Page_001')
page_002 = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/027/Students.xlsx', sheet_name='Page_002')

# print(page_001)
# print(page_002)

students = page_001.append(page_002).reset_index(drop=True)  # drop the old index

# stu = pd.Series({'ID': 41, 'Name': 'Abel', 'Score': 99})
# students = students.append(stu, ignore_index=True)

# students.at[39, 'Name'] = 'Bailey'
# students.at[39, 'Score'] = 120

# stu = pd.Series({'ID': 40, 'Name': 'Beiley', 'Score': 120})
# students.iloc[39] = stu

# #  insert series
# stu = pd.Series({'ID': 101, 'Name': 'Danni', 'Score': 101})
# part1 = students[:20]
# part2 = students[20:]
# students = part1.append(stu, ignore_index=True).append(part2).reset_index(drop=True)

# delete series
# students.drop(index=[0, 1, 2], inplace=True)
# students.drop(index=range(0,10), inplace=True)
# students.drop(index=students[0:10].index, inplace=True)

for i in range(5, 15):
    students['Name'].at[i] = ''

missing = students.loc[students['Name'] == '']
students.drop(index=missing.index, inplace=True)

print(students)
