"""
Created on 07.03.2025

@author: goran
"""


class Archer:
    def __init__(self, hp, mana, arrows):
        self.hp = hp
        self.mana = mana
        self._arrows = arrows #Ein unterstrich signalisiert, bitte Zugrif nur über Instance Method , nicht direkt über instance
                              # Doppelte Unterstich, ist quasi ein privates Attribute aber doch keins

    def walk(self):
        print(f" ich bin {self} und laufe")

    def shoot(self):
        if self._arrows > 1:
            self._arrows -= 1
            print(f"Bogenschütze hat geschossen, es bleibt noch {self._arrows} übrig")
        elif self._arrows == 1:
            self._arrows -= 1
            print(f"Ende")
        else:
            print(f"Bogenschütze hat kein Pfeil mehr")

    @classmethod
    def class_method(cls):
        print(f"ich bin eine klassmethod {cls}")

    # class method wird als factory für Instanzen verwendet
    @classmethod
    def from_data(cls, hp, mana, arrows):
        return cls(hp, mana, arrows)
    #Aufruf über beide: Klasse und Instance
    @staticmethod
    def static():
        print(f"ich bin  static method")


print(Archer.__dict__)  #Die Klasse speichert Attibute in einem dictionary mappingproxy
print("**********     1   ***********")
print(type(Archer.__dict__))
print("**********     2   ***********")


arch1 = Archer(100, 0, 3)
arch2 = Archer(90, 0, 3)
print(arch1.__dict__)
print("**********     3   ***********")
print(type(arch1.__dict__))
print("**********     4   ***********")
arch1.walk()
print(arch1.hp)
print("**********     5   ***********")
print(arch1.mana)
print("**********     6   ***********")
arch1.shoot()
arch1.shoot()
arch1.shoot()
arch1.shoot()

Archer.class_method()
archer3 = Archer.from_data(100, 5, 0)
print(archer3.hp)
print("**********     7   ***********")
print(archer3.mana)
print("**********     8   ***********")
Archer.static()
arch1.static()

class PrivatesAttribute:
    def __init__(self, quasi_private, store=0):
        self.__quasie_private = quasi_private
        self.store = self.__quasie_private
        
quasi_private = PrivatesAttribute(23, 0)

print(quasi_private.__dict__)
print(quasi_private._PrivatesAttribute__quasie_private) # Zugriff auf quasi privat 
quasi_private._PrivatesAttribute__quasie_private = 15
print(quasi_private.store)
