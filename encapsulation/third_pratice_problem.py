# ============================================================
# PILLAR: Encapsulation
# PROGRAM 3: Employee Salary (Getter & Setter)
# ============================================================
#
# PROBLEM:
# Create an Employee class where salary is private.
# Use Python @property to create a getter and setter.
# - Salary cannot be negative.
# - Salary cannot exceed 200000.
# - Use @property for get_salary and @salary.setter for set.
#
# EXAMPLE USAGE:
#   emp = Employee("Carol", 50000)
#   print(emp.salary)         # 50000
#   emp.salary = 75000        # OK
#   emp.salary = -100         # "Salary cannot be negative!"
#   emp.salary = 300000       # "Salary exceeds maximum limit!"
#   print(emp.salary)         # 75000

class Employee:

    Max_Salary = 200000

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        self.salary = salary
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("salary cannot be negative")
        elif value > 200000:
            print("salary excued minium limit")
        else:
            self._salary = value

emp = Employee("ritik" , 50000)

print(emp.salary)

emp.salary = -85

print(emp.salary)