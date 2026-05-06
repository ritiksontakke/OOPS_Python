# ============================================================
# PILLAR: Polymorphism
# PROGRAM 16: Method Overriding — Animal Sounds
# ============================================================
#
# PROBLEM:
# Polymorphism means "many forms." The same method name can
# behave DIFFERENTLY in different classes.
#
# Create a base class Animal with:
# - speak(): prints "Some generic animal sound"
#
# Create subclasses that each OVERRIDE speak():
# - Dog: speak() → "Woof! Woof!"
# - Cat: speak() → "Meow!"
# - Cow: speak() → "Moo!"
# - Duck: speak() → "Quack!"
#
# Then write a function make_noise(animal) that calls
# animal.speak() — it works for ANY animal type!
#
# KEY CONCEPT:
# Same function make_noise() works on Dog, Cat, Cow, Duck.
# Python decides at runtime which speak() to call.
# This is called Runtime Polymorphism.
#
# EXAMPLE USAGE:
#   animals = [Dog(), Cat(), Cow(), Duck()]
#   for a in animals:
#       make_noise(a)
#
# OUTPUT:
#   Woof! Woof!
#   Meow!
#   Moo!
#   Quack!
# ============================================================

class Animal :

    def speak(self):
        print("Some genric animal sound")
    
# overridding 

class Dog(Animal):
    def speak(self):
        print("woof woof")

class Cat(Animal):
    def speak(self):
        print("meow meow")

class Cow(Animal):
    def speak(self):
        print("Moo!")


class Duck(Animal):
    def speak(self):
        print("Quack!")


# Function using polymorphism
def make_noise(animal):
    animal.speak()

animals = [Dog(), Cat(), Cow(), Duck()]

for a in animals:
    make_noise(a)