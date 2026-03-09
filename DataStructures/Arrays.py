"""
Create an Array in Python
Array in Python can be created by importing an array module. array( data_type , value_list )
is used to create array in Python with data type and value list specified in its arguments.
"""

import array as arr

a = arr.array("i", [1, 2, 3])

for i in range(0, 3):
    print(a[i], end=" ")
print(type(a))
print(a)

print("\n***********Adding Elements and Accessing an Array**************")

import array as arr

a = arr.array("i", [1, 2, 3])
print(*a)

a.insert(1, 4)  # Insert 4 at index 1
print(*a)
print(a[0])
print(a[3])

print("\n***********Removing Elements from the Array**************")
import array

a = array.array("i", [1, 2, 3, 1, 5])

# remove first occurance of 1
a.remove(1)
print(*a)

# remove item at index 2
a.pop(2)
print(*a)

print("\n***********Slicing of an Array**************")
import array as arr

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = arr.array("i", a)

res = a[3:8]
print(res)

res = a[5:]
print(res)

res = a[:]
print(res)

print("\n***********Searching Element in an Array**************")
import array

a = array.array("i", [1, 2, 3, 1, 2, 5])

# index of 1st occurrence of 2
print(a.index(2))

# index of 1st occurrence of 1
print(a.index(1))

print("\n***********Extend Element from Array**************")

a = arr.array("i", [1, 2, 3, 4, 5])

a.extend([6, 7, 8, 9, 10])
print(a)
