''' Your job is to create a function, that takes 3 number: a,b,c and returns 
    True if the last digit of a*b= the last digit of c. Check the examples 
    below for an explanation.'''

def last_dig(a,b,c):
    return str(a*b)[-1] == str(c)[-1]

print(last_dig(25, 21, 125))
print(last_dig(55, 226, 5190))
print(last_dig(12, 215, 2142))