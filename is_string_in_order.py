''' Create a function that takes a string and returns True or False, depending
    on whether the characters are in order or not.'''

def is_in_order(txt):
    print(sorted(txt))
    return list(txt) == sorted(txt)

print(is_in_order('abc'))