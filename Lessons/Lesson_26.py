# class Transport:
    
#     def __init__(self, speed, color) -> None:
#         self.speed = speed
#         self.color = color
        
#     def beep(self):
#         print('beep')

# tr = Transport(180, 'black')
# # tr.beep()


# class Car(Transport):
    
#     def __init__(self, speed, color, owner) -> None:
#         super().__init__(speed, color)
#         self.owner = owner
        
#     def say_owner(self):
#         print(f'Владелец {self.owner}')
        
#     def move(self):
#         print('Car moving')
        

# class Bus(Transport):
    
#     def __init__(self, speed, color,seeds) -> None:
#         super().__init__(speed, color)
#         self.seeds = seeds
        
#     def say_seeds(self):
#         print(f'Кол-во мест {self.seeds}')
        
# car1 = Car(100, 'red', 'Peter')
# print(car1.color)
# print(car1.speed)
# print(car1.owner)
# car1.beep()
# car1.say_owner()
# bus1 = Bus(60, 'green', 33)
# bus1.say_seeds()

# class SportCar(Car, Transport):
#     pass


# car2 = SportCar(200 , 'black', 'John')
# car2.beep()
# car2.say_owner()
# car2.beep()
# car2.move()


class Person():
    
    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        
class Student(Person):
    def __init__(self, name, surname, age, subject) -> None:
        super().__init__(name, surname, age)
        self.subject = subject

p = Person('ivan', 'ivanov', 55)
s = Student('Anna', 'Petrova', 15, 'Python')

print(p.__dict__) 
print(s.__dict__) 