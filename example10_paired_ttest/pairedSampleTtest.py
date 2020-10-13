import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import docx
import os

# RawData 로드하기
data = pd.read_excel("./example10_paired_ttest/pairedTtestData.xlsx", na_values=[999]) # RawData 파일 경로와 결측치 값 설정
df = pd.DataFrame(data, columns = ['edu_Pre', 'edu_Post']) # 컬럼 정의
df = df.dropna() # 결측치 column 제거
edu_Pre = df['edu_Pre']
edu_Post = df['edu_Post']

교육전사례수 = len(edu_Pre)
print("교육전사례수", 교육전사례수)
교육후사례수 =len(edu_Post)
print("교육후사례수", 교육후사례수)
교육전평균 = np.mean(edu_Pre)
print("교육전평균:", 교육전평균)
교육전분산 = np.var(edu_Pre)
print("교육전분산:", 교육전분산)
교육전표준편차 = np.std(edu_Pre)
print("교육전표준편차:", 교육전표준편차)
교육후평균 = np.mean(edu_Post)
print("교육후평균:", 교육후평균)
교육후분산 = np.var(edu_Post)
print("교육후분산:", 교육후분산)
교육후표준편차 = np.std(edu_Post)
print("교육후표준편차:", 교육후표준편차)

result = stats.ttest_rel(edu_Pre, edu_Post)
print(result)