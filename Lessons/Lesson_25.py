# n = int(input('Введите число: '))
# Option 1
# i = 1
# while n > 1:
#     i *= n
#     n -= 1
# print(i)
# ----------------------------------------------------------------------------#

# Option 2

# res = 1
# for i in range(1, n+1):
#     res *= i
# print(res)
# ----------------------------------------------------------------------------#
# Option 1

# import random
#
# num = random.randint(1, 10)
# print(num)
#
# count = 0
# user = -1
# while num != user and count != 3:
#     user = int(input('Введите число: '))
#     if user < num:
#         print('Ваше число меньше')
#     elif user > num:
#         print('Ваше число больше')
#     else:
#         print('Вы угадали')
#     count +=1

# Option 2
# count = 3
# for i in range(count):
#     user = int(input('Введите число: '))
#
#     if user < i:
#         print(f'Ваше число меньше, у вас осталось {count - 1} попыток')
#
#     elif user > i:
#         print(f'Ваше число больше у вас осталось {count - 1} попыток')
#
#     elif i == user:
#         print('Вы угадали')
#         break
#     else:
#         print('Вы не угадали.')
# ----------------------------------------------------------------------------#
# Option 1
# n = [int(i) for i in input().split()]
# print(max(n))
# ----------------------------------------------------------------------------#

# Option 2
# x = -1
# res = []
# while x != 0:
#     x = int(input('Enter number: '))
#     res.append(x)
# print(max(res))

# ----------------------------------------------------------------------------#
# user = input('Enter text: ')
# sp = user.replace(' ', '').lower()
# letters = 'б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ'
# i = 0
# count = 0
# Option 1
# while len(sp) > i:
#     if sp[i].lower() in letters:
#         count += 1
#     i += 1
# print(count)
# ----------------------------------------------------------------------------#

# Option 2
# for i in sp:
#     if i in letters:
#         count += 1
# print(count)

# ----------------------------------------------------------------------------#
# user = int(input())
# for i in range(1, 10):
#     print(i * user)
# ----------------------------------------------------------------------------#

# user = int(input())
# for i in range(1, user+1):
#     if user % i == 0:
#         print(i)
# ----------------------------------------------------------------------------#


#                                  ООП
# ----------------------------------------------------------------------------#
# class Person:
#     name = 'Ivan'
#     age = 35
#
#     def say(self):
#         print('Hello')
#
#
# person1 = Person()
# print(person1.name)
# person1.say()
#
# person2 = Person()
# person2.name = 'Vasia'
# print(person2.name)
# person2.say()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# person1 = Person('Ivan', 15)
# person2 = Person('Петр', 32)
# print(person1.name)
# print(person1.age)
# print(person2.name)
# print(person2.age)


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'My name is {self.name}'


person1 = Person('Ivan')
print(person1)
