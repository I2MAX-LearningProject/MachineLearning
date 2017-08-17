# Day_04_04_comprehension.py
import random

random.seed(1)

# a = [i for i in range(10)]
a = [random.randrange(100) for _ in range(10)]
print(a)
print(sum(a), max(a), min(a))

# b = [i*2 for i in a]
b = [i for i in reversed(a)]
print(b)

c = [i for i in a if i%2 == 1]
print(c)

# for i in a:
#     if i%2 == 1:
#         i
print('-'*50)

a1 = [random.randrange(100) for _ in range(random.randrange(5, 15))]
a2 = [random.randrange(100) for _ in range(random.randrange(5, 15))]
a3 = [random.randrange(100) for _ in range(random.randrange(5, 15))]
all = [a1, a2, a3]
print(*all, sep='\n')

# 문제
# all에 들어있는 숫자의 갯수를 세어 보세요.
# all에서 가장 큰 값을 찾아보세요.
print(sum([len(i) for i in all]))
print(max([max(i) for i in all]))

s = 'AABBCCAA'
print(s.count('A'))

# 문제
# 10000보다 작은 양수에 포함된 8의 갯수를 세어 보세요.
# 808  -->  2
print([str(i) for i in range(10)])
print([str(i).count('8') for i in range(10)])
print(sum([str(i).count('8') for i in range(10000)]))
print(str([i for i in range(10000)]).count('8'))
print(str(list(range(10000))).count('8'))

# 문제
# 2차원 리스트 all 변수를 1차원으로 저장해 보세요.
# [26, 12, 62, 3, 49, 55, 77, 97, 98, 0, 89]
# [34, 92, 29, 75, 13, 40, 3, 2, 3, 83, 69, 1]
# [87, 27, 54, 92, 3, 67, 28, 97, 56, 63, 70]

# [26, 12, 62, 3, 49, 55, 77, 97, 98, 0, 89, 34, 92, 29, 75, 13, 40, 3, 2, 3, 83, 69, 1, 87, 27, 54, 92, 3, 67, 28, 97, 56, 63, 70]
print([j for i in all for j in i])
# for i in all:
#     for j in i:
#         j

print([[i, i] for i in range(3)])
print([[j for j in range(3)] for i in range(3)])
print('-'*50)

# 문제
# all을 완전히 거꾸로 뒤집어 보세요.
print(*[[j for j in reversed(i)] for i in reversed(all)], sep='\n')











print('\n\n\n\n\n\n\n\n')



