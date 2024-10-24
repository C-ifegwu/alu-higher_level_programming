#!/usr/bin/python3
from magic_calculation_102 import add, sub
def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
if __name__ == "__main__":
    result1 = magic_calculation(3, 5)
    print("Result of magic_calculation(3, 5):", result1)
    result2 = magic_calculation(6, 5)
    print("Result of magic_calculation(6, 5):", result2)
