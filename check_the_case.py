''' create a function that return True if an input string contains only uppercase
    or only lowercase letters. '''

def same_case(txt):
    return txt.isupper() or txt.islower()


print(same_case("HELLO"))
print(same_case("HEllo"))
print(same_case("mArmALadE"))