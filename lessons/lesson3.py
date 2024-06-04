# принципы ООП
# 4 наследование полиморфизм
# инкапсуляция абстракция

class BigO:
    def __init__(self): ...

    def res(self):
        print('метод класса 1')


class BigO2(BigO):

    def res(self):
        print('метод класса 2 ')
        super().res()


a = BigO()
b = BigO2()
a.res()
b.res()


# уровни доступа 3
# 1 публичный  2 защищенный _  3скрытый __
class Bank(object):
    def __init__(self, name, balance, pin, svv):
        self.name = name
        self.__balance = balance
        self._pin = pin
        self.svv = svv

    def setpin(self,other,wer):
        self._pin = other
        self.__balance = wer

    def getpin(self):
        return f'{self._pin}{self.__balance}'




    def result(self):
        print(self._pin, self.svv)

    def __str__(self):
        return f'{self.name} {self.__balance}'


beka = Bank('beka', 1000, 2525, 644)
beka1 = Bank('beka', 1000, 2525, 644)
print(beka,
      beka.result())
beka.setpin(5453,10000)
print(beka.getpin())
print(beka)
# beka.result()
# print(beka)
# beka.balance = 100000
# print(beka.balance)
# beka.__balance = 100000000
# print(beka)
# beka._Bank__balance = 75
# print(dir(beka))
# print(beka)


class Person(Bank): pass


cl = Person('beka', 1000, 2525, 644)
print(dir(cl))

print(Person.mro())

