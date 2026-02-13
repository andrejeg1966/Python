'''
Created on 06.03.2025

@author: goran
'''
x = 1

y = 2

#Variable uebeschreiben

x = "Hallo"


s = "Python is great!"

def fun():
    global s
    s += " GFG"   # Modify global variable
    print(s)
    s = "Look for GeeksforGeeks Python Section"  # Reassign global
    print(s)

fun()
print(s)

a = 1  # Global variable

def f():
    print("f():", a)  # Uses global a

def g():
    a = 2  # Local shadows global
    print("g():", a)

def h():
    global a
    a = 3  # Modifies global a
    print("h():", a)

print("global:", a)
f()
print("global:", a)
g()
print("global:", a)
h()
print("global:", a)

#Assign Function to a Variable in Python
print("Assign Function to a Variable in Python")

# defining a function
def a(): 
  print("GFG")
  
# assigning function to a variable
var=a

# calling the variable
var()
print("**************")
x = 123  # global variable

def display():
    x = 98  # local variable
    print(x)  
    print(globals()['x'])  # accesses global x

print(x) 

a = display  # assign function to a variable
a()  # call function
a()  # call function