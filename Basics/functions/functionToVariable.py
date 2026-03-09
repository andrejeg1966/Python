x = 123  # global variable


def display():
    x = 98  # local variable
    print(x)
    print(globals()["x"])  # accesses global x


print(x)

a = display  # assign function to a variable
a()  # call function
a()  # call function

print("\n**********Example 2**************")


# defining a function
def fun(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


# assigning function to a variable
a = fun
# calling function using the variable
a(67)
a(10)
a(7)
