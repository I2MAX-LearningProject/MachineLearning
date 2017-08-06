# Day_02_01_loop.py

def not_used_1():
    count = int(input('count : '))

    if count == 1:
        print('Good morning!')
    elif count == 2:
        print('Good morning!')
        print('Good morning!')
    elif count == 3:
        print('Good morning!')
        print('Good morning!')
        print('Good morning!')


    count = 3
    if count > 0:
        print('Good morning!')
        count -= 1
    if count > 0:
        print('Good morning!')
        count -= 1
    if count > 0:
        print('Good morning!')
        count -= 1

    count = 3
    i = 0
    if i < count:
        print('Good morning!')
        i += 1
    if i < count:
        print('Good morning!')
        i += 1
    if i < count:
        print('Good morning!')
        i += 1


# 문제
# count에 0~3 사이의 숫자를 입력 받아서
# 입력 받은 숫자만큼 아침 인사를 해봅니다.
# 2가지 종류의 코드를 만들어 봅니다.
# count = 2
# i = 0
# if i < count:
#     print('Good morning!')
#     i += 1
#     if i < count:
#         print('Good morning!')
#         i += 1
#         if i < count:
#             print('Good morning!')
#             i += 1
#             if i < count:
#                 print('Good morning!')
#                 i += 1

    count = 2
    i = 0
    while i < count:
        print('Good morning!')
        i += 1


    # 규칙
    # 1 3 5 7 9     1, 9, 2     시작, 종료, 증감
    # 0 1 2 3 4     0, 4, 1
    # 5 4 3 2 1     5, 1, -1

    i = 1                   # 시작
    while i <= 9:           # 종료
        print('hello')
        i += 2              # 증감

    i = 0                   # 시작
    while i <= 4:           # 종료
        print('hello')
        i += 1              # 증감

    i = 5                   # 시작
    while i >= 1:           # 종료
        print('hello')
        i -= 1              # 증감

# 문제
# 0~99까지 출력하는 함수를 만드세요.
# 0~99까지 한 줄에 10개씩 출력하는 함수를 만드세요.
# print('hello', end='***')
# print('python')

def show100():      # 0, 99, 1
    i = 0
    while i < 100:
        print(i, end=' ')

        if i%10 == 9:
            print()

        i += 1

    # not good.
    # i = 0
    # while i < 100:
    #     print(i, end=' ')
    #     i += 1
    #
    #     if i%10 == 0:
    #         print()

# show100()

# 0 1 2 3 4 5 6 7 8 9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49
# 50 51 52 53 54 55 56 57 58 59
# 60 61 62 63 64 65 66 67 68 69
# 70 71 72 73 74 75 76 77 78 79
# 80 81 82 83 84 85 86 87 88 89
# 90 91 92 93 94 95 96 97 98 99

for i in range(0, 10, 1):   # 시작, 종료, 증감
    print(i, end=' ')
print()

for i in range(0, 10):      # 시작, 종료, 증감(1)
    print(i, end=' ')
print()

for i in range(10):         # 시작(0), 종료, 증감(1)
    print(i, end=' ')
print()

# 문제
# for문을 사용해서 100보다 작은 양수의 홀수와 짝수 합계를
# 각각 구하는 함수를 만드세요.
# 함수 반환값은 여러 개 가능.
def sumOfOddEven():
    odd, even = 0, 0
    # for i in range(1, 100):
    #     if i%2 == 1:    odd  += i
    #     else:           even += i

    # 1, 99, 2
    # 2, 98, 2
    # for i in range(1, 100, 2):
    #     odd += i
    # for i in range(2, 100, 2):
    #     even += i

    for i in range(0, 100, 2):
        even += i
        odd  += i+1

    return odd, even

s1, s2 = sumOfOddEven()
print(s1, s2)
print('-'*50)

import random

print(random.randrange(10))
print(random.randrange(10, 20))
print(random.randrange(10, 20, 2))

# placeholder
random.seed(1)
for _ in range(5):
    print(random.randrange(10), end=' ')
print()

# next = 1
# def rand():
#     global next
#     next = next * 1103515245 + 12345
#     return int((next//65536) % 32768)

# 문제
# 10개의 100보다 작은 난수 중에서 가장 큰 숫자를 찾는 함수를 만드세요.
def maxNumber():
    # m = 0
    # wrong.
    # for _ in range(10):
    #     print(random.randrange(100), end=' ')
    #     if m < random.randrange(100):
    #         m = random.randrange(100)

    # -63 -97 -57 -60 -83 -48 -26 -12 -62 -3
    m = -random.randrange(100)
    print(m, end=' ')
    for _ in range(10-1):
        n = -random.randrange(100)
        print(n, end=' ')
        if m < n:
            m = n

    print()
    return m

print(maxNumber())
print('-'*50)

s1, s2 = sumOfOddEven()
print(s1, s2)

sum = sumOfOddEven()
print(sum)

