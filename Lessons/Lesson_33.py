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
