#                             Работа с файлами
# ----------------------------------------------------------------------------#

# file = open('example.txt', 'a')  # Открывает файл, a -добавляет зн.
# file.write('\npython')           # Записывает файл
# # print(file.read())             # Читает файл
# file.close()                     # Закрывает файл
# file = open('example.txt', 'r')  # Открывает файл
# print(file.read())
# file.close()


# with open('example.txt') as file:     # With - открывает файл и автоматически закрывает его.
#     print(file.read())

# f = open('example.txt', 'r')
# print(f.read(7))                # Выводит первые 7-мь символов

# print(f.readline())             # Выводит первые 1 строку

# a = f.readlines()               # Выводит все строки в списке
# print(a[2])                     # Выводит  строку по индексу

# f = open('example23.txt', 'w')
# f.write('Hello wold')
# f.close()

# file = 'example.txt'
# with open(file, encoding='utf-8') as file:
#     data = file.read()
#     print(data)


# file = 'example.txt'

# with open(file, encoding='utf-8') as file:
#     data = file.readlines()
#     print(data)

# with open(file, encoding='utf-8') as file:
#     for line in file:
#         print(line.strip())

# import os

# os.rename('example23.txt', 'examp.txt')        # rename - переименовывает файл


# file_name = input()
#
#
# def read_file(file_name):
#     with open(file_name, 'r') as lines:
#         line = lines.readline()
#     os.rename(file_name, 'example.txt')
#     return line


# print(read_file('txt.txt'))


# import os

# os.system('45.jpg')  # Открывает любые файлы


# with open('example.txt', encoding='utf-8') as file:
#     str1 = file.read()
# word_list = str1.split()
# result = ', '.join(word_list)
# # for word in word_list:
# #     result += word + ', '
# print(result)



import json

# filename = 'file.json'
# info = {
#     'ФИО': 'Иван Иванов Иванович',
#     'Оценки': {
#         'Матеиатика': 4,
#         'Физика': 5,
#         'Информатика': 5
#     },
#     'Хобби': ['Программирование','Плавание'],
#     'Возраст': 14,
#     'ДомЖивотное': None,
# }
# # Записываем в JSON файл
# with open(filename,'w', encoding='utf-8') as file:
#     file.write(json.dumps(info, ensure_ascii=False, indent=4))   # Dumps - запаковывает в JSON
#
# # Считывае с JSON файла
# info_2 = []
# with open(filename, encoding='utf-8') as file:
#     info_2 = json.loads(file.read())                        # Loads - распаковывает JSON в словарь
# print(info_2)



# x =  '{ "name":"John", "age":30, "city":"New York"}'  # JSON
# y = json.loads(x)           # Loads - распаковывает JSON в словарь
# print(y['age'])            # Достаем из словаря

# x = {
#   "name": "РОман",
#   "age": 30,
#   "city": "New York"
# }
# print(type(x))
# y = json.dumps(x, ensure_ascii=False, indent=4)
# print(y)


# Задание 1
# Дан текстовый файл. Необходимо создать новый файл,
# в который требуется переписать из исходного файла все
# слова, состоящие не менее чем из семи букв


# with open('txt.txt', 'r') as file:
#     text = file.read()

# words = text.split()

# filter_words = [i for i in words if len(i) >= 7]
# filter_text = ' '.join(filter_words)

# with open('output.txt', 'w') as txt:
#     txt.write(filter_text)


# Задание 2
# Дан текстовый файл. Необходимо переписать его
# строки в другой файл. Порядок строк во втором файле
# должен совпадать с порядком строк в заданном файле.

# with open('txt.txt', 'r') as file:
#     lines = file.readlines()
# with open('out.txt', 'w') as txt:
#     txt.writelines(lines)


# Задание 4
# Дан текстовый файл. Добавить в него строку из двенад-
# цати звездочек (************), поместив ее после последней
# из строк, в которых нет запятой. Если таких строк нет,
# то новая строка должна быть добавлена после всех строк
# имеющегося файла. Результат записать в другой файл

# with open('txt.txt', 'r') as file:
#     lines = file.readlines()

# comma = [i for i in lines if ',' not in lines]

# if comma:
#     last_line = len(lines) - lines[::-1].index(comma[-1])
#     lines.insert(last_line + 1, '************\\n')
# else:
#     lines.append('************\\n')

# with open('out.txt', 'w') as f:
#     f.writelines(lines)


# Задание 5
# Дан текстовый файл. Подсчитать количество слов,
# начинающихся с символа, который задаёт пользователь.

# user = 'i'
# with open('txt.txt') as f:
#     file = f.read()
# sp = [i[0] for i in file.split()]
# count = 0
# for i in range(len(sp)):
#     if sp[i].lower() == user.lower():
#         count += 1
# print(count)

# Задание 6
# Дан текстовый файл. Переписать в другой файл все его
# строки с заменой в них символа * на символ & и наоборот.

# with open('txt.txt') as f:
#     text = f.read()
# text = text.replace('*', 'TEMP_SYMBOL').replace('&', '*').replace('TEMP_SYMBOL', '&')

# stars = [i.replace('*', '&') for i in text ]
# stars2 = [i.replace('&', '*') for i in text]
# with open('out.txt', 'w') as txt:
#     txt.writelines(text)
# with open('txt.txt', 'w') as t:
#     t.writelines(text)


# Задание 7
# Дан массив строк. Записать их в файл, расположив
# каждый элемент массива на отдельной строке с сохране-
# нием порядка

# lst = ["It's", 'different', 'task', "i'm", 'wrong']

# with open('out.txt', 'w') as f:
#     for i in lst:
#         f.write(i +'\n')


# Задание 8
# Дан текстовый файл. Подсчитать количество симво-
# лов в нём.

# with open('txt.txt', 'r') as f:
#     file = f.read()
#     txt = sum(1 for i in file if i.isalpha())
#     print(txt)


# Задание 9
# Дан текстовый файл. Подсчитать количество строк
# в нём

# with open('txt.txt') as f:
#     line = f.readlines()
#     summa = sum(1 for _ in line)
#     print(summa)

# Задание 10
# Дан текстовый файл. Необходимо создать новый файл
# убрав из него все неприемлемые слова. Список неприем-
# лемых слов находится в другом файле

# with open('bad.txt', 'w') as f:
#     f.write('говно\n лопата \n')
#     f.write('writting\nSome \n')

# with open('txt.txt', 'r') as file:
#     text = file.read()

# with open('bad.txt', 'r') as file:
#     bad_words = file.read().splitlines()

#     for word in bad_words:
#         text = text.replace(word, '@@@')

#     with open('out.txt', 'w') as file:
#         file.write(text)


# def remove_bad_words(input_file, bad_words_file, output_file):
#     with open(input_file, 'r') as file:
#         text = file.read()

#     with open(bad_words_file, 'r') as file:
#         bad_words = file.read().splitlines()

#     for word in bad_words:
#         text = text.replace(word, '')

#     with open(output_file, 'w') as file:
#         file.write(text)

# # Пример использования
# input_file = 'txt.txt'
# bad_words_file = 'bad.txt'
# output_file = 'out.txt'

# remove_bad_words(input_file, bad_words_file, output_file)