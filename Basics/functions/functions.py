'''
Created on 06.03.2025

@author: goran
'''


print("**********Einfache Funktion**************")
def add (a, b):
    return (a + b)

x = add(3, 4)
print(x)


print("**********args argumenten**************")
#This way, the function will receive a tuple of arguments and can access the items accordingly:
print("**********Example 1**************")
def addVar(*args):
    result = 0
    for arg in args:
        result += arg
    return result
x = addVar(2,3)
y = addVar(2,3,4)
z = addVar(2,3,4,5)
print(x)
print(y)
print(z)

print("\n**********Example 2**************")
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

print("\n**********Example 3**************")
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

print("\n**********Example 4**************")
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus") #Regular parameters must come before *args:


print("\n**********kwargs argumenten**************")
#This way, the function will receive a tuple of arguments and can access the items accordingly:
print("**********Example 1**************")
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

print("\n**********Example 2**************")
def addArgKwarg(*args, **kwargs):
    for arg in args:
        print(f" Args: {arg}")
    for key, value in kwargs.items():
        print(f"Kwargs: {value}")
        
print(addArgKwarg(2,3, z=10))

print("\n**********Example 3**************")
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

print("\n**********Example 4**************")
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding") #Regular parameters must come before **kwargs:

print("\n**********Example 5**************")
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo") #Combining *args and **kwargs
#High order functions


#comprehensions
print("**********list comprehensions**************")

result = []
for item in arr:
    result.append(item + 2)
print(result)

#oder bevorzugt so

result = [item + 2 for item in arr]
print(result)

#auch mit filter
result = [item + 2 for item in arr if item < 4]
print (result)
result = [item + 2 if item < 4 else item + 10 for item in arr]
print(result)

#Pass by Reference and Pass by Value
print("***************Pass by Reference and Pass by Value****************")

# Function modifies the first element of list
def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun(lst)
print(lst)   # list is modified

# Function tries to modify an integer
def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)     # integer is not modified