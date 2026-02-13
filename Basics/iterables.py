'''
Created on 06.03.2025

@author: goran
'''
#Liste ist veränderbar (mutable)

#auch doppelte Werte

x = [100, 23.4, "Hallo", "Hallo"]
y = []
print(x)
print(x[2])
print(x[0:1])
print(x[0:2])
print(x[2:4])
print(x[:4])
print(x[1:])

#von den letzten element
print(x[-1:])

#jedes zweites Element
print(x[:5:2])

#umgekehrte liste
y = x[::-1]
print(y)

#*****************************
#Tupel ist nicht veränderbar (inmutable)
print("***************Tuppel*****************")

z = (100, 23.4, "Hallo", "Hallo")
print(z[::-1])

#Uebeschreiben von Tuppel nicht erlaubt
#z[1] = 123

#set ist nicht veränderbar (inmutable), unique , kein Index
print("***************Set*****************")
p = {100, 23.4, "Hallo", "Hallo"}
#p[0] = 123

print(p)