''' create a function that returns the nubmer of decimal places
    a number has. Any zeros after the decimal point count towards the number
    of decimal places.'''

def get_decimal_places(n):
    new_n = n.split('.')
    if len(new_n) == 2:
        new_str = new_n[1]
        return len(new_str)
    else:
        return 0


print(get_decimal_places("43.202"))
print(get_decimal_places("400"))
print(get_decimal_places("3.1"))