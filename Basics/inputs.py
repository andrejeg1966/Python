'''
Created on 06.03.2025

@author: goran
'''

name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")

x = int(input("erste Zahl: "))
y = int(input("zweite Zahl: "))
z = x + y

print(z)

print("Multiple Input in Python")


str1 = input("Enter two values: ")
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print(str1)
print(type(str1))
print(type(x))

s = "one,two,three"
words = s.split(',')
print(words)
print(type(words))
print(s)