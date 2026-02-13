'''
Created on 06.03.2025

@author: goran
'''
#High order functions
print("**********lambda**************")

add = lambda x: x + 2
print(add)

arr = [1,2,3,4,5]
x = list(map(lambda x: x + 2, arr))
print(x)
y = list(filter(lambda x: x < 4, arr))
print(y)

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