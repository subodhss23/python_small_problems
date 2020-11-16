''' Dividing y 0 is a huge mistake and should be avoided at all costs.
    Create a function that when given a math expression as a string, return Trueif at any point,
    the expresssion involves dividing by 0.'''

def catch_zero_division(expr):
    try:
        eval(expr)
    except ZeroDivisionError: 
        return True
    return False


print(catch_zero_division("2 / 0"))
print(catch_zero_division("4 / (2 + 3 - 5)"))
print(catch_zero_division("2 * 5 - 10") )

