def fun1(name):
    def wrap():
        return f"Hello, {name}!"
    return wrap

# Get the function returned by fun1()
msg = fun1("Emma")

print(msg())


def B():
    print("Inside the method B.")

def A():
    print("Inside the method A.") 
    return B  # function A returns function B

return_fun = A()  
return_fun()