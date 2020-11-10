''' Create a function which concantenates the number 7 
    to the end of every chords in a list. Ignore all chords 
    which already end with 7. '''

def jazzify(lst):
    new_lst = []
    for i in lst:
        if '7' not in i:
            new_lst.append(i+'7')
        else:
            new_lst.append(i)
    return new_lst

print(jazzify(["G", "F", "C"]))
print(jazzify(["Dm", "G", "E", "A"]) )
print(jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))