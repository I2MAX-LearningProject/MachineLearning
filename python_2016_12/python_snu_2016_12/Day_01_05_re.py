# Day_01_05_re.py
import re

db = '''3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534'''

# db = '3412    Bob 123\n' \
#      '3834  Jonny 333\n' \
#      '1248   Kate 634'

print(db)

# ''' ''' 설명
# raw 문자열 설명

# 파이썬 문자열 : \n, \t, \a

ns = re.findall(r'[0-9]+', db)      # raw
print(ns)

# 문제
# 이름만 찾아보세요.
# names = re.findall(r'[A-z]+', db)   # bug.
names = re.findall(r'[A-Za-z]+', db)
names = re.findall(r'[A-Z][a-z]+', db)
print(names)

# 문제
# T로 시작하는 이름만 찾아보세요.
# T로 시작하지 않는 이름만 찾아보세요.
print(re.findall(r'T[a-z]+', db))
# print(re.findall(r'[^T][a-z]+', db))    # buf
print(re.findall(r'[A-SU-Z][a-z]+', db))











