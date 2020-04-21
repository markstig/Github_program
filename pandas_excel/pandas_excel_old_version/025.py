import pandas as pd


def low_score_red(s):
    color = 'red' if s < 60 else 'green'
    return f'color:{color}'


students = pd.read_excel('/Users/markli/OneDrive/Study/temp/markpython/pandas_excel/025/Students.xlsx')
students.style.applymap(low_score_red, subset=['Test_1', 'Test_2', 'Test_3'])

