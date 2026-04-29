# ============================================================
# PILLAR: Abstraction
# PROGRAM 7: Abstract Animal
# ============================================================
#
# PROBLEM:
# Create an abstract Animal class with two abstract methods:
# - speak(): returns the sound the animal makes
# - move(): returns how the animal moves
#
# Implement three concrete classes:
# - Dog: speaks "Woof!", moves "runs on four legs"
# - Bird: speaks "Tweet!", moves "flies with wings"
# - Fish: speaks "...(blub)", moves "swims with fins"
#
# Also add a non-abstract method describe() in Animal that
# uses speak() and move() to print a description.
#
# EXAMPLE USAGE:
#   animals = [Dog("Rex"), Bird("Tweety"), Fish("Nemo")]
#   for a in animals:
#       a.describe()
#
# OUTPUT:
#   Rex says: Woof! and runs on four legs
#   Tweety says: Tweet! and flies with wings
#   Nemo says: ...(blub) and swims with fins

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def describe(self):
        print(f"{self.name} says : {self.speak()} and {self.move()}")

class Dog(Animal):
    def speak(self):
        return "woof"
    
    def move(self):
        return "runs on four legs"
    
class Bird(Animal):
    def speak(self):
        return "Tweet"
    
    def move(self):
        return "files with wings"
    
animals = [Dog("Rex"), Bird("Ritik")]

for a in animals:
    a.describe()
    