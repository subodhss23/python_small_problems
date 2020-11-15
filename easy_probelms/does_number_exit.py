''' Create a function which validates whether a given number exists, and could 
    represent a real life quality. Inputs will be given as a string.'''

def valid_str_number(n):
    try: float(n)
    except: return False
    return True


print(valid_str_number("3.2"))
print(valid_str_number("324"))
print(valid_str_number("54..4"))
print(valid_str_number("number"))