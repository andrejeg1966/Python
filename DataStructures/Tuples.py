"""
A tuple in Python is an immutable ordered collection of elements.

Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable).
Tuples can hold elements of different data types.
The main characteristics of tuples are being ordered, heterogeneous and immutable.
"""

print("************Creating a Tuple****************")
tup = ()
print(tup)

# Using String
tup = ("Geeks", "For")
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple("Geeks")
print(tup)

print("************Accessing of Tuples****************")
# Accessing Tuple with Indexing
tup = tuple("Geeks")
print(tup[0])

# Accessing a range of elements using slicing
print(tup[1:4])
print(tup[:3])

# Tuple unpacking
tup = ("Geeks", "For", "Geeks")

# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)

print("************Slicing of Tuple****************")
tup = tuple("GEEKSFORGEEKS")

# Removing First element
print(tup[1:])

# Reversing the Tuple
print(tup[::-1])

# Printing elements of a Range
print(tup[4:9])
