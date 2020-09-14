# 정수
정수a = 123
정수b = -123
print('정수a', 정수a, '정수b', 정수b)

# 실수
실수a = 1.23
실수b = -1.23
print('실수a', 실수a)
print('실수b', 실수b)

# 12300000000.0,  0.100000000123표현하기
긴실수a = 1.23E10
긴실수b = 1.23E-10
print('긴실수a', 긴실수a)
print('긴실수b', 긴실수b)

# 2진수: 0b
if 42 == 0b101010:
    print('42 == 0b101010', 'true')
else:
    print('42 == 0b101010', 'false')

# 8진수: 0o
if 42 == 0o52:
    print('42 == 0o52', 'true')
else:
    print('42 == 0o52', 'false')

# 16진수: 0x
if 42 == 0o52:
    print('42 == 0x2a', 'true')
else:
    print('42 == 0x2a', 'false')