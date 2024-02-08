                            # while
#----------------------------------------------------------------------------#

# num1 = int(input('Enter number 1: '))
# num2 = int(input('Enter number 2: '))
# res = 0

# if num1 < num2:
#     while num1 <= num2:
#         res += num1
#         num1 +=1
# else:
#     while num2 <= num1:
#         res += num2
#         num2 +=1
# print('Sum is: ', res)

# num = 0 
# while num != 15:       # Бесконечный цикл num никогда нестанет 15
#     num += 2
#     print(num)

# num = 1
# while True:
#     print(num)
#     num += 1


                                # For
#----------------------------------------------------------------------------#

# str = input('Enter some text ')
# for letter in str:
#     print(letter)
    
# str = 'Enter some text '
# for letter in str [0:6:1]:         # С 0 до 6 буквы, с шагом 1
#     print(letter)

# str = 'Enter some text '
# for letter in str [::-1]:            # -1 Выводит строку задом-наперед
#     print(letter)

# Таблица умножения
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i*j, end="\t")
#     print("\n")

#----------------------------------------------------------------------------#

# floor = 1
# energy = 70
# print("i'm on the 1st floor")
# while floor != 5:
#     step = 0
#     while step != 20:
#         step +=1
#         energy -=1
#         if energy == 0:
#             print("i'm tired. i'll rest a little")
#             energy = 70
#     floor +=1
#     print("Now i'm on the ", floor, 'floor')
# print("i'm got the right floor")

#----------------------------------------------------------------------------#
# x = 1

# while x < 10:
#     print(x)
#     x +=1
#     if x >5:
#         break
# x = 1

# while x < 10:
#     x +=1
#     if x % 2 != 0 :
#         continue
#     print(x)

#----------------------------------------------------------------------------#

# num_1 = int(input('Enter 1st num: '))
# num_2 = int(input('Enter 2nd num: '))


# while num_1 <= num_2:
#     if num_1 % 7 == 0:
#         print(num_1)
#     num_1 +=1
    
# num_1 = int(input('Enter 1st num: '))
# num_2 = int(input('Enter 2nd num: '))

# x = num_1
# y = num_2

# for i in range(num_1, num_2):
#     print(i)
# x = num_1
# y = num_2

# print ("Less diaposone: ")  
# while y >= x:
#     print(y)
#     y -= 1

# print("Кратное 5: ")
# x = num_1
# y = num_2

# while x <= y:
#     if x % 5 == 0:
#         print(num_1)
#     x +=1


#----------------------------------------------------------------------------#

# num_1 = int(input('Enter 1st num: '))
# num_2 = int(input('Enter 2nd num: '))

# # num_1 = 5
# # num_2 = 155
# while num_1 < num_2:
#     if num_1 % 3 == 0 and num_1 % 5 != 0:
#         print("Fizz")
#     if  num_1 % 5 == 0 and num_1 % 3 != 0:
#         print('Buzz')
#     if num_1 % 3 == 0 and num_1 % 5 == 0:
#         print('Fizz Buzz')
#     if num_1 % 3 != 0 and num_1 % 5 != 0:
#         print(num_1)  

#----------------------------------------------------------------------------#
# count = int(input('Enter count of symbols '))
# symbols = input("Enter symbol: ")
# i = 0
# while i < count:
#     print(symbols)
#     i += 1

#----------------------------------------------------------------------------#

# while True:
#     num_1 = int(input('Enter 1st num: '))
#     if num_1 > 0 and num_1 != 7:
#         print("Num positive")
#     if num_1 < 0:
#         print("Num negative")
#     if num_1 == 0:
#         print("Num equal to zero")
#     if num_1 == 7:
#         print("Good Bye")
#         break
#----------------------------------------------------------------------------#

# num_1 = input('Enter  num: ')
# x = ''
# for i in num_1:
#     if i != '3' and i != '6':
#         x +=i
# print(x)

#----------------------------------------------------------------------------#
i = 100
count = 0
while i <= 9999:
    num = str(i)
    if (i < 1000):
        if num[0] != num[1] != num[2]:
            count += 1
    else:
        if num[0] != num[1] != num[2]  != num[3]:
            count += 1
    i += 1
print('Different num: ', count)