# Day_01_04_function.py

# 함수의 핵심 : 데이터 넘겨주고 넘겨받기.

# 매개변수 : 교수님께서 나에게 넘겨주는 데이터
# 반환값 : 내가 교수님께 넘겨주는 데이터

# 매개변수 없고, 반환값 없고.
def f_1():
    print('f_1')

f_1()

# 매개변수 있고, 반환값 없고.
def f_2(a, b):
    print('f_2', a, b)

f_2(23, 'abc')

# 매개변수 없고, 반환값 있고.
def f_3():
    # pass
    print('f_3')
    return 17

# a = return 17
a = f_3()
print(a)
print(f_3())

# 매개변수 있고, 반환값 있고.
# 2자리 양수를 거꾸로 뒤집는 함수를 만드세요.
def f_4(n):
    return n%10*10 + n//10

print(f_4(37))
print(f_4(82))






print('\n\n\n\n\n\n\n\n\n\n\n\n\n')
