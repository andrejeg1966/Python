'''
Created on 06.03.2025

@author: goran
'''
try:
    10 / "ss"
except ZeroDivisionError as e:
    print("Fehler: " + str(e))
except TypeError as e:
    print("Type Fehler: "+ str(e))
        

try:
    x = int("str")  # This will cause ValueError
    inv = 1 / x   # Inverse calculation
    
except ValueError as e:
    print("Not Valid!: " + str(e))
    
print("*************Catching Multiple Exceptions*****************")
a = ["10", "twenty", 30]  # Mixed list of integers and strings
try:
    total = int(a[0]) + int(a[3])  # 'twenty' cannot be converted to int
    
except (ValueError, TypeError) as e:
    print("Error: ", str(e))
    
except IndexError:
    print("Index out of range.")
print("****************Catch-All Handlers and Their Risks*****************")
try:  
    res = "100" / 20 # Risky operation: dividing string by number
except (ArithmeticError) as e:
    print("Aritmetic Error: ", str(e))
except:
    print("Something went wrongS")

print("**********Raise an Exception*************")
def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)

print("***************Custom Exceptions***************")  
class AgeError(Exception):
    pass

def set(age):
    if age < 0:
        raise AgeError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except AgeError as e:
    print(e)
    

# Step 1: Define a custom exception class
class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120"):
        self.age = age
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.age} -> {self.msg}'

# Step 2: Use the custom exception in your code
def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print(f"Age set to: {age}")

# Step 3: Handling the custom exception
try:
    set_age(150)  # This will raise the custom exception
except InvalidAgeError as e:
    print(e)
    
class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120", error_code=1001):
        self.age = age
        self.msg = msg
        self.error_code = error_code
        super().__init__(self.msg)

    def __str__(self):
        return f"[Error Code {self.error_code}] {self.age} -> {self.msg}"
        
try:
    set_age(150)  # This will raise the custom exception
except InvalidAgeError as e:
    print(e)