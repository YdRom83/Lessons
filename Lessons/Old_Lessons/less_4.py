#----------------------------------------------------------------------------#
# num = int(input('Enter a number: '))
# i = 0
# while i < num:
#     print('*  '*num)
#     i += 1
    

        
# weidht = 10
# heigth = 5
# i = 0
# j = 0
# for i in range:
#     print('*'*weidht)
# while i < weidht :
#     while j < heigth:
#         print('*'* heigth)
#         print('*'* weidht)
#     i += 1


# count = 5
# i = 0
# while i < count:
#     if (i == 0 or i == count -1):
#         print('*' * count)
#     else:
#         print("*" + (" "*(count-2)) + '*')
#     i += 1
                            # Строки
#----------------------------------------------------------------------------#

# str = 'Hello, world!'
# for i in str:
#     print(i)

# str = 'Hello, world!'
# print(id(str))
# print(type(str))
# print(len(str))

# str1 = 'Hello '
# str2 = 'World! '
# str3 = str1 + str2
# print(str3 * 5)


# str = 'Hello, world! I\'m Roman!'
# print(str.capitalize())      # capitalize() делает 1-е букву заглавной
# print(str.lower())
# print(str.upper())
# print(str.title())          # title() делает все 1-е буквы большими
# print(str.swapcase())      # swapcase() Делает большие буквы в маленкие и на оборот

# str = 'Hello, world! I\'m Roman! Hello everyone'
# print(str.count('Hello', 10, 50))   # count считает указанное слово в строке. 10 указываем с кого символа считать. 50 до кокого искать.


# str = 'Hello, world! I\'m Roman! Hello everyone'
# print(str.find('Hello'))     # показывает индекс с которого начинается искомое слово 


# str = 'Hello, world! I\'m Roman! Hello everyone'
# print(str.index('Hello', 2, 10)) 


# str = 'Hello, world! I\'m Roman! Hello everyone'
# print(str.rfind('Hello'))   # rfind() ищет с конца


# str = 'Hello, world! I\'m Roman! Hello everyone'
# print(str.startswith('w', 7))   # startswith() проверяет с чего начинается слово. 7 с кагодо индеса искать
# print(str.endswith('ne'))        # endswith() проверяет с чего заканчивается строка


# str = 'Hello, world! I\'m Roman! Hello everyone'
# print(str.isalnum())    #  набор букв цифр выдаст TRUe


# str = 'Hello, world! I\'m Roman! Hello everyone'
# print(str.isalpha()) # выдает true если одни буквы

# str = 'Hello, world! I\'m Roman! Hello everyone'
# str2 = '232'
# print(str2.isdigit()) # выдает true если одни цифры

# str2 = 'sdf'
# print(str2.islower())   # проверяет на мал. буквы


# str2 = ''
# print(str2.isupper())

# str2 = '    h'
# print(str2.isspace()) # проверяет на пробелы выдает True когда одни пробелы

# str = 'Hello, World!'
# print(str.istitle()) # выдает true если первые буквы заглавные

str = 'Hello world'
# print(str[::-1])
invert = ''
count = len(str) - 1
while count >= 0:
    invert += str[count]
    count -= 1
print(invert)