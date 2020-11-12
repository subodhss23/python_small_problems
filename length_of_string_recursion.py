# write a recursive function that returns the length of a string.

def length(txt):
    if txt == '':
        return 0
    return 1 + length(txt[1:])

print(length('apple'))
print(length('make'))
print(length('a'))
print(length(''))