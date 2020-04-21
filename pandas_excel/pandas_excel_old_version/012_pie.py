import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/012/Students.xlsx', index_col='From')
print(students)

# students['2017'].sort_values(ascending=True).plot.pie(fontsize=4, startangle=-270)
students['2017'].plot.pie(fontsize=4, counterclock=False, startangle=-270)
plt.title('Source of International Students', fontsize=16, fontweight='bold')
plt.ylabel('2017', fontsize=12, fontweight='bold')

plt.show()
