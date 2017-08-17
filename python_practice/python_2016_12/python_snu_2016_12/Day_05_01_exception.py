# Day_05_01_exception.py
import random

# 기존 : 음수(실패), 양수/제로(성공)
# 수정 : 음수(실패), 양수(성공), 제로(보류)
def validate(n):
    if n < 0:
        return False

    return True

a = random.randrange(-5, 5)
print('input :', a)

if validate(a):
    print('pass')
else:
    print('fail')

print('-'*50)

try:
    b = [1, 5, 9]
    print(b[len(b)])
except IndexError:
    print('IndexError')
except ValueError:
    print('ValueError')
except:
    print('unknown error.')
else:
    print('else')
finally:
    print('finally')

print('-'*50)

# while True:
#     try:
#         c = input('number : ')
#         c = int(c)
#         print('result :', c**2)
#         break
#     except ValueError:
#         print('ValueError')
#
# print(c * c)
# print('end of code.')
