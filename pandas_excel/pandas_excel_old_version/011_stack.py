import pandas as pd
import matplotlib.pyplot as plt


users = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/011/users.xlsx')
users['Total'] = users['Oct'] + users['Nov'] + users['Dec']
users.sort_values(by='Total', inplace=True, ascending=False)
print(users)

users.plot.bar(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True, title='User Behavior')
users.plot.barh(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True, title='User Behavior')

plt.tight_layout()
plt.show()
