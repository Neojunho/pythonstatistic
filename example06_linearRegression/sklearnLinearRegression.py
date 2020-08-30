from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#분석할 데이터 불러오기
data = pd.read_csv("./regressionData(2019).csv", na_values=[999])
df = pd.DataFrame(data, columns = ['학업스트레스', '가족스트레스', '우울', '스마트폰중독']) # 상관 분석을 하고자 하는 컬럼 선택
df = df.dropna() # 결측치 column 제거

x = df["학업스트레스"]
y = df["스마트폰중독"]
# plt.plot(x, y, 'o')
# plt.show()

#Linear Regression 분석
xCon = sm.add_constant(x)
model = sm.OLS(y, xCon)
result = model.fit()
resultSummary = result.summary()
print(resultSummary)


line_fitter = LinearRegression()
line_fitter.fit(x.values.reshape(-1,1), y) #다중회귀분석을 위한 변환

newStress = 3.12
newStudents = line_fitter.predict([[3]])
print('학업stress가', newStress, '점일때, 20학번 신입생의 1년 후 스마트폰중독 수준 예측:', newStudents)

# regCoef = line_fitter.coef_
# regInter = line_fitter.intercept_
# modelFit = line_fitter.score

# print(regCoef)
# print(regInter)
# print(modelFit)

plt.plot(x, y, 'o')
plt.plot(x, line_fitter.predict(x.values.reshape(-1,1)))
plt.show()



