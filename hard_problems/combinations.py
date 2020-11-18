''' Create a function that takes a variable number of arguments, each argument representing the number
    of items in a group, and returns the number of permutations(combinations) of items that you could 
    get by taking one item from each group.'''


def combinations(*items):
    total = 1
    for i in items:
        if i != 0:
            total *= i
    return total

print(combinations(2, 3))
print(combinations(3, 7, 4))
print(combinations(2, 3, 4, 5))
print(combinations(6, 7, 0))