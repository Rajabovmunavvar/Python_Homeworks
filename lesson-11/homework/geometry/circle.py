# circle.py

def calculate_area(raduis: int) -> float:
    try:
        from math import pi
        area = pi * (raduis ** 2)
        return round(area,2)
    except TypeError:
        print("Radius must be integer !")


def calculate_circumference(raduis: int) -> float:
    try:
        from math import pi
        circumference = 2 * (pi * raduis)
        return round(circumference,2)
    except TypeError:
        print("Radius must be integer !")
