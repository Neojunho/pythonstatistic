from numpy import arange, linspace, mean
from scipy.stats import expon, zscore, norm
import matplotlib.pyplot as plt
from math import log10

# 30개의 샘플을 추출하고 표준화 하는 과정
times = 10
l = 10
loc = 0

m = []

for i in arange(times):
   m.append(mean(expon(loc, l).rvs(size=30))) #Lambda = 10인 지수분포를 랜덤으로 30개 생성하고 그 평균을 구해 배열(m)에 담기

z = zscore(m) # z score를 이용한 표준화(평균 0, 표준편차 1)
print(z)

# 위와 같은 방식으로 샘플을 추출하고 그 평균을 구해 그래프로 그리기
def test (times):
    
    t = times
    l = 10
    loc = 0

    m = []

    for i in arange(t):
       m.append(mean(expon(loc, l).rvs(size=30)))
    
    z = zscore(m)
    
    b = int(6 * log10(t))
    
    fig = plt.figure(figsize=(12, 6))

    ax1 = fig.add_subplot(1, 2, 1)
    ax1 = plt.hist(m, bins=b, facecolor='wheat')
    ax1 = plt.xlabel('m')
    ax1 = plt.ylabel('frequency')
    ax1 = plt.title(r'Histogram of Random Exponential ($\lambda = 10, size = $' + str(t) + ')')
    ax1 = plt.grid()

    x = linspace(-3, 3, 101)

    ax2 = fig.add_subplot(1, 2, 2)
    ax2 = plt.hist(z, bins=b, density=True, facecolor='skyblue')
    ax2 = plt.plot(x, norm(0, 1).pdf(x), 'r--')
    ax2 = plt.xlabel('z')
    ax2 = plt.ylabel('density')
    ax2 = plt.title(r'Histogram of Random Exponential ($\lambda = 10, size = $' + str(t) + ')')
    ax2 = plt.grid()

    plt.show()

# 30회 시뮬레이션
test(1000)