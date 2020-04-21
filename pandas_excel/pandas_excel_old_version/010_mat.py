import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/010/Students.xlsx')
students.sort_values(by='2017', inplace=True, ascending=False)
# students.index = range(0, len(students))

# print(students)

bar_width = 0.5
x_pos = np.arange(len(students)*2, step=2)
print(x_pos)

plt.bar(x_pos, students['2017'], color='green', width=bar_width)
plt.bar(x_pos + bar_width, students['2016'], color='blue', width=bar_width)

plt.xticks(x_pos + bar_width / 2, students['Field'], rotation=45, ha='right')
plt.title('International Student by Field', fontsize=16)
plt.xlabel('Field')
plt.ylabel('Number')

plt.tight_layout()
plt.show()
