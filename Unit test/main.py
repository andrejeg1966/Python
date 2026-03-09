"""
Created on 13.03.2025

@author: goran
"""

from random import randint


def add(a, b):
    return a + b


def devide(a, b):
    return a / b


# unit test testet nur die code logic. manchmal code ist abhängig von datenbamk verbindung oder Api
# Datenbankverbindung oder Server Verbindung wird nicht getestet, sondern die Funktione oder Objekten werden gemockt


def play_random():
    # die Funktion randint() muss man mocken, durch einen fixen Wert ersetzen
    num = randint(0, 10)
    if num > 5:
        return "groesser"
    else:
        return "kleiner"


# Mocken nur eine teil der Klasse
class ProductionClass:
    def method(self):
        self.something(1, 2, 3)

    # Diese Funtionen soll gemockt werden
    def something(self, a, b, c):
        pass


def print_me():
    print("hello")


def if_not_flat(data):
    return any(isinstance(i, list) for i in data)


def sum_list(data):
    return sum(data)
