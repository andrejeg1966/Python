'''
Created on 06.03.2025

@author: goran
'''
x =[1,2,3,4,5,6]

for item in x:
    print(x)

print("*******************")

for item in x:
    if (item == 4):
        print(item * 10)
    else:
        print(item * 2)

print("*******************")

for item in x:
    if (item == 4):
        continue
    else:
        print(item * 2)
        

print("*******************")

for item in x:
    if (item == 4):
        break
    else:
        print(item * 2)
        
print("*******************")
x =[123,24,378,42,56,61]
for index, item in enumerate(x):
    print(index, item)

print("********while schleife***********")

i = 0
while i < 3:
    print(x[i])
    i = i + 1