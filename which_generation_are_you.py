''' Try finding your ancestors and offspring with code.

    Create a function that takes a number x and a character y ("m" for male, "f"
    for female), and returns the name of an ancestor (m/f) or descendant (m/f).
        - If the nubmer is negative, return the related ancestor.
        - If positive, return the related descendant.
        - You are generation 0. In the case of 0 (male or female), return "me!".
'''

def generation(x, y):
    if x > 0:
        if y == 'm':
            if x == 1:
                return 'son'
            elif x == 2:
                return 'grandson'
            elif x == 3:
                return 'great grandson'
        elif y == 'f':
            if x == 1:
                return 'daughter'
            elif x == 2:
                return 'granddaughter'
            elif x == 3:
                return 'great granddaughter'
    elif x < 0:
        if y == "m":
            if x == -1:
                return 'father'
            elif x == -2:
                return 'grandfather'
            elif x == -3:
                return 'great grandfather'
        elif y == 'f':
            if x == -1:
                return 'mother'
            elif x == -2:
                return 'grandmother'
            elif x == -3:
                return 'great grandmother'
    elif x == 0:
        return 'me!'


print(generation(2, 'f'))
print(generation(-3, "m"))
print(generation(1, "f"))