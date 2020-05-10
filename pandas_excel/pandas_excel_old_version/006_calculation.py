import pandas as pd

books = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/006/books.xlsx', index_col='ID')
# books['Price'] = books['ListPrice']*books['Discount']*0.8  # We use series multiply series

# for i in books.index:
#     books['Price'].at[i] = books['ListPrice'].at[i]*books['Discount'].at[i]  # We use cells multiply cells

# for i in range(5, 16):
#     books['Price'].at[i] = books['ListPrice'].at[i]*books['Discount'].at[i]

# books['ListPrice'] = books['ListPrice']+2


# def add_2(x):
#     return x+2
# books['ListPrice'] = books['ListPrice'].apply(add_2)  #注意这里是用函数名，函数不要加括号，这里不是要调用这个函数

books['ListPrice'] = books['ListPrice'].apply(lambda x: x+2)  #不用创建函数，用lambda表达式

print(books)
