'''
Created on 11.03.2025

@author: goran
'''

class Archer:
    def __init__(self, hp, dmg):
        self._hp = hp
        self._dmg = dmg
        self.crit = 1.3
        self._overall_damage = None
    
    # def get_hp(self):
        #return self._hp
    
    # def set_hp(self, value):
        #self_hp = value
        
    #property(fget=get_hp, fset=set_hp)
    
    #getter
    @property
    def hp(self):
        return self._hp
    
    #setter
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
            return self.dmg * self.crit
        return self._overall_damage
    
archer = Archer(100, 50)
archer.hp = 99
print(archer.hp)
print("**********    1    *************")
print(archer.overall_damage)
print("**********    2    *************")
archer.dmg = 500
print(archer.overall_damage)
print("**********    3    *************")
print(archer.overall_damage)
print("**********    4    *************")

