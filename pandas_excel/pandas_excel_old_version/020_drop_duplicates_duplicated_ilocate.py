import pandas as pd

students = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/020/Students_Duplicates.xlsx')

# students.drop_duplicates(subset='Name', inplace=True, keep='first')  # default of keep is first, it means we keep the first duplicate or last duplicates
# students.drop_duplicates(subset=['ID', 'Name'])

dupe = students.duplicated(subset='Name')
# print(dupe)
# print(dupe.any())
# print(type(dupe))

dupe = dupe[dupe == True]
print(dupe.index)
print(students.iloc[dupe.index])  # relocate by the new index

# print(students)
