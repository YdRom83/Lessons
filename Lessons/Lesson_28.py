# ----------------------------------------------------------------------------#
# import random
# import string
#
#
# def generate_password(num):
#     user_password = ''.join(random.sample(string.ascii_letters + string.digits, num))
#     return user_password
#
#
# print(generate_password(15))
# def gen_pass(n):
#     letters = 'asdfghjkklzxcvbnmqertyuuiopZXCVBNMASDFGHJKLQWERTYUIOP'
#     digits = '1234567890'
#     all_chars = letters + digits
#     res = ''.join(random.choice(all_chars) for _ in range(n))
#     return res

# print(gen_pass(8))

# ----------------------------------------------------------------------------#

# def count_words(words):
#     res = words.split()
#     return len(res)
#
#
# print(count_words('hello some world'))
# ----------------------------------------------------------------------------#

# def simple_num(n):
#
#     for i in range(2, n+1):
#         if n % i == 0 and i != n:
#             return False
#     return True
#
# print(simple_num(5))
# ----------------------------------------------------------------------------#

# def generate_simple_nums(num):
#     for i in range(2, num):
#         for j in range(2, int(num**0.5) + 1):
#             if i % j == 0 and i != j:
#                 break
#         else:
#             print(i)

# generate_simple_nums(10)
# ----------------------------------------------------------------------------#


# def multy_table(n):
#      for i in range(1, n+1):
#          print(f'{i} x {n} = {i * n}')
#
# print(multy_table(5))

# ----------------------------------------------------------------------------#
# def split_str(my_str, n):
#     for i in range(n):
#         print(my_str[i])
#
# split_str('hello', 3)

# ----------------------------------------------------------------------------#
# def same_str(str1 , str2):
#     set1 = set(str1)
#     set2 = set(str2)
#     if set1 == set2:
#         print('Анаграмма')
#     else:
#         print('Не анаграмма')
#
# same_str('hello', 'hello2')

# ----------------------------------------------------------------------------#


# n = 11
# for i in range(2, n+1):
#     if n % i == 0 and n == i:
#         print(i)

# ----------------------------------------------------------------------------#
# import math
#
#
# class Circle:
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def square_circle(self):
#         return math.pi * self.radius ** 2
#
#     def lenght_circle(self):
#         return 2 * math.pi * self.radius
#
# c = Circle(5)
#
# print(c.square_circle())
# print(c.lenght_circle())

# ----------------------------------------------------------------------------#

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print(f'Имя: {self.name}. Возраст: {self.age}')


# class Employee(Person):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary

#     def display_salary(self):
#         print(f'Зарплата: {self.salary} Имя: {self.name} Возраст {self.age}')


# p = Person('Ivan', 56)
# p.display_info()
# e = Employee('ivan', 56, 896)
# print(e.age)

# e.display_salary()
# ----------------------------------------------------------------------------#
# import math

# class Shape:


#     def area(self):
#         pass


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2


# class Triangle:
#     def __init__(self, height, a):
#         self.height = height
#         self.a = a

#     def area(self):
#         return 1 / 2 * self.a * self.height


# c = Circle(5)
# print(c.area())
# r = Triangle(5, 5)
# print(r.area())
# ----------------------------------------------------------------------------#

class Car:
    def __init__(self, brand, model, speed) -> None:
        self._brand = brand
        self._model = model
        self._speed = speed

    def set_brand(self, brand):
        self._brand = brand

    def set_model(self, model):
        self._model = model

    def set_speed(self, speed):
        self._speed = speed

    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

    def get_speed(self):
        return self._speed


c = Car('BMW', 'M3', 170)
c.set_model('X6')
c.set_speed(200)
print(c.get_model())
print(c.get_speed())
