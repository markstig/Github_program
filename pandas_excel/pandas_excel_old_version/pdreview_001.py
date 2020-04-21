import pandas as pd

# Creat empty excel file
df = pd.DataFrame()  # DataFrame equal to worksheet
df.to_excel(
    "/users/markli/onedrive/study/temp/markpython/pandas_excel/test/output.xlsx")

# Create file with data
df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Tim', 'Victor', 'Nick']})
df.to_excel(
    "/users/markli/onedrive/study/temp/markpython/pandas_excel/test/output1.xlsx")

# Create file with data and set index
df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Tim', 'Victor', 'Nick']})
df = df.set_index('ID')
df.to_excel(
    "/users/markli/onedrive/study/temp/markpython/pandas_excel/test/output2.xlsx")
print('Done!')

# Read file, read shape, read columns, read head and tail.
people = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/002/people.xlsx')
print(people.shape)
print(people.columns)
print(people.index)
print(people.head(3))
print(people.tail(3))

# Read file, the column is at row 2
people = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/002/people_2.xlsx', header = 1)
print(people.columns)

# Set new columns and index for a dataframe
people = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/002/people_3.xlsx', header=None)  # Tell pandas that this file didn't have columns now
people.columns = ['ID', 'Type', 'Title', 'FirstName', 'MiddleName', 'LastName']
print(people.columns)
people = people.set_index('ID')  # set the new index, or use this: people.set_index('ID', inplace = True)
# make a new file with the new columns
people.to_excel(
    "/users/markli/onedrive/study/temp/markpython/pandas_excel/test/setcolumns.xlsx")

# Set index column
df = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/002/people.xlsx', index_col='ID')
print(df.head())

# Concept of dict, range, directly, pd.Series
d = {'x': 100, 'y': 200, 'z': 300}
print(d.keys())
print(d.values())

s1 = pd.Series(d)
print(s1)
print(s1.index)

L1 = [100, 200, 300]
L2 = ['x', 'y', 'z']
s2 = pd.Series(L1, index=L2)
print(s2)

s3 = pd.Series([100, 200, 300], index=['x', 'y', 'z'])
print(s3)

# Series and DataFrame
S1 = pd.Series([1,2,3], index=[1,2,3], name='A')
S2 = pd.Series([10,20,30], index=[1,2,3], name='B')
S3 = pd.Series([200,300,400], index=[2,4,3], name='C')

df = pd.DataFrame({S1.name: S1, S2.name: S2, S3.name: S3})
print(df)

df2 = pd.DataFrame([S1, S2, S3])
print(df2)
