#                                Генераторы
# ----------------------------------------------------------------------------#

# st =[324, 456, 34,234]
#
# print(next(st))
# print(next(st))
# print(next(st))

# Фибонначи

# class Fib:
#     def __init__(self, nn):
#         print("__init__")
#         self.__n = nn
#         self.__i = 0
#         self.__p1 = self.__p2 = 1
#
#     def __iter__(self):
#         print("__iter__")
#         return self
#
#     def __next__(self):
#         print("__next__")
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2, ret
#         return ret
#
# for i in Fib(10):
#     print(i)

# def fun(n):
#     for i in range(n):
#         return i
# print(fun(5))

# ----------------------------------------------------------------------------#

# def fruit_generate():
#     # Создадим итератор при помощи генератора.
#     for item in ['apple', 'banana', 'cherry']:
#         yield item
#
# fruit = fruit_generate()
#
# print(next(fruit))
# # apple
# print(next(fruit))
# # # banana
# print(next(fruit))
# ----------------------------------------------------------------------------#

# st =[324, 456, 34,234]
#
# def list_yield(arr):
#     for i in arr:
#         yield i
# lst = list_yield(st)
# print(next(lst))
# print(next(lst))
# print(next(lst))
# print(next(lst))
# ----------------------------------------------------------------------------#


# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
#
# seq = infinite_sequence()
# for i in range(15):
#     print(next(seq))

# ----------------------------------------------------------------------------#

# def filter_num(nums):
#     for num in nums:
#         if num % 2 == 0:
#             yield num
#
# even_nums = filter_num([1, 3, 43, 34, 44, 342, 444])
# for num in even_nums:
#     print(num)

# lst = [1, 3, 43, 34, 44, 342, 444]
# def even_num(l):
#     res = []
#     for i in l:
#         if i % 2 == 0:
#             res += i
#     return  res
# ----------------------------------------------------------------------------#

# def fibonacci(n):
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
# fib = fibonacci(5)
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# ----------------------------------------------------------------------------#

# nums = [1, 23, 34, 44]

# def doubl(nums):
#     count = []
#     for num in nums:
#         count.append(num * 2)
#     return count
# print(doubl(nums))
#
# d = doubl(nums)
# for i in d:
#     print(i)

# def doub(nums):
#     for num in nums:
#         yield num * 2
#
# doubs_nums = doub(nums)
# print(next(doubs_nums))               # yield - выводит значение которое нужно, а не весь список
# print(next(doubs_nums))

# ----------------------------------------------------------------------------#

# def fun(n):
#     for i in range(n):
#         yield i
#
#
# for v in fun(5):
#     print(v)

# ----------------------------------------------------------------------------#

# def powersOf2(n):
#     pow = 1
#     for i in range(n):
#         yield pow
#         pow *= 2
#
#
# t = [x for x in powersOf2(5)]
# print(t)


# def powersOf2(n):
#      pow = 1
#      for i in range(n):
#         yield pow
#         pow *= 2
# for i in range(20):
#     if i in powersOf2(4):
#         print(i)

# Фибонначи
# ----------------------------------------------------------------------------#
# def Fib(n):
#     p = pp = 1
#     for i in range(n):
#         if i in [0, 1]:
#             yield 1
#         else:
#             n = p + pp
#             pp, p = p, n
#             yield n
#
#
# fibs = list(Fib(10))
# print(fibs)


# ----------------------------------------------------------------------------#

# listOne = []
# # Option 1
# for ex in range(6):
#     listOne.append(10**ex)
#
# # Option 2
# listTwo = [10 ** ex for ex in range(6)]
#
# print(listOne)
# print(listTwo)

# ----------------------------------------------------------------------------#

# lst = []
# # Option 1
#
# for x in range(10):
#     lst.append(1 if x % 2 == 0 else 0)
# print(lst)
#
# # # Option 2
# lst = [1 if x % 2 == 0 else 0 for x in range(10)]
# print(lst)

# ----------------------------------------------------------------------------#
# Option 1
for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end='')
print()
# Option 2
for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end='')
print()