<<<<<<< HEAD
# # ----------------------------------------------------------------------------#
=======
# # ----------------------------------------------------------------------------#
# def my_decorator(func):
#     def wrapper():
#         print('Before launch function')
#         func()
#         print('After launch function ')
#
#     return wrapper
#
#
# @my_decorator
# def say_hello():
#     print('Hello')
# # ----------------------------------------------------------------------------#
from random import randint
import time

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr


# def decorator(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         finish = end - start
#         print(finish)
#
#     return wrapper
#
# @decorator
# def sort_lst():
#     lst = []
#     for i in range(10000):
#         lst.append(randint(0, 100000))
#     lst = bubble_sort(lst)
#     print(lst)
#
# sort_lst()
# # ----------------------------------------------------------------------------#

# def my_decorator_with_attributes(attribute1, attribute2):
#     def decorator(fn):
#         def wrapper(*args, **kwargs):
#             print(f'Декоратор с атрибутами: {attribute1}, {attribute2}')
#             result = fn(*args, **kwargs)
#             return result
#
#         return wrapper
#
#     return decorator
#
#
# @my_decorator_with_attributes("атрибут1", 'атрибут2')
# def my_function():
#     print('Пример функции, обернутой в декоратор')


# my_function()
# # ----------------------------------------------------------------------------#
# def my_decorator_with_attributes(attribute1, attribute2):
#     def decorator(fn):
#         def wrapper(*args):
#             print(f'Декоратор с атрибутами: {attribute1}, {attribute2}')
#             result = fn(*args)
#             return result
#
#         return wrapper
#
#     return decorator
#
#
# @my_decorator_with_attributes('attr1', 'attr2')
# def my_func(*args):
#     print('Example function wrapper in decorate')
#     print(args)
#
#
# my_func('Test1', 'test2')

# # ----------------------------------------------------------------------------#

# def my_decorate(func):
#     def wrapper(*args, **kwargs):
#         wrapper.calls += 1
#         print(f'Function {func.__name__} called {wrapper.calls} once.')
#         return func(*args, **kwargs)
#
#     wrapper.calls = 0
#     return wrapper
#
#
# @my_decorate
# def say_hello(name):
#     print(f'Hello, {name}')
#
#
# say_hello('World')
# say_hello('Everyone')
# # ----------------------------------------------------------------------------#

# list1 = [i*i for i in range(1, 11) if i % 2 == 0]

# pwr = lambda x, y: x ** y

lst = [randint(1, 10000) for i in range(10000)]


def calc_time(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        end = time.time()
        print("Время: ", end - start)
        return res

    return wrapper

def stars(fn):
    def wrapper(*args, **kwargs):
        print('***************')
        res = fn(*args, **kwargs)
        return res
        print('***************')
    return wrapper
# # Сортировка Вставками
# @calc_time
# @stars
def insertion_sort(lst):
    if not isinstance(lst, list):
        raise AttributeError('Аттрибут должен быть спиком!!!')
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

    return lst
#
#
# a = 3
# print(insertion_sort(a))
#
#
# @calc_time
# @stars
def bubble_sort(arr):
    if len(arr) > 1000:
        raise AttributeError('Не должно быть БОЛЬШЕ 1000 символов!!!')
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0  and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
# print(bubble_sort(lst))
try:
    bubble_sort(lst)
except AttributeError as a:
    print(a)


# Сортировка слиянием
# @calc_time
# @calc_time
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     # Разделение массива на две половины
#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]
#
#     # Рекурсивная сортировка каждой половины
#     left_half = merge_sort(left_half)
#     right_half = merge_sort(right_half)
#
#     # Объединение отсортированных половин
#     return merge(left_half, right_half)

# @calc_time
# @stars
# def merge(left, right):
#     merged = []
#     left_index = 0
#     right_index = 0
#
#     # Слияние двух отсортированных половин
#
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] < right[right_index]:
#             merged.append(left[left_index])
#             left_index += 1
#         else:
#             merged.append(right[right_index])
#             right_index += 1
#
#     # Добавление оставшихся элементов
#     merged.extend(left[left_index:])
#     merged.extend(right[right_index:])
#     return merged
# print(merge_sort(lst))
# # ----------------------------------------------------------------------------#


>>>>>>> deaa2a33b0bc573cf77fb39ddee8945b6466c618
