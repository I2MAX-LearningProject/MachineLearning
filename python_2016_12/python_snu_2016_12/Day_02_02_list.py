# Day_02_02_list.py
import random

def makeRandoms():
    # a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # a = [0]*10
    # for i in range(10):
    #     a[i] = random.randrange(100)

    a = []
    for _ in range(10):     # 시작(0), 종료, 증감(1)
        a.append(random.randrange(100))

    return a

if __name__ == '__main__':
    # collection : []    ()     {}              <>
    #              list  tuple  set/dictionary  not_used
    # array : index를 사용해서 데이터에 접근

    a = [1, 3, 5, 7]
    print(a)
    print(a[0], a[1], a[2])

    a[0] = 99
    print(a)

    # a[0]
    # a[1]
    # a[2]

    for i in range(len(a)):
        print(a[i])
    print('-'*30)

    # 문제
    # 100보다 작은 난수 10개로 이루어진 리스트를
    # 반환하는 함수를 만드세요.


    random.seed(19)
    b = makeRandoms()
    print(b)

    # a = [1, 3, 5, 7]
    # a.append(15)
    # print(a)

    # 문제
    # 리스트를 거꾸로 뒤집는 함수를 만드세요.

    #  0  1   2   3   4   4   3   2   1   0
    # 86, 5, 66, 15, 65, 25, 50, 44, 67, 37
    # 37                                 86
    #     67                          5
    def reverseList(c):     # c = b
        # a = []
        # for i in range(len(c)-1, -1, -1):
        #     a.append(c[i])
        # for i in range(len(a)):
        #     c[i] = a[i]
        # return a

        for i in range(len(c)//2):
            c[i], c[len(c)-1-i] = c[len(c)-1-i], c[i]

    # print(reverseList(b))
    reverseList(b)
    print(b)

    #  0  1  2
    # [1, 5, 9]
    print('-'*50)

    print(b)

    for i in b:             # range, list --> iterable
        print(i, end=' ')
    print()

    print(type(range(5)), type(b))

    for i in reversed(b):
        print(i, end=' ')
    print()

    for i in reversed(range(len(b))):
        print(b[i], end=' ')
    print()

    for i in enumerate(b):
        print(i, i[0], i[1])
    print()

    for i, v in enumerate(b):
        print(i, v)
    print()

    # tuple은 list의 상수 버전.
    # t = (1, 2, 3)
    # t[0] = 99

    t1, t2 = 1, 2
    print(t1, t2)

    t3 = 1, 2
    print(t3)

    # t4, t5 = 1
    # print(t4, t5)
    print('-'*50)

    a = list(range(0, 10, 2))
    print(a)

    b = a               # shallow copy(얕은 복사)
    c = a.copy()        # deep copy(깊은 복사)
    a[0] = 99
    print(a)
    print(b)
    print(c)
    print('-'*50)

    print(a[0])
    print(a[-1], a[len(a)-1])
    print(a[-2], a[-len(a)])














    print('\n\n\n\n\n\n\n\n\n\n')

# __main__ : 내가 첫 번째 실행한 파일
# Day_02_02_list : 다른 파일에서 나를 import 했을 때
print(__name__)











