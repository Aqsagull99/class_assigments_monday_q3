# Custom exception
class NegativeNumberError(Exception):
    pass

def sqrt_positive(x):
    if x < 0:
        raise NegativeNumberError("Number cannot be negative")
    return x ** 0.5

try:
    print(sqrt_positive(-4))
except NegativeNumberError as e:
    print(e)