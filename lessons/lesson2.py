# принципы ооп
# Наследование Полиморфизм

# Инкапсуляция Абстракция
# git .gitignore



# супер класс \ родительский класс
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print('метод класса CAR')

    def __str__(self):
        return (f"---------\n"
                f"year:{self.year}\n"
                f"make: {self.make}\n"
                f"model: {self.model}\n"
                f"----------")

car1=Car("Ford","Ford",2020)
car2=Car("Ford","Ford",2020)
car3=Car("Ford","Ford",2020)
car4=Car("Ford","Ford",2020)
car5=Car("Ford","Ford",2020)
car6=Car("Ford","Ford",2020)
car7=Car("Ford","Ford",2020)
print(car1)
# car1.describe_car()

# DRY

# дочерний класс
#

class Car2(Car):
    pass

c=Car2('Ford','Ford',2020)
print(c)
# c.describe_car()
#полиморфизм-изменение поведения унаследованных методов

class Car3(Car2):
    def __init__(self,make,model,year,color):
        super().__init__(make,model,year)
        Car2.__init__(self,make,model,year)
        self.color = color

    def speak(self):
        print(f"I am")
    def describe_car(self):
        print('метод класса класса car3')
        super().describe_car()


    def new(self):
        self.describe_car()

    def __str__(self):
        return (f"{super().__str__()}\n"
                f"color: {self.color}\n")

c1=Car3('BMW','m5',2022,'black')
c3=Car3('BMW','m5',2022,'black')
c2=Car3('BMW','m5',2022,'black')
c4=Car3('BMW','m5',2022,'black')
# print(c1,c4,c2,c3)
# c1.describe_car()
c1.new()
