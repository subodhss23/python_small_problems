''' A repdigit is a positive number composed out of the same digit. Create a function that takes an
    integer and returns whether it's a repdigit or not.

    Notes:-
        - The nubmer 0 should return True(even though it's not a positive number).
'''
def is_repdigit(num):
    if num < 0:
        return False
    elif num == 0:
        return True
    else:
        new_str = str(num)
        return len(set(new_str)) == 1

print(is_repdigit(66))
print(is_repdigit(0))
print(is_repdigit(-11))