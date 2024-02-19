# ----------------------------------------------------------------------------#
# import time
#
# import arcade
#
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
#
# CHARACTER_SCALING = 1
# TILE_SCALING = 0.5
#
# PLAYER_MOVEMENT_SPEED = 5
#
# GRAVITY = 2
# PLAYER_JUMP_SPEED = 20
#
#
# class Player(arcade.Sprite):
#     def __init__(self):
#         super().__init__(
#             ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
#             CHARACTER_SCALING,
#         )
#         self.center_x = 64
#         self.center_y = 128
#
#     def update(self):
#         self.center_x += self.change_x
#         self.center_y += self.change_y
#         self.center_y -= GRAVITY
#         if self.center_y <= 128:
#             self.center_y = 128
#             game.isGround = True
#
#
# class Box(arcade.Sprite):
#     def __init__(self):
#         super().__init__(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
#         self.change_y = 2
#
#     def update(self):
#         self.center_y += self.change_y
#         if self.top >= 500 or self.bottom <= 64:
#             self.change_y = -self.change_y
#
#
# class Game(arcade.Window):
#     def __init__(self):
#         super().__init__(
#             width=SCREEN_WIDTH,
#             height=SCREEN_HEIGHT,
#             title="Работа со спрайтами",
#         )
#         self.player_sprite = None
#         self.scene = None
#
#         self.isGround = True
#
#     def setup(self):
#         self.scene = arcade.Scene()
#         self.scene.add_sprite_list("Player")
#         self.scene.add_sprite_list("Walls", use_spatial_hash=True)
#
#         self.player_sprite = Player()
#         self.scene.add_sprite("Player", self.player_sprite)
#
#         for x in range(0, 1250, 64):
#             ground = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
#             ground.center_x = x
#             ground.center_y = 32
#             self.scene.add_sprite("Walls", ground)
#
#         # coordinate_list = [[512, 96], [256, 96], [768, 96]]
#
#         self.box = Box()
#         self.box.position = [512, 96]
#         self.scene.add_sprite("Walls", self.box)
#
#     def on_draw(self):
#         self.clear()
#         self.scene.draw()
#
#     def on_key_press(self, key, modifiers):
#         if self.isGround:
#             if key == arcade.key.UP or key == arcade.key.W:
#                 self.player_sprite.change_y = PLAYER_JUMP_SPEED
#                 self.isGround = False
#         if key == arcade.key.LEFT or key == arcade.key.A:
#             self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
#         elif key == arcade.key.RIGHT or key == arcade.key.D:
#             self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
#
#     def on_key_release(self, key, modifiers):
#         if key == arcade.key.LEFT or key == arcade.key.A:
#             self.player_sprite.change_x = 0
#         elif key == arcade.key.RIGHT or key == arcade.key.D:
#             self.player_sprite.change_x = 0
#         elif key == arcade.key.W or key == arcade.key.UP:
#             self.player_sprite.change_y = 0
#
#     def update(self, delta_time: float):
#         self.player_sprite.update()
#         self.box.update()
#
#
# if __name__ == "__main__":
#     game = Game()
#     game.setup()
#     arcade.run()

# ----------------------------------------------------------------------------#
# import math


# class Square:
#     def __init__(self, side_length):
#         self.side_length = side_length

#     def area(self):
#         return self.side_length ** 2


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area2(self):
#         return math.pi * self.radius ** 2


# class CircleToSquare(Square, Circle):
#     def __init__(self, side_length):
#         Square.__init__(self, side_length)
#         Circle.__init__(self, side_length / 2)

#     def info(self):
#         print(f'Side a square: {self.side_length}')
#         print(f'Area a square: {self.area():.2f}')
#         print(f'Radius a circle: {self.radius}')
#         print(f'Area a circle: {self.area2():.2f}')


# s = Square(5)
# c = Circle(5)
# cs = CircleToSquare(5)

# cs.info()
# ----------------------------------------------------------------------------#

# class A:
#     def method_a(self):
#         print('Method class A')
#
#
# class B:
#     def method_b(self):
#         print('Method class B')
#
#
# class C(A, B):
#     def method_c(self):
#         print('Method class C')
#
#
# obj = C()
# obj.method_a()
# obj.method_b()
# obj.method_c()
# ----------------------------------------------------------------------------#
# class Car:
#     def __init__(self, brand):
#         self.brand = brand


# class Value:
#     def __init__(self, value):
#         self.value = value


# class Wheels:
#     def __init__(self, count_w):
#         self.count_w = count_w

# class Auto(Car, Value, Wheels):
#     def __init__(self, brand, value, count_w):
#         Car.__init__(self, brand)
#         Value.__init__(self, value)
#         Wheels.__init__(self, count_w)
#     def info(self):
#         print(self.brand)
#         print(self.value)
#         print(self.count_w)

# a = Auto('BMW', 1600, 4)
# a.info()

# ----------------------------------------------------------------------------#

# Задание 1
# Создайте класс Число (или используйте уже ранее
# созданный вами). Класс число хранит внутри одно зна-
# чение. Используя перегрузку операторов реализуйте для
# него арифметические операции для работы с числом
# (операции +, -, *, /).

# class Number:
#     def __init__(self, value) -> None:
#         self.value = value

#     def __add__(self, num):
#         return self.value + num.value

#     def __sub__(self, num):
#         return self.value - num.value

#     def __mul__(self, num):
#         return self.value * num.value

#     def __truediv__(self, num):
#         return self.value / num.value


# c = Number(25)
# c2 = Number(5)
# print(c + c2)
# print(c - c2)
# print(c * c2)
# print(c / c2)
# ----------------------------------------------------------------------------#

# Задание 2
# Создайте класс Дробь (или используйте уже ранее
# созданный вами). Используя перегрузку операторов ре-
# ализуйте для него арифметические операции для работы
# с дробями (операции +, -, *, /)

# class Fraction:
#     def __init__(self, n, d) -> None:
#         self.n = n
#         self.d = d

#     def __add__(self, num):
#         new_n = self.n * num.d + num.n * self.d
#         new_d = self.d * num.d
#         # return f'{new_n} / {new_d}'

#         return Fraction(new_n, new_d)

#     def __sub__(self, num):
#         new_n = self.n * num.d - num.n * self.d
#         new_d = self.d * num.d
#         return Fraction(new_n, new_d)

#     def __mul__(self, num):
#         new_n = self.n * num.n
#         new_d = self.d * num.d
#         return Fraction(new_n, new_d)

#     def __truediv__(self, num):
#         if num.n != 0:
#             new_n = self.n * num.d
#             new_d = self.d * num.n
#             return Fraction(new_n, new_d)
#         else:
#             raise ValueError('DIVISION BY ZERO')

#     def __str__(self) -> str:
#         return f'{self.n}/{self.d}'


# fraction1 = Fraction(1, 2)
# fraction2 = Fraction(3, 4)

# result_add = fraction1 + fraction2
# result_sub = fraction1 - fraction2
# result_mul = fraction1 * fraction2
# result_div = fraction1 / fraction2

# print("Addition:", result_add)
# print("Subtraction:", result_sub)
# print("Multiplication:", result_mul)
# print("Division:", result_div)
# ----------------------------------------------------------------------------#
# Задание 3
# Создайте класс Библиотека. Класс предназначен для
# хранения информации о библиотеке (название, адрес, ко-
# личество книг и т.д.). Реализуйте необходимые для класса
# методы. Используя перегрузку операторов реализуйте для
# него следующие арифметические операции:
# ■ + добавляет к количеству книг указанное значение;
# ■ - вычитает из количества книг указанное значение;

# ■ += добавляет к количеству книг указанное значение;
# ■ -= вычитает из количества книг указанное значение;
# Используя перегрузку операторов реализуйте (срав-
# нение по количеству книг):
# ■ <; ■ >; ■ <=; ■ >=; ■ ==; ■ !=.

# class Library:
#     def __init__(self, name, address, qty) -> None:
#         self.name = name
#         self.address = address
#         self.qty = qty

#     def __add__(self, num):
#         return self.qty + num.qty

#     def __sub__(self, num):
#         return self.qty - num.qty

#     def __iadd__(self, num):
#         self.qty += num
#         return self

#     def __isub__(self, num):
#         self.qty -= num
#         return self

#     def __lt__(self, num):
#         return self.qty < num.qty

#     def __gt__(self, num):
#         return self.qty > num.qty

#     def __le__(self, num):
#         return self.qty <= num.qty

#     def __ge__(self, num):
#         return self.qty >= num.qty

#     def __eq__(self, num):
#         return self.qty == num.qty

#     def __ne__(self, num):
#         return self.qty != num.qty


# l = Library('Anna', 'f2', 5)
# l2 = Library('Anna', 'f2', 1)
# # print(l + l2)
# # print(l - l2)
# l += 12
# print(l.qty)
# l -= 7
# print(l.qty)
# library1 = Library('Library1', 'Address1', 10)
# library2 = Library('Library2', 'Address2', 5)

# print(library1 < library2)
# print(library1 > library2)
# print(library1 <= library2)
# print(library1 >= library2)
# print(library1 == library2)
# print(library1 != library2)

# ----------------------------------------------------------------------------#

