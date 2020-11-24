''' Create a function that takes a division equation d and checks if ti will return a whole number
    without decimals after dividing.'''

def valid_division(d):
    try:
        if eval(d) == int(eval(d)):
            return True
        return False
    except ZeroDivisionError:
        return 'invalid'

print(valid_division("6/3"))
print(valid_division("30/25"))
print(valid_division("0/3"))
print(valid_division('10/0'))