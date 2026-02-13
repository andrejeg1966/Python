def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')


'''
Keyword Arguments (**kwargs)
The special syntax **kwargs allows us to pass any number of keyword arguments (arguments in the form key=value). 
These arguments are collected into a dictionary, where:
'''

def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')