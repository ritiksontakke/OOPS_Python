# ============================================================
# PILLAR: Inheritance
# PROGRAM 11: Animal → Dog and Cat
# ============================================================
#
# PROBLEM:
# Create a base class Animal with:
# - __init__(name, age)
# - eat(): prints "{name} is eating."
# - sleep(): prints "{name} is sleeping."
# - __str__(): returns "Animal: {name}, Age: {age}"
#
# Create a subclass Dog(Animal) that:
# - adds breed in __init__
# - adds fetch(item): prints "{name} fetched the {item}!"
# - overrides __str__ to include breed
#
# Create a subclass Cat(Animal) that:
# - adds color in __init__
# - adds purr(): prints "{name} is purring..."
# - overrides __str__ to include color
#
# KEY CONCEPT:
# Dog and Cat inherit eat() and sleep() from Animal.
# They only define what is NEW or DIFFERENT.
#
# EXAMPLE USAGE:
#   dog = Dog("Bruno", 3, "Labrador")
#   dog.eat()          # Bruno is eating.
#   dog.fetch("ball")  # Bruno fetched the ball!
#   print(dog)         # Dog: Bruno, Age: 3, Breed: Labrador
#
#   cat = Cat("Whiskers", 2, "orange")
#   cat.sleep()        # Whiskers is sleeping.
#   cat.purr()         # Whiskers is purring...
#   print(cat)         # Cat: Whiskers, Age: 2, Color: orange
# ============================================================

class Animal :

    def __init__(self, name , age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def __str__(self):
        return f"Animal : {self.name}, Age : {self.age}"
    
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def fetch(self, item):
        print(f"{self.name} fetched the {item}!")

    def __str__(self):
        return f"Dog : {self.name}, Age: {self.age}, breed : {self.breed}"
    
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # Call parent constructor
        self.color = color

    def purr(self):
        print(f"{self.name} is purring...")

    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}, Color: {self.color}"
    
dog = Dog("Bruno", 3, "Labrador")
dog.eat()          # Bruno is eating.
dog.fetch("ball")  # Bruno fetched the ball!
print(dog)         # Dog: Bruno, Age: 3, Breed: Labrador

print()  # Just for spacing