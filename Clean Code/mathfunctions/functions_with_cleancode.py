import numpy as np
import pandas as pd

Vector = "list[float]"


def my_add(a: int, b: int) -> int:
    """adds two integers and returns a new integer

    Parameters
    ----------
    a : int
        first integer
    b : int
        second integer

    Returns
    -------
    int
        integer
    """
    return a + b


def my_multiply(a: int, b: int) -> int:
    """multiplay two integers and returns a new integer

    Parameters
    ----------
    a : int
        first integer
    b : int
        second integer

    Returns
    -------
    int
        integer
    """
    return a * b


def my_scale(scalar: float, vector: Vector) -> Vector:
    """muptiplay list with a scalar and return a new list

    Parameters
    ----------
    scalar : float
        scalar
    vector : Vector
        list

    Returns
    -------
    Vector
        list
    """
    return [scalar * num for num in vector]


def lists_to_df(list1: Vector, list2: Vector) -> pd.DataFrame:
    """return data frame

    Parameters
    ----------
    list1 : Vector
        list
    list2 : Vector
        list

    Returns
    -------
    pd.DataFrame
        data frame
    """
    x = np.array([list1, list2])
    df = pd.DataFrame(data=x, index=["row1", "row2"], columns=["column1", "column2"])
    return df