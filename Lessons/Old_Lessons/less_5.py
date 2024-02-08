#----------------------------------------------------------------------------#
# str = 'hello. my names Roman. i am programmer'

# array = str.split('. ')

# OPtion 1
# p1 = array[0].capitalize()
# p2 = array[1].capitalize()
# p3 = array[2].capitalize()
# print(p1 + '.', p2 + '.', p3)

# Option2
# result = ''
# for i in array:
#     result += i.capitalize() + '. '
# print(result)

#                                   Строки
#----------------------------------------------------------------------------#
# str = 'Hello\tSome string'
# print(str.center(110, "="))   # center сколко пробелов отсупить
# print(str.expandtabs(tabsize=10))  #  expandtabs() добавляет отступы, \t -обязательно надо указывать в строке.


# str = '@Hello. Some string!'
# print(str)
# print(str.lstrip("@"))  # lstrip() убирает пробелы в начале или символы
# print(str.rstrip("!"))  # lstrip() убирает пробелы справа или символы
# print(str.strip("@!"))  # strip() убирает все указанные  символы
# print(str.zfill(100))     # zfill() добавляет нули в начало строки

# userName = input('Ваше имя: ')
# str = f'Hello, {userName}! Welcome to website!'
# print(str)

# userName = input('Ваше имя: ')
# age = input('Ваш возраст: ')
# profession = input('Ваша профессия: ')
# str = 'Привет, {}! Ваш возраст: {} лет. Ваша профессия: {}'
# res = str.format(userName, age, profession)
# print(res)


#                                  Модули Строки
#----------------------------------------------------------------------------#
# import string
# import random

# user_login = ''.join(random.sample(string.ascii_lowercase, 10))
# user_password = ''.join(random.sample(string.ascii_letters + string.digits, 10))
# print("Login: ", user_login)
# print("Pass: ", user_password)


# from string import Template

# str = Template("$userName имеет права на $userRights в этом $app.")
# resStr = str.substitute(
#     userName = 'Olga',
#     userRights = 'укправление блогом',
#     app = 'приложение'
# )
# print(resStr)


#                            Регулярные выражения
#----------------------------------------------------------------------------#

import re          # re модуль  Регулярныx выражения

# str ='+7 (123) 789-45-45'
# match = re.search(r'\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}', str)   # Проверка телефона
# print(match)

# str ='j313'

# match = re.search(r'[0-9a-f]', str)  
# print(match)

str ='j'

match = re.search(r'\d', str)  
if(match != None):
    print('Cheked')
else:
    print('Not cheked')