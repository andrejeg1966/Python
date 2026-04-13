
class Archer:
    hp = 100
    
archer = Archer()
print(type(archer))
print(archer.__dict__)
print(type(Archer))
print(type(type))

Archer = type("Archer2", (), {"hp": 200})
archer2 = Archer()
print(type(archer2))
print(type(Archer))
print(archer2.hp)
# print name of class
print(type(archer2).__name__)