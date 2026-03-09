"""
Created on 13.03.2025

@author: goran
"""


class Archer:
    hp = 100


archer = Archer()
print(type(archer))
print(type(Archer))
print(type(type))

# Eine Class kann man auch so definieren

Archer = type("Archer2", (), {"hp": 100})
archer2 = Archer()
print(type(archer2))
print(type(Archer))
# print name of class
print(type(archer2).__name__)


print("*****************MyMetaClass*************")


class MyMetaClass(type):
    def __call__(self, *args, **kwargs):
        print("__call__")
        return super().__call__(*args, **kwargs)

    @classmethod
    def __prepare__(metacls, name, bases):
        print("__prepare__")
        return {"hp": 100, "mana": 10}

    def __new__(metacls, name, bases, namespace):
        print("__new__")
        print(namespace)
        return super().__new__(metacls, name, bases, namespace)


class Archer3(metaclass=MyMetaClass):
    hp = 200


# print(type(Archer3))
archer3 = Archer3()
archer4 = Archer3()
print(id(archer3))
print(id(archer4))


print("*****************Singelton*************")


class Singelton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances


class MySingelton(metaclass=Singelton):
    pass


a = MySingelton()
b = MySingelton()
print(id(a))
print(id(b))
