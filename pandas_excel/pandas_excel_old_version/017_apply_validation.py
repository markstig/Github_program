# Excel可以用data validation， 设置好条件后，在data选项中，选择圈出错误值，这样之前的错误值就被圈出来了。 新的错误值才会被进行数据校验。
import pandas as pd


# def score_validation(row):  # make a function for the validation
#     try:
#         assert 0 <= row.Score <= 100  # 断定下值是不是符合条件
#     except:
#         print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}') # 如果不符合条件，抛出异常

def score_validation_if(row):
    if not 0 <= row.Score <= 100:
        print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}.')

students = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/017/Students.xlsx')  # 进行数据校验前，最好不要设置index，这样所有的列都会以普通列进行展示，所有的列都会被校验到。

# print(students)

# students.apply(score_validation, axis=1)  # axis=0 from top to bottom, axis=1 from left to right

students.apply(score_validation_if, axis=1)
