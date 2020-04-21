import pandas as pd
from datetime import date, timedelta

# Test add_month function
# def add_month(d, i):
#     while i < 100:
#         addy = i // 12
#         m = d.month + i % 12
#         if m > 12:
#             addy += m // 12
#             m = m % 12
#         new = date(d.year + addy, m, d.day)
#         i += 1
#         print(new)
#
# d = date(2019,10,1)
# i = 0
# add_month(d, i)


# read dataframe from the file, skip empty cells, set datatype, set value for special cell.
books = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/004/books.xlsx', skiprows=3, usecols='c:f', index_col=None, dtype={'ID': str, 'Instore': str, 'Date': str})

print(books)
print(books['ID'])
print(type(books['ID']))

# books['ID'].at[0] = 100
# print(books['ID'])


def add_month(d, md):
    yd = md // 12
    m = d.month + md % 12
    if m != 12:
        yd += m // 12
        m = m % 12
    return date(d.year + yd, m, d.day)


start = date(2019, 2, 1)
for i in books.index:
    books['ID'].at[i] = i + 1
    books['Instore'].at[i] = 'Yes' if i % 2 == 0 else 'No'
    books['Date'].at[i] = add_month(start, i)

books.set_index('ID', inplace=True)

print(books['ID'])
