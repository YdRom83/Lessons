import turtle
from turtle import *


# turtle.shape('turtle')
# def make_square():
#     for  i in range(4):
#         turtle.forward(100)
#         turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.done()

# def MyFunction():
#     print('Привет')
#
# MyFunction()

# def make_triangle():
#     turtle.forward(150)
#     turtle.left(120)
#     turtle.forward(150)
#     turtle.left(120)
#     turtle.forward(150)
#
#     for  i in range(4):
#         turtle.forward(100)
#         turtle.left(90)
# make_triangle()
# make_square()

# from math import sin, pi
# print(sin(pi/2))

# def MyFunction_1(fname, lname):
#     print(fname, lname, ' Student')
#
#
# MyFunction_1('Anna', 'Ivanova')

# def square(num):
#     return num**2
# print(square(4))

# import math
# for name in dir(math):
#     print(name, end=" ")

# from math import ceil, floor, trunc
# x = 1.4
# y = 2.6
# print(floor(x), floor(y))
# print(floor(-x), floor(-y))
# print(ceil(x), ceil(y))
# print(ceil(-x), ceil(-y))
# print(trunc(x), trunc(y))      # trunc убирает дробную часть
# print(trunc(-x), trunc(-y))

# from random import random, seed
# # for name in dir(random):
# #     print(name)
#
# seed(20)
# for i in range(5):
#     print(random())
# import random
#
# for i in range(5):
#
#     # Any number can be used in place of '11'.
#     random.seed(15)      # seed генерирует одно и тоже число
#
#     # Generated random number will be between 1 to 1000.
#     print(random.randint(1, 1000))


from random import randrange, randint, choice, sample

# print(randrange(1), end=' ')
# print(randrange(0, 1), end=' ')
# print(randrange(0, 1, 1), end=' ')
# print(randint(0, 1))

from random import randint
# for i in range(10):
#     print(randint(1, 10), end=',')

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(choice(lst))
# print(sample(lst, 5))
# print(sample(lst, 10))
# a = randint(1, 6)
# count = 0
# # for _ in range(a):
# if a == 1:
#        print('Промах')
# elif  a == 2:
#         print('Промах')
# if  a == 3:
#       count += 1
#       print('Убит')
# elif  a == 4:
#         print('Промах')
# elif  a == 5:
#         print('Промах')
# elif  a == 6:
#        print('Промах')
# print('Убит ', count, 'раз')