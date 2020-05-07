import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns=777  # show all the columns
homes = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/014/home_data.xlsx')

print(homes.head())

# homes.plot.scatter(x='sqft_living', y='price')  # can easily handle lots of data, and we can change x axis and y axis very easily.


# homes.sqft_living.plot.hist(bins=100)  # hist chart, and set the buskets to show the data more precise
# plt.xticks(range(0, max(homes.sqft_living), 500), fontsize=8, rotation=90)

# homes.sqft_living.plot.kde()  # Kernal density estimation 密度图
# plt.xticks(range(0, max(homes.sqft_living), 500), fontsize=8, rotation=90)

# plt.show()

print(homes.corr())  # correlation 相关性
