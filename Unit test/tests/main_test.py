"""
Created on 13.03.2025

@author: goran
"""

from unittest import mock

# zum Ausführen von pytest in cmd oder PowerShell:
# 1. In Cmd Befehl: pip install pytest
# 2. Befehl am Anfang ausführen: python -m pytest
# 3. Für jedes weitere Testausführung, Befehl: pytest
import pytest
from _pytest.capture import capsys
from main import (
    ProductionClass,
    add,
    devide,
    if_not_flat,
    play_random,
    print_me,
    sum_list,
)


def test_add():
    result = add(2, 3)
    assert result == 5


@pytest.mark.parametrize("input1, input2, expected", [(1, 2, 3), (2, 3, 5), (5, 6, 11)])
def test_add_par(input1, input2, expected):
    resultPar = add(input1, input2)
    assert resultPar == expected


def test_devide():
    result = devide(8, 4)
    assert result == 2
    with pytest.raises(ZeroDivisionError):
        10 / 0


# die Funktion randint() muss man mocken, durch einen fixen Wert ersetzen (in diesem Fall, return Value ist 7)
@mock.patch("main.randint", return_value=7)
def test_play_random(mocked_randint):
    result = play_random()
    assert result == "groesser"


def test_productionclass():
    instanz = ProductionClass()
    # Mocken die Funktion something
    instanz.something = mock.MagicMock()
    # die Parent Funtion aufrufen
    instanz.method()
    # Prüfen ob die Funtion something() mit richtigen Parameter aufgerufen wurde
    instanz.something.assert_called_once_with(1, 2, 3)


# Fixture zum testen von std out
def test_print_me(capsys):
    print_me()
    captures = capsys.readouterr()
    assert captures.out == "hello\n"


# parameter my_data ist fixture (list) aus file conftest.py
def test_if_not_flat(my_data):
    assert if_not_flat(my_data) == False


def test_sum_list(my_data):
    assert sum_list(my_data) == 10
