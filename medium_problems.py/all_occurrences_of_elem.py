''' Create a function that returns the indices of all occurrences of an item in
    the list. '''

def get_indices(lst,el):
    result = []
    for i in range(len(lst)):
        if lst[i] == el:
            result.append(i)
    return result



print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
print(get_indices([1, 5, 5, 2, 7], 7))
print(get_indices([1, 5, 5, 2, 7], 5))
print(get_indices([1, 5, 5, 2, 7], 8))