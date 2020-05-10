import pandas as pd


def age_18_to_30(a):
    return a >= 18 and a < 30  # you can also write 18<=a<30 in python


def level_a(s):
    return 85 <= s <= 100


students = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/008/Students.xlsx', index_col='ID')
# students = students.loc[students['Age'].apply(age_18_to_30)].loc[students['Score'].apply(level_a)]  # loc is an attribute, so it is with []

# students = students.loc[students.Age.apply(age_18_to_30)].loc[students.Score.apply(level_a)]

students = students.loc[students.Age.apply(lambda a: 18 <= a < 30)].loc[students.Score.apply(lambda s: 85 <= s <= 100)]  # if the line is too long, we can use '\ ' to warp the text

print(students)
