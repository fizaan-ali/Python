class Car:

    color = None

class Motorcycle:

    color = None

def change_color(vehicle, color):
    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

mot_1 = Motorcycle()
mot_2 = Motorcycle()

change_color(color="blue", vehicle=car_1) #keyword argument
change_color(car_2, "orange") # positional argument
change_color(car_3, "Black")
change_color(mot_1, "white")
change_color(vehicle=mot_2, color="Grey")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(mot_1.color)
print(mot_2.color)