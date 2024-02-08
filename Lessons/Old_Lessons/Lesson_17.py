# ----------------------------------------------------------------------------#
# str1 = 'sadfewfasf'
# t = 's'
#
# print(t in str1)
# print(t not in str1)


#                              Линейный поиск
# ----------------------------------------------------------------------------#
# Линейный поиск - Проверяет все элементы по порядку
# def LinearSearch(lys, element):
#     for i in range(len(lys)):
#         if lys[i] == element:
#             return 'Element finded!'
#     return 'Element not finded!'
#
#
# print(LinearSearch([1, 2, 3, 4, 5], 1))


#                              Бинарный поиск
# ----------------------------------------------------------------------------#
# Бинарный поиск - Делет список по полам и проверяет элемент больше или меньше искомого.
# Массив должнен быть ОТСОРТИРОВАН!

# def BinarySearch(lys, val):
#     first = 0
#     last = len(lys) - 1
#     index = -1
#     while (first <= last) and (index == -1):
#         mid = (first + last) // 2
#         if lys[mid] == val:
#             index = mid
#         else:
#             if val < lys[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return lys[index]
#
#
# print(BinarySearch([1, 2, 3, 4, 55, 67, 777], 777))
# print(BinarySearch([2342, 45, 1, 2, 3, 4, 55, 67, 777], 4))
# arr = [23423, 2342, 45, 1, 2, 3, 4, 55, 67, 777]
# print(sorted(arr))
#
# print(BinarySearch(sorted(arr), 2))


#                              Jump Search
# ----------------------------------------------------------------------------#

# import math
#
#
# def JumpSearch(lys, val):
#     length = len(lys)
#     jump = int(math.sqrt(length))
#     left, right = 0, 0
#     while left < length and lys[left] <= val:
#         right = min(length - 1, left + jump)
#         if lys[left] <= val and lys[right] >= val:
#             break
#         left += jump
#     if left >= length or lys[left] > val:
#         return -1
#     right = min(length - 1, right)
#     i = left
#     while i <= right and lys[i] <= val:
#         if lys[i] == val:
#             return i
#         i += 1
#     return -1
#
#
# print(JumpSearch([1, 2, 3, 4, 55, 67, 777], 3))


#                                 Множества
# ----------------------------------------------------------------------------#
# Множества - Изменяемый тип данных, все элементы УНИКАЛЬНЫ. Но все эл. хранятся впроизвольном порядке

# our_set = set()  # 1-й способ создания
# our_set_2 = {92}  # 2-й способ создания
#
# our_set.add('Tomato')  # ADD - добавляет значение в множества
# our_set.add('Apple')
# our_set.add(2)
#
# our_set_2.add('Tomato')  # ADD - добавляет значение в множества
#
# our_set_2.add('Word')
# our_set_2.add('Work')
# our_set_2.add('May')
# x = 'Tomato'
# print(x in our_set)
# print(x in our_set_2)
# print(our_set)
# print(our_set_2)
#
# print(our_set.isdisjoint(our_set_2))  # isdisjoint - проверяет 2 множества на наличие совпадений элементов.
#
# our_set_3 = our_set.union(our_set_2)  # union - Объединяет эл. из других множеств.
# print(our_set_3)
#
# our_set.update(our_set_2)  # update - Объединяет эл. из других множеств.
# print(our_set)
#
#
# print(our_set_2.issubset(our_set_3))
#
# print(our_set_3.issuperset(our_set_2)) # issuperset()  проверяет, принадлежит ли множество внутри скобок

# our_products = {"Apple", "Tesla", "McDonald's"}
# range_of_the_company_1 = {"Samsung", "Sony"}
# range_of_the_company_2 = {"Apple", "IBM", "Tesla"}
# range_of_the_company_3 = {"BMW", "Tesla", "Ferrari"}
#
# print(our_products.intersection(range_of_the_company_1))  # intersection - ищет нужные нам совпадения(our_products)
#
# print(our_products.intersection(range_of_the_company_2))
# print(our_products.intersection(range_of_the_company_3))

# our_products = {"Apple", "Tesla", "McDonald's"}
# range_of_the_company_1 = {"Samsung", "Sony"}
# range_of_the_company_2 = {"Apple", "IBM", "Tesla"}
# range_of_the_company_3 = {"BMW", "Tesla", "Ferrari"}
# print(our_products.difference(range_of_the_company_1))  #  difference - Показывает чего не хватает из нащего списка (our_products)
# print(our_products.difference(range_of_the_company_2))
# print(our_products.difference(range_of_the_company_3))


# our_products = {"Apple", "Tesla", "McDonald's"}
# range_of_the_company_2 = {"Apple", "IBM", "Tesla"}
# print(our_products.symmetric_difference(range_of_the_company_2))  # symmetric_difference - Исключает общии элементы
# print(our_products)
# our_products.intersection_update(range_of_the_company_2)
# print(our_products)

# our_products.difference_update(range_of_the_company_2)  # symmetric_difference - Исключает общии элементы
# print(our_products)

# our_products.symmetric_difference_update(range_of_the_company_2)
# print(our_products)


# our_products = {"Apple", "Tesla", "McDonald's"}
# our_products.discard('Apple')  # discard - удаляет элемент
# our_products.remove('Tesla')     # Remove - удаляет элемен
# print(our_products)

my_frozenset = frozenset()
print(type(my_frozenset))
my_tuple = tuple()
print(type(my_tuple))
my_tuple_2 = (0,)
print(type(my_tuple_2))
my_tuple_3 = 0,
print(type(my_tuple_3))
my_tuple_4 = (0)
print(type(my_tuple_4))