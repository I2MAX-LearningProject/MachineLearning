# Day_05_03_lambda.py
from operator import itemgetter

def makeDouble(n):
    return n*2

f1 = makeDouble
print(f1(3))
print(makeDouble(3))

f2 = lambda n: n*2
print(f2(3))
print((lambda n: n*2)(3))
print('-'*50)


def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def proxy(f, a1, a2):
    return f(a1, a2)

print(proxy(add, 3, 5))
print(proxy(sub, 3, 5))
print(proxy(lambda a, b: a+b, 3, 5))
print('-'*50)

import Day_02_02_list

Day_02_02_list.random.seed(1)
a = Day_02_02_list.makeRandoms()
print(a)

print(sorted(a))
print(a)

# print(a.sort())
# print(a)

# def temp():
#     pass
#
# b = None
# print(temp())

# t1 = None
# t2 = []
#
# t2.append(1)
# t1.append(1)

def under10(n):
    # print(n)
    return n%10

# sort : ascend, descend
print(sorted(a, reverse=True))
print(sorted(a, key=lambda n: n%10))
print(sorted(a, key=under10))
print('-'*50)

colors = ['Yellow', 'green', 'RED', 'bLuE', 'WHITE']

print(sorted(colors))
print(sorted(colors, key=lambda s: s.lower()))

# 문제
# 길이순으로 정렬해 보세요.
print(sorted(colors, key=lambda s: len(s)))

items = [('kim', 10), ('han', 20), ('han', 50), ('kim', 20),
         ('kim', 70), ('kim', 50), ('han', 80), ('han', 70)]
print(items)
print(sorted(items))
print(sorted(items, key=lambda t: t[1]))

print(sorted(items, key=itemgetter(0)))
print(sorted(items, key=itemgetter(1)))
print(sorted(items, key=itemgetter(1, 0)))

# list.sort(a)    # unbound method
# a.sort()        #   bound method






print('\n\n\n\n\n\n\n')
