'''
Public members are variables or methods that can be accessed from anywhere inside the class, outside the class or from other modules. 
By default, all members in Python are public. They are defined without any underscore prefix
Docstring for OOP.PublicMembers
'''

class Employee:
    def __init__(self, name):
        self.name = name   # public attribute

    def display_name(self):   # public method
        print(self.name)

emp = Employee("John")
emp.display_name()   # Accessible
print(emp.name)      # Accessible