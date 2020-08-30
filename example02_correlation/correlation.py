# f = open('./sample/cc.csv', 'r', encoding='utf-8');
# data = f.read()
# print(data)
# f.close()

import pandas as pd
import os

path = "./" # 파일 경로 지정
file_list = os.listdir(path) # 경로에 로드하고자 하는 파일이 있는지 확인
print(file_list) # 경로에 있는 파일 리스트 출력(배열)

data = pd.read_csv("./example02_correlation/correlation.csv", na_values=[999]) # 파일 로드, 결측치는 999
df = pd.DataFrame(data, columns = ['학업스트레스', '가족스트레스', '우울', '스마트폰중독']) # 상관 분석을 하고자 하는 컬럼 선택
df = df.dropna() # 결측치 column 제거

corr = df.corr(method = 'pearson') # pearson 상관분석 실시
print(corr) # 상관분석 결과 출력