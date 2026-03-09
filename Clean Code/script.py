
#Code in script.py ist kein gute Python code

import numpy as np
import pandas as pd


def x(a, b):
    return a + b


def y(a, b):
    return a * b


def z(a, b):
    return [a * x for x in b]


def u(a, b):
    x = np.array([a, b])
    df = pd.DataFrame(data=x, index=["row1", "row2"], columns=["column1", "column2"])
    return df


print(2, 3)
print(10, 5)
print(2.3, [1, 2, 3, 4, 5])
print(u([1, 2], [2, 3]))
