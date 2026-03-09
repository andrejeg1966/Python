from pydantic import BaseModel  # pydentc doesn't work


class WaffenKammer(BaseModel):
    zimmer: int
    waffen: list[Waffen]


kammer = WaffenKammer(zimmer=3, waffen=["Schwert", "Axt"])
print(kammer)
# kammer.model_dump() veraltet, verwende ,odel_dump()
print(kammer.model_dump())
print("**************    4    ***************")


# Pydentic


class PyDanticBogen(BaseModel):
    name: str
    preis: float
    schaden: int = 100


PyDanticBogen(name="Magic Bogen", preis=100, schaden=30)
print(PyDanticBogen)
