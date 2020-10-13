import numpy

# 리스트(List)
x = 80 # integer
y = 90 # integer
testScore = [90, 80, 70, 85, 79, 70, 80, 70, 80, 80]
print(testScore)

# 리스트 개별 값을 꺼내오기
print(testScore[0])

# 합계 구하기
testScoreSum = testScore[0] + testScore[1] + testScore[2] + testScore[3] + testScore[4] + testScore[5] + testScore[6] + testScore[7] + testScore[8] + testScore[9]
print('testScoreSum:', testScoreSum)

# 평균 구하기
testScoreMean = testScoreSum / 10
print('testScoreMean:', testScoreMean)

# 분산 구하기
testScoreVar = ((testScore[0]-testScoreMean)**2 + (testScore[1]-testScoreMean)**2 + (testScore[2]-testScoreMean)**2 + (testScore[3]-testScoreMean)**2 + (testScore[4]-testScoreMean)**2 + (testScore[5]-testScoreMean)**2 + (testScore[6]-testScoreMean)**2 + (testScore[7]-testScoreMean)**2 + (testScore[8]-testScoreMean)**2 + (testScore[9]-testScoreMean)**2) / 10
print('testScoreVar:', testScoreVar)

print("numpy패키지 분산구하기", numpy.var(testScore))