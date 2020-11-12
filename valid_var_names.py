''' When creating variables, the variable name must always start with a letter
    and cannot contain spaces, through numbers and underscores are allowed to be 
    contained in it also.

    Create a function which returns True if a given variable name is valid,
    otherwise return False. '''

def variable_valid(var):
    if var[0].isalpha():
        if " " not in var:
            return True
    return False

print(variable_valid("result")) 
print(variable_valid("odd_nums")) 
print(variable_valid("2TimesN"))