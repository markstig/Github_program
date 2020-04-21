import pandas as pd

# create blank file
df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Mark', 'Jason', 'Molley']})
df.to_excel('/users/markli/downloads/testing.xlsx')