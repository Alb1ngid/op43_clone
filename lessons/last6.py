# 1 классы внутренности класса
# принципы ООП Наследование-Полиморфизм, Абстракция Инкапсуляция
# защита 3 уровня _ __


def a(b):
    print(b)


a(1232)

class A:
    def __str__(self):
        return f'выполняю роль принта {self._name,self.key,self.age} '
    def __init__(self,name,key,age):
        self._name = name
        self.key = key
        self.age = age
    def __len__(self):
        return len(self._name)

    def none(self):
        print(self._name,'ничего не умеет')

# экземпляр\обьект
p=A('John',123,23)
print(p)
print(len(p))
p.none()

po='wqegrv'

class B(A):
    def __init__(self, name, key, age,old):
        super().__init__(name, key, age)
        self.old=old
    def none(self):
        print(self._name,'умею летать')

    def __newB(self):
        print('умею бегать')
l=B('we',12,12,9876)
print(dir(l))


print(l)
print(len(l))
l.none()


class D(B):
    def none(self):
        super().none()
        A.none(self)
    def newD(self):
        super()._B__newB()

new=D('beka',12,12,9876)

new.none()
print(dir(new))
new.newD()