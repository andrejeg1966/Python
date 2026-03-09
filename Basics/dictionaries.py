"""
Created on 06.03.2025

@author: goran
"""

x = {"key1": 5, "key2": 6, "key3": 30}
print(x)

print(x.keys())
print(x.items())
print(x.values())
# dictionaries sind veränderbar
x["key1"] = 20

print(x)

# konvertiere in einer liste
print(list(x.values()))

for key, value in x.items():
    print(x)
print("********************")
for key, value in x.items():
    print(key, value)
