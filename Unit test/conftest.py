"""
Created on 13.03.2025

@author: goran
"""

import pytest


# erstellen eigene Fixture
@pytest.fixture()
def my_data():
    return [1, 2, 3, 4]
