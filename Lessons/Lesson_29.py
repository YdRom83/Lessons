# ----------------------------------------------------------------------------#
# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя,
# объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ
# к отдельным полям через методы класса


# class Car:
#     def __init__(self):
#         self.model = ''
#         self.year = ''
#         self.brand = ''
#         self.value = ''
#         self.color = ''
#         self.price = ''
#
#     def get_model(self):
#         self.model = input('Enter a brand: ')
#
#     def get_year(self):
#         self.year = input('Enter year: ')
#
#     def get_brand(self):
#         self.year = input('Enter brand: ')
#
#     def get_value(self):
#         self.year = input('Enter value: ')
#
#     def get_color(self):
#         self.color = input('Enter color: ')
#
#     def get_price(self):
#         self.price = int(input('Enter price: '))
#
#     def show_model(self):
#         print(self.model)
#
#     def show_year(self):
#         print(self.year)
#
#     def show_brand(self):
#         print(self.brand)
#
#     def show_value(self):
#         print(self.value)
#
#     def show_color(self):
#         print(self.color)
#
#     def show_price(self):
#         print(self.price)
#
#
# c = Car()
# c.get_model()
# c.get_year()
# c.get_color()
# c.show_model()
# c.show_year()
# c.show_color()

# ----------------------------------------------------------------------------#

# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

# class Book:
#     def __init__(self):
#         self.name = ''
#         self.year = ''
#         self.publisher = ''
#         self.genre = ''
#         self.__author = ''
#         self.price = ''
#
#     def get_author(self):
#         self.__author = input('Enter author: ')
#
#     def get_name(self):
#         self.name = input('Enter name: ')
#
#     def get_year(self):
#         self.year = input('Enter year: ')
#
#     def get_publisher(self):
#         self.publisher = input('Enter publisher: ')
#
#     def get_genre(self):
#         self.genre = input('Enter genre: ')
#
#     def get_price(self):
#         self.price = input('Enter price: ')
#
#     def show_author(self):
#         print(self.__author)
#
#     def show_name(self):
#         print(self.name)
#
#     def show_year(self):
#         print(self.year)
#
#     def show_publisher(self):
#         print(self.publisher)
#
#     def show_price(self):
#         print(self.price)
#
#
# b = Book()
# b.get_author()
# b.show_author()
# b.get_name()
# b.show_name()

# ----------------------------------------------------------------------------#


# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса

# class Stadium:
#     def __init__(self):
#         self.name = ''
#         self.year = ''
#         self.city = ''
#         self.volume = ''
#
#     def get_name(self):
#         self.name = input('Enter name: ')
#
#     def get_year(self):
#         self.year = input('Enter year')

# ----------------------------------------------------------------------------#
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#
# person = Person('Alice', 30)
# print(person.get_name())
# person.set_name('Bob')
# print(person.get_name())
# ----------------------------------------------------------------------------#
# class Calculator:
#     def __init__(self):
#         pass
#
#     def __add(self, a, b):
#         return a + b
#
#     def add_numbers(self, a, b):
#         return self.__add(a, b)
#
#
# calc = Calculator()
# res = calc.add_numbers(3, 5)
# print(res)
# ----------------------------------------------------------------------------#
# class Vehicle:
#     def __init__(self, brand):
#         self._brand = brand
#
#
# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model
#
#
# car = Car('Toyota', 'Corolla')
# print(car._brand)
# ----------------------------------------------------------------------------#
# class MyClass:
#     def __init__(self, name) -> None:
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value
#
#
# a = MyClass('Ivan')
# a.name = 'sergey'
# print(a.name)

# ----------------------------------------------------------------------------#
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print(Calculator.add(5, 4))
print(Calculator.multiply(5, 4))
