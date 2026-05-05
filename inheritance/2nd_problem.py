# ============================================================
# PILLAR: Inheritance
# PROGRAM 12: Person → Student and Teacher
# ============================================================
#
# PROBLEM:
# Create a base class Person with:
# - __init__(name, age)
# - greet(): prints "Hi, I'm {name} and I'm {age} years old."
#
# Create a subclass Student(Person) that:
# - adds school and grade in __init__
# - adds study(subject): prints "{name} is studying {subject}."
# - adds show_info(): prints name, age, school, grade
#
# Create a subclass Teacher(Person) that:
# - adds subject and school in __init__
# - adds teach(): prints "{name} is teaching {subject}."
# - adds show_info(): prints name, age, school, subject
#
# EXAMPLE USAGE:
#   s = Student("Aryan", 16, "City High School", 10)
#   s.greet()              # Hi, I'm Aryan and I'm 16 years old.
#   s.study("Math")        # Aryan is studying Math.
#   s.show_info()
#
#   t = Teacher("Mrs. Sharma", 35, "Physics", "City High School")
#   t.greet()              # Hi, I'm Mrs. Sharma and I'm 35 years old.
#   t.teach()              # Mrs. Sharma is teaching Physics.
#   t.show_info()
# ============================================================

# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


# Subclass: Student
class Student(Person):
    def __init__(self, name, age, school, grade):
        super().__init__(name, age)
        self.school = school
        self.grade = grade

    def study(self, subject):
        print(f"{self.name} is studying {subject}.")

    def show_info(self):
        print("Student Info:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"School: {self.school}")
        print(f"Grade: {self.grade}")


# Subclass: Teacher
class Teacher(Person):
    def __init__(self, name, age, subject, school):
        super().__init__(name, age)
        self.subject = subject
        self.school = school

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def show_info(self):
        print("Teacher Info:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"School: {self.school}")
        print(f"Subject: {self.subject}")


# Example usage
s = Student("Aryan", 16, "City High School", 10)
s.greet()
s.study("Math")
s.show_info()

print()  # Just for spacing

t = Teacher("Mrs. Sharma", 35, "Physics", "City High School")
t.greet()
t.teach()
t.show_info()