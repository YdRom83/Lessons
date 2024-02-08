#                                 Кортежи
# ----------------------------------------------------------------------------#
# Кортежи - не изменяемый тип данных

# num_tu = (1, 2, 3, 5 + 4, 2, 6, 3 + 4j)
# num_tu_2 = (True, False)
# num_tu_3 = ('True', 'False')
# print(num_tu)
# print(num_tu_2)
# print(num_tu_3)
#
#
# num_tuv =((1, 2),('a', 'b'))
# print(num_tuv)

# tuple_list = ([1, 2, 3], [1, 2, 3], [1, 2, 3])
# print(*tuple_list)

# tuple_dict = ({'name': 'Ruslan', 'age': 30}, {'name': 'Anna', 'age': 36})
# print(tuple_dict)

# mut_tup = ([1, 2, 4], [123, 3, 4])
# print(mut_tup)
#
# mut_tup[0][1] = 10
# mut_tup[1].append(89)
# print(mut_tup)

# a = (10, 20, 30, 30, 50, 60)
# b = [10, 20, 30, 30, 50, 60]
#
# print(a.__sizeof__())   # __sizeof__ - выводит размер в байтах
# print(b.__sizeof__())


# my_dict = {'Key': 56, ('b', 2): 89}

# my_tuple = (1, 2, 4, 54, 35,)
# my_tuple_2 = 1, 2, 4, 54, 35,
#
# my_tuple_3 = tuple([1, 2, 3, 4, 5, 6, 7, 'krt'])
# last = my_tuple_3[::-1]
# print(last)
# print(my_tuple_3)


# a = 1
# b = 2
# c = 3
#
# my_tuple = a, b, c
# print(my_tuple)


# s = [0, 1, 2, 3, 4, 5, 6]
# print(s[1::2])
# print(s[0::2])


# my_tuple = (1, 2, 3, 4, 5, (3, 6, 7), 6)
# print(my_tuple[0])
# print(my_tuple[5][1])

#                               Упаковка  Кортежа
# ----------------------------------------------------------------------------#

# my_tuple = 1, 2, 3, 'hello'
# print(my_tuple)


#                               Распаковка  Кортежа
# ----------------------------------------------------------------------------#
# a, b, c, d = my_tuple
# print(a)
# print(b)
# print(c)
# print(d)

# s = [1, 3, 43, 545]
# print(1 in s)
#
# my_tuple = (23, 434, 543, 23)
# print(203 in my_tuple)


# ----------------------------------------------------------------------------#
# my_tuple = (23, 434, 543, 23, 34)
# for el in my_tuple:
#     print(el)


# my_tuple = (23, 434, 543, 23, 34)
#
# i = 0
# while i < len(my_tuple):
#     print(my_tuple[i])
#     i += 1

# my_tuple = (23, 434, 543, 23, 34)
# del my_tuple            # DEL - полностью удаляет кортеж
# print(my_tuple)         # my_tuple - будет ошибка т.к. my_tuple удален

# my_tuple = (23, 434, 543, 23, 34)
# my_tuple2 = (3423, 4, 434, 543, 23, 34, 55)
#
# concat_tuple = my_tuple + my_tuple2          # Складывает два кортежа
# print(concat_tuple)


# my_tuple = (23, 434, 543, 23, 34, 345)
# # print(sorted(my_tuple))
# sort_2 = tuple(sorted(my_tuple, reverse=True))
# print(sort_2)


# my_list = [12, 3, 'sdfdsf', 56, True]
# my_set = {1, 45, 67, 777}
# my_tuple = (23, 434, 543, 23, 34, 345)

# print(dir(my_list))
# print(dir(my_set))
# print(dir(my_tuple))

# ----------------------------------------------------------------------------#


# castel = [1, ['c'], 543, 'P', ['n', ['r']], 'i', [[['s']]], 'e', ['s']] # Princess
# print(castel[3], castel[4][1][0], castel[5], castel[4][0], castel[1][0], castel[7], castel[8][0], castel[6][0][0][0])


# ----------------------------------------------------------------------------#

message = [('We',), 'rec', {'r': 'o'}, {'o':'r'}, {'m1':'ded'}, {'m3':["a "], 'm4':{'m5': 'Ufo'}}]
# We recorded Ufo

print(message[0][0], message[1] + message[2]['r'] + message[3]['o'] + message[4]['m1'], message[5]['m4']['m5'])