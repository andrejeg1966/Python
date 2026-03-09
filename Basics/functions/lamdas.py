print("****************lambda***************")
print("**********Example 1**************")
add = lambda x: x**2
print(add(3))
print(add(4))

print("\n**********Example 2**************")
check = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check(5))
print(check(-3))
print(check(0))

print("\n**********Example 3**************")
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(4))
print(check(7))

print("\n**********Example 4**************")
calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)
print(type(res))

print("**********lambda using with List Comprehension************")
func = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in func:
    print(i())

print("************lambda using with filter()*********")
print("**********Example 1**************")


def even(n):
    return n % 2 == 0


a = [1, 2, 3, 4, 5, 6]
b = filter(even, a)
print(list(b))  # Convert filter object to a list

print("\n**********Example 2**************")
c = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, c)
print(list(even))

print("\n**********Example 3**************")
# This code uses filter() with None as the function to remove all falsy values (like empty strings, None and 0) from a list.
L = ["apple", "", None, "banana", 0, "cherry"]
A = filter(None, L)
print(list(A))


print("************lambda using with map()*************")
print("**********Example 1**************")
# Let's start with a simple example of using map() to convert a list of strings into a list of integers.
s = ["1", "2", "3", "4"]
res = map(int, s)
print(list(res))


# Custom function to be applied in map
def double(val):
    return val * 2


# Let us apply double on every member
a = [1, 2, 3, 4]
res = list(map(double, a))
print(res)

print("\n**********Example 2**************")
a = [1, 2, 3, 4]
double = map(lambda x: x * 2, a)
print(list(double))

print("\n**********Example 3**************")
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
c = map(lambda x: x * 2, b)
print(list(c))

print("\n**********Example 4**************")
a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))

print("************lambda using with reduce()*************")
from functools import reduce

a = [1, 2, 3, 4]
mul = reduce(lambda x, y: x * y, a)
print(mul)
