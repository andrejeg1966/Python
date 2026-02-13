'''
Created on 12.03.2025

@author: goran
'''
from abc import ABC, abstractmethod

class AbstractArcher(ABC):
    @property
    @abstractmethod
    def hp(self):
        pass
    
    @abstractmethod
    def walk(self):
        pass
    
    @abstractmethod
    def walk2(self):
        print("Ich laufe in ABC")

class Archer(AbstractArcher):
    def walk(self):
        print("Ich laufe...")
    
    def walk2(self):
        super().walk2()
    
    def __init__(self, hp):
        self._hp = hp
        
    @property
    def hp(self):
        return self._hp
    
    
        
archer = Archer(100)
archer.walk()
print(archer.hp)
archer.walk2()