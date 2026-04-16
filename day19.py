'''
Introduction to OOP's
classes
objects
attributes
methods

OOP's
------
-->Object-Oriented Language(oop) is a style of programming where we model real world things
as objects that contain both data and functions()
-->reusability of code 

Class
------
-->it is a blue print or template that defines what kind of data and behaviour a certain
type of object will have

syntax:-
class class_name:
    pass

Object
-------
-->this is instance of class or an object is a real instance created from the class
it is the actual thing that exists in memory while the program runtime.

syntax:-
class car:
    pass
car1=car()   #object
car2=car()   #object

attributes:-
-------------
-->these are variables that store data related to a class or object

class car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
car_1=car("Toyota","white")
car_2=car("Thar","red")
print(car_1.brand)
print(car_1.color)
print(car_2.brand)
print(car_2.color)

class dog:
    def __init__(self,breed,shape):
        self.breed=breed
        self.shape=shape
dog_1=dog("bull dog","muscular")
dog_2=dog("shiba","small and puffy")
print(dog_1.shape)
print(dog_1.breed)
        
#different animals,food,vegetables,fruits,humans
'''
class car:
    wheels=4
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.mileage=20
    def drive(self,miles):
        self.mileage+=miles
        return f"Drove {miles} miles,total: {self.mileage}"

    def info(self):
        return f"{self.make} {self.model} {self.year}"
car_1=car("ford","mustang", "2008")
car_2=car("toyota","camry", "2026")
print(car_1.model)
print(car_2.make)





























