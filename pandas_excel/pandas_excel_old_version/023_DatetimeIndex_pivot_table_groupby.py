import pandas as pd
import numpy as np

pd.options.display.max_columns = 999
orders = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/023/Orders.xlsx')

orders['Year'] = pd.DatetimeIndex(orders['Date']).year

# print(orders.head())
# print(orders.Date.dtype)

# pt1 = orders.pivot_table(index='Category', columns='Year', values='Total', aggfunc=np.sum)
# print(pt1)  # This way is a simulation of pivot table

groups = orders.groupby(['Category', 'Year'])
s = groups['Total'].sum()
c = groups['ID'].count()

pt2 = pd.DataFrame({'Sum': s, 'Count': c})
print(pt2)
