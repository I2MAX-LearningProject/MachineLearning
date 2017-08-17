# Day_03_06_function.py

def not_used():
    def f_1(a, b, c):
        print(a, b, c)

    f_1(1, 2, 3)            # position argument
    f_1(a=1, b=2, c=3)      # keyword argument
    f_1(b=2, c=3, a=1)
    f_1(1, b=2, c=3)
    # f_1(a=1, 2, c=3)        # position은 keyword 앞에.


    def f_2(a=0, b=0, c=0):     # default parameter
        print(a, b, c, sep='**')

    f_2(1, 2, 3)
    f_2()
    f_2(1)
    f_2(1, 2)
    f_2(a=1, b=2, c=3)
    f_2(c=3)


    def f_3(*args):         # 가변인자
        print(args)
        print(*args)        # unpack

    f_3()
    f_3(1)
    f_3(1, 2)
    f_3(1, 2, 3)            # pack

    # t1 = (1)
    # t2 = (1,)
    # print(type(t1), type(t2))

    a = ['hello', 'python', 'welcome']
    print(a)
    print(*a)
    print(*a, sep='\n')

def f_5(**kwargs):
    f_4(d=kwargs)
    f_4(**kwargs)       # unpack

def f_4(**kwargs):      # keyword argument
    print(kwargs)

# f_4(1, 2, 3)          # error.
f_4(a=1, b=2, c=3)
f_5(a=1, b=2, c=3)
