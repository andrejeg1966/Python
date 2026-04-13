# Beispiel __add__ method
class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        
    def __add__(self, other):
        if (isinstance(other, int)):
            total = self.balance + other
        else:
            total = self.balance + other.balance
        return BankAccount(total)
    
    def __radd__(self, other):
        return self.__add__(other) #self == account, other == 5000
        

account1 = BankAccount(1000)
account2 = BankAccount(2000)
new_account = account1 + account2
new_account1 = account1 + 4000 #call __add__ method
new_account2 = 5000 + account1 #call __radd__ method
print(f"New Account: {new_account.balance}")
print(f"New Account1: {new_account1.balance}")
print(f"New Account2: {new_account2.balance}")


class A:
    def __init__(self, a):
        self.a = a

    # define behavior of +
    def __add__(self, o):
        return self.a + o.a


ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)  # integer addition
print(ob3 + ob4)  # string concatenation

# actual working (internally)
print(A.__add__(ob1, ob2))
print(ob1.__add__(ob2))

print("Class Complex")

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b


Ob1 = Complex(1, 2)
Ob2 = Complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)

print("class MyClass")


class MyClass:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        return MyClass(self.value and other.value)


a = MyClass(True)
b = MyClass(False)
c = a & b
print(c.value)
