import pandas as pd

# create a series in excel, data, name and index are three most important things for a series
# series is very much like a dict in python
d = {'x': 100, 'y': 200, 'z': 300}  # this is a dictionary, it contains 3 keys values pairs (键，值，对)
print(d.keys())
print(d.values())

s1 = pd.Series(d)
print(s1)
print(s1.index)
print(s1.data)

# create a series through two list
L1 = [100, 200, 300]
L2 = ['x', 'y', 'z']
s2 = pd.Series(L1, index=L2)
print(s2)

# create a series directly
s3 = pd.Series([100, 200, 300], index=['x', 'y', 'z'])
print(s3)
