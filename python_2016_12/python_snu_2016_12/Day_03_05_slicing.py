# Day_03_05_slicing.py
import Day_02_02_list
# __main__ : 첫 번째 실행되는 파일
# __name__ : 파일별로 존재하는 파일 이름 변수

Day_02_02_list.random.seed(1)
a = Day_02_02_list.makeRandoms()
print(a)

print(a[0], a[-2], a[-1])
print(a[0:5])
print(a[5:10])
print(a[len(a)//2:len(a)])
print('-'*30)
print(a[5:])
print(a[:5])
print(a[:])
print(a[len(a)//2:])

# 문제
# 뒤쪽 절반을 출력해 보세요.
# 짝수 번째 요소만 출력해 보세요.
# 홀수 번째 요소만 출력해 보세요.
print(a[::2])
print(a[1::2])

# 문제
# 거꾸로 출력해 보세요.
# 거꾸로 짝수 번째만 출력해 보세요.
# 거꾸로 홀수 번째만 출력해 보세요.
print(a[::-1])
print(a[len(a)-1:0:-1])
print(a[len(a)-1:-1:-1])
print(a[-1:-1:-1])
print(a[3:3])
print(a[::-2])
print(a[-2::-2])
print('-'*50)

b = a
c = a[:]    # a.copy()
a[0] = -1

print(a)
print(b)
print(c)

for i in range(0, len(a), 2):
    print(a[i], end=' ')
print()

for i in a[::2]:
    print(i, end=' ')
print()






