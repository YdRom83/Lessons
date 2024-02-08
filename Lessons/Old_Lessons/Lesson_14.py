#                                 Lambda
# ----------------------------------------------------------------------------#

# two = lambda: 2
# sqr = lambda x: x * x
# pwr = lambda x, y: x ** y
# print(two())
# print(sqr(2))
# print(pwr(5, 3))
#
#
# for a in range(-2, 3):
#     print(sqr(a), end=' ')
#     print(pwr(a, two()))


# def printfun(args, fun):
#     for x in args:
#         print('f(', x, ')=', fun(x), sep='')
#
# def poly(x):
#     return 2 * x ** 2 - 4 * x + 2
#
# printfun([x for x in range(1, 3)], poly)


# def printfun(args, fun):
#     for x in args:
#         print('f(', x,')=', fun(x), sep='')
# printfun([x for x in range(2, 3)], lambda x: 2 * x ** 2 - 4 * x+2 )


# is_even = lambda x: x % 2 == 0
# print(is_even(6))
# print(is_even(5))

#                                 Map
# ----------------------------------------------------------------------------#

# list1 = [x for x in range(5)]
# list2 = list(map(lambda x: 2 ** x, list1))
# print(list2)
#
# for x in map(lambda x: x * x, list2):
#     print(x, end=' ')
# print()

# numbers = [1, 2, 4, 5, 6, 435, 77, 54]
# doubted = list(map(lambda x: x + 2, numbers))
# print(doubted)

# def umn2(x):
#     return x * 2
#
# doubted = list(map(umn2, numbers))
# print(doubted)


#                                 Filter
# ----------------------------------------------------------------------------#
# num = [1, 2, 4, 5, 56, 77, 66, 88]
# even_num = list(filter(lambda x: x % 2 == 0, num))
# print(even_num)
#
#
# words = ['apple54', 'banana65', 'cherry', 'lemon']
# long_words = list(filter(lambda x: len(x) > 5, words))
# print(long_words)


# from random import  randint
#
# data = [randint(-10, 10) for x in range(5)]
# filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
# print(data)
# print(filtered)


#                                 Замыкание
# ----------------------------------------------------------------------------#

# def outer(par):
#     loc = par
#
#     def inner():
#         return loc
#
#     return inner
#
#
# var = 5
# fun = outer(var)
# print(fun())


# def makeclosure(par):
#     loc = par
#
#     def power(p):
#         return p ** loc
#
#     return power
#
#
# fsqr = makeclosure(2)
# fcub = makeclosure(3)
# for i in range(5):
#     print(i, fsqr(i), fcub(i))


def filter_long_words(words):
    return list(filter(lambda x: len(x) > 5, words))


words_list = ['apple', 'banana', 'strawberry', 'lemon']

filtered = filter_long_words(words_list)
print(filtered)
