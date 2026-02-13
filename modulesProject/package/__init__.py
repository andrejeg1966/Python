#es wird bei import von dem package ausgefuehrt
print("Package: __init__")

#damit alle module aus diese package importier werden in scriptAllModule
__all__ = ["subpackageModule", "packageModule"]