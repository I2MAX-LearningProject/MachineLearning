# Day_03_02_dictionary.py

a = {}              # dict
print(type(a), a)
a = {1}             # set
print(type(a), a)
a = {1:2}           # dict
print(type(a), a)

b = {5, 1, 3, 1, 3, 1, 3, 5, 5}
print(b)

c = [5, 1, 3, 1, 3, 1, 3, 5, 5]
print(c)

# 문제
# 리스트에 들어있는 중복된 데이터를 모두 제거해 보세요.
c = list(set(c))
print(c)
print('-'*50)

d = {'color': 'red', 'price': 100}
d = dict(color='red', price=100)
print(d)
print(d['color'], d['price'])

# []   ()    {}
# list tuple set/dictionary

d['title'] = 'pen'      # insert
d['title'] = 'bread'    # update
d['title'] = 'bread'
d['title'] = 'bread'
d['title'] = 'bread'
print(d)

print(d.keys())
print(d.values())
print(d.items())

# 문제
# keys, values, items를 for문과 연결해서 처리해 보세요.
for k in d.keys():
    print(k, d[k])
print('-'*10)

for v in d.values():
    print(v)
print('-'*10)

for i in d.items():
    print(i, i[0], i[1])

for k, v in d.items():
    print(k, v)
print('-'*10)

for i in enumerate(d.items()):
    print(i)
    print(i[0], i[1])
    print(i[0], i[1][0], i[1][1])
print('-'*10)

# 문제
# 출력에서 모든 ()를 없애보세요.
for i, item in enumerate(d.items()):
    print(i, item)
    print(i, item[0], item[1])
print('-'*10)

for i, (k, v) in enumerate(d.items()):
    print(i, k, v)

t1, t2, t3 = 1, 2, 3
t1, (t2, t3) = 1, (2, 3)
print(t1, t2, t3)



print('\n\n\n\n\n\n\n\n\n\n\n\n')