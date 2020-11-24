''' Create a function that takes a string and returns a new string with its first and last characters swapped,
    except under three conditions:
        1. If the length of the string is less than two, return "Incompatible."
        2. If the argument is not a string, return "Incompatible."
        3. If the first and last characters are the same, return "Two's a pair."'''

def flip_end_chars(txt):
    # return type(txt) != str
    if len(txt) < 2:
        return "Incompatible."
    elif type(txt) != str:
        return 'Incompatible.'
    elif txt[0] == txt[-1]:
        return "Two's a pair."
    else:
        return txt[-1]+ txt[1:-1] + txt[0]

print(flip_end_chars("Cat, dog, and mouse."))
print(flip_end_chars("ada"))
print(flip_end_chars("Ada"))
print(flip_end_chars("z") )
print(flip_end_chars([1, 2, 3]))
