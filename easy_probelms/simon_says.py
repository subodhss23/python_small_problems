''' Create a function that takes in two lists and return True if the second list
    follows the first list by one element, and False otherwise. In other words,
    determine if the second list is the first list shifted to right by 1. '''

def simon_says(lst1, lst2):
    new_lst1 = lst1[:-1]
    new_lst2 = lst2[1:]
    return new_lst1 == new_lst2

print(simon_says([1, 2], [5, 1]))
print(simon_says([1, 2], [5, 5]))
print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))
print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) )