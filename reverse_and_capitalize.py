''' create a function that takes a string of lowercase character and returns
    the string reversed and in upper case. '''

def reverse_capitalize(txt):
    reversed = txt[::-1]
    return reversed.upper()

print(reverse_capitalize('abc'))
print(reverse_capitalize('hellothere'))