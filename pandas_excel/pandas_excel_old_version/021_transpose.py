import pandas as pd

pd.options.display.max_columns = 999
videos = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/021/Videos.xlsx', index_col='Month')

table = videos.transpose()

print(table)
