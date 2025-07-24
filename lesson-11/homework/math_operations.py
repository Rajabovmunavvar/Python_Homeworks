
# math_operations.py

def add(num_1: int, num_2: int):
    try:
        result = num_1 + num_2
        return result
    except TypeError:
        print("Numbers must be integer !!")

def substract(num_1: int, num_2: int):
    try:
        result = num_1 - num_2
        return result
    except TypeError:
        print("Numbers must be integer !!")

def multiply(num_1: int, num_2: int):
    try:
        result = num_1 * num_2
        return result
    except TypeError:
        print("Numbers must be integer !!")

def devide(num_1: int, num_2: int):
    try:
        result = num_1 / num_2
        return result
    except TypeError:
        print("Numbers must be integer !!")

