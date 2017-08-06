# Day_01_02_operator.py

# 연산자 : 산술, 관계, 논리, 비트
# 산술 : +  -  *  /  //  %  **
a, b = 17, 5
c = a+b
print(c)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#      3    몫 //
#   +----
# 5 | 17
#     15
#    ----
#      2    나머지 %

# 문제
# 2자리 양수를 거꾸로 뒤집어 보세요.
# 37  -->  73
# 3*10+7  -->  7*10+3

n = 37
a1 = n//10      # 3
a2 = n %10      # 7

n = a2*10 + a1
print(n)
print(n%10*10 + n//10)

#       3
#    +----
# 10 | 37
#      30
#     ----
#       7
print('-'*50)

# 관계 : >  >=  <  <=  ==  !=
print(a, b)

print(a >  b)
print(a >= b)
print(a <  b)
print(a <= b)
print(a == b)
print(a != b)

# 형변환(casting) : int, float, str, bool
print(int(True))
print('345')
print(int('345'))
print(int(a != b))
print(int(False))

# 문제
# 10대인지를 판단해 보세요.
age = 15
b1 = age >= 10      # T, F
b2 = age <= 19      # T, F

# T * T = T
# T * F = F
# F * T = F
# F * F = F

print(bool(b1*b2))
print((age >= 10) * (age <= 19))
print(10 <= age <= 19)
print(True * True)
print('-'*50)

# 논리 : and  or  not
print(True  and True )
print(True  and False)
print(False and True )
print(False and False)

print(age >= 10 and age <= 19)








print('\n\n\n\n\n\n\n\n\n\n\n\n\n')
