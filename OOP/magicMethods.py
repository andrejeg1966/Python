"""
Created on 07.03.2025

@author: goran
"""


class Archer:
    def __init__(self, hp, mana, arrows):
        self.hp = hp
        self.mana = mana
        self.arrows = arrows

    def __str__(self):

        return f"__str__: Archer mit {self.hp} HP und {self.mana} MANA mit {self.arrows} Pfeilen"

    # falls __str__ existiert wird __repr__ nicht geprintet

    def __repr__(self):
        return f"Archer({self.hp}, {self.mana}, {self.arrows})"

    # vergleichen zwei Objekten auf gleicheit

    def __eq__(self, other):
        if not isinstance(other, Archer):
            False
        else:
            return (
                self.hp == other.hp
                and self.mana == other.mana
                and self.arrows == other.arrows
            )

    def __gt__(self, other):
        if not isinstance(other, Archer):
            return NotImplemented
        else:
            return self.hp > other.hp

    def __ge__(self, other):
        if not isinstance(other, Archer):
            return NotImplemented
        else:
            return self.hp >= other.hp

    def __hash__(self):
        return hash((self.hp, self.mana, self.arrows))


class Company:
    def __init__(self, size):
        self.size = size
        self.archers = []
        self.index = 0

    def add_archer(self, archer):
        if not isinstance(archer, Archer):
            raise TypeError("Nur Archer in Company erlaubt")
        if len(self.archers) >= self.size:
            raise ValueError("Company bereits voll")
        self.archers.append(archer)

    def __add__(self, other):
        if not isinstance(other, Archer):
            raise TypeError("Nur Archer addieren erlaubt")
        new_company = Company(self.size)
        for archer in self.archers:
            new_company.add_archer(archer)
        print("vor add_archer()")
        print(new_company.archers)
        print("nach add_archer()")
        new_company.add_archer(other)
        print(new_company.archers)
        return new_company

    def __radd__(self, other):
        if not isinstance(other, Archer):
            raise TypeError("radd: Nur Archer addieren erlaubt")
        return self + other

    def __iter__(self):
        print("__iter__ function ")
        return iter(self.archers)

    def __next__(self):
        print("__next__ function ")
        if self.index > len(self.archers):
            raise StopIteration
        new_archer = next(self)
        print(f"new_archer: {new_archer}")
        print(f"index: {self.index}")
        self.index += 1
        return new_archer


archer1 = Archer(101, 1, 6)
archer2 = Archer(102, 2, 7)
archer3 = Archer(103, 3, 8)
archer4 = Archer(104, 4, 9)
print(archer1)
print(repr(archer1))
print(archer1 == archer2)
print(archer1 > archer2)
print(archer1 >= archer2)
print("*********        1            **************")

company = Company(5)
# __ad_archer__
company.add_archer(archer1)
company.add_archer(archer2)
# company.add_archer(archer3)
print(company.archers)
print("*********        2            **************")
# __add__
company = company + archer3
print(company.archers)
print("*********        3            **************")
# __radd__
company = archer4 + company
print(company.archers)
print("*********        4            **************")


# __str__
for soldier in company.archers:
    print(soldier)
print("*********        5            **************")

# __iter__ und __next__
print("__iter__ und __next__")
for soldier in company:
    print(soldier)

# hashen
print(hash(archer1))
# zum erzeugen von dictionaries brauchen wir eine hash objekt auf archer
archers_dict = {archer1: "Happy", archer2: "Depressed"}
