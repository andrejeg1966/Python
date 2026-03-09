"""
Protected members are variables or methods that are intended to be accessed only within the class and its subclasses.
They are not strictly private but should be treated as internal.
In Python, protected members are defined with a single underscore prefix (e.g., self._name).
Docstring for OOP.ProtectedMembers
"""


class Employee:
    def __init__(self, name, age):
        self.name = name  # public
        self._age = age  # protected


class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)  # Accessible in subclass


emp = SubEmployee("Ross", 30)
print(emp.name)  # Public accessible
emp.show_age()  # Protected accessed through subclass
