''''
Created on 12.03.2025

@author: goran
'''

class Descriptor:
    def __init__(self, value):
        self._value = value
        
    #dexriptor protokol
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if value < 0 or value > self._value:
            raise ValueError(f"Property {self.name} erlaubt nur werte  zwischen 0 ind {self._value}")
        instance.__dict__[self.name] = value
    #wird sobald ausgeführt wenn __init__ ausgeführt
    def __set_name__(self, owner, name):
        self.name = name
#das ist auch ein Descriptor, weil hat __set__ und __get__ methode
class Lifes:
    def __get__(self, instance, owner):
        return 3
    
    def __set__(self, instance, owner):
        pass
      
class Archer:
    hp = Descriptor(100)  # 100 ist maximalle Wert für hp
    mana = Descriptor(50) # 50 ist maximalle Wert für mana
    lifes = Lifes()
    
    def __init__(self, hp, mana, lifes):
        self.hp = hp
        self.mana = mana
        self.lifes = Lifes()


# bei vollwertigen Descriptor mro schaut zuerst in Dataclass, d.h was in Lifes gesetztz ist, das heist 3
# bei nicht vollwertigen Descriptor wird gesetzt was in Aufruf von Konstruktor steht. das hesst 5 

archer1 = Archer(100,30,40)
#archer1.hp = 100
#archer1.mana = 50

archer2 = Archer(20,50,5)
#archer2.hp = 80
#archer2.mana = 40

print(archer1.__dict__)

print(archer1.hp)
print(archer1.mana)
print(archer2.hp)
print(archer2.mana)
print(archer1.lifes)
print(archer2.lifes)

