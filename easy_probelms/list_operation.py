''' create a function that takes three parameters where:
    - x is the start of the range(inclusive)
    - y is the end of the range(inclusive)
    - n is the divisor to be checked against.

    Return an ordered list with nubmers in the range that are divisible by the third parameter
    n. Return an empty list if there are no numbers that are divisible by n.'''

def list_operation(x, y, z):
    new_lst = []
    for i in range(x, y+1):
        if i % z == 0:
            new_lst.append(i)
    return new_lst


print(list_operation(1, 10, 3))
print(list_operation(7, 9, 2))
print(list_operation(15, 20, 7) )