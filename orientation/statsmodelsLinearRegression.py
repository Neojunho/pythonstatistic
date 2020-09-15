import statsmodels.api as sm
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data = pd.read_csv("./orientation/regressionData(2019).csv", na_values=[999])
df = pd.DataFrame(data, columns = ['depress', 'averagegrade']) # 상관 분석을 하고자 하는 컬럼 선택
df = df.dropna() # 결측치 column 제거

x = df["학업스트레스"]
y = df["스마트폰중독"]
# plt.plot(x, y, 'o')
# plt.show()

x = sm.add_constant(x)
model = sm.OLS(y, x)
result = model.fit()

resultSummary = result.summary()
coefArr = result.params
rsquared = result.rsquared
rsquared_adj = result.rsquared_adj
stderr = result.bse
tvalue = result.tvalues
fvalue = result.fvalue
f_pvalue = result.f_pvalue
print(fvalue, f_pvalue)
print(result.t_test([0, 1]))

# standardizing dataframe
df = df.dropna().apply(stats.zscore)
x = df["학업스트레스"]
y = df["스마트폰중독"]
x = sm.add_constant(x)
model = sm.OLS(y, x)
result = model.fit()

stdCoefArr = result.params[1]

# print(stdCoefArr)

# df_z = df.select_dtypes(include=[np.number]).dropna().apply(stats.zscore)
# fitting regression
# df = df.dropna().apply(stats.zscore)
# formula = 'y ~ x1 + x2 + x3'
# result = sm.OLS(formula, data=df_z).fit()
# # checking results
# print(result.params)