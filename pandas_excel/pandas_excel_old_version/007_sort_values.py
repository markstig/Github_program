import pandas as pd

products = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/007/List.xlsx', index_col='ID')
# products.sort_values(by='Price', inplace=True, ascending=False)

products.sort_values(by=['Worthy', 'Price'], inplace=True, ascending=[True, False])

print(products)
