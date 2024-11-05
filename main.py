# class Car:

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def car_type(self):
#         return f"I like {self.make} {self.model} {self.year} car"
    
# car1 = Car("Toyota", "Camry", 2021)
# car2 = Car("Honda", "Civic", 2016)

# print(car1.make)
# print(car1.model)
# print(car1.year)
# print(car1.car_type())
# print(car2.car_type())


# class Person:

#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def my_info(self):
#         return f"My name is {self.name}, I'm {self.age} years old, I'm also a {self.gender}"
    
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# gender = input("Enter your gender: ")

# person = Person(name, age, gender)

# print(person.my_info())
        

# class Car:

#     def __init__(self, make, model, year, speed=0):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = speed

#     def accelerate(self, increase):
#         self.speed += increase
#         return f"{self.make} {self.model} {self.year} speed increase by {self.speed} km/hr"
    
#     def brake(self, decrease):
#         self.speed -= decrease
#         return f"{self.make} {self.model} {self.year} speed decrease by {self.speed} km/hr"
    
#     def __str__(self):
#         return f"{self.make} {self.model} {self.year} at {self.speed} km/hr"
    
# car1 = Car("Honda", "Accord", 2017)

# print(car1)
# print(car1.accelerate(50))
# print(car1)
# print(car1.brake(20))
# print(car1)


# import re

# text = "The rain in Spain stays mainly in the plain."

# find_all = re.findall(r"in", text)

# search = re.search(r"in", text)

# sub = re.sub(r"Spain", "France", text)

# split = re.split(r" ", text)

# print(find_all)

# print(search)

# print(sub)

# print(split)

import json

person = {
    "name": "Alice",
    "age": 30,
    "email": "olamide@gmailcom",
    "is_verify": False
}

print(person)

json_dumps = json.dumps(person)

python_load = json.loads(json_dumps)

print(python_load)

with open("json_text.json", "w") as json_file:
    json.dump(person, json_file)
    # print(json_file)

with open("json_text.json", "r") as json_file:
    py_file = json.load(json_file)
    print("File convert to PY object:", py_file)



