import pandas as pd
import matplotlib.pyplot as plt
students = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/010/Students.xlsx')
print(students)

students.sort_values(by='2017', inplace=True, ascending=False)  # inplace是true的话不会形成新的dataframe
# students.plot.bar(x='Field', y=['2016', '2017'], color=['orange', 'red'], title='International Students by Field')  # You can't change the font size here in pandas, but you can change it in matplotlib

students.plot.bar(x='Field', y=['2016', '2017'], color=['orange', 'red'])
plt.title('International Students by Field', fontsize=16, fontweight='bold')
plt.xlabel('Field', fontsize=13, fontweight='bold')
plt.ylabel('Number', fontsize=13, fontweight='bold')

ax = plt.gca()  # gca = get current axis
ax.set_xticklabels(students['Field'], rotation=45, ha='right')  # ha = horizaon alignment

f = plt.gcf()  # gcf = get current figures 拿到图形
f.subplots_adjust(left=0.2, bottom=0.2)

plt.tight_layout()
plt.show()
