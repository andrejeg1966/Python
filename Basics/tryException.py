#Exception nur auslösen, nicht drauf reagieren. Programm wird untebrochen
def int_squere(n: int) -> int:
    for m in range(n + 1):
        if (m * m == n):
            return m
    raise ValueError(f"{n} is not a squere number")

#Exception nur auslösen, und drauf reagieren. Program wird nicht untebrochen nach except block
def print_int_squere1(n):
    try:
        root = int_squere(n)
        print(f"Der root from {n} is {root}")
    except ValueError as err:
        print(f"Error: {err}")
        
print_int_squere1(9)
print_int_squere1(8)