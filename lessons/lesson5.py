#множественное наследование

class A:
    def __init__(self, name, balance, pin, svv):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.svv = svv

    def a(self):
        print('метод класса А')


class B(A):
    def a(self):
        print('метод класса В')


class C:
    def __init__(self,key):
        self.key = key

    def a(self):
        print('метод С')

# MRO - порядок выполнения методов
class D(B,C):
    def __init__(self, name, balance, pin, svv,key):
        A.__init__(self,name, balance, pin, svv)
        C.__init__(self,key)

    def A(self):
        print('метод D')

print(dir(D))

d=D('beka',10000,10000,10000,'qwertydfghj')
print(dir(d))
d.a()

print(D.mro())