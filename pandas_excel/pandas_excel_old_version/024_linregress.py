import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress  # 线性回归的缩写 linear regression

sales = pd.read_excel('/users/markli/onedrive/study/temp/markpython/pandas_excel/024/Sales.xlsx', dtype={'Month': str})
# print(sales)

slope, intercept, r, p, std_err = linregress(sales.index, sales.Revenue)  # 坡度， Y轴上的截距，std_err=标准差

# print(slope)

exp = sales.index*slope + intercept  # 算期望值
# print(exp)

plt.scatter(sales.index, sales.Revenue)
plt.plot(sales.index, exp, color='orange')  # here is a problem

plt.title(f'y={slope}*x+{intercept}')
plt.xticks(sales.index, sales.Month, rotation=90)

plt.tight_layout()
plt.show()

# print(slope*35 + intercept)  # prediction
