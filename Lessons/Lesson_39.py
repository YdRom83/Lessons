# def fun(*args):
#     print(args[0])
#     print(args)
#
#
# fun('Python', 'C++', 'Java')

# ------------------------------------------------------------------------#

# def sum_num(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
# print(sum_num(1, 2, 3))
# print(sum_num(1, 2, 3, 4))
# print(sum_num(1, 2, 3, 4, 5, 6))

# ------------------------------------------------------------------------#
# def fun(**kwargs):
#     print(kwargs)
#
# fun(name='Tom', age=35, company='Google')
# fun(lan='Python', version='3.12')

# ------------------------------------------------------------------------#
# def fun(**kwargs):
#     for key in kwargs:
#         print(f'{key} = {kwargs[key]}')
#
# fun(name='Tom', age=35, company='Google')

# ------------------------------------------------------------------------#

# def sum_num(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
#
# numbers = (1, 2, 3, 4, 5)
# print(sum_num(*numbers))

# ------------------------------------------------------------------------#

# def print_person(name, age, company):
#     print(f'Name: {name}, Age: {age}, Company: {company}')
#
#
# person = ('Tom', 56, 'Yandex')
# print_person(*person)  # Кортеж нужно распаковывать, а то ошибка

# ------------------------------------------------------------------------#

# def print_person(name, age, company):
#     print(f'Name: {name}, Age: {age}, Company: {company}')
#
# tom = {'name': 'Tom', 'age': 56, 'company': 'Google'}
# print_person(**tom)

# ------------------------------------------------------------------------#

# def sum_num(num1, num2, *nums):
#     result = num1 + num2
#     for i in nums:
#         result += i
#     return result
# print(sum_num(1, 2, 4))
# print(sum_num(1, 2, 4, 45, 66))

# ------------------------------------------------------------------------#

# def vvp(c, i, g, e, im):
#     y = c + i + g + e - im
#     return y
# user = int(input('Enter c: '))
# user2 = int(input('Enter i: '))
# user3 = int(input('Enter g: '))
# user4 = int(input('Enter e: '))
# user5 = int(input('Enter im: '))
#
# dict = {'c': user, 'i': user2, 'g': user3, 'e': user4, 'im': user5}
# print(vvp(**dict))

# ------------------------------------------------------------------------#
#
# def nums(*args):
#     positive = sorted([i for i in args if i < 0], reverse=True)
#     negetive = sorted([i for i in args if i > 0], reverse=True)
#     return positive, negetive
#
# digits = [1, 2, 4, 556, -5, -9]
#
# print(nums(*digits))

# ------------------------------------------------------------------------#
'''
                                Рекурсия!!!
'''
# ------------------------------------------------------------------------#

# def summa(n):
#     x = 0
#     for n in range(1, n+1):
#         x += n
#     return x
# print(summa(5))

# def summa(n):
#     if n == 1:
#         return 1
#     return n + summa(n - 1)
#
# print(summa(5))
# ------------------------------------------------------------------------#

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))

















