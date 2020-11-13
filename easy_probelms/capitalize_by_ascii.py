''' Create a function that takes a string as input and capitalizes a letter if
    its ASCII code is even and return its lower case version if it ASCII code is
    odd.'''

def ascii_capitalize(txt):
    new_txt = ''
    for i in txt:
        if ord(i) % 2 == 0:
            new_txt+= i.upper()
        elif ord(i) % 2 != 0:
            new_txt+= i.lower()
    return new_txt


print(ascii_capitalize("to be or not to be!"))
print(ascii_capitalize("THE LITTLE MERMAID"))
print(ascii_capitalize("Oh what a beautiful morning.") )