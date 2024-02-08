# name = input('Ваше имя ')
# age = int(input('Ваш возраст '))
# print("вас зовут ", name, ' год вашего рождения: ' + str(2023-age) + " лет")
# print(name * 4) 


#                    IF 
#-------------------------------------------------#

# a = 1
# b = 2
# if a < b:
#     print('Is True')

# print('1 == 1', 1 == 1)   # Различные операторы
# print('1 > 1', 1 > 1)
# print('1 < 1', 1 < 1)
# print('1 >= 1', 1 >= 1)
# print('1 != 1', 1 != 1)


# print(bool(''))
# print(bool(0.0))
# print(bool(None))
# print(bool('Some string'))
# print(bool(1))


# var1 = True
# var2 = False

# print(var1 and not var2)

#-------------------------------------------------#

# time = int(input('Какое сейчас время в часах? '))
# ticket = False
# money = True
# luggage = False
# print((money or ticket) and not luggage and time > 6 and time <= 24)

# car_speed = 60

# if car_speed >= 50 and car_speed <= 100:
# if 50 <= car_speed <= 100:
#     print('car ride 50 km and  less 100 km')


# num = 2
# if num > 1:
#     print('String1')
#     print('String2')
#     print('String3')
    
# print('Выражение за условием')

#-------------------------------------------------#

# car_speed = 150
# bike_speed = 140

# if car_speed > bike_speed:
#     print('Car move faster than bike')
#     bike_speed += 50
# elif car_speed < bike_speed:
#      car_speed += 50
#      print('Car move slowly than bike')
# else:
#     print('Speed equel')
     
     
#-------------------------------------------------#

# flowers = 3
# if flowers > 2:
#     print('У вас как миниму 3 цветка')
#     if flowers < 5:
#         print('У вас как меньше 5  цветков')

#-------------------------------------------------#

# number = int(input('Enter number: '))
# num1 = number // 10
# num2 = number % 10
# print(num1)
# print(num2)

#-------------------------------------------------#
# number = int(input('Enter number: '))
# num1 = number // 100
# num2 = (number - num1 * 100) // 10
# num3 = number % 10

# print(num1)
# print(num2)
# print(num3)
# print(str(num1) + str(num2) + str(num3))
#-------------------------------------------------#
# degree = int(input('Enter degree: '))
# print(degree * 1.8 + 32, 'F')

#-------------------------------------------------#

# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))

# if num1 > num2:
#     print('First number more than second number')
# else:
#      print('First number less than second number')

#-------------------------------------------------#
 
# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# sign = input('Choose action ')

# if sign == '*':
#     print(num1 * num2)
# if sign == '/':
#     print(num1 / num2)
# if sign == '+':
#     print(num1 + num2) 
# if sign == "-":
#     if(num1 > num2):
#         print(num1 - num2)
#     else :
#         print(num2 - num1)
# if sign == '@':
#     print((num1+num2)/2)   


#                  Исключения
#-------------------------------------------------#

# try:
#     num1 = input('Число 1: ')
#     num2 = int(input('Число 2: '))
#     res = num1 / num2
#     print(res)
# except:
#     print('Нельзя делить строку на число')


# try:
#     amount = int(input('Введите количество отправленных посылок '))
#     items_type = input('Тип посылок ')
#     parts_number = int(input('Количество элементов в посылке '))
#     parts_amount = amount / parts_number
    
#     print(amount, items_type, 'сохраненные')
#     print('Каждая из ', parts_number, ' частей содержит ', parts_amount, items_type)
# except ValueError:
#     print('Количесво должно быть целым числом')
# except ZeroDivisionError:
#     print('Вы не можете делить на ноль')
# finally:
#     print('Программа выполнена успешно')


# try:
#     f = open('test.txt', 'w')   # Создает файл
# except:
#     f.close()
