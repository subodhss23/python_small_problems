# create a functiont hat sorts a list and removes all duplicate items from it.

def setify(lst):
    new_set = set(lst)
    new_lst = []
    new_lst = list(new_set)
    return sorted(new_lst)

print(setify([1, 3, 3, 5, 5]))
print(setify([4, 4, 4, 4]))
print(setify([5, 7, 8, 9, 10, 15]))
print(setify([3, 3, 3, 2, 1]))
print(setify([5, 9, 9]))