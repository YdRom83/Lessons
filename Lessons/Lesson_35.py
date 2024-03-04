# -----------------------------------------------------------------------------#
from functools import wraps


#
# def log_decorator(func):
#     @wraps(func)
#     def wrapper():
#         print(f'Call  function: {func.__name__}')
#         func()
#
#     return wrapper
#
#
# @log_decorator
# def hello_world():
#     print('Hello world')
#
#
# hello_world()
#
# print(f'Function: {hello_world.__name__}')

# ----------------------------------------------------------------------------#
# def log_decorator(func):
#     @wraps(func)
#     def wrapper():
#         print(f'Вызов функции: {func.__name__}')
#         func()
#
#     return wrapper
#
#
# @log_decorator
# def hello_world():
#     print("Hello, world!")
#
#
# print(hello_world.__name__)
# ----------------------------------------------------------------------------#
# def type_check(*types):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             if len(args) != len(types):
#                 raise TypeError(f'Expected {len(types)} arguments, but got {len(args)}')
#
#             for arg, t in zip(args, types):
#                 if not isinstance(arg, t):
#                     raise TypeError(f'Expected {t} but got {type(arg)}')
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @type_check(int, str)
# def example_func(num, text):
#     return f'Number {num}, Text: {text}'
#
# try:
#     print(example_func(10, 'Hello'))
#     print(example_func("10", 'Hello'))
# except TypeError as e:
#     print(f'TypeError: {e}')

# ----------------------------------------------------------------------------#

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Decorator is working')
#         for key, value in kwargs.items():
#             print(f'{key}: {value}')
#         res = func(*args, **kwargs)
#         return res
#
#     return wrapper
#
#
# @my_decorator
# def greeting(name, age, location):
#     print(f'Hello my name is {name}, im old {age} and i from {location}')
#
#
# greeting(name='Alice', age=30, location='New York')

# ----------------------------------------------------------------------------#

# def black_hole(*args):
#     print(type(args))
#     for argument in args:
#         print(argument)
#
#
# black_hole(0, 5, 6, "Name", 'address', 2 * 5)

# def black_hole(**kwargs):
#     print(type(kwargs))
#     for argument in kwargs:
#         print(argument)
#
#
# black_hole(name='NIck', planet='Earth', galaxy='Milky Way', age=1300000)

# ----------------------------------------------------------------------------#
# class Authenticator:
#     logger_in = False
#
#     @classmethod
#     def login(cls, username, password):
#         if username == 'admin' and password == 'password':
#             cls.logger_in = True
#
#     @classmethod
#     def logout(cls):
#         cls.logger_in = False
#
#     @staticmethod
#     def is_logged_in():
#         return Authenticator.logger_in
#
#
# def login_required(func):
#     def wrapper(*args, **kwargs):
#         if Authenticator.is_logged_in():
#             return func(*args, **kwargs)
#         else:
#             print('You must be logged in to access this function.')
#
#     return wrapper
#
#
# @login_required
# def secret_function():
#     print('This is a secret function.')
#
#
# Authenticator.login('admin', 'password')
# secret_function()
#
# Authenticator.logout()
# secret_function()

# ----------------------------------------------------------------------------#

def add_property(cls):
    def wrapper(*args, **kwargs):
        if not hasattr(cls, 'additional_property'):
            cls.additional_property = 'This is an additional property'
        return cls(*args, **kwargs)

    return wrapper


class ClassA:
    def __init__(self):
        print('ClassA constructor called')

    def method_a(self):
        print('Method A called')


class ClassB:
    def __init__(self):
        print('ClassB constructor called')

    def method_b(self):
        print('Method B called')


@add_property
class MyNewClass(ClassA, ClassB):
    def __init__(self):
        super().__init__()
        print("MyNewClass constructor called")


obj = MyNewClass()
# obj.method_a()
# obj.method_b()
print(obj.additional_property)
