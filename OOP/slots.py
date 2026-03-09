"""
Created on 12.03.2025

@author: goran
"""


class Archer:
    # definieren eines slots, keine magic methode sondern Datenobject
    # slots sind statische objekte um Resourcen zu schonen. Also wird nicht meht´r in instance dictonary gespeichert
    __slots__ = ("hp", "mana")

    def __init__(self, hp, mana):
        self.hp = hp
        self.mana = mana


# ohne slots
class Archer2:
    def __init__(self, hp, mana):
        self.hp = hp
        self.mana = mana


archer = Archer(100, 50)

# keine weitere Atributte ist erlaubt
# archer.arrows = 12
print(archer.hp)
# Keine dynamsches dictionary, sonder statischer slots wird verwenden
# print(archer.__dict__)2
archer2 = Archer2(100, 50)

from pympler import asizeof  # um grösser von Objekten zu prüfen

print(asizeof.asized(archer))
print(asizeof.asized(archer2))


class MagicArcher(Archer):
    # fallse parent class slots implementiert und child class nicht, dann es gibt dictionary mit dem atribbute aus child class
    __slots__ = "arrows"

    def __init__(self, hp, mana, arrows):
        super().__init__(hp, mana)
        self.arrows = arrows


marcher = MagicArcher(hp=100, mana=50, arrows=12)
# print(marcher.__dict__)
