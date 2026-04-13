"""
Created on 13.03.2025

@author: goran
"""

print("Implementierung MyMetaClass*************")

class MyMetaClass(type):
    def __call__(self, *args, **kwargs):
        print("__call__")
        return super().__call__(*args, **kwargs)

    @classmethod
    def __prepare__(metacls, name, bases):
        print("__prepare__")
        print(name)
        print(bases)
        return {"hp": 100, "mana": 10}

    def __new__(metacls, name, bases, namespace):
        print("__new__")
        print(namespace)
        print(name)
        print(bases)
        return super().__new__(metacls, name, bases, namespace)


class Archer(metaclass=MyMetaClass):
    hp = 200
    mana = 20


# print(type(Archer3))
archer1 = Archer()
archer2 = Archer()
print(id(archer1))
print(id(archer2))
