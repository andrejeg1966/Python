'''
Docstring for DataStructures.Sets
Python set is an unordered collection of multiple items having different datatypes. 
In Python, sets are mutable, unindexed and do not contain duplicates. The order of elements in a set is not preserved and can change.

Can store None values.
Implemented using hash tables internally.
Do not implement interfaces like Serializable or Cloneable.
Python sets are not inherently thread-safe; synchronization is needed if used across threads.
'''

print("***************Creating a Set in Python****************")

set1 = {1, 2, 3, 4}
print(set1)

set1 = set()
print(set1)

set1 = set("GeeksForGeeks")
print(set1)

# Creating a Set with the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# Creating a Set with the use of a tuple
tup = ("Geeks", "for", "Geeks")
print(set(tup))

# Creating a Set with the use of a dictionary
d = {"Geeks": 1, "for": 2, "Geeks": 3}
print(set(d))

print("\n***************Unindexed ******************")
set1 = {3, 1, 4, 1, 5, 9, 2}

print(set1)  # Output may vary: {1, 2, 3, 4, 5, 9}

# Unindexed: Accessing elements by index is not possible
# This will raise a TypeError
try:
    print(set1[0])
except TypeError as e:
    print(e)
    
print("\n*****************Adding Elements to a Set in Python****************")
# Creating a set
set1 = {1, 2, 3}

# Add one item
set1.add(4)

# Add multiple items
set1.update([5, 6])

print(set1)

print("\n*****************Accessing a Set in Python****************")
set1 = set(["Geeks", "For", "Geeks."])

# Accessing element using For loop
for i in set1:
    print(i, end=" ")

# Checking the element# using in keyword
print("Geeks" in set1)

print("\n*****************Removing Elements from the Set in Python****************")
# Using Remove Method
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)  

# Attempting to remove an element that does not exist
try:
    set1.remove(10)
except KeyError as e:
    print("Error:", e)  

# Using discard() Method
set1.discard(4)
print(set1)  

# Attempting to discard an element that does not exist
set1.discard(10)  # No error raised
print(set1)

set1 = {1, 2, 3, 4, 5}
val = set1.pop()
print(val)
print(set1)

# Using pop on an empty set
set1.clear()  # Clear the set to make it empty
try:
    set1.pop()
except KeyError as e:
    print("Error:", e)

print("\n*****************Typecasting Objects into Sets****************")
# Typecasting list into set
li = [1, 2, 3, 3, 4, 5, 5, 6, 2]
set1 = set(li)
print(set1)

# Typecasting string into set
s = "GeeksforGeeks"
set1 = set(s)
print(set1)

# Typecasting dictionary into set
d = {1: "One", 2: "Two", 3: "Three"}
set1 = set(d)
print(set1)