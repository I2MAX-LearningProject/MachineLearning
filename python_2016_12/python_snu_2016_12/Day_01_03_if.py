# Day_01_03_if.py

a = 13
print(a%2)

if a%2 == 1:
    print('홀수')
else:
    print('짝수')

if a%2:
    print('홀수')
else:
    print('짝수')

if a:
    print('홀수')
else:
    print('짝수')

if a:
    print('홀수')

# 문제
# 0~999 사이의 숫자를 입력 받아서
# 몇 자리 숫자인지 맞춰 보세요.

a = 128     #int(input('number : '))
print(type(a))

if a >= 100:
    print(3)
if 100 > a >= 10:
    print(2)
if 10 > a >= 0:
    print(1)

if a >= 100:
    print(3)
else:
    # print(2, 1)
    if a >= 10:
        print(2)
    else:
        print(1)

a1, a2, a3 = bool(a//100), bool(a//10), bool(a//1)
print(a1 + a2 + a3)

digit = 1
# if a >= 100:    digit = digit+1;    a = a // 10
# if a >=  10:    digit = digit+1;    a = a // 10

if a >= 10:    digit = digit+1;    a = a // 10
if a >= 10:    digit = digit+1;    a = a // 10

print(digit)

# applekoong@naver.com
# 이름을 적어서 비어있는 메일 보내세요.

if a >= 100:
    print(3)
elif a >= 10:
    print(2)
else:
    print(1)

if a >= 100:
    print(3)
else:
    # print(2, 1)
    if a >= 10:
        print(2)
    else:
        print(1)

print('end')
# 공백 : space, return, tab

# 문제
# 2개의 정수 중에서 큰 숫자를 찾는 함수를 만드세요.
# return 키워드 여러 번 사용 가능.
def max2(a, b):
    # if a >= b:
    #     return a
    # else:
    #     return b

    # if a >= b:
    #     return a
    # return b

    if a >= b:
        b = a
    return b

print(max2(3, 7))
print(max2(7, 3))

# 4개의 정수 중에서 큰 숫자를 찾는 함수를 만드세요.
# 힌트 : 복면가왕, 한국시리즈
def max4(a, b, c, d):
    # return max2(max2(a, b), max2(c, d))
    return max2(max2(max2(a, b), c), d)

print(max4(1, 2, 3, 4))
print(max4(4, 1, 2, 3))
print(max4(3, 4, 1, 2))
print(max4(4, 1, 2, 3))












