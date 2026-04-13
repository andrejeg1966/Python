"""
Created on 11.03.2025

@author: goran
"""
# @property bietet eine elegante Möglichkeit, den Zugriff auf Attribute zu steuern, 
# ohne auf explizite Getter- und Setter-Methoden (wie getName() / setName()) zurückgreifen zu müssen, 
# was Python sauberer und intuitiver macht.
class Person:
    def __init__(self, name):
        self._name = name  # Das "_" signalisiert ein internes Attribut

    @property
    def name(self):
        """Getter: Gibt den Namen zurück"""
        return self._name

    @name.setter
    def name(self, value):
        """Setter: Ändert den Namen mit Validierung"""
        if not isinstance(value, str):
            raise ValueError("Name muss ein String sein")
        self._name = value

# Nutzung
p = Person("Max")
print(p.name)  # Zugriff wie auf ein Attribut (keine Klammern!)
p.name = "Lisa"  # Aufruf des Setters
print(p.name)


class Archer:
    def __init__(self, hp, dmg):
        self._hp = hp
        self._dmg = dmg
        self.crit = 1.3
        self._overall_damage = None

    #Implementierung mit getter und setter
    # def get_hp(self):
    # return self._hp
    # def set_hp(self, value):
    # self_hp = value
    # property(fget=get_hp, fset=set_hp)

    # getter
    @property
    def hp(self):
        return self._hp

    # setter
    @hp.setter
    def hp(self, value):
        if value > 100:
            raise ValueError("HP darf maximal 100 sein")
        self._hp = value

    @property
    def dmg(self):
        return self._dmg

    @dmg.setter
    def dmg(self, value):
        self._dmg = value
        self._overall_damage = None
    
    @property
    def overall_damage(self):
        if self._overall_damage is None:
            print("Berechnung wird durchgeführt")
            self._overall_damage = self.dmg * self.crit
        return self._overall_damage


archer = Archer(100, 50)
print(f"hp: {archer.hp}")
print(f"overall_damage: {archer.overall_damage}")
archer.dmg = 500
print(f"overall_damage: {archer.overall_damage}")
print("***************************")
print(f"overall_damage: {archer.overall_damage}")

