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
