'''Create a function that moves all capital lettes to the front of a word.'''

def cap_to_front(s):
    upper = ''
    lower = ''
    for i in s:
        if i.isupper():
            upper+=i
        if i.islower():
            lower+=i
    return upper+lower

# def cap_to_front(s):
#     new_s = sorted(s)
#     return ''.join(new_s)

print(cap_to_front("hApPy"))
print(cap_to_front("moveMENT") )
print(cap_to_front("shOrtCAKE"))