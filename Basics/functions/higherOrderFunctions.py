def process(func, text):  # applies a function to text  
    return func(text)  

def uppercase(text):  # converts text to uppercase  
    return text.upper()  

print(process(uppercase, "hello"))

print("*****************")

# higher-order function
def fun(func, number):
    return func(number)

# function to double a number
def double(x):
    return x * 2

print(fun(double, 5))

print("****************")