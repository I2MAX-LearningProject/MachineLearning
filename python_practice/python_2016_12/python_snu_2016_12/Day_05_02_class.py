# Day_05_02_class.py

class Info:
    def __init__(self, age):
        print('c-tor')
        self.age = age

    def show(self):
        print('show', self.age)

    @property
    def myAge(self):
        return self.age + 100


i1 = Info(10)
i2 = Info(20)
print(i1)

Info.show(i1)   # unbound method
i1.show()       #   bound method
i2.show()

print('age :', i1.age)
# print('my age :', i1.myAge())
print('my age :', i1.myAge)
# i1.myAge = 30








print('\n\n\n\n\n\n\n\n\n\n')