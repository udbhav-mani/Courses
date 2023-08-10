from typing import Union

def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Divisor cant be zero!! ")
    return float(dividend / divisor)

def multiply(*args: Union[int, float]):
    if len(args) == 0:
        raise ValueError("Atleast one value needed!! ")
    
    total = 1
    for arg in args:
        total *= arg

    return total

