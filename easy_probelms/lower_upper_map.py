''' Write a function that creates a dictionary with each (key, value) pair
    being the (lower case, upper case) version of a letter, respectively.'''

def mapping(letters):
    new_obj = {}
    for i in letters:
        new_obj[i] = i.upper()
    return new_obj

print(mapping(["p", "s"]))
print(mapping(["a", "b", "c"]))
print(mapping(["a", "v", "y", "z"])