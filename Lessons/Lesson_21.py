# ----------------------------------------------------------------------------#
# CSV - создает таблицу наподобие exel
# import csv
#
# filename = 'test.csv'
# shop_list = {
#     'картофель':[2, 100],
#     'яблоки': [3, 250],
#     'морковь': [1, 35],
# }
#
# with open(filename, 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file, quoting=csv.QUOTE_ALL)
#     writer.writerow(['Наименование', 'Вес', 'Цена'])
#     for name, value in sorted(shop_list.items()):
#         writer.writerow([name, *value])
#     writer.writerow(['мука', '4', '70'])
#
# rows = []
#
# with open(filename, 'r', encoding='utf-8') as file:
#     reader = csv.reader(file)

#                           Сериализация
# ----------------------------------------------------------------------------#
# Сериализация — процесс перевода какой-либо структуры данных в последовательность битов.
# Десериализация, соответственно обратный процесс.
# Чаще всего сериализация используется для сохранения объектов в файлы или передачи их по сети.


# import pickle
# filename = 'test.txt'
# shop_list = {
#     "овощи": ["картофель", "капуста"],
#     "бакалея": ["мука"],
#     "бюджет": 500,
# }
#
# with open(filename, 'wb') as file:
#     pickle.dump(shop_list, file)
#
# shop_list_2 =[]
# with open(filename, 'rb') as file:
#     shop_list_2 = pickle.load(file)
# print(shop_list_2)

# Задача 1
# Написать программу, которая запрашивает у пользователя имя и возраст и записывает в словарь.
# Ввод продолжается до тех пор, пока количество пар(ключ/значение) в словаре не равно 3.
# Если пользователь ввел повторное имя, то программа должна вывести соответствующее сообщение.
# После окончания ввода данные записываются в файл test.txt в формате json.

import json

# user = {}
# while len(user) != 3:
#     name = input('Введите имя: ')
#     age = input('Введите возраст: ')
#     if name not in user:
#         user[name] = age
#     else:
#         print('Данное имя уже существует')
#
# with open('test.json', 'w', encoding='utf-8') as file:
#     file.write(json.dumps(user, ensure_ascii=False, indent=4))

# with open('test.json') as file:
#     load = json.loads(file.read())
# print(load)


# Задача 2
# Написать программу список дел, которая спрашивает у пользователя значение n,
# после этого запрашивает на ввод n строк различных дел и сохраняет их в список,
# а после записывает значения из списка через одно в файл в одну строку


# ----------------------------------------------------------------------------#

import json

# smartphone_json = ('{"name": "iPear 23",'
#                    '"colors": ["black", "white", "red", "blue"],'
#                    '"price": 999.9,'
#                    ' "inStock": true}')
# smart = json.loads(smartphone_json)
# print(smart)
# price = smart['price']
# colors = smart['colors']
# print(price)
# print(colors)

# json_str = '15.4'
# json_str2 = '[1,2,3]'
# float_var = json.loads(json_str)
# float_var1 = json.loads(json_str2)
# print(type(float_var))
# print(type(float_var1))


import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'
response = requests.get(url)
body_dict = response.json()

user_id = body_dict['userId']
print((user_id))