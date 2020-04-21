import pandas as pd
from datetime import date, timedelta


def add_month(d, md):
    yd = md // 12  # 整除
    m = d.month + md % 12  # %取余数
    if m != 12:
        yd += m//12
        m = m % 12
    return date(d.year + yd, m, d.day)


books = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/004/books.xlsx', skiprows=3, usecols='C:F', index_col=None, dtype={'ID': str, 'InStore': str, 'Date': str})  # Don't set the index now, because we are going to use the fill_in here, if we set the index now, it will cause some problems.

# print(books)
# print(books['ID'])
# print(type(books['ID']))


# books['ID'].at[0] = 100
# print(books['ID'])


start = date(2018, 1, 1)
for i in books.index:
    books['ID'].at[i] = i + 1  # row + 1, default is float number, because this column is NAN before, pandas will set the float type for such NAN cells.
    books['InStore'].at[i] = 'Yes' if i % 2 == 0 else 'No'
    # books['Date'].at[i] = start + timedelta(days=i)
    # books['Date'].at[i] = date(start.year + i, start.month, start.day)
    books['Date'].at[i] = add_month(start, i)

books.set_index('ID', inplace=True)

print(books)

books.to_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/004/books_finished.xlsx')

# modify in the data frame directly, not get the data series firt.
# for i in books.index:
#     books.at[i, 'ID'] = i + 1
#     books.at[i, 'InStore'] = 'Yes' if i % 2 == 0 else 'No'
#     books.at[i, 'Date'] = add_month(start, i)
