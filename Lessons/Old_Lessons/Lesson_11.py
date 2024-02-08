# ----------------------------------------------------------------------------#
# import platform
#
# print(platform.system())
# print(platform.platform())  # Инфа о винде
# print(platform.node())     # Имя компьютера
# print(platform.uname())   # Выводит: system, node, release, version, machine и processor.


# ----------------------------------------------------------------------------#
# def say_hello(name):
#     print(f"Hello, {name}")
#
#
# def summa(*args):  # *args - множество параметров
#     return sum(args)
#
#
# def factorial(n):
#     pr = 1
#     for i in range(1, n + 1):
#         pr *= i
#     return pr
#
#
# my_str = 'строчка'
# my_num = 1
# my_num_2 = 2
#
#
# def plus(a, b):
#     return a + b


# ----------------------------------------------------------------------------#

# def my_function(*kids):
#     print("Дети", kids[2])
#
#
# my_function('Anna', 'Olga', 'Ivan')

# ----------------------------------------------------------------------------#
# def my_function_2(child3, child2, child1):
#     print(child3, child2, child1)
#
#
# my_function_2(child1='Sergey', child2='Olga', child3='Anna')

# ----------------------------------------------------------------------------#
# def my_function_3(**kid):
#     print('Last name is ' +kid['lname'], kid['fname'])
#
#
# my_function_3(fname='Tony', lname='Hawk')


# import turtle
#
# turtle.shape('turtle')
# turtle.speed(10)
#
#
# def make_rectangle(h, w):
#     for i in range(2):
#         turtle.forward(w)
#         turtle.left(90)
#         turtle.forward(h)
#         turtle.left(90)
#
#
# make_rectangle(150, 200)
#
#
# def make_square():
#     for i in range(4):
#         turtle.forward(100)
#         turtle.left(90)
#
#
# make_square()
# # def circle(h, s):
# #     for i in range(360):
# #         turtle.forward(h)
# #         turtle.right(s)
# # circle(2, 1)
#
# turtle.circle(150)
# turtle.done()


def quote():
    author = 'Steve Jobs'
    form_author= author.rjust(70, ' ')
    return f"Don't let the noise of others' opinions drown out your own inner voice.”\n {form_author} "

print(quote())


def odd_number(a, b):
    for i in range(a, b+1):
        if i % 2 != 0:
            print(i)

odd_number(1, 10)


# def line(lenght, direction, sign):
#     diriction_1 = lenght * sign
#     # if direction == h:
#     #     for i in range(lenght):
#     #         print(i*sign)
#
# line(50,  '=')

