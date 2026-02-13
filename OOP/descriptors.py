'''
Created on 12.03.2025

@author: goran
'''
from weakref import WeakKeyDictionary

#mit getter und setter bzw. property müssen wir sehr viele Properties schreiben. Descriptor löst das Problem
class Descriptor:
    
    def __init__(self, value):
        self._data = WeakKeyDictionary()
        self._value = value
    
    #dexriptor protokol: Vollwertige Descriptor hat get und set
    def __get__(self, instance, owner):
        print(instance)
        return self._data.get(instance)
    
    def __set__(self, instance, value):
        if value < 0 or value > 500:
            raise ValueError("Nur value zwischen 0 ind 100 erlaubt")
        self._data[instance] = value
    
class Archer:
    hp = Descriptor(80)
    mana = Descriptor(50)
    
archer1 = Archer()
archer1.hp = 100

archer2 = Archer()
archer2.hp = 200

print(archer1.hp)
print(archer2.hp)