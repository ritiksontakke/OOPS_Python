# ============================================================
# PILLAR: Encapsulation
# PROGRAM 2: Student Grades
# ============================================================
#
# PROBLEM:
# Create a Student class that keeps grades private.
# - Grades list should not be directly modifiable from outside.
# - Provide add_grade(grade) to add a grade (0-100 only).
# - Provide get_average() to return the average grade.
# - Provide get_grades() to return a copy of the grades list.
#
# EXAMPLE USAGE:
#   s = Student("Bob")
#   s.add_grade(85)
#   s.add_grade(92)
#   s.add_grade(110)    # "Invalid grade! Must be between 0 and 100."
#   print(s.get_average())  # 88.5
#   print(s.get_grades())   # [85, 92]

class Student:

    def __init__(self, name):
        self.name = name
        self.__grades= []
    
    def add_grade(self, grade):
        if 0 <= grade <=100:
            self.__grades.append(grade)
        else:
            print("Invalid grade")
    
    def get_avg(self):
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)
    
    def get_grade(self):
        return self.__grades.copy()
    
s1 = Student("vicky")
s1.add_grade(88)

print(s1.get_grade())