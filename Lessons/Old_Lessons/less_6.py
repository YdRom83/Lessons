#                              H.W
#----------------------------------------------------------------------------#

# str = "Some string break for"
# print("Enter list reserve words. Words separate comma")
# reserve_words = input()
# reserve_words_arr = reserve_words.split(',')
# textWordsArr = str.split(' ')
# newStr = ' '

# for textWords in textWordsArr:
#     newW = textWords
#     for reserve_words in reserve_words_arr:
#         if (textWords.lower() == reserve_words.lower()):
#             newW = textWords.upper() + ' '
#     newStr += newW + ' '
# print(newStr)


# text = "Some. string. break for."
# textArr = text.strip().split('. ')
# # textArr = text.count('.')
# count = len(textArr)
# print(count)


#                               Списки
#----------------------------------------------------------------------------#

# list = ['red', 'green', 'blue', 'black']
# # print(list[1])
# for color in list:
#     print(color)


# genres = ['Drama', 'Comedy', 'Mystery', 'Fantasy']
# for genre in genres:
#     print(genre)

# test = list(('sdfds', 'dsfsdf'))
# print(test)

# arr3 = ['red', 'blue', ['orange', 'apple']]
# print(arr3[2][0])

# string = list('Hello')
# print(string)

# option 1
# list1 = [i*i for i in range(1, 11) if i % 2 == 0]   # В начале идет условие (i * i)
# print(list1)

# # option 2
# list2 = []
# for a in range(1, 11):
#     if a % 2 == 0:
#         list2.append(a * a)
# print(list2)
    

# list3 = [10, 'red', 'blue', 10.5, True, False]
# print(list3[1])
# print(list3[-1])

# list3 = [10, 'red', 'blue', 10.5, True, False]
# # print(list3[1:3])
# list4 = list3[0:6:2]
# print(list4)


# list3 = [10, 'red', 'blue', 10.5, True, False]
# list3[0] = 'yellow'                           # Перезаписывем первый элемент в спмске
# print(list3)



# list3 = [10, 'red', 'blue', 10.5, True, False]
# print(len(list3))                             # LEn считает количество в списке   


# list5 = [1, 23, 3, 4, 56, 34, 111]
# print(max(list5))                    # max выводит max значение
# print(min(list5))                    # min выводит min значение
# print(sum(list5))                    # sum складывает  значения
# print(sorted(list5))                 # sorted сортирует значения
# print(sorted(list5, reverse=True))   #  сортирует значения с конца
# list5.append(666)                    # добавляет в список значение
# print(list5)


fruits = ['apple', 'banana', 'coconut', "apple"]
# colors = ['red', 'green', 'yellow']
# fruits.extend(colors)               # extend соединяет два массива
# fruits.extend(['potato', 'carrot'])

# fruits.insert(2, 'juice')           # insert добовляет в список новый эл. по любому индексу(2)
# fruits.insert(-1, 100 )
# print(fruits)

# fruits.remove(100)                 # remove удаляет значение из списка
# fruits.remove('carrot')
# print(fruits)

# fruits.pop(1)                      # pop удаляет эл. по индексу, если идекс не указывать, то удалится поседний эл.
# print(fruits)

# # fruits.clear()                   # clear очищает список
# # print(fruits)

# print(fruits.index('red'))        # index получаем индекс значения
# print(fruits.count('apple'))      # count считае сколько указанных значений

# fruits.sort()                     # Сортирует список       
# fruits.sort(reverse=True)         # Сортирует список в обратном порядке
# print(fruits) 


# поиск в списке
# if 'apple' in fruits:
#     print('Find')
# else:
#     print('Not find')


list1 = [10, 20, 30]
list2 = list1.copy()          # copy копирует список
list2.append(100)
print(list1, list2)