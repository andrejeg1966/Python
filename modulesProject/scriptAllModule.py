'''
Created on 06.03.2025

@author: goran
'''
from package import packageModule
print("**************   1    ******************")
from package.subpackage import subpackageModule
print("**************   1    ******************")
from package.subpackage.subpackageModule import test_function
from package.packageModule import test_function as tf2

packageModule.test_function()
subpackageModule.test_function()
test_function()
tf2()
