# Day_01_01_Basic.py

print('Hello, python!'*3)

print('Hello, python!Hello, python!Hello, python!')

print('Hello, python!')
print('Hello, python!')
print('Hello, python!')

print("Hello, python!" "Hello, python!" "Hello, python!")
print("Hello, python!" \
      "Hello, python!" \
      "Hello, python!")
print("Hello, python!"
      "Hello, python!"
      "Hello, python!")
print("Hello, python!", "Hello, python!", "Hello, python!")

# 문제
# Hello, python!을 3회 출력하는 코드를 3가지 만들어 보세요.

# 프로그래밍 : 프로그램을 만드는 과정
# 프로그램 : 코드, 데이터
# 데이터 : 변수, 상수
# 데이터 : 숫자(실수 float, 정수 integer), 글자(문자열,string), 논리값(boolean)

print(3.14, 56, 'hello', True)
print(type(3.14), type(56), type('hello'), type(True))

a = 3.14            # 대입 연산자(assignment)
print(3.14, a)
a = 56
print(a, type(a))

print('hell\no, python!')   # newline, 개행문자
print('"hello"')
print("'hello'")
print('-'*50)

# a = 7
# b = 19
a, b = 7, 19
# a = 7; b = 19
print(a, b)

# 문제
# 아래쪽 코드에서 거꾸로 출력하도록 코드를 추가해 보세요.
# a와 b를 서로 교환합니다.

# bug.
# a = 19
# b = 7

# 주스, 콜라
# 빈컵 = 주스
# 주스 = 콜라
# 콜라 = 빈컵
t = a           # swap
a = b
b = t

print(a, b)

a, b = b, a     # 다중치환

print(a, b)














print('\n\n\n\n\n\n\n\n\n\n\n\n')
