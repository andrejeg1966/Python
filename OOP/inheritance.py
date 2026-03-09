"""
Created on 10.03.2025

@author: goran
"""


class BasePlayer:
    def __init__(self, hp):
        self.hp = hp

    def walk(self):
        print("Ich laufe ...")


class Archer(BasePlayer):
    def __init__(self, hp, arrows):
        # BasePlayer.__init__(self, hp = hp)
        # oder mit supper class
        super().__init__(hp=hp)
        self.arrows = arrows


class Wizard(BasePlayer):
    pass


archer = Archer(100, 10)
wizard = Wizard(11)

print(f" ich bin archer mit {archer.hp} hp")
print(f" ich bin wizard mit {wizard.hp} hp")

# Beispiel: Mit Vererbung und magic method wird dictionary unverändbar

x = {"bla": 122}
x["bla"] = 123
print(x)


class NoUpdateDictionary(dict):
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError("Key existiert bereits")
        super().__setitem__(key, value)


x = NoUpdateDictionary()
x["key"] = 125
# x["key"] = 123
