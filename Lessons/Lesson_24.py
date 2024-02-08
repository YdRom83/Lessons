# ----------------------------------------------------------------------------#
# a = 44
# b = -44
# if a > b:
#     print(a)
# else:
#     print(b)
#
# n = int(input())
# m = int(input())
# if (n - m == 135) or (m - n == 135):
#     print('YES')
# else:
#     print('NO')

# num = -155
# if num > 100 or num < -100:
#     print('-')
# else:
#     print('+')

# user = int(input())
# season = ['Зима', 'Весна', 'Лето', 'Осень']
# if user == 12 or user == 1 or user == 2:
#     print(season[0])
# elif user == 3 or user == 4 or user == 5:
#     print(season[1])
# elif user == 6 or user == 7 or user == 8:
#     print(season[2])
# elif user == 9 or user == 10 or user == 11:
#     print(season[3])
# else:
#     print('Вы ввели не то число!!!')
# if user == 12 or user == 1 or user == 2:
#     print('Зима')
# elif user == 3 or user == 4 or user == 5:
#     print('Весна')
# elif user == 6 or user == 7 or user == 8:
#     print('Лето')
# elif user == 9 or user == 10 or user == 11:
#     print('Осень')


# x = -4
# y = 5
# z = 43
# if x > 0 and y > 0 and z > 0:
#     print('3 числа' )
# elif x > 0 and y > 0 and z < 0:
#     print('2 числа')
# elif x > 0 and y < 0 and z >0:
#     print('2 числа')
# elif x > 0 and y < 0 and z < 0:
#     print('1 число')
# elif x < 0 and y > 0 and z > 0:
#     print('2 числа')
# else:
#     print('1 число')

# x = 5
# y = 3
# z = -4
# my_list = [x, y, z]
# count = 0
# for i in my_list:
#     if i > 0:
#         count += 1
# print(count)

# ----------------------------------------------------------------------------#

import telebot

token = '6272411751:AAFM3VyFky-kRXW9VD0lfe9ovzbNL5U7Zhk'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет враг!')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
