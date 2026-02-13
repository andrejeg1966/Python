'''
Created on 06.03.2025

@author: goran
'''
def test_function():
    print("Hi in test_function() subpackage module")
    
a = 10

def test_name():
    print(f"ich werde in test_name() in module {__name__} ausgefuehrt")

#1. wenn man die Funktion in in diesem module ausfuert , ist der name = main
#2. wenn man der Funktion in anderem module ausfuehrt hat name = name des dieses module   
test_name()

#3 Steuern die Ausfuehrung der Funtion . Nur in diesem module soll ausgefuehrt sein
def test_nameSteuern():
    print(f"ich werde in test_nameSteuern() in module {__name__} ausgefuert ")
    
if __name__ == "__main__":
    test_nameSteuern()
    
    