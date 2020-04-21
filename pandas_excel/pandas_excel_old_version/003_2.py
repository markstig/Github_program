import pandas as pd

S1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
S2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
S3 = pd.Series([200, 300, 400], index=[2, 3, 4], name='C')

# add the data with a dict
df = pd.DataFrame({S1.name: S1, S2.name: S2, S3.name: S3})
print(df)

# add the data with a list
df2 = pd.DataFrame([S1, S2, S3])
print(df2)
