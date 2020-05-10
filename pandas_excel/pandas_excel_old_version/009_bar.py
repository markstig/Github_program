# 文不如表，表不如图
import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/009/Students.xlsx')
print(students)

students.sort_values(by='Number', inplace=True, ascending=False)  # 排序之后生成了一个新的data frame， 所以这里要加 inplace=True
# students.plot.bar(x='Field', y='Number', color='Orange', title='International Students by Fields')  # this we use pandas to get the picture

plt.bar(students.Field, students.Number, color='orange')
plt.xticks(students.Field, rotation='90')
plt.xlabel('Field')
plt.ylabel('Number')
plt.title('International Students by Fields', fontsize=16)

plt.tight_layout()
plt.show()
