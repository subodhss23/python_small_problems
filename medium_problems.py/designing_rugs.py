''' Write a function that accepts the width and height(m,n) and an optional proc s and generates a 
    list with m elements. Each element is a string consisting of either:
    - The default character (hash #) repeating n time (if no proc is given).
    - The character passed in through the proc repeating n times.
'''

def make_rug(m, n, s='#'):
    new_lst = []
    for i in range(m):
        new_lst.append(n*s)
    return new_lst

print(make_rug(3, 5))
print(make_rug(3, 5, '$'))
print(make_rug(2, 2, 'A'))
