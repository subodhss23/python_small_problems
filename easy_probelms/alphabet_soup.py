''' Create a function that takes a string and returns a string with its
    letters in alphabetical order.'''

def alphabet_soup(txt):
    new_lst = sorted(txt)
    return ''.join(new_lst)

print(alphabet_soup('what'))