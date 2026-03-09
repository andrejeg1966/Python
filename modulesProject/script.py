"""
Created on 06.03.2025

@author: goran
"""

# import module
from package.subpackage import subpackageModule

print("**************   1    ******************")
subpackageModule.test_function()

print(f"a in subpackage module {subpackageModule.a}")

# import einzelne Funktionen und variablen aus module
# wenn die module2 die test_function aus moduele maskiert, definieren wir alias für test_function in module 1
from package.subpackage.subpackageModule import test_function as tf1

print("**************   2    ******************")
from hauptModule import test_function

print("**************   3    ******************")
from package.subpackage.subpackageModule import a

print("**************   4    ******************")
tf1()
test_function()
print(a)
