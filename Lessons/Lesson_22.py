# ----------------------------------------------------------------------------#

# import urllib.request
# import json
#
# url = 'https://jsonplaceholder.typicode.com/todos/1'
# with urllib.request.urlopen(url) as response:
#     body_json = response.read()
#
# body_dict = json.loads(body_json)
# print(body_dict)
# user_id = body_dict['title']
#
# print(user_id)



# url = 'https://samples-files.com/samples/Code/json/sample3.json'
# with urllib.request.urlopen(url) as response:
#     body_json = response.read()
#
# body_dict = json.loads(body_json)
# # print(body_dict)
# user_title1 = body_dict['books'][0]['title']
# user_title2 = body_dict['books'][1]['title']
# user_title3 = body_dict['books'][2]['title']
# author1 = body_dict['books'][0]['author']
# author2 = body_dict['books'][1]['author']
# author3 = body_dict['books'][2]['author']
# print(f'Автор {author1} название {user_title1}')

# with open('txt.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
# sp = text.split()
# print(sp)
# for i in sp:
#
#     if i == 'Автор':
#         sp.replace(i, author1)
#     elif i == 'Название':
#         sp.replace(i,user_title1)
#     else:
#         sp += i
#     tx = ' '.join(sp)
# with open('out.txt', 'w') as f:
#     f.write(tx)


# x = 10
# y = '20'
# c = int(y)
# print(type(x))
# print(type(y))
# print(type(c))

# a = 56.5
# b = -5
# print(a / b)

# user = float(input())
# user2 = float(input())
# print(user + user2)


# n = int(input())
# print(n % 2 == 0)


# user = input('Введите предложение: ')
# third = user[2:].replace(' ', '_')
# print(third)

# s = 'Hello'
# sp = s[::-1]
# print(sp)
# user = input('Enter: ')
# lst = list(user)
# print(lst[::-1])

# ----------------------------------------------------------------------------#
import requests
from datetime import datetime
api_key = 'ad8358d5cd972a66531a1f0c02165e33'
city = 'Тольятти'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

response = requests.get(url)
data = response.json()
print(data)
print('Город:', data['name'])
temperature =  data['main']['temp']
degree = temperature * 9 / 5 + 32
print('Температура:',degree)

s= data['sys']['sunrise']
ss = data['sys']['sunset']

sunrise = datetime.fromtimestamp(s)
sunset = datetime.fromtimestamp(ss)

print('Восход:', sunrise)


