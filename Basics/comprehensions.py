"""
Created on 06.03.2025

@author: goran
"""

# High order functions
print("**********lambda**************")

add = lambda x: x + 2
print(add)
print(add(2))

arr = [1, 2, 3, 4, 5]
# map( function, iterable)
x = list(map(lambda x: x + 2, arr))
print(x)
#filter(function, iterable)
y = list(filter(lambda x: x < 4, arr))
print(y)

# comprehensions
print("**********list comprehensions**************")

# mit for loop über list iterieren
result = []
for item in arr:
    result.append(item + 2)
print(result)

# oder mit list comprehension. Signatur: <item for item in iterable>
result = []
result = [item + 2 for item in arr]
print(result)

# auch mit filter
result = []
result = [item + 2 for item in arr if item < 4]
print(result)
result = [item + 2 if item < 4 else item + 10 for item in arr]
print(result)
