# ----------------------------------------------------------------------------#
# class Stars:
#     def __init__(self, n):
#         self.qty = '*' * n
#
#     def __add__(self, n):
#         return self.qty + '*' * n
#
#
# a = Stars(3)
# b = a + 5
# print(b)
# ----------------------------------------------------------------------------#
# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         return self.value + other.value
#
#     def __sub__(self, other):
#         return self.value - other.value
#
#     def __mul__(self, other):
#         return self.value * other.value
#
#     def __truediv__(self, other):
#         if other.value != 0:
#             return self.value / other.value
#         else:
#             raise ZeroDivisionError('Делить на 0 нельзя')
#
#
# num1 = Number(10)
# num2 = Number(5)
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)

# ----------------------------------------------------------------------------#

# class A:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __str__(self):
#         return str(self.arg)
#
#
# #
# class B:
#     def __init__(self, *args):
#         self.alist = []
#         for i in args:
#             self.alist.append(A(i))
#
#     def __getitem__(self, i):
#         return self.alist[i]
#
#
# group = B(4, 6, 'abs')
# print(group.alist[1])
# print(group[0])
# a = A(8)
# print(a)
# ----------------------------------------------------------------------------#

# class Changeable:
#     def __init__(self, color):
#         self.color = color
#
#     def __call__(self, newcolor):
#         self.color = newcolor
#
#     def __str__(self):
#         return self.color
#
#
# canvas = Changeable('green')
# frame = Changeable('Blue')
# canvas('red')
# frame('yellow')
# print(canvas, frame)

# ----------------------------------------------------------------------------#
import math


#
# class Fraction:
#     def __init__(self, n, d):
#         self.n = n
#         self.d = d
#
#     def __add__(self, other):
#         new_n = self.n * other.d + other.n * self.d
#         new_d = self.n * other.d
#         # return f'{math.gcd(new_n)}/{math.gcd(new_d)}'
#         return f'{self.n * other.d + other.n * self.d}/{self.n * other.d}'
#
#     def __sub__(self, other):
#         return f'{self.n * other.d - other.n * self.d} / {self.n * other.d}'
#
#     def __mul__(self, other):
#         return f'{self.n * other.n} / {self.d * other.d}'
#
#     def __truediv__(self, other):
#         if  other.d != 0:
#             return f'{self.n * other.d} / {self.d * other.n}'
#         else:
#             raise ZeroDivisionError('Делить на 0 нельзя')
#
#
# f = Fraction(2, 2)
# f2 = Fraction(4, 5)
# print(f + f2)
# print(f - f2)
# print(f * f2)
# print(f / f2)
# ----------------------------------------------------------------------------#
class Library:
    def __init__(self, name, address, qty):
        self.name = name
        self.address = address
        self.qty = qty

    def __add__(self, other):
        return self.qty + other.qty

    def __sub__(self, other):
        return self.qty - other.qty

    def __iadd__(self, other):
        self.qty += other
        return self

    def __isub__(self, other):
        self.qty -= other
        return self

    def __lt__(self, other):
        return self.qty < other.qty

    def __gt__(self, other):
        return self.qty > other.qty

    def __le__(self, other):
        return self.qty <= other.qty

    def __ge__(self, other):
        return self.qty >= other.qty

    def __eq__(self, other):
        return self.qty == other.qty

    def __ne__(self, other):
        return self.qty != other.qty


l = Library('Pushkin', 'address', 20)
l2 = Library('HHH', 'aadd', 30)
l += 10
print(l.qty)
l -= 15
print(l.qty)
print(l > l2)
print(l < l2)
print(l >= l2)
print(l <= l2)
print(l == l2)
print(l != l2)
