"""
Can contain duplicate items
Mutable: items can be modified, replaced, or removed
Ordered: maintains the order in which items are added
Index-based: items are accessed using their position (starting from 0)
Can store mixed data types (integers, strings, booleans, even other lists)
"""

print("***************Creating a List Using Square Brackets*************")
a = [1, 2, 3, 4, 5]  # List of integers
b = ["apple", "banana", "cherry"]  # List of strings
c = [1, "hello", 3.14, True]  # Mixed data types

print(a)
print(b)
print(c)

print("\n*****************Creating a List Using list() Constructor*******************")
a = list((1, 2, 3, "apple", 4.5))
print(a)

b = list("GFG")
print(b)

print("\n****************Adding Elements into List*************")

a = []

a.append(10)
print("After append(10):", a)

a.insert(0, 5)
print("After insert(0, 5):", a)

a.extend([15, 20, 25])
print("After extend([15, 20, 25]):", a)

a.clear()
print("After clear():", a)

print("\n****************Removing Elements from List*************")
a = [10, 20, 30, 40, 50]

a.remove(30)
print("After remove(30):", a)

popped_val = a.pop(1)
print("Popped element:", popped_val)
print("After pop(1):", a)

del a[0]
print("After del a[0]:", a)

print("\n****************Iterating Over Lists*************")
a = ["apple", "banana", "cherry"]
for item in a:
    print(item)

print("\n****************Nested Lists*************")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])

print("\n****************List Comprehension*************")
print("*****************Example 1*********************")
a = [2, 3, 4, 5]
res = [val**2 for val in a]
print(res)

print("\n*****************Example 2*********************")
# Conditional Statements in List Comprehension
a = [1, 2, 3, 4, 5]
res = [val for val in a if val % 2 == 0]
print(res)

res = [val < 2 and val > 4 for val in a]
print(res)
