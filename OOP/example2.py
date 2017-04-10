from example import *

# car = Car("TOyota","red")
# car._Car__color = "yellow"
# # print(car.__color) # marche pas car color privé
# print(car._brand)
# car.changeColor("RED")

class MiniCar(Car):
    pass

mc = MiniCar("Mini", "reds")
print(mc._brand)
print(mc.__color)


PRIVATE : ACCESSIBLE FROM INSIDE THE CLASS ONLY
PROTECTED : ACCESSIBLE FROM INSIDE THE CLASS AND ITS SUBCLASSES
