import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 101) #-5부터 5까지 사이를 101등분하기
print(x)

y = (1 / np.sqrt(2 * np.pi)) * np.exp(- x ** 2 / 2 ) #평균이 0, 분산이 1일 때 정규분포의 y축 값
print(y)

plt.figure(figsize=(10, 6))          # 플롯 사이즈 지정
plt.plot(x, y)                       
plt.xlabel("x")                      # x축 레이블 지정
plt.ylabel("y")                      # y축 레이블 지정
plt.grid()                           # 플롯에 격자 보이기
plt.title("Normal Distribution without scipy")     # 타이틀 표시
plt.legend(["N(0, 1)"])              # 범례 표시
plt.show()                           # 플롯 보이기