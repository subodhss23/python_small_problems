''' Create a function that takes two lists and insert the second
    list in the middle of the first list.'''

def tuck_in(lst1, lst2):
    lst2.insert(0, lst1[0])
    lst2.insert(len(lst2), lst1[1])
    return lst2

print(tuck_in([1, 10], [2, 3, 4, 5, 6, 7, 8, 9]))
print(tuck_in([15,150], [45, 75, 35]))
print(tuck_in([[1, 2], [5, 6]], [[3, 4]]))
