# ------------------------------------------------------------------------#
'''
У нас есть 4 паттерна:
Порождающий- представляет возможность создпния контролируемым образом иницилизации
и конфигурации объектов на основе требуемых критериев.

Структурный - помогает организовывать структуры связаных объктов и классов, предостовляя
новые функциональные возможности

Поведеньческие - направлены на выявления общих моделей взаимодействия между объектами

Concurrency(Паралелизм)(тип паттернов проетироавние) - который имеет с много поточной парадигмой программирования.

Singletone  - паттернов проетироавние цель которого ограничеть возможность создания объектов одним экземпляром
он обеспечивает глобалность до одного экз. и глобальный доступ к созданному объекту.
'''

# class Singletone:
#     _instance = None
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(Singletone, cls).__new__(cls)
#         return cls._instance
#
#     def __init__(self):
#         pass
#
#
# sin = Singletone()
# sin2 = Singletone()
# print(sin is sin2)

# ------------------------------------------------------------------------#

# class GameManager:
#     _instance = None
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(GameManager, cls).__new__(cls)
#             cls._instance.state = 'initialized'
#             # cls._instance.state = 56
#         return cls._instance
#
#
# game = GameManager()
# game2 = GameManager()
# game.state = 'running'
# print(game2.state)

# ------------------------------------------------------------------------#
#
# class Logger:
#
#     _instance = None
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(Logger, cls).__new__(cls)
#         return cls._instance
#
#     def log(self, msg):
#         print('Logging: ', msg)
#     def create_user(self, username):
#         self.logger.log(f'User "{username}" created')
# class UserManager:
#     def __init__(self):
#         self.logger = Logger()
#
#     def create_user(self, username):
#         self.logger.log(f'User "{username}" created')
#
# user = UserManager()
# user2 = UserManager()
# user.create_user('John')
# user2.create_user('John')
# print(user is user2)

# ------------------------------------------------------------------------#
# class Logger:
#     def log(self, msg):
#         print('Logging: ', msg)
#
#
# class UserManager:
#     def __init__(self):
#         self.logger = Logger()
#
#     def create_user(self, username):
#         self.logger.log(f"User {username} created")
#
#
# class Database:
#     def save_user(selfself, user_data):
#         print("Saving user to the database:", user_data)
#
# class UserService:
#     def __init__(self):
#         self.user_manager = UserManager()
#         self.database = Database()
#
#     def create_user(self, username):
#         self.user_manager.create_user(username)
#         user_data = username
#         self.database.save_user(user_data)
#
# user = UserService()
# user.create_user('John Doe')

# ------------------------------------------------------------------------#
class AbstractFactory(object):
    def create_drink(self):
        raise NotImplementedError()

    def create_food(self):
        raise NotImplementedError()


class Drink(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Food(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class ConcreteFactory1(AbstractFactory):
    def create_drink(self):
        return Drink('Coca-cola')

    def create_food(self):
        return Food('Hamburger')


class ConcreteFactory2(AbstractFactory):
    def create_drink(self):
        return Drink('Pepsi')

    def create_food(self):
        return Food('Cheeseburger')


def get_factory(ident):
    if ident == 0:
        return ConcreteFactory1()
    elif ident == 1:
        return ConcreteFactory2()

factory = get_factory(0)
print(factory.create_drink())  # Pepsi
print(factory.create_food())  # Cheeseburger


















