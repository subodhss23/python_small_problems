''' Create a function that returns the frequency distribution of a list. This
    function should return an object, where they keys are the unique elements
    and the values are the frequency in which those elements occur.'''

def get_frequencies(lst):
    new_dict = {}
    # new_dict['A'] = 2
    # return new_dict
    for i in lst:
        new_dict[i] = lst.count(i)
    return new_dict


print(get_frequencies(["A", "B", "A", "A", "A"]))
print(get_frequencies([1, 2, 3, 3, 2]))
print(get_frequencies([True, False, True, False, False]))
print(get_frequencies([]))