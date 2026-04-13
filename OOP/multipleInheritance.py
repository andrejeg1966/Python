"""
Created on 10.03.2025

@author: goran
"""


class A(object):
    def sayhi(self):
        print("Hello von A")


class B(A):
    def sayhi(self):
        print("Hello von B")


class C(A):
    def sayhi(self):
        print("Hello von C")


class D(C, B):
    pass


d = D()
d.sayhi()

# method resolution order, zeigt die Reihenfolge von Vererbung. Links for rechts , d.h zuerst C danach B
print(A.__dict__)
print(D.__mro__)
print("*************   1    ****************")


# class mixing
import json

class JsonMixin:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__ )  # instance object in ein json object umwandeln mit lambda Funktion

#diese Klasse erbt von Archer, das ist in SuperArcher durch die Reiehenfolge 
class SuperWalkMixin:
    def walk(self):
        return f"{super().walk()} extrem schnell"  # super class ist Archer


class Archer:
    def __init__(self, hp, mana):
        self._hp = hp
        self._mana = mana

    def walk(self):
        return "Ich laufe..."


# method resolution order (mro) ist wichtig
class SuperArcher(JsonMixin, SuperWalkMixin, Archer):
    pass


a = Archer(100, 20)
print(a.walk())

superArcher = SuperArcher(120, 30)
print(superArcher.walk())
print(superArcher.toJSON())
print(SuperArcher.__mro__)
