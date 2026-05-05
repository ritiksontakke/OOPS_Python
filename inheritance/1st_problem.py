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


