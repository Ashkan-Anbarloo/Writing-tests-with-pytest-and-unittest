def add(a , b):
    return a+b

def subtract(a , b):
    return a-b

def multiply(a , b):
    return a*b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a/b

def is_even(number):
    return number % 2 == 0

def contains_element(collection, element):
    return element in collection


