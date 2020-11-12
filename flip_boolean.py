''' Create a function that reverses a boolean value and returns the string
    'boolean expected' if another variable type is given.'''

def reverse(arg):
    if type(arg) != bool:
        return 'boolean expected'
    return not bool(arg)

print(reverse(True))
print(reverse(False))
print(reverse(0))
print(reverse(None))