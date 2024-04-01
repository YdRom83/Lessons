
# print('строка 1')
# print('строка 2')
# print('строка 3')
# # print(a)
# 1/0
# print('строка 4')
# print('строка 5')
# print('строка 6')
# print('строка 7')

# try:
#     file = open('mygile.txt')
# except FileNotFoundError:
#     print('Невозможно открыть файл')

# try:
#     x, y = map(int, input().split())
#     res = x / y
#     # print(res)
# except (ZeroDivisionError, ValueError):
#     print('Делить на 0 нельзя')
# except ValueError:
#     print('Ошибка типа данных')


# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError as z:
#     print(z)
# except ValueError as z:
#     print(z)


# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ValueError:
#     print('Ошибка типа данных')
# except Exception as e:
#     # print('Делить на 0 нельзя')
#     print(e)

# try:
#     x, y = map(int, input().split())
#     res = x / y
# except:
#     print('Error')

# try:
#     lst = [1, 2, 3]
#     print(lst[6])
# except IndexError :
#     print('OUT RANGE')


# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError as z:
#         print(z)
# except ValueError as z:
#         print(z)
# else:
#     print('Исключений не произошло')
# finally:
#     print('Блок finally выполняется всегда')


# try:
#     f = open("myfile.txt", 'w')
#     f.write('Hello')
# except FileNotFoundError as z:
#     print(z)
# except:
#     print('Other Error!!')
# finally:
#     if f:
#         f.close()
#         print('File closed')


# try:
#     with open("myfile.txt", 'a') as f:
#         f.write('\nhello' )
# except FileNotFoundError as z:
#     print(z)
# except:
#     print('Other Error')


# def get_value():
#     try:
#         x, y = map(int, input().split())
#         return x, y
#     except ValueError as v:
#         print(v)
#         return 0, 0
#     finally:
#         print('Finally accept before return')
#
#
# print(get_value())

# try:
#     x, y = map(int, input().split())
#     try:
#         res = x / y
#     except ZeroDivisionError:
#         print('Zero by Division')
# except ValueError:
#     print('TYPE ERROR')


# def div(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return 'Zero by Division'
#
#
# try:
#     a, b = map(int, input().split())
#     res = div(a, b)
#     print(res)
# except ValueError:
#     print('TYPE ERROR')

def func2():
    return 1 / 0


def func1():
    return func2()


print('str1')
print('str2')
func1()
print('str3')
print('str4')

# print('строка 1')
# print('строка 2')
# print('строка 3')
# # print(a)
# 1/0
# print('строка 4')
# print('строка 5')
# print('строка 6')
# print('строка 7')

# try:
#     file = open('mygile.txt')
# except FileNotFoundError:
#     print('Невозможно открыть файл')

# try:
#     x, y = map(int, input().split())
#     res = x / y
#     # print(res)
# except (ZeroDivisionError, ValueError):
#     print('Делить на 0 нельзя')
# except ValueError:
#     print('Ошибка типа данных')


# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError as z:
#     print(z)
# except ValueError as z:
#     print(z)


# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ValueError:
#     print('Ошибка типа данных')
# except Exception as e:
#     # print('Делить на 0 нельзя')
#     print(e)

# try:
#     x, y = map(int, input().split())
#     res = x / y
# except:
#     print('Error')

# try:
#     lst = [1, 2, 3]
#     print(lst[6])
# except IndexError :
#     print('OUT RANGE')


# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError as z:
#         print(z)
# except ValueError as z:
#         print(z)
# else:
#     print('Исключений не произошло')
# finally:
#     print('Блок finally выполняется всегда')


# try:
#     f = open("myfile.txt", 'w')
#     f.write('Hello')
# except FileNotFoundError as z:
#     print(z)
# except:
#     print('Other Error!!')
# finally:
#     if f:
#         f.close()
#         print('File closed')


# try:
#     with open("myfile.txt", 'a') as f:
#         f.write('\nhello' )
# except FileNotFoundError as z:
#     print(z)
# except:
#     print('Other Error')


# def get_value():
#     try:
#         x, y = map(int, input().split())
#         return x, y
#     except ValueError as v:
#         print(v)
#         return 0, 0
#     finally:
#         print('Finally accept before return')
#
#
# print(get_value())

# try:
#     x, y = map(int, input().split())
#     try:
#         res = x / y
#     except ZeroDivisionError:
#         print('Zero by Division')
# except ValueError:
#     print('TYPE ERROR')


# def div(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return 'Zero by Division'
#
#
# try:
#     a, b = map(int, input().split())
#     res = div(a, b)
#     print(res)
# except ValueError:
#     print('TYPE ERROR')

def func2():
    return 1 / 0


def func1():
    return func2()


print('str1')
print('str2')
func1()
print('str3')
print('str4')

