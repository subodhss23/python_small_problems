''' The "Reverser" takes a string as input and returns that string in reverse order, with the 
    opposite case.'''

def reverse(txt):
    return txt[::-1].swapcase()

print(reverse('Hello, World.'))