#                               Списки
# ----------------------------------------------------------------------------#


# numbers = [1, 2, 3, 4, 5, 6, 7]
# print(numbers[0] == 1)
# lang = ['python', 'C#', 'Java']
#
# my_list = []        # Создаем список
# my_list2 = list()   # Создаем список


# num = list(range(5))
# print(*num)  # * - очищает от скобок и запятых


# s = 'asdasfdfew'
# chars = list(s)  # Создаем список
# print(chars)


# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(numbers[1][1])


# numbers = [545, 433, 4, 54, 34, 12]
# numbers2  = [23, 438, 90]
# numbers.append(666) # Добавляет значение в конец списка
# numbers.remove(545)# Удаляет указанное число
# numbers.pop(2)    # удаляет по индексу
# numbers.clear()  # Очищает список
# numbers.sort() # Сортировка
# numbers.extend(numbers2) # Расширяет список
# print(numbers.index(12)) # Показывает индек
# numbers.insert(6, 9900) # Добавляет число по индеку
# print(numbers)

#                                Кортежи
# ----------------------------------------------------------------------------#
# Кортежи - неизменяемый тип данных

# a =(34, 24, 65, 443)
# print(a)
# print(list(a)) # Кортеж преобразовали в список
# print(tuple(a))#  Список преобразовали в кортеж

# s = [232, 34, 33, 45, 54, 77, 90]
# res = []
# for i in s:
#     if i % 2 == 0:
#         res.append(i)
#         res.sort()
# print(res)


a = [1, 2, 3, 4, 5, 6]
# # Option 1
# i = 0
# n = len(a)
# while i < n:
#     if a[i] % 2 == 0:
#         a[i] //= 2
#         i += 1
#     else:
#         a.pop(i)
#         n -= 1
# print(a)

# Option 2
for i in range(len(a)-1, -1, -1):
    if a[i] % 2 == 0:
        a[i] //=2
    else:
        a.pop(i)

print(a)




#                                Генераторы
# ----------------------------------------------------------------------------#

# list1=[i*i for  i in range(6)] # Генерирует список
# print(list1)
#
# list2 = [i+"*" for i in "example"]
# print(list2)
#
# list3 = [i*i for i in range(1, 11) if i%2 ==0]
# print(list3)
#
#
# customers=['Bob','Anna','Joe','Bob','Nick']
# list5=[i for i in customers if i!='Bob' and i!='Joe']
# print(list5) #['Anna', 'Nick']
#
# guests  = ['Peter', 'Anna', 'Olga', 'Ivan', 'Misha']
# list6 = [i for i in guests if i != 'Peter' and i != 'Misha' and i != 'Ivan']
# print(list6)
#
# guests  = ['Peter', 'Anna', 'Olga', 'Ivan', 'Misha']
# list7 = [i for i in guests if i == 'Peter' and i == 'Olga' and i == 'Anna']
# print(list7)


# list8 = [x*y for x in range(1, 4) for y in range(1, 4)]
# print(list8) # [1, 2, 3, 2, 4, 6, 3, 6, 9]
#
# list9  = [[x*y for x in range(1, 4)] for y in range(1, 4)]
# print(list9) # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


# import random
# number = [random.randint(-10, 10) for _  in range(10)] # Генерируе  список
# print(number)
# num = [-1, 34, -343, 435, 34, -435, 45, 434]
# negative = []
# even = []
# odd = []
# multy = []
# for i in num:
#     if i < 0:
#         negative.append(i)
# print(sum(negative))
# for i in num:
#     if i % 2 == 0:
#         even.append(i)
# print(sum(even))
# for i in num:
#     if i % 2 != 0:
#         odd.append(i)
# print(sum(odd))
# n = 1
# for i in range(len(num)):
#     if i % 3 == 0:
#         multy.append(num[i])
# for j in multy:
#     n *= j
# print(n)
# num2 = sorted(num)
# s = 1
# for i in range(len(num2)):
#     if i != 0 and [i] != -1:
        