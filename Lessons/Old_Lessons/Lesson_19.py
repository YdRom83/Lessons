#                               Словари
# ----------------------------------------------------------------------------#
# my_dict = {'Key 1': 'Value 1'}
# my_dict_2 = {'Macbook': 'Pro',
#              'Developer': 'Nick',
#              'Iphone': 1,
#              }
# key = 'fruits'          # Добавление новых эл. в словарь
# value = 'orange'        # Добавление новых эл. в словарь
# my_dict_2[key] = value  # Добавление новых эл. в словарь

# print(my_dict)
# print(my_dict_2)
# print(my_dict_2['Macbook'])    # Доступ к значению по ключу

# my_dict.update(my_dict_2)  # Update - объединяет два словаря
# print(my_dict)

# my_list = [['key', 'value'], ['key_2', 'value_2']]
# my_dict_3 = dict(my_list)  # Создание словаря
# print(my_dict_3)

# my_dict_4 = dict.fromkeys(('Macbook', 'Iphone'), 1)
# print(my_dict_4)

# keys = ['a', 'b', 'c']  # Создание словаря
# default = 0
# new_dict = dict.fromkeys(keys, default)
# print((new_dict))


# my_dict_5 = {'Macbook': 'Pro',
#              'Developer': 'Nick',
#              'Iphone': 1,
#              'QW': 5,
#              'QW1': 6,
#              }
# print(my_dict_5.keys())    # Keys - Выводит ключи, без значений
# print(my_dict_5.values())  # Values - Выводит значения
# print(my_dict_5.items())   # Items - Выводит значения и ключи
# print(my_dict_5.get('Developer'))
# print(my_dict_5.get('Key'))         # GET - если нет ключа не выводит ошибку
# print(my_dict_5)
# print(my_dict_5.setdefault('Key'))  # setdefault - Добавляет  ключ
# print(my_dict_5)
# print(my_dict_5.pop('Macbook'))     # Pop - удаляет
# print(my_dict_5)
# print(my_dict_5.popitem())            # Удаляет последний эл.
# print(my_dict_5)


# a = {'a': 1}
# a['a'] = 4
# a['b'] = 2
# a.clear()      # Clear - очищает словарь
# print(a)

# a = {2: 1}
# print(a.get(2, 3))
# print(a.get('key', 'value'))


# a = {2: 1}
# b = a.copy()   # создаем копию
# c = a
# print(a)
# print(b)

# a = {2: 1}
# a.update({'a': 2})
# print(a)

# a = {2: 1, 'a': 2}
# for key in a:     # выводит ключи
#     print(key)

# for key, value in a.items():  # Выводит ключ значение
#     print(key, value)

# for item in a.items():      # Выводит ключ значение в кортеже
#     print(item)


my_dict = {"Nick": {"Phone": "0735558895",
                    "instagram": "@nick465", "tiktok": "@nicklike", 'city': 'Moscow'},
           "Ann": {"Phone": "0995588401",
                   "instagram": "@ann582", "tiktok": "@ann_02", 'city': 'Paris'},
           "Jane": {"Phone": "0505314589",
                    "instagram": "@jane_me", "tiktok": "@transformer", 'city': 'New-York'}}
user = my_dict[input("Enter a name ")][input("Enter the contact type ")]
print(user)
