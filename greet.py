class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0 

    def accelerate(self, increase):
        self.speed += increase
        print(f"The car accelerates to {self.speed} km/h.")

    def brake(self, decrease):
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0
        print(f"The car slows down to {self.speed} km/h.")

    def __str__(self):
        return f"{self.year} {self.color} {self.make} {self.model} at {self.speed} km/h"


my_car = Car("Toyota", "Corolla", 2021, "blue")


print(my_car)             
my_car.accelerate(50)
print(my_car)
my_car.brake(20)           
print(my_car)              
