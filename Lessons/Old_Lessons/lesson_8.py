# myStr="Python2023"
# print(myStr.center(30))
# print(myStr.center(30,'*'))
# print(myStr.center(5))

#----------------------------------------------------------------------------#

# myStr="Python2021\n\t\tPython- cool!"
# print(myStr.expandtabs(tabsize=5))

# rawStr = r"This is a \n raw string"   # \n - не работает при использовании r
# print(rawStr)

# userLogin=input("Your login: ")
# print("Welcome,", userLogin, ". Let's start game!")
# strMsg="Dear, "+userLogin+". Game over!"
# print(strMsg)

# strMsg = "My name is {}, I'm {}, i'm {} and i learn {}".format("Roman", 25, 'student', 'python')
# print(strMsg)
#
# strMsg2 = "My name is {0}, I'm {1}".format("Roman", 25)
# print(strMsg2)
#
# strMsg3 = "My name is {name}, I'm {age}".format(name="Student",age=25)
# print(strMsg3)
#
# strMsg = "Your salary is {0:9.2f}".format(200.846)   # 2f - сколько цифр после запятой
# print(strMsg)

# userNumber = 255
# myStrB = "The binary representation of a number {n} is {n:b}".format(n=userNumber)
# print(myStrB)


# myStr1="The number1 range from {0:-} to {1:-}".format(-10,10)
# print(myStr1)

# import string
# print(string.ascii_letters)
# print(string.octdigits)
# print(string.punctuation)


# from string import Template
# t = Template('$userName has the rights to $userRights in the $appName')
# resStr = t.substitute(userName='Admin', userRights = 'edit', appName='uperApp.')
# print(resStr)

import re

# text = "Привет, питон"
# result = re.search(r'п\w+', text)
# print(result.group())

# date = "12-06-2020"
# result = re.match(r'\d{2}-\d{2}-\d{4}',date)
# print(result.group())
telephone = '89261234567'

phone = re.match(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', telephone)
print(phone)