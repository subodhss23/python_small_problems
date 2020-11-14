''' Create a function that takes a single word string and does the following:

    1. Concatenates 'inator' to the end if the word ends with c consonant,
        otherwise, concatente -inator instead.

    2. Adds the word leneth of the original word to the end, supplies with '000'.
'''

def inator_inator(inv):
    if inv[-1].lower() in 'aeiou':
        return inv + "-inator " + str(len(inv)) + "000"
    else:
        return inv + "inator " + str(len(inv)) + "000"
    

print(inator_inator("Shrink"))
print(inator_inator("Doom"))
print(inator_inator("EvilClone"))

