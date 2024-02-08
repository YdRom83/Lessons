# def get_name(name='Ivan'):
#     print(name)

# get_name()
# get_name('Peter')

# class Car:
#     def __init__(self, speed, color='Yellow', owner=None) -> None:
#         self.speed = speed
#         self.color = color
#         self.owner = owner

#     def say_owner(self):
#         if self.owner:
#             print(f'Владелец {self.owner}')
#         else:
#             print('Нет владельца.')


# car1 = Car(100,  None, 'Ivan')
# print(car1.color)
# car2 = Car(90, 'Blue')
# car1.say_owner()
# car2.say_owner()
# print(f'{car1.color}')
# print(f'{car2.color}')


# class Person:
#     _age = 15
#     def __say_hello():
#         print('Hello')
# person1 = Person
# # print(person1._age)
# # person1._age = 14
# # print(person1._age)
# person1._Person__say_hello()


# class MyClass:
#     def __init__(self, name) -> None:
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         self._name = value


# a = MyClass('Ivan')
# a.name = 'sergey'
# print(a.name)


# class Animales:
#     def __init__(self, color, kind_of_animal) -> None:
#         self._color = color
#         self.caws = kind_of_animal

#     @property
#     def _bits(self):
#         return 'Bits you'


# a = Animales('yellow', 'tiger')
# print(a._color)
# print(a._bits)


# class Parent:

#     def say_hello():
#         print("I'm parent")


# class Children(Parent):

#     def say_hello():
#         print("I'm daughter classes")

# c = Children
# c.say_hello()


# class Test(list):
    
#     def append(self, object) -> None:
#         for i in range(len(self)):
#             self[i] **= object
            
# a = Test([1, 2, 3])
# print(a)
# a.append(4)
# print(a)


class Test(int):
    
    def __init__(self, num) -> None:
        super().__init__()
        self.num = num
        
    def __add__(self, num2) -> int:
        return self.num * num2

a = Test(5)
print(a + 100)