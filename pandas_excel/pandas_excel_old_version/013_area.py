import pandas as pd
import matplotlib.pyplot as plt

weeks = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/013/Orders.xlsx', index_col='Week')

print(weeks)
print(weeks.columns)

# Normal trend chart, and area chart
weeks.plot.area(y=['Accessories', 'Bikes', 'Clothing', 'Components'])
plt.title('Sales Weekly Trend', fontsize=16, fontweight='bold')
plt.ylabel('Total', fontsize=12, fontweight='bold')
plt.xticks(weeks.index, fontsize=8)

plt.show()
