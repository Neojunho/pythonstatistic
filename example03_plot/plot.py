
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

data = pd.read_csv("./example03_plot/scatter.csv", na_values=[999])
# 상관 분석을 하고자 하는 컬럼 선택. 변수명에 한글이 들어가면 오류가 나기 때문에 x1, y1, z1, e1으로 변수명 변경
# df = pd.DataFrame(data, columns = ['학업스트레스', '가족스트레스', '우울', '스마트폰중독']) 
df = pd.DataFrame(data, columns = ['X1', 'Y1', 'Z1', 'E1'])
df = df.dropna() # 결측치 column 제거
# print(df)
plt.figure(figsize=(10, 10)) #그래프 크기 설정
plt.scatter(df.X1, df.Y1) # X축에는 X1 변수 Y축에는 Y1변수로 산점도 셋팅
plt.xlabel("X1") #X축 이름 지정
plt.ylabel("Y1") #Y축 이름 지정
plt.grid(True) #그래프 격자 무늬 표시
plt.show() #그래프 그리기