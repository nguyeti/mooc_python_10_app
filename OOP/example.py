class Machine:
    def __init__(self):
        print("I am a Machine")

class DrivingMachine(Machine):
    def __init__(self):
        print("I am a DrivingMachine")

    def start(self):
        print("Machine starts")

class Bike(DrivingMachine):
    def __init__(self, brand, color):
        self.brand = brand # __attrName > makes it private
        self.color = color
        print("I am a Bike")

    def start(self):
        print("Override : Bike starts")

    def getattr(self, name):
        return self.name

class Car(DrivingMachine):
    def __init__(self, brand, color):
        self.__color = color # __attrName > makes it private  Can't be seen and accessed from outside
        self._brand = brand # _A > makes it protected Like a public member, but they shouldn't be directly accessed from outside.
        print("I am a Car")

    def start(self):
        print("Override : car starts")

    def changeColor(self, color):
        self.__color = color
# machine = Machine()
# d = DrivingMachine()
# bike = Bike("Suzuki", "red")
# car = Car("Toyota", "black")
# d.start() # calls the parent's start() method
# bike.start()
# car.start()
#
# print("Bike : " + bike.brand + " : " + bike.color)
# print("Bike : " + getattr(bike,"brand") + " : " + getattr(bike,"color"))
# print(hasattr(bike, "color"))
# setattr(bike, "color", "yellow")
# print("Bike : " + getattr(bike,"brand") + " : " + getattr(bike,"color"))
# # print(issubclass(Bike,Machine))
# # print(issubclass(Bike,DrivingMachine))
# # print(isinstance(bike,Machine))
# # print(isinstance(bike,DrivingMachine))
#
# # print("Car : " + car.brand + " : " + car.color) # AttributeError: 'Car' object has no attribute 'brand'
# # print("Car : " + getattr(car, "brand") + " : " + car.color) # pareil fonctionne pas
# print("Car :" + car._Car__color)
# car._Car__color ="purple"
# print("Car :" + car._Car__color)
