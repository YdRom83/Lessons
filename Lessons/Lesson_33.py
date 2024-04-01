
# ----------------------------------------------------------------------------#
# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError('Делить на 0 нельзя!!!')
#     return a / b


# try:
#     result = divide(10, 0)
# except ZeroDivisionError as e:
#     print(e)

# ----------------------------------------------------------------------------#
# class CustomError(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#
#
# def func():
#     raise CustomError('Это пользовательское исключение!!!')
#
#
# try:
#     func()
# except CustomError as e:
#     print(e)

# ----------------------------------------------------------------------------#

# class CustomError(Exception):
#     def __init__(self, message):
#         self.message = message
#
#
# class Calculate:
#     def divide(self, a, b):
#         if b == 0:
#             raise CustomError('DIVIDED BY ZERO!!!')
#         return a / b
#
#
# calc = Calculate()
#
# try:
#     res = calc.divide(10, 0)
# except CustomError as e:
#     print(e)
# # ----------------------------------------------------------------------------#
# class CustomError(Exception):
#     def __init__(self, message):
#         self.message = message
#
#
# class Mult:
#
#     def mult_num(self, a, b):
#         if isinstance(a, str) or isinstance(b, str):
#             raise CustomError('Числа не должны быть строками!!!')
#         return a * b
#
#
# m = Mult()
# try:
#     m.mult_num('0', 5)
# except CustomError as e:
#     print(e)

# # ----------------------------------------------------------------------------#

#                               Декораторы
# # ----------------------------------------------------------------------------#

# def decorator(func):
#     def wrapper():
#         print('Функция оболочка')
#         func()
#
#     return wrapper
#
#
# def basic():
#     print('Основная функция')
#
#
# wrapped = decorator(basic)
# print('start program')
# basic()
# wrapped()
# print('finish program')
# # ----------------------------------------------------------------------------#

# def decorator(func):
#     '''Основная функция'''
#     print('Декоратор')
#
#     def wrapper():
#         print('--до функции', func.__name__)
#         func()
#         print('--после функции', func.__name__)
#
#     return wrapper
#
#
# @decorator
# def wrapped():
#     print('--обернутая функция')
#
#
# print('-старт программы...')
# wrapped()
# print('-конец функции...')

# # ----------------------------------------------------------------------------#

# def decorator_1(func):
#     print('Декоратор 1')

#     def wrapper():
#         print('перед функцией 1')
#         func()

#     return wrapper


# def decorator_2(func):
#     print('Декоратор 2')

#     def wrapper():
#         print('перед функцией 2')
#         func()

#     return wrapper


# @decorator_1
# @decorator_2
# def basic_1():
#     print('basic_1')


# # @decorator_1
# # def basic_2():
# #     print('basic_2')

# print('>> start')
# basic_1()
# # basic_2()
# print('>> finish')
# # ----------------------------------------------------------------------------#
# Задание 1 и Задание 2
# Создайтефункциюдляотображениятекущеговремени.
# Функция не принимает параметров. Функция не исполь-
# зуя синтаксис декораторов, произведите декорирование
# функции с помощью другой функции. Потенциальный
# вывод данных на экран:
# ***************************
# 23:00
# ***************************
# В этом выводе на экран две линии из звездочек – ре-
# зультаты декорирования

# from datetime import datetime


# def decorator(fn):
#     def wrapper():
#         print('***************************')
#         fn()
#         print('***************************')
#     return wrapper


# def decorator_2(fn):
#     def wrapper():
#         fn()
#         current_time = datetime.now()
#         print(current_time.strftime('%Y-%m-%d'))
#     return wrapper


# @decorator
# @decorator_2
# def show_time():
#     current_time = datetime.now()
#     time = current_time.strftime('%H:%M:%S')
#     print(time)


# show_time()


# # ----------------------------------------------------------------------------#
# Задание 4
# Создайте приложение по выпечке пиццы. Каждая
# пицца содержит разные компоненты. Используя механизм
# декораторов создайте разные пиццы:
# ■ Маргарита;
# ■ Четыре сыра;
# ■ Капричоза;
# ■ Гавайская.

def pizza_margherita(fn):
    def wrapper():
        fn('Маргарита')
        print('сыр, помидоры')
    return wrapper


def pizza_four_cheese(fn):
    def wrapper():
        fn('Четыре сыра')
        print('моцарелла, пармезан, гауда, горгонзолла')
    return wrapper


def pizza_capricciosa(fn):
    def wrapper():
        fn('Капричоза')
        print('моцарелла, ветчина, грибы, томаты, артишоки')
    return wrapper


def pizza_hawaiian(fn):
    def wrapper():
        fn('Гавайская')
        print('куриное филе, ветчина, ананасы, моцарелла')
    return wrapper


@pizza_four_cheese
# @pizza_margherita
# @pizza_capricciosa
# @pizza_hawaiian
def pizza(name):
    print(f'Пицца {name} содержит: тесто, кетчуп, ', end='')


pizza()

# ----------------------------------------------------------------------------#
# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError('Делить на 0 нельзя!!!')
#     return a / b


# try:
#     result = divide(10, 0)
# except ZeroDivisionError as e:
#     print(e)

# ----------------------------------------------------------------------------#
# class CustomError(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#
#
# def func():
#     raise CustomError('Это пользовательское исключение!!!')
#
#
# try:
#     func()
# except CustomError as e:
#     print(e)

# ----------------------------------------------------------------------------#

# class CustomError(Exception):
#     def __init__(self, message):
#         self.message = message
#
#
# class Calculate:
#     def divide(self, a, b):
#         if b == 0:
#             raise CustomError('DIVIDED BY ZERO!!!')
#         return a / b
#
#
# calc = Calculate()
#
# try:
#     res = calc.divide(10, 0)
# except CustomError as e:
#     print(e)
# # ----------------------------------------------------------------------------#
# class CustomError(Exception):
#     def __init__(self, message):
#         self.message = message
#
#
# class Mult:
#
#     def mult_num(self, a, b):
#         if isinstance(a, str) or isinstance(b, str):
#             raise CustomError('Числа не должны быть строками!!!')
#         return a * b
#
#
# m = Mult()
# try:
#     m.mult_num('0', 5)
# except CustomError as e:
#     print(e)

# # ----------------------------------------------------------------------------#

#                               Декораторы
# # ----------------------------------------------------------------------------#

# def decorator(func):
#     def wrapper():
#         print('Функция оболочка')
#         func()
#
#     return wrapper
#
#
# def basic():
#     print('Основная функция')
#
#
# wrapped = decorator(basic)
# print('start program')
# basic()
# wrapped()
# print('finish program')
# # ----------------------------------------------------------------------------#

# def decorator(func):
#     '''Основная функция'''
#     print('Декоратор')
#
#     def wrapper():
#         print('--до функции', func.__name__)
#         func()
#         print('--после функции', func.__name__)
#
#     return wrapper
#
#
# @decorator
# def wrapped():
#     print('--обернутая функция')
#
#
# print('-старт программы...')
# wrapped()
# print('-конец функции...')

# # ----------------------------------------------------------------------------#

def decorator_1(func):
    print('Декоратор 1')

    def wrapper():
        print('перед функцией 1')
        func()

    return wrapper


def decorator_2(func):
    print('Декоратор 2')

    def wrapper():
        print('перед функцией 2')
        func()

    return wrapper


@decorator_1
@decorator_2
def basic_1():
    print('basic_1')


# @decorator_1
# def basic_2():
#     print('basic_2')

print('>> start')
basic_1()
# basic_2()
print('>> finish')

