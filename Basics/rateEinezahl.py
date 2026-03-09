"""
Created on 06.03.2025

@author: goran
"""

from random import randint

min_x = 0
max_x = 10
x = randint(min_x, max_x)

max_try = 3
i = 1
while True:
    guess = int(input(f"rate eine Zwhl zwischen: {min_x} und {max_x}"))
    if guess == x:
        print("nummer is korrekt")
        break
    elif guess > x:
        print(f"nummer zu groß: Versuch {i} von {max_try}")
    else:
        print(f"nummer zu klein: Versuch {i} von {max_try}")
    if i == max_try:
        print("Verloren, alle versuche aufgebraucht")
        break
    else:
        i += 1
