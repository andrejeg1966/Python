'''
Created on 07.03.2025

@author: goran
'''


class Archer:
    def __init__(self, hp, mana, arrows):
        self.hp = hp
        self.mana = mana
        self.arrows = arrows
        
    def walk(self):
        print(f" ich bin {self} und laufe")
        
    def shoot(self):
        if (self.arrows > 1):
            self.arrows -= 1
            print(f"Bogenschütze hat geschossen, es bleibt noch {self.arrows} übrig")
        elif (self.arrows == 1):
            self.arrows -= 1
            print(f"Ende")
        else:
            print(f"Bogenschütze hat kein Pfeil mehr")
            
    @classmethod
    def class_method(cls):
        print(f"ich bin eine klassmethod {cls}")
    #class method wird als factory für Instanzen verwendet
    
    @classmethod
    def from_data(cls, hp, mana, arrows):
        return cls(hp, mana, arrows)
    
    @staticmethod
    def static():
        print(f"ich bin  static method")    

print(Archer.__dict__)
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