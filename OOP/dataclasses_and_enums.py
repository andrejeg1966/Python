'''
Created on 10.03.2025

@author: goran
'''
from test.test_pprint import dataclass1

'''

class Bogen:
    def __init__(self, name, preis , schaden):
        self.name = name
        self.preis = preis
        self.schaden = schaden

bogen_a = Bogen("Toller bogen", 10, 100)
'''

from dataclasses import dataclass
from enum import Enum
# Dataclass macht syntax deutlich simple und die magic methoden sind nicht mehr notwending
# wird verwendet nur für Daten
@dataclass(frozen=False, repr=True)
class Bogen:
    name: str
    preis: float
    schaden: int = 100


#Vererbung
@dataclass(frozen=False)
class MagicBogen(Bogen):
    mcg_dmg: int = 200

bogen1 = Bogen("Standard Bogen", 500, 90)
print(bogen1)
bogen2 = Bogen("Standard Bogen", 500, 910)
print(bogen1 == bogen2)
print("**************    1    ***************")

bogen3 = MagicBogen("Magic Bogen", 100, 20, 34)
bogen3.magie = 10
print(bogen3)
print("**************    2    ***************")



#enum
#@unique         # um values unique festzulegen
class Waffen(Enum):
    S = "Schwert"
    B = "Bogen"
    C = "Axt"
   
print(Waffen)
print(repr(Waffen.B))  
print(Waffen.B.name) 
print(Waffen.B.value)    
print("**************    3    ***************")


