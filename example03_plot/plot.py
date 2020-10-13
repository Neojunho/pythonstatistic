import pandas as pd
import numpy
import matplotlib.pyplot as plt

data = pd.read_csv("./example03_plot/scatter.csv", na_values=[999])

df = pd.DataFrame(data, columns = ['학업스트레스', '가족스트레스', '우울', '스마트폰중독'])
df = df.dropna() # 결측치 column 제거

plt.figure(figsize=(10, 10)) #그래프 크기 설정
plt.scatter(df.학업스트레스, df.가족스트레스) # X축에는 X1 변수 Y축에는 Y1변수로 산점도 셋팅
plt.xlabel("academicStress") #X축 이름 지정
plt.ylabel("familyStress") #Y축 이름 지정
plt.grid(True) #그래프 격자 무늬 표시
plt.show() #그래프 그리기