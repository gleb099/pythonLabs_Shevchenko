class Person:

    def __init__(self, name):
        self.__name = name  # имя человека

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name} ")


class Employee(Person):

    def work(self):
        print(f"{self.name} works")


tom = Employee("Tom")
print(tom.name)  # Tom
tom.display_info()  # Name: Tom
tom.work()  # Tom works