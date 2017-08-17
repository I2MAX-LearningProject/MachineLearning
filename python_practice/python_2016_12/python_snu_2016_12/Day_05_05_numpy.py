# Day_05_05_numpy.py
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(10)
print(a)
print(type(a))

print(a[0], a[1], a[-1])
print(a[:5])
print(a[::-1])

a[:] = -1
print(a)
a[::2] = 99
print(a)
print('-'*50)

b = a.reshape(2, 5)
# b = np.reshape(a, (2, 5))
print(b)

c = np.arange(12).reshape(3, 4)
print(c)

print(c[0])
print(c[0][1])
print(c[-1][-1])

print(c[1, 1])
print(c[1, 1:])

# 문제
print(c[::-1, ::-1])

print(c > 7)
print(c[c>7])
print(c * 2)

# -------------------------------------- #

# plt.plot([10, 20, 30, 40, 50])
# plt.ylabel('price')

plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0,6,0,20])

plt.show()












