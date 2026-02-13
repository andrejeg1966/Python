# simple decorator example

import time
import logging 


# Simple decorator  
print("**********Example 1**************")
def deco(f):  
    def wrap():  
        print("Before")  # Pre-execution message  
        f()  
        print("After")   # Post-execution message  
    return wrap  

# Applying decorator  
@deco  
def func():  
    print("Running...")  # Main function execution  

func()  # Call decorated function
 
print("\n**********Example 2**************")
def decorator_fun(original_fun):
    def wrapper_fun():
        print("Hello, this is before function execution")
        original_fun()
        print("This is after function execution")
    return wrapper_fun

@decorator_fun
def display():
    print("This is inside the function !!")

# calling the decorated function
display()

print("\n**********Example 3**************")
def apply_lambda(func, value):
    return func(value)

square = lambda x: x ** 2
print("Square of 2 is:", apply_lambda(square, 2))

print("\n**********Example 4**************")
#Measuring Execution time
def timeit(f):  
    """Measures execution time."""  
    def wrap(*args, **kwargs):  
        t1 = time.time()  
        res = f(*args, **kwargs)
        print(f"{f.__name__} ran in {time.time() - t1:.6f}s")  
        return res  
    return wrap  

@timeit  
def countdown(n):  
    """Counts down from n."""  
    while n:  
        n -= 1  

countdown(5)  
countdown(1000)

print("\n**********Example 5**************")
#whitout args and kwargs
def timeit(f):  
    """Measures execution time."""  
    def wrap(n):  
        t1 = time.time()  
        res = f(n)
        print(f"{f.__name__} ran in {time.time() - t1:.6f}s")  
        return res  
    return wrap  

@timeit  
def countdown(n):  
    """Counts down from n."""  
    while n:  
        n -= 1  

countdown(5)  
countdown(1000)

print("\n**********Example 6**************")
def admin_only(f):
    """Restricts access to admin users."""
    def wrap(user):
        if user != "admin":
            return print("Access Denied!")
        #return f(user)
    return wrap

@admin_only
def access_data(user):
    print(f"Welcome {user}, access granted.")

# Test cases
access_data("guest")
access_data("admin")

print("\n**********Example 5**************")

logging.basicConfig(level=logging.INFO) 

def logger(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with {args}, {kwargs}") 
        return func(*args, **kwargs) 
    return wrapper

@logger
def add(a, b, c=5):
    return a + b + c  
print(add(3, 4))