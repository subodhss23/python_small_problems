''' Create a fucntion that takes a string road and returns the car that/'s in first place. The road will 
    be madeof "=", and cars will be represented by letters in the alphabet.'''


def first_place(road):        
    for i in reversed(road):
        if i.isalpha():
            return i
    return i



print(first_place("====b===O===e===U=A=="))
print(first_place("e==B=Fe"))
print(first_place("proeNeoOJGnfl"))
