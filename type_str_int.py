# giving variable's type

def int_to_string(var):
    if type(var) == str:
        return 'str'
    elif type(var) == int:
        return 'int'

print(int_to_string(1))
print(int_to_string("Hello"))